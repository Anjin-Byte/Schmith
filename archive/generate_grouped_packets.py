#!/usr/bin/env python3
"""
Generate grouped prompt packets from IR schemas for Trimble XChange Data Object generation.

This script identifies parent-child schema relationships and generates prompt packets
that include nested types within their parent DataObjects.

Parent-child relationships are detected by:
1. Naming conventions (e.g., CustomerContact is child of Customer)
2. Field references to object/array types
3. Schemas that are only used as nested types (never as operation responses)

Usage:
    python generate_grouped_packets.py <ir_name>
    python generate_grouped_packets.py servicefusion
    python generate_grouped_packets.py servicefusion --schema Customer
    python generate_grouped_packets.py servicefusion --show-groups

Output:
    Creates grouped prompt packets in: ./prompt_packets_grouped/<ir_name>/<ParentName>DataObject.json
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict:
    """Load JSON from a file."""
    with open(path) as f:
        return json.load(f)


def load_ir(ir_path: Path) -> dict:
    """Load all IR data into memory."""
    manifest = load_json(ir_path / "manifest.json")
    schemas_index = load_json(ir_path / "schemas" / "index.json")
    operations_index = load_json(ir_path / "operations" / "index.json")

    return {
        "manifest": manifest,
        "schemas_index": schemas_index,
        "operations_index": operations_index,
        "ir_path": ir_path,
    }


def extract_clean_name(schema_id: str, name_hint: str | None) -> str:
    """Extract a clean name from schema_id or name_hint."""
    if name_hint:
        name = name_hint
        if name.startswith("typ."):
            name = name[4:]
        return name

    if "anon/" in schema_id:
        hash_part = schema_id.split("anon/")[-1][:8]
        return f"Anonymous_{hash_part}"

    return schema_id.split("/")[-1]


def is_error_schema(name: str) -> bool:
    """Check if a schema represents an error response."""
    error_indicators = ["Error", "error", "Exception", "Problem"]
    return any(ind in name for ind in error_indicators)


def is_primitive_schema(schema: dict) -> bool:
    """Check if a schema is a primitive type."""
    kind = schema.get("kind", "")
    primitive_kinds = {"string", "integer", "number", "boolean", "null"}
    name_hint = schema.get("name_hint", "")
    if name_hint in {"string", "integer", "number", "boolean", "object", "array"}:
        return True
    return kind in primitive_kinds


def load_schema_details(ir_path: Path, schema_id: str) -> dict | None:
    """Load detailed schema data from individual schema file."""
    filename = schema_id.replace("schema:", "schema_").replace("/", "_").replace(".", "_") + ".json"
    schema_path = ir_path / "schemas" / filename
    if schema_path.exists():
        return load_json(schema_path)
    return None


def find_parent_child_relationships(schemas: list[dict]) -> dict[str, list[str]]:
    """
    Identify parent-child relationships based on naming conventions.

    Returns a dict mapping parent names to list of child names.
    E.g., {"Customer": ["CustomerContact", "CustomerEmail", ...]}
    """
    # Get all valid schema names (excluding errors, primitives, Body/View variants)
    names = set()
    for schema in schemas:
        name_hint = schema.get("name_hint")
        if not name_hint:
            continue
        name = extract_clean_name(schema["schema_id"], name_hint)
        if is_error_schema(name):
            continue
        if is_primitive_schema(schema):
            continue
        names.add(name)

    # Find potential parent names (base names without suffixes)
    # Skip names ending in Body, View as these are variants not parents
    potential_parents = set()
    for name in names:
        if name.endswith("Body") or name.endswith("View"):
            continue
        potential_parents.add(name)

    # Build parent -> children mapping
    parent_children: dict[str, list[str]] = defaultdict(list)

    for name in names:
        # Skip Body/View variants - they're not children, they're variants
        if name.endswith("Body") or name.endswith("View"):
            continue

        # Check if this name starts with a potential parent name
        for parent in potential_parents:
            if name == parent:
                continue  # Skip self

            # Check if name starts with parent name and has additional suffix
            if name.startswith(parent) and len(name) > len(parent):
                # The suffix should start with uppercase (e.g., CustomerContact, not Customers)
                suffix = name[len(parent):]
                if suffix and suffix[0].isupper():
                    parent_children[parent].append(name)
                    break

    return dict(parent_children)


def get_root_schemas(schemas: list[dict], parent_children: dict[str, list[str]]) -> list[str]:
    """
    Get list of root schema names (schemas that should be top-level DataObjects).

    Root schemas are:
    - Parents with children
    - Schemas that are not children of any parent
    - Excludes Body/View variants
    """
    # Get all children
    all_children = set()
    for children in parent_children.values():
        all_children.update(children)

    # Get all valid schema names
    roots = []
    for schema in schemas:
        name_hint = schema.get("name_hint")
        if not name_hint:
            continue
        name = extract_clean_name(schema["schema_id"], name_hint)

        # Skip errors, primitives
        if is_error_schema(name):
            continue
        if is_primitive_schema(schema):
            continue

        # Skip Body/View variants
        if name.endswith("Body") or name.endswith("View"):
            continue

        # Skip if it's a child
        if name in all_children:
            continue

        roots.append(name)

    return sorted(roots)


# Type mapping from IR schema types to C# types
IR_TO_CSHARP_TYPE = {
    "schema:types/string": "string",
    "schema:types/integer": "int",
    "schema:types/number": "double",
    "schema:types/boolean": "bool",
    "schema:types/datetime": "DateTime",
    "schema:types/date": "DateOnly",
    "schema:types/time": "TimeOnly",
    "schema:types/array": "[]",
    "schema:types/object": "object",
}


def schema_id_to_csharp_type(schema_id: str, schemas_by_id: dict) -> tuple[str, bool]:
    """Convert an IR schema_id to a C# type. Returns (type, is_complex)."""
    if schema_id in IR_TO_CSHARP_TYPE:
        return (IR_TO_CSHARP_TYPE[schema_id], False)

    schema = schemas_by_id.get(schema_id)
    if not schema:
        return ("object", False)

    kind = schema.get("kind", "object")
    if kind == "array":
        items_id = schema.get("items_schema_id")
        if items_id:
            item_type, _ = schema_id_to_csharp_type(items_id, schemas_by_id)
            return (f"{item_type}[]", True)
        return ("object[]", True)

    name_hint = schema.get("name_hint")
    if name_hint:
        clean_name = extract_clean_name(schema_id, name_hint)
        return (clean_name, True)

    if kind in ("string", "integer", "number", "boolean"):
        return (IR_TO_CSHARP_TYPE.get(f"schema:types/{kind}", "object"), False)

    return ("object", False)


