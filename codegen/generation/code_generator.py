"""Code generation from prompt packets using LLMs.

This module handles the generation of C# code from prompt packets
by calling LLM providers and writing the output files.
"""

import json
from pathlib import Path
from typing import Iterator

from ..providers.llm import LLMProvider, extract_code_from_response
from .manifest import write_manifest

FIELDS_START_MARKER = "// BEGIN_FIELDS"
FIELDS_END_MARKER = "// END_FIELDS"


def format_fields_section(fields: list[dict], indent: str = "  ") -> list[str]:
    """Format a list of fields for the prompt.

    Args:
        fields: List of field info dictionaries
        indent: Indentation string

    Returns:
        List of formatted lines
    """
    lines = []
    for field in fields:
        attrs = []
        if field.get("required"):
            attrs.append("required")
        if field.get("nullable"):
            attrs.append("nullable")
        if field.get("deprecated"):
            attrs.append("deprecated")

        attr_str = f" [{', '.join(attrs)}]" if attrs else ""
        type_str = field["csharp_type"]
        if field.get("nullable") and not type_str.endswith("?"):
            type_str += "?"

        lines.append(f"{indent}{field['json_name']}: {type_str}{attr_str}")
        if field.get("description"):
            lines.append(f"{indent}  Description: {field['description']}")
        enum_values = field.get("enum_values")
        if isinstance(enum_values, list) and enum_values:
            lines.append(f"{indent}  Enum: {', '.join(str(v) for v in enum_values)}")
            enum_names = field.get("enum_names")
            if isinstance(enum_names, list) and enum_names:
                lines.append(f"{indent}  Enum Names: {', '.join(str(v) for v in enum_names)}")
        lines.append("")
    return lines


def _extract_field_block(code: str) -> str:
    """Extract field-only blocks from generated code."""
    if FIELDS_START_MARKER in code and FIELDS_END_MARKER in code:
        start = code.split(FIELDS_START_MARKER, 1)[1]
        return start.split(FIELDS_END_MARKER, 1)[0].strip()
    return code.strip()


def _insert_fields(base_code: str, fields_code: str) -> str:
    """Insert fields before the closing brace of the first class block.

    When a class has enums or other types defined after it, we need to find
    the closing brace of the main class (first block), not the last brace
    in the file.
    """
    # Find the first class's closing brace by tracking brace depth
    depth = 0
    insert_at = -1
    in_first_block = False

    for i, char in enumerate(base_code):
        if char == "{":
            if depth == 0:
                in_first_block = True
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0 and in_first_block:
                # Found the closing brace of the first top-level block
                insert_at = i
                break

    if insert_at == -1:
        return f"{base_code.rstrip()}\n\n{fields_code.strip()}\n"

    before = base_code[:insert_at].rstrip()
    after = base_code[insert_at:]
    return f"{before}\n\n{fields_code.strip()}\n{after.lstrip()}"


def _normalize_class_indentation(code: str, indent: str = "    ") -> str:
    """Ensure member lines inside class braces are indented consistently."""
    lines = code.splitlines()
    out: list[str] = []
    depth = 0
    for line in lines:
        stripped = line.lstrip()
        # Update depth after processing line with opening brace
        if depth > 0 and stripped and not line.startswith(indent):
            if stripped.startswith(("[", "///", "//", "/*", "*", "public", "private", "protected", "internal")):
                line = indent + stripped
        out.append(line)
        # Update depth based on braces in stripped line
        depth += stripped.count("{")
        depth -= stripped.count("}")
        if depth < 0:
            depth = 0
    return "\n".join(out)


def _schema_output_mode(schema: dict, page_index: int) -> str:
    """Determine output mode for a schema/page."""
    if page_index == 1:
        return "class_only" if schema.get("role") == "nested" else "full_class"
    return "fields_only"


