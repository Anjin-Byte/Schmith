"""Prompt packet generation for LLM-based code generation.

This module generates "prompt packets" - self-contained JSON files that
provide all the information needed by an LLM to generate C# DataObjects.

Supports two modes:
- Flat packets: One packet per schema
- Grouped packets: Parent with nested child types in one packet
"""

import json
import math
from pathlib import Path
from typing import Iterator

from .composition import CompositionResolver
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
    find_parent_child_relationships_from_ir,
    find_reachable_component_names,
    get_root_schemas,
    is_error_schema,
    is_primitive_schema,
    is_variant_schema,
)


_PROMPT_CACHE: dict[str, str] | None = None


def _load_prompt_texts() -> dict[str, str]:
    """Load prompt text from the prompts.json file."""
    global _PROMPT_CACHE
    if _PROMPT_CACHE is not None:
        return _PROMPT_CACHE

    prompt_path = Path(__file__).parent / "prompts.json"
    if prompt_path.exists():
        with open(prompt_path, encoding="utf-8") as f:
            _PROMPT_CACHE = json.load(f)
            return _PROMPT_CACHE

    _PROMPT_CACHE = {}
    return _PROMPT_CACHE


def generate_instructions(grouped: bool = False) -> str:
    """Generate base LLM instructions for code generation."""
    prompts = _load_prompt_texts()
    instructions = prompts.get("instructions")
    if instructions:
        if isinstance(instructions, list):
            return "\n".join(instructions)
        return instructions
    return """Generate a C# Trimble XChange DataObject class based on the provided schema information.

REQUIREMENTS:
1. Use the exact JSON property names from the schema with [JsonPropertyName] attributes
2. Convert JSON field names to PascalCase for C# property names
3. Add [Description] attributes using the field descriptions from the schema
4. Mark required fields with [Required] attribute and use 'required' keyword
5. Mark nullable fields with [Nullable(true)] attribute and use nullable type (e.g., string?)
6. Use 'init' accessors for immutable data objects: { get; init; }
7. Include a [PrimaryKey("id", nameof(Id))] attribute ONLY on the main DataObject class (the one ending in 'DataObject') if an 'id' field exists. Do NOT add [PrimaryKey] to nested/helper types.
8. Add XML summary comments for the class
9. Use appropriate C# types:
    - string for text
    - int/long for integers
    - double/decimal for numbers
    - bool for booleans
    - DateTime for datetime fields
    - DateOnly for date-only fields

OUTPUT:
Return ONLY the C# code, no explanations or markdown."""


