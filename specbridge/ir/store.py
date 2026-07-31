"""In-memory schema store — replaces the file-based IRLoader from legacy."""

from __future__ import annotations

from typing import Any, Callable

Schema = dict[str, Any]


class SchemaStore:
    """In-memory registry of all schemas extracted from a spec.

    Populated by a spec adapter (openapi.py or raml.py) and consumed
    by type tree traversal and composition resolution.

    The store intentionally has a minimal API — it is a keyed dict with
    a resolver callable factory. Nothing else belongs here.
    """

    def __init__(self, schemas: dict[str, Schema]) -> None:
        self._schemas: dict[str, Schema] = dict(schemas)

    def get(self, schema_id: str) -> Schema | None:
        return self._schemas.get(schema_id)

    def all(self) -> dict[str, Schema]:
        return self._schemas

    def resolver(self) -> Callable[[str], Schema | None]:
        """Return a callable suitable for CompositionResolver and type_tree."""
        return self.get

    def __len__(self) -> int:
        return len(self._schemas)

    def __contains__(self, schema_id: object) -> bool:
        return schema_id in self._schemas
