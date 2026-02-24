"""OpenAPI spec adapter — produces in-memory schemas dict and operations list.

Supports OpenAPI 3.x and Swagger 2.0. Returns plain dicts; no file I/O.
"""

from __future__ import annotations

import re
from typing import Any

from schmith.shared.hashing import canonical_json_hash
from schmith.shared.provenance import Provenance
from schmith.shared.schema_ids import schema_id_for_schema, schema_id_from_ref

HTTP_METHODS = {"get", "post", "put", "patch", "delete", "head", "options"}


def _title_to_pascal_case(title: str) -> str:
    """Convert a schema title to a valid PascalCase C# identifier.

    Handles three cases:
    - Multi-word with separators: "Company User" → "CompanyUser"
    - Already a single PascalCase/camelCase token: "TimecardTimeType" → "TimecardTimeType"
    - Single lowercase word: "timesheets" → "Timesheets"
    """
    title = title.strip()
    if not title:
        return title
    if re.search(r"[\s\-_]", title):
        parts = re.split(r"[\s\-_]+", title)
        return "".join(p.capitalize() for p in parts if p)
    # Single token — preserve internal capitalisation, just ensure first char is upper
    return title[0].upper() + title[1:]


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _collapse_single_ref_schema(schema: dict) -> str | None:
    """Return $ref target if schema is a pure single-ref allOf wrapper."""
    if not isinstance(schema, dict):
        return None
    all_of = schema.get("allOf")
    if not isinstance(all_of, list) or len(all_of) != 1:
        return None
    entry = all_of[0]
    if not isinstance(entry, dict):
        return None
    ref = entry.get("$ref")
    if not isinstance(ref, str):
        return None
    allowed_keys = {
        "allOf", "title", "description", "readOnly",
        "deprecated", "nullable", "example", "examples", "default",
    }
    for key in schema.keys():
        if key in allowed_keys or key.startswith("x-"):
            continue
        return None
    return ref


def resolve_ref(spec: dict[str, Any], ref: str) -> dict[str, Any] | None:
    """Resolve a JSON reference within the spec."""
    if not ref.startswith("#/"):
        return None
    node: Any = spec
    for part in ref.lstrip("#/").split("/"):
        if not isinstance(node, dict):
            return None
        node = node.get(part)
        if node is None:
            return None
    return node if isinstance(node, dict) else None


def detect_nullable(schema: dict[str, Any]) -> bool | None:
    if "nullable" in schema:
        return bool(schema.get("nullable"))
    type_value = schema.get("type")
    if isinstance(type_value, list):
        return "null" in type_value
    return None


def extract_constraints(schema: dict[str, Any]) -> dict[str, Any]:
    constraints = {}
    for key in (
        "minLength", "maxLength", "pattern", "minimum", "maximum",
        "minItems", "maxItems", "uniqueItems", "enum", "const",
    ):
        if key in schema:
            constraints[key] = schema[key]
    return constraints


def extract_composition(schema: dict[str, Any]) -> dict[str, Any] | None:
    for key in ("oneOf", "anyOf", "allOf"):
        if key in schema and isinstance(schema.get(key), list):
            members = []
            for entry in schema.get(key) or []:
                if isinstance(entry, dict) and "$ref" in entry:
                    members.append(schema_id_from_ref(entry["$ref"]))
                elif isinstance(entry, dict):
                    members.append(schema_id_for_schema(entry))
            return {"kind": key, "members": [m for m in members if m]}
    return None


def _build_field(
    name: str,
    schema_id: str | None,
    required: bool,
    field_schema: dict[str, Any],
    pointer: str,
    provenance: Provenance,
) -> dict[str, Any]:
    enum_values = field_schema.get("enum") if isinstance(field_schema.get("enum"), list) else None
    enum_names = field_schema.get("x-enumNames") if isinstance(field_schema.get("x-enumNames"), list) else None
    return {
        "json_name": name,
        "schema_id": schema_id,
        "required": required,
        "nullable": detect_nullable(field_schema),
        "description": field_schema.get("description"),
        "deprecated": field_schema.get("deprecated"),
        "read_only": field_schema.get("readOnly"),
        "write_only": field_schema.get("writeOnly"),
        "examples": field_schema.get("examples"),
        "constraints": extract_constraints(field_schema),
        "enum_values": enum_values,
        "enum_names": enum_names,
        "json_pointer": pointer,
        "provenance": provenance.__dict__,
    }


