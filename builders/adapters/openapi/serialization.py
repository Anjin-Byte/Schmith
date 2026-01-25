"""OpenAPI adapter for serialization extraction."""

from typing import Any, Dict, List, Tuple

from builders.shared.hashing import canonical_json_hash
from builders.shared.io import operation_id
from builders.shared.schema_ids import schema_id_for_schema

HTTP_METHODS = {"get", "post", "put", "patch", "delete", "head", "options"}


def schema_id_from_ref(ref: str) -> str:
    """Generate a schema ID from an OpenAPI $ref string."""
    if ref.startswith("#/components/schemas/"):
        return f"schema:components/{ref.split('/')[-1]}"
    if ref.startswith("#/components/"):
        return f"schema:components/{ref.lstrip('#/components/')}".replace("/", "_")
    if ref.startswith("#/definitions/"):
        return f"schema:definitions/{ref.split('/')[-1]}"
    return f"schema:ref/{ref.lstrip('#/')}".replace("/", "_")


def add_json_paths(schemas_map: Dict[str, List[str]], schema_id: str, pointer: str) -> None:
    """Add a JSON path to a schema's path list."""
    schemas_map.setdefault(schema_id, [])
    if pointer not in schemas_map[schema_id]:
        schemas_map[schema_id].append(pointer)


def collect_inline_json_paths(schema: Any, schema_id: str, json_paths: Dict[str, List[str]]) -> None:
    """Collect JSON paths from inline schema properties."""
    if not isinstance(schema, dict):
        return

    props = schema.get("properties")
    if isinstance(props, dict):
        for prop_name, prop_schema in props.items():
            add_json_paths(json_paths, schema_id, f"$.{prop_name}")
            if isinstance(prop_schema, dict):
                child_id = schema_id_for_schema(prop_schema)
                if child_id:
                    collect_inline_json_paths(prop_schema, child_id, json_paths)

    if schema.get("type") == "array" and isinstance(schema.get("items"), dict):
        items = schema.get("items")
        child_id = schema_id_for_schema(items)
        if child_id:
            collect_inline_json_paths(items, child_id, json_paths)


def extract_serialization(spec: Dict[str, Any]) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """
    Extract serialization information from an OpenAPI/Swagger specification.

    Supports both OpenAPI 3.x and Swagger 2.0 formats.

    Args:
        spec: Parsed OpenAPI specification.

    Returns:
        A tuple of (media_types, json_paths) dictionaries.
    """
    media_types: Dict[str, Any] = {}
    json_paths: Dict[str, List[str]] = {}

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

                op_id = operation_id(method, path_template)
                op_entry = media_types.setdefault(op_id, {"request": [], "responses": {}})

                if spec.get("swagger") == "2.0":
                    # Swagger 2.0 style
                    consumes = operation.get("consumes") if isinstance(operation.get("consumes"), list) else []
                    produces = operation.get("produces") if isinstance(operation.get("produces"), list) else []
                    op_entry["request"] = sorted(set(consumes))
                    if produces:
                        op_entry["responses"] = {"default": sorted(set(produces))}
                    parameters = operation.get("parameters")
                    if isinstance(parameters, list):
                        for param in parameters:
                            if not isinstance(param, dict):
                                continue
                            if param.get("in") != "body":
                                continue
                            schema = param.get("schema")
                            if isinstance(schema, dict):
                                schema_id = schema_id_for_schema(schema)
                                if schema_id:
                                    collect_inline_json_paths(schema, schema_id, json_paths)
                else:
                    # OpenAPI 3.x style
                    request_body = operation.get("requestBody")
                    if isinstance(request_body, dict):
                        content = request_body.get("content")
                        if isinstance(content, dict):
                            op_entry["request"] = sorted(content.keys())
                            for media in content.values():
                                if not isinstance(media, dict):
                                    continue
                                schema = media.get("schema")
                                if isinstance(schema, dict):
                                    schema_id = schema_id_for_schema(schema)
                                    if schema_id:
                                        collect_inline_json_paths(schema, schema_id, json_paths)

                    responses = operation.get("responses")
                    if isinstance(responses, dict):
                        response_media: Dict[str, List[str]] = {}
                        for status, response in responses.items():
                            if not isinstance(response, dict):
                                continue
                            content = response.get("content")
                            if isinstance(content, dict):
                                response_media[str(status)] = sorted(content.keys())
                                for media in content.values():
                                    if not isinstance(media, dict):
                                        continue
                                    schema = media.get("schema")
                                    if isinstance(schema, dict):
                                        schema_id = schema_id_for_schema(schema)
                                        if schema_id:
                                            collect_inline_json_paths(schema, schema_id, json_paths)
                        op_entry["responses"] = response_media

    # Extract JSON paths from named schemas
    if spec.get("swagger") == "2.0":
        definitions = spec.get("definitions") if isinstance(spec.get("definitions"), dict) else {}
        for name, schema in definitions.items():
            if not isinstance(schema, dict):
                continue
            schema_id = f"schema:definitions/{name}"
            props = schema.get("properties")
            if isinstance(props, dict):
                for prop_name in props.keys():
                    add_json_paths(json_paths, schema_id, f"$.{prop_name}")
            collect_inline_json_paths(schema, schema_id, json_paths)
    else:
        components = spec.get("components") if isinstance(spec.get("components"), dict) else {}
        comp_schemas = components.get("schemas") if isinstance(components.get("schemas"), dict) else {}
        for name, schema in comp_schemas.items():
            if not isinstance(schema, dict):
                continue
            schema_id = f"schema:components/{name}"
            props = schema.get("properties")
            if isinstance(props, dict):
                for prop_name in props.keys():
                    add_json_paths(json_paths, schema_id, f"$.{prop_name}")
            collect_inline_json_paths(schema, schema_id, json_paths)

    return {"operations": media_types}, {"schemas": json_paths}
