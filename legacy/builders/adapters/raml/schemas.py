"""RAML adapter for schemas extraction."""

from typing import Any, Dict, Iterable, List, Optional, Tuple, cast

from builders.shared.hashing import canonical_json_hash
from builders.shared.provenance import Provenance


# Structural fields that indicate a RAML body contains an inline schema definition
# (rather than just a type reference). This detection is independent from the
# operations builder's detection, allowing the invariant test to validate consistency.
RAML_BODY_STRUCTURE_FIELDS = {"properties", "items", "additionalProperties", "facets"}

# Fields to exclude when hashing inline schema content (metadata, not schema structure)
RAML_BODY_EXCLUDE_FIELDS = {"name", "displayName", "examples", "example", "key"}


def normalize_raml_schema_content(schema: Dict[str, Any]) -> Dict[str, Any]:
    """Strip non-structural fields before hashing or matching schemas."""
    return {k: v for k, v in schema.items() if k not in RAML_BODY_EXCLUDE_FIELDS}


def raml_structural_fingerprint(schema: Dict[str, Any]) -> Dict[str, Any]:
    """Return a minimal, structural payload for deterministic schema matching."""
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
        return {"type": kind, "constraints": extract_constraints(schema)}
    # Fallback to normalized content when type is missing or unknown.
    return normalize_raml_schema_content(schema)


def inline_name_hint(schema: Dict[str, Any]) -> Optional[str]:
    """Return a name hint for inline schemas when RAML provides one."""
    name = schema.get("name")
    if isinstance(name, str) and name:
        return name
    display = schema.get("displayName")
    if isinstance(display, str) and display:
        return display
    return None


def schema_id_for_raml_type(type_decl: Any, allow_name_field: bool = True) -> Optional[str]:
    """
    Generate schema ID for RAML type declarations.

    Args:
        type_decl: The type declaration (string reference or dict).
        allow_name_field: If True, use the internal 'name' field for dict types.
                         Set to False for inline type definitions where the name
                         field should be ignored.

    Returns:
        A schema ID string, or None if type_decl is invalid.
    """
    if isinstance(type_decl, str):
        return f"schema:types/{type_decl}"
    if isinstance(type_decl, dict):
        type_dict = cast(Dict[str, Any], type_decl)
        type_value = type_dict.get("type")
        if isinstance(type_value, str) and not any(
            type_dict.get(field) for field in RAML_BODY_STRUCTURE_FIELDS
        ):
            return f"schema:types/{type_value}"
        if allow_name_field:
            name = type_dict.get("name")
            if isinstance(name, str):
                return f"schema:types/{name}"
        return f"schema:anon/{canonical_json_hash(type_dict)}"
    return None


def extract_inline_schema_from_body(
    body: Dict[str, Any]
) -> Optional[Tuple[str, Dict[str, Any]]]:
    """
    Detect and extract inline schema from a RAML request/response body.

    This function independently detects when a body contains an inline schema
    definition (has structural fields like 'properties') vs. a simple type
    reference. The detection logic is intentionally independent from the
    operations builder to allow cross-validation via invariant tests.

    Args:
        body: A RAML body dict (from method.body or response.body).

    Returns:
        A tuple of (schema_id, schema_content) if an inline schema is detected,
        or None if the body is just a type reference.
    """
    has_structure = any(body.get(field) for field in RAML_BODY_STRUCTURE_FIELDS)

    if has_structure:
        schema_content = normalize_raml_schema_content(body)
        schema_id = f"schema:anon/{canonical_json_hash(raml_structural_fingerprint(schema_content))}"
        return (schema_id, schema_content)

    body_type = body.get("type")
    if isinstance(body_type, dict):
        schema_id = schema_id_for_raml_type(body_type)
        if schema_id:
            return (schema_id, body_type)

    return None


def walk_resources(node: Any, base_path: str) -> Iterable[Dict[str, Any]]:
    """
    Recursively yield methods from nested RAML resources.

    Args:
        node: Current resource node (list or dict).
        base_path: Accumulated path from parent resources.

    Yields:
        Dicts with path and method for each endpoint.
    """
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