def generate_example_code(grouped: bool = False) -> str:
    """Generate example code pattern for the LLM."""
    prompts = _load_prompt_texts()
    example_code = prompts.get("example_code")
    if example_code:
        if isinstance(example_code, list):
            return "\n".join(example_code)
        return example_code
    return '''/// <summary>
/// {Description}
/// </summary>
[PrimaryKey("id", nameof({PrimaryKeyProperty}))]
[Description("{Description}")]
public class {ClassName}
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

    def __init__(self, loader: IRLoader, max_fields_per_page: int = 10):
        """Initialize the builder with an IR loader."""
        self.loader = loader
        self.max_fields_per_page = max_fields_per_page
        self._schemas_by_id: dict[str, dict] | None = None
        self._schemas_by_name: dict[str, dict] | None = None
        self._composition_resolver: CompositionResolver | None = None

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

    @property
    def composition_resolver(self) -> CompositionResolver:
        """Get the composition resolver, creating it lazily."""
        if self._composition_resolver is None:
            self._composition_resolver = CompositionResolver(
                self.loader.load_schema_detail,
                self.schemas_by_id,
            )
        return self._composition_resolver

    def _paginate_fields(self, fields: list[dict]) -> list[list[dict]]:
        """Split fields into evenly sized pages with a max cap."""
        if not fields:
            return [[]]

        max_fields = self.max_fields_per_page if self.max_fields_per_page > 0 else len(fields)
        if len(fields) <= max_fields:
            return [fields]

        page_count = math.ceil(len(fields) / max_fields)
        base_size = len(fields) // page_count
        remainder = len(fields) % page_count

        pages: list[list[dict]] = []
        index = 0
        for i in range(page_count):
            size = base_size + (1 if i < remainder else 0)
            pages.append(fields[index : index + size])
            index += size
        return pages

    def _build_pages(self, fields: list[dict]) -> list[dict]:
        """Build page dictionaries with pagination metadata."""
        pages = self._paginate_fields(fields)
        page_count = len(pages)
        return [
            {
                "page_index": i + 1,
                "page_count": page_count,
                "field_count": len(page_fields),
                "fields": page_fields,
            }
            for i, page_fields in enumerate(pages)
        ]

    def _build_related_info(self, schema: dict) -> dict[str, dict]:
        """Build related schema info for nested object fields."""
        related = self._find_related_schemas(schema, depth=2)
        related_info: dict[str, dict] = {}
        for rel_id, rel_schema in related.items():
            rel_name = extract_clean_name(rel_id, rel_schema.get("name_hint"))
            # Resolve properties including composition for related schemas
            rel_resolved, _ = self.composition_resolver.resolve_properties(rel_schema)
            rel_fields = [
                build_field_info(prop, self.schemas_by_id)
                for prop in rel_resolved
            ]
            related_info[rel_name] = {
                "schema_id": rel_id,
                "description": (rel_schema.get("description") or "").strip(),
                "fields": rel_fields,
            }
        return related_info

    def _build_schema_packet(
        self,
        schema: dict,
        class_name: str,
        role: str,
        nested_type_names: set[str] | None = None,
        parent_context: dict | None = None,
    ) -> dict:
        """Build a schema packet with paged fields and context."""
        schema_id = schema.get("id", "")
        name_hint = schema.get("name_hint")
        clean_name = extract_clean_name(schema_id, name_hint)

        # Resolve properties including composition (allOf)
        resolved_properties, _ = self.composition_resolver.resolve_properties(schema)

        fields = [
            build_field_info(prop, self.schemas_by_id, nested_type_names)
            for prop in resolved_properties
        ]

        # Find primary key using cascading detection:
        # 1. Prefer field named 'id' (if non-nullable)
        # 2. Fall back to first required field
        # 3. Fall back to first explicitly non-nullable field
        # 4. If all fail, flag for LLM selection
        primary_key = None
        primary_key_needs_selection = False

        # Step 1: Look for 'id' field
        for field in fields:
            if field["json_name"] in ("id", "Id", "ID") and not field.get("nullable"):
                primary_key = field["csharp_name"]
                break

        # Step 2: Fall back to first required field
        if not primary_key:
            for field in fields:
                if field.get("required") and not field.get("nullable"):
                    primary_key = field["csharp_name"]
                    break

        # Step 3: Fall back to first explicitly non-nullable field
        if not primary_key:
            for field in fields:
                if field.get("nullable") is False:
                    primary_key = field["csharp_name"]
                    break

        # Step 4: Flag for LLM selection if no suitable field found
        if not primary_key and fields:
            primary_key_needs_selection = True

        pages = self._build_pages(fields)

        # Build related schemas info, but exclude types that will be generated
        # as nested types (to avoid duplicate class definitions in output)
        related_schemas = self._build_related_info(schema)
        if nested_type_names:
            related_schemas = {
                name: info
                for name, info in related_schemas.items()
                if name not in nested_type_names
            }

        packet = {
            "schema_id": schema_id,
            "schema_name": clean_name,
            "class_name": class_name,
            "description": (schema.get("description") or "").strip(),
            "kind": schema.get("kind", "object"),
            "primary_key_field": primary_key,
            "primary_key_needs_selection": primary_key_needs_selection,
            "field_count": len(fields),
            "field_names": [field["json_name"] for field in fields],
            "pages": pages,
            "related_schemas": related_schemas,
            "role": role,
        }

        if nested_type_names:
            packet["nested_type_names"] = sorted(nested_type_names)

        if parent_context:
            packet["parent_context"] = parent_context

        return packet

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

        schema_packet = self._build_schema_packet(
            schema,
            class_name=data_object_name,
            role="flat",
        )

        return {
            "metadata": {
                "schema_id": schema_id,
                "schema_name": clean_name,
                "data_object_name": data_object_name,
                "ir_name": self.loader.spec_name,
                "description": schema_packet["description"],
                "kind": schema_packet["kind"],
                "primary_key_field": schema_packet.get("primary_key_field"),
                "field_count": schema_packet["field_count"],
                "page_count": len(schema_packet["pages"]),
                "max_fields_per_page": self.max_fields_per_page,
                "is_grouped": False,
            },
            "schemas": [schema_packet],
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
        parent_class_name = format_data_object_name(parent_name)

        # Build parent schema packet
        parent_info = self._build_schema_packet(
            parent_schema,
            class_name=parent_class_name,
            role="parent",
            nested_type_names=nested_type_names,
        )

        parent_context = {
            "class_name": parent_info["class_name"],
            "schema_name": parent_info["schema_name"],
            "description": parent_info["description"],
            "field_names": parent_info["field_names"],
            "field_count": parent_info["field_count"],
            "nested_type_names": sorted(nested_type_names),
        }

        # Build nested types info
        nested_types = []
        for child_name in sorted(child_names):
            child_entry = self.schemas_by_name.get(child_name)
            if not child_entry:
                continue
            child_schema = self.loader.load_schema_detail(child_entry["schema_id"])
            if not child_schema:
                continue
            child_info = self._build_schema_packet(
                child_schema,
                class_name=child_name,
                role="nested",
                parent_context=parent_context,
            )
            nested_types.append(child_info)

        return {
            "metadata": {
                "ir_name": self.loader.spec_name,
                "data_object_name": parent_class_name,
                "is_grouped": True,
                "schema_count": 1 + len(nested_types),
                "nested_type_count": len(nested_types),
                "max_fields_per_page": self.max_fields_per_page,
            },
            "schemas": [parent_info] + nested_types,
            "generation": {
                "instructions": generate_instructions(grouped=True),
                "example_code": generate_example_code(grouped=True),
            },
        }

    def build_flat_packets(
        self,
        include_errors: bool = False,
        only_reachable: bool = True,
    ) -> Iterator[dict]:
        """Build flat prompt packets for all suitable schemas.

        Args:
            include_errors: Include error schemas
            only_reachable: Only include schemas reachable from operations (default True).
                This filters out orphan schemas that are not used by any operation
                and are not referenced by any schema that is used by an operation.
                Uses BFS traversal from operation-used schemas through the adjacency graph.

        Yields:
            Prompt packet dictionaries
        """
        # Find all schemas reachable from operations
        reachable_names: set[str] | None = None
        if only_reachable:
            adjacency = self.loader.adjacency()
            operations = self.loader.operations()
            reachable_names = find_reachable_component_names(
                operations, adjacency, self.schemas_by_id
            )

        schemas = filter_schemas(
            self.loader.schemas(),
            include_errors=include_errors,
            include_primitives=False,
            include_anonymous=False,
            include_orphans=True,  # We handle orphan filtering via reachability
        )

        for schema_info in schemas:
            # Filter to only reachable schemas
            if reachable_names is not None and schema_info.name not in reachable_names:
                continue
            packet = self.build_flat_packet(schema_info.schema_id)
            if packet:
                yield packet

    def build_grouped_packets(
        self,
        exclude_variants: bool = True,
        only_reachable: bool = True,
    ) -> Iterator[dict]:
        """Build grouped prompt packets with parent-child relationships.

        Args:
            exclude_variants: Exclude Body/View variants from grouping (default True)
            only_reachable: Only include schemas reachable from operations (default True).
                This filters out orphan schemas that are not used by any operation
                and are not referenced by any schema that is used by an operation.

        Yields:
            Grouped prompt packet dictionaries
        """
        # Load adjacency data and operations
        adjacency = self.loader.adjacency()
        operations = self.loader.operations()

        # Find all schemas reachable from operations via the adjacency graph
        reachable_names: set[str] | None = None
        if only_reachable:
            reachable_names = find_reachable_component_names(
                operations, adjacency, self.schemas_by_id
            )

        # Get valid schemas for grouping
        valid_schemas = [
            s for s in self.loader.schemas()
            if s.get("name_hint")
            and not s.get("is_inline")
            and s.get("kind") == "object"
            and "anon/" not in s.get("schema_id", "")
        ]

        # Filter to only reachable schemas
        if reachable_names is not None:
            valid_schemas = [
                s for s in valid_schemas
                if extract_clean_name(s["schema_id"], s.get("name_hint")) in reachable_names
            ]

        # Filter out Body/View variants - they shouldn't be grouped with DataObjects
        if exclude_variants:
            valid_schemas = [
                s for s in valid_schemas
                if not is_variant_schema(
                    extract_clean_name(s["schema_id"], s.get("name_hint"))
                )
            ]

        # Use IR adjacency data for accurate parent-child relationships
        # Pass reachable_names to filter relationships to only include reachable schemas
        parent_children = find_parent_child_relationships_from_ir(
            adjacency, self.schemas_by_id, reachable_names
        )
        root_schemas = get_root_schemas(valid_schemas, parent_children)

        for parent_name in root_schemas:
            children = parent_children.get(parent_name, [])
            packet = self.build_grouped_packet(parent_name, children)
            if packet:
                yield packet

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

            kind = ref_schema.get("kind", "")

            # Skip inline/anonymous with no useful info (but allow arrays
            # so we can follow their items_schema_id to find nested types)
            if ref_schema.get("is_inline") and not ref_schema.get("name_hint"):
                if kind != "array":
                    continue

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
