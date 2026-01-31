"""Manifest generation for codegen outputs."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def _parent_schema(packet: dict) -> dict | None:
    for schema in packet.get("schemas", []):
        if schema.get("role") == "parent":
            return schema
    return None


def _nested_schemas(packet: dict) -> list[dict]:
    return [s for s in packet.get("schemas", []) if s.get("role") == "nested"]


def build_manifest(packets: list[dict], output_dir: Path, packets_dir: Path) -> dict[str, Any]:
    """Build a manifest dictionary from prompt packets."""
    if not packets:
        return {
            "manifest_version": "1.0",
            "generation": {"timestamp": datetime.now(timezone.utc).isoformat()},
            "outputs": {"root_dir": str(output_dir)},
            "counts": {"roots": 0, "nested_only": 0, "eligible": 0},
            "roots": [],
            "nested_only": [],
            "index": {"by_name": {}, "by_schema_id": {}, "by_root": {}},
        }

    ir_name = packets[0].get("metadata", {}).get("ir_name")
    grouped = packets[0].get("metadata", {}).get("is_grouped", True)

    roots = []
    nested_by_name: dict[str, str] = {}
    root_schema_names: set[str] = set()
    index_by_name: dict[str, dict[str, Any]] = {}
    index_by_schema_id: dict[str, str] = {}
    index_by_root: dict[str, list[str]] = {}

    for packet in packets:
        meta = packet.get("metadata", {})
        data_object_name = meta.get("data_object_name")
        parent = _parent_schema(packet)
        if not parent or not data_object_name:
            continue

        schema_name = parent.get("schema_name")
        schema_id = parent.get("schema_id")
        nested_names = parent.get("nested_type_names") or []

        root_schema_names.add(schema_name)
        index_by_root[data_object_name] = list(nested_names)
        if schema_id:
            index_by_schema_id[schema_id] = data_object_name

        entry = {
            "name": data_object_name,
            "schema_name": schema_name,
            "schema_id": schema_id,
            "nested_types": list(nested_names),
            "source_file": f"_source/{data_object_name}.cs",
            "schema_file": f"_schemas/{data_object_name}.md",
            "packet_file": f"{data_object_name}.json",
        }
        roots.append(entry)
        index_by_name[data_object_name] = entry

        for nested in _nested_schemas(packet):
            nested_name = nested.get("schema_name")
            nested_id = nested.get("schema_id")
            if nested_name and nested_id:
                nested_by_name.setdefault(nested_name, nested_id)

    nested_only = []
    for name, schema_id in sorted(nested_by_name.items()):
        if name in root_schema_names:
            continue
        nested_only.append({
            "name": name,
            "schema_id": schema_id,
            "parent_roots": [root for root, children in index_by_root.items() if name in children],
        })

    manifest = {
        "manifest_version": "1.0",
        "api": {
            "name": ir_name,
        },
        "generation": {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "grouped": bool(grouped),
            "packets_dir": str(packets_dir),
        },
        "outputs": {
            "root_dir": str(output_dir),
            "source_dir": str(output_dir / "_source"),
            "schemas_dir": str(output_dir / "_schemas"),
            "reports_dir": str(output_dir / "_reports"),
        },
        "counts": {
            "roots": len(roots),
            "nested_only": len(nested_only),
            "eligible": len(roots) + len(nested_only),
        },
        "roots": roots,
        "nested_only": nested_only,
        "index": {
            "by_name": index_by_name,
            "by_schema_id": index_by_schema_id,
            "by_root": index_by_root,
        },
    }

    return manifest


def write_manifest(packets: list[dict], output_dir: Path, packets_dir: Path) -> Path:
    """Write a manifest.json file to the output directory."""
    manifest = build_manifest(packets, output_dir, packets_dir)
    output_path = output_dir / "manifest.json"
    output_path.write_text(
        __import__("json").dumps(manifest, indent=2),
        encoding="utf-8",
    )
    return output_path