def _resolve_namespace(packet_meta: dict, schema: dict) -> str:
    """Resolve namespace for the class based on packet metadata."""
    ir_name = packet_meta.get("ir_name", "api")
    if schema.get("role") == "nested":
        parent_context = schema.get("parent_context", {})
        class_name = parent_context.get("class_name", schema.get("class_name", "DataObject"))
    else:
        class_name = schema.get("class_name", "DataObject")

    resource_name = class_name
    if resource_name.endswith("DataObject"):
        resource_name = resource_name[: -len("DataObject")]

    return f"Connector.{ir_name}.v1.{resource_name}"


def _paging_instructions(output_mode: str, class_name: str) -> list[str]:
    """Build paging-specific instructions (supplements base instructions from prompts.json)."""
    lines = []
    if output_mode == "full_class":
        # Base instructions come from prompts.json, just add paging note
        lines.append("PAGING NOTE:")
        lines.append("- Include only the fields listed for this page.")
    elif output_mode == "class_only":
        lines.append("OUTPUT MODE: class_only")
        lines.append(f"- Return ONLY the class declaration for `{class_name}`.")
        lines.append("- Do NOT include namespace or using statements.")
        lines.append("- Include only the fields listed for this page.")
    else:
        lines.append("OUTPUT MODE: fields_only")
        lines.append("- Return ONLY the property blocks for this page.")
        lines.append("- Do NOT include namespace, using statements, class declaration, or closing braces.")
        lines.append(f"- Wrap properties with `{FIELDS_START_MARKER}` and `{FIELDS_END_MARKER}` markers.")
    return lines


def _paging_example_code(output_mode: str, class_name: str, base_example: str | None) -> str:
    """Generate example code for paging modes, using base example for full_class.

    Args:
        output_mode: The output mode (full_class, class_only, fields_only)
        class_name: The class name for substitution
        base_example: The example_code from prompts.json (used for full_class)
    """
    if output_mode == "fields_only":
        return f"""{FIELDS_START_MARKER}
    [JsonPropertyName("example_field")]
    [Description("Example field")]
    [Nullable(true)]
    public string? ExampleField {{ get; init; }}
{FIELDS_END_MARKER}"""

    if output_mode == "class_only":
        return f"""public class {class_name}
{{
    [JsonPropertyName("example_field")]
    [Description("Example field")]
    [Nullable(true)]
    public string? ExampleField {{ get; init; }}
}}"""

    # full_class mode: use base example from prompts.json
    if base_example:
        return base_example

    # Fallback if no base example provided
    return f"""/// <summary>
/// Example description.
/// </summary>
[PrimaryKey("id", nameof(Id))]
[Description("Example description.")]
public class {class_name}
{{
    [JsonPropertyName("id")]
    [Description("Unique identifier")]
    [Required]
    public required string Id {{ get; init; }}
}}"""


def _related_for_page(fields: list[dict], related_schemas: dict) -> dict:
    """Filter related schemas to the ones referenced by page fields."""
    if not related_schemas:
        return {}

    results: dict[str, dict] = {}
    for name, info in related_schemas.items():
        for field in fields:
            schema_id = field.get("schema_id")
            type_name = (field.get("csharp_type") or "").rstrip("?")
            type_name = type_name[:-2] if type_name.endswith("[]") else type_name
            if schema_id and schema_id == info.get("schema_id"):
                results[name] = info
                break
            if type_name == name:
                results[name] = info
                break
    return results


