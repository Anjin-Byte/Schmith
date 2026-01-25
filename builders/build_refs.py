#!/usr/bin/env python3
"""Build IR reference topology indexes.

This builder processes existing IR schema files to extract reference
relationships between schemas (property refs, items refs, etc.).
Unlike other builders, this doesn't use adapters since the IR format
is adapter-agnostic.
"""
# pyright: reportUnknownVariableType=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownArgumentType=false
# pyright: reportUnnecessaryIsInstance=false
# pyright: reportOptionalIterable=false
import argparse
import json
import os
import sys
from typing import Any, Dict, List

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from pipeline.config import api_name, load_config

CONFIG_DEFAULT = os.path.join(ROOT, "config.toml")


def load_schema_files(spec_name: str) -> List[Dict[str, Any]]:
    schema_dir = os.path.join(ROOT, "ir", spec_name, "schemas")
    schemas: List[Dict[str, Any]] = []
    if not os.path.isdir(schema_dir):
        return schemas
    for filename in os.listdir(schema_dir):
        if not filename.endswith(".json"):
            continue
        if filename == "index.json":
            continue
        path = os.path.join(schema_dir, filename)
        with open(path, "r", encoding="utf-8") as handle:
            schemas.append(json.load(handle))
    return schemas


def build_edges(schemas: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    edges: List[Dict[str, Any]] = []
    for schema in schemas:
        schema_id = schema.get("id")
        if not schema_id:
            continue
        provenance = schema.get("provenance") or {}

        for field in schema.get("properties", []):
            if not isinstance(field, dict):
                continue
            target = field.get("schema_id")
            if not target:
                continue
            edges.append({
                "from_schema_id": schema_id,
                "from_json_pointer": field.get("json_pointer"),
                "to_schema_id": target,
                "kind": "property_ref",
                "provenance": field.get("provenance") or provenance,
            })

        items_schema_id = schema.get("items_schema_id")
        if items_schema_id:
            edges.append({
                "from_schema_id": schema_id,
                "from_json_pointer": "$[]",
                "to_schema_id": items_schema_id,
                "kind": "items_ref",
                "provenance": provenance,
            })

        additional_props_id = schema.get("additional_properties_schema_id")
        if additional_props_id:
            edges.append({
                "from_schema_id": schema_id,
                "from_json_pointer": "$.additionalProperties",
                "to_schema_id": additional_props_id,
                "kind": "additional_props_ref",
                "provenance": provenance,
            })

    return edges


def build_adjacency(edges: List[Dict[str, Any]]) -> Dict[str, Dict[str, List[Dict[str, Any]]]]:
    outgoing: Dict[str, List[Dict[str, Any]]] = {}
    incoming: Dict[str, List[Dict[str, Any]]] = {}
    for edge in edges:
        from_id = edge.get("from_schema_id")
        to_id = edge.get("to_schema_id")
        if from_id:
            outgoing.setdefault(from_id, []).append(edge)
        if to_id:
            incoming.setdefault(to_id, []).append(edge)
    return {"outgoing": outgoing, "incoming": incoming}


def write_refs(spec_name: str, edges: List[Dict[str, Any]]) -> None:
    refs_dir = os.path.join(ROOT, "ir", spec_name, "refs")
    os.makedirs(refs_dir, exist_ok=True)
    edges_path = os.path.join(refs_dir, "edges.json")
    adjacency_path = os.path.join(refs_dir, "adjacency.json")

    with open(edges_path, "w", encoding="utf-8") as handle:
        json.dump({"edges": edges}, handle, indent=2)
        handle.write("\n")

    adjacency = build_adjacency(edges)
    with open(adjacency_path, "w", encoding="utf-8") as handle:
        json.dump(adjacency, handle, indent=2)
        handle.write("\n")


def update_manifest(spec_name: str, edge_count: int) -> None:
    manifest_path = os.path.join(ROOT, "ir", spec_name, "manifest.json")
    if not os.path.exists(manifest_path):
        return
    with open(manifest_path, "r", encoding="utf-8") as handle:
        manifest = json.load(handle)
    manifest.setdefault("counts", {})["edges"] = edge_count
    with open(manifest_path, "w", encoding="utf-8") as handle:
        json.dump(manifest, handle, indent=2)
        handle.write("\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build IR reference topology indexes.")
    parser.add_argument("--config", default=CONFIG_DEFAULT, help="Path to config.toml.")
    args = parser.parse_args()

    config = load_config(args.config)
    spec_name = api_name(config)

    schemas = load_schema_files(spec_name)
    edges = build_edges(schemas)
    write_refs(spec_name, edges)
    update_manifest(spec_name, len(edges))
    print(f"Wrote {len(edges)} edges to ir/{spec_name}/refs")
    return 0


if __name__ == "__main__":
    sys.exit(main())
