#!/usr/bin/env python3
import argparse
import json
import os
import re
import sys
from typing import Any, Dict, List, Optional

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ROOT)
sys.path.append(SCRIPT_DIR)

from ingest.adapter import load_adapter
from pipeline.config import load_config, resolve_report_path, resolve_spec_path


CONFIG_DEFAULT = os.path.join(ROOT, "config.toml")
PATH_PARAM_RE = re.compile(r"{([^}]+)}")

SpecType = Dict[str, Any]
SchemaType = Dict[str, Any]


def resolve_ref(spec: SpecType, ref: Optional[str]) -> Optional[SchemaType]:
    if not ref or not ref.startswith("#/"):
        return None
    node = spec
    for part in ref.lstrip("#/").split("/"):
        if not isinstance(node, dict):
            return None
        node = node.get(part)
        if node is None:
            return None
    return node


def resolve_schema(spec: SpecType, schema: Any) -> SchemaType:
    if not isinstance(schema, dict):
        return {}
    if "$ref" in schema:
        resolved = resolve_ref(spec, schema["$ref"])
        return resolve_schema(spec, resolved or {})
    if "allOf" in schema:
        merged = {"type": "object", "properties": {}}
        for item in schema.get("allOf", []):
            item = resolve_schema(spec, item)
            props = item.get("properties") or {}
            for name, value in props.items():
                merged["properties"][name] = value
        return merged
    return schema


def resolve_parameter(spec: SpecType, param: Any) -> Optional[Dict[str, Any]]:
    ref = None
    if isinstance(param, dict) and "$ref" in param:
        ref = param.get("$ref")
        param = resolve_ref(spec, ref) or {}
    if not isinstance(param, dict):
        return None
    schema = resolve_schema(spec, param.get("schema") or {})
    return {
        "name": param.get("name"),
        "in": param.get("in"),
        "required": bool(param.get("required")) if param.get("required") is not None else None,
        "schema_ref": ref,
        "schema": schema if schema else None,
        "style": param.get("style"),
        "explode": param.get("explode"),
    }


def resolve_request_body(spec: SpecType, request_body: Any) -> Dict[str, Dict[str, Any]]:
    ref = None
    if isinstance(request_body, dict) and "$ref" in request_body:
        ref = request_body.get("$ref")
        request_body = resolve_ref(spec, ref) or {}
    if not isinstance(request_body, dict):
        return {}
    content = request_body.get("content") or {}
    resolved = {}
    for media_type, media in content.items():
        schema = resolve_schema(spec, (media or {}).get("schema") or {})
        schema_ref = (media or {}).get("schema", {}).get("$ref") if isinstance(media, dict) else None
        resolved[media_type] = {
            "schema_ref": schema_ref,
            "schema": schema if schema else None,
        }
    return resolved


def resolve_responses(spec: SpecType, responses: Any) -> Dict[str, Dict[str, Any]]:
    if not isinstance(responses, dict):
        return {}
    resolved = {}
    for status, response in responses.items():
        ref = None
        if isinstance(response, dict) and "$ref" in response:
            ref = response.get("$ref")
            response = resolve_ref(spec, ref) or {}
        content = (response or {}).get("content") or {}
        per_media = {}
        for media_type, media in content.items():
            schema = resolve_schema(spec, (media or {}).get("schema") or {})
            schema_ref = (media or {}).get("schema", {}).get("$ref") if isinstance(media, dict) else None
            per_media[media_type] = {
                "schema_ref": schema_ref,
                "schema": schema if schema else None,
            }
        resolved[str(status)] = {
            "response_ref": ref,
            "content": per_media,
        }
    return resolved


def extract_content_keys(responses: Dict[str, Dict[str, Any]]) -> List[str]:
    keys = set()
    for response in responses.values():
        for media_type in (response.get("content") or {}).keys():
            keys.add(media_type)
    return sorted(keys)