def json_name_to_csharp_property(json_name: str) -> str:
    """Convert a JSON field name to a C# property name (PascalCase)."""
    parts = re.split(r"[_\-\s]+", json_name)
    return "".join(part.capitalize() for part in parts if part)


def build_field_info(prop: dict, schemas_by_id: dict, nested_type_names: set[str] | None = None) -> dict:
    """Build field information for a property."""
    json_name = prop.get("json_name", "")
    schema_id = prop.get("schema_id", "")
    description = (prop.get("description") or "").strip()

    csharp_type, is_complex = schema_id_to_csharp_type(schema_id, schemas_by_id)
    csharp_name = json_name_to_csharp_property(json_name)

    # Check if this field should use a nested type
    # If the field name matches a nested type (by convention), use that type
    if nested_type_names and csharp_type == "object":
        # Try to match field name to nested type
        for nested_name in nested_type_names:
            # e.g., field "repeat" might match "CalendarTaskRepeat" -> use "CalendarTaskRepeat"
            if nested_name.lower().endswith(json_name.lower()):
                csharp_type = nested_name
                is_complex = True
                break

    nullable = prop.get("nullable")
    required = prop.get("required", False)
    if not required and nullable is None:
        nullable = True

    return {
        "json_name": json_name,
        "csharp_name": csharp_name,
        "csharp_type": csharp_type,
        "is_complex_type": is_complex,
        "description": description,
        "required": required,
        "nullable": nullable,
        "deprecated": prop.get("deprecated"),
        "schema_id": schema_id,
    }


def build_schema_info(schema: dict, schemas_by_id: dict, nested_type_names: set[str] | None = None) -> dict:
    """Build complete schema info including fields."""
    schema_id = schema.get("id", "")
    name_hint = schema.get("name_hint")
    clean_name = extract_clean_name(schema_id, name_hint)

    fields = []
    for prop in schema.get("properties", []):
        field_info = build_field_info(prop, schemas_by_id, nested_type_names)
        fields.append(field_info)

    # Find primary key
    primary_key = None
    for field in fields:
        if field["json_name"] in ("id", "Id", "ID"):
            primary_key = field["csharp_name"]
            break

    return {
        "schema_id": schema_id,
        "name": clean_name,
        "description": (schema.get("description") or "").strip(),
        "kind": schema.get("kind", "object"),
        "primary_key_field": primary_key,
        "fields": fields,
        "required_fields": schema.get("required", []),
    }


