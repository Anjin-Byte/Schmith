"""Prompt packet generation for LLM-based code generation.

This module generates "prompt packets" - self-contained JSON files that
provide all the information needed by an LLM to generate C# DataObjects.

Supports two modes:
- Flat packets: One packet per schema
- Grouped packets: Parent with nested child types in one packet
"""

import json
from pathlib import Path
from typing import Any, Iterator

from .ir_loader import IRLoader
from .type_mapping import (
    IR_TO_CSHARP_TYPE,
    build_field_info,
    extract_clean_name,
    format_data_object_name,
    schema_id_to_csharp_type,
)
from .schema_filter import (
    filter_schemas,
    find_parent_child_relationships,
    get_root_schemas,
    is_error_schema,
    is_primitive_schema,
)


def generate_instructions(grouped: bool = False) -> str:
    """Generate LLM instructions for code generation.

    Args:
        grouped: Whether this is for grouped packets with nested types
    """
    base_instructions = """Generate a C# Trimble XChange DataObject class based on the provided schema information.

REQUIREMENTS:
1. Use the exact JSON property names from the schema with [JsonPropertyName] attributes
2. Convert JSON field names to PascalCase for C# property names
3. Add [Description] attributes using the field descriptions from the schema
4. Mark required fields with [Required] attribute and use 'required' keyword
5. Mark nullable fields with [Nullable(true)] attribute and use nullable type (e.g., string?)
6. Use 'init' accessors for immutable data objects: { get; init; }
7. Include a [PrimaryKey] attribute on the class if an 'id' field exists
8. Add XML summary comments for the class
9. Use appropriate C# types:
    - string for text
    - int/long for integers
    - double/decimal for numbers
    - bool for booleans
    - DateTime for datetime fields
    - DateOnly for date-only fields

NAMESPACE PATTERN:
Connector.{ApiName}.v1.{ResourceName}

USINGS:
using Json.Schema.Generation;
using System.Text.Json.Serialization;
using Xchange.Connector.SDK.CacheWriter;

OUTPUT:
Return ONLY the C# code, no explanations or markdown."""

    if grouped:
        return base_instructions + """

This prompt includes a PARENT DataObject with NESTED TYPES that should be defined in the same file.
Generate the parent DataObject class first, then all nested type classes.
For nested object fields, use the nested type name (defined below in the same file).
"""
    return base_instructions


