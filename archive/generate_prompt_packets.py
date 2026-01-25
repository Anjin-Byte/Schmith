#!/usr/bin/env python3
"""
Generate prompt packets from IR schemas for Trimble XChange Data Object generation.

This script reads an IR (Intermediate Representation) and generates "prompt packets"
containing all the information needed by an LLM to generate C# XChange Data Objects.

Each prompt packet is a self-contained JSON file that includes:
- Schema metadata (name, description, kind)
- Field definitions with types, descriptions, and attributes
- Related schemas (for nested types)
- Example code patterns
- Instructions for the LLM

Usage:
    python generate_prompt_packets.py <ir_name>
    python generate_prompt_packets.py servicefusion
    python generate_prompt_packets.py servicefusion --schema CustomerDataObject
    python generate_prompt_packets.py servicefusion --output-dir ./packets

Output:
    Creates prompt packets in: ./prompt_packets/<ir_name>/<SchemaName>.json
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any


# Type mapping from IR schema types to C# types
IR_TO_CSHARP_TYPE = {
    "schema:types/string": "string",
    "schema:types/integer": "int",
    "schema:types/number": "double",
    "schema:types/boolean": "bool",
    "schema:types/datetime": "DateTime",
    "schema:types/date": "DateOnly",
    "schema:types/time": "TimeOnly",
    "schema:types/array": "[]",  # Will be combined with items type
    "schema:types/object": "object",
}


def load_json(path: Path) -> dict:
    """Load JSON from a file."""
    with open(path) as f:
        return json.load(f)


def load_ir(ir_path: Path) -> dict:
    """Load all IR data into memory."""
    manifest = load_json(ir_path / "manifest.json")
    schemas_index = load_json(ir_path / "schemas" / "index.json")
    operations_index = load_json(ir_path / "operations" / "index.json")

    # Load adjacency for relationships
    adjacency_path = ir_path / "refs" / "adjacency.json"
    adjacency = load_json(adjacency_path) if adjacency_path.exists() else {}

    return {
        "manifest": manifest,
        "schemas_index": schemas_index,
        "operations_index": operations_index,
        "adjacency": adjacency,
        "ir_path": ir_path,
    }


def extract_clean_name(schema_id: str, name_hint: str | None) -> str:
    """Extract a clean name from schema_id or name_hint."""
    if name_hint:
        # Strip common prefixes
        name = name_hint
        if name.startswith("typ."):
            name = name[4:]
        return name

    # Fall back to parsing schema_id
    if "anon/" in schema_id:
        hash_part = schema_id.split("anon/")[-1][:8]
        return f"Anonymous_{hash_part}"

    return schema_id.split("/")[-1]


def schema_id_to_csharp_type(
    schema_id: str,
    schemas_by_id: dict[str, dict],
    nullable: bool | None = None,
) -> tuple[str, bool]:
    """
    Convert an IR schema_id to a C# type.

    Returns: (csharp_type, is_complex_type)
    """
    # Check primitive types first
    if schema_id in IR_TO_CSHARP_TYPE:
        base_type = IR_TO_CSHARP_TYPE[schema_id]
        return (base_type, False)

    # Look up the schema
    schema = schemas_by_id.get(schema_id)
    if not schema:
        return ("object", False)

    kind = schema.get("kind", "object")

    # Handle arrays
    if kind == "array":
        items_id = schema.get("items_schema_id")
        if items_id:
            item_type, _ = schema_id_to_csharp_type(items_id, schemas_by_id)
            return (f"{item_type}[]", True)
        return ("object[]", True)

    # Handle named complex types
    name_hint = schema.get("name_hint")
    if name_hint:
        clean_name = extract_clean_name(schema_id, name_hint)
        return (clean_name, True)

    # Primitives by kind
    if kind in ("string", "integer", "number", "boolean"):
        return (IR_TO_CSHARP_TYPE.get(f"schema:types/{kind}", "object"), False)

    return ("object", False)


def json_name_to_csharp_property(json_name: str) -> str:
    """Convert a JSON field name to a C# property name (PascalCase)."""
    # Split on underscores and non-alphanumeric
    parts = re.split(r"[_\-\s]+", json_name)
    # Capitalize each part
    return "".join(part.capitalize() for part in parts if part)