def _build_paged_prompt(
    packet_meta: dict,
    schema: dict,
    page: dict,
    generation: dict,
) -> str:
    """Build prompt for a single schema page."""
    output_mode = _schema_output_mode(schema, page["page_index"])
    namespace = _resolve_namespace(packet_meta, schema)
    composition_only = set(packet_meta.get("composition_only_types", []))

    lines: list[str] = []

    # Use base instructions from prompts.json
    instructions = generation.get("instructions") if generation else None
    if instructions:
        lines.append(instructions)
        lines.append("")

    # Add paging-specific instructions (supplements, doesn't duplicate)
    paging_instr = _paging_instructions(output_mode, schema["class_name"])
    if paging_instr:
        lines.extend(paging_instr)
        lines.append("")

    lines.append("=" * 60)
    lines.append(f"SCHEMA: {schema['class_name']} ({schema['schema_name']})")
    lines.append("=" * 60)
    lines.append(f"API Name: {packet_meta.get('ir_name')}")
    lines.append(f"Schema ID: {schema.get('schema_id')}")
    lines.append(f"Description: {schema.get('description') or 'No description'}")
    if schema.get("primary_key_field"):
        lines.append(f"Primary Key: {schema['primary_key_field']}")
    lines.append(f"Namespace: {namespace}")
    lines.append(f"Role: {schema.get('role')}")
    enum_values = schema.get("enum_values")
    if isinstance(enum_values, list) and enum_values:
        lines.append("")
        lines.append("ENUM:")
        lines.append(f"  Values: {', '.join(str(v) for v in enum_values)}")
        enum_names = schema.get("enum_names")
        if isinstance(enum_names, list) and enum_names:
            lines.append(f"  Names: {', '.join(str(v) for v in enum_names)}")
    lines.append("")

    lines.append("PAGING:")
    lines.append(f"  Page: {page['page_index']} of {page['page_count']}")
    lines.append(f"  Fields in this page: {page['field_count']}")
    lines.append(f"  Total fields: {schema.get('field_count', 0)}")
    lines.append(f"  All field names: {', '.join(schema.get('field_names', []))}")
    lines.append("")

    parent_context = schema.get("parent_context")
    if parent_context:
        lines.append("PARENT CONTEXT:")
        lines.append(f"  Parent Class: {parent_context.get('class_name')}")
        lines.append(f"  Parent Description: {parent_context.get('description') or 'No description'}")
        lines.append(f"  Parent Field Count: {parent_context.get('field_count', 0)}")
        lines.append(f"  Parent Field Names: {', '.join(parent_context.get('field_names', []))}")
        nested_names = parent_context.get("nested_type_names", [])
        if composition_only and nested_names:
            nested_names = [name for name in nested_names if name not in composition_only]
        if nested_names:
            lines.append(f"  Parent Nested Types: {', '.join(nested_names)}")
        lines.append("")

    nested_type_names = schema.get("nested_type_names", [])
    if composition_only and nested_type_names:
        nested_type_names = [name for name in nested_type_names if name not in composition_only]
    if nested_type_names:
        lines.append(f"NESTED TYPES: {', '.join(nested_type_names)}")
        lines.append("Use these class names for matching nested object fields in this schema.")
        lines.append("")

    lines.append("FIELDS (this page):")
    lines.append("-" * 40)
    lines.extend(format_fields_section(page["fields"]))

    related = _related_for_page(page["fields"], schema.get("related_schemas", {}))
    if related:
        lines.append("")
        lines.append("RELATED TYPES (for nested objects):")
        lines.append("-" * 40)
        for rel_name, rel_info in related.items():
            lines.append(f"\n  {rel_name}:")
            if rel_info.get("description"):
                lines.append(f"    Description: {rel_info['description']}")
            for rf in rel_info.get("fields", [])[:10]:
                rf_attrs = []
                if rf.get("required"):
                    rf_attrs.append("required")
                if rf.get("nullable"):
                    rf_attrs.append("nullable")
                if rf.get("write_only"):
                    rf_attrs.append("PII")
                attr_str = f" [{', '.join(rf_attrs)}]" if rf_attrs else ""
                lines.append(f"      {rf['json_name']}: {rf['csharp_type']}{attr_str}")
            if len(rel_info.get("fields", [])) > 10:
                lines.append(f"      ... and {len(rel_info['fields']) - 10} more fields")

    lines.append("")
    lines.append("EXAMPLE CODE PATTERN:")
    lines.append("-" * 40)
    base_example = generation.get("example_code") if generation else None
    lines.append(_paging_example_code(output_mode, schema["class_name"], base_example))

    return "\n".join(lines)


