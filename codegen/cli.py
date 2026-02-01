"""Unified CLI for XChange DataObject code generation.

This module provides a command-line interface with subcommands for:
- config: Show current configuration
- list: List available IRs and potential DataObjects
- groups: Show parent-child schema relationships
- coverage: Show schema coverage report (what's generated vs filtered)
- endpoints: Endpoint response coverage report (schemas ↔ DataObjects)
- packets: Generate prompt packets from IR
- generate: Generate C# code from prompt packets

Configuration is loaded from codegen/config.toml. Command-line arguments
override configuration file settings.

Usage:
    python -m codegen config                  # Show configuration
    python -m codegen list                    # List available IRs
    python -m codegen list servicefusion      # List DataObjects for an IR
    python -m codegen groups servicefusion    # Show schema groups
    python -m codegen coverage servicefusion  # Show coverage report
    python -m codegen endpoints servicefusion # Endpoint response coverage report
    python -m codegen packets servicefusion   # Generate prompt packets
    python -m codegen generate servicefusion  # Generate C# code
"""

import argparse
import json
import shutil
import sys
from pathlib import Path

from .config import CodegenConfig, get_config
from .filters import get_filters, SchemaFilters
from .ir.loader import IRLoader
from .schema.filter import (
    find_parent_child_relationships_from_ir,
    get_root_schemas,
    find_reachable_component_names,  # coverage aligns roots with reachable schemas
)
from .schema.type_mapping import extract_clean_name, format_data_object_name  # normalize names in coverage
from .generation.prompt_packets import PromptPacketBuilder, write_packets
from .providers.llm import get_provider
from .generation.code_generator import generate_from_packets_dir
from .generation.endpoints_report import write_endpoints_report


def cmd_config(args: argparse.Namespace, config: CodegenConfig) -> int:
    """Show current configuration."""
    paths = config.resolve_paths()
    filters = get_filters()

    print("XChange DataObject Code Generation Configuration")
    print("=" * 60)

    print(f"\nConfig file: {Path(__file__).parent / 'config.toml'}")
    print("\n[paths]")
    print(f"  ir_dir = {config.paths.ir_dir}")
    print(f"    -> {paths.ir_dir}")
    print(f"  packets_dir = {config.paths.packets_dir}")
    print(f"    -> {paths.packets_dir}/grouped/<ir>/")
    print(f"  generated_dir = {config.paths.generated_dir}")
    print(f"    -> {paths.generated_dir}")

    print("\n[llm]")
    print(f"  provider = {config.llm.provider}")
    print(f"  model = {config.llm.model or '(provider default)'}")
    print(f"  max_tokens = {config.llm.max_tokens}")

    print("\n[prompting]")
    print(f"  max_fields_per_page = {config.prompting.max_fields_per_page}")

    print(f"\nFilters file: {Path(__file__).parent / 'filters.toml'}")
    print("\n[categories]")
    print(f"  include_errors = {filters.categories.include_errors}")
    print(f"  include_anonymous = {filters.categories.include_anonymous}")
    print(f"  include_variants = {filters.categories.include_variants}")
    print(f"  include_primitives = {filters.categories.include_primitives}")

    print("\n[patterns]")
    print(f"  exclude = {filters.patterns.exclude}")
    print(f"  include = {filters.patterns.include}")

    print("\n[explicit]")
    print(f"  exclude = {filters.explicit.exclude}")
    print(f"  include = {filters.explicit.include}")

    return 0


