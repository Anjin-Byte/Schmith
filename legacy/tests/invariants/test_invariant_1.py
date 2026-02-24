#!/usr/bin/env python3
"""Invariant Test 1: Operation Schema Usage Consistency"""
import argparse
import os
import sys
from typing import Any, Dict, List, Set

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ROOT)
sys.path.append(SCRIPT_DIR)

from lib.ir_loader import IRDataLoader
from tests.invariants.framework import InvariantTest
from pipeline.config import api_name, load_config

CONFIG_DEFAULT = os.path.join(ROOT, "config.toml")


class OperationSchemaUsageTest(InvariantTest):
    """
    Test that schemas referenced in operations have matching backlinks in the schema index.

    Verifies:
    - Every schema referenced in an operation's request/response bodies
      appears in that operation's where_used list in the schema index
    - No extra schemas are listed in where_used that aren't actually referenced
    """

    @property
    def invariant_id(self) -> str:
        return "invariant_1_operation_schema_usage"

    @property
    def output_filename(self) -> str:
        return "invariant_1_operation_schema_usage.json"

    def run_validation(self) -> List[Dict[str, Any]]:
        loader = IRDataLoader(self.root_dir, self.spec_name)
        operations = loader.load_operations()
        backlinks = self._load_schema_backlinks(loader)

        failures = []
        for operation in operations:
            op_id = operation.get("id")
            if not op_id:
                continue

            op_schemas = self._extract_operation_schemas(operation)
            backlink_schemas = backlinks.get(op_id, set())

            missing = sorted(op_schemas - backlink_schemas)
            extra = sorted(backlink_schemas - op_schemas)

            if missing or extra:
                failures.append({
                    "operation_id": op_id,
                    "missing_in_backlinks": missing,
                    "extra_in_backlinks": extra,
                    "topology_check": "not_applicable",
                })

        return failures

    def _extract_operation_schemas(self, operation: Dict[str, Any]) -> Set[str]:
        """Extract all schema IDs referenced in an operation's request/response bodies."""
        schema_ids: Set[str] = set()
        for surface_key in ("declared", "effective"):
            surface = operation.get(surface_key) or {}
            for body in surface.get("request_bodies", []):
                schema_id = body.get("schema_id") if isinstance(body, dict) else None
                if schema_id:
                    schema_ids.add(schema_id)
            for response in surface.get("responses", []):
                schema_id = response.get("schema_id") if isinstance(response, dict) else None
                if schema_id:
                    schema_ids.add(schema_id)
        return schema_ids

    def _load_schema_backlinks(self, loader: IRDataLoader) -> Dict[str, Set[str]]:
        """Load where_used backlinks from the schema index."""
        index_data = loader.load_schema_index()
        backlinks: Dict[str, Set[str]] = {}
        for entry in index_data.get("schemas", []):
            schema_id = entry.get("schema_id")
            for op_id in entry.get("where_used", []) or []:
                if not schema_id or not op_id:
                    continue
                backlinks.setdefault(op_id, set()).add(schema_id)
        return backlinks


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate invariant 1 (operation-schema usage consistency)."
    )
    parser.add_argument("--config", default=CONFIG_DEFAULT, help="Path to config.toml.")
    parser.add_argument("--verbose", action="store_true", help="Print detailed output")
    args = parser.parse_args()

    config = load_config(args.config)
    spec_name = api_name(config)

    test = OperationSchemaUsageTest(ROOT, spec_name)
    return test.run(verbose=args.verbose)


if __name__ == "__main__":
    sys.exit(main())
