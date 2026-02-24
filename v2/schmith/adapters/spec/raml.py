"""RAML spec adapter — produces in-memory schemas dict and operations list.

Consolidates legacy raml/schemas.py and raml/operations.py into one module.
Returns plain dicts; no file I/O.
"""

from __future__ import annotations

from typing import Any, Iterable

from schmith.shared.hashing import canonical_json_hash
from schmith.shared.provenance import Provenance

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

RAML_BODY_STRUCTURE_FIELDS = {"properties", "items", "additionalProperties", "facets"}
RAML_BODY_EXCLUDE_FIELDS = {"name", "displayName", "examples", "example", "key"}
RAML_PRIMITIVE_TYPES = {"object", "array", "string", "number", "integer", "boolean", "null"}

# ---------------------------------------------------------------------------
# Schema ID helpers
# ---------------------------------------------------------------------------


def _normalize_schema_content(schema: dict[str, Any]) -> dict[str, Any]:
    return {k: v for k, v in schema.items() if k not in RAML_BODY_EXCLUDE_FIELDS}


def _structural_fingerprint(schema: dict[str, Any]) -> dict[str, Any]:
    kind = schema.get("type")
    if kind == "object":
        if isinstance(schema.get("properties"), list):
            return {"type": "object", "properties": schema.get("properties")}
        if isinstance(schema.get("additionalProperties"), dict):
            return {"type": "object", "additionalProperties": schema.get("additionalProperties")}
        return {"type": "object"}
    if kind == "array":
        return {"type": "array", "items": schema.get("items")}
    if kind:
        return {"type": kind, "constraints": _extract_constraints(schema)}
    return _normalize_schema_content(schema)


def schema_id_for_raml_type(type_decl: Any, allow_name_field: bool = True) -> str | None:
    if isinstance(type_decl, str):
        return f"schema:types/{type_decl}"
    if isinstance(type_decl, dict):
        type_value = type_decl.get("type")
        if isinstance(type_value, str) and not any(type_decl.get(f) for f in RAML_BODY_STRUCTURE_FIELDS):
            return f"schema:types/{type_value}"
        if allow_name_field:
            name = type_decl.get("name")
            if isinstance(name, str):
                return f"schema:types/{name}"
        return f"schema:anon/{canonical_json_hash(type_decl)}"
    return None


def _schema_id_for_body(body: dict[str, Any]) -> str | None:
    """Generate schema ID for a RAML request/response body."""
    has_structure = any(body.get(f) for f in RAML_BODY_STRUCTURE_FIELDS)
    if has_structure:
        schema_content = _normalize_schema_content(body)
        return f"schema:anon/{canonical_json_hash(_structural_fingerprint(schema_content))}"
    body_type = body.get("type")
    if isinstance(body_type, str):
        return f"schema:types/{body_type}"
    if isinstance(body_type, dict):
        return schema_id_for_raml_type(body_type)
    return None


def _inline_name_hint(schema: dict[str, Any]) -> str | None:
    name = schema.get("name")
    if isinstance(name, str) and name:
        return name
    display = schema.get("displayName")
    if isinstance(display, str) and display:
        return display
    return None


# ---------------------------------------------------------------------------
# Schema field/constraint helpers
# ---------------------------------------------------------------------------


def _detect_nullable(schema: dict[str, Any]) -> bool | None:
    if "nullable" in schema:
        return bool(schema.get("nullable"))
    type_value = schema.get("type")
    if isinstance(type_value, list):
        return "null" in type_value
    return None


def _extract_constraints(schema: dict[str, Any]) -> dict[str, Any]:
    constraints = {}
    for key in ("minLength", "maxLength", "pattern", "minimum", "maximum",
                "minItems", "maxItems", "uniqueItems", "enum", "const"):
        if key in schema:
            constraints[key] = schema[key]
    return constraints


def _build_field(
    name: str,
    schema_id: str | None,
    required: bool,
    field_schema: dict[str, Any],
    pointer: str,
    provenance: Provenance,
    items_schema_id: str | None = None,
) -> dict[str, Any]:
    return {
        "json_name": name,
        "schema_id": schema_id,
        "required": required,
        "nullable": _detect_nullable(field_schema),
        "description": field_schema.get("description"),
        "deprecated": field_schema.get("deprecated"),
        "read_only": field_schema.get("readOnly"),
        "write_only": field_schema.get("writeOnly"),
        "examples": field_schema.get("examples"),
        "constraints": _extract_constraints(field_schema),
        "json_pointer": pointer,
        "items_schema_id": items_schema_id,
        "provenance": provenance.__dict__,
    }