def _format_prompt_text(packet: dict) -> str:
    """Build a human-readable prompt text for storage."""
    if "schemas" not in packet:
        return build_prompt_from_packet(packet)

    parts: list[str] = []
    for schema, page, _, prompt in _iter_schema_pages(packet):
        header = (
            f"{schema.get('class_name')} ({schema.get('role')}) "
            f"page {page.get('page_index')}/{page.get('page_count')}"
        )
        parts.append("=" * 80)
        parts.append(header)
        parts.append("=" * 80)
        parts.append(prompt)
        parts.append("")
    return "\n".join(parts).strip() + "\n"


def _format_schema_markdown(packet: dict) -> str:
    """Build a simple markdown summary of schema structure."""
    metadata = packet.get("metadata", {})
    lines = [f"# {metadata.get('data_object_name', 'DataObject')}", ""]

    composition_only = set(packet.get("metadata", {}).get("composition_only_types", []))
    for schema in _normalize_packet_schemas(packet):
        lines.append(f"## {schema.get('class_name', 'Schema')}")
        lines.append(f"- Role: {schema.get('role', 'schema')}")
        if schema.get("role") == "nested":
            parent_context = schema.get("parent_context", {})
            parent_name = parent_context.get("class_name", "")
            if parent_name:
                lines.append(f"- Parent: {parent_name}")
        lines.append(f"- Schema Name: {schema.get('schema_name', '')}")
        lines.append(f"- Schema ID: {schema.get('schema_id', '')}")
        if schema.get("primary_key_field"):
            lines.append(f"- Primary Key: {schema['primary_key_field']}")
        lines.append("")
        enum_values = schema.get("enum_values")
        has_enum = isinstance(enum_values, list) and enum_values
        if has_enum:
            lines.append("### Enum")
            lines.append("")
            lines.append(f"Values: {', '.join(str(v) for v in enum_values)}")
            enum_names = schema.get("enum_names")
            if isinstance(enum_names, list) and enum_names:
                lines.append(f"Names: {', '.join(str(v) for v in enum_names)}")
            lines.append("")
        fields = schema.get("fields")
        if not fields:
            fields = []
            for page in schema.get("pages", []):
                fields.extend(page.get("fields", []))
        if has_enum and not fields:
            #lines.append("")
            continue
        lines.append("### Fields")
        if fields:
            lines.append("")
            lines.append("| Field | Type |")
            lines.append("|------|------|")
            for field in fields:
                field_name = field.get("json_name", "")
                field_type = field.get("csharp_type", "")
                lines.append(f"| `{field_name}` | `{field_type}` |")
        lines.append("")

        if schema.get("role") == "parent":
            nested = [name for name in schema.get("nested_type_names", []) if name not in composition_only]
            if nested:
                lines.append("### Nested Types")
                for name in nested:
                    lines.append(f"- `{name}`")
                lines.append("")

    return "\n".join(lines).strip() + "\n"


def _ensure_symlink(link_path: Path, target_path: Path) -> None:
    """Create or replace a symlink to the target path."""
    if link_path.exists() or link_path.is_symlink():
        link_path.unlink()
    try:
        link_path.symlink_to(target_path)
    except OSError:
        # Fallback to copying if symlinks aren't supported.
        link_path.write_text(target_path.read_text(encoding="utf-8"), encoding="utf-8")


def build_prompt_from_packet(packet: dict) -> str:
    """Build the full LLM prompt from a prompt packet.

    This handles legacy packet formats (without 'schemas' key).
    New packets with 'schemas' key should use _iter_schema_pages() instead.

    Args:
        packet: Prompt packet dictionary

    Returns:
        Formatted prompt string
    """
    return _build_grouped_prompt(packet)


