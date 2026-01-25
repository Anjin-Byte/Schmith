#!/usr/bin/env python3
import argparse
import json
import os
import sys
from collections import Counter
from typing import Any, Dict, List, Optional


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_DEFAULT = os.path.join(ROOT, "reports", "common_nodes.json")
OUTPUT_DEFAULT = os.path.join(ROOT, "reports", "common_data_objects.json")


def to_pascal_case(name: Optional[str]) -> str:
    if not name:
        return "CommonType"
    parts = []
    for token in name.replace("-", "_").split("_"):
        if not token:
            continue
        parts.append(token[:1].upper() + token[1:])
    return "".join(parts)


def main() -> int:
    parser = argparse.ArgumentParser(description="Summarize common nodes into candidate data objects.")
    parser.add_argument("--in", dest="input_path", default=INPUT_DEFAULT, help="Path to common_nodes.json")
    parser.add_argument("--out", dest="output_path", default=OUTPUT_DEFAULT, help="Path to write report JSON")
    args = parser.parse_args()

    with open(args.input_path, "r", encoding="utf-8") as handle:
        data = json.load(handle)

    report: List[Dict[str, Any]] = []
    for node in data.get("commonNodes", []):
        occurrences = node.get("occurrences", [])
        name_counts = Counter(o.get("containerField") for o in occurrences if o.get("containerField"))
        if name_counts:
            most_common_name, _ = name_counts.most_common(1)[0]
        else:
            most_common_name = "common_type"

        report.append({
            "sigHash": node.get("sigHash"),
            "suggestedName": to_pascal_case(most_common_name),
            "originalNames": sorted(name_counts.keys()),
            "parentCount": node.get("parentCount"),
            "fieldNames": node.get("fieldNames", []),
            "occurrences": occurrences,
        })

    report.sort(key=lambda x: (-x["parentCount"], x["suggestedName"]))

    os.makedirs(os.path.dirname(args.output_path), exist_ok=True)
    with open(args.output_path, "w", encoding="utf-8") as handle:
        json.dump({"commonDataObjects": report}, handle, indent=2)
        handle.write("\n")

    print(f"Wrote common data object report to {args.output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
