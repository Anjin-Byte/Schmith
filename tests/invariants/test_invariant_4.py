#!/usr/bin/env python3
"""Invariant Test 4: Reference Edge Consistency

Validates that schema references in Domain 2 have corresponding edges in Domain 4.
"""
import argparse
import os
import sys
from typing import Any, Dict, List, Set, Tuple

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ROOT)
sys.path.append(SCRIPT_DIR)

from lib.ir_loader import IRDataLoader
from tests.invariants.framework import InvariantTest
from pipeline.config import api_name, load_config

CONFIG_DEFAULT = os.path.join(ROOT, "config.toml")


# Edge representation: (from_schema_id, to_schema_id, kind, json_pointer)
EdgeTuple = Tuple[str, str, str, str]


class ReferenceEdgeConsistencyTest(InvariantTest):
    """
    Test that all schema references in Domain 2 have corresponding edges in Domain 4.

    Verifies:
    - Every field's schema_id reference has a matching property_ref edge
    - Every items_schema_id has a matching items_ref edge
    - Every additional_properties_schema_id has a matching additional_props_ref edge
    - No extra edges exist in Domain 4 that aren't derived from Domain 2
    """

    # Primitive types that don't need edge tracking
    PRIMITIVE_TYPES = frozenset([
        "schema:types/string",
        "schema:types/integer",
        "schema:types/number",
        "schema:types/boolean",
        "schema:types/null",
        "schema:types/any",
        "schema:types/object",
        "schema:types/array",
    ])

    @property
    def invariant_id(self) -> str:
        return "invariant_4_reference_edge_consistency"

    @property
    def output_filename(self) -> str:
        return "invariant_4_reference_edge_consistency.json"

    def run_validation(self) -> List[Dict[str, Any]]:
        loader = IRDataLoader(self.root_dir, self.spec_name)
        schemas = loader.load_schemas()
        edges_data = loader.load_reference_edges()

        if edges_data is None:
            return [{
                "error": "refs/edges.json not found",
                "schema_id": None,
            }]

        # Build expected edges from Domain 2 schemas
        expected_edges = self._derive_expected_edges(schemas)

        # Build actual edges from Domain 4
        actual_edges = self._parse_actual_edges(edges_data)

        # Compare and find discrepancies
        failures = []

        # Group edges by from_schema_id for comparison
        expected_by_schema: Dict[str, Set[EdgeTuple]] = {}
        actual_by_schema: Dict[str, Set[EdgeTuple]] = {}

        for edge in expected_edges:
            expected_by_schema.setdefault(edge[0], set()).add(edge)

        for edge in actual_edges:
            actual_by_schema.setdefault(edge[0], set()).add(edge)

        # Find all schema IDs that have edges
        all_schema_ids = set(expected_by_schema.keys()) | set(actual_by_schema.keys())

        for schema_id in sorted(all_schema_ids):
            expected = expected_by_schema.get(schema_id, set())
            actual = actual_by_schema.get(schema_id, set())

            missing = expected - actual
            extra = actual - expected

            if missing or extra:
                failure: Dict[str, Any] = {"schema_id": schema_id}

                if missing:
                    failure["missing_edges"] = [
                        {
                            "to_schema_id": e[1],
                            "kind": e[2],
                            "json_pointer": e[3],
                        }
                        for e in sorted(missing)
                    ]

                if extra:
                    failure["extra_edges"] = [
                        {
                            "to_schema_id": e[1],
                            "kind": e[2],
                            "json_pointer": e[3],
                        }
                        for e in sorted(extra)
                    ]

                failures.append(failure)

        return failures

    def _derive_expected_edges(self, schemas: Dict[str, Dict[str, Any]]) -> Set[EdgeTuple]:
        """Derive expected edges from Domain 2 schema definitions."""
        edges: Set[EdgeTuple] = set()

        for schema_id, schema in schemas.items():
            # Skip primitive types
            if schema_id in self.PRIMITIVE_TYPES:
                continue

            # Property references
            properties = schema.get("properties") or []
            for prop in properties:
                ref_schema_id = prop.get("schema_id")
                json_pointer = prop.get("json_pointer") or f"$.{prop.get('json_name', '')}"

                if ref_schema_id and ref_schema_id not in self.PRIMITIVE_TYPES:
                    edges.add((schema_id, ref_schema_id, "property_ref", json_pointer))

                items_schema_id = prop.get("items_schema_id")
                if items_schema_id and items_schema_id not in self.PRIMITIVE_TYPES:
                    # Property-level array items should be represented in refs so adjacency
                    # captures nested array item relationships, not just array wrappers.
                    edges.add((schema_id, items_schema_id, "items_ref", f"{json_pointer}[]"))

            # Items reference (for arrays)
            items_schema_id = schema.get("items_schema_id")
            if items_schema_id and items_schema_id not in self.PRIMITIVE_TYPES:
                edges.add((schema_id, items_schema_id, "items_ref", "$[]"))

            # Additional properties reference (for maps)
            additional_props_schema_id = schema.get("additional_properties_schema_id")
            if additional_props_schema_id and additional_props_schema_id not in self.PRIMITIVE_TYPES:
                edges.add((schema_id, additional_props_schema_id, "additional_props_ref", "$.*"))

        return edges

    def _parse_actual_edges(self, edges_data: Dict[str, Any]) -> Set[EdgeTuple]:
        """Parse actual edges from Domain 4 refs/edges.json."""
        edges: Set[EdgeTuple] = set()

        for edge in edges_data.get("edges") or []:
            from_schema_id = edge.get("from_schema_id")
            to_schema_id = edge.get("to_schema_id")
            kind = edge.get("kind")
            json_pointer = edge.get("from_json_pointer") or ""

            # Normalize json_pointer for additional_props_ref
            # Both "$.additionalProperties" and "$.*" represent map value references
            if kind == "additional_props_ref":
                json_pointer = "$.*"

            # Skip edges to primitive types
            if to_schema_id in self.PRIMITIVE_TYPES:
                continue

            if from_schema_id and to_schema_id and kind:
                edges.add((from_schema_id, to_schema_id, kind, json_pointer))

        return edges


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate invariant 4 (reference edge consistency)."
    )
    parser.add_argument("--config", default=CONFIG_DEFAULT, help="Path to config.toml.")
    parser.add_argument("--verbose", "-v", action="store_true", help="Print detailed output")
    args = parser.parse_args()

    config = load_config(args.config)
    spec_name = api_name(config)

    test = ReferenceEdgeConsistencyTest(ROOT, spec_name)
    return test.run(verbose=args.verbose)


if __name__ == "__main__":
    sys.exit(main())