def build_field(
    name: str,
    schema_id: Optional[str],
    required: bool,
    field_schema: Dict[str, Any],
    pointer: str,
    provenance: Provenance,
    items_schema_id: Optional[str] = None,
) -> Dict[str, Any]:
    """Build a field entry for a schema.

    Args:
        name: Field name.
        schema_id: Schema ID for the field type.
        required: Whether the field is required.
        field_schema: Raw field schema dict.
        pointer: JSON pointer to the field.
        provenance: Provenance information.
        items_schema_id: For array fields, the schema ID of the array items.

    Returns:
        Field record dictionary.
    """
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
        "constraints": extract_constraints(field_schema),
        "json_pointer": pointer,
        "items_schema_id": items_schema_id,
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
        "json_pointer": "adapter",
        "items_schema_id": "native" if items_schema_id else "absent",
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

    if is_inline and not name_hint:
        # Use inline name/displayName if present to improve nested type naming.
        name_hint = inline_name_hint(schema)

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
            pointer = f"$.{prop_name}"
            prop_type = prop.get("type")
            prop_schema_id = schema_id_for_raml_type(prop_type)

            # Inline object properties should be treated as structured schemas.
            if prop_type == "object" and isinstance(prop.get("properties"), list):
                schema_content = normalize_raml_schema_content(prop)
                content_hash = canonical_json_hash(raml_structural_fingerprint(schema_content))
                if content_hash in schema_hashes:
                    # Exact structural match to a named schema.
                    prop_schema_id = schema_hashes[content_hash]
                else:
                    prop_schema_id = f"schema:anon/{content_hash}"
                    if register_nested:
                        register_schema(
                            prop_schema_id, inline_name_hint(prop), schema_content, True, provenance,
                            spec, schemas, schema_hashes
                        )

            # For array properties, compute items_schema_id from the items field
            prop_items_schema_id = None
            if prop_type == "array":
                items = prop.get("items")
                if isinstance(items, dict):
                    # First check if items content matches an existing named type
                    items_hash = canonical_json_hash(
                        raml_structural_fingerprint(normalize_raml_schema_content(items))
                    )
                    if items_hash in schema_hashes:
                        # Use the existing named type's schema ID
                        prop_items_schema_id = schema_hashes[items_hash]
                    else:
                        prop_items_schema_id = schema_id_for_raml_type(items, allow_name_field=False)

            properties.append(
                build_field(prop_name, prop_schema_id, prop_required, prop, pointer, provenance, prop_items_schema_id)
            )
            if register_nested and isinstance(prop, dict):
                if isinstance(prop_type, dict):
                    nested_id = schema_id_for_raml_type(prop_type, allow_name_field=False)
                    if nested_id:
                        register_schema(
                            nested_id, None, prop_type, True, provenance,
                            spec, schemas, schema_hashes
                        )
                elif prop_type == "array":
                    items = prop.get("items")
                    items_id = None
                    if isinstance(items, dict):
                        items_id = schema_id_for_raml_type(items, allow_name_field=False)
                    if items_id:
                        register_schema(
                            items_id, inline_name_hint(items), items, True, provenance,
                            spec, schemas, schema_hashes
                        )

    items_schema_id = None
    if kind == "array":
        items = schema.get("items") if isinstance(schema.get("items"), dict) else None
        if isinstance(items, dict):
            items_schema_id = schema_id_for_raml_type(items, allow_name_field=False)
            if register_nested and items_schema_id:
                register_schema(
                    items_schema_id, inline_name_hint(items), items, True, provenance,
                    spec, schemas, schema_hashes
                )

    additional_properties_schema_id = None
    additional_props = schema.get("additionalProperties")
    if isinstance(additional_props, dict):
        additional_properties_schema_id = schema_id_for_raml_type(additional_props, allow_name_field=False)
        if register_nested and additional_properties_schema_id:
            register_schema(
                additional_properties_schema_id, inline_name_hint(additional_props), additional_props, True, provenance,
                spec, schemas, schema_hashes
            )

    schema_record = {
        "id": schema_id,
        "name_hint": name_hint,
        "kind": kind or "unknown",
        "title": schema.get("title"),
        "description": schema.get("description"),
        "properties": properties,
        "required": list(required_fields) if isinstance(required_fields, list) else [],
        "items_schema_id": items_schema_id,
        "additional_properties_schema_id": additional_properties_schema_id,
        "constraints": extract_constraints(schema),
        "composition": None,
        "provenance": provenance.__dict__,
        "is_inline": is_inline,
    }
    schema_record["availability"] = {
        "id": "adapter",
        "name_hint": "native" if name_hint else "absent",
        "kind": "native" if schema.get("type") is not None else "absent",
        "title": "native" if schema.get("title") else "absent",
        "description": "native" if schema.get("description") else "absent",
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


def register_nested_schemas(
    schema: Dict[str, Any],
    provenance: Provenance,
    spec: Dict[str, Any],
    schemas: Dict[str, Dict[str, Any]],
    schema_hashes: Dict[str, str],
) -> None:
    """Register nested inline schemas within a schema's properties."""
    props = schema.get("properties")

    if isinstance(props, list):
        for prop in props:
            if not isinstance(prop, dict):
                continue
            prop_type = prop.get("type")
            if prop_type == "object" and isinstance(prop.get("properties"), list):
                schema_content = normalize_raml_schema_content(prop)
                content_hash = canonical_json_hash(raml_structural_fingerprint(schema_content))
                if content_hash in schema_hashes:
                    nested_id = schema_hashes[content_hash]
                else:
                    nested_id = f"schema:anon/{content_hash}"
                register_schema(
                    nested_id, inline_name_hint(prop), schema_content, True, provenance,
                    spec, schemas, schema_hashes
                )
            elif isinstance(prop_type, dict):
                nested_id = schema_id_for_raml_type(prop_type, allow_name_field=False)
                if nested_id:
                    register_schema(nested_id, None, prop_type, True, provenance, spec, schemas, schema_hashes)
            elif prop_type == "array":
                items = prop.get("items")
                if isinstance(items, dict):
                    items_id = schema_id_for_raml_type(items, allow_name_field=False)
                    if items_id:
                        register_schema(
                            items_id, inline_name_hint(items), items, True, provenance,
                            spec, schemas, schema_hashes
                        )

    kind = schema.get("type") or "unknown"
    if kind == "array":
        items = schema.get("items") if isinstance(schema.get("items"), dict) else None
        if isinstance(items, dict):
            items_schema_id = schema_id_for_raml_type(items, allow_name_field=False)
            if items_schema_id:
                register_schema(items_schema_id, None, items, True, provenance, spec, schemas, schema_hashes)

    additional_props = schema.get("additionalProperties")
    if isinstance(additional_props, dict):
        additional_properties_schema_id = schema_id_for_raml_type(additional_props, allow_name_field=False)
        if additional_properties_schema_id:
            register_schema(additional_properties_schema_id, None, additional_props, True, provenance, spec, schemas, schema_hashes)


def extract_schemas(spec: Dict[str, Any], spec_path: str) -> Dict[str, Dict[str, Any]]:
    """
    Extract schemas from a RAML specification.

    Args:
        spec: Parsed RAML specification.
        spec_path: Path to the source spec file.

    Returns:
        Dictionary mapping schema IDs to schema records.
    """
    schemas: Dict[str, Dict[str, Any]] = {}
    schema_hashes: Dict[str, str] = {}

    # Register primitive types
    for primitive in ("object", "array"):
        schema_id = f"schema:types/{primitive}"
        provenance = Provenance(spec_path, f"raml:types:{primitive}")
        register_schema(schema_id, primitive, {"type": primitive}, False, provenance, spec, schemas, schema_hashes)

    # Pass 0: Pre-populate schema_hashes with all named types
    # This ensures array items can reference named types regardless of iteration order
    types = spec.get("types")
    if isinstance(types, dict):
        for name, schema in types.items():
            if not isinstance(schema, dict):
                continue
            content_hash = canonical_json_hash(
                raml_structural_fingerprint(normalize_raml_schema_content(schema))
            )
            schema_id = f"schema:types/{name}"
            schema_hashes[content_hash] = schema_id

    # Pass 1: Register all top-level named types without nested schemas
    if isinstance(types, dict):
        for name, schema in types.items():
            if not isinstance(schema, dict):
                continue
            schema_id = f"schema:types/{name}"
            provenance = Provenance(spec_path, f"raml:types:{name}")
            register_schema(schema_id, name, schema, False, provenance, spec, schemas, schema_hashes, register_nested=False)

    # Pass 2: Process nested schemas within named types
    if isinstance(types, dict):
        for name, schema in types.items():
            if not isinstance(schema, dict):
                continue
            provenance = Provenance(spec_path, f"raml:types:{name}")
            register_nested_schemas(schema, provenance, spec, schemas, schema_hashes)

    # Walk resources to find inline schemas in operation bodies
    resources = spec.get("resources", spec.get("paths"))

    for endpoint in walk_resources(resources, ""):
        method = endpoint.get("method")
        path = endpoint.get("path", "")
        if not isinstance(method, dict):
            continue

        # Process request bodies
        body = method.get("body") if isinstance(method.get("body"), list) else []
        for entry in body:
            if not isinstance(entry, dict):
                continue
            inline_result = extract_inline_schema_from_body(entry)
            if inline_result:
                schema_id, schema_content = inline_result
                provenance = Provenance(spec_path, f"raml:{path}:body")
                register_schema(schema_id, None, schema_content, True, provenance, spec, schemas, schema_hashes)

        # Process response bodies
        responses = method.get("responses") if isinstance(method.get("responses"), list) else []
        for response in responses:
            if not isinstance(response, dict):
                continue
            bodies = response.get("body") if isinstance(response.get("body"), list) else []
            for entry in bodies:
                if not isinstance(entry, dict):
                    continue
                inline_result = extract_inline_schema_from_body(entry)
                if inline_result:
                    schema_id, schema_content = inline_result
                    provenance = Provenance(spec_path, f"raml:{path}:responses")
                    register_schema(schema_id, None, schema_content, True, provenance, spec, schemas, schema_hashes)

    return schemas