def load_schema_details(ir_path: Path, schema_id: str) -> dict | None:
    """Load detailed schema data from individual schema file."""
    # Convert schema_id to filename
    # schema:types/typ.Customer -> schema_types_typ_Customer.json
    # schema:anon/abc123 -> schema_anon_abc123.json
    filename = schema_id.replace("schema:", "schema_").replace("/", "_").replace(".", "_") + ".json"
    schema_path = ir_path / "schemas" / filename

    if schema_path.exists():
        return load_json(schema_path)
    return None


def build_field_info(prop: dict, schemas_by_id: dict[str, dict]) -> dict:
    """Build field information for a property."""
    json_name = prop.get("json_name", "")
    schema_id = prop.get("schema_id", "")
    description = (prop.get("description") or "").strip()

    csharp_type, is_complex = schema_id_to_csharp_type(schema_id, schemas_by_id)
    csharp_name = json_name_to_csharp_property(json_name)

    # Determine nullability
    nullable = prop.get("nullable")
    required = prop.get("required", False)

    # For non-required fields, default to nullable unless explicitly marked
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
        "read_only": prop.get("read_only"),
        "write_only": prop.get("write_only"),
        "deprecated": prop.get("deprecated"),
        "schema_id": schema_id,
    }


def find_related_schemas(
    schema: dict,
    schemas_by_id: dict[str, dict],
    ir_path: Path,
    depth: int = 1,
) -> dict[str, dict]:
    """Find schemas that are referenced by this schema's properties."""
    related = {}

    if depth <= 0:
        return related

    for prop in schema.get("properties", []):
        ref_schema_id = prop.get("schema_id", "")

        # Skip primitives
        if ref_schema_id in IR_TO_CSHARP_TYPE:
            continue

        ref_schema = schemas_by_id.get(ref_schema_id)
        if not ref_schema:
            continue

        # Skip if inline/anonymous with no useful info
        if ref_schema.get("is_inline") and not ref_schema.get("name_hint"):
            continue

        kind = ref_schema.get("kind", "")

        # Include objects and named types
        if kind == "object" or ref_schema.get("name_hint"):
            # Load full details
            details = load_schema_details(ir_path, ref_schema_id)
            if details:
                related[ref_schema_id] = details

                # Recurse for nested types
                nested = find_related_schemas(details, schemas_by_id, ir_path, depth - 1)
                related.update(nested)

        # Handle arrays - get item type
        elif kind == "array":
            items_id = ref_schema.get("items_schema_id")
            if items_id and items_id not in IR_TO_CSHARP_TYPE:
                items_schema = schemas_by_id.get(items_id)
                if items_schema and items_schema.get("kind") == "object":
                    details = load_schema_details(ir_path, items_id)
                    if details:
                        related[items_id] = details

    return related


def generate_example_code() -> str:
    """Generate example code pattern for the LLM."""
    return '''// Example XChange DataObject pattern:
namespace Connector.{ApiName}.v1.{ResourceName};

using Json.Schema.Generation;
using System.Text.Json.Serialization;
using Xchange.Connector.SDK.CacheWriter;

/// <summary>
/// {Description}
/// </summary>
[PrimaryKey("id", nameof({PrimaryKeyProperty}))]
[Description("{Description}")]
public class {ClassName}DataObject
{
    [JsonPropertyName("id")]
    [Description("Unique identifier")]
    [Required]
    public required string Id { get; init; }

    [JsonPropertyName("name")]
    [Description("Display name")]
    [Nullable(true)]
    public string? Name { get; init; }

    [JsonPropertyName("createdAt")]
    [Description("Creation timestamp")]
    [Nullable(true)]
    public DateTime? CreatedAt { get; init; }
}'''


