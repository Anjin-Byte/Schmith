"""RAML adapter for operations extraction."""

from typing import Any, Dict, Iterable, List, Optional

from builders.shared.hashing import canonical_json_hash
from builders.shared.io import operation_id
from builders.shared.provenance import Provenance


# Fields that indicate an inline schema definition (not just a type reference)
RAML_INLINE_SCHEMA_FIELDS = {"properties", "items", "additionalProperties", "facets"}

# Primitive type names that should trigger inline schema hashing when combined with structure
RAML_PRIMITIVE_TYPES = {"object", "array", "string", "number", "integer", "boolean", "null"}


def schema_id_for_raml_type(type_decl: Any) -> Optional[str]:
    """
    Generate schema ID for RAML type declarations.

    Args:
        type_decl: The type declaration (string reference or dict).

    Returns:
        A schema ID string, or None if type_decl is invalid.
    """
    if isinstance(type_decl, str):
        return f"schema:types/{type_decl}"
    if isinstance(type_decl, dict):
        name = type_decl.get("name")
        if isinstance(name, str):
            return f"schema:types/{name}"
        return f"schema:anon/{canonical_json_hash(type_decl)}"
    return None


def schema_id_for_raml_body(body: Dict[str, Any]) -> Optional[str]:
    """
    Generate schema ID for a RAML request/response body.

    Handles inline schemas by hashing the body content when it contains
    structural definitions (properties, items, etc.) rather than just
    returning a generic 'schema:types/object'.

    This detection logic is independent from the schemas builder to allow
    cross-validation via invariant tests.

    Args:
        body: The RAML body dict containing type, properties, etc.

    Returns:
        A schema ID string or None.
    """
    body_type = body.get("type")

    # Check if body has inline schema structure
    has_inline_structure = any(body.get(field) for field in RAML_INLINE_SCHEMA_FIELDS)

    if has_inline_structure:
        # Inline schema - create anonymous hash from schema content
        # Exclude fields that are not part of the schema definition
        exclude_fields = {"name", "displayName", "examples", "example", "key"}
        schema_content = {k: v for k, v in body.items() if k not in exclude_fields}
        return f"schema:anon/{canonical_json_hash(schema_content)}"

    # No inline structure - check if type is a named reference
    if isinstance(body_type, str):
        if body_type not in RAML_PRIMITIVE_TYPES:
            # Named type reference (e.g., "typ.Customer")
            return f"schema:types/{body_type}"
        # Primitive type without structure - return generic type
        return f"schema:types/{body_type}"

    if isinstance(body_type, dict):
        # Dict type declaration - use the standard function
        return schema_id_for_raml_type(body_type)

    return None


def walk_resources(node: Any, base_path: str) -> Iterable[Dict[str, Any]]:
    """
    Recursively walk RAML resources and yield endpoint details.

    Args:
        node: Current resource node (list or dict).
        base_path: Accumulated path from parent resources.

    Yields:
        Dicts with method, path, and details for each endpoint.
    """
    if isinstance(node, list):
        for item in node:
            yield from walk_resources(item, base_path)
        return
    if isinstance(node, dict):
        rel = node.get("relativeUri")
        path = f"{base_path}{rel}" if rel else base_path
        methods = node.get("methods") if isinstance(node.get("methods"), list) else []
        for method in methods:
            if isinstance(method, dict):
                yield {"method": method.get("method"), "path": path, "details": method}
        children = node.get("resources") if isinstance(node.get("resources"), list) else []
        for child in children:
            yield from walk_resources(child, path)


def extract_operations(spec: Dict[str, Any], spec_path: str) -> List[Dict[str, Any]]:
    """
    Extract operations from a RAML specification.

    Args:
        spec: Parsed RAML specification.
        spec_path: Path to the source spec file.

    Returns:
        List of operation dictionaries.
    """
    operations: List[Dict[str, Any]] = []
    resources = spec.get("resources", spec.get("paths"))

    for endpoint in walk_resources(resources, ""):
        method = endpoint.get("method")
        path_template = endpoint.get("path")
        details = endpoint.get("details") if isinstance(endpoint.get("details"), dict) else {}
        if not isinstance(method, str) or not isinstance(path_template, str):
            continue

        op_id = operation_id(method, path_template)

        # Extract parameters
        parameters: List[Dict[str, Any]] = []
        for location_key, location in (
            ("uriParameters", "path"),
            ("queryParameters", "query"),
            ("headers", "header"),
        ):
            params = details.get(location_key)
            if not isinstance(params, dict):
                continue
            for name, param in params.items():
                if not isinstance(param, dict):
                    continue
                schema_id = schema_id_for_raml_type(param)
                parameters.append({
                    "name": name,
                    "location": location,
                    "required": param.get("required"),
                    "schema_id": schema_id,
                    "description": param.get("description"),
                    "deprecated": param.get("deprecated"),
                    "explode": None,
                    "style": None,
                    "provenance": Provenance(
                        source_file=spec_path,
                        source_pointer=f"raml:{path_template}:{method}:{location_key}:{name}",
                    ).__dict__,
                })

        # Extract request bodies
        bodies: List[Dict[str, Any]] = []
        body_section = details.get("body")
        if isinstance(body_section, list):
            for body in body_section:
                if not isinstance(body, dict):
                    continue
                media_type = body.get("name")
                schema_id = schema_id_for_raml_body(body)
                bodies.append({
                    "media_type": media_type,
                    "schema_id": schema_id,
                    "required": body.get("required"),
                    "description": body.get("description"),
                    "examples": body.get("examples"),
                    "provenance": Provenance(
                        source_file=spec_path,
                        source_pointer=f"raml:{path_template}:{method}:body",
                    ).__dict__,
                })

        # Extract responses
        responses: List[Dict[str, Any]] = []
        responses_section = details.get("responses")
        if isinstance(responses_section, list):
            for response in responses_section:
                if not isinstance(response, dict):
                    continue
                status_code = response.get("code")
                body_list = response.get("body") if isinstance(response.get("body"), list) else []
                if body_list:
                    for body in body_list:
                        if not isinstance(body, dict):
                            continue
                        media_type = body.get("name")
                        schema_id = schema_id_for_raml_body(body)
                        responses.append({
                            "status_code": str(status_code),
                            "media_type": media_type,
                            "schema_id": schema_id,
                            "description": body.get("description"),
                            "provenance": Provenance(
                                source_file=spec_path,
                                source_pointer=f"raml:{path_template}:{method}:responses:{status_code}",
                            ).__dict__,
                        })
                else:
                    responses.append({
                        "status_code": str(status_code),
                        "media_type": None,
                        "schema_id": None,
                        "description": response.get("description"),
                        "provenance": Provenance(
                            source_file=spec_path,
                            source_pointer=f"raml:{path_template}:{method}:responses:{status_code}",
                        ).__dict__,
                    })

        operations.append({
            "id": op_id,
            "method": method.upper(),
            "path_template": path_template,
            "declared": {
                "parameters": parameters,
                "request_bodies": bodies,
                "responses": responses,
            },
            "effective": {
                "parameters": parameters,
                "request_bodies": bodies,
                "responses": responses,
            },
            "tags": [],
            "summary": details.get("displayName"),
            "description": details.get("description"),
            "provenance": Provenance(
                source_file=spec_path,
                source_pointer=f"raml:{path_template}:{method}",
            ).__dict__,
        })

    return operations
