#!/usr/bin/env python3
"""Tests for naming strategies.

Run with: python -m pytest tests/test_naming_strategies.py -v
Or directly: python tests/test_naming_strategies.py
"""

import sys
import os

# Add project root to path
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from codegen.schema.naming import (
    NamingConfig,
    VerboseNamingStrategy,
    SemanticNamingStrategy,
    ResourceNamingStrategy,
    get_naming_strategy,
    create_config_from_dict,
)


# Sample Procore-like paths for testing
TEST_CASES = [
    {
        "method": "DELETE",
        "path": "/rest/v1.0/bim/model/revision/viewpoints/bulk-delete",
        "status": "200",
        "operation": {},
    },
    {
        "method": "GET",
        "path": "/rest/v2.0/companies/{company_id}/projects/{project_id}/tasks",
        "status": "200",
        "operation": {},
    },
    {
        "method": "POST",
        "path": "/rest/v1.0/folders/{folder_id}/files",
        "status": "201",
        "operation": {},
    },
    {
        "method": "GET",
        "path": "/oauth/token/info",
        "status": "200",
        "operation": {},
    },
    {
        "method": "PATCH",
        "path": "/rest/v1.1/companies/{id}/users/{user_id}/permissions",
        "status": "200",
        "operation": {},
    },
    {
        "method": "GET",
        "path": "/rest/v1.0/bim/model/revision/plans/batch",
        "status": "200",
        "operation": {"operationId": "getBimPlans"},  # Has operationId
    },
]


def test_verbose_strategy():
    """Test verbose naming (original behavior)."""
    config = NamingConfig(strategy="verbose")
    strategy = VerboseNamingStrategy(config)

    print("\n=== VERBOSE STRATEGY ===")
    for case in TEST_CASES:
        name = strategy.generate_response_name(
            case["operation"],
            case["method"],
            case["path"],
            case["status"],
        )
        print(f"{case['method']} {case['path']}")
        print(f"  → {name}")
        print(f"  Length: {len(name)} chars")
        print()


def test_semantic_strategy():
    """Test semantic naming (strips versions, keeps meaningful segments)."""
    config = NamingConfig(
        strategy="semantic",
        strip_version_prefixes=True,
        max_segments=0,  # No limit
    )
    strategy = SemanticNamingStrategy(config)

    print("\n=== SEMANTIC STRATEGY ===")
    for case in TEST_CASES:
        name = strategy.generate_response_name(
            case["operation"],
            case["method"],
            case["path"],
            case["status"],
        )
        print(f"{case['method']} {case['path']}")
        print(f"  → {name}")
        print(f"  Length: {len(name)} chars")
        print()


def test_semantic_with_limit():
    """Test semantic naming with segment limit."""
    config = NamingConfig(
        strategy="semantic",
        strip_version_prefixes=True,
        max_segments=3,
    )
    strategy = SemanticNamingStrategy(config)

    print("\n=== SEMANTIC STRATEGY (max 3 segments) ===")
    for case in TEST_CASES:
        name = strategy.generate_response_name(
            case["operation"],
            case["method"],
            case["path"],
            case["status"],
        )
        print(f"{case['method']} {case['path']}")
        print(f"  → {name}")
        print(f"  Length: {len(name)} chars")
        print()


def test_resource_strategy():
    """Test resource-focused naming (last N segments only)."""
    config = NamingConfig(
        strategy="resource",
        resource_depth=2,
    )
    strategy = ResourceNamingStrategy(config)

    print("\n=== RESOURCE STRATEGY (depth=2) ===")
    for case in TEST_CASES:
        name = strategy.generate_response_name(
            case["operation"],
            case["method"],
            case["path"],
            case["status"],
        )
        print(f"{case['method']} {case['path']}")
        print(f"  → {name}")
        print(f"  Length: {len(name)} chars")
        print()


def test_with_abbreviations():
    """Test semantic naming with abbreviations."""
    config = NamingConfig(
        strategy="semantic",
        strip_version_prefixes=True,
        abbreviations={
            "Response": "Resp",
            "Companies": "Co",
            "Projects": "Proj",
        },
    )
    strategy = SemanticNamingStrategy(config)

    print("\n=== SEMANTIC WITH ABBREVIATIONS ===")
    for case in TEST_CASES:
        name = strategy.generate_response_name(
            case["operation"],
            case["method"],
            case["path"],
            case["status"],
        )
        print(f"{case['method']} {case['path']}")
        print(f"  → {name}")
        print(f"  Length: {len(name)} chars")
        print()


def test_config_from_dict():
    """Test creating config from dictionary (as would come from TOML)."""
    config_dict = {
        "strategy": "semantic",
        "strip_version_prefixes": True,
        "max_segments": 4,
        "preserve_method": True,
        "abbreviations": {"Response": "Resp"},
    }
    config = create_config_from_dict(config_dict)
    strategy = get_naming_strategy(config)

    print("\n=== CONFIG FROM DICT ===")
    print(f"Strategy type: {type(strategy).__name__}")
    print(f"Config: {config}")

    name = strategy.generate_response_name(
        {},
        "GET",
        "/rest/v1.0/companies/{id}/projects",
        "200",
    )
    print(f"Sample: GET /rest/v1.0/companies/{{id}}/projects → {name}")


def compare_strategies():
    """Compare all strategies side by side."""
    configs = {
        "verbose": NamingConfig(strategy="verbose"),
        "semantic": NamingConfig(strategy="semantic", strip_version_prefixes=True),
        "semantic-3": NamingConfig(strategy="semantic", strip_version_prefixes=True, max_segments=3),
        "resource-2": NamingConfig(strategy="resource", resource_depth=2),
        "resource-1": NamingConfig(strategy="resource", resource_depth=1),
    }

    strategies = {name: get_naming_strategy(cfg) for name, cfg in configs.items()}

    print("\n" + "=" * 100)
    print("STRATEGY COMPARISON")
    print("=" * 100)

    for case in TEST_CASES:
        print(f"\n{case['method']} {case['path']} ({case['status']})")
        print("-" * 80)
        for name, strategy in strategies.items():
            result = strategy.generate_response_name(
                case["operation"],
                case["method"],
                case["path"],
                case["status"],
            )
            print(f"  {name:15} → {result} ({len(result)} chars)")


if __name__ == "__main__":
    test_verbose_strategy()
    test_semantic_strategy()
    test_semantic_with_limit()
    test_resource_strategy()
    test_with_abbreviations()
    test_config_from_dict()
    compare_strategies()
    print("\n✓ All tests passed!")
