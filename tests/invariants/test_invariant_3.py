#!/usr/bin/env python3
"""Invariant Test 3: Media Type Mapping Consistency"""
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


class MediaTypeMappingTest(InvariantTest):
    """
    Test that media types are consistent between operation definitions and serialization indexes.

    Verifies:
    - Every media type referenced in an operation's request/response bodies (Domain 1)
      appears in the serialization media_types index (Domain 3)
    - No extra media types are listed in serialization that aren't in the operation definition
    """

    @property
    def invariant_id(self) -> str:
        return "invariant_3_media_type_mapping"

    @property
    def output_filename(self) -> str:
        return "invariant_3_media_type_mapping.json"

    def run_validation(self) -> List[Dict[str, Any]]:
        loader = IRDataLoader(self.root_dir, self.spec_name)
        operations = loader.load_operations()
        serialization_media_types = self._load_serialization_media_types(loader)

        failures = []
        for operation in operations:
            op_id = operation.get("id")
            if not op_id:
                continue

            op_media_types = self._extract_operation_media_types(operation)
            serialization_types = serialization_media_types.get(op_id, set())

            missing = sorted(op_media_types - serialization_types)
            extra = sorted(serialization_types - op_media_types)

            if missing or extra:
                failures.append({
                    "operation_id": op_id,
                    "missing_in_serialization": missing,
                    "extra_in_serialization": extra,
                })

        return failures

    def _extract_operation_media_types(self, operation: Dict[str, Any]) -> Set[str]:
        """Extract all media types from an operation's request/response bodies."""
        media_types: Set[str] = set()

        for surface_key in ("declared", "effective"):
            surface = operation.get(surface_key) or {}

            # Extract from request bodies
            request_bodies = surface.get("request_bodies") or []
            for body in request_bodies:
                if isinstance(body, dict):
                    media_type = body.get("media_type")
                    if media_type:
                        media_types.add(media_type)

            # Extract from responses
            responses = surface.get("responses") or []
            for response in responses:
                if isinstance(response, dict):
                    media_type = response.get("media_type")
                    if media_type:
                        media_types.add(media_type)

        return media_types

    def _load_serialization_media_types(self, loader: IRDataLoader) -> Dict[str, Set[str]]:
        """Load media types from the serialization index."""
        data = loader.load_serialization_media_types()
        operations = data.get("operations") or {}
        media_type_map: Dict[str, Set[str]] = {}

        for op_id, op_data in operations.items():
            media_types: Set[str] = set()

            # Extract from request media types
            request = op_data.get("request")
            if isinstance(request, list):
                media_types.update(request)

            # Extract from response media types
            responses = op_data.get("responses") or {}
            for status_code, types in responses.items():
                if isinstance(types, list):
                    media_types.update(types)

            media_type_map[op_id] = media_types

        return media_type_map


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate invariant 3 (media type mapping consistency)."
    )
    parser.add_argument("--config", default=CONFIG_DEFAULT, help="Path to config.toml.")
    parser.add_argument("--verbose", action="store_true", help="Print detailed output")
    args = parser.parse_args()

    config = load_config(args.config)
    spec_name = api_name(config)

    test = MediaTypeMappingTest(ROOT, spec_name)
    return test.run(verbose=args.verbose)


if __name__ == "__main__":
    sys.exit(main())
