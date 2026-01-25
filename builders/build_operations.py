#!/usr/bin/env python3
"""Build IR operations index and detail files.

This orchestrator delegates to format-specific adapters for extraction
and handles common operations like writing output and updating manifests.
"""
# pyright: reportUnknownVariableType=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownArgumentType=false
# pyright: reportUnnecessaryIsInstance=false
# pyright: reportOptionalIterable=false
import argparse
import json
import os
import sys
from typing import Any, Dict, List

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from builders.adapters.openapi.operations import extract_operations as extract_openapi_operations
from builders.adapters.raml.operations import extract_operations as extract_raml_operations
from builders.shared.io import escape_id, load_spec
from pipeline.config import api_name, load_config, resolve_spec_path

CONFIG_DEFAULT = os.path.join(ROOT, "config.toml")


def wrap_availability_operation(operation: Dict[str, Any]) -> Dict[str, Any]:
    """Add availability annotations to an operation."""
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
    """Create an index entry for an operation."""
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
    """Write operation files and index."""
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
    """Update or create the IR manifest."""
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
    """Main entry point."""
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
