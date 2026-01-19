#!/usr/bin/env python3
# pyright: reportUnknownVariableType=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownArgumentType=false
# pyright: reportUnnecessaryIsInstance=false
# pyright: reportOptionalIterable=false
import argparse
import hashlib
import json
import os
import re
import sys
from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Optional, Tuple

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ROOT)
sys.path.append(SCRIPT_DIR)

from pipeline.config import api_name, load_config, resolve_spec_path

CONFIG_DEFAULT = os.path.join(ROOT, "config.toml")
HTTP_METHODS = {"get", "post", "put", "patch", "delete", "head", "options"}


@dataclass(frozen=True)
class Provenance:
    source_file: str
    source_pointer: str
    via: Tuple[str, ...] = ()


def canonical_json_hash(payload: Any) -> str:
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha1(canonical.encode("utf-8")).hexdigest()


def schema_id_from_ref(ref: str) -> str:
    if ref.startswith("#/components/schemas/"):
        return f"schema:components/{ref.split('/')[-1]}"
    if ref.startswith("#/components/"):
        return f"schema:components/{ref.lstrip('#/components/') }".replace("/", "_")
    return f"schema:ref/{ref.lstrip('#/') }".replace("/", "_")


def schema_id_for_schema(schema: Any) -> Optional[str]:
    if not isinstance(schema, dict):
        return None
    ref = schema.get("$ref")
    if isinstance(ref, str):
        return schema_id_from_ref(ref)
    return f"schema:anon/{canonical_json_hash(schema)}"


def schema_id_for_raml_type(type_decl: Any) -> Optional[str]:
    if isinstance(type_decl, str):
        return f"schema:types/{type_decl}"
    if isinstance(type_decl, dict):
        name = type_decl.get("name")
        if isinstance(name, str):
            return f"schema:types/{name}"
        return f"schema:anon/{canonical_json_hash(type_decl)}"
    return None


def escape_id(raw: str) -> str:
    return re.sub(r"[^A-Za-z0-9_]+", "_", raw).strip("_")


def availability(value: Any, state: str) -> Dict[str, Any]:
    return {"value": value, "availability": state}


def operation_id(method: str, path_template: str) -> str:
    return f"op:{method.upper()}:{path_template}"


def resolve_ref(spec: Dict[str, Any], ref: str) -> Optional[Dict[str, Any]]:
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