def _build_grouped_prompt(packet: dict) -> str:
    """Build prompt for a grouped packet with nested types."""
    metadata = packet["metadata"]
    parent = packet["parent"]
    nested_types = packet.get("nested_types", [])
    generation = packet["generation"]

    lines = []

    # Instructions
    lines.append(generation["instructions"])
    lines.append("")

    # Parent schema
    lines.append("=" * 60)
    lines.append(f"PARENT DATAOBJECT: {metadata['data_object_name']}")
    lines.append("=" * 60)
    lines.append("")
    lines.append(f"API Name: {metadata['ir_name']}")
    lines.append(f"Schema ID: {parent['schema_id']}")
    lines.append(f"Description: {parent['description'] or 'No description'}")
    if parent.get("primary_key_field"):
        lines.append(f"Primary Key: {parent['primary_key_field']}")
    resource_name = metadata["data_object_name"].removesuffix("DataObject")
    lines.append(f"Namespace: Connector.{metadata['ir_name']}.v1.{resource_name}")
    lines.append("")

    lines.append("FIELDS:")
    lines.append("-" * 40)
    lines.extend(format_fields_section(parent["fields"]))

    # Nested types
    if nested_types:
        lines.append("")
        lines.append("=" * 60)
        lines.append("NESTED TYPES (define in same file)")
        lines.append("=" * 60)

        for nested in nested_types:
            lines.append("")
            lines.append(f"CLASS: {nested['name']}")
            lines.append("-" * 40)
            if nested.get("description"):
                lines.append(f"Description: {nested['description']}")
            lines.append("")
            lines.append("FIELDS:")
            lines.extend(format_fields_section(nested["fields"], indent="  "))

    # Example
    lines.append("")
    lines.append("EXAMPLE CODE PATTERN:")
    lines.append("-" * 40)
    lines.append(generation["example_code"])

    return "\n".join(lines)


def _legacy_schema_entry(
    schema_info: dict,
    class_name: str,
    role: str,
    related_schemas: dict | None = None,
    parent_context: dict | None = None,
) -> dict:
    """Normalize legacy schema info into the paged schema format."""
    fields = schema_info.get("fields", [])
    page = {
        "page_index": 1,
        "page_count": 1,
        "field_count": len(fields),
        "fields": fields,
    }
    entry = {
        "schema_id": schema_info.get("schema_id"),
        "schema_name": schema_info.get("schema_name") or schema_info.get("name"),
        "class_name": class_name,
        "description": schema_info.get("description") or "",
        "kind": schema_info.get("kind") or "object",
        "primary_key_field": schema_info.get("primary_key_field"),
        "field_count": len(fields),
        "field_names": [field.get("json_name", "") for field in fields],
        "pages": [page],
        "related_schemas": related_schemas or {},
        "role": role,
    }
    if parent_context:
        entry["parent_context"] = parent_context
    return entry


def _normalize_packet_schemas(packet: dict) -> list[dict]:
    """Return schema entries for paged and legacy grouped packet formats."""
    if "schemas" in packet:
        return packet["schemas"]

    # Handle legacy grouped format (parent/nested_types keys)
    metadata = packet.get("metadata", {})
    parent = packet.get("parent", {})
    nested_types = packet.get("nested_types", [])
    parent_class_name = metadata.get("data_object_name") or parent.get("name", "DataObject")
    parent_entry = _legacy_schema_entry(
        parent,
        class_name=parent_class_name,
        role="parent",
    )
    parent_context = {
        "class_name": parent_entry["class_name"],
        "schema_name": parent_entry["schema_name"],
        "description": parent_entry["description"],
        "field_names": parent_entry["field_names"],
        "field_count": parent_entry["field_count"],
    }

    entries = [parent_entry]
    for nested in nested_types:
        entries.append(
            _legacy_schema_entry(
                nested,
                class_name=nested.get("name", "NestedType"),
                role="nested",
                parent_context=parent_context,
            )
        )
    return entries


