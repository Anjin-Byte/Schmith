"""CLI entry point for Schmith v2.

Usage:
    schmith GET /customers
    schmith GET /customers/{id} --config my_config.yaml
    schmith POST /jobs --status 201 --dry-run
    schmith GET /customers --debug

    # Run validation checks on a previously generated DataObject:
    schmith validate output/GET_rest_v1.0_projects_{project_id}_timesheets/
    schmith validate output/GET_rest_*/          # shell glob — multiple dirs
    schmith validate output/ --fail-on-errors    # exit 1 if any errors found

The generate flow reads config.yaml (or the file passed via --config), then
delegates to pipeline.run() and writes three artefacts to the output directory:
    ir.json           — type closure IR data
    schema.md         — human-readable schema summary
    <Name>DataObject.cs — generated C# DataObject
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def _load_config(config_path: str) -> dict[str, Any]:
    try:
        import yaml  # type: ignore[import-untyped]
    except ImportError:
        print("Error: pyyaml not installed. Run: pip install pyyaml", file=sys.stderr)
        sys.exit(1)

    path = Path(config_path)
    if not path.exists():
        print(f"Error: config file not found: {config_path}", file=sys.stderr)
        sys.exit(1)

    with open(path, encoding="utf-8") as f:
        result = yaml.safe_load(f)

    return result if isinstance(result, dict) else {}


def _path_slug(path: str) -> str:
    """Convert an endpoint path to a filesystem-safe slug.

    /customers/{id} → customers_{id}
    """
    slug = path.strip("/").replace("/", "_")
    # Trim leading/trailing underscores from repeated slashes
    slug = slug.strip("_") or "root"
    return slug


def _packet_from_ir(ir_data: dict[str, Any]) -> dict[str, Any]:
    """Reconstruct a minimal validation packet from ir.json contents.

    Only the fields required by validate_generated_code are populated:
    metadata (method, path, data_object_name), root/nested type names,
    and the json_name of every field. Full csharp_type resolution is
    skipped because it is not needed for any validation check.
    """
    from schmith.generation.type_mapping import format_data_object_name

    def _to_entry(type_dict: dict[str, Any]) -> dict[str, Any]:
        props: list[dict[str, Any]] = type_dict.get("properties") or []
        fields = [{"json_name": p["json_name"]} for p in props if p.get("json_name")]
        return {
            "name": type_dict.get("name") or "",
            "fields": fields,
            "enum_values": type_dict.get("enum_values"),
        }

    endpoint: dict[str, Any] = ir_data.get("endpoint") or {}
    root_type: dict[str, Any] = ir_data.get("root_type") or {}
    nested_types: list[dict[str, Any]] = ir_data.get("nested_types") or []

    root_entry = _to_entry(root_type)
    return {
        "metadata": {
            "method": endpoint.get("method") or "",
            "path": endpoint.get("path") or "",
            "data_object_name": format_data_object_name(str(root_entry["name"])),
            "response_description": "",
        },
        "root": root_entry,
        "nested_types": [_to_entry(nt) for nt in nested_types],
    }


def _main_validate(argv: list[str]) -> None:
    """Handle ``schmith validate <dir> [<dir> ...]`` invocations.

    Each argument may be:
    - A generated output directory (contains ir.json + *.cs)
    - A direct path to a .cs file  (ir.json is resolved from the same directory)

    Shell glob expansion (``output/GET_*``) is supported naturally since the
    shell expands the pattern before passing arguments to the process.
    """
    parser = argparse.ArgumentParser(
        prog="schmith validate",
        description="Run deterministic validation checks on previously generated DataObjects.",
    )
    parser.add_argument(
        "dirs",
        nargs="+",
        metavar="DIR",
        help="Output directory (or .cs file) to validate. Accepts multiple paths.",
    )
    parser.add_argument(
        "--fail-on-errors",
        action="store_true",
        help="Exit with status 1 if validation errors are found in any target.",
    )
    args = parser.parse_args(argv)

    from rich.console import Console
    from schmith.validation import print_validation_report, validate_generated_code

    console = Console(stderr=True)
    any_errors = False

    for raw_path in args.dirs:
        target = Path(raw_path)

        # Accept either a directory or a direct .cs file path.
        if target.is_file() and target.suffix == ".cs":
            output_dir = target.parent
        elif target.is_dir():
            output_dir = target
        else:
            console.print(f"[red]Error:[/red] not found: {raw_path}", highlight=False)
            any_errors = True
            continue

        ir_path = output_dir / "ir.json"
        if not ir_path.exists():
            console.print(
                f"[red]Error:[/red] ir.json not found in {output_dir}",
                highlight=False,
            )
            any_errors = True
            continue

        cs_files = sorted(output_dir.glob("*.cs"))
        if not cs_files:
            console.print(
                f"[red]Error:[/red] no .cs file found in {output_dir}",
                highlight=False,
            )
            any_errors = True
            continue

        cs_path = cs_files[0]
        if len(cs_files) > 1:
            console.print(
                f"[yellow]Warning:[/yellow] multiple .cs files in {output_dir};"
                f" validating {cs_path.name}",
                highlight=False,
            )

        with open(ir_path, encoding="utf-8") as f:
            ir_data = json.load(f)

        csharp_code = cs_path.read_text(encoding="utf-8")
        packet = _packet_from_ir(ir_data)

        ep = ir_data.get("endpoint") or {}
        endpoint_label = f"{ep.get('method', '')} {ep.get('path', '')}".strip()
        console.print(
            f"\n[bold]Validating[/bold] [cyan]{cs_path.name}[/cyan]"
            f"  [dim]{endpoint_label}[/dim]"
        )

        result = validate_generated_code(csharp_code, packet)
        print_validation_report(result, console)

        if result.has_errors:
            any_errors = True

    if args.fail_on_errors and any_errors:
        sys.exit(1)


def main() -> None:
    # Dispatch `schmith validate ...` before the normal method/path parser so
    # that the existing `schmith GET /path` interface is fully preserved.
    if len(sys.argv) > 1 and sys.argv[1] == "validate":
        _main_validate(sys.argv[2:])
        return

    parser = argparse.ArgumentParser(
        prog="schmith",
        description="Generate a C# DataObject for a single API endpoint.",
    )
    parser.add_argument(
        "method",
        metavar="METHOD",
        help="HTTP method (GET, POST, PUT, PATCH, DELETE, …)",
    )
    parser.add_argument(
        "path",
        metavar="PATH",
        help="Endpoint path template, e.g. /customers/{id}",
    )
    parser.add_argument(
        "--config",
        default="config.yaml",
        metavar="FILE",
        help="Path to config.yaml (default: config.yaml)",
    )
    parser.add_argument(
        "--status",
        default="200",
        metavar="CODE",
        help="Preferred response status code (default: 200)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Skip the LLM call — useful for validating spec parsing",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Run pipeline invariant checks after each stage",
    )

    args = parser.parse_args()

    config = _load_config(args.config)
    api_cfg: dict[str, Any] = config.get("api") or {}

    spec_path: str = api_cfg.get("spec") or ""
    if not spec_path:
        print("Error: config.yaml must set api.spec", file=sys.stderr)
        sys.exit(1)

    spec_format: str = api_cfg.get("format") or "openapi"
    adapter_ref: str | None = api_cfg.get("adapter") or None

    llm_config: dict[str, Any] = dict(config.get("llm") or {})
    if args.dry_run:
        llm_config["dry_run"] = True

    codegen_cfg: dict[str, Any] = config.get("codegen") or {}
    fields_per_page: int | None = codegen_cfg.get("fields_per_page") or None
    enum_values_per_page: int | None = codegen_cfg.get("enum_values_per_page") or None

    output_base = Path((config.get("output") or {}).get("dir") or "output")

    # Import here so import errors surface with a clear message
    from schmith.adapters.api import load_adapter
    from schmith import pipeline
    from schmith.pipeline import EndpointMatchError, SpecLoadError
    from schmith import pipeline_invariants

    try:
        adapter = load_adapter(adapter_ref)
    except (ValueError, ImportError, AttributeError) as exc:
        print(f"Error loading adapter '{adapter_ref}': {exc}", file=sys.stderr)
        sys.exit(1)

    try:
        ir_data, schema_md, csharp_code = pipeline.run(
            spec_path=spec_path,
            spec_format=spec_format,
            method=args.method,
            path=args.path,
            adapter=adapter,
            llm_config=llm_config,
            target_status=args.status,
            debug=args.debug,
            fields_per_page=fields_per_page,
            enum_values_per_page=enum_values_per_page,
        )
    except SpecLoadError as exc:
        print(f"Spec load error: {exc}", file=sys.stderr)
        sys.exit(1)
    except EndpointMatchError as exc:
        print(f"Endpoint not found: {exc}", file=sys.stderr)
        sys.exit(1)
    except pipeline_invariants.InvariantViolation as exc:
        print(f"Pipeline invariant violated:\n{exc}", file=sys.stderr)
        sys.exit(1)
    except Exception as exc:
        print(f"Unexpected error: {exc}", file=sys.stderr)
        if args.debug:
            import traceback
            traceback.print_exc()
        sys.exit(1)

    # ------------------------------------------------------------------
    # Write output artefacts
    # ------------------------------------------------------------------
    method_upper = args.method.upper()
    slug = _path_slug(args.path)
    output_dir = output_base / f"{method_upper}_{slug}"
    output_dir.mkdir(parents=True, exist_ok=True)

    # ir.json
    ir_path = output_dir / "ir.json"
    with open(ir_path, "w", encoding="utf-8") as f:
        json.dump(ir_data, f, indent=2, default=str)

    # schema.md
    schema_path = output_dir / "schema.md"
    schema_path.write_text(schema_md, encoding="utf-8")

    # <Name>DataObject.cs
    raw_name: str = (ir_data.get("root_type") or {}).get("name") or "DataObject"
    data_object_name = raw_name if raw_name.endswith("DataObject") else f"{raw_name}DataObject"
    cs_path = output_dir / f"{data_object_name}.cs"
    cs_path.write_text(csharp_code, encoding="utf-8")

    print(f"Output written to: ./v2/{output_dir}/{data_object_name}.cs")