def generate_instructions() -> str:
    """Generate LLM instructions for code generation."""
    return """Generate a C# Trimble XChange DataObject class based on the provided schema information.

REQUIREMENTS:
1. Use the exact JSON property names from the schema with [JsonPropertyName] attributes
2. Convert JSON field names to PascalCase for C# property names
3. Add [Description] attributes using the field descriptions from the schema
4. Mark required fields with [Required] attribute and use 'required' keyword
5. Mark nullable fields with [Nullable(true)] attribute and use nullable type (e.g., string?)
6. Mark read-only fields with [ReadOnly] attribute
7. Mark write-only/sensitive fields with [WriteOnly] attribute (PII like names, emails, addresses)
8. Use 'init' accessors for immutable data objects: { get; init; }
9. Include a [PrimaryKey] attribute on the class if an 'id' field exists
10. Add XML summary comments for the class
11. Use appropriate C# types:
    - string for text
    - int/long for integers
    - double/decimal for numbers
    - bool for booleans
    - DateTime for datetime fields
    - DateOnly for date-only fields
12. For nested objects, reference the related type (generate inline if simple, or reference if complex)
13. For arrays, use the appropriate array type (e.g., Contact[]?)

NAMESPACE PATTERN:
Connector.{ApiName}.v1.{ResourceName}

USINGS:
using Json.Schema.Generation;
using System.Text.Json.Serialization;
using Xchange.Connector.SDK.CacheWriter;

OUTPUT:
Return ONLY the C# code, no explanations or markdown."""


def build_prompt_packet(
    schema_id: str,
    ir_data: dict,
    schemas_by_id: dict[str, dict],
) -> dict | None:
    """Build a complete prompt packet for a schema."""
    schema_index_entry = schemas_by_id.get(schema_id)
    if not schema_index_entry:
        return None

    # Load full schema details
    schema = load_schema_details(ir_data["ir_path"], schema_id)
    if not schema:
        return None

    name_hint = schema.get("name_hint")
    clean_name = extract_clean_name(schema_id, name_hint)
    data_object_name = f"{clean_name}DataObject"

    # Build field information
    fields = []
    for prop in schema.get("properties", []):
        field_info = build_field_info(prop, schemas_by_id)
        fields.append(field_info)

    # Find related schemas for nested types
    related = find_related_schemas(schema, schemas_by_id, ir_data["ir_path"], depth=2)

    # Build related schemas info (simplified for prompt)
    related_info = {}
    for rel_id, rel_schema in related.items():
        rel_name = extract_clean_name(rel_id, rel_schema.get("name_hint"))
        rel_fields = []
        for prop in rel_schema.get("properties", []):
            rel_fields.append(build_field_info(prop, schemas_by_id))
        related_info[rel_name] = {
            "schema_id": rel_id,
            "description": (rel_schema.get("description") or "").strip(),
            "fields": rel_fields,
        }

    # Determine primary key candidate
    primary_key_field = None
    for field in fields:
        if field["json_name"] in ("id", "Id", "ID"):
            primary_key_field = field["csharp_name"]
            break

    # Build the packet
    packet = {
        "metadata": {
            "schema_id": schema_id,
            "schema_name": clean_name,
            "data_object_name": data_object_name,
            "ir_name": ir_data["manifest"].get("spec_name", "unknown"),
            "description": (schema.get("description") or "").strip(),
            "kind": schema.get("kind", "object"),
            "primary_key_field": primary_key_field,
        },
        "fields": fields,
        "related_schemas": related_info,
        "generation": {
            "instructions": generate_instructions(),
            "example_code": generate_example_code(),
        },
    }

    return packet


def is_error_schema(schema: dict) -> bool:
    """Check if a schema represents an error response."""
    name_hint = schema.get("name_hint", "")
    schema_id = schema.get("schema_id", "")
    error_indicators = ["Error", "error", "Exception", "exception", "Problem"]
    return any(ind in name_hint or ind in schema_id for ind in error_indicators)


def is_primitive_schema(schema: dict) -> bool:
    """Check if a schema is a primitive type."""
    kind = schema.get("kind", "")
    primitive_kinds = {"string", "integer", "number", "boolean", "null"}
    name_hint = schema.get("name_hint", "")
    if name_hint in {"string", "integer", "number", "boolean", "object", "array"}:
        return True
    return kind in primitive_kinds


