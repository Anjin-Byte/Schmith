"""OpenAPI adapter for schemas extraction."""

from typing import Any, Dict, List, Optional

from builders.shared.hashing import canonical_json_hash
from builders.shared.provenance import Provenance
from builders.shared.schema_ids import schema_id_for_schema, schema_id_from_ref


def resolve_ref(spec: Dict[str, Any], ref: str) -> Optional[Dict[str, Any]]:
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
    if isinstance(node, dict):
        return node
    return None


def detect_nullable(schema: Dict[str, Any]) -> Optional[bool]:
    """Detect if a schema is nullable."""
    if "nullable" in schema:
        return bool(schema.get("nullable"))
    type_value = schema.get("type")
    if isinstance(type_value, list):
        return "null" in type_value
    return None


def extract_constraints(schema: Dict[str, Any]) -> Dict[str, Any]:
    """Extract validation constraints from a schema."""
    constraints = {}
    for key in (
        "minLength", "maxLength", "pattern", "minimum", "maximum",
        "minItems", "maxItems", "uniqueItems", "enum", "const",
    ):
        if key in schema:
            constraints[key] = schema.get(key)
    return constraints


def extract_composition(schema: Dict[str, Any], spec: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Extract composition (oneOf, anyOf, allOf) from a schema."""
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


def build_field(
    name: str,
    schema_id: Optional[str],
    required: bool,
    field_schema: Dict[str, Any],
    pointer: str,
    provenance: Provenance,
) -> Dict[str, Any]:
    """Build a field entry for a schema."""
    enum_values = field_schema.get("enum") if isinstance(field_schema.get("enum"), list) else None
    enum_names = field_schema.get("x-enumNames") if isinstance(field_schema.get("x-enumNames"), list) else None
    field = {
        "json_name": name,
        "schema_id": schema_id,
        "required": required,
        "nullable": detect_nullable(field_schema),
        "description": field_schema.get("description"),
        "deprecated": field_schema.get("deprecated"),
        "read_only": field_schema.get("readOnly"),
        "write_only": field_schema.get("writeOnly"),
        "examples": field_schema.get("examples"),
        "enum_values": enum_values,
        "enum_names": enum_names,
        "json_pointer": pointer,
        "provenance": provenance.__dict__,
    }
    field["availability"] = {
        "json_name": "native" if name else "absent",
        "schema_id": "adapter" if schema_id else "absent",
        "required": "native",
        "nullable": "native" if field["nullable"] is not None else "absent",
        "description": "native" if field["description"] else "absent",
        "deprecated": "native" if field["deprecated"] is not None else "absent",
        "read_only": "native" if field["read_only"] is not None else "absent",
        "write_only": "native" if field["write_only"] is not None else "absent",
        "examples": "native" if field["examples"] is not None else "absent",
        "enum_values": "native" if enum_values is not None else "absent",
        "enum_names": "native" if enum_names is not None else "absent",
        "json_pointer": "adapter",
        "provenance": "native",
    }
    return field


def register_schema(
    schema_id: str,
    name_hint: Optional[str],
    schema: Dict[str, Any],
    is_inline: bool,
    provenance: Provenance,
    spec: Dict[str, Any],
    schemas: Dict[str, Dict[str, Any]],
    schema_hashes: Dict[str, str],
    register_nested: bool = True,
) -> None:
    """Register a schema in the schemas dictionary."""
    if schema_id in schemas:
        return

    # Check if this schema is already registered under a different ID
    if schema_id.startswith("schema:anon/"):
        content_hash = schema_id.split("/")[-1]
        if content_hash in schema_hashes:
            return
        schema_hashes[content_hash] = schema_id

    kind = schema.get("type") or "unknown"
    if isinstance(kind, list):
        kind = next((k for k in kind if k != "null"), "unknown")

    properties = []
    required_raw = schema.get("required")
    required_fields: List[str] = required_raw if isinstance(required_raw, list) else []

    props = schema.get("properties")
    if isinstance(props, dict):
        for prop_name, prop_schema in props.items():
            if not isinstance(prop_schema, dict):
                continue
            prop_ref = prop_schema.get("$ref")
            if isinstance(prop_ref, str):
                prop_schema_id = schema_id_from_ref(prop_ref)
            else:
                prop_schema_id = schema_id_for_schema(prop_schema)
            pointer = f"$.{prop_name}"
            properties.append(
                build_field(prop_name, prop_schema_id, prop_name in required_fields, prop_schema, pointer, provenance)
            )
            if register_nested and isinstance(prop_schema, dict) and "$ref" not in prop_schema:
                nested_id = schema_id_for_schema(prop_schema)
                if nested_id:
                    register_schema(nested_id, None, prop_schema, True, provenance, spec, schemas, schema_hashes)

    items_schema_id = None
    if kind == "array":
        items = schema.get("items") if isinstance(schema.get("items"), dict) else None
        if isinstance(items, dict):
            items_schema_id = schema_id_for_schema(items)
            # Don't register $ref schemas - they will be registered when their target is processed
            if register_nested and items_schema_id and "$ref" not in items:
                register_schema(items_schema_id, None, items, True, provenance, spec, schemas, schema_hashes)

    additional_properties_schema_id = None
    additional_props = schema.get("additionalProperties")
    if isinstance(additional_props, dict):
        additional_properties_schema_id = schema_id_for_schema(additional_props)
        # Don't register $ref schemas - they will be registered when their target is processed
        if register_nested and additional_properties_schema_id and "$ref" not in additional_props:
            register_schema(additional_properties_schema_id, None, additional_props, True, provenance, spec, schemas, schema_hashes)

    schema_record = {
        "id": schema_id,
        "name_hint": name_hint,
        "kind": kind or "unknown",
        "title": schema.get("title"),
        "description": schema.get("description"),
        "enum_values": schema.get("enum") if isinstance(schema.get("enum"), list) else None,
        "enum_names": schema.get("x-enumNames") if isinstance(schema.get("x-enumNames"), list) else None,
        "properties": properties,
        "required": list(required_fields) if isinstance(required_fields, list) else [],
        "items_schema_id": items_schema_id,
        "additional_properties_schema_id": additional_properties_schema_id,
        "constraints": extract_constraints(schema),
        "composition": extract_composition(schema, spec),
        "provenance": provenance.__dict__,
        "is_inline": is_inline,
    }
    schema_record["availability"] = {
        "id": "adapter",
        "name_hint": "native" if name_hint else "absent",
        "kind": "native" if schema.get("type") is not None else "absent",
        "title": "native" if schema.get("title") else "absent",
        "description": "native" if schema.get("description") else "absent",
        "enum_values": "native" if schema_record["enum_values"] is not None else "absent",
        "enum_names": "native" if schema_record["enum_names"] is not None else "absent",
        "properties": "native" if properties else "absent",
        "required": "native" if required_fields else "absent",
        "items_schema_id": "native" if items_schema_id else "absent",
        "additional_properties_schema_id": "native" if additional_properties_schema_id else "absent",
        "constraints": "native" if schema_record["constraints"] else "absent",
        "composition": "native" if schema_record["composition"] else "absent",
        "provenance": "native",
    }
    schemas[schema_id] = schema_record

    if not is_inline:
        content_hash = canonical_json_hash(schema)
        schema_hashes[content_hash] = schema_id


def extract_schemas(spec: Dict[str, Any], spec_path: str) -> Dict[str, Dict[str, Any]]:
    """
    Extract schemas from an OpenAPI/Swagger specification.

    Supports both OpenAPI 3.x and Swagger 2.0 formats.

    Args:
        spec: Parsed OpenAPI specification.
        spec_path: Path to the source spec file.

    Returns:
        Dictionary mapping schema IDs to schema records.
    """
    schemas: Dict[str, Dict[str, Any]] = {}
    schema_hashes: Dict[str, str] = {}

    # Extract named schemas
    if spec.get("swagger") == "2.0":
        definitions = spec.get("definitions")
        if isinstance(definitions, dict):
            for name, schema in definitions.items():
                if not isinstance(schema, dict):
                    continue
                schema_id = f"schema:definitions/{name}"
                provenance = Provenance(spec_path, f"#/definitions/{name}")
                register_schema(schema_id, name, schema, False, provenance, spec, schemas, schema_hashes)
    else:
        components = spec.get("components")
        if isinstance(components, dict):
            comp_schemas = components.get("schemas")
            if isinstance(comp_schemas, dict):
                for name, schema in comp_schemas.items():
                    if not isinstance(schema, dict):
                        continue
                    schema_id = f"schema:components/{name}"
                    provenance = Provenance(spec_path, f"#/components/schemas/{name}")
                    register_schema(schema_id, name, schema, False, provenance, spec, schemas, schema_hashes)

    # Extract inline schemas from operations
    paths = spec.get("paths")
    if isinstance(paths, dict):
        for path_template, path_item in paths.items():
            if not isinstance(path_item, dict):
                continue
            for method, operation in path_item.items():
                if not isinstance(method, str) or not isinstance(operation, dict):
                    continue

                # Swagger 2.0 body parameters
                if spec.get("swagger") == "2.0":
                    parameters = operation.get("parameters")
                    if isinstance(parameters, list):
                        for idx, param in enumerate(parameters):
                            if not isinstance(param, dict):
                                continue
                            if param.get("in") != "body":
                                continue
                            schema = param.get("schema")
                            if isinstance(schema, dict):
                                schema_id = schema_id_for_schema(schema)
                                if schema_id:
                                    provenance = Provenance(spec_path, f"#/paths/{path_template}/{method}/parameters/{idx}")
                                    register_schema(schema_id, None, schema, True, provenance, spec, schemas, schema_hashes)
                else:
                    # OpenAPI 3.x request body
                    if "requestBody" in operation and isinstance(operation.get("requestBody"), dict):
                        content = operation["requestBody"].get("content")
                        if isinstance(content, dict):
                            for media_type, media in content.items():
                                if not isinstance(media, dict):
                                    continue
                                schema = media.get("schema")
                                if isinstance(schema, dict):
                                    schema_id = schema_id_for_schema(schema)
                                    if schema_id:
                                        provenance = Provenance(spec_path, f"#/paths/{path_template}/{method}/requestBody/content/{media_type}")
                                        register_schema(schema_id, None, schema, True, provenance, spec, schemas, schema_hashes)

                # Responses
                responses = operation.get("responses")
                if isinstance(responses, dict):
                    for status, response in responses.items():
                        if not isinstance(response, dict):
                            continue
                        if spec.get("swagger") == "2.0":
                            schema = response.get("schema")
                            if isinstance(schema, dict):
                                schema_id = schema_id_for_schema(schema)
                                if schema_id:
                                    provenance = Provenance(spec_path, f"#/paths/{path_template}/{method}/responses/{status}")
                                    register_schema(schema_id, None, schema, True, provenance, spec, schemas, schema_hashes)
                        else:
                            content = response.get("content")
                            if isinstance(content, dict):
                                for media_type, media in content.items():
                                    if not isinstance(media, dict):
                                        continue
                                    schema = media.get("schema")
                                    if isinstance(schema, dict):
                                        schema_id = schema_id_for_schema(schema)
                                        if schema_id:
                                            provenance = Provenance(spec_path, f"#/paths/{path_template}/{method}/responses/{status}/content/{media_type}")
                                            register_schema(schema_id, None, schema, True, provenance, spec, schemas, schema_hashes)

    return schemas