def cmd_list(args: argparse.Namespace, config: CodegenConfig) -> int:
    """List available IRs or DataObjects for a specific IR."""
    paths = config.resolve_paths()
    ir_base = args.ir_dir or paths.ir_dir
    filters = get_filters()

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

    # Filter schemas using centralized filters
    all_schemas = list(loader.schemas())
    filtered_schemas = filters.filter_schemas(all_schemas)

    # Build schema info list for display
    schemas = []
    for schema in filtered_schemas:
        schema_id = schema.get("schema_id", "")
        name_hint = schema.get("name_hint", "")
        clean_name = extract_clean_name(schema_id, name_hint)
        schemas.append({
            "name": clean_name,
            "schema_id": schema_id,
            "kind": schema.get("kind", ""),
            "usage_count": len(schema.get("where_used", [])),
        })

    # Sort by name
    schemas.sort(key=lambda s: s["name"].lower())

    if args.json:
        output = {
            "ir_name": args.ir_name,
            "total_schemas": loader.counts.get("schemas", 0),
            "filtered_count": len(schemas),
            "xchange_objects": [
                {
                    "data_object_name": format_data_object_name(s["name"]),
                    "schema_name": s["name"],
                    "schema_id": s["schema_id"],
                    "kind": s["kind"],
                    "usage_count": s["usage_count"],
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
            name = format_data_object_name(schema["name"])
            if args.verbose:
                print(f"  {name}")
                print(f"    Schema ID: {schema['schema_id']}")
                print(f"    Kind: {schema['kind']}")
                print(f"    Used in {schema['usage_count']} operation(s)")
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

    # Use IR adjacency data for accurate parent-child relationships
    adjacency = loader.adjacency()
    schemas_by_id = loader.schemas_by_id()
    parent_children = find_parent_child_relationships_from_ir(adjacency, schemas_by_id)
    root_schemas = get_root_schemas(valid_schemas, parent_children)

    # Helper to collect all descendants recursively
    def collect_all_descendants(
        parent_name: str,
        parent_children: dict[str, list[str]],
        visited: set[str] | None = None,
    ) -> list[str]:
        """Recursively collect all descendants of a parent schema."""
        if visited is None:
            visited = set()
        if parent_name in visited:
            return []
        visited.add(parent_name)
        all_descendants: list[str] = []
        for child in parent_children.get(parent_name, []):
            if child not in visited:
                all_descendants.append(child)
                all_descendants.extend(collect_all_descendants(child, parent_children, visited))
        return all_descendants

    # Helper to print tree with proper indentation for deeply nested types
    def print_tree(
        name: str,
        parent_children: dict[str, list[str]],
        indent: str = "  ",
        visited: set[str] | None = None,
    ) -> None:
        """Recursively print nested types as a tree."""
        if visited is None:
            visited = set()
        if name in visited:
            return
        visited.add(name)
        children = parent_children.get(name, [])
        for i, child in enumerate(sorted(children)):
            is_last = i == len(children) - 1
            prefix = "└── " if is_last else "├── "
            print(f"{indent}{prefix}{child}")
            # Recurse with increased indentation
            next_indent = indent + ("    " if is_last else "│   ")
            print_tree(child, parent_children, next_indent, visited)

    print(f"\nParent-Child Relationships for '{args.ir_name}':")
    print("=" * 50)

    for parent in sorted(parent_children.keys()):
        print(f"\n{parent}DataObject:")
        print_tree(parent, parent_children, "  ", set())

    print(f"\n\nRoot Schemas (standalone DataObjects): {len(root_schemas)}")
    print("=" * 50)
    for name in root_schemas:
        # Show total descendants (including deeply nested), not just direct children
        all_descendants = collect_all_descendants(name, parent_children)
        if all_descendants:
            print(f"  {name}DataObject (+ {len(all_descendants)} nested types)")
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

    # Determine output directory
    if args.output_dir:
        output_dir = args.output_dir
    else:
        output_dir = paths.packets_for(args.ir_name)

    print(f"Loading IR from {loader.ir_path}...")

    packets = builder.build_grouped_packets()

    # Filter to specific schema if requested
    if args.schema:
        target = args.schema.lower().replace("dataobject", "")
        packets = (
            p for p in packets
            if target in p["metadata"]["data_object_name"].lower()
        )

    print(f"Processing schemas...")
    if not args.dry_run and not args.no_clean and output_dir.exists():
        # Avoid stale packets by clearing the target directory unless opted out.
        shutil.rmtree(output_dir)
    count = write_packets(packets, output_dir, dry_run=args.dry_run)

    print(f"\nGenerated {count} prompt packets")
    if not args.dry_run:
        print(f"Output directory: {output_dir}")

    return 0


def cmd_generate(args: argparse.Namespace, config: CodegenConfig) -> int:
    """Generate C# code from prompt packets."""
    paths = config.resolve_paths()

    # Determine packets directory
    if args.packets_dir:
        packets_dir = args.packets_dir
    else:
        packets_dir = paths.packets_for(args.ir_name)

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
        if not args.no_clean and output_dir.exists():
            # Avoid stale generated code by clearing the target directory unless opted out.
            shutil.rmtree(output_dir)

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


def cmd_coverage(args: argparse.Namespace, config: CodegenConfig) -> int:
    """Show schema coverage report - what's generated vs filtered."""
    from datetime import datetime

    paths = config.resolve_paths()
    ir_base = args.ir_dir or paths.ir_dir
    filters = get_filters()

    try:
        loader = IRLoader(args.ir_name, ir_base)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    all_schemas = list(loader.schemas())

    # Categorize schemas using centralized filters
    categories = filters.categorize_schemas(all_schemas)

    # Build reachability-aware root vs nested sets for coverage reporting.
    adjacency = loader.adjacency()  # refs/adjacency.json for parent/child links
    operations = loader.operations()  # operations/index.json for reachability
    schemas_by_id = loader.schemas_by_id()  # needed for relationship resolution
    reachable_names = find_reachable_component_names(
        operations, adjacency, schemas_by_id
    )  # align coverage with packet generation

    eligible_schemas = categories["generated"]  # eligible for DataObject generation
    eligible_names = {
        extract_clean_name(s.get("schema_id", ""), s.get("name_hint"))
        for s in eligible_schemas
    }  # normalize for RAML/OpenAPI naming

    # Restrict to reachable schemas to match packet generation semantics.
    if reachable_names:
        eligible_names = {name for name in eligible_names if name in reachable_names}  # filter by reachability
        eligible_schemas = [
            s for s in eligible_schemas
            if extract_clean_name(s.get("schema_id", ""), s.get("name_hint")) in reachable_names
        ]  # keep schemas in sync with name filter

    parent_children = find_parent_child_relationships_from_ir(
        adjacency, schemas_by_id, reachable_names
    )  # parent/child mapping for roots vs nested
    root_names = set(get_root_schemas(eligible_schemas, parent_children))  # roots that generate scaffolding
    nested_only_names = sorted(eligible_names - root_names)  # nested-only schemas included under roots

    # Check for unaccounted
    total_categorized = sum(len(v) for v in categories.values())
    unaccounted = len(all_schemas) - total_categorized
    coverage_pct = (len(categories["generated"]) / len(all_schemas) * 100) if all_schemas else 0
    reachable_root_count = len(root_names)  # roots that generate standalone scaffolding
    nested_only_count = len(nested_only_names)  # nested-only schemas under roots

    # Category labels for display
    filter_categories = [
        ("anonymous", "Anonymous/inline schemas"),
        ("primitive", "Primitive types"),
        ("non_object", "Non-object kinds"),
        ("error", "Error schemas"),
        ("variant", "Body/View variants"),
        ("pattern_exclude", "Pattern excluded"),
        ("explicit_exclude", "Explicitly excluded"),
    ]

    # Build markdown report
    md_lines = [
        f"# Schema Coverage Report: {args.ir_name}",
        "",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"**IR Source:** `{loader.ir_path}`",
        "",
        "## Summary",
        "",
        "| Metric | Count |",
        "|--------|-------|",
        f"| Total schemas in spec | {len(all_schemas)} |",
        f"| Generated DataObjects | {len(categories['generated'])} |",
        f"| Generated Roots | {reachable_root_count} |",
        f"| Nested-only Schemas | {nested_only_count} |",
        f"| Filtered out | {len(all_schemas) - len(categories['generated'])} |",
        f"| **Coverage** | **{coverage_pct:.1f}%** |",
        "",
        "## Filtered Schemas by Category",
        "",
        "| Category | Count | Description |",
        "|----------|-------|-------------|",
    ]

    for key, label in filter_categories:
        count = len(categories.get(key, []))
        if count > 0:
            md_lines.append(f"| {label} | {count} | Intentionally excluded |")

    if unaccounted != 0:
        md_lines.append(f"| **UNACCOUNTED** | **{unaccounted}** | **Potential issue!** |")

    # Generated DataObjects section (eligible schemas)
    md_lines.extend([
        "",
        "## Generated DataObjects (Eligible Schemas)",
        "",
        f"The following {len(categories['generated'])} schemas are eligible for generation (before root/nested split):",
        "",
        "| # | DataObject Name | Schema ID |",
        "|---|-----------------|-----------|",
    ])

    for i, schema in enumerate(
        sorted(categories["generated"], key=lambda s: (s.get("name_hint") or "").lower()), 1
    ):
        name = extract_clean_name(schema.get("schema_id", ""), schema.get("name_hint"))  # normalized name for consistency
        schema_id = schema.get("schema_id", "")
        md_lines.append(f"| {i} | `{format_data_object_name(name)}` | `{schema_id}` |")

    # Roots section (actual scaffolding)
    md_lines.extend([
        "",
        "## Generated Roots (Standalone DataObjects)",
        "",
        f"The following {reachable_root_count} schemas produce standalone scaffolding:",
        "",
        "| # | DataObject Name |",
        "|---|-----------------|",
    ])
    for i, name in enumerate(sorted(root_names), 1):
        md_lines.append(f"| {i} | `{format_data_object_name(name)}` |")

    # Nested-only section
    md_lines.extend([
        "",
        "## Nested-only Schemas",
        "",
        f"The following {nested_only_count} schemas are included as nested types under roots:",
        "",
        "| # | Schema Name |",
        "|---|-------------|",
    ])
    for i, name in enumerate(nested_only_names, 1):
        md_lines.append(f"| {i} | `{name}` |")

    # Filtered schemas details
    md_lines.extend([
        "",
        "## Filtered Schema Details",
        "",
    ])

    for key, label in filter_categories:
        cat_schemas = categories.get(key, [])
        if cat_schemas:
            md_lines.extend([
                f"### {label} ({len(cat_schemas)})",
                "",
                "| Name | Schema ID |",
                "|------|-----------|",
            ])
            for schema in sorted(cat_schemas, key=lambda s: s.get("schema_id", "")):
                schema_id = schema.get("schema_id", "")
                name = schema.get("name_hint", "(no name)")
                md_lines.append(f"| `{name}` | `{schema_id}` |")
            md_lines.append("")

    # Status
    md_lines.extend([
        "## Status",
        "",
    ])
    if unaccounted == 0:
        md_lines.append("✅ **All schemas accounted for** - Every schema in the spec is either generated or intentionally filtered.")
    else:
        md_lines.append(f"⚠️ **WARNING:** {unaccounted} schemas are unaccounted for and may indicate a categorization bug.")

    md_content = "\n".join(md_lines)

    # Determine output path: generated/<ir_name>/reports/
    if args.output_dir:
        report_dir = args.output_dir
    else:
        report_dir = paths.generated_dir / args.ir_name / "_reports"

    report_path = report_dir / "coverage.md"

    # Write report if not dry-run
    if not args.dry_run:
        report_dir.mkdir(parents=True, exist_ok=True)
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(md_content)
        print(f"Coverage report written to: {report_path}")
    else:
        print("--- DRY RUN: Report would be written to:", report_path)

    # Also print summary to console
    print(f"\nSchema Coverage Report for '{args.ir_name}'")
    print("=" * 60)
    print(f"Total schemas in spec:  {len(all_schemas)}")
    print(f"Generated DataObjects:  {len(categories['generated'])}")
    print(f"Generated Roots:        {reachable_root_count}")
    print(f"Nested-only Schemas:    {nested_only_count}")
    print(f"Filtered out:           {len(all_schemas) - len(categories['generated'])}")
    print(f"\nCoverage: {coverage_pct:.1f}%")

    if unaccounted == 0:
        print("All schemas accounted for ✓")
    else:
        print(f"WARNING: {unaccounted} schemas unaccounted for!")
        return 1

    return 0


def cmd_endpoints(args: argparse.Namespace, config: CodegenConfig) -> int:
    """Generate endpoint response coverage report."""
    paths = config.resolve_paths()
    ir_dir = args.ir_dir or paths.ir_dir
    generated_dir = args.generated_dir or paths.generated_dir

    report_path = write_endpoints_report(args.ir_name, ir_dir, generated_dir)
    print(f"\nEndpoints report written to: {report_path}")
    return 0


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

    packets = builder.build_grouped_packets()

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
    python -m codegen coverage servicefusion    # Show schema coverage report
    python -m codegen packets servicefusion     # Generate prompt packets
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
        description="List available IRs or show potential DataObjects for a specific IR. "
                    "Filtering is configured in filters.toml.",
    )
    list_parser.add_argument(
        "ir_name",
        nargs="?",
        help="IR name to list DataObjects for (omit to list available IRs)",
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

    # Coverage command
    coverage_parser = subparsers.add_parser(
        "coverage",
        help="Show schema coverage report",
        description="Show what schemas are generated vs filtered and why.",
    )
    coverage_parser.add_argument(
        "ir_name",
        help="IR name to analyze",
    )
    coverage_parser.add_argument(
        "--output-dir",
        type=Path,
        help="Output directory for report (default: generated/<ir_name>/_reports/)",
    )
    coverage_parser.add_argument(
        "--ir-dir",
        type=Path,
        help="Base directory containing IR folders",
    )
    coverage_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be written without creating files",
    )
    coverage_parser.set_defaults(func=cmd_coverage)

    # Endpoints command
    endpoints_parser = subparsers.add_parser(
        "endpoints",
        help="Generate endpoint response coverage report",
        description="Map response schemas to generated DataObjects.",
    )
    endpoints_parser.add_argument(
        "ir_name",
        help="IR name to analyze",
    )
    endpoints_parser.add_argument(
        "--ir-dir",
        type=Path,
        help="Base directory containing IR folders",
    )
    endpoints_parser.add_argument(
        "--generated-dir",
        type=Path,
        help="Base directory containing generated output",
    )
    endpoints_parser.set_defaults(func=cmd_endpoints)

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
    packets_parser.add_argument(
        "--no-clean",
        action="store_true",
        help="Do not clear existing output before generating packets",
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
    gen_parser.add_argument(
        "--no-clean",
        action="store_true",
        help="Do not clear existing output before generating code",
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