def load_spec(spec_path: str) -> Dict[str, Any]:
    ext = spec_path.lower().split(".")[-1]
    if ext in ("yaml", "yml"):
        try:
            import warnings
            from ruamel.yaml import YAML  # type: ignore

            yaml_parser = YAML(typ="safe")
            if hasattr(yaml_parser, "allow_duplicate_keys"):
                setattr(yaml_parser, "allow_duplicate_keys", True)
            if hasattr(yaml_parser, "allow_duplicate_anchors"):
                setattr(yaml_parser, "allow_duplicate_anchors", True)
            with open(spec_path, "r", encoding="utf-8") as handle:
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore")
                    return yaml_parser.load(handle)
        except Exception:
            pass
        import yaml  # type: ignore

        with open(spec_path, "r", encoding="utf-8") as handle:
            return yaml.safe_load(handle)
    with open(spec_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def extract_openapi_operations(spec: Dict[str, Any], spec_path: str) -> List[Dict[str, Any]]:
    operations: List[Dict[str, Any]] = []
    paths = spec.get("paths")
    if not isinstance(paths, dict):
        return operations

    # Check if this is Swagger 2.0
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

            # Swagger 2.0 request body handling (body and formData parameters)
            if is_swagger_2:
                consumes = operation.get("consumes")
                if not isinstance(consumes, list):
                    consumes = []
                # Check for body or formData parameters
                has_form_data = False
                for param in op_params:
                    resolved = resolve_parameter(spec, param)
                    if resolved:
                        if resolved.get("in") == "body":
                            # Body parameter with schema
                            schema = resolved.get("schema")
                            schema_id = schema_id_for_schema(schema) if schema else None
                            if consumes:
                                # Create one body per media type in consumes
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
                                # No consumes defined
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
                            break  # Only one body parameter allowed
                        elif resolved.get("in") == "formData":
                            has_form_data = True

                # If we have formData parameters but no bodies created, add request bodies for consumes
                if has_form_data and not bodies and consumes:
                    for media_type in consumes:
                        bodies.append({
                            "media_type": media_type,
                            "schema_id": None,  # formData doesn't have a unified schema
                            "required": None,
                            "description": None,
                            "examples": None,
                            "provenance": Provenance(
                                source_file=spec_path,
                                source_pointer=f"#/paths/{path_template}/{method}/parameters",
                            ).__dict__,
                        })

            responses: List[Dict[str, Any]] = []
            responses_obj = operation.get("responses")
            if isinstance(responses_obj, dict):
                responses_dict: Dict[str, Any] = {str(k): v for k, v in responses_obj.items()}
                for status_code, response in responses_dict.items():
                    if not isinstance(response, dict):
                        continue
                    content = response.get("content")
                    if isinstance(content, dict):
                        # OpenAPI 3.x style with content object
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
                        # Swagger 2.0: use 'produces' for media types
                        produces = operation.get("produces")
                        if isinstance(produces, list) and produces:
                            # If produces is defined, create one response per media type
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
                            # No produces defined, create response with null media_type
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
                        # OpenAPI 3.x without content - no media type
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


def extract_raml_operations(spec: Dict[str, Any], spec_path: str) -> List[Dict[str, Any]]:
    operations: List[Dict[str, Any]] = []
    resources = spec.get("resources", spec.get("paths"))

    def walk_resources(node: Any, base_path: str) -> Iterable[Dict[str, Any]]:
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

    for endpoint in walk_resources(resources, ""):
        method = endpoint.get("method")
        path_template = endpoint.get("path")
        details = endpoint.get("details") if isinstance(endpoint.get("details"), dict) else {}
        if not isinstance(method, str) or not isinstance(path_template, str):
            continue
        op_id = operation_id(method, path_template)
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

        bodies: List[Dict[str, Any]] = []
        body_section = details.get("body")
        if isinstance(body_section, list):
            for body in body_section:
                if not isinstance(body, dict):
                    continue
                media_type = body.get("name")
                schema_id = schema_id_for_raml_type(body.get("type"))
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
                        schema_id = schema_id_for_raml_type(body.get("type"))
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


def wrap_availability_operation(operation: Dict[str, Any]) -> Dict[str, Any]:
    availability_map = {
        "id": "adapter",
        "method": "native",
        "path_template": "native",
        "declared": "adapter",
        "effective": "adapter",
        "tags": "native" if operation.get("tags") else "absent",
        "summary": "native" if operation.get("summary") else "absent",
        "description": "native" if operation.get("description") else "absent",
    }

    def wrap_param(param: Dict[str, Any]) -> Dict[str, Any]:
        param["availability"] = {
            "name": "native" if param.get("name") else "absent",
            "location": "native" if param.get("location") else "absent",
            "required": "native" if param.get("required") is not None else "absent",
            "schema_id": "adapter" if param.get("schema_id") else "absent",
            "description": "native" if param.get("description") else "absent",
            "deprecated": "native" if param.get("deprecated") is not None else "absent",
            "explode": "native" if param.get("explode") is not None else "absent",
            "style": "native" if param.get("style") is not None else "absent",
            "provenance": "native" if param.get("provenance") else "absent",
        }
        return param

    def wrap_body(body: Dict[str, Any]) -> Dict[str, Any]:
        body["availability"] = {
            "media_type": "native" if body.get("media_type") else "absent",
            "schema_id": "adapter" if body.get("schema_id") else "absent",
            "required": "native" if body.get("required") is not None else "absent",
            "description": "native" if body.get("description") else "absent",
            "examples": "native" if body.get("examples") is not None else "absent",
            "provenance": "native" if body.get("provenance") else "absent",
        }
        return body

    def wrap_response(response: Dict[str, Any]) -> Dict[str, Any]:
        response["availability"] = {
            "status_code": "native" if response.get("status_code") else "absent",
            "media_type": "native" if response.get("media_type") else "absent",
            "schema_id": "adapter" if response.get("schema_id") else "absent",
            "description": "native" if response.get("description") else "absent",
            "provenance": "native" if response.get("provenance") else "absent",
        }
        return response

    for surface_key in ("declared", "effective"):
        surface = operation.get(surface_key) or {}
        surface["parameters"] = [wrap_param(p) for p in surface.get("parameters", [])]
        surface["request_bodies"] = [wrap_body(b) for b in surface.get("request_bodies", [])]
        surface["responses"] = [wrap_response(r) for r in surface.get("responses", [])]
        operation[surface_key] = surface

    operation["availability"] = availability_map
    return operation


def operation_index_entry(operation: Dict[str, Any]) -> Dict[str, Any]:
    requests = [b.get("schema_id") for b in operation.get("effective", {}).get("request_bodies", [])]
    responses = [r.get("schema_id") for r in operation.get("effective", {}).get("responses", [])]
    return {
        "operation_id": operation.get("id"),
        "method": operation.get("method"),
        "path": operation.get("path_template"),
        "requests": [s for s in requests if s],
        "responses": [s for s in responses if s],
        "tags": operation.get("tags") or [],
    }


def write_operations(spec_name: str, operations: List[Dict[str, Any]]) -> None:
    base_dir = os.path.join(ROOT, "ir", spec_name, "operations")
    os.makedirs(base_dir, exist_ok=True)
    index_entries = []
    for op in operations:
        op = wrap_availability_operation(op)
        index_entries.append(operation_index_entry(op))
        filename = f"{escape_id(op['id'])}.json"
        with open(os.path.join(base_dir, filename), "w", encoding="utf-8") as handle:
            json.dump(op, handle, indent=2)
            handle.write("\n")

    index_path = os.path.join(base_dir, "index.json")
    with open(index_path, "w", encoding="utf-8") as handle:
        json.dump({"operations": index_entries}, handle, indent=2)
        handle.write("\n")


def update_manifest(spec_name: str, operation_count: int) -> None:
    manifest_path = os.path.join(ROOT, "ir", spec_name, "manifest.json")
    if os.path.exists(manifest_path):
        with open(manifest_path, "r", encoding="utf-8") as handle:
            manifest = json.load(handle)
    else:
        manifest = {
            "spec_name": spec_name,
            "spec_version": None,
            "base_urls": [],
            "adapter": None,
            "generated_at": None,
            "counts": {"operations": 0, "schemas": 0, "edges": 0},
            "indexes": {
                "operations": "operations/index.json",
                "schemas": "schemas/index.json",
                "refs_edges": "refs/edges.json",
                "refs_adjacency": "refs/adjacency.json",
                "media_types": "serialization/media_types.json",
                "json_paths": "serialization/json_paths.json",
            },
        }
    manifest["counts"]["operations"] = operation_count
    os.makedirs(os.path.dirname(manifest_path), exist_ok=True)
    with open(manifest_path, "w", encoding="utf-8") as handle:
        json.dump(manifest, handle, indent=2)
        handle.write("\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build IR operations index and detail files.")
    parser.add_argument("--config", default=CONFIG_DEFAULT, help="Path to config.toml.")
    parser.add_argument("--spec", default="", help="Path to spec file.")
    parser.add_argument("--adapter", default="openapi", help="Spec adapter: openapi or raml.")
    args = parser.parse_args()

    config = load_config(args.config)
    spec_path = resolve_spec_path(config, args.spec)
    spec_name = api_name(config)

    spec = load_spec(spec_path)
    if args.adapter == "openapi":
        operations = extract_openapi_operations(spec, spec_path)
    elif args.adapter == "raml":
        operations = extract_raml_operations(spec, spec_path)
    else:
        raise ValueError(f"Unknown adapter: {args.adapter}")

    write_operations(spec_name, operations)
    update_manifest(spec_name, len(operations))
    print(f"Wrote {len(operations)} operations to ir/{spec_name}/operations")
    return 0


if __name__ == "__main__":
    sys.exit(main())
