"""Schema composition resolution for allOf/oneOf/anyOf.

This module handles resolving composed schemas by merging properties
from all referenced member schemas recursively.
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    pass

logger = logging.getLogger(__name__)


class SchemaResolver(Protocol):
    """Protocol for resolving schema IDs to schema data."""

    def __call__(self, schema_id: str) -> dict | None:
        """Resolve a schema ID to its full schema data."""
        ...


class CompositionResolver:
    """Resolve composition to get merged properties.

    Example:
        resolver = CompositionResolver(loader.load_schema_detail, loader.schemas_by_id())
        props, required = resolver.resolve_properties(schema)
    """

    def __init__(
        self,
        load_schema: SchemaResolver,
        schemas_by_id: dict[str, dict],
        max_depth: int = 10,
    ):
        """Initialize the resolver.

        Args:
            load_schema: Function to load full schema details by ID
            schemas_by_id: Index of all schemas for quick lookup
            max_depth: Maximum recursion depth to prevent infinite loops
        """
        self._load_schema = load_schema
        self._schemas_by_id = schemas_by_id
        self._max_depth = max_depth
        self._cache: dict[str, tuple[list[dict], list[str]]] = {}

    def resolve_properties(
        self,
        schema: dict,
        depth: int = 0,
    ) -> tuple[list[dict], list[str]]:
        """Resolve all properties for a schema, including composed members.

        Args:
            schema: The schema dictionary to resolve
            depth: Current recursion depth (for cycle detection)

        Returns:
            Tuple of (merged_properties, merged_required)
            - merged_properties: List of all property dicts
            - merged_required: List of all required field names
        """
        schema_id = schema.get("id", "")

        # Check cache
        if schema_id and schema_id in self._cache:
            return self._cache[schema_id]

        # Depth check
        if depth > self._max_depth:
            logger.warning(
                f"Max composition depth ({self._max_depth}) exceeded for {schema_id}"
            )
            return schema.get("properties", []), schema.get("required", [])

        # Start with empty collections
        merged_props: dict[str, dict] = {}  # json_name -> property dict
        merged_required: set[str] = set()

        # Process composition first (base classes / unions treated as merge)
        composition = schema.get("composition")
        if composition and composition.get("kind") in {"allOf", "oneOf", "anyOf"}:
            members = composition.get("members", [])
            for member_id in members:
                member_props, member_required = self._resolve_member(
                    member_id, depth + 1
                )
                # Merge properties (later members override earlier)
                for prop in member_props:
                    json_name = prop.get("json_name", "")
                    if json_name and json_name in merged_props:
                        logger.debug(
                            f"Property '{json_name}' in {schema_id} overrides "
                            f"inherited property from composition"
                        )
                    if json_name:
                        merged_props[json_name] = prop
                # Union required fields
                merged_required.update(member_required)

        # Add direct properties (highest precedence)
        for prop in schema.get("properties", []):
            json_name = prop.get("json_name", "")
            if json_name and json_name in merged_props:
                logger.debug(
                    f"Direct property '{json_name}' in {schema_id} overrides "
                    f"inherited property"
                )
            if json_name:
                merged_props[json_name] = prop

        # Add direct required fields
        for req in schema.get("required", []):
            merged_required.add(req)

        # Convert back to list, preserving some order
        result_props = list(merged_props.values())
        result_required = list(merged_required)

        # Cache result
        if schema_id:
            self._cache[schema_id] = (result_props, result_required)

        return result_props, result_required

    def _resolve_member(
        self,
        member_id: str,
        depth: int,
    ) -> tuple[list[dict], list[str]]:
        """Resolve properties for a composition member.

        Args:
            member_id: Schema ID of the member
            depth: Current recursion depth

        Returns:
            Tuple of (properties, required) for the member
        """
        # Check cache first
        if member_id in self._cache:
            return self._cache[member_id]

        # Try to load full schema details
        member_schema = self._load_schema(member_id)

        if not member_schema:
            # Try the index as fallback
            member_schema = self._schemas_by_id.get(member_id)

        if not member_schema:
            logger.warning(f"Could not resolve composition member: {member_id}")
            return [], []

        # Recursively resolve the member
        return self.resolve_properties(member_schema, depth)

    def clear_cache(self) -> None:
        """Clear the resolution cache."""
        self._cache.clear()


def resolve_schema_properties(
    schema: dict,
    load_schema: SchemaResolver,
    schemas_by_id: dict[str, dict],
) -> tuple[list[dict], list[str]]:
    """Convenience function to resolve properties for a single schema.

    Args:
        schema: The schema to resolve
        load_schema: Function to load full schema details
        schemas_by_id: Index of all schemas

    Returns:
        Tuple of (merged_properties, merged_required)
    """
    resolver = CompositionResolver(load_schema, schemas_by_id)
    return resolver.resolve_properties(schema)