def generate_example_code(grouped: bool = False) -> str:
    """Generate example code pattern for the LLM."""
    if grouped:
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
    [Description("Type of repeat")]
    [Nullable(true)]
    public string? RepeatType { get; init; }
}'''

    return '''namespace Connector.{ApiName}.v1.{ResourceName};

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
}'''


class PromptPacketBuilder:
    """Build prompt packets from IR data.

    Example:
        loader = IRLoader("servicefusion")
        builder = PromptPacketBuilder(loader)

        # Build flat packets
        for packet in builder.build_flat_packets():
            print(packet["metadata"]["data_object_name"])

        # Build grouped packets
        for packet in builder.build_grouped_packets():
            print(packet["metadata"]["data_object_name"])
    """

    def __init__(self, loader: IRLoader):
        """Initialize the builder with an IR loader."""
        self.loader = loader
        self._schemas_by_id: dict[str, dict] | None = None
        self._schemas_by_name: dict[str, dict] | None = None

    @property
    def schemas_by_id(self) -> dict[str, dict]:
        """Get schemas indexed by ID."""
        if self._schemas_by_id is None:
            self._schemas_by_id = self.loader.schemas_by_id()
        return self._schemas_by_id

    @property
    def schemas_by_name(self) -> dict[str, dict]:
        """Get schemas indexed by clean name."""
        if self._schemas_by_name is None:
            self._schemas_by_name = {}
            for s in self.loader.schemas():
                name_hint = s.get("name_hint")
                if name_hint:
                    clean = extract_clean_name(s["schema_id"], name_hint)
                    self._schemas_by_name[clean] = s
        return self._schemas_by_name

    def build_flat_packet(self, schema_id: str) -> dict | None:
        """Build a flat prompt packet for a single schema.

        Args:
            schema_id: The schema ID to build a packet for

        Returns:
            Prompt packet dictionary or None if schema not found
        """
        schema_index_entry = self.schemas_by_id.get(schema_id)
        if not schema_index_entry:
            return None

        # Load full schema details
        schema = self.loader.load_schema_detail(schema_id)
        if not schema:
            return None

        name_hint = schema.get("name_hint")
        clean_name = extract_clean_name(schema_id, name_hint)
        data_object_name = format_data_object_name(clean_name)

        # Build field information
        fields = [
            build_field_info(prop, self.schemas_by_id)
            for prop in schema.get("properties", [])
        ]

        # Find related schemas for nested types
        related = self._find_related_schemas(schema, depth=2)

        # Build related schemas info
        related_info = {}
        for rel_id, rel_schema in related.items():
            rel_name = extract_clean_name(rel_id, rel_schema.get("name_hint"))
            rel_fields = [
                build_field_info(prop, self.schemas_by_id)
                for prop in rel_schema.get("properties", [])
            ]
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

        return {
            "metadata": {
                "schema_id": schema_id,
                "schema_name": clean_name,
                "data_object_name": data_object_name,
                "ir_name": self.loader.spec_name,
                "description": (schema.get("description") or "").strip(),
                "kind": schema.get("kind", "object"),
                "primary_key_field": primary_key_field,
                "is_grouped": False,
            },
            "fields": fields,
            "related_schemas": related_info,
            "generation": {
                "instructions": generate_instructions(grouped=False),
                "example_code": generate_example_code(grouped=False),
            },
        }

    def build_grouped_packet(
        self,
        parent_name: str,
        child_names: list[str],
    ) -> dict | None:
        """Build a grouped prompt packet with parent and nested types.

        Args:
            parent_name: Clean name of the parent schema
            child_names: List of child schema names

        Returns:
            Grouped prompt packet or None if parent not found
        """
        parent_entry = self.schemas_by_name.get(parent_name)
        if not parent_entry:
            return None

        # Load full parent schema
        parent_schema = self.loader.load_schema_detail(parent_entry["schema_id"])
        if not parent_schema:
            return None

        nested_type_names = set(child_names)

        # Build parent info
        parent_info = self._build_schema_info(parent_schema, nested_type_names)

        # Build nested types info
        nested_types = []
        for child_name in sorted(child_names):
            child_entry = self.schemas_by_name.get(child_name)
            if not child_entry:
                continue
            child_schema = self.loader.load_schema_detail(child_entry["schema_id"])
            if not child_schema:
                continue
            child_info = self._build_schema_info(child_schema)
            nested_types.append(child_info)

        return {
            "metadata": {
                "ir_name": self.loader.spec_name,
                "data_object_name": format_data_object_name(parent_name),
                "is_grouped": True,
                "nested_type_count": len(nested_types),
            },
            "parent": parent_info,
            "nested_types": nested_types,
            "generation": {
                "instructions": generate_instructions(grouped=True),
                "example_code": generate_example_code(grouped=True),
            },
        }

    def build_flat_packets(
        self,
        include_errors: bool = False,
    ) -> Iterator[dict]:
        """Build flat prompt packets for all suitable schemas.

        Args:
            include_errors: Include error schemas

        Yields:
            Prompt packet dictionaries
        """
        schemas = filter_schemas(
            self.loader.schemas(),
            include_errors=include_errors,
            include_primitives=False,
            include_anonymous=False,
        )

        for schema_info in schemas:
            packet = self.build_flat_packet(schema_info.schema_id)
            if packet:
                yield packet

    def build_grouped_packets(self) -> Iterator[dict]:
        """Build grouped prompt packets with parent-child relationships.

        Yields:
            Grouped prompt packet dictionaries
        """
        # Get valid schemas for grouping
        valid_schemas = [
            s for s in self.loader.schemas()
            if s.get("name_hint")
            and not s.get("is_inline")
            and s.get("kind") == "object"
            and "anon/" not in s.get("schema_id", "")
        ]

        parent_children = find_parent_child_relationships(valid_schemas)
        root_schemas = get_root_schemas(valid_schemas, parent_children)

        for parent_name in root_schemas:
            children = parent_children.get(parent_name, [])
            packet = self.build_grouped_packet(parent_name, children)
            if packet:
                yield packet

    def _build_schema_info(
        self,
        schema: dict,
        nested_type_names: set[str] | None = None,
    ) -> dict:
        """Build schema info dict for a packet."""
        schema_id = schema.get("id", "")
        name_hint = schema.get("name_hint")
        clean_name = extract_clean_name(schema_id, name_hint)

        fields = [
            build_field_info(prop, self.schemas_by_id, nested_type_names)
            for prop in schema.get("properties", [])
        ]

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
        }

    def _find_related_schemas(
        self,
        schema: dict,
        depth: int = 1,
    ) -> dict[str, dict]:
        """Find schemas referenced by this schema's properties."""
        related: dict[str, dict] = {}

        if depth <= 0:
            return related

        for prop in schema.get("properties", []):
            ref_schema_id = prop.get("schema_id", "")

            # Skip primitives
            if ref_schema_id in IR_TO_CSHARP_TYPE:
                continue

            ref_schema = self.schemas_by_id.get(ref_schema_id)
            if not ref_schema:
                continue

            # Skip inline/anonymous with no useful info
            if ref_schema.get("is_inline") and not ref_schema.get("name_hint"):
                continue

            kind = ref_schema.get("kind", "")

            # Include objects and named types
            if kind == "object" or ref_schema.get("name_hint"):
                details = self.loader.load_schema_detail(ref_schema_id)
                if details:
                    related[ref_schema_id] = details
                    nested = self._find_related_schemas(details, depth - 1)
                    related.update(nested)

            # Handle arrays - get item type
            elif kind == "array":
                items_id = ref_schema.get("items_schema_id")
                if items_id and items_id not in IR_TO_CSHARP_TYPE:
                    items_schema = self.schemas_by_id.get(items_id)
                    if items_schema and items_schema.get("kind") == "object":
                        details = self.loader.load_schema_detail(items_id)
                        if details:
                            related[items_id] = details

        return related


def write_packets(
    packets: Iterator[dict],
    output_dir: Path,
    dry_run: bool = False,
) -> int:
    """Write prompt packets to files.

    Args:
        packets: Iterator of prompt packet dictionaries
        output_dir: Directory to write packets to
        dry_run: If True, don't write files

    Returns:
        Number of packets written
    """
    if not dry_run:
        output_dir.mkdir(parents=True, exist_ok=True)

    count = 0
    for packet in packets:
        name = packet["metadata"]["data_object_name"]
        nested_count = packet["metadata"].get("nested_type_count", 0)

        if dry_run:
            if nested_count > 0:
                print(f"  Would generate: {name}.json (+ {nested_count} nested types)")
            else:
                print(f"  Would generate: {name}.json")
        else:
            output_path = output_dir / f"{name}.json"
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(packet, f, indent=2)
            if nested_count > 0:
                print(f"  Generated: {output_path} (+ {nested_count} nested types)")
            else:
                print(f"  Generated: {output_path}")

        count += 1

    return count
