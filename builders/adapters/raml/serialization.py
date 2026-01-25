"""RAML adapter for serialization extraction."""

import hashlib
import json
from typing import Any, Dict, List, Optional, Tuple

from builders.shared.io import operation_id


# Structural fields that indicate a RAML body contains an inline schema definition
# (rather than just a type reference). This detection is independent from the
# operations and schemas builders' detection, allowing the invariant test to validate consistency.
RAML_BODY_STRUCTURE_FIELDS = {"properties", "items", "additionalProperties", "facets"}

# Fields to exclude when hashing inline schema content (metadata, not schema structure)
RAML_BODY_EXCLUDE_FIELDS = {"name", "displayName", "examples", "example", "key"}


def canonical_json_hash(obj: Any) -> str:
    """Generate a canonical SHA1 hash for a JSON-serializable object."""
    canonical = json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha1(canonical.encode("utf-8")).hexdigest()


def schema_id_for_raml_type(
    type_decl: Any,
    allow_name_field: bool = True,
    schema_hashes: Optional[Dict[str, str]] = None
) -> str:
    """
    Generate schema ID for RAML type declarations.

    Args:
        type_decl: The type declaration (string reference or dict).
        allow_name_field: If True, use the internal 'name' field for dict types.
        schema_hashes: Optional mapping of content hashes to schema IDs for deduplication.

    Returns:
        A schema ID string.
    """
    if isinstance(type_decl, str):
        return f"schema:types/{type_decl}"
    if isinstance(type_decl, dict):
        if allow_name_field:
            name = type_decl.get("name")
            if isinstance(name, str):
                return f"schema:types/{name}"
        canonical = json.dumps(type_decl, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
        digest = hashlib.sha1(canonical.encode("utf-8")).hexdigest()
        if schema_hashes and digest in schema_hashes:
            return schema_hashes[digest]
        return f"schema:anon/{digest}"
    return "schema:unknown"


def extract_inline_schema_from_body(
    body: Dict[str, Any]
) -> Optional[Tuple[str, Dict[str, Any]]]:
    """
    Detect and extract inline schema from a RAML request/response body.

    This function independently detects when a body contains an inline schema
    definition (has structural fields like 'properties') vs. a simple type
    reference. The detection logic is intentionally independent from the
    operations and schemas builders to allow cross-validation via invariant tests.

    Args:
        body: A RAML body dict (from method.body or response.body).

    Returns:
        A tuple of (schema_id, schema_content) if an inline schema is detected,
        or None if the body is just a type reference.
    """
    has_structure = any(body.get(field) for field in RAML_BODY_STRUCTURE_FIELDS)

    if has_structure:
        schema_content = {
            k: v for k, v in body.items() if k not in RAML_BODY_EXCLUDE_FIELDS
        }
        schema_id = f"schema:anon/{canonical_json_hash(schema_content)}"
        return (schema_id, schema_content)

    body_type = body.get("type")
    if isinstance(body_type, dict):
        schema_id = schema_id_for_raml_type(body_type)
        if schema_id and schema_id != "schema:unknown":
            return (schema_id, body_type)

    return None


def add_json_paths(schemas_map: Dict[str, List[str]], schema_id: str, pointer: str) -> None:
    """Add a JSON path to a schema's path list."""
    schemas_map.setdefault(schema_id, [])
    if pointer not in schemas_map[schema_id]:
        schemas_map[schema_id].append(pointer)


def collect_inline_json_paths(
    schema: Any,
    schema_id: str,
    json_paths: Dict[str, List[str]],
    schema_hashes: Optional[Dict[str, str]] = None
) -> None:
    """Collect JSON paths from inline schema properties."""
    if not isinstance(schema, dict):
        return

    props = schema.get("properties")
    if isinstance(props, dict):
        for prop_name, prop_schema in props.items():
            add_json_paths(json_paths, schema_id, f"$.{prop_name}")
            if isinstance(prop_schema, dict):
                child_id = schema_id_for_raml_type(prop_schema, allow_name_field=False, schema_hashes=schema_hashes)
                collect_inline_json_paths(prop_schema, child_id, json_paths, schema_hashes)
    elif isinstance(props, list):
        for prop in props:
            if not isinstance(prop, dict):
                continue
            name = prop.get("name")
            if isinstance(name, str):
                add_json_paths(json_paths, schema_id, f"$.{name}")
            prop_type = prop.get("type")
            if isinstance(prop_type, dict):
                child_id = schema_id_for_raml_type(prop_type, allow_name_field=False, schema_hashes=schema_hashes)
                collect_inline_json_paths(prop_type, child_id, json_paths, schema_hashes)
            elif prop_type == "array":
                items = prop.get("items")
                if isinstance(items, dict):
                    items_id = schema_id_for_raml_type(items, allow_name_field=False, schema_hashes=schema_hashes)
                    collect_inline_json_paths(items, items_id, json_paths, schema_hashes)

    if schema.get("type") == "array" and isinstance(schema.get("items"), dict):
        items = schema.get("items")
        child_id = schema_id_for_raml_type(items, allow_name_field=False, schema_hashes=schema_hashes)
        collect_inline_json_paths(items, child_id, json_paths, schema_hashes)


def extract_serialization(spec: Dict[str, Any]) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """
    Extract serialization information from a RAML specification.

    Args:
        spec: Parsed RAML specification.

    Returns:
        A tuple of (media_types, json_paths) dictionaries.
    """
    media_types: Dict[str, Any] = {}
    json_paths: Dict[str, List[str]] = {}

    # Build hash-to-name mapping for deduplication
    schema_hashes: Dict[str, str] = {}
    types = spec.get("types") if isinstance(spec.get("types"), dict) else {}
    for name, schema in types.items():
        if isinstance(schema, dict):
            canonical = json.dumps(schema, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
            digest = hashlib.sha1(canonical.encode("utf-8")).hexdigest()
            schema_hashes[digest] = f"schema:types/{name}"

    resources = spec.get("resources", spec.get("paths"))

    def walk_resources(node: Any, base_path: str) -> None:
        if isinstance(node, list):
            for item in node:
                walk_resources(item, base_path)
            return
        if isinstance(node, dict):
            rel = node.get("relativeUri")
            path = f"{base_path}{rel}" if rel else base_path
            methods = node.get("methods") if isinstance(node.get("methods"), list) else []
            for method in methods:
                if not isinstance(method, dict):
                    continue
                method_name = method.get("method")
                if not isinstance(method_name, str):
                    continue
                op_id = operation_id(method_name, path)
                op_entry = media_types.setdefault(op_id, {"request": [], "responses": {}})
                body = method.get("body") if isinstance(method.get("body"), list) else []
                op_entry["request"] = sorted({b.get("name") for b in body if isinstance(b, dict) and b.get("name")})

                for entry in body:
                    if not isinstance(entry, dict):
                        continue
                    # Detect inline schemas independently
                    inline_result = extract_inline_schema_from_body(entry)
                    if inline_result:
                        schema_id, schema_content = inline_result
                        collect_inline_json_paths(schema_content, schema_id, json_paths, schema_hashes)
                    else:
                        schema = entry.get("type")
                        schema_id = schema_id_for_raml_type(schema, schema_hashes=schema_hashes)
                        if schema:
                            collect_inline_json_paths(schema, schema_id, json_paths, schema_hashes)

                responses = method.get("responses") if isinstance(method.get("responses"), list) else []
                response_media: Dict[str, List[str]] = {}
                for response in responses:
                    if not isinstance(response, dict):
                        continue
                    status_code = response.get("code")
                    bodies = response.get("body") if isinstance(response.get("body"), list) else []
                    response_media[str(status_code)] = sorted({b.get("name") for b in bodies if isinstance(b, dict) and b.get("name")})

                    for entry in bodies:
                        if not isinstance(entry, dict):
                            continue
                        # Detect inline schemas independently
                        inline_result = extract_inline_schema_from_body(entry)
                        if inline_result:
                            schema_id, schema_content = inline_result
                            collect_inline_json_paths(schema_content, schema_id, json_paths, schema_hashes)
                        else:
                            schema = entry.get("type")
                            schema_id = schema_id_for_raml_type(schema, schema_hashes=schema_hashes)
                            if schema:
                                collect_inline_json_paths(schema, schema_id, json_paths, schema_hashes)

                op_entry["responses"] = response_media
            children = node.get("resources") if isinstance(node.get("resources"), list) else []
            for child in children:
                walk_resources(child, path)

    walk_resources(resources, "")

    # Process named types for JSON paths
    types = spec.get("types") if isinstance(spec.get("types"), dict) else {}
    for name, schema in types.items():
        if not isinstance(schema, dict):
            continue
        schema_id = f"schema:types/{name}"
        props = schema.get("properties")
        if isinstance(props, list):
            for prop in props:
                if not isinstance(prop, dict):
                    continue
                prop_name = prop.get("name")
                if isinstance(prop_name, str):
                    add_json_paths(json_paths, schema_id, f"$.{prop_name}")
        elif isinstance(props, dict):
            for prop_name in props.keys():
                add_json_paths(json_paths, schema_id, f"$.{prop_name}")
        collect_inline_json_paths(schema, schema_id, json_paths, schema_hashes)

    return {"operations": media_types}, {"schemas": json_paths}