# ---------------------------------------------------------------------------
# Resource walking (shared by schemas + operations)
# ---------------------------------------------------------------------------


def walk_resources(node: Any, base_path: str) -> Iterable[dict[str, Any]]:
    if isinstance(node, list):
        for item in node:
            yield from walk_resources(item, base_path)
        return
    if isinstance(node, dict):
        rel = node.get("relativeUri", "")
        path = f"{base_path}{rel}" if rel else base_path
        methods = node.get("methods") if isinstance(node.get("methods"), list) else []
        for method in methods:
            if isinstance(method, dict):
                yield {"path": path, "method": method}
        children = node.get("resources") if isinstance(node.get("resources"), list) else []
        for child in children:
            yield from walk_resources(child, path)


# ---------------------------------------------------------------------------
# Schema registration
# ---------------------------------------------------------------------------


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

    if not name_hint and is_inline:
        name_hint = _inline_name_hint(schema)

    if schema_id.startswith("schema:anon/"):
        content_hash = schema_id.split("/")[-1]
        if content_hash in schema_hashes:
            return
        schema_hashes[content_hash] = schema_id

    kind = schema.get("type") or "unknown"
    if isinstance(kind, list):
        kind = next((k for k in kind if k != "null"), "unknown")

    required_raw = schema.get("required")
    required_fields: list[str] = required_raw if isinstance(required_raw, list) else []

    properties = []
    props = schema.get("properties")
    if isinstance(props, list):
        required_fields = []
        for prop in props:
            if not isinstance(prop, dict):
                continue
            prop_name = prop.get("name")
            if not isinstance(prop_name, str):
                continue
            prop_required = bool(prop.get("required")) if prop.get("required") is not None else False
            if prop_required:
                required_fields.append(prop_name)
            prop_type = prop.get("type")
            prop_schema_id = schema_id_for_raml_type(prop_type)

            if prop_type == "object" and isinstance(prop.get("properties"), list):
                schema_content = _normalize_schema_content(prop)
                content_hash = canonical_json_hash(_structural_fingerprint(schema_content))
                if content_hash in schema_hashes:
                    prop_schema_id = schema_hashes[content_hash]
                else:
                    prop_schema_id = f"schema:anon/{content_hash}"
                    if register_nested:
                        _register_schema(prop_schema_id, _inline_name_hint(prop), schema_content,
                                         True, provenance, schemas, schema_hashes)

            prop_items_schema_id = None
            if prop_type == "array":
                items = prop.get("items")
                if isinstance(items, dict):
                    items_hash = canonical_json_hash(
                        _structural_fingerprint(_normalize_schema_content(items))
                    )
                    if items_hash in schema_hashes:
                        prop_items_schema_id = schema_hashes[items_hash]
                    else:
                        prop_items_schema_id = schema_id_for_raml_type(items, allow_name_field=False)

            properties.append(
                _build_field(prop_name, prop_schema_id, prop_required, prop,
                             f"$.{prop_name}", provenance, prop_items_schema_id)
            )

            if register_nested:
                if isinstance(prop_type, dict):
                    nested_id = schema_id_for_raml_type(prop_type, allow_name_field=False)
                    if nested_id:
                        _register_schema(nested_id, None, prop_type, True, provenance, schemas, schema_hashes)
                elif prop_type == "array":
                    items = prop.get("items")
                    if isinstance(items, dict):
                        items_id = schema_id_for_raml_type(items, allow_name_field=False)
                        if items_id:
                            _register_schema(items_id, _inline_name_hint(items), items, True,
                                             provenance, schemas, schema_hashes)

    items_schema_id = None
    if kind == "array":
        items = schema.get("items") if isinstance(schema.get("items"), dict) else None
        if isinstance(items, dict):
            items_schema_id = schema_id_for_raml_type(items, allow_name_field=False)
            if register_nested and items_schema_id:
                _register_schema(items_schema_id, _inline_name_hint(items), items, True,
                                 provenance, schemas, schema_hashes)

    additional_properties_schema_id = None
    additional_props = schema.get("additionalProperties")
    if isinstance(additional_props, dict):
        additional_properties_schema_id = schema_id_for_raml_type(additional_props, allow_name_field=False)
        if register_nested and additional_properties_schema_id:
            _register_schema(additional_properties_schema_id, _inline_name_hint(additional_props),
                             additional_props, True, provenance, schemas, schema_hashes)

    schemas[schema_id] = {
        "id": schema_id,
        "name_hint": name_hint,
        "kind": kind or "unknown",
        "title": schema.get("title"),
        "description": schema.get("description"),
        "properties": properties,
        "required": list(required_fields),
        "items_schema_id": items_schema_id,
        "additional_properties_schema_id": additional_properties_schema_id,
        "constraints": _extract_constraints(schema),
        "composition": None,
        "provenance": provenance.__dict__,
        "is_inline": is_inline,
    }

    if not is_inline:
        content_hash = canonical_json_hash(schema)
        schema_hashes[content_hash] = schema_id


