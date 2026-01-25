#!/usr/bin/env python3
"""
List potential Trimble XChange Data Object names from an IR representation.

This script reads an IR (Intermediate Representation) for an API and outputs
the list of schema names that would become XChange Data Objects if mapped.

Usage:
    python list_xchange_objects.py <ir_name>
    python list_xchange_objects.py servicefusion
    python list_xchange_objects.py ukg_v2_client
    python list_xchange_objects.py --list          # List available IRs

Options:
    --list              List available IR names and exit
    --include-errors    Include error response schemas (e.g., 400Error, 404Error)
    --include-primitives Include primitive type schemas (string, integer, etc.)
    --include-anonymous Include anonymous/inline schemas
    --json              Output as JSON instead of plain text
    --verbose           Show additional details about each schema
"""

import argparse
import json
import os
import sys
from pathlib import Path
from typing import NamedTuple


class SchemaInfo(NamedTuple):
    """Information about a schema that could become an XChange object."""
    schema_id: str
    name: str
    kind: str
    is_inline: bool
    usage_count: int


def load_ir_schemas(ir_path: Path) -> list[dict]:
    """Load the schemas index from an IR directory."""
    schemas_index = ir_path / "schemas" / "index.json"
    if not schemas_index.exists():
        raise FileNotFoundError(f"Schemas index not found: {schemas_index}")

    with open(schemas_index) as f:
        data = json.load(f)

    return data.get("schemas", [])


def load_manifest(ir_path: Path) -> dict:
    """Load the manifest from an IR directory."""
    manifest_path = ir_path / "manifest.json"
    if not manifest_path.exists():
        raise FileNotFoundError(f"Manifest not found: {manifest_path}")

    with open(manifest_path) as f:
        return json.load(f)


def extract_object_name(schema: dict) -> str:
    """
    Extract the XChange object name from a schema.

    Naming convention:
    - Use name_hint if available
    - Strip 'typ.' prefix if present (RAML convention)
    - Append 'DataObject' suffix for the class name
    """
    name_hint = schema.get("name_hint")
    if not name_hint:
        # For anonymous schemas, use a hash-based name
        schema_id = schema.get("schema_id", "")
        if "anon/" in schema_id:
            hash_part = schema_id.split("anon/")[-1][:8]
            return f"Anonymous_{hash_part}"
        return schema_id.split("/")[-1]

    # Strip common prefixes
    name = name_hint
    if name.startswith("typ."):
        name = name[4:]

    return name


def is_error_schema(schema: dict) -> bool:
    """Check if a schema represents an error response."""
    name_hint = schema.get("name_hint", "")
    schema_id = schema.get("schema_id", "")

    error_indicators = ["Error", "error", "Exception", "exception", "Problem", "problem"]
    return any(ind in name_hint or ind in schema_id for ind in error_indicators)


def is_primitive_schema(schema: dict) -> bool:
    """Check if a schema is a primitive type."""
    kind = schema.get("kind", "")
    primitive_kinds = {"string", "integer", "number", "boolean", "null"}

    # Also check for schemas that are just wrappers around primitives
    name_hint = schema.get("name_hint", "")
    if name_hint in {"string", "integer", "number", "boolean", "object", "array"}:
        return True

    return kind in primitive_kinds


def filter_schemas(
    schemas: list[dict],
    include_errors: bool = False,
    include_primitives: bool = False,
    include_anonymous: bool = False,
) -> list[SchemaInfo]:
    """
    Filter schemas to get the list of potential XChange objects.

    By default, excludes:
    - Error response schemas
    - Primitive type schemas
    - Anonymous/inline schemas
    """
    results = []

    for schema in schemas:
        schema_id = schema.get("schema_id", "")
        name_hint = schema.get("name_hint")
        kind = schema.get("kind", "unknown")
        is_inline = schema.get("is_inline", False)
        where_used = schema.get("where_used", [])

        # Apply filters
        if not include_anonymous and (is_inline or not name_hint or "anon/" in schema_id):
            continue

        if not include_primitives and is_primitive_schema(schema):
            continue

        if not include_errors and is_error_schema(schema):
            continue

        object_name = extract_object_name(schema)
        results.append(SchemaInfo(
            schema_id=schema_id,
            name=object_name,
            kind=kind,
            is_inline=is_inline,
            usage_count=len(where_used),
        ))

    return results