def parse_path_segments(path_template: str) -> List[Dict[str, Optional[str]]]:
    segments = [s for s in path_template.split("/") if s]
    parent_chain = []
    current = None
    for segment in segments:
        match = PATH_PARAM_RE.match(segment)
        if match:
            param = match.group(1)
            if current is None:
                current = {"collection_segment": None, "param": param}
                parent_chain.append(current)
                current = None
            else:
                current["param"] = param
                current = None
        else:
            current = {"collection_segment": segment, "param": None}
            parent_chain.append(current)
    return parent_chain


def infer_resource_hints(
    path_template: str,
    method: str,
    parameters: List[Dict[str, Any]],
    responses: Dict[str, Dict[str, Any]],
) -> Dict[str, Any]:
    path_params = [p for p in parameters if p and p.get("in") == "path"]
    identifier_params = [p.get("name") for p in path_params if p.get("name")]
    parent_chain = parse_path_segments(path_template)

    response_media = responses.get("200") or next(iter(responses.values()), {})
    response_schema = None
    for media in (response_media.get("content") or {}).values():
        if media.get("schema"):
            response_schema = media["schema"]
            break

    root_type = response_schema.get("type") if isinstance(response_schema, dict) else None
    collection_like = method == "get" and (not identifier_params or root_type == "array")
    item_like = method == "get" and bool(identifier_params) and root_type == "object"

    return {
        "collection_like": collection_like,
        "item_like": item_like,
        "identifier_params": identifier_params,
        "parent_chain": parent_chain,
    }


def build_operation_id(method: str, path_template: str) -> str:
    normalized = re.sub(r"[^A-Za-z0-9]+", "_", path_template.strip("/"))
    normalized = normalized or "root"
    return f"{method.lower()}_{normalized}"


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a normalized endpoint model from OpenAPI.")
    parser.add_argument("--config", default=CONFIG_DEFAULT, help="Path to config.toml.")
    parser.add_argument("--spec", default="", help="Path to spec file.")
    parser.add_argument("--adapter", default="openapi", help="Spec adapter (openapi).")
    parser.add_argument("--out", default="", help="Path to write endpoint model JSON.")
    args = parser.parse_args()

    config = load_config(args.config)
    spec_path = resolve_spec_path(config, args.spec)
    out_path = resolve_report_path(config, "endpoint_model.json", args.out)

    adapter = load_adapter(args.adapter)
    if getattr(adapter, "name", "") != "openapi":
        raise RuntimeError("Endpoint model is only supported for OpenAPI specs.")

    spec = adapter.load_spec(spec_path)
    operations = []

    for path_template, path_item in (spec.get("paths") or {}).items():
        if not isinstance(path_item, dict):
            continue
        path_params = path_item.get("parameters") or []
        for method, operation in path_item.items():
            if method.lower() not in ("get", "post", "put", "patch", "delete", "head", "options"):
                continue
            if not isinstance(operation, dict):
                continue
            op_params = (operation.get("parameters") or []) + path_params
            parameters = []
            for param in op_params:
                resolved = resolve_parameter(spec, param)
                if resolved:
                    parameters.append(resolved)

            request_body = resolve_request_body(spec, operation.get("requestBody") or {})
            responses = resolve_responses(spec, operation.get("responses") or {})
            produces = extract_content_keys(responses)
            consumes = sorted(request_body.keys())

            record = {
                "path_template": path_template,
                "http_method": method.upper(),
                "operation_id": operation.get("operationId") or build_operation_id(method, path_template),
                "tags": operation.get("tags") or [],
                "summary": operation.get("summary"),
                "description": operation.get("description"),
                "parameters": parameters,
                "path_params": [p for p in parameters if p.get("in") == "path"],
                "request_body": request_body,
                "responses": responses,
                "produces": produces,
                "consumes": consumes,
            }
            record["resource_hints"] = infer_resource_hints(
                path_template,
                method.lower(),
                parameters,
                responses,
            )
            operations.append(record)

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as handle:
        json.dump({"operations": operations, "specPath": spec_path}, handle, indent=2)
        handle.write("\n")

    print(f"Wrote endpoint model to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