def generate_instructions() -> str:
    """Generate LLM instructions for grouped code generation."""
    return """Generate C# Trimble XChange DataObject classes based on the provided schema information.

This prompt includes a PARENT DataObject with NESTED TYPES that should be defined in the same file.

REQUIREMENTS:
1. Generate the parent DataObject class first, then all nested type classes
2. Use the exact JSON property names from the schema with [JsonPropertyName] attributes
3. Convert JSON field names to PascalCase for C# property names
4. Add [Description] attributes using the field descriptions from the schema
5. Mark required fields with [Required] attribute and use 'required' keyword
6. Mark nullable fields with [Nullable(true)] attribute and use nullable type (e.g., string?)
7. Use 'init' accessors for immutable data objects: { get; init; }
8. Include a [PrimaryKey] attribute on the parent class if an 'id' field exists
9. For nested object fields, use the nested type name (defined below in the same file)
10. For arrays of nested types, use Type[]? syntax

DO NOT:
- Add placeholder comments like "// nested types would go here" or "// define other types similarly"
- Add TODO comments or notes about missing implementations
- Add any explanatory comments - only generate the actual code
- Add [WriteOnly] or [ReadOnly] attributes (PII classification is handled separately)

NAMESPACE PATTERN:
Connector.{ApiName}.v1.{ResourceName}

USINGS:
using Json.Schema.Generation;
using System.Text.Json.Serialization;
using Xchange.Connector.SDK.CacheWriter;

FILE STRUCTURE:
1. Namespace and usings
2. Parent DataObject class (with [PrimaryKey] attribute)
3. Nested type classes (without [PrimaryKey], simpler helper classes)

OUTPUT:
Return ONLY the complete C# code. No markdown, no explanations, no placeholder comments."""


def generate_example_code() -> str:
    """Generate example code pattern."""
    return '''namespace Connector.servicefusion.v1.CalendarTask;

using Json.Schema.Generation;
using System.Text.Json.Serialization;
using Xchange.Connector.SDK.CacheWriter;

[PrimaryKey("id", nameof(Id))]
[Description("A calendar task")]
public class CalendarTaskDataObject
{
    [JsonPropertyName("id")]
    [Description("Task identifier")]
    [Nullable(true)]
    public int? Id { get; init; }

    [JsonPropertyName("description")]
    [Description("Task description")]
    [Nullable(true)]
    public string? Description { get; init; }

    [JsonPropertyName("repeat")]
    [Description("Repeat schedule")]
    [Nullable(true)]
    public CalendarTaskRepeat? Repeat { get; init; }
}

public class CalendarTaskRepeat
{
    [JsonPropertyName("id")]
    [Description("Repeat identifier")]
    [Nullable(true)]
    public int? Id { get; init; }

    [JsonPropertyName("repeat_type")]
    [Description("Type of repeat (Daily, Weekly, etc.)")]
    [Nullable(true)]
    public string? RepeatType { get; init; }
}'''


def build_grouped_prompt_packet(
    parent_name: str,
    child_names: list[str],
    ir_data: dict,
    schemas_by_name: dict[str, dict],
    schemas_by_id: dict[str, dict],
) -> dict | None:
    """Build a grouped prompt packet with parent and nested types."""

    parent_schema_entry = schemas_by_name.get(parent_name)
    if not parent_schema_entry:
        return None

    # Load full parent schema
    parent_schema = load_schema_details(ir_data["ir_path"], parent_schema_entry["schema_id"])
    if not parent_schema:
        return None

    # Get nested type names for field type inference
    nested_type_names = set(child_names)

    # Build parent info
    parent_info = build_schema_info(parent_schema, schemas_by_id, nested_type_names)

    # Build nested types info
    nested_types = []
    for child_name in sorted(child_names):
        child_entry = schemas_by_name.get(child_name)
        if not child_entry:
            continue
        child_schema = load_schema_details(ir_data["ir_path"], child_entry["schema_id"])
        if not child_schema:
            continue
        child_info = build_schema_info(child_schema, schemas_by_id)
        nested_types.append(child_info)

    # Build the packet
    packet = {
        "metadata": {
            "ir_name": ir_data["manifest"].get("spec_name", "unknown"),
            "data_object_name": f"{parent_name}DataObject",
            "is_grouped": True,
            "nested_type_count": len(nested_types),
        },
        "parent": parent_info,
        "nested_types": nested_types,
        "generation": {
            "instructions": generate_instructions(),
            "example_code": generate_example_code(),
        },
    }

    return packet