def _register_nested_schemas(
    schema: dict[str, Any],
    provenance: Provenance,
    schemas: dict[str, dict],
    schema_hashes: dict[str, str],
) -> None:
    props = schema.get("properties")
    if isinstance(props, list):
        for prop in props:
            if not isinstance(prop, dict):
                continue
            prop_type = prop.get("type")
            if prop_type == "object" and isinstance(prop.get("properties"), list):
                schema_content = _normalize_schema_content(prop)
                content_hash = canonical_json_hash(_structural_fingerprint(schema_content))
                nested_id = schema_hashes.get(content_hash) or f"schema:anon/{content_hash}"
                _register_schema(nested_id, _inline_name_hint(prop), schema_content,
                                 True, provenance, schemas, schema_hashes)
            elif isinstance(prop_type, dict):
                nested_id = schema_id_for_raml_type(prop_type, allow_name_field=False)
                if nested_id:
                    _register_schema(nested_id, None, prop_type, True, provenance, schemas, schema_hashes)
            elif prop_type == "array":
                items = prop.get("items")
                if isinstance(items, dict):
                    items_id = schema_id_for_raml_type(items, allow_name_field=False)
                    if items_id:
                        _register_schema(items_id, _inline_name_hint(items), items, True,
                                         provenance, schemas, schema_hashes)

    kind = schema.get("type") or "unknown"
    if kind == "array":
        items = schema.get("items") if isinstance(schema.get("items"), dict) else None
        if isinstance(items, dict):
            items_id = schema_id_for_raml_type(items, allow_name_field=False)
            if items_id:
                _register_schema(items_id, None, items, True, provenance, schemas, schema_hashes)

    additional_props = schema.get("additionalProperties")
    if isinstance(additional_props, dict):
        additional_id = schema_id_for_raml_type(additional_props, allow_name_field=False)
        if additional_id:
            _register_schema(additional_id, None, additional_props, True, provenance, schemas, schema_hashes)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def extract_schemas(spec: dict[str, Any], spec_path: str) -> dict[str, dict]:
    """Extract all schemas from a RAML spec into a flat dict.

    Args:
        spec: Parsed RAML specification.
        spec_path: Path to the source spec file (for provenance).

    Returns:
        Dict mapping schema_id -> schema record.
    """
    schemas: dict[str, dict] = {}
    schema_hashes: dict[str, str] = {}

    for primitive in ("object", "array"):
        sid = f"schema:types/{primitive}"
        prov = Provenance(spec_path, f"raml:types:{primitive}")
        _register_schema(sid, primitive, {"type": primitive}, False, prov, schemas, schema_hashes)

    types = spec.get("types")

    # Pass 0: Pre-populate hash table with all named types for forward-reference resolution
    if isinstance(types, dict):
        for name, schema in types.items():
            if not isinstance(schema, dict):
                continue
            content_hash = canonical_json_hash(
                _structural_fingerprint(_normalize_schema_content(schema))
            )
            schema_hashes[content_hash] = f"schema:types/{name}"

    # Pass 1: Register all named types (without nested schemas)
    if isinstance(types, dict):
        for name, schema in types.items():
            if not isinstance(schema, dict):
                continue
            prov = Provenance(spec_path, f"raml:types:{name}")
            _register_schema(f"schema:types/{name}", name, schema, False, prov,
                             schemas, schema_hashes, register_nested=False)

    # Pass 2: Process nested schemas within named types
    if isinstance(types, dict):
        for name, schema in types.items():
            if not isinstance(schema, dict):
                continue
            prov = Provenance(spec_path, f"raml:types:{name}")
            _register_nested_schemas(schema, prov, schemas, schema_hashes)

    # Walk resources to register inline schemas from operation bodies
    resources = spec.get("resources", spec.get("paths"))
    for endpoint in walk_resources(resources, ""):
        method = endpoint.get("method")
        path = endpoint.get("path", "")
        if not isinstance(method, dict):
            continue
        for body in method.get("body") or []:
            if not isinstance(body, dict):
                continue
            has_structure = any(body.get(f) for f in RAML_BODY_STRUCTURE_FIELDS)
            if has_structure:
                schema_content = _normalize_schema_content(body)
                sid = f"schema:anon/{canonical_json_hash(_structural_fingerprint(schema_content))}"
                prov = Provenance(spec_path, f"raml:{path}:body")
                _register_schema(sid, None, schema_content, True, prov, schemas, schema_hashes)
        for response in method.get("responses") or []:
            if not isinstance(response, dict):
                continue
            for body in response.get("body") or []:
                if not isinstance(body, dict):
                    continue
                has_structure = any(body.get(f) for f in RAML_BODY_STRUCTURE_FIELDS)
                if has_structure:
                    schema_content = _normalize_schema_content(body)
                    sid = f"schema:anon/{canonical_json_hash(_structural_fingerprint(schema_content))}"
                    prov = Provenance(spec_path, f"raml:{path}:responses")
                    _register_schema(sid, None, schema_content, True, prov, schemas, schema_hashes)

    return schemas


