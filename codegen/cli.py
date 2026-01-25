"""Unified CLI for XChange DataObject code generation.

This module provides a command-line interface with subcommands for:
- config: Show current configuration
- list: List available IRs and potential DataObjects
- groups: Show parent-child schema relationships
- packets: Generate prompt packets from IR
- generate: Generate C# code from prompt packets

Configuration is loaded from codegen/config.toml. Command-line arguments
override configuration file settings.

Usage:
    python -m codegen config                  # Show configuration
    python -m codegen list                    # List available IRs
    python -m codegen list servicefusion      # List DataObjects for an IR
    python -m codegen groups servicefusion    # Show schema groups
    python -m codegen packets servicefusion   # Generate prompt packets
    python -m codegen generate servicefusion  # Generate C# code
"""

import argparse
import json
import sys
from pathlib import Path

from .config import CodegenConfig, get_config
from .ir_loader import IRLoader
from .schema_filter import filter_schemas, find_parent_child_relationships, get_root_schemas
from .type_mapping import format_data_object_name
from .prompt_packets import PromptPacketBuilder, write_packets
from .llm_providers import get_provider
from .code_generator import generate_from_packets_dir


def cmd_config(args: argparse.Namespace, config: CodegenConfig) -> int:
    """Show current configuration."""
    paths = config.resolve_paths()

    print("XChange DataObject Code Generation Configuration")
    print("=" * 60)
    print(f"\nConfig file: {Path(__file__).parent / 'config.toml'}")

    print("\n[paths]")
    print(f"  ir_dir = {config.paths.ir_dir}")
    print(f"    -> {paths.ir_dir}")
    print(f"  packets_dir = {config.paths.packets_dir}")
    print(f"    -> {paths.packets_dir}/flat/<ir>/")
    print(f"    -> {paths.packets_dir}/grouped/<ir>/")
    print(f"  generated_dir = {config.paths.generated_dir}")
    print(f"    -> {paths.generated_dir}")

    print("\n[llm]")
    print(f"  provider = {config.llm.provider}")
    print(f"  model = {config.llm.model or '(provider default)'}")
    print(f"  max_tokens = {config.llm.max_tokens}")

    print("\n[generation]")
    print(f"  include_errors = {config.generation.include_errors}")
    print(f"  include_anonymous = {config.generation.include_anonymous}")
    print(f"  grouped = {config.generation.grouped}")

    print("\n[prompting]")
    print(f"  max_fields_per_page = {config.prompting.max_fields_per_page}")

    print("\n[filters]")
    print(f"  exclude_patterns = {config.filters.exclude_patterns}")
    print(f"  include_patterns = {config.filters.include_patterns}")

    return 0


def cmd_list(args: argparse.Namespace, config: CodegenConfig) -> int:
    """List available IRs or DataObjects for a specific IR."""
    paths = config.resolve_paths()
    ir_base = args.ir_dir or paths.ir_dir

    # List available IRs
    if not args.ir_name:
        available = IRLoader.list_available(ir_base)
        if not available:
            print(f"No IRs found in {ir_base}")
            return 1

        print("Available IRs:")
        print("=" * 50)
        for name in available:
            try:
                loader = IRLoader(name, ir_base)
                counts = loader.counts
                print(f"\n  {name}")
                print(f"    Operations: {counts.get('operations', '?')}")
                print(f"    Schemas: {counts.get('schemas', '?')}")
            except FileNotFoundError:
                print(f"\n  {name} (error loading)")
        return 0

    # List DataObjects for specific IR
    try:
        loader = IRLoader(args.ir_name, ir_base)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    # Use config defaults if not specified on command line
    include_errors = args.include_errors or config.generation.include_errors
    include_anonymous = args.include_anonymous or config.generation.include_anonymous

    schemas = filter_schemas(
        loader.schemas(),
        include_errors=include_errors,
        include_primitives=False,
        include_anonymous=include_anonymous,
    )

    # Apply filter patterns from config
    if not args.no_filter:
        schemas = [s for s in schemas if not config.filters.should_exclude(s.name)]

    # Sort by name
    schemas.sort(key=lambda s: s.name.lower())

    if args.json:
        output = {
            "ir_name": args.ir_name,
            "total_schemas": loader.counts.get("schemas", 0),
            "filtered_count": len(schemas),
            "xchange_objects": [
                {
                    "data_object_name": format_data_object_name(s.name),
                    "schema_name": s.name,
                    "schema_id": s.schema_id,
                    "kind": s.kind,
                    "usage_count": s.usage_count,
                }
                for s in schemas
            ],
        }
        print(json.dumps(output, indent=2))
    else:
        print(f"XChange Data Objects for '{args.ir_name}'")
        print("=" * 50)
        print(f"Total schemas in IR: {loader.counts.get('schemas', 0)}")
        print(f"Data Objects to generate: {len(schemas)}")
        print()

        for schema in schemas:
            name = format_data_object_name(schema.name)
            if args.verbose:
                print(f"  {name}")
                print(f"    Schema ID: {schema.schema_id}")
                print(f"    Kind: {schema.kind}")
                print(f"    Used in {schema.usage_count} operation(s)")
                print()
            else:
                print(f"  {name}")

    return 0


