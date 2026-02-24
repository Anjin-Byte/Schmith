#!/usr/bin/env python3
"""Build IR schema index and detail files.

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

from builders.adapters.openapi.schemas import extract_schemas as extract_openapi_schemas
from builders.adapters.raml.schemas import extract_schemas as extract_raml_schemas
from builders.shared.io import escape_id, load_spec
from pipeline.config import api_name, load_config, resolve_spec_path

CONFIG_DEFAULT = os.path.join(ROOT, "config.toml")
CODEGEN_CONFIG = os.path.join(ROOT, "codegen", "config.toml")


def load_naming_config() -> Dict[str, Any] | None:
    """Load naming configuration from codegen/config.toml if available.

    Returns:
        Dictionary with naming config, or None to use default verbose naming.
    """
    if not os.path.exists(CODEGEN_CONFIG):
        return None

    try:
        import tomllib
    except ImportError:
        try:
            import tomli as tomllib  # type: ignore
        except ImportError:
            # No TOML parser available, use defaults
            return None

    try:
        with open(CODEGEN_CONFIG, "rb") as f:
            config = tomllib.load(f)
        naming = config.get("naming")
        if naming is None:
            return None
        # Handle nested abbreviations table
        if "abbreviations" in naming and isinstance(naming["abbreviations"], dict):
            naming["abbreviations"] = dict(naming["abbreviations"])
        return naming
    except Exception:
        return None


def load_operations_index(spec_name: str) -> Dict[str, List[str]]:
    """Load the operations index to determine where schemas are used."""
    operations_index_path = os.path.join(ROOT, "ir", spec_name, "operations", "index.json")
    if not os.path.exists(operations_index_path):
        return {}
    with open(operations_index_path, "r", encoding="utf-8") as handle:
        data = json.load(handle)
    mapping: Dict[str, List[str]] = {}
    for entry in data.get("operations", []):
        op_id = entry.get("operation_id")
        for schema_id in entry.get("requests", []) + entry.get("responses", []):
            if not schema_id:
                continue
            mapping.setdefault(schema_id, []).append(op_id)
    return mapping


def write_schemas(spec_name: str, schemas: Dict[str, Dict[str, Any]]) -> None:
    """Write schema files and index."""
    base_dir = os.path.join(ROOT, "ir", spec_name, "schemas")
    os.makedirs(base_dir, exist_ok=True)
    usage = load_operations_index(spec_name)
    index_entries = []
    for schema_id, schema in schemas.items():
        schema["where_used"] = usage.get(schema_id, [])
        schema["availability"]["where_used"] = "adapter" if schema["where_used"] else "absent"
        index_entries.append({
            "schema_id": schema_id,
            "name_hint": schema.get("name_hint"),
            "kind": schema.get("kind"),
            "where_used": schema.get("where_used"),
            "is_inline": bool(schema.get("is_inline")),
        })
        filename = f"{escape_id(schema_id)}.json"
        with open(os.path.join(base_dir, filename), "w", encoding="utf-8") as handle:
            json.dump(schema, handle, indent=2)
            handle.write("\n")

    index_path = os.path.join(base_dir, "index.json")
    with open(index_path, "w", encoding="utf-8") as handle:
        json.dump({"schemas": index_entries}, handle, indent=2)
        handle.write("\n")


def update_manifest(spec_name: str, schema_count: int) -> None:
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
    manifest["counts"]["schemas"] = schema_count
    os.makedirs(os.path.dirname(manifest_path), exist_ok=True)
    with open(manifest_path, "w", encoding="utf-8") as handle:
        json.dump(manifest, handle, indent=2)
        handle.write("\n")


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Build IR schema index and detail files.")
    parser.add_argument("--config", default=CONFIG_DEFAULT, help="Path to config.toml.")
    parser.add_argument("--spec", default="", help="Path to spec file.")
    parser.add_argument("--adapter", default="openapi", help="Spec adapter: openapi or raml.")
    parser.add_argument(
        "--naming",
        default=None,
        choices=["verbose", "semantic", "resource"],
        help="Naming strategy override. Default: use codegen/config.toml setting.",
    )
    args = parser.parse_args()

    config = load_config(args.config)
    spec_path = resolve_spec_path(config, args.spec)
    spec_name = api_name(config)

    # Load naming config (can be overridden by --naming flag)
    naming_config = load_naming_config()
    if args.naming:
        # Override strategy from command line
        if naming_config is None:
            naming_config = {}
        naming_config["strategy"] = args.naming

    spec = load_spec(spec_path)
    if args.adapter == "openapi":
        schemas = extract_openapi_schemas(spec, spec_path, naming_config=naming_config)
    elif args.adapter == "raml":
        # RAML adapter doesn't support naming config yet
        schemas = extract_raml_schemas(spec, spec_path)
    else:
        raise ValueError(f"Unknown adapter: {args.adapter}")

    # Log naming strategy used
    strategy = (naming_config or {}).get("strategy", "verbose")
    print(f"Using naming strategy: {strategy}")

    write_schemas(spec_name, schemas)
    update_manifest(spec_name, len(schemas))
    print(f"Wrote {len(schemas)} schemas to ir/{spec_name}/schemas")
    return 0


if __name__ == "__main__":
    sys.exit(main())
