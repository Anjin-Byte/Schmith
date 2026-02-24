"""Endpoint coverage report (responses -> DataObjects)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from ..ir.loader import IRLoader


def _load_manifest(manifest_path: Path) -> dict[str, Any]:
    if not manifest_path.exists():
        return {}
    return json.loads(manifest_path.read_text())


def _manifest_schema_map(manifest: dict[str, Any]) -> dict[str, dict[str, str]]:
    """Return schema_id -> {name, kind} map from manifest."""
    mapping: dict[str, dict[str, str]] = {}
    for entry in manifest.get("roots", []):
        schema_id = entry.get("schema_id")
        if schema_id:
            mapping[schema_id] = {"name": entry.get("name", ""), "kind": "root"}
    for entry in manifest.get("nested_only", []):
        schema_id = entry.get("schema_id")
        if schema_id and schema_id not in mapping:
            mapping[schema_id] = {"name": entry.get("name", ""), "kind": "nested_only"}
    return mapping


def build_endpoints_report(
    ir_name: str,
    ir_dir: Path,
    generated_dir: Path,
) -> str:
    """Build a markdown report mapping endpoint responses to DataObjects."""
    loader = IRLoader(ir_name, ir_dir)
    operations = loader.operations()

    manifest_path = generated_dir / ir_name / "manifest.json"
    manifest = _load_manifest(manifest_path)
    schema_map = _manifest_schema_map(manifest)

    rows: list[tuple[str, str, str, str, str]] = []
    response_schemas: set[str] = set()
    unmapped: set[str] = set()

    for op in operations:
        method = op.get("method", "")
        path = op.get("path", "")
        responses = op.get("responses") or []
        for schema_id in responses:
            response_schemas.add(schema_id)
            mapped = schema_map.get(schema_id)
            if mapped:
                rows.append((method, path, schema_id, mapped["name"], mapped["kind"]))
            else:
                unmapped.add(schema_id)
                rows.append((method, path, schema_id, "", "missing"))

    mapped_count = len(response_schemas) - len(unmapped)

    lines: list[str] = []
    lines.append(f"# Endpoint Response Coverage: {ir_name}")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("| Metric | Count |")
    lines.append("|--------|-------|")
    lines.append(f"| Total endpoints | {len(operations)} |")
    lines.append(f"| Total response schemas | {len(response_schemas)} |")
    lines.append(f"| Mapped response schemas | {mapped_count} |")
    lines.append(f"| Unmapped response schemas | {len(unmapped)} |")
    lines.append("")

    lines.append("## Endpoint Responses")
    lines.append("")
    lines.append("| Method | Path | Response Schema | DataObject | Mapping |")
    lines.append("|--------|------|-----------------|-----------|---------|")
    for method, path, schema_id, name, kind in rows:
        data_object = name or ""
        mapping = kind
        lines.append(f"| `{method}` | `{path}` | `{schema_id}` | `{data_object}` | `{mapping}` |")

    if unmapped:
        lines.append("")
        lines.append("## Unmapped Schemas")
        lines.append("")
        for schema_id in sorted(unmapped):
            lines.append(f"- `{schema_id}`")

    lines.append("")
    return "\n".join(lines)


def write_endpoints_report(
    ir_name: str,
    ir_dir: Path,
    generated_dir: Path,
) -> Path:
    """Write the endpoint coverage report and return its path."""
    report = build_endpoints_report(ir_name, ir_dir, generated_dir)
    report_dir = generated_dir / ir_name / "_reports"
    report_dir.mkdir(parents=True, exist_ok=True)
    report_path = report_dir / "endpoints.md"
    report_path.write_text(report, encoding="utf-8")
    return report_path