def _iter_schema_pages(packet: dict) -> Iterator[tuple[dict, dict, str, str]]:
    """Yield schema/page/output_mode/prompt tuples for a packet."""
    metadata = packet.get("metadata", {})
    generation = packet.get("generation", {})
    composition_only = set(metadata.get("composition_only_types", []))
    for schema in _normalize_packet_schemas(packet):
        if schema.get("role") == "nested" and schema.get("class_name") in composition_only:
            continue
        sources = schema.get("sources") or []
        if schema.get("role") == "nested" and set(sources) == {"composition"}:
            continue
        for page in schema.get("pages", []):
            output_mode = _schema_output_mode(schema, page["page_index"])
            prompt = _build_paged_prompt(metadata, schema, page, generation)
            yield schema, page, output_mode, prompt


def _format_page_status(packet_meta: dict, schema: dict, page: dict) -> str:
    """Format a status line for schema/page processing."""
    data_object = packet_meta.get("data_object_name", "DataObject")
    schema_name = schema.get("class_name", "Schema")
    role = schema.get("role", "schema")
    parent_context = schema.get("parent_context", {})
    parent_name = parent_context.get("class_name") if role == "nested" else None
    field_count = page.get("field_count", 0)
    page_index = page.get("page_index", 1)
    page_count = page.get("page_count", 1)

    if parent_name:
        return (
            f"Processing: {data_object} -> {schema_name} ({role}) "
            f"page {page_index}/{page_count} - {field_count} fields"
        )
    return (
        f"Processing: {data_object} -> {schema_name} ({role}) "
        f"page {page_index}/{page_count} - {field_count} fields"
    )


def generate_from_packet(
    packet: dict,
    provider: LLMProvider,
    show_prompt: bool = False,
) -> str:
    """Generate C# code from a prompt packet.

    Args:
        packet: Prompt packet dictionary
        provider: LLM provider instance
        show_prompt: Print the prompt before generating

    Returns:
        Generated C# code
    """
    if "schemas" not in packet:
        prompt = build_prompt_from_packet(packet)
        if show_prompt:
            print("\n--- PROMPT ---")
            print(prompt[:2000])
            if len(prompt) > 2000:
                print(f"\n... ({len(prompt) - 2000} more characters)")
            print("--- END PROMPT ---\n")
        response = provider.generate(prompt)
        return extract_code_from_response(response)

    schema_outputs: list[str] = []
    for schema in _normalize_packet_schemas(packet):
        page_outputs: list[str] = []
        for page in schema.get("pages", []):
            print(_format_page_status(packet.get("metadata", {}), schema, page))
            prompt = _build_paged_prompt(packet["metadata"], schema, page, packet.get("generation", {}))
            if show_prompt:
                print(
                    f"\n--- PROMPT ({schema['class_name']} page {page['page_index']}/{page['page_count']}) ---"
                )
                print(prompt[:2000])
                if len(prompt) > 2000:
                    print(f"\n... ({len(prompt) - 2000} more characters)")
                print("--- END PROMPT ---\n")

            response = provider.generate(prompt)
            page_outputs.append(extract_code_from_response(response))

        if not page_outputs:
            continue

        class_code = page_outputs[0]
        for extra in page_outputs[1:]:
            fields_block = _extract_field_block(extra)
            class_code = _insert_fields(class_code, fields_block)
        schema_outputs.append(_normalize_class_indentation(class_code).rstrip())

    return "\n\n".join(schema_outputs).rstrip() + "\n"


