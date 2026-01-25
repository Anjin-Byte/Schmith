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
from ingest.model import ResponseSchema
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


def signature_for_properties(properties: List[Any]) -> str:
    parts = []
    for prop in properties or []:
        if isinstance(prop, str):
            name = prop
            prop_type = "unknown"
        else:
            name = prop.get("name") or ""
            prop_type = prop.get("type") or "unknown"
        items_type = ""
        if prop_type == "array":
            items = prop.get("items") or {}
            items_type = items.get("type") or ""
        tokens = "_".join(normalize_tokens(name))
        parts.append(f"{tokens}:{prop_type}:{items_type}")
    parts.sort()
    signature = "|".join(parts)
    sig_hash = hashlib.sha256(signature.encode("utf-8")).hexdigest()[:16]
    return sig_hash


def detect_list_detail(entry: ResponseSchema) -> Tuple[str, Optional[str]]:
    root_type = entry.root_type
    properties = entry.properties or []
    if root_type == "array":
        items = entry.items or {}
        item_props = items.get("properties") or []
        return "list", signature_for_properties(item_props)
    if root_type == "object":
        items_prop = next((p for p in properties if p.get("name") == "items" and p.get("type") == "array"), None)
        if items_prop:
            items = items_prop.get("items") or {}
            item_props = items.get("properties") or []
            return "list", signature_for_properties(item_props)
        return "detail", signature_for_properties(properties)
    return "unknown", None


def main() -> int:
    parser = argparse.ArgumentParser(description="Identify list vs detail endpoints from an API spec.")
    parser.add_argument("--config", default=CONFIG_DEFAULT, help="Path to config.toml.")
    parser.add_argument("--adapter", default="raml", help="Spec adapter: raml or openapi.")
    parser.add_argument("--spec", default="", help="Optional path to spec file.")
    parser.add_argument("--out", default="", help="Optional path to output report JSON.")
    args = parser.parse_args()

    config = load_config(args.config)
    spec_path = resolve_spec_path(config, args.spec)
    out_path = resolve_report_path(config, "list_detail.json", args.out)

    adapter = load_adapter(args.adapter)
    spec = adapter.load_spec(spec_path)
    endpoints = list(adapter.iter_response_schemas(spec))

    report: Dict[str, Any] = {
        "specPath": spec_path,
        "endpointCount": len(endpoints),
        "listEndpoints": [],
        "detailEndpoints": [],
        "unclassified": [],
        "pairs": [],
    }

    list_by_path: Dict[str, List[Dict[str, Any]]] = {}
    detail_by_path: Dict[str, List[Dict[str, Any]]] = {}

    for entry in endpoints:
        kind, sig_hash = detect_list_detail(entry)
        record = {
            "method": entry.method,
            "path": entry.path,
            "code": entry.code,
            "signature": sig_hash,
        }
        if kind == "list":
            report["listEndpoints"].append(record)
            list_by_path.setdefault(entry.path, []).append(record)
        elif kind == "detail":
            report["detailEndpoints"].append(record)
            detail_by_path.setdefault(entry.path, []).append(record)
        else:
            report["unclassified"].append(record)

    # Pair list/detail by shared signature regardless of path
    details_by_sig: Dict[str, List[Dict[str, Any]]] = {}
    for detail in report["detailEndpoints"]:
        details_by_sig.setdefault(detail["signature"], []).append(detail)

    for list_item in report["listEndpoints"]:
        matches = details_by_sig.get(list_item["signature"], [])
        if matches:
            report["pairs"].append({
                "list": list_item,
                "details": matches,
            })

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as handle:
        json.dump(report, handle, indent=2)
        handle.write("\n")

    print(f"Wrote list/detail report to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
