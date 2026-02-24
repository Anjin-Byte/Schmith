#!/usr/bin/env python3
"""Invariant Test 2: Field Name Serialization Consistency"""
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


class FieldNameSerializationTest(InvariantTest):
    """
    Test that field names are consistent between schema definitions and serialization indexes.

    Verifies:
    - Every field (property) defined in a schema appears in the serialization json_paths
    - No extra fields are listed in serialization that aren't in the schema definition
    """

    @property
    def invariant_id(self) -> str:
        return "invariant_2_field_name_serialization"

    @property
    def output_filename(self) -> str:
        return "invariant_2_field_name_serialization.json"

    def run_validation(self) -> List[Dict[str, Any]]:
        loader = IRDataLoader(self.root_dir, self.spec_name)
        schema_fields = self._load_schema_fields(loader)
        serialization_fields = self._load_serialization_fields(loader)

        failures = []
        all_schema_ids = set(schema_fields.keys()) | set(serialization_fields.keys())

        for schema_id in sorted(all_schema_ids):
            schema_names = schema_fields.get(schema_id, set())
            serialization_names = serialization_fields.get(schema_id, set())

            missing = sorted(schema_names - serialization_names)
            extra = sorted(serialization_names - schema_names)

            if missing or extra:
                failures.append({
                    "schema_id": schema_id,
                    "missing_in_serialization": missing,
                    "extra_in_serialization": extra,
                })

        return failures

    def _load_schema_fields(self, loader: IRDataLoader) -> Dict[str, Set[str]]:
        """Extract field names from schema definitions."""
        schemas = loader.load_schemas()
        schema_fields: Dict[str, Set[str]] = {}

        for schema_id, schema in schemas.items():
            fields = set()
            for field in schema.get("properties", []):
                if isinstance(field, dict):
                    name = field.get("json_name")
                    if isinstance(name, str):
                        fields.add(name)
            schema_fields[schema_id] = fields

        return schema_fields

    def _load_serialization_fields(self, loader: IRDataLoader) -> Dict[str, Set[str]]:
        """Extract field names from serialization json_paths."""
        data = loader.load_serialization_json_paths()
        schemas = data.get("schemas") or {}
        serialization_fields: Dict[str, Set[str]] = {}

        for schema_id, pointers in schemas.items():
            if not isinstance(pointers, list):
                continue
            names = set()
            for pointer in pointers:
                if not isinstance(pointer, str):
                    continue
                if pointer.startswith("$."):
                    names.add(pointer[2:])
            serialization_fields[schema_id] = names

        return serialization_fields


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate invariant 2 (field name serialization consistency)."
    )
    parser.add_argument("--config", default=CONFIG_DEFAULT, help="Path to config.toml.")
    parser.add_argument("--verbose", action="store_true", help="Print detailed output")
    args = parser.parse_args()

    config = load_config(args.config)
    spec_name = api_name(config)

    test = FieldNameSerializationTest(ROOT, spec_name)
    return test.run(verbose=args.verbose)


if __name__ == "__main__":
    sys.exit(main())
