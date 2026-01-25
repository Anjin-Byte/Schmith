#!/usr/bin/env python3
import argparse
import hashlib
import json
import os
import re
import sys
from typing import Any, Dict, List, Optional, Tuple

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ROOT)
sys.path.append(SCRIPT_DIR)

from ingest.adapter import load_adapter
from pipeline.config import load_config, resolve_report_path, resolve_spec_path
CONFIG_DEFAULT = os.path.join(ROOT, "config.toml")


TOKEN_SPLIT_RE = re.compile(r"(?<!^)(?=[A-Z])")


def normalize_tokens(text: Optional[str]) -> List[str]:
    if not text:
        return []
    text = TOKEN_SPLIT_RE.sub(" ", text)
    text = re.sub(r"[^A-Za-z0-9]+", " ", text)
    tokens = [t.lower() for t in text.split() if t]
    return tokens


def signature_for_fields(fields: List[Dict[str, Any]]) -> Tuple[str, str]:
    parts = []
    for field in fields:
        name = field.get("name") or ""
        field_type = field.get("type") or "unknown"
        items_type = field.get("itemsType") or ""
        name_tokens = normalize_tokens(name)
        token_blob = "_".join(name_tokens)
        parts.append(f"{token_blob}:{field_type}:{items_type}")
    parts.sort()
    signature = "|".join(parts)
    sig_hash = hashlib.sha256(signature.encode("utf-8")).hexdigest()[:16]
    return signature, sig_hash


def extract_objects_from_properties(
    properties: Optional[List[Dict[str, Any]]],
    path: str,
    objects: List[Dict[str, Any]],
    parent_sig: Optional[str] = None,
    container_field: Optional[str] = None,
    container_type: Optional[str] = None,
) -> None:
    if not properties:
        return
    fields = []
    field_names = []
    for prop in properties:
        name = prop.get("name")
        prop_type = prop.get("type")
        items = prop.get("items") if prop_type == "array" else None
        if name:
            field_names.append(name)
        fields.append({
            "name": name,
            "type": prop_type,
            "itemsType": items.get("type") if isinstance(items, dict) else None,
            "items": items,
        })

    signature, sig_hash = signature_for_fields(fields)
    objects.append({
        "path": path,
        "signature": signature,
        "sigHash": sig_hash,
        "fields": fields,
        "fieldNames": field_names,
        "parentSigHash": parent_sig,
        "containerField": container_field,
        "containerType": container_type,
    })

    for prop in properties:
        name = prop.get("name")
        prop_type = prop.get("type")
        child_path = f"{path}.{name}" if name else path

        if prop_type == "object" and prop.get("properties"):
            extract_objects_from_properties(
                prop.get("properties"),
                child_path,
                objects,
                parent_sig=sig_hash,
                container_field=name,
                container_type="object",
            )
        if prop_type == "array":
            items = prop.get("items")
            if isinstance(items, dict) and items.get("type") == "object" and items.get("properties"):
                extract_objects_from_properties(
                    items.get("properties"),
                    f"{child_path}[]",
                    objects,
                    parent_sig=sig_hash,
                    container_field=name,
                    container_type="array",
                )


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a type relationship graph from the Service Fusion spec.")
    parser.add_argument("--config", default=CONFIG_DEFAULT, help="Path to config.toml.")
    parser.add_argument("--spec", default="", help="Path to spec file.")
    parser.add_argument("--adapter", default="raml", help="Spec adapter: raml or openapi.")
    parser.add_argument("--out", default="", help="Path to write type graph JSON.")
    parser.add_argument("--common-out", default="", help="Path to write common nodes JSON.")
    parser.add_argument("--min-degree", type=int, default=2, help="Minimum parents to qualify as common node.")
    args = parser.parse_args()

    config = load_config(args.config)
    spec_path = resolve_spec_path(config, args.spec)
    graph_path = resolve_report_path(config, "type_graph.json", args.out)
    common_path = resolve_report_path(config, "common_nodes.json", args.common_out)

    adapter = load_adapter(args.adapter)
    spec = adapter.load_spec(spec_path)
    endpoints = list(adapter.iter_response_schemas(spec))

    objects: List[Dict[str, Any]] = []
    for endpoint in endpoints:
        base = f"{endpoint.method.upper()} {endpoint.path} {endpoint.code}"
        properties = endpoint.properties
        extract_objects_from_properties(properties, base, objects)

    nodes: Dict[str, Dict[str, Any]] = {}
    edges: List[Dict[str, Any]] = []

    for obj in objects:
        sig = obj["sigHash"]
        node = nodes.setdefault(sig, {
            "sigHash": sig,
            "signature": obj["signature"],
            "fieldNames": sorted(set(obj["fieldNames"])),
            "occurrences": [],
        })
        node["occurrences"].append({
            "path": obj["path"],
            "containerField": obj.get("containerField"),
            "containerType": obj.get("containerType"),
        })
        if obj.get("parentSigHash"):
            edges.append({
                "from": obj["parentSigHash"],
                "to": sig,
                "containerField": obj.get("containerField"),
                "containerType": obj.get("containerType"),
                "path": obj.get("path"),
            })

    # compute parent counts
    parent_counts: Dict[str, set[str]] = {}
    for edge in edges:
        parent_counts.setdefault(edge["to"], set()).add(edge["from"])

    common_nodes: List[Dict[str, Any]] = []
    for sig, parents in parent_counts.items():
        if len(parents) >= args.min_degree:
            node = nodes.get(sig, {})
            common_nodes.append({
                "sigHash": sig,
                "parentCount": len(parents),
                "fieldNames": node.get("fieldNames", []),
                "occurrences": node.get("occurrences", []),
            })

    common_nodes.sort(key=lambda x: (-x["parentCount"], x["sigHash"]))

    os.makedirs(os.path.dirname(graph_path), exist_ok=True)
    with open(graph_path, "w", encoding="utf-8") as handle:
        json.dump({"nodes": list(nodes.values()), "edges": edges}, handle, indent=2)
        handle.write("\n")

    with open(common_path, "w", encoding="utf-8") as handle:
        json.dump({"commonNodes": common_nodes}, handle, indent=2)
        handle.write("\n")

    print(f"Wrote graph to {graph_path}")
    print(f"Wrote common nodes to {common_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