def _register_schema(
    schema_id: str,
    name_hint: str | None,
    schema: dict[str, Any],
    is_inline: bool,
    provenance: Provenance,
    schemas: dict[str, dict],
    schema_hashes: dict[str, str],
    register_nested: bool = True,
) -> None:
    if schema_id in schemas:
        return
    if schema_id.startswith("schema:anon/"):
        content_hash = schema_id.split("/")[-1]
        if content_hash in schema_hashes:
            return
        schema_hashes[content_hash] = schema_id

    # Use schema title as name_hint when no explicit name is provided.
    # Many OpenAPI specs (e.g. Procore) use "title" on inline object schemas
    # rather than $ref names; this surfaces those names during type traversal.
    # _title_to_pascal_case handles multi-word ("Company User" → "CompanyUser")
    # and already-PascalCase titles ("TimecardTimeType" → "TimecardTimeType").
    if name_hint is None:
        title = schema.get("title")
        if isinstance(title, str) and title.strip():
            name_hint = _title_to_pascal_case(title)

    kind = schema.get("type") or "unknown"
    if isinstance(kind, list):
        kind = next((k for k in kind if k != "null"), "unknown")

    required_raw = schema.get("required")
    required_fields: list[str] = required_raw if isinstance(required_raw, list) else []

    properties = []
    props = schema.get("properties")
    if isinstance(props, dict):
        for prop_name, prop_schema in props.items():
            if not isinstance(prop_schema, dict):
                continue
            prop_ref = prop_schema.get("$ref") or _collapse_single_ref_schema(prop_schema)
            prop_schema_id = schema_id_from_ref(prop_ref) if isinstance(prop_ref, str) else schema_id_for_schema(prop_schema)
            properties.append(
                _build_field(prop_name, prop_schema_id, prop_name in required_fields,
                             prop_schema, f"$.{prop_name}", provenance)
            )
            if register_nested and "$ref" not in prop_schema and not _collapse_single_ref_schema(prop_schema):
                nested_id = schema_id_for_schema(prop_schema)
                if nested_id:
                    _register_schema(nested_id, None, prop_schema, True, provenance, schemas, schema_hashes)

    items_schema_id = None
    if kind == "array":
        items = schema.get("items") if isinstance(schema.get("items"), dict) else None
        if isinstance(items, dict):
            items_ref = items.get("$ref") or _collapse_single_ref_schema(items)
            items_schema_id = schema_id_from_ref(items_ref) if isinstance(items_ref, str) else schema_id_for_schema(items)
            if register_nested and items_schema_id and "$ref" not in items and not _collapse_single_ref_schema(items):
                _register_schema(items_schema_id, None, items, True, provenance, schemas, schema_hashes)

    additional_properties_schema_id = None
    additional_props = schema.get("additionalProperties")
    if isinstance(additional_props, dict):
        addl_ref = additional_props.get("$ref") or _collapse_single_ref_schema(additional_props)
        additional_properties_schema_id = (
            schema_id_from_ref(addl_ref) if isinstance(addl_ref, str)
            else schema_id_for_schema(additional_props)
        )
        if register_nested and additional_properties_schema_id and "$ref" not in additional_props:
            _register_schema(additional_properties_schema_id, None, additional_props, True, provenance, schemas, schema_hashes)

    composition = extract_composition(schema)
    if register_nested and composition:
        for key in ("oneOf", "anyOf", "allOf"):
            for entry in schema.get(key) or []:
                if isinstance(entry, dict) and "$ref" not in entry:
                    member_id = schema_id_for_schema(entry)
                    if member_id:
                        _register_schema(member_id, None, entry, True, provenance, schemas, schema_hashes)

    schemas[schema_id] = {
        "id": schema_id,
        "name_hint": name_hint,
        "kind": kind or "unknown",
        "title": schema.get("title"),
        "description": schema.get("description"),
        "enum_values": schema.get("enum") if isinstance(schema.get("enum"), list) else None,
        "enum_names": schema.get("x-enumNames") if isinstance(schema.get("x-enumNames"), list) else None,
        "properties": properties,
        "required": list(required_fields),
        "items_schema_id": items_schema_id,
        "additional_properties_schema_id": additional_properties_schema_id,
        "constraints": extract_constraints(schema),
        "composition": composition,
        "provenance": provenance.__dict__,
        "is_inline": is_inline,
    }

    if not is_inline:
        content_hash = canonical_json_hash(schema)
        schema_hashes[content_hash] = schema_id


