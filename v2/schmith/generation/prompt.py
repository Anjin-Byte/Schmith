"""Prompt packet builder for single-endpoint DataObject generation.

Responsibilities:
- build_prompt_packet: assemble the structured data packet that captures
  everything the LLM needs (schema info, field types, endpoint context).
- build_system_prompt: load generation instructions from prompts.json.
- build_user_prompt: format the packet into the user-facing LLM message.
- format_schema_markdown: produce the schema.md artefact for human review.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from schmith.generation.type_mapping import (
    build_field_info,
    format_data_object_name,
    json_name_to_csharp_property,
)
from schmith.ir.models import Endpoint

_PROMPTS_PATH = Path(__file__).parent / "prompts.json"

# Maximum number of fields to include per page when a type is large.
# If a type exceeds this, its fields are chunked so each LLM call stays
# manageable.  The results are stitched back together by the caller.
MAX_FIELDS_PER_PAGE = 6
MAX_ENUM_VALUES_PER_PAGE = 30


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _load_prompts() -> dict[str, Any]:
    with open(_PROMPTS_PATH, encoding="utf-8") as f:
        return json.load(f)


def _join_lines(value: str | list[str]) -> str:
    """Normalise a prompts.json value that may be a list of lines or a string."""
    if isinstance(value, list):
        return "\n".join(value)
    return value


def _process_type(type_entry: dict[str, Any], schemas_by_id: dict[str, dict[str, Any]]) -> dict[str, Any]:
    """Convert a raw type_tree entry into a prompt-ready dict with field infos."""
    raw_props: list[dict[str, Any]] = type_entry.get("properties") or []
    fields: list[dict[str, Any]] = [build_field_info(prop, schemas_by_id) for prop in raw_props]

    # The type tree assigns names to anonymous schemas during traversal and
    # stores them as `resolved_type` on each property.  build_field_info works
    # from schemas_by_id, which only has name_hint values from the original spec
    # — it cannot see names the type tree created.  Override csharp_type with
    # the type-tree name whenever build_field_info left the type unresolved.
    for field, prop in zip(fields, raw_props):
        resolved_type = prop.get("resolved_type")
        if (
            resolved_type
            and not resolved_type.startswith("schema:")
            and field.get("type_unresolved")
        ):
            field["csharp_type"] = resolved_type
            field["is_complex_type"] = True
            field["type_unresolved"] = False

    return {
        "name": type_entry.get("name", "UnknownType"),
        "schema_id": type_entry.get("schema_id", ""),
        "description": type_entry.get("description") or "",
        "kind": type_entry.get("kind", "object"),
        "fields": fields,
        "enum_values": type_entry.get("enum_values"),
        "enum_names": type_entry.get("enum_names"),
        "is_inline": type_entry.get("is_inline", False),
    }


def _format_fields_section(fields: list[dict[str, Any]], indent: str = "  ") -> list[str]:
    """Format a list of field info dicts into human-readable prompt lines."""
    lines: list[str] = []
    for field in fields:
        attrs = []
        if field.get("required"):
            attrs.append("required")
        if field.get("nullable"):
            attrs.append("nullable")
        if field.get("deprecated"):
            attrs.append("deprecated")
        if field.get("read_only"):
            attrs.append("read-only")
        if field.get("write_only"):
            attrs.append("write-only")
        if field.get("type_unresolved"):
            attrs.append("type_unresolved")

        attr_str = f" [{', '.join(attrs)}]" if attrs else ""
        type_str = field["csharp_type"]
        if field.get("nullable") and not type_str.endswith("?"):
            type_str += "?"

        json_name = field["json_name"]
        csharp_name = field.get("csharp_name", "")
        # Always include the computed C# property name so the LLM doesn't have
        # to derive it — especially important for %{...} template keys which
        # require our custom sanitisation logic.
        name_str = f"{json_name} [→ {csharp_name}]" if csharp_name else json_name
        lines.append(f"{indent}{name_str}: {type_str}{attr_str}")
        if field.get("description"):
            lines.append(f"{indent}  Description: {field['description']}")
        enum_values = field.get("enum_values")
        if isinstance(enum_values, list) and enum_values:
            lines.append(f"{indent}  Enum: {', '.join(str(v) for v in enum_values)}")
            enum_names = field.get("enum_names")
            if isinstance(enum_names, list) and enum_names:
                lines.append(f"{indent}  Enum Names: {', '.join(str(v) for v in enum_names)}")
        constraints = field.get("constraints") or {}
        if constraints:
            parts = [f"{k}={v}" for k, v in constraints.items()]
            lines.append(f"{indent}  Constraints: {', '.join(parts)}")
        lines.append("")
    return lines


# ---------------------------------------------------------------------------
# Pagination helpers
# ---------------------------------------------------------------------------

# Marker strings used to delimit extra field blocks in paged LLM responses.
# The LLM is instructed to wrap fields_only pages with these markers so they
# can be extracted and stitched into the base class output.
FIELDS_START_MARKER = "// BEGIN_FIELDS"
FIELDS_END_MARKER = "// END_FIELDS"


def _output_mode(is_root: bool, page_index: int, is_enum: bool) -> str:
    if is_enum:
        return "enum_only" if page_index == 1 else "enum_values_only"
    if page_index == 1:
        return "full_class" if is_root else "class_only"
    return "fields_only"


def _paging_instructions(output_mode: str, class_name: str) -> list[str]:
    """Build mode-specific instructions that supplement the base system prompt."""
    lines: list[str] = []
    if output_mode == "enum_only":
        lines.append("OUTPUT MODE: enum_only")
        lines.append("- This schema defines a standalone enum, NOT a class.")
        lines.append(f"- Return ONLY a standalone enum definition named `{class_name}`.")
        lines.append("- Add [JsonConverter(typeof(JsonStringEnumConverter))] to the enum.")
        lines.append('- Add [JsonStringEnumMemberName("value")] to each enum member.')
        lines.append("- Do NOT wrap the enum in a class.")
        lines.append("- Do NOT include namespace or using statements.")
    elif output_mode == "full_class":
        lines.append("PAGING NOTE:")
        lines.append("- Include only the fields listed for this page.")
    elif output_mode == "class_only":
        lines.append("OUTPUT MODE: class_only")
        lines.append(f"- Return ONLY the class declaration for `{class_name}`.")
        lines.append("- Do NOT include namespace or using statements.")
        lines.append("- Include only the fields listed for this page.")
    elif output_mode == "enum_values_only":
        lines.append("OUTPUT MODE: enum_values_only")
        lines.append("- Return ONLY the enum members for this page.")
        lines.append(
            "- Do NOT include the enum declaration, namespace, or using statements."
        )
        lines.append(
            f"- Wrap members with `{FIELDS_START_MARKER}` and `{FIELDS_END_MARKER}` markers."
        )
        lines.append('- Add [JsonStringEnumMemberName("value")] to each member.')
        lines.append("- Include a trailing comma after every member.")
    else:  # fields_only
        lines.append("OUTPUT MODE: fields_only")
        lines.append("- Return ONLY the property blocks for this page.")
        lines.append(
            "- Do NOT include namespace, using statements, class declaration, or closing braces."
        )
        lines.append(
            f"- Wrap properties with `{FIELDS_START_MARKER}` and `{FIELDS_END_MARKER}` markers."
        )
    return lines


def _paging_example_code(output_mode: str, class_name: str, base_example: str | None) -> str:
    """Return a mode-appropriate example code snippet for the prompt."""
    if output_mode == "enum_only":
        return (
            "/// <summary>\n"
            "/// Description of the enum.\n"
            "/// </summary>\n"
            "[JsonConverter(typeof(JsonStringEnumConverter))]\n"
            f"public enum {class_name}\n"
            "{\n"
            '    [JsonStringEnumMemberName("value_one")]\n'
            "    ValueOne,\n\n"
            '    [JsonStringEnumMemberName("value_two")]\n'
            "    ValueTwo\n"
            "}"
        )
    if output_mode == "enum_values_only":
        return (
            f"{FIELDS_START_MARKER}\n"
            '    [JsonStringEnumMemberName("value_three")]\n'
            "    ValueThree,\n\n"
            '    [JsonStringEnumMemberName("value_four")]\n'
            "    ValueFour,\n"
            f"{FIELDS_END_MARKER}"
        )
    if output_mode == "fields_only":
        return (
            f"{FIELDS_START_MARKER}\n"
            '    [JsonPropertyName("example_field")]\n'
            '    [Description("Example field")]\n'
            "    [Nullable(true)]\n"
            "    public string? ExampleField { get; init; }\n"
            f"{FIELDS_END_MARKER}"
        )
    if output_mode == "class_only":
        return (
            f"public class {class_name}\n"
            "{\n"
            '    [JsonPropertyName("example_field")]\n'
            '    [Description("Example field")]\n'
            "    [Nullable(true)]\n"
            "    public string? ExampleField { get; init; }\n"
            "}"
        )
    # full_class: use the base example from prompts.json
    if base_example:
        return base_example
    return (
        f"public class {class_name}\n"
        "{\n"
        '    [JsonPropertyName("id")]\n'
        '    [Description("Unique identifier")]\n'
        "    [Required]\n"
        "    public required string Id { get; init; }\n"
        "}"
    )


def build_type_page_prompt(
    packet: dict[str, Any],
    type_entry: dict[str, Any],
    fields_page: list[dict[str, Any]],
    page_index: int,
    page_count: int,
    is_root: bool,
    values_page: list[Any] | None = None,
    names_page: list[Any] | None = None,
) -> str:
    """Build an LLM prompt for a single page of a single type.

    Args:
        packet: Full prompt packet (for metadata and generation instructions).
        type_entry: Processed type dict (from _process_type / build_prompt_packet).
        fields_page: The subset of fields for this page.
        page_index: 1-based page index.
        page_count: Total number of pages for this type.
        is_root: True if this is the root DataObject class (not a nested type).

    Returns:
        Formatted prompt string for one LLM call.
    """
    metadata = packet["metadata"]
    generation = packet["generation"]
    nested_types = packet.get("nested_types", [])

    class_name = type_entry["name"]
    is_enum = bool(type_entry.get("enum_values") and not type_entry.get("fields"))
    output_mode = _output_mode(is_root, page_index, is_enum)

    all_fields: list[dict[str, Any]] = type_entry.get("fields") or []
    all_field_names = [f["json_name"] for f in all_fields]
    all_enum_values: list[Any] = type_entry.get("enum_values") or []

    lines: list[str] = []

    # Base instructions from prompts.json
    instructions = generation.get("instructions")
    if instructions:
        lines.append(instructions)
        lines.append("")

    # Mode-specific paging instructions
    paging_instr = _paging_instructions(output_mode, class_name)
    if paging_instr:
        lines.extend(paging_instr)
        lines.append("")

    # For multi-page enums, page 1 must include a trailing comma on its last member
    # so the stitched members from subsequent pages are valid C#.
    if is_enum and output_mode == "enum_only" and page_count > 1:
        lines.append(
            "- Include a trailing comma after the last enum member on this page;"
            " additional members will follow from subsequent pages."
        )
        lines.append("")

    lines.append("=" * 60)
    lines.append(f"ENDPOINT: {metadata['method']} {metadata['path']}")
    if metadata.get("response_description"):
        lines.append(f"Response: {metadata['response_description']}")
    lines.append(f"CLASS: {class_name}")
    lines.append("=" * 60)
    lines.append(f"Schema ID: {type_entry.get('schema_id', '')}")
    lines.append(f"Description: {type_entry.get('description') or 'No description'}")
    lines.append("")

    if page_count > 1:
        lines.append("PAGING:")
        lines.append(f"  Page: {page_index} of {page_count}")
        if is_enum:
            page_values = values_page if values_page is not None else all_enum_values
            lines.append(f"  Values in this page: {len(page_values)}")
            lines.append(f"  Total values: {len(all_enum_values)}")
        else:
            lines.append(f"  Fields in this page: {len(fields_page)}")
            lines.append(f"  Total fields: {len(all_fields)}")
            if all_field_names:
                lines.append(f"  All field names: {', '.join(all_field_names)}")
        lines.append("")

    # Nested type names hint — root page 1 only
    if is_root and page_index == 1 and nested_types:
        nested_names = [nt["name"] for nt in nested_types]
        lines.append(f"NESTED TYPES: {', '.join(nested_names)}")
        lines.append("Use these class names for complex field types. Do NOT generate them here.")
        lines.append("")

    if is_enum:
        display_values = values_page if values_page is not None else all_enum_values
        display_names = names_page if names_page is not None else type_entry.get("enum_names")
        if display_values:
            header = (
                f"ENUM (values {(page_index - 1) * len(display_values) + 1}–"
                f"{(page_index - 1) * len(display_values) + len(display_values)}"
                f" of {len(all_enum_values)}):"
                if page_count > 1
                else "ENUM:"
            )
            lines.append(header)
            lines.append(f"  Values: {', '.join(str(v) for v in display_values)}")
            if isinstance(display_names, list) and display_names:
                lines.append(f"  Names: {', '.join(str(v) for v in display_names)}")
            lines.append("")
    else:
        lines.append("FIELDS (this page):" if page_count > 1 else "FIELDS:")
        lines.append("-" * 40)
        lines.extend(_format_fields_section(fields_page))

    lines.append("EXAMPLE CODE PATTERN:")
    lines.append("-" * 40)
    base_example = generation.get("example_code")
    lines.append(_paging_example_code(output_mode, class_name, base_example))

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def build_prompt_packet(
    root_type: dict[str, Any],
    nested_types: list[dict[str, Any]],
    endpoint: Endpoint,
    schemas_by_id: dict[str, dict[str, Any]],
    max_fields_per_page: int = MAX_FIELDS_PER_PAGE,
    response_description: str | None = None,
) -> dict[str, Any]:
    """Assemble a prompt packet from a collected type closure.

    Args:
        root_type: Root type entry from build_type_hierarchy.
        nested_types: List of nested type entries from build_type_hierarchy.
        endpoint: The endpoint that was resolved (for context metadata).
        schemas_by_id: Schema registry for field type resolution.
        max_fields_per_page: Maximum fields per LLM page (for large types).

    Returns:
        A structured dict consumed by build_user_prompt and
        format_schema_markdown. Keys: metadata, root, nested_types, generation.
    """
    prompts = _load_prompts()

    root = _process_type(root_type, schemas_by_id)
    nested = [_process_type(nt, schemas_by_id) for nt in nested_types]

    data_object_name = format_data_object_name(root["name"])

    return {
        "metadata": {
            "method": endpoint.method,
            "path": endpoint.path,
            "data_object_name": data_object_name,
            "response_description": response_description or "",
        },
        "root": root,
        "nested_types": nested,
        "max_fields_per_page": max_fields_per_page,
        "generation": {
            "instructions": _join_lines(prompts["instructions"]),
            "example_code": _join_lines(prompts["example_code"]),
        },
    }


def build_system_prompt() -> str:
    """Return the system-level LLM prompt (generation instructions).

    Reads from the bundled prompts.json. The system prompt is stable across
    calls and can be cached by the caller if desired.
    """
    prompts = _load_prompts()
    return _join_lines(prompts["instructions"])


def build_user_prompt(packet: dict[str, Any]) -> str:
    """Format a prompt packet as the user-facing LLM message.

    Produces a single, self-contained prompt that describes the root type,
    all nested types, and the expected output pattern.

    Args:
        packet: Dict produced by build_prompt_packet.

    Returns:
        Formatted prompt string.
    """
    metadata = packet["metadata"]
    root = packet["root"]
    nested = packet.get("nested_types", [])
    generation = packet["generation"]

    lines: list[str] = []

    lines.append("=" * 60)
    lines.append(f"ENDPOINT: {metadata['method']} {metadata['path']}")
    lines.append(f"DATAOBJECT: {metadata['data_object_name']}")
    lines.append("=" * 60)
    lines.append("")

    # Root type
    lines.append(f"SCHEMA ID: {root['schema_id']}")
    lines.append(f"Description: {root['description'] or 'No description'}")
    lines.append("")

    # Enum-only root
    if root.get("enum_values") and not root["fields"]:
        lines.append("ENUM:")
        lines.append(f"  Values: {', '.join(str(v) for v in root['enum_values'])}")
        if isinstance(root.get("enum_names"), list):
            lines.append(f"  Names: {', '.join(str(v) for v in root['enum_names'])}")
        lines.append("")
    else:
        # Nested type names hint
        nested_names = [nt["name"] for nt in nested]
        if nested_names:
            lines.append(f"NESTED TYPES: {', '.join(nested_names)}")
            lines.append("Use these class names for complex field types. Do NOT generate them here.")
            lines.append("")

        lines.append("FIELDS:")
        lines.append("-" * 40)
        lines.extend(_format_fields_section(root["fields"]))

    # Nested types
    if nested:
        lines.append("")
        lines.append("=" * 60)
        lines.append("NESTED TYPES (define in same file, after root class)")
        lines.append("=" * 60)

        for nt in nested:
            lines.append("")
            lines.append(f"CLASS: {nt['name']}")
            lines.append("-" * 40)
            if nt.get("description"):
                lines.append(f"Description: {nt['description']}")
                lines.append("")
            if nt.get("enum_values") and not nt["fields"]:
                lines.append("ENUM:")
                lines.append(f"  Values: {', '.join(str(v) for v in nt['enum_values'])}")
                if isinstance(nt.get("enum_names"), list):
                    lines.append(f"  Names: {', '.join(str(v) for v in nt['enum_names'])}")
            else:
                lines.append("FIELDS:")
                lines.extend(_format_fields_section(nt["fields"], indent="  "))

    # Example
    lines.append("")
    lines.append("EXAMPLE CODE PATTERN:")
    lines.append("-" * 40)
    lines.append(generation["example_code"])

    return "\n".join(lines)


def format_schema_markdown(root_type: dict[str, Any], nested_types: list[dict[str, Any]]) -> str:
    """Produce the schema.md artefact for human review.

    Generates a Markdown summary of the root type and all nested types,
    including field names and C# types in a table. This file is written
    alongside the generated C# code so developers can inspect the schema
    without reading the IR JSON.

    Args:
        root_type: Raw root type entry from build_type_hierarchy (NOT the
            processed packet entry — schemas_by_id is not available here,
            so field types come from the "resolved_type" in properties).
        nested_types: Raw nested type entries.

    Returns:
        Markdown string.
    """
    lines: list[str] = []

    def _render_type(entry: dict[str, Any], level: int = 2) -> None:
        prefix = "#" * level
        lines.append(f"{prefix} {entry.get('name', 'Schema')}")
        lines.append("")
        if entry.get("description"):
            lines.append(entry["description"])
            lines.append("")
        lines.append(f"- Schema ID: `{entry.get('schema_id', '')}`")
        lines.append(f"- Kind: {entry.get('kind', 'object')}")
        lines.append("")

        enum_values = entry.get("enum_values")
        if isinstance(enum_values, list) and enum_values:
            lines.append("### Enum Values")
            lines.append("")
            enum_names = entry.get("enum_names")
            if isinstance(enum_names, list) and len(enum_names) == len(enum_values):
                lines.append("| Value | Name |")
                lines.append("|-------|------|")
                for v, n in zip(enum_values, enum_names):
                    lines.append(f"| `{v}` | `{n}` |")
            else:
                for v in enum_values:
                    lines.append(f"- `{v}`")
            lines.append("")

        props: list[dict[str, Any]] = entry.get("properties") or []
        if props:
            lines.append("### Fields")
            lines.append("")
            lines.append("| C# Property | Resolved Type |")
            lines.append("|-------------|--------------|")
            for prop in props:
                json_name = prop.get("json_name", "")
                display_name = json_name_to_csharp_property(json_name) if json_name else json_name
                resolved = prop.get("resolved_type") or prop.get("schema_id", "")
                lines.append(f"| `{display_name}` | `{resolved or 'object'}` |")
            lines.append("")

    root_name = root_type.get("name", "DataObject")
    lines.append(f"# {root_name}")
    lines.append("")
    _render_type(root_type, level=2)

    if nested_types:
        lines.append("---")
        lines.append("")
        lines.append("## Nested Types")
        lines.append("")
        for nt in nested_types:
            _render_type(nt, level=3)

    return "\n".join(lines).rstrip() + "\n"
