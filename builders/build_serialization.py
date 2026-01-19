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
from typing import Any, Dict, List, Optional, Tuple

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ROOT)
sys.path.append(SCRIPT_DIR)

from pipeline.config import api_name, load_config, resolve_spec_path

CONFIG_DEFAULT = os.path.join(ROOT, "config.toml")
HTTP_METHODS = {"get", "post", "put", "patch", "delete", "head", "options"}


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


def operation_id(method: str, path_template: str) -> str:
    return f"op:{method.upper()}:{path_template}"


def schema_id_from_ref(ref: str) -> str:
    if ref.startswith("#/components/schemas/"):
        return f"schema:components/{ref.split('/')[-1]}"
    if ref.startswith("#/components/"):
        return f"schema:components/{ref.lstrip('#/components/') }".replace("/", "_")
    if ref.startswith("#/definitions/"):
        return f"schema:definitions/{ref.split('/')[-1]}"
    return f"schema:ref/{ref.lstrip('#/') }".replace("/", "_")


def schema_id_for_schema(schema: Any) -> str:
    if not isinstance(schema, dict):
        return "schema:unknown"
    ref = schema.get("$ref")
    if isinstance(ref, str):
        return schema_id_from_ref(ref)
    # fallback to anon hash
    canonical = json.dumps(schema, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    digest = hashlib.sha1(canonical.encode("utf-8")).hexdigest()
    return f"schema:anon/{digest}"


def schema_id_for_raml_type(type_decl: Any, allow_name_field: bool = True, schema_hashes: Optional[Dict[str, str]] = None) -> str:
    """
    Generate schema ID for RAML type declarations (matches build_ir_schemas.py logic).

    Args:
        type_decl: The type declaration (string reference or dict)
        allow_name_field: If True, use the internal 'name' field for dict types.
                         Set to False for inline type definitions where the name
                         field should be ignored.
    """
    if isinstance(type_decl, str):
        return f"schema:types/{type_decl}"
    if isinstance(type_decl, dict):
        # Only use the 'name' field if explicitly allowed (for top-level types)
        # For inline types, the 'name' field is an internal RAML field and should be ignored
        if allow_name_field:
            name = type_decl.get("name")
            if isinstance(name, str):
                return f"schema:types/{name}"
        # fallback to anon hash
        canonical = json.dumps(type_decl, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
        digest = hashlib.sha1(canonical.encode("utf-8")).hexdigest()
        # Check if this hash corresponds to a named type (deduplication)
        if schema_hashes and digest in schema_hashes:
            return schema_hashes[digest]
        return f"schema:anon/{digest}"
    return "schema:unknown"


def add_json_paths(schemas_map: Dict[str, List[str]], schema_id: str, pointer: str) -> None:
    schemas_map.setdefault(schema_id, [])
    if pointer not in schemas_map[schema_id]:
        schemas_map[schema_id].append(pointer)


def collect_inline_json_paths(schema: Any, schema_id: str, json_paths: Dict[str, List[str]], is_raml: bool = False, schema_hashes: Optional[Dict[str, str]] = None) -> None:
    if not isinstance(schema, dict):
        return

    # Choose the appropriate schema ID function based on adapter type
    get_schema_id = schema_id_for_raml_type if is_raml else schema_id_for_schema

    props = schema.get("properties")
    if isinstance(props, dict):
        for prop_name, prop_schema in props.items():
            add_json_paths(json_paths, schema_id, f"$.{prop_name}")
            if isinstance(prop_schema, dict):
                # For inline nested schemas, don't use the name field
                if is_raml:
                    child_id = schema_id_for_raml_type(prop_schema, allow_name_field=False, schema_hashes=schema_hashes)
                else:
                    child_id = get_schema_id(prop_schema)
                collect_inline_json_paths(prop_schema, child_id, json_paths, is_raml, schema_hashes)
    elif isinstance(props, list):
        for prop in props:
            if not isinstance(prop, dict):
                continue
            name = prop.get("name")
            if isinstance(name, str):
                add_json_paths(json_paths, schema_id, f"$.{name}")
            # For RAML, check if prop has a type field that's a dict (inline definition)
            if isinstance(prop, dict):
                prop_type = prop.get("type")
                if isinstance(prop_type, dict):
                    # For inline types, don't use the internal 'name' field
                    child_id = schema_id_for_raml_type(prop_type, allow_name_field=False, schema_hashes=schema_hashes) if is_raml else get_schema_id(prop_type)
                    collect_inline_json_paths(prop_type, child_id, json_paths, is_raml, schema_hashes)
                # Also handle array properties with inline items
                elif prop_type == "array":
                    items = prop.get("items")
                    if isinstance(items, dict):
                        if is_raml:
                            items_id = schema_id_for_raml_type(items, allow_name_field=False, schema_hashes=schema_hashes)
                        else:
                            items_id = get_schema_id(items)
                        collect_inline_json_paths(items, items_id, json_paths, is_raml, schema_hashes)

    if schema.get("type") == "array" and isinstance(schema.get("items"), dict):
        items = schema.get("items")
        # For inline array items, use RAML-aware schema ID generation without using name field
        if is_raml:
            child_id = schema_id_for_raml_type(items, allow_name_field=False, schema_hashes=schema_hashes)
        else:
            child_id = get_schema_id(items)
        collect_inline_json_paths(items, child_id, json_paths, is_raml, schema_hashes)


def extract_openapi_serialization(spec: Dict[str, Any]) -> Tuple[Dict[str, Any], Dict[str, Any]]:
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
                                collect_inline_json_paths(schema, schema_id, json_paths)
                else:
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
                                        collect_inline_json_paths(schema, schema_id, json_paths)
                        op_entry["responses"] = response_media

    # schema json paths
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


def extract_raml_serialization(spec: Dict[str, Any]) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    media_types: Dict[str, Any] = {}
    json_paths: Dict[str, List[str]] = {}

    # Build hash-to-name mapping for deduplication (same as schema script)
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
                    schema = entry.get("type")
                    schema_id = schema_id_for_raml_type(schema, schema_hashes=schema_hashes)
                    collect_inline_json_paths(schema, schema_id, json_paths, is_raml=True, schema_hashes=schema_hashes)
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
                        schema = entry.get("type")
                        schema_id = schema_id_for_raml_type(schema, schema_hashes=schema_hashes)
                        collect_inline_json_paths(schema, schema_id, json_paths, is_raml=True, schema_hashes=schema_hashes)
                op_entry["responses"] = response_media
            children = node.get("resources") if isinstance(node.get("resources"), list) else []
            for child in children:
                walk_resources(child, path)

    walk_resources(resources, "")

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
        collect_inline_json_paths(schema, schema_id, json_paths, is_raml=True, schema_hashes=schema_hashes)

    return {"operations": media_types}, {"schemas": json_paths}


def write_serialization(spec_name: str, media_types: Dict[str, Any], json_paths: Dict[str, Any]) -> None:
    base_dir = os.path.join(ROOT, "ir", spec_name, "serialization")
    os.makedirs(base_dir, exist_ok=True)
    with open(os.path.join(base_dir, "media_types.json"), "w", encoding="utf-8") as handle:
        json.dump(media_types, handle, indent=2)
        handle.write("\n")
    with open(os.path.join(base_dir, "json_paths.json"), "w", encoding="utf-8") as handle:
        json.dump(json_paths, handle, indent=2)
        handle.write("\n")


def update_manifest(spec_name: str) -> None:
    manifest_path = os.path.join(ROOT, "ir", spec_name, "manifest.json")
    if not os.path.exists(manifest_path):
        return
    with open(manifest_path, "r", encoding="utf-8") as handle:
        manifest = json.load(handle)
    os.makedirs(os.path.dirname(manifest_path), exist_ok=True)
    with open(manifest_path, "w", encoding="utf-8") as handle:
        json.dump(manifest, handle, indent=2)
        handle.write("\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build IR serialization indexes.")
    parser.add_argument("--config", default=CONFIG_DEFAULT, help="Path to config.toml.")
    parser.add_argument("--spec", default="", help="Path to spec file.")
    parser.add_argument("--adapter", default="openapi", help="Spec adapter: openapi or raml.")
    args = parser.parse_args()

    config = load_config(args.config)
    spec_path = resolve_spec_path(config, args.spec)
    spec_name = api_name(config)

    spec = load_spec(spec_path)
    if args.adapter == "openapi":
        media_types, json_paths = extract_openapi_serialization(spec)
    elif args.adapter == "raml":
        media_types, json_paths = extract_raml_serialization(spec)
    else:
        raise ValueError(f"Unknown adapter: {args.adapter}")

    write_serialization(spec_name, media_types, json_paths)
    update_manifest(spec_name)
    print(f"Wrote serialization indexes to ir/{spec_name}/serialization")
    return 0


if __name__ == "__main__":
    sys.exit(main())