def _operation_id(method: str, path_template: str) -> str:
    return f"op:{method.upper()}:{path_template}"


def _resolve_parameter(spec: dict, param: Any) -> dict | None:
    if not isinstance(param, dict):
        return None
    if "$ref" in param and isinstance(param.get("$ref"), str):
        resolved = resolve_ref(spec, param["$ref"])
        if resolved is None:
            return None
        param = resolved
    return param if isinstance(param, dict) else None


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def extract_schemas(spec: dict[str, Any], spec_path: str) -> dict[str, dict]:
    """Extract all schemas from an OpenAPI/Swagger spec into a flat dict.

    Args:
        spec: Parsed OpenAPI specification.
        spec_path: Path to the source spec file (for provenance).

    Returns:
        Dict mapping schema_id -> schema record.
    """
    schemas: dict[str, dict] = {}
    schema_hashes: dict[str, str] = {}
    is_swagger2 = spec.get("swagger") == "2.0"

    # Named component schemas
    if is_swagger2:
        definitions = spec.get("definitions")
        if isinstance(definitions, dict):
            for name, schema in definitions.items():
                if not isinstance(schema, dict):
                    continue
                sid = f"schema:definitions/{name}"
                prov = Provenance(spec_path, f"#/definitions/{name}")
                _register_schema(sid, name, schema, False, prov, schemas, schema_hashes)
    else:
        comp_schemas = (spec.get("components") or {}).get("schemas")
        if isinstance(comp_schemas, dict):
            for name, schema in comp_schemas.items():
                if not isinstance(schema, dict):
                    continue
                sid = f"schema:components/{name}"
                prov = Provenance(spec_path, f"#/components/schemas/{name}")
                _register_schema(sid, name, schema, False, prov, schemas, schema_hashes)

    # Inline schemas from operations
    paths = spec.get("paths")
    if isinstance(paths, dict):
        for path_template, path_item in paths.items():
            if not isinstance(path_item, dict):
                continue
            for method, operation in path_item.items():
                if not isinstance(method, str) or method.lower() not in HTTP_METHODS:
                    continue
                if not isinstance(operation, dict):
                    continue

                if is_swagger2:
                    for idx, param in enumerate(operation.get("parameters") or []):
                        if not isinstance(param, dict) or param.get("in") != "body":
                            continue
                        schema = param.get("schema")
                        if isinstance(schema, dict):
                            sid = schema_id_for_schema(schema)
                            if sid:
                                prov = Provenance(spec_path, f"#/paths/{path_template}/{method}/parameters/{idx}")
                                _register_schema(sid, None, schema, True, prov, schemas, schema_hashes)
                else:
                    content = (operation.get("requestBody") or {}).get("content")
                    if isinstance(content, dict):
                        for media_type, media in content.items():
                            if isinstance(media, dict):
                                schema = media.get("schema")
                                if isinstance(schema, dict):
                                    sid = schema_id_for_schema(schema)
                                    if sid:
                                        prov = Provenance(spec_path, f"#/paths/{path_template}/{method}/requestBody/content/{media_type}")
                                        _register_schema(sid, None, schema, True, prov, schemas, schema_hashes)

                responses = operation.get("responses")
                if not isinstance(responses, dict):
                    continue
                for status, response in responses.items():
                    if not isinstance(response, dict):
                        continue
                    status_str = str(status)
                    if is_swagger2:
                        schema = response.get("schema")
                        if isinstance(schema, dict):
                            sid = schema_id_for_schema(schema)
                            if sid:
                                prov = Provenance(spec_path, f"#/paths/{path_template}/{method}/responses/{status_str}")
                                _register_schema(sid, None, schema, True, prov, schemas, schema_hashes)
                    else:
                        content = response.get("content")
                        if isinstance(content, dict):
                            for media_type, media in content.items():
                                if isinstance(media, dict):
                                    schema = media.get("schema")
                                    if isinstance(schema, dict):
                                        sid = schema_id_for_schema(schema)
                                        if sid:
                                            prov = Provenance(spec_path, f"#/paths/{path_template}/{method}/responses/{status_str}/content/{media_type}")
                                            _register_schema(sid, None, schema, True, prov, schemas, schema_hashes)

    return schemas