def filter_schemas_for_generation(schemas: list[dict]) -> list[dict]:
    """Filter schemas to only those suitable for DataObject generation."""
    filtered = []
    for schema in schemas:
        schema_id = schema.get("schema_id", "")
        name_hint = schema.get("name_hint")
        is_inline = schema.get("is_inline", False)

        # Skip anonymous/inline schemas
        if is_inline or not name_hint or "anon/" in schema_id:
            continue

        # Skip primitives
        if is_primitive_schema(schema):
            continue

        # Skip errors
        if is_error_schema(schema):
            continue

        # Only include objects
        if schema.get("kind") != "object":
            continue

        filtered.append(schema)

    return filtered


def main():
    parser = argparse.ArgumentParser(
        description="Generate prompt packets from IR schemas for XChange DataObject generation.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "ir_name",
        help="Name of the IR to process (e.g., 'servicefusion', 'ukg_v2_client')",
    )
    parser.add_argument(
        "--schema",
        help="Generate packet for a specific schema only (e.g., 'CustomerDataObject' or 'Customer')",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Output directory for prompt packets (default: ./prompt_packets/<ir_name>)",
    )
    parser.add_argument(
        "--ir-dir",
        type=Path,
        default=None,
        help="Base directory containing IR folders (default: ./ir)",
    )
    parser.add_argument(
        "--include-errors",
        action="store_true",
        help="Include error response schemas",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would be generated without writing files",
    )

    args = parser.parse_args()

    # Determine paths
    script_dir = Path(__file__).parent
    ir_base = args.ir_dir or (script_dir / "ir")
    ir_path = ir_base / args.ir_name

    if not ir_path.exists():
        print(f"Error: IR directory not found: {ir_path}", file=sys.stderr)
        sys.exit(1)

    output_dir = args.output_dir or (script_dir / "prompt_packets" / args.ir_name)

    # Load IR data
    print(f"Loading IR from {ir_path}...")
    ir_data = load_ir(ir_path)

    # Build schema lookup
    schemas_by_id = {s["schema_id"]: s for s in ir_data["schemas_index"]["schemas"]}

    # Determine which schemas to process
    schemas_to_process = ir_data["schemas_index"]["schemas"]

    if args.schema:
        # Find specific schema
        target = args.schema.replace("DataObject", "")
        matches = [
            s for s in schemas_to_process
            if target.lower() in extract_clean_name(s["schema_id"], s.get("name_hint")).lower()
        ]
        if not matches:
            print(f"Error: No schema matching '{args.schema}' found", file=sys.stderr)
            sys.exit(1)
        schemas_to_process = matches
    else:
        # Filter to suitable schemas
        schemas_to_process = filter_schemas_for_generation(schemas_to_process)
        if args.include_errors:
            # Re-add error schemas
            error_schemas = [
                s for s in ir_data["schemas_index"]["schemas"]
                if is_error_schema(s) and s.get("kind") == "object"
            ]
            schemas_to_process.extend(error_schemas)

    print(f"Processing {len(schemas_to_process)} schemas...")

    # Create output directory
    if not args.dry_run:
        output_dir.mkdir(parents=True, exist_ok=True)

    # Generate packets
    generated = 0
    for schema_entry in schemas_to_process:
        schema_id = schema_entry["schema_id"]
        packet = build_prompt_packet(schema_id, ir_data, schemas_by_id)

        if not packet:
            continue

        name = packet["metadata"]["data_object_name"]

        if args.dry_run:
            print(f"  Would generate: {name}.json")
        else:
            output_path = output_dir / f"{name}.json"
            with open(output_path, "w") as f:
                json.dump(packet, f, indent=2)
            print(f"  Generated: {output_path}")

        generated += 1

    print(f"\nGenerated {generated} prompt packets")
    if not args.dry_run:
        print(f"Output directory: {output_dir}")


if __name__ == "__main__":
    main()
