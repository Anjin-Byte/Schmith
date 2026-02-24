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
_MAX_FIELDS_PER_PAGE = 30


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _load_prompts() -> dict:
    with open(_PROMPTS_PATH, encoding="utf-8") as f:
        return json.load(f)


def _join_lines(value: str | list[str]) -> str:
    """Normalise a prompts.json value that may be a list of lines or a string."""
    if isinstance(value, list):
        return "\n".join(value)
    return value


def _process_type(type_entry: dict, schemas_by_id: dict[str, dict]) -> dict:
    """Convert a raw type_tree entry into a prompt-ready dict with field infos."""
    raw_props: list[dict] = type_entry.get("properties") or []
    fields: list[dict] = [build_field_info(prop, schemas_by_id) for prop in raw_props]

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


def _format_fields_section(fields: list[dict], indent: str = "  ") -> list[str]:
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

        lines.append(f"{indent}{field['json_name']}: {type_str}{attr_str}")
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
# Public API
# ---------------------------------------------------------------------------


def build_prompt_packet(
    root_type: dict,
    nested_types: list[dict],
    endpoint: Endpoint,
    schemas_by_id: dict[str, dict],
    max_fields_per_page: int = _MAX_FIELDS_PER_PAGE,
) -> dict:
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


def build_user_prompt(packet: dict) -> str:
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


def format_schema_markdown(root_type: dict, nested_types: list[dict]) -> str:
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

    def _render_type(entry: dict, level: int = 2) -> None:
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

        props: list[dict] = entry.get("properties") or []
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
