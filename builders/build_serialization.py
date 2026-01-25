#!/usr/bin/env python3
"""Build IR serialization indexes.

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
from typing import Any, Dict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from builders.adapters.openapi.serialization import extract_serialization as extract_openapi_serialization
from builders.adapters.raml.serialization import extract_serialization as extract_raml_serialization
from builders.shared.io import load_spec
from pipeline.config import api_name, load_config, resolve_spec_path

CONFIG_DEFAULT = os.path.join(ROOT, "config.toml")


def write_serialization(spec_name: str, media_types: Dict[str, Any], json_paths: Dict[str, Any]) -> None:
    """Write serialization files."""
    base_dir = os.path.join(ROOT, "ir", spec_name, "serialization")
    os.makedirs(base_dir, exist_ok=True)
    with open(os.path.join(base_dir, "media_types.json"), "w", encoding="utf-8") as handle:
        json.dump(media_types, handle, indent=2)
        handle.write("\n")
    with open(os.path.join(base_dir, "json_paths.json"), "w", encoding="utf-8") as handle:
        json.dump(json_paths, handle, indent=2)
        handle.write("\n")


def update_manifest(spec_name: str) -> None:
    """Update the IR manifest (no-op for serialization, just ensures structure)."""
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
    """Main entry point."""
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
