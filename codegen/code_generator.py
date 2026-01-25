"""Code generation from prompt packets using LLMs.

This module handles the generation of C# code from prompt packets
by calling LLM providers and writing the output files.
"""

import json
from pathlib import Path
from typing import Any, Iterator

from .llm_providers import LLMProvider, extract_code_from_response


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
        lines.append("")
    return lines


def build_prompt_from_packet(packet: dict) -> str:
    """Build the full LLM prompt from a prompt packet.

    Args:
        packet: Prompt packet dictionary

    Returns:
        Formatted prompt string
    """
    # Check if this is a grouped packet
    if packet.get("metadata", {}).get("is_grouped"):
        return _build_grouped_prompt(packet)
    return _build_flat_prompt(packet)


def _build_flat_prompt(packet: dict) -> str:
    """Build prompt for a flat (non-grouped) packet."""
    metadata = packet["metadata"]
    fields = packet["fields"]
    related = packet.get("related_schemas", {})
    generation = packet["generation"]

    lines = []

    # Instructions
    lines.append(generation["instructions"])
    lines.append("")

    # Schema information
    lines.append("=" * 60)
    lines.append(f"SCHEMA: {metadata['data_object_name']}")
    lines.append("=" * 60)
    lines.append("")
    lines.append(f"API Name: {metadata['ir_name']}")
    lines.append(f"Schema ID: {metadata['schema_id']}")
    lines.append(f"Description: {metadata['description'] or 'No description'}")
    if metadata.get("primary_key_field"):
        lines.append(f"Primary Key: {metadata['primary_key_field']}")
    lines.append("")

    # Fields
    lines.append("FIELDS:")
    lines.append("-" * 40)
    lines.extend(format_fields_section(fields))

    # Related schemas
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

    # Example
    lines.append("")
    lines.append("EXAMPLE CODE PATTERN:")
    lines.append("-" * 40)
    lines.append(generation["example_code"])

    return "\n".join(lines)


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
    prompt = build_prompt_from_packet(packet)

    if show_prompt:
        print("\n--- PROMPT ---")
        print(prompt[:2000])
        if len(prompt) > 2000:
            print(f"\n... ({len(prompt) - 2000} more characters)")
        print("--- END PROMPT ---\n")

    response = provider.generate(prompt)
    return extract_code_from_response(response)


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

    for packet_file in packet_files:
        with open(packet_file, encoding="utf-8") as f:
            packet = json.load(f)

        name = packet["metadata"]["data_object_name"]
        print(f"\n{'=' * 60}")
        print(f"Processing: {name}")
        print(f"{'=' * 60}")

        if dry_run:
            prompt = build_prompt_from_packet(packet)
            if show_prompt:
                print("\n--- PROMPT ---")
                print(prompt[:2000])
                if len(prompt) > 2000:
                    print(f"\n... ({len(prompt) - 2000} more characters)")
                print("--- END PROMPT ---\n")
            print(f"  Would generate: {name}.cs")
            generated += 1
            continue

        try:
            code = generate_from_packet(packet, provider, show_prompt)
            output_path = output_dir / f"{name}.cs"
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(code)
            print(f"  Generated: {output_path}")
            generated += 1
        except Exception as e:
            print(f"  Error: {e}")
            errors += 1

    return generated, errors
