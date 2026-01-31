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
    include_orphans: bool = True,
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
        include_orphans: Include schemas not used by any operation (default True)

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

        # Exclude orphan schemas (not used by any operation or other schema)
        if not include_orphans and len(where_used) == 0:
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


def _extract_component_name(schema_id: str) -> str | None:
    """Extract component name from schema ID.

    Args:
        schema_id: Full schema ID like 'schema:components/Customer'

    Returns:
        Component name like 'Customer', or None if not a component
    """
    if "components/" in schema_id:
        return schema_id.split("components/")[-1]
    if "definitions/" in schema_id:
        return schema_id.split("definitions/")[-1]
    # Support RAML-style IR names (schema:types/typ.Name or schema:types/typ/Name).
    # This keeps grouping logic format-agnostic across OpenAPI/RAML.
    if schema_id.startswith("schema:types/typ."):
        return schema_id.split("schema:types/typ.", 1)[-1]
    if schema_id.startswith("schema:types/typ/"):
        return schema_id.split("schema:types/typ/", 1)[-1]
    # Avoid treating primitive and generic container schemas as named components.
    if schema_id.startswith("schema:types/"):
        tail = schema_id.split("schema:types/", 1)[-1]
        if tail in {"string", "integer", "number", "boolean", "null", "object", "array", "any"}:
            return None
        return tail
    return None


def find_reachable_schemas(
    operations: list[dict],
    adjacency: dict,
    schemas_by_id: dict[str, dict],
) -> set[str]:
    """Find all schema IDs reachable from operations via the adjacency graph.

    This performs a graph traversal starting from schemas used in operations
    (requests and responses) and follows all schema references to find the
    complete set of schemas that are actually used by the API.

    Args:
        operations: List of operation dicts from operations/index.json
        adjacency: Adjacency graph from refs/adjacency.json
        schemas_by_id: Dict mapping schema IDs to schema data

    Returns:
        Set of schema IDs that are reachable from operations
    """
    # Collect initial set of schemas from operations
    root_schemas: set[str] = set()
    for op in operations:
        for schema_id in op.get("requests", []):
            root_schemas.add(schema_id)
        for schema_id in op.get("responses", []):
            root_schemas.add(schema_id)

    # BFS to find all reachable schemas
    reachable: set[str] = set()
    queue = list(root_schemas)
    outgoing = adjacency.get("outgoing", {})

    while queue:
        current_id = queue.pop(0)
        if current_id in reachable:
            continue
        reachable.add(current_id)

        # Follow outgoing references
        for ref in outgoing.get(current_id, []):
            target_id = ref.get("to_schema_id", "")
            if target_id and target_id not in reachable:
                queue.append(target_id)

                # Also follow items_schema_id for arrays
                target_schema = schemas_by_id.get(target_id)
                if target_schema and target_schema.get("kind") == "array":
                    items_id = target_schema.get("items_schema_id")
                    if items_id and items_id not in reachable:
                        queue.append(items_id)

    return reachable


def find_reachable_component_names(
    operations: list[dict],
    adjacency: dict,
    schemas_by_id: dict[str, dict],
) -> set[str]:
    """Find component names of all schemas reachable from operations.

    This is a convenience wrapper that returns clean component names
    instead of full schema IDs.

    Args:
        operations: List of operation dicts from operations/index.json
        adjacency: Adjacency graph from refs/adjacency.json
        schemas_by_id: Dict mapping schema IDs to schema data

    Returns:
        Set of component names (e.g., "Customer", "Order") that are reachable
    """
    reachable_ids = find_reachable_schemas(operations, adjacency, schemas_by_id)
    names: set[str] = set()

    for schema_id in reachable_ids:
        name = _extract_component_name(schema_id)
        if name:
            names.add(name)

    return names


def find_parent_child_relationships_from_ir(
    adjacency: dict,
    schemas_by_id: dict[str, dict],
    reachable_names: set[str] | None = None,
) -> dict[str, list[str]]:
    """Identify parent-child relationships using actual IR reference data.

    Uses the adjacency graph from the IR to find schemas that are directly
    referenced by other schemas via property_ref or items_ref.

    Args:
        adjacency: Adjacency graph from IR (refs/adjacency.json)
        schemas_by_id: Dict mapping schema IDs to schema data
        reachable_names: Optional set of schema names to include. If provided,
            only relationships where BOTH parent and child are in this set
            will be included. Use find_reachable_component_names() to get this.

    Returns:
        Dict mapping parent names to list of child schema names
    """
    outgoing = adjacency.get("outgoing", {})
    parent_children: dict[str, set[str]] = defaultdict(set)

    for parent_id, refs in outgoing.items():
        parent_name = _extract_component_name(parent_id)
        if not parent_name:
            continue

        # Skip if not in reachable set (when filtering is enabled)
        if reachable_names is not None and parent_name not in reachable_names:
            continue

        # Check if parent is a valid object schema
        parent_schema = schemas_by_id.get(parent_id)
        if not parent_schema:
            continue
        if parent_schema.get("kind") != "object":
            continue
        if is_error_schema(parent_schema):
            continue

        for ref in refs:
            child_id = ref.get("to_schema_id", "")
            ref_kind = ref.get("kind", "")

            # Only follow property_ref and items_ref (not additional_props_ref)
            if ref_kind not in ("property_ref", "items_ref"):
                continue

            # If child is an array (named or anonymous), follow its items_schema_id
            child_schema = schemas_by_id.get(child_id)
            if child_schema and child_schema.get("kind") == "array":
                items_id = child_schema.get("items_schema_id")
                if items_id:
                    child_id = items_id

            child_name = _extract_component_name(child_id)
            if not child_name:
                continue

            # Skip if not in reachable set (when filtering is enabled)
            if reachable_names is not None and child_name not in reachable_names:
                continue

            # Check if child is a valid object schema (not primitive, not error)
            child_schema = schemas_by_id.get(child_id)
            if not child_schema:
                continue
            if child_schema.get("kind") != "object":
                continue
            if is_error_schema(child_schema):
                continue
            if is_primitive_schema(child_schema):
                continue

            # Don't add self-references
            if child_name != parent_name:
                parent_children[parent_name].add(child_name)

    return {k: sorted(v) for k, v in parent_children.items()}


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
