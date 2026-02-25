"""Schema composition resolution for allOf/oneOf/anyOf.

Merges properties from composed member schemas recursively with caching
and depth-guarded cycle detection.
"""

from __future__ import annotations

import logging
from typing import Any, Protocol

logger = logging.getLogger(__name__)

Schema = dict[str, Any]


class SchemaResolver(Protocol):
    def __call__(self, schema_id: str) -> Schema | None: ...


class CompositionResolver:
    """Resolve composition to get merged properties.

    Example:
        resolver = CompositionResolver(store.resolver(), store.all())
        props, required = resolver.resolve_properties(schema)
    """

    def __init__(
        self,
        load_schema: SchemaResolver,
        schemas_by_id: dict[str, Schema],
        max_depth: int = 10,
    ):
        self._load_schema = load_schema
        self._schemas_by_id = schemas_by_id
        self._max_depth = max_depth
        self._cache: dict[str, tuple[list[Schema], list[str]]] = {}

    def resolve_properties(
        self,
        schema: Schema,
        depth: int = 0,
    ) -> tuple[list[Schema], list[str]]:
        """Resolve all properties for a schema, including composed members.

        Returns:
            Tuple of (merged_properties, merged_required).
        """
        schema_id: str = schema.get("id", "")

        if schema_id and schema_id in self._cache:
            return self._cache[schema_id]

        if depth > self._max_depth:
            logger.warning("Max composition depth (%d) exceeded for %s", self._max_depth, schema_id)
            props: list[Schema] = schema.get("properties", [])
            required: list[str] = schema.get("required", [])
            return props, required

        merged_props: dict[str, Schema] = {}
        merged_required: set[str] = set()

        composition: Schema | None = schema.get("composition")
        if composition and composition.get("kind") in {"allOf", "oneOf", "anyOf"}:
            for member_id in composition.get("members", []):
                member_props, member_required = self._resolve_member(member_id, depth + 1)
                for prop in member_props:
                    json_name: str = prop.get("json_name", "")
                    if json_name:
                        merged_props[json_name] = prop
                merged_required.update(member_required)

        for prop in schema.get("properties", []):
            json_name = prop.get("json_name", "")
            if json_name:
                merged_props[json_name] = prop

        for req in schema.get("required", []):
            merged_required.add(req)

        result: tuple[list[Schema], list[str]] = list(merged_props.values()), list(merged_required)
        if schema_id:
            self._cache[schema_id] = result
        return result

    def _resolve_member(self, member_id: str, depth: int) -> tuple[list[Schema], list[str]]:
        if member_id in self._cache:
            return self._cache[member_id]
        member_schema: Schema | None = self._load_schema(member_id) or self._schemas_by_id.get(member_id)
        if not member_schema:
            logger.warning("Could not resolve composition member: %s", member_id)
            return [], []
        return self.resolve_properties(member_schema, depth)

    def clear_cache(self) -> None:
        self._cache.clear()
