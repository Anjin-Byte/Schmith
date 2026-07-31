"""CLI entry point for SpecBridge.

Usage:
    specbridge GET /customers
    specbridge GET /customers/{id} --config my_config.yaml
    specbridge POST /jobs --status 201 --dry-run
    specbridge GET /customers --debug

    # Run validation checks on a previously generated DataObject:
    specbridge validate output/GET_rest_v1.0_projects_{project_id}_timesheets/
    specbridge validate output/GET_rest_*/          # shell glob — multiple dirs
    specbridge validate output/ --fail-on-errors    # exit 1 if any errors found

The generate flow reads config.yaml (or the file passed via --config), then
delegates to pipeline.run() and writes to the output directory:
    ir.json               — type closure IR data
    schema.md             — human-readable schema summary
    <Name>DataObject.cs   — generated C# DataObject (derived from pages.json)
    codegen/prompts.json  — system+user prompt text for every codegen call
    codegen/pages.json    — raw codegen outputs (source of truth for assembly)
    pii/prompts.json      — prompt text for every PII classification call
    pii/pages.json        — raw PII classification outputs

The pii/ artefacts are written only when the PII pre-pass runs.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Protocol, cast


class _ConsolePrinter(Protocol):
    """Minimal structural interface for the rich Console we use."""

    def print(self, *args: Any, **kwargs: Any) -> None: ...


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
        result: Any = yaml.safe_load(f)

    if not isinstance(result, dict):
        return {}
    # Safe: yaml.safe_load on a well-formed config file produces str-keyed mappings.
    return cast(dict[str, Any], result)


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
    from specbridge.generation.type_mapping import format_data_object_name

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
    """Handle ``specbridge validate <dir> [<dir> ...]`` invocations.

    Each argument may be:
    - A generated output directory (contains ir.json + *.cs)
    - A direct path to a .cs file  (ir.json is resolved from the same directory)

    Shell glob expansion (``output/GET_*``) is supported naturally since the
    shell expands the pattern before passing arguments to the process.
    """
    parser = argparse.ArgumentParser(
        prog="specbridge validate",
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

    from rich.console import Console  # type: ignore[import-not-found]
    from specbridge.validation import print_validation_report, validate_generated_code

    # cast: Console satisfies _ConsolePrinter; needed because rich is not
    # resolvable by the IDE's interpreter (uv venv path mismatch).
    console: _ConsolePrinter = cast(_ConsolePrinter, Console(stderr=True))
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
            # Safe: json.load returns Any; ir.json is always a str-keyed object.
            ir_data: dict[str, Any] = cast(dict[str, Any], json.load(f))

        csharp_code = cs_path.read_text(encoding="utf-8")
        packet = _packet_from_ir(ir_data)

        # Safe: "endpoint" is always a dict in our ir.json output.
        ep: dict[str, Any] = cast(dict[str, Any], ir_data.get("endpoint") or {})
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
    # Dispatch `specbridge validate ...` before the normal method/path parser so
    # that the existing `specbridge GET /path` interface is fully preserved.
    if len(sys.argv) > 1 and sys.argv[1] == "validate":
        _main_validate(sys.argv[2:])
        return

    parser = argparse.ArgumentParser(
        prog="specbridge",
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

    pii_cfg: dict[str, Any] = config.get("pii") or {}

    codegen_cfg: dict[str, Any] = config.get("codegen") or {}
    fields_per_page: int | None = codegen_cfg.get("fields_per_page") or None
    enum_values_per_page: int | None = codegen_cfg.get("enum_values_per_page") or None
    _max_retries_cfg = codegen_cfg.get("max_retries")
    max_retries: int = int(_max_retries_cfg) if _max_retries_cfg is not None else 2

    # Safe: "output" section is always a dict when present in config.
    output_cfg: dict[str, Any] = cast(dict[str, Any], config.get("output") or {})
    output_base = Path(cast(str, output_cfg.get("dir") or "output"))

    # Import here so import errors surface with a clear message
    from specbridge.adapters.api import load_adapter
    from specbridge import pipeline
    from specbridge.pipeline import EndpointMatchError, SpecLoadError
    from specbridge import pipeline_invariants

    try:
        adapter = load_adapter(adapter_ref)
    except (ValueError, ImportError, AttributeError) as exc:
        print(f"Error loading adapter '{adapter_ref}': {exc}", file=sys.stderr)
        sys.exit(1)

    try:
        ir_data, schema_md, csharp_code, page_entries = pipeline.run(
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
            max_retries=max_retries,
            pii_config=pii_cfg,
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

    # ir.json  (excludes prompts and pii_log — those go to their own files)
    ir_path = output_dir / "ir.json"
    ir_without_logs = {k: v for k, v in ir_data.items() if k not in ("prompts", "pii_log")}
    with open(ir_path, "w", encoding="utf-8") as f:
        json.dump(ir_without_logs, f, indent=2, default=str)

    # codegen/  (codegen system+user prompts + raw LLM outputs per page)
    from specbridge.generation.pages import page_entry_to_dict
    from specbridge.shared.hashing import canonical_json_hash
    codegen_dir = output_dir / "codegen"
    codegen_dir.mkdir(exist_ok=True)
    # Safe: ir_without_logs is our own str-keyed dict.
    ir_hash = "sha1:" + canonical_json_hash(cast(dict[str, Any], ir_without_logs))
    with open(codegen_dir / "prompts.json", "w", encoding="utf-8") as f:
        json.dump(ir_data.get("prompts", []), f, indent=2, ensure_ascii=False)
    pages_envelope: dict[str, Any] = {
        "version": 1,
        "endpoint": cast(dict[str, Any], ir_data.get("endpoint") or {}),
        "ir_hash": ir_hash,
        "pages": [page_entry_to_dict(e) for e in page_entries],
    }
    with open(codegen_dir / "pages.json", "w", encoding="utf-8") as f:
        json.dump(pages_envelope, f, indent=2, ensure_ascii=False)

    # pii/  (PII classification prompts + raw LLM outputs, one entry per batch)
    pii_log_data: dict[str, Any] = cast(dict[str, Any], ir_data.get("pii_log") or {})
    if pii_log_data.get("pages"):
        pii_dir = output_dir / "pii"
        pii_dir.mkdir(exist_ok=True)
        with open(pii_dir / "prompts.json", "w", encoding="utf-8") as f:
            json.dump(pii_log_data.get("prompts", []), f, indent=2, ensure_ascii=False)
        pii_pages_envelope: dict[str, Any] = {
            "version": 1,
            "endpoint": cast(dict[str, Any], ir_data.get("endpoint") or {}),
            "ir_hash": ir_hash,
            "pages": pii_log_data.get("pages", []),
        }
        with open(pii_dir / "pages.json", "w", encoding="utf-8") as f:
            json.dump(pii_pages_envelope, f, indent=2, ensure_ascii=False)

    # schema.md
    schema_path = output_dir / "schema.md"
    schema_path.write_text(schema_md, encoding="utf-8")

    # <Name>DataObject.cs
    # Safe: "root_type" is always a dict in pipeline output; "name" is always str.
    root_type_ir: dict[str, Any] = cast(dict[str, Any], ir_data.get("root_type") or {})
    raw_name: str = cast(str, root_type_ir.get("name") or "DataObject")
    data_object_name: str = raw_name if raw_name.endswith("DataObject") else f"{raw_name}DataObject"
    cs_path = output_dir / f"{data_object_name}.cs"
    cs_path.write_text(csharp_code, encoding="utf-8")

    print(f"Output written to: {cs_path}")


if __name__ == "__main__":
    main()