def cmd_groups(args: argparse.Namespace, config: CodegenConfig) -> int:
    """Show detected parent-child schema groups."""
    paths = config.resolve_paths()
    ir_base = args.ir_dir or paths.ir_dir

    try:
        loader = IRLoader(args.ir_name, ir_base)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    # Get valid schemas for grouping
    valid_schemas = [
        s for s in loader.schemas()
        if s.get("name_hint")
        and not s.get("is_inline")
        and s.get("kind") == "object"
        and "anon/" not in s.get("schema_id", "")
    ]

    parent_children = find_parent_child_relationships(valid_schemas)
    root_schemas = get_root_schemas(valid_schemas, parent_children)

    print(f"\nParent-Child Relationships for '{args.ir_name}':")
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

    return 0


def cmd_packets(args: argparse.Namespace, config: CodegenConfig) -> int:
    """Generate prompt packets from IR."""
    paths = config.resolve_paths()
    ir_base = args.ir_dir or paths.ir_dir

    try:
        loader = IRLoader(args.ir_name, ir_base)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    builder = PromptPacketBuilder(
        loader,
        max_fields_per_page=config.prompting.max_fields_per_page,
    )

    # Use config default for grouped if not specified
    grouped = args.grouped if args.grouped else config.generation.grouped

    # Determine output directory
    if args.output_dir:
        output_dir = args.output_dir
    else:
        output_dir = paths.packets_for(args.ir_name, grouped=grouped)

    # Use config defaults for include options
    include_errors = args.include_errors or config.generation.include_errors

    print(f"Loading IR from {loader.ir_path}...")

    if grouped:
        # Generate grouped packets
        packets = builder.build_grouped_packets()
    else:
        # Generate flat packets
        packets = builder.build_flat_packets(include_errors=include_errors)

    # Filter to specific schema if requested
    if args.schema:
        target = args.schema.lower().replace("dataobject", "")
        packets = (
            p for p in packets
            if target in p["metadata"]["data_object_name"].lower()
        )

    print(f"Processing schemas...")
    count = write_packets(packets, output_dir, dry_run=args.dry_run)

    print(f"\nGenerated {count} prompt packets")
    if not args.dry_run:
        print(f"Output directory: {output_dir}")

    return 0


def cmd_generate(args: argparse.Namespace, config: CodegenConfig) -> int:
    """Generate C# code from prompt packets."""
    paths = config.resolve_paths()

    # Use config default for grouped if not specified
    grouped = args.grouped if args.grouped else config.generation.grouped

    # Determine packets directory
    if args.packets_dir:
        packets_dir = args.packets_dir
    else:
        packets_dir = paths.packets_for(args.ir_name, grouped=grouped)

    if not packets_dir.exists():
        print(f"Error: Prompt packets directory not found: {packets_dir}", file=sys.stderr)
        print(f"\nRun 'python -m codegen packets {args.ir_name}' first.", file=sys.stderr)
        return 1

    # Determine output directory
    output_dir = args.output_dir or paths.generated_for(args.ir_name)

    # Use config defaults for provider/model
    provider_name = args.provider or config.llm.provider
    model = args.model or config.llm.model or None

    # Get provider
    try:
        provider = get_provider(provider_name, model=model, dry_run=args.dry_run)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    print(f"Processing packets from {packets_dir}...")
    if not args.dry_run:
        print(f"Using {provider_name}" + (f" ({model})" if model else ""))

    generated, errors = generate_from_packets_dir(
        packets_dir,
        output_dir,
        provider,
        schema_filter=args.schema,
        limit=args.limit,
        dry_run=args.dry_run,
        show_prompt=args.show_prompt,
    )

    print(f"\n{'=' * 60}")
    print("SUMMARY")
    print("=" * 60)
    print(f"Generated: {generated}")
    print(f"Errors: {errors}")
    if not args.dry_run and generated > 0:
        print(f"Output directory: {output_dir}")

    return 0 if errors == 0 else 1