def extract_operations(spec: dict[str, Any], spec_path: str) -> list[dict]:
    """Extract all operations from an OpenAPI/Swagger spec.

    Args:
        spec: Parsed OpenAPI specification.
        spec_path: Path to the source spec file (for provenance).

    Returns:
        List of operation dicts.
    """
    operations: list[dict] = []
    paths = spec.get("paths")
    if not isinstance(paths, dict):
        return operations

    is_swagger2 = spec.get("swagger") == "2.0"

    for path_template, path_item in paths.items():
        if not isinstance(path_item, dict):
            continue
        path_params = path_item.get("parameters") or []

        for method, operation in path_item.items():
            if not isinstance(method, str) or method.lower() not in HTTP_METHODS:
                continue
            if not isinstance(operation, dict):
                continue

            op_id = _operation_id(method, path_template)
            op_params = operation.get("parameters") or []

            parameters = []
            for param in list(op_params) + list(path_params):
                resolved = _resolve_parameter(spec, param)
                if not resolved:
                    continue
                schema = resolved.get("schema")
                parameters.append({
                    "name": resolved.get("name"),
                    "location": resolved.get("in"),
                    "required": resolved.get("required"),
                    "schema_id": schema_id_for_schema(schema) if schema else None,
                    "description": resolved.get("description"),
                    "deprecated": resolved.get("deprecated"),
                    "provenance": Provenance(spec_path, f"#/paths/{path_template}/{method}/parameters").__dict__,
                })

            bodies: list[dict] = []
            request_body = operation.get("requestBody")
            if isinstance(request_body, dict):
                content = request_body.get("content")
                if isinstance(content, dict):
                    for media_type, media in content.items():
                        bodies.append({
                            "media_type": media_type,
                            "schema_id": schema_id_for_schema(media.get("schema")) if isinstance(media, dict) else None,
                            "required": request_body.get("required"),
                            "description": request_body.get("description"),
                            "provenance": Provenance(spec_path, f"#/paths/{path_template}/{method}/requestBody").__dict__,
                        })

            if is_swagger2:
                for param in op_params:
                    resolved = _resolve_parameter(spec, param)
                    if resolved and resolved.get("in") == "body":
                        schema = resolved.get("schema")
                        bodies.append({
                            "media_type": None,
                            "schema_id": schema_id_for_schema(schema) if schema else None,
                            "required": resolved.get("required"),
                            "description": resolved.get("description"),
                            "provenance": Provenance(spec_path, f"#/paths/{path_template}/{method}/parameters").__dict__,
                        })
                        break

            responses: list[dict] = []
            responses_obj = operation.get("responses")
            if isinstance(responses_obj, dict):
                for status_code, response in responses_obj.items():
                    if not isinstance(response, dict):
                        continue
                    status_str = str(status_code)
                    if is_swagger2:
                        schema = response.get("schema")
                        responses.append({
                            "status_code": status_str,
                            "media_type": None,
                            "schema_id": schema_id_for_schema(schema) if schema else None,
                            "description": response.get("description"),
                            "provenance": Provenance(spec_path, f"#/paths/{path_template}/{method}/responses/{status_str}").__dict__,
                        })
                    else:
                        content = response.get("content")
                        if isinstance(content, dict):
                            for media_type, media in content.items():
                                responses.append({
                                    "status_code": status_str,
                                    "media_type": media_type,
                                    "schema_id": schema_id_for_schema(media.get("schema")) if isinstance(media, dict) else None,
                                    "description": response.get("description"),
                                    "provenance": Provenance(spec_path, f"#/paths/{path_template}/{method}/responses/{status_str}/content/{media_type}").__dict__,
                                })
                        else:
                            responses.append({
                                "status_code": status_str,
                                "media_type": None,
                                "schema_id": None,
                                "description": response.get("description"),
                                "provenance": Provenance(spec_path, f"#/paths/{path_template}/{method}/responses/{status_str}").__dict__,
                            })

            operations.append({
                "id": op_id,
                "method": method.upper(),
                "path_template": path_template,
                "parameters": parameters,
                "request_bodies": bodies,
                "responses": responses,
                "tags": operation.get("tags") or [],
                "summary": operation.get("summary"),
                "description": operation.get("description"),
                "provenance": Provenance(spec_path, f"#/paths/{path_template}/{method}").__dict__,
            })

    return operations
