#!/usr/bin/env python3
"""Invariant Test 5: Provenance Coverage Consistency

Validates that all analysis-relevant facts in Domains 1-4 carry provenance
at the required granularity (source_file, source_pointer, via chain).
"""
import argparse
import os
import sys
from typing import Any, Dict, List, Optional

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ROOT)
sys.path.append(SCRIPT_DIR)

from lib.ir_loader import IRDataLoader
from tests.invariants.framework import InvariantTest
from pipeline.config import api_name, load_config

CONFIG_DEFAULT = os.path.join(ROOT, "config.toml")


class ProvenanceCoverageTest(InvariantTest):
    """
    Test that all items across Domains 1-4 have proper provenance information.

    Verifies:
    - Operations have provenance (Domain 1)
    - Operation parameters, request bodies, and responses have provenance
    - Schemas have provenance (Domain 2)
    - Schema fields have provenance
    - Reference edges have provenance (Domain 4)
    """

    @property
    def invariant_id(self) -> str:
        return "invariant_5_provenance_coverage"

    @property
    def output_filename(self) -> str:
        return "invariant_5_provenance_coverage.json"

    def run_validation(self) -> List[Dict[str, Any]]:
        loader = IRDataLoader(self.root_dir, self.spec_name)
        failures: List[Dict[str, Any]] = []

        # Domain 1: Operations
        failures.extend(self._validate_operations(loader))

        # Domain 2: Schemas
        failures.extend(self._validate_schemas(loader))

        # Domain 4: Reference Edges
        failures.extend(self._validate_edges(loader))

        return failures

    def _validate_provenance(
        self,
        provenance: Optional[Dict[str, Any]],
        require_via: bool = False
    ) -> List[str]:
        """
        Validate a provenance object has required fields.

        Args:
            provenance: The provenance dict to validate
            require_via: Whether 'via' field is required

        Returns:
            List of missing field names
        """
        missing = []

        if provenance is None:
            return ["provenance (missing entirely)"]

        if not isinstance(provenance, dict):
            return ["provenance (invalid type)"]

        if not provenance.get("source_file"):
            missing.append("source_file")

        if not provenance.get("source_pointer"):
            missing.append("source_pointer")

        if require_via and "via" not in provenance:
            missing.append("via")

        return missing

    def _validate_operations(self, loader: IRDataLoader) -> List[Dict[str, Any]]:
        """Validate provenance for Domain 1: Operations."""
        failures = []
        operations = loader.load_operations()

        for operation in operations:
            op_id = operation.get("id") or "unknown"

            # Check operation-level provenance
            op_provenance = operation.get("provenance")
            missing = self._validate_provenance(op_provenance)
            if missing:
                failures.append({
                    "domain": "operations",
                    "item_type": "operation",
                    "identifier": op_id,
                    "missing_fields": missing,
                })

            # Check declared/effective surfaces
            for surface_key in ("declared", "effective"):
                surface = operation.get(surface_key) or {}

                # Check parameters
                for param in surface.get("parameters") or []:
                    param_name = param.get("name") or "unknown"
                    param_prov = param.get("provenance")
                    missing = self._validate_provenance(param_prov)
                    if missing:
                        failures.append({
                            "domain": "operations",
                            "item_type": f"parameter ({surface_key})",
                            "identifier": f"{op_id}:param:{param_name}",
                            "missing_fields": missing,
                        })

                # Check request bodies
                for body in surface.get("request_bodies") or []:
                    media_type = body.get("media_type") or "unknown"
                    body_prov = body.get("provenance")
                    missing = self._validate_provenance(body_prov)
                    if missing:
                        failures.append({
                            "domain": "operations",
                            "item_type": f"request_body ({surface_key})",
                            "identifier": f"{op_id}:request:{media_type}",
                            "missing_fields": missing,
                        })

                # Check responses
                for response in surface.get("responses") or []:
                    status = response.get("status_code") or "unknown"
                    media = response.get("media_type") or "unknown"
                    resp_prov = response.get("provenance")
                    missing = self._validate_provenance(resp_prov)
                    if missing:
                        failures.append({
                            "domain": "operations",
                            "item_type": f"response ({surface_key})",
                            "identifier": f"{op_id}:response:{status}:{media}",
                            "missing_fields": missing,
                        })

        return failures

    def _validate_schemas(self, loader: IRDataLoader) -> List[Dict[str, Any]]:
        """Validate provenance for Domain 2: Schemas."""
        failures = []
        schemas = loader.load_schemas()

        for schema_id, schema in schemas.items():
            # Check schema-level provenance
            schema_prov = schema.get("provenance")
            missing = self._validate_provenance(schema_prov)
            if missing:
                failures.append({
                    "domain": "schemas",
                    "item_type": "schema",
                    "identifier": schema_id,
                    "missing_fields": missing,
                })

            # Check field-level provenance
            for prop in schema.get("properties") or []:
                json_name = prop.get("json_name") or "unknown"
                json_pointer = prop.get("json_pointer") or f"$.{json_name}"
                prop_prov = prop.get("provenance")
                missing = self._validate_provenance(prop_prov)
                if missing:
                    failures.append({
                        "domain": "schemas",
                        "item_type": "field",
                        "identifier": f"{schema_id}:{json_pointer}",
                        "missing_fields": missing,
                    })

        return failures

    def _validate_edges(self, loader: IRDataLoader) -> List[Dict[str, Any]]:
        """Validate provenance for Domain 4: Reference Edges."""
        failures = []
        edges_data = loader.load_reference_edges()

        if edges_data is None:
            # No edges file - not necessarily a failure, might be empty spec
            return []

        for i, edge in enumerate(edges_data.get("edges") or []):
            from_schema = edge.get("from_schema_id") or "unknown"
            to_schema = edge.get("to_schema_id") or "unknown"
            kind = edge.get("kind") or "unknown"
            json_pointer = edge.get("from_json_pointer") or ""

            edge_prov = edge.get("provenance")
            missing = self._validate_provenance(edge_prov)
            if missing:
                failures.append({
                    "domain": "refs",
                    "item_type": "edge",
                    "identifier": f"{from_schema} --[{kind}]--> {to_schema} @ {json_pointer}",
                    "missing_fields": missing,
                })

        return failures


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate invariant 5 (provenance coverage consistency)."
    )
    parser.add_argument("--config", default=CONFIG_DEFAULT, help="Path to config.toml.")
    parser.add_argument("--verbose", "-v", action="store_true", help="Print detailed output")
    args = parser.parse_args()

    config = load_config(args.config)
    spec_name = api_name(config)

    test = ProvenanceCoverageTest(ROOT, spec_name)
    return test.run(verbose=args.verbose)


if __name__ == "__main__":
    sys.exit(main())
