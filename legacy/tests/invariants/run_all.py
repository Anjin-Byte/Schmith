#!/usr/bin/env python3
"""
Run all IR invariant validation tests.

This script discovers and runs all available invariant tests,
reporting on their collective status.
"""
import argparse
import os
import sys
from typing import Dict, List

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ROOT)
sys.path.append(SCRIPT_DIR)

from tests.invariants.framework import InvariantTest
from pipeline.config import api_name, load_config

# Import all test classes
from tests.invariants.test_invariant_1 import OperationSchemaUsageTest
from tests.invariants.test_invariant_2 import FieldNameSerializationTest
from tests.invariants.test_invariant_3 import MediaTypeMappingTest
from tests.invariants.test_invariant_4 import ReferenceEdgeConsistencyTest
from tests.invariants.test_invariant_5 import ProvenanceCoverageTest

CONFIG_DEFAULT = os.path.join(ROOT, "config.toml")

# Registry of all available tests
ALL_TESTS: List[type] = [
    OperationSchemaUsageTest,
    FieldNameSerializationTest,
    MediaTypeMappingTest,
    ReferenceEdgeConsistencyTest,
    ProvenanceCoverageTest,
]


def run_all_tests(root_dir: str, spec_name: str, verbose: bool = False) -> Dict[str, int]:
    """
    Run all registered invariant tests.

    Args:
        root_dir: Root directory of the project
        spec_name: Name of the API spec being tested
        verbose: If True, print detailed output

    Returns:
        Dictionary mapping test ID to exit code (0=pass, 1=fail)
    """
    results: Dict[str, int] = {}

    if verbose:
        print(f"Running {len(ALL_TESTS)} invariant test(s) for {spec_name}...\n")

    for test_class in ALL_TESTS:
        test = test_class(root_dir, spec_name)
        exit_code = test.run(verbose=verbose)
        results[test.invariant_id] = exit_code

        if verbose:
            print()  # Blank line between tests

    return results


def print_summary(results: Dict[str, int]) -> None:
    """Print a summary of test results."""
    passed = sum(1 for code in results.values() if code == 0)
    failed = sum(1 for code in results.values() if code != 0)
    total = len(results)

    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Total tests:  {total}")
    print(f"Passed:       {passed}")
    print(f"Failed:       {failed}")
    print()

    if failed > 0:
        print("Failed tests:")
        for test_id, code in results.items():
            if code != 0:
                print(f"  - {test_id}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run all IR invariant validation tests."
    )
    parser.add_argument("--config", default=CONFIG_DEFAULT, help="Path to config.toml.")
    parser.add_argument("--verbose", "-v", action="store_true", help="Print detailed output")
    parser.add_argument("--summary", "-s", action="store_true", help="Print summary at end")
    args = parser.parse_args()

    config = load_config(args.config)
    spec_name = api_name(config)

    results = run_all_tests(ROOT, spec_name, verbose=args.verbose)

    if args.summary or not args.verbose:
        print_summary(results)

    # Exit with 1 if any test failed
    return 1 if any(code != 0 for code in results.values()) else 0


if __name__ == "__main__":
    sys.exit(main())
