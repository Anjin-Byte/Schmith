"""Core IR data models passed through the pipeline and into adapter hooks."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

Schema = dict[str, Any]


@dataclass
class Endpoint:
    """An HTTP endpoint specified as input to the pipeline."""

    method: str   # Uppercase: "GET", "POST", etc.
    path: str     # "/customers/{id}"

    def __str__(self) -> str:
        return f"{self.method} {self.path}"


@dataclass
class OperationResponse:
    """The resolved response entry for a specific endpoint and status code."""

    status_code: str          # "200", "201", etc.
    schema_id: str | None     # May be None for responses with no body
    media_type: str | None
    description: str | None


@dataclass
class SchemaNode:
    """A navigable wrapper around a raw IR schema dict.

    This is what adapter hooks receive. It provides typed access to
    the most common schema fields without requiring adapter code to
    parse raw dict internals.

    The parent/edge_kind/depth fields provide traversal context so
    the adapter can make decisions based on where in the tree the node
    sits, not just what the node itself contains.
    """

    schema_id: str
    schema: Schema
    parent: SchemaNode | None = field(default=None, repr=False)
    edge_kind: str | None = None   # "property", "array_items", "composition_member", etc.
    depth: int = 0

    # ------------------------------------------------------------------
    # Convenience accessors
    # ------------------------------------------------------------------

    def get(self, key: str, default: Any = None) -> Any:
        return self.schema.get(key, default)

    @property
    def kind(self) -> str:
        return self.schema.get("kind", "object")

    @property
    def name_hint(self) -> str | None:
        return self.schema.get("name_hint")

    @property
    def is_anonymous(self) -> bool:
        return "anon/" in self.schema_id

    @property
    def properties(self) -> list[Schema]:
        return self.schema.get("properties", [])

    @property
    def composition(self) -> Schema | None:
        return self.schema.get("composition")

    @property
    def description(self) -> str | None:
        return self.schema.get("description")