def generate_from_packets_dir(
    packets_dir: Path,
    output_dir: Path,
    provider: LLMProvider,
    schema_filter: str | None = None,
    limit: int | None = None,
    dry_run: bool = False,
    show_prompt: bool = False,
) -> tuple[int, int]:
    """Generate code from all packets in a directory.

    Args:
        packets_dir: Directory containing prompt packet JSON files
        output_dir: Directory to write generated C# files
        provider: LLM provider instance
        schema_filter: Optional filter for specific schema name
        limit: Optional limit on number of schemas to process
        dry_run: If True, don't call LLM or write files
        show_prompt: Print prompts before generating

    Returns:
        Tuple of (generated_count, error_count)
    """
    # Get list of packets to process
    packet_files = sorted(packets_dir.glob("*.json"))

    if schema_filter:
        target = schema_filter.replace(".json", "")
        if not target.endswith("DataObject"):
            target = f"{target}DataObject"
        packet_files = [f for f in packet_files if target in f.stem]
        if not packet_files:
            raise FileNotFoundError(f"No packet matching '{schema_filter}' found")

    if limit:
        packet_files = packet_files[:limit]

    if not dry_run:
        output_dir.mkdir(parents=True, exist_ok=True)

    generated = 0
    errors = 0

    packets_for_manifest: list[dict] = []

    for packet_file in packet_files:
        with open(packet_file, encoding="utf-8") as f:
            packet = json.load(f)
        packets_for_manifest.append(packet)

        name = packet["metadata"]["data_object_name"]
        print(f"\n{'=' * 60}")
        print(f"Processing: {name}")
        print(f"{'=' * 60}")

        object_dir = output_dir / name
        source_dir = output_dir / "_source"
        schema_dir = output_dir / "_schemas"
        object_dir.mkdir(parents=True, exist_ok=True)
        source_dir.mkdir(parents=True, exist_ok=True)
        schema_dir.mkdir(parents=True, exist_ok=True)
        prompt_text = _format_prompt_text(packet)
        schema_md = _format_schema_markdown(packet)

        prompt_path = object_dir / "prompt.txt"
        schema_path = object_dir / "schema.md"
        schema_target_path = schema_dir / f"{name}.md"
        with open(prompt_path, "w", encoding="utf-8") as f:
            f.write(prompt_text)
        with open(schema_target_path, "w", encoding="utf-8") as f:
            f.write(schema_md)
        _ensure_symlink(schema_path, schema_target_path)

        if dry_run:
            if "schemas" in packet:
                prompts = list(_iter_schema_pages(packet))
                if show_prompt:
                    for schema, page, output_mode, prompt in prompts:
                        print(
                            f"\n--- PROMPT ({schema['class_name']} page {page['page_index']}/{page['page_count']}) ---"
                        )
                        print(prompt[:2000])
                        if len(prompt) > 2000:
                            print(f"\n... ({len(prompt) - 2000} more characters)")
                        print("--- END PROMPT ---\n")
                print(f"  Would generate: _source/{name}.cs (linked in {name}/)")
            else:
                prompt = build_prompt_from_packet(packet)
                if show_prompt:
                    print("\n--- PROMPT ---")
                    print(prompt[:2000])
                    if len(prompt) > 2000:
                        print(f"\n... ({len(prompt) - 2000} more characters)")
                    print("--- END PROMPT ---\n")
                print(f"  Would generate: _source/{name}.cs (linked in {name}/)")
            generated += 1
            continue

        try:
            code = generate_from_packet(packet, provider, show_prompt)
            output_path = source_dir / f"{name}.cs"
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(code)
            _ensure_symlink(object_dir / f"{name}.cs", output_path)
            print(f"  Generated: {output_path}")
            generated += 1
        except Exception as e:
            message = str(e)
            if "429" in message or "insufficient_quota" in message:
                print(f"  Error: {e}")
                print("  Stopping generation due to quota/rate limit error (HTTP 429).")
                errors += 1
                break
            print(f"  Error: {e}")
            errors += 1

    # Write manifest even in dry-run since scaffolding is written above.
    write_manifest(packets_for_manifest, output_dir, packets_dir)

    return generated, errors
