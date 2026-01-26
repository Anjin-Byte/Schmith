"""Schema filtering utilities for DataObject generation.

This module provides functions for filtering IR schemas to determine which
ones are suitable for DataObject generation, and for identifying parent-child
relationships between schemas.
"""

from collections import defaultdict
from typing import NamedTuple

from .type_mapping import extract_clean_name


class SchemaInfo(NamedTuple):
    """Information about a schema that could become a DataObject."""

    schema_id: str
    name: str
    kind: str
    is_inline: bool
    usage_count: int


def is_error_schema(schema: dict) -> bool:
    """Check if a schema represents an error response.

    Args:
        schema: Schema dictionary from IR

    Returns:
        True if schema appears to be an error type
    """
    name_hint = schema.get("name_hint", "")
    schema_id = schema.get("schema_id", "")
    error_indicators = ["Error", "error", "Exception", "exception", "Problem", "problem"]
    return any(ind in name_hint or ind in schema_id for ind in error_indicators)


def is_primitive_schema(schema: dict) -> bool:
    """Check if a schema is a primitive type.

    Args:
        schema: Schema dictionary from IR

    Returns:
        True if schema represents a primitive type
    """
    kind = schema.get("kind", "")
    primitive_kinds = {"string", "integer", "number", "boolean", "null"}

    # Also check for schemas that are just wrappers around primitives
    name_hint = schema.get("name_hint", "")
    if name_hint in {"string", "integer", "number", "boolean", "object", "array"}:
        return True

    return kind in primitive_kinds


def is_variant_schema(name: str) -> bool:
    """Check if a schema name indicates a Body/View variant.

    Args:
        name: Clean schema name

    Returns:
        True if this is a Body or View variant
    """
    return name.endswith("Body") or name.endswith("View")


def filter_schemas(
    schemas: list[dict],
    include_errors: bool = False,
    include_primitives: bool = False,
    include_anonymous: bool = False,
    include_variants: bool = True,
) -> list[SchemaInfo]:
    """Filter schemas to get the list suitable for DataObject generation.

    By default, excludes:
    - Error response schemas
    - Primitive type schemas
    - Anonymous/inline schemas

    Args:
        schemas: List of schema dictionaries from IR
        include_errors: Include error response schemas
        include_primitives: Include primitive type schemas
        include_anonymous: Include anonymous/inline schemas
        include_variants: Include Body/View variants (default True)

    Returns:
        List of SchemaInfo for schemas suitable for generation
    """
    results = []

    for schema in schemas:
        schema_id = schema.get("schema_id", "")
        name_hint = schema.get("name_hint")
        kind = schema.get("kind", "unknown")
        is_inline = schema.get("is_inline", False)
        where_used = schema.get("where_used", [])

        # Apply filters
        if not include_anonymous and (is_inline or not name_hint or "anon/" in schema_id):
            continue

        if not include_primitives and is_primitive_schema(schema):
            continue

        if not include_errors and is_error_schema(schema):
            continue

        # Include objects and schemas with composition (allOf/oneOf/anyOf)
        has_composition = bool(schema.get("composition"))
        if kind != "object" and not has_composition:
            continue

        object_name = extract_clean_name(schema_id, name_hint)

        if not include_variants and is_variant_schema(object_name):
            continue

        results.append(
            SchemaInfo(
                schema_id=schema_id,
                name=object_name,
                kind=kind,
                is_inline=is_inline,
                usage_count=len(where_used),
            )
        )

    return results


def find_parent_child_relationships(schemas: list[dict]) -> dict[str, list[str]]:
    """Identify parent-child relationships based on naming conventions.

    Detects relationships like:
    - Customer -> CustomerContact, CustomerEmail, CustomerLocation
    - Job -> JobTask, JobNote, JobExpense

    Args:
        schemas: List of schema dictionaries from IR

    Returns:
        Dict mapping parent names to list of child names
    """
    # Get all valid schema names (excluding errors, primitives)
    names: set[str] = set()
    for schema in schemas:
        name_hint = schema.get("name_hint")
        if not name_hint:
            continue
        name = extract_clean_name(schema["schema_id"], name_hint)
        if is_error_schema(schema):
            continue
        if is_primitive_schema(schema):
            continue
        names.add(name)

    # Find potential parent names
    potential_parents: set[str] = set()
    for name in names:
        potential_parents.add(name)

    # Build parent -> children mapping
    parent_children: dict[str, list[str]] = defaultdict(list)

    for name in names:
        # Check if this name starts with a potential parent name
        for parent in potential_parents:
            if name == parent:
                continue

            # Check if name starts with parent name and has additional suffix
            if name.startswith(parent) and len(name) > len(parent):
                suffix = name[len(parent) :]
                # Suffix should start with uppercase (CustomerContact, not Customers)
                if suffix and suffix[0].isupper():
                    parent_children[parent].append(name)
                    break

    return dict(parent_children)


def get_root_schemas(
    schemas: list[dict],
    parent_children: dict[str, list[str]],
) -> list[str]:
    """Get list of root schema names (top-level DataObjects).

    Root schemas are:
    - Parents with children
    - Schemas that are not children of any parent

    Args:
        schemas: List of schema dictionaries from IR
        parent_children: Parent-child relationship mapping

    Returns:
        Sorted list of root schema names
    """
    # Get all children
    all_children: set[str] = set()
    for children in parent_children.values():
        all_children.update(children)

    # Get all valid schema names
    roots: list[str] = []
    for schema in schemas:
        name_hint = schema.get("name_hint")
        if not name_hint:
            continue

        name = extract_clean_name(schema["schema_id"], name_hint)

        # Skip errors, primitives
        if is_error_schema(schema):
            continue
        if is_primitive_schema(schema):
            continue

        # Skip if it's a child
        if name in all_children:
            continue

        # Must be an object
        if schema.get("kind") != "object":
            continue

        roots.append(name)

    return sorted(roots)
