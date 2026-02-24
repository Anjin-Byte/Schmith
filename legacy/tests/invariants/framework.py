#!/usr/bin/env python3
"""
Base framework for IR invariant validation tests.

Provides common utilities for running tests and generating reports.
"""
import json
import os
import sys
from abc import ABC, abstractmethod
from datetime import datetime, timezone
from typing import Any, Dict, List

# Add project root to path
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)

from lib.ir_loader import IRDataLoader


class InvariantTest(ABC):
    """Base class for invariant validation tests."""

    def __init__(self, root_dir: str, spec_name: str):
        """
        Initialize the test.

        Args:
            root_dir: Root directory of the project
            spec_name: Name of the API spec being tested
        """
        self.root_dir = root_dir
        self.spec_name = spec_name
        self.loader = IRDataLoader(root_dir, spec_name)
        self.manifest = self.loader.load_manifest()

    @property
    @abstractmethod
    def invariant_id(self) -> str:
        """Return the unique identifier for this invariant test."""
        pass

    @property
    @abstractmethod
    def output_filename(self) -> str:
        """Return the filename for the test report (e.g., 'invariant_1_operation_schema_usage.json')."""
        pass

    @abstractmethod
    def run_validation(self) -> List[Dict[str, Any]]:
        """
        Run the validation logic and return a list of failures.

        Returns:
            List of failure dictionaries. Empty list means all tests passed.
        """
        pass

    def generate_report(self, failures: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Generate a standardized test report.

        Args:
            failures: List of failure dictionaries from run_validation()

        Returns:
            Report dictionary with status, timestamp, and failures
        """
        status = "pass" if not failures else "fail"
        severity = "info" if not failures else "error"
        return {
            "invariant_id": self.invariant_id,
            "status": status,
            "severity": severity,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "adapter": self.manifest.get("adapter"),
            "spec_version": self.manifest.get("spec_version"),
            "failures": failures,
        }

    def write_report(self, report: Dict[str, Any]) -> str:
        """
        Write the test report to the analysis directory.

        Args:
            report: Report dictionary from generate_report()

        Returns:
            Path to the written report file
        """
        out_dir = os.path.join(self.root_dir, "analysis", self.spec_name, "invariants")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, self.output_filename)
        with open(out_path, "w", encoding="utf-8") as handle:
            json.dump(report, handle, indent=2)
            handle.write("\n")
        return out_path

    def run(self, verbose: bool = False) -> int:
        """
        Run the complete test workflow: validate, report, and write results.

        Args:
            verbose: If True, print detailed output

        Returns:
            0 if all tests passed, 1 if any failures
        """
        if verbose:
            print(f"Running {self.invariant_id}...")

        failures = self.run_validation()
        report = self.generate_report(failures)
        out_path = self.write_report(report)

        if verbose:
            if failures:
                print(f"  FAIL: {len(failures)} failure(s)")
            else:
                print(f"  PASS")

        print(f"Wrote invariant report to {out_path}")
        return 0 if report["status"] == "pass" else 1