def extract_operations(spec: dict[str, Any], spec_path: str) -> list[dict]:
    """Extract all operations from a RAML spec.

    Args:
        spec: Parsed RAML specification.
        spec_path: Path to the source spec file (for provenance).

    Returns:
        List of operation dicts.
    """
    operations: list[dict] = []
    resources = spec.get("resources", spec.get("paths"))

    for endpoint in walk_resources(resources, ""):
        method_obj = endpoint.get("method")
        path_template = endpoint.get("path")
        if not isinstance(method_obj, dict) or not isinstance(path_template, str):
            continue

        method = (method_obj.get("method") or "").upper()
        if not method:
            continue

        op_id = f"op:{method}:{path_template}"

        parameters: list[dict] = []
        for loc_key, loc in (("uriParameters", "path"), ("queryParameters", "query"), ("headers", "header")):
            params = method_obj.get(loc_key)
            if not isinstance(params, dict):
                continue
            for name, param in params.items():
                if not isinstance(param, dict):
                    continue
                parameters.append({
                    "name": name,
                    "location": loc,
                    "required": param.get("required"),
                    "schema_id": schema_id_for_raml_type(param),
                    "description": param.get("description"),
                    "deprecated": param.get("deprecated"),
                    "provenance": Provenance(spec_path, f"raml:{path_template}:{method}:{loc_key}:{name}").__dict__,
                })

        bodies: list[dict] = []
        for body in method_obj.get("body") or []:
            if not isinstance(body, dict):
                continue
            bodies.append({
                "media_type": body.get("name"),
                "schema_id": _schema_id_for_body(body),
                "required": body.get("required"),
                "description": body.get("description"),
                "provenance": Provenance(spec_path, f"raml:{path_template}:{method}:body").__dict__,
            })

        responses: list[dict] = []
        for response in method_obj.get("responses") or []:
            if not isinstance(response, dict):
                continue
            status_code = str(response.get("code", ""))
            body_list = response.get("body") or []
            if body_list:
                for body in body_list:
                    if not isinstance(body, dict):
                        continue
                    responses.append({
                        "status_code": status_code,
                        "media_type": body.get("name"),
                        "schema_id": _schema_id_for_body(body),
                        "description": body.get("description"),
                        "provenance": Provenance(spec_path, f"raml:{path_template}:{method}:responses:{status_code}").__dict__,
                    })
            else:
                responses.append({
                    "status_code": status_code,
                    "media_type": None,
                    "schema_id": None,
                    "description": response.get("description"),
                    "provenance": Provenance(spec_path, f"raml:{path_template}:{method}:responses:{status_code}").__dict__,
                })

        operations.append({
            "id": op_id,
            "method": method,
            "path_template": path_template,
            "parameters": parameters,
            "request_bodies": bodies,
            "responses": responses,
            "tags": [],
            "summary": method_obj.get("displayName"),
            "description": method_obj.get("description"),
            "provenance": Provenance(spec_path, f"raml:{path_template}:{method}").__dict__,
        })

    return operations