def cmd_pages(args: argparse.Namespace, config: CodegenConfig) -> int:
    """Show pagination view for schemas as submitted to the LLM."""
    paths = config.resolve_paths()
    ir_base = args.ir_dir or paths.ir_dir

    try:
        loader = IRLoader(args.ir_name, ir_base)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    builder = PromptPacketBuilder(
        loader,
        max_fields_per_page=config.prompting.max_fields_per_page,
    )

    grouped = args.grouped if args.grouped else config.generation.grouped
    include_errors = args.include_errors or config.generation.include_errors

    if grouped:
        packets = builder.build_grouped_packets()
    else:
        packets = builder.build_flat_packets(include_errors=include_errors)

    schema_filter = args.schema.lower().replace("dataobject", "") if args.schema else None
    total_pages = 0

    for packet in packets:
        schemas = packet.get("schemas", [])
        if not schemas:
            continue

        if schema_filter:
            matched = []
            for schema in schemas:
                class_name = schema.get("class_name", "").lower()
                schema_name = schema.get("schema_name", "").lower()
                if schema_filter in class_name or schema_filter in schema_name:
                    matched.append(schema)
            schemas = matched
            if not schemas:
                continue

        print("\n" + "=" * 60)
        print(f"DataObject: {packet['metadata']['data_object_name']}")
        print(f"Grouped: {packet['metadata'].get('is_grouped', False)}")
        print(f"Max Fields/Page: {packet['metadata'].get('max_fields_per_page')}")

        for schema in schemas:
            pages = schema.get("pages", [])
            page_count = len(pages)
            total_pages += page_count

            print("\n" + "-" * 60)
            print(f"Schema: {schema.get('class_name')} ({schema.get('schema_name')})")
            print(f"Role: {schema.get('role')}")
            print(f"Total Fields: {schema.get('field_count')}")
            print(f"Pages: {page_count}")

            for page in pages:
                fields = page.get("fields", [])
                field_names = ", ".join(f.get("json_name", "") for f in fields)
                print(
                    f"  Page {page['page_index']}/{page['page_count']}"
                    f" - {page['field_count']} fields"
                )
                if args.show_fields:
                    print(f"    {field_names}")

    print("\n" + "=" * 60)
    print(f"Total prompt pages: {total_pages}")
    return 0