def main():
    parser = argparse.ArgumentParser(
        description="Generate grouped prompt packets with parent-child relationships.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "ir_name",
        help="Name of the IR to process",
    )
    parser.add_argument(
        "--schema",
        help="Generate packet for a specific parent schema only",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Output directory (default: ./prompt_packets_grouped/<ir_name>)",
    )
    parser.add_argument(
        "--ir-dir",
        type=Path,
        default=None,
        help="Base directory containing IR folders (default: ./ir)",
    )
    parser.add_argument(
        "--show-groups",
        action="store_true",
        help="Show detected parent-child groups and exit",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be generated without writing files",
    )

    args = parser.parse_args()

    # Paths
    script_dir = Path(__file__).parent
    ir_base = args.ir_dir or (script_dir / "ir")
    ir_path = ir_base / args.ir_name

    if not ir_path.exists():
        print(f"Error: IR directory not found: {ir_path}", file=sys.stderr)
        sys.exit(1)

    output_dir = args.output_dir or (script_dir / "prompt_packets_grouped" / args.ir_name)

    # Load IR
    print(f"Loading IR from {ir_path}...")
    ir_data = load_ir(ir_path)

    # Filter to valid schemas
    schemas = [
        s for s in ir_data["schemas_index"]["schemas"]
        if s.get("name_hint")
        and not s.get("is_inline")
        and s.get("kind") == "object"
        and "anon/" not in s.get("schema_id", "")
    ]

    # Build lookups
    schemas_by_name = {}
    schemas_by_id = {}
    for s in ir_data["schemas_index"]["schemas"]:
        name_hint = s.get("name_hint")
        if name_hint:
            clean = extract_clean_name(s["schema_id"], name_hint)
            schemas_by_name[clean] = s
        schemas_by_id[s["schema_id"]] = s

    # Find parent-child relationships
    parent_children = find_parent_child_relationships(schemas)
    root_schemas = get_root_schemas(schemas, parent_children)

    if args.show_groups:
        print("\nDetected Parent-Child Relationships:")
        print("=" * 50)
        for parent in sorted(parent_children.keys()):
            children = parent_children[parent]
            print(f"\n{parent}DataObject:")
            for child in sorted(children):
                print(f"  └── {child}")

        print(f"\n\nRoot Schemas (standalone DataObjects): {len(root_schemas)}")
        print("=" * 50)
        for name in root_schemas:
            if name in parent_children:
                print(f"  {name}DataObject (+ {len(parent_children[name])} nested types)")
            else:
                print(f"  {name}DataObject")
        sys.exit(0)

    # Filter to specific schema if requested
    if args.schema:
        target = args.schema.replace("DataObject", "")
        if target in parent_children or target in root_schemas:
            root_schemas = [target]
        else:
            # Check if it matches any root
            matches = [r for r in root_schemas if target.lower() in r.lower()]
            if matches:
                root_schemas = matches
            else:
                print(f"Error: Schema '{args.schema}' not found", file=sys.stderr)
                sys.exit(1)

    print(f"Processing {len(root_schemas)} root schemas...")

    if not args.dry_run:
        output_dir.mkdir(parents=True, exist_ok=True)

    generated = 0
    for parent_name in root_schemas:
        children = parent_children.get(parent_name, [])

        packet = build_grouped_prompt_packet(
            parent_name,
            children,
            ir_data,
            schemas_by_name,
            schemas_by_id,
        )

        if not packet:
            continue

        name = packet["metadata"]["data_object_name"]
        nested_count = packet["metadata"]["nested_type_count"]

        if args.dry_run:
            if nested_count > 0:
                print(f"  Would generate: {name}.json (+ {nested_count} nested types)")
            else:
                print(f"  Would generate: {name}.json")
        else:
            output_path = output_dir / f"{name}.json"
            with open(output_path, "w") as f:
                json.dump(packet, f, indent=2)
            if nested_count > 0:
                print(f"  Generated: {output_path} (+ {nested_count} nested types)")
            else:
                print(f"  Generated: {output_path}")

        generated += 1

    print(f"\nGenerated {generated} grouped prompt packets")
    if not args.dry_run:
        print(f"Output directory: {output_dir}")


if __name__ == "__main__":
    main()
