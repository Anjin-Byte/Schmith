"""OpenAPI adapter for operations extraction."""

from typing import Any, Dict, List, Optional

from builders.shared.io import operation_id
from builders.shared.provenance import Provenance
from builders.shared.schema_ids import schema_id_for_schema

HTTP_METHODS = {"get", "post", "put", "patch", "delete", "head", "options"}


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


def resolve_parameter(spec: Dict[str, Any], param: Any) -> Optional[Dict[str, Any]]:
    """Resolve a parameter, following $ref if present."""
    if not isinstance(param, dict):
        return None
    if "$ref" in param and isinstance(param.get("$ref"), str):
        resolved = resolve_ref(spec, param["$ref"])
        if resolved is None:
            return None
        param = resolved
    if not isinstance(param, dict):
        return None
    return param


def extract_operations(spec: Dict[str, Any], spec_path: str) -> List[Dict[str, Any]]:
    """
    Extract operations from an OpenAPI/Swagger specification.

    Supports both OpenAPI 3.x and Swagger 2.0 formats.

    Args:
        spec: Parsed OpenAPI specification.
        spec_path: Path to the source spec file.

    Returns:
        List of operation dictionaries.
    """
    operations: List[Dict[str, Any]] = []
    paths = spec.get("paths")
    if not isinstance(paths, dict):
        return operations

    is_swagger_2 = spec.get("swagger") == "2.0"

    for path_template, path_item in paths.items():
        if not isinstance(path_item, dict):
            continue
        path_params = path_item.get("parameters")
        if not isinstance(path_params, list):
            path_params = []

        for method, operation in path_item.items():
            if not isinstance(method, str) or method.lower() not in HTTP_METHODS:
                continue
            if not isinstance(operation, dict):
                continue

            op_id = operation_id(method, path_template)
            op_params = operation.get("parameters")
            if not isinstance(op_params, list):
                op_params = []

            # Extract parameters
            parameters = []
            for param in list(op_params) + list(path_params):
                resolved = resolve_parameter(spec, param)
                if not resolved:
                    continue
                schema_id = None
                schema = resolved.get("schema")
                if schema is not None:
                    schema_id = schema_id_for_schema(schema)
                parameters.append({
                    "name": resolved.get("name"),
                    "location": resolved.get("in"),
                    "required": bool(resolved.get("required")) if resolved.get("required") is not None else None,
                    "schema_id": schema_id,
                    "description": resolved.get("description"),
                    "deprecated": resolved.get("deprecated"),
                    "explode": resolved.get("explode"),
                    "style": resolved.get("style"),
                    "provenance": Provenance(
                        source_file=spec_path,
                        source_pointer=f"#/paths/{path_template}/{method}/parameters",
                    ).__dict__,
                })

            # Extract request bodies
            bodies: List[Dict[str, Any]] = []

            # OpenAPI 3.x request body handling
            request_body = operation.get("requestBody")
            if isinstance(request_body, dict):
                content = request_body.get("content")
                if isinstance(content, dict):
                    for media_type, media in content.items():
                        schema_id = None
                        if isinstance(media, dict):
                            schema_id = schema_id_for_schema(media.get("schema"))
                        bodies.append({
                            "media_type": media_type,
                            "schema_id": schema_id,
                            "required": bool(request_body.get("required")) if request_body.get("required") is not None else None,
                            "description": request_body.get("description"),
                            "examples": request_body.get("examples"),
                            "provenance": Provenance(
                                source_file=spec_path,
                                source_pointer=f"#/paths/{path_template}/{method}/requestBody",
                            ).__dict__,
                        })

            # Swagger 2.0 request body handling
            if is_swagger_2:
                consumes = operation.get("consumes")
                if not isinstance(consumes, list):
                    consumes = []
                has_form_data = False
                for param in op_params:
                    resolved = resolve_parameter(spec, param)
                    if resolved:
                        if resolved.get("in") == "body":
                            schema = resolved.get("schema")
                            schema_id = schema_id_for_schema(schema) if schema else None
                            if consumes:
                                for media_type in consumes:
                                    bodies.append({
                                        "media_type": media_type,
                                        "schema_id": schema_id,
                                        "required": bool(resolved.get("required")) if resolved.get("required") is not None else None,
                                        "description": resolved.get("description"),
                                        "examples": None,
                                        "provenance": Provenance(
                                            source_file=spec_path,
                                            source_pointer=f"#/paths/{path_template}/{method}/parameters",
                                        ).__dict__,
                                    })
                            else:
                                bodies.append({
                                    "media_type": None,
                                    "schema_id": schema_id,
                                    "required": bool(resolved.get("required")) if resolved.get("required") is not None else None,
                                    "description": resolved.get("description"),
                                    "examples": None,
                                    "provenance": Provenance(
                                        source_file=spec_path,
                                        source_pointer=f"#/paths/{path_template}/{method}/parameters",
                                    ).__dict__,
                                })
                            break
                        elif resolved.get("in") == "formData":
                            has_form_data = True

                if has_form_data and not bodies and consumes:
                    for media_type in consumes:
                        bodies.append({
                            "media_type": media_type,
                            "schema_id": None,
                            "required": None,
                            "description": None,
                            "examples": None,
                            "provenance": Provenance(
                                source_file=spec_path,
                                source_pointer=f"#/paths/{path_template}/{method}/parameters",
                            ).__dict__,
                        })

            # Extract responses
            responses: List[Dict[str, Any]] = []
            responses_obj = operation.get("responses")
            if isinstance(responses_obj, dict):
                responses_dict: Dict[str, Any] = {str(k): v for k, v in responses_obj.items()}
                for status_code, response in responses_dict.items():
                    if not isinstance(response, dict):
                        continue
                    content = response.get("content")
                    if isinstance(content, dict):
                        for media_type, media in content.items():
                            schema_id = None
                            if isinstance(media, dict):
                                schema_id = schema_id_for_schema(media.get("schema"))
                            responses.append({
                                "status_code": status_code,
                                "media_type": media_type,
                                "schema_id": schema_id,
                                "description": response.get("description"),
                                "provenance": Provenance(
                                    source_file=spec_path,
                                    source_pointer=f"#/paths/{path_template}/{method}/responses/{status_code}",
                                ).__dict__,
                            })
                    elif is_swagger_2:
                        produces = operation.get("produces")
                        if isinstance(produces, list) and produces:
                            schema = response.get("schema")
                            schema_id = schema_id_for_schema(schema) if schema else None
                            for media_type in produces:
                                responses.append({
                                    "status_code": status_code,
                                    "media_type": media_type,
                                    "schema_id": schema_id,
                                    "description": response.get("description"),
                                    "provenance": Provenance(
                                        source_file=spec_path,
                                        source_pointer=f"#/paths/{path_template}/{method}/responses/{status_code}",
                                    ).__dict__,
                                })
                        else:
                            schema = response.get("schema")
                            schema_id = schema_id_for_schema(schema) if schema else None
                            responses.append({
                                "status_code": status_code,
                                "media_type": None,
                                "schema_id": schema_id,
                                "description": response.get("description"),
                                "provenance": Provenance(
                                    source_file=spec_path,
                                    source_pointer=f"#/paths/{path_template}/{method}/responses/{status_code}",
                                ).__dict__,
                            })
                    else:
                        responses.append({
                            "status_code": status_code,
                            "media_type": None,
                            "schema_id": None,
                            "description": response.get("description"),
                            "provenance": Provenance(
                                source_file=spec_path,
                                source_pointer=f"#/paths/{path_template}/{method}/responses/{status_code}",
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
                "tags": operation.get("tags") or [],
                "summary": operation.get("summary"),
                "description": operation.get("description"),
                "provenance": Provenance(
                    source_file=spec_path,
                    source_pointer=f"#/paths/{path_template}/{method}",
                ).__dict__,
            })

    return operations