def main() -> int:
    """Main entry point for the CLI."""
    # Load configuration
    config = get_config()

    parser = argparse.ArgumentParser(
        prog="codegen",
        description="XChange DataObject code generation tools",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Configuration is loaded from codegen/config.toml.
Command-line arguments override config file settings.

Examples:
    python -m codegen config                    # Show configuration
    python -m codegen list                      # List available IRs
    python -m codegen list servicefusion -v     # List schemas with details
    python -m codegen groups servicefusion      # Show parent-child groups
    python -m codegen packets servicefusion     # Generate prompt packets
    python -m codegen packets servicefusion --grouped  # With nested types
    python -m codegen generate servicefusion    # Generate C# code
""",
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Config command
    config_parser = subparsers.add_parser(
        "config",
        help="Show current configuration",
        description="Display the current configuration settings.",
    )
    config_parser.set_defaults(func=cmd_config)

    # List command
    list_parser = subparsers.add_parser(
        "list",
        help="List available IRs or DataObjects",
        description="List available IRs or show potential DataObjects for a specific IR.",
    )
    list_parser.add_argument(
        "ir_name",
        nargs="?",
        help="IR name to list DataObjects for (omit to list available IRs)",
    )
    list_parser.add_argument(
        "--include-errors",
        action="store_true",
        help="Include error response schemas",
    )
    list_parser.add_argument(
        "--include-anonymous",
        action="store_true",
        help="Include anonymous/inline schemas",
    )
    list_parser.add_argument(
        "--no-filter",
        action="store_true",
        help="Disable config exclude_patterns filtering",
    )
    list_parser.add_argument(
        "--json",
        action="store_true",
        help="Output as JSON",
    )
    list_parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show additional details",
    )
    list_parser.add_argument(
        "--ir-dir",
        type=Path,
        help="Base directory containing IR folders",
    )
    list_parser.set_defaults(func=cmd_list)

    # Groups command
    groups_parser = subparsers.add_parser(
        "groups",
        help="Show parent-child schema relationships",
        description="Detect and display parent-child schema relationships.",
    )
    groups_parser.add_argument(
        "ir_name",
        help="IR name to analyze",
    )
    groups_parser.add_argument(
        "--ir-dir",
        type=Path,
        help="Base directory containing IR folders",
    )
    groups_parser.set_defaults(func=cmd_groups)

    # Packets command
    packets_parser = subparsers.add_parser(
        "packets",
        help="Generate prompt packets from IR",
        description="Generate prompt packets for LLM code generation.",
    )
    packets_parser.add_argument(
        "ir_name",
        help="IR name to generate packets for",
    )
    packets_parser.add_argument(
        "--schema",
        help="Generate packet for specific schema only",
    )
    packets_parser.add_argument(
        "--grouped",
        action="store_true",
        help=f"Generate grouped packets with nested types (config default: {config.generation.grouped})",
    )
    packets_parser.add_argument(
        "--include-errors",
        action="store_true",
        help="Include error schemas",
    )
    packets_parser.add_argument(
        "--output-dir",
        type=Path,
        help="Output directory for packets",
    )
    packets_parser.add_argument(
        "--ir-dir",
        type=Path,
        help="Base directory containing IR folders",
    )
    packets_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be generated without writing files",
    )
    packets_parser.set_defaults(func=cmd_packets)

    # Generate command
    gen_parser = subparsers.add_parser(
        "generate",
        help="Generate C# code from prompt packets",
        description="Generate C# DataObject code using an LLM.",
    )
    gen_parser.add_argument(
        "ir_name",
        help="IR name (matches prompt_packets directory)",
    )
    gen_parser.add_argument(
        "--schema",
        help="Generate for specific schema only",
    )
    gen_parser.add_argument(
        "--grouped",
        action="store_true",
        help=f"Use grouped packets (config default: {config.generation.grouped})",
    )
    gen_parser.add_argument(
        "--provider",
        choices=["anthropic", "openai"],
        help=f"LLM provider (config default: {config.llm.provider})",
    )
    gen_parser.add_argument(
        "--model",
        help=f"Model override (config: {config.llm.model or 'provider default'})",
    )
    gen_parser.add_argument(
        "--packets-dir",
        type=Path,
        help="Directory containing prompt packets",
    )
    gen_parser.add_argument(
        "--output-dir",
        type=Path,
        help="Output directory for generated code",
    )
    gen_parser.add_argument(
        "--limit",
        type=int,
        help="Limit number of schemas to process",
    )
    gen_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show prompts without calling LLM",
    )
    gen_parser.add_argument(
        "--show-prompt",
        action="store_true",
        help="Print prompts being sent to LLM",
    )
    gen_parser.set_defaults(func=cmd_generate)

    # Pagination view command
    pages_parser = subparsers.add_parser(
        "pages",
        help="Show pagination view for LLM prompts",
        description="Display how schema fields are paged for LLM submission.",
    )
    pages_parser.add_argument(
        "ir_name",
        help="IR name to analyze",
    )
    pages_parser.add_argument(
        "--schema",
        help="Filter to a specific schema",
    )
    pages_parser.add_argument(
        "--grouped",
        action="store_true",
        help=f"Use grouped packets (config default: {config.generation.grouped})",
    )
    pages_parser.add_argument(
        "--include-errors",
        action="store_true",
        help="Include error schemas",
    )
    pages_parser.add_argument(
        "--show-fields",
        action="store_true",
        help="Show field names for each page",
    )
    pages_parser.add_argument(
        "--ir-dir",
        type=Path,
        help="Base directory containing IR folders",
    )
    pages_parser.set_defaults(func=cmd_pages)

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 0

    return args.func(args, config)


if __name__ == "__main__":
    sys.exit(main())
