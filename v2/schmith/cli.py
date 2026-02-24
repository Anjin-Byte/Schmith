"""CLI entry point for Schmith v2.

Usage:
    schmith GET /customers
    schmith GET /customers/{id} --config my_config.yaml
    schmith POST /jobs --status 201 --dry-run
    schmith GET /customers --debug

The CLI reads config.yaml (or the file passed via --config), then delegates
to pipeline.run() and writes three artefacts to the output directory:
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


def main() -> None:
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

    print(f"Output written to {output_dir}/")
    print(f"  ir.json")
    print(f"  schema.md")
    print(f"  {data_object_name}.cs")