def format_as_data_object_name(name: str) -> str:
    """Format a schema name as an XChange DataObject class name."""
    # Already ends with DataObject? Return as-is
    if name.endswith("DataObject"):
        return name
    return f"{name}DataObject"


def main():
    parser = argparse.ArgumentParser(
        description="List potential Trimble XChange Data Object names from an IR.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "ir_name",
        nargs="?",
        default=None,
        help="Name of the IR to analyze (e.g., 'servicefusion', 'ukg_v2_client')",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List available IR names and exit",
    )
    parser.add_argument(
        "--include-errors",
        action="store_true",
        help="Include error response schemas",
    )
    parser.add_argument(
        "--include-primitives",
        action="store_true",
        help="Include primitive type schemas",
    )
    parser.add_argument(
        "--include-anonymous",
        action="store_true",
        help="Include anonymous/inline schemas",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output as JSON",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show additional details about each schema",
    )
    parser.add_argument(
        "--ir-dir",
        type=Path,
        default=None,
        help="Base directory containing IR folders (default: ./ir)",
    )

    args = parser.parse_args()

    # Determine IR path
    if args.ir_dir:
        base_dir = args.ir_dir
    else:
        # Default to ./ir relative to this script
        script_dir = Path(__file__).parent
        base_dir = script_dir / "ir"

    # Handle --list option
    if args.list:
        print("Available IRs:")
        if base_dir.exists():
            found = False
            for item in sorted(base_dir.iterdir()):
                if item.is_dir() and (item / "manifest.json").exists():
                    found = True
                    manifest = load_manifest(item)
                    counts = manifest.get("counts", {})
                    print(f"  {item.name}")
                    print(f"    Operations: {counts.get('operations', '?')}")
                    print(f"    Schemas: {counts.get('schemas', '?')}")
            if not found:
                print("  (none found)")
        else:
            print(f"  IR directory not found: {base_dir}")
        sys.exit(0)

    # Require ir_name if not listing
    if not args.ir_name:
        parser.error("ir_name is required (or use --list to see available IRs)")

    ir_path = base_dir / args.ir_name

    if not ir_path.exists():
        print(f"Error: IR directory not found: {ir_path}", file=sys.stderr)
        print(f"\nAvailable IRs in {base_dir}:", file=sys.stderr)
        if base_dir.exists():
            for item in base_dir.iterdir():
                if item.is_dir() and (item / "manifest.json").exists():
                    print(f"  - {item.name}", file=sys.stderr)
        sys.exit(1)

    try:
        manifest = load_manifest(ir_path)
        schemas = load_ir_schemas(ir_path)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    # Filter schemas
    filtered = filter_schemas(
        schemas,
        include_errors=args.include_errors,
        include_primitives=args.include_primitives,
        include_anonymous=args.include_anonymous,
    )

    # Sort by name
    filtered.sort(key=lambda s: s.name.lower())

    # Output
    if args.json:
        output = {
            "ir_name": args.ir_name,
            "total_schemas": manifest.get("counts", {}).get("schemas", 0),
            "filtered_count": len(filtered),
            "xchange_objects": [
                {
                    "data_object_name": format_as_data_object_name(s.name),
                    "schema_name": s.name,
                    "schema_id": s.schema_id,
                    "kind": s.kind,
                    "usage_count": s.usage_count,
                }
                for s in filtered
            ],
        }
        print(json.dumps(output, indent=2))
    else:
        print(f"Trimble XChange Data Objects for '{args.ir_name}'")
        print(f"=" * 50)
        print(f"Total schemas in IR: {manifest.get('counts', {}).get('schemas', 0)}")
        print(f"Data Objects to generate: {len(filtered)}")
        print()

        for schema in filtered:
            data_object_name = format_as_data_object_name(schema.name)
            if args.verbose:
                print(f"  {data_object_name}")
                print(f"    Schema ID: {schema.schema_id}")
                print(f"    Kind: {schema.kind}")
                print(f"    Used in {schema.usage_count} operation(s)")
                print()
            else:
                print(f"  {data_object_name}")


if __name__ == "__main__":
    main()
