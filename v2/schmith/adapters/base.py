"""ApiAdapter base class and associated types.

The ApiAdapter is the seam between general pipeline logic and API-specific
knowledge. All hook methods have default pass-through implementations so the
base class produces valid output with no overrides required.

Subclass ApiAdapter and override only the hooks you need. The general pipeline
never imports concrete adapter subclasses — it only interacts with this interface.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from schmith.ir.models import Endpoint, SchemaNode
    from schmith.generation.type_tree import NamingContext


class NodeClassification(Enum):
    """How a schema node should be handled during class generation."""

    NAMED_CLASS = "named_class"
    """Generate this node as its own named C# record/class."""

    INLINE = "inline"
    """Fold this node's properties into the parent class."""

    COLLAPSE = "collapse"
    """Treat this node as transparent — follow through to its children."""


@dataclass
class TreeContext:
    """Context passed to classify_node so the adapter can make decisions
    based on a node's position in the type tree, not just its content."""

    parent: SchemaNode | None
    edge_kind: str | None   # How this node was reached from its parent
    depth: int              # Distance from the root (0 = root)
    root_schema_id: str     # Schema ID of the tree root


class ApiAdapter:
    """Base adapter — all hooks are pass-throughs.

    Override only the methods you need. The general pipeline calls these
    at each decision point. Returning None from any hook defers to the
    general heuristic built into the pipeline.
    """

    def resolve_root(
        self,
        endpoint: Endpoint,
        response_node: SchemaNode,
    ) -> SchemaNode:
        """Select the actual DataObject root from the endpoint's response schema.

        The candidate is the schema the spec directly associates with the
        response. Override to unwrap pagination envelopes, follow indirection,
        or select the correct branch of a union type.

        Default: return response_node unchanged.
        """
        return response_node

    def transform_tree(
        self,
        root_type: dict,
        nested_types: list[dict],
    ) -> tuple[dict, list[dict]]:
        """Transform the collected type closure before code generation.

        Called after the type tree has been fully collected. The adapter
        receives the flat closure and may rename, remove, merge, or reorder
        types. The root_type dict and nested_types list are the same format
        produced by build_type_hierarchy.

        Default: return (root_type, nested_types) unchanged.
        """
        return root_type, nested_types

    def name_anonymous(
        self,
        node: SchemaNode,
        context: NamingContext,
    ) -> str | None:
        """Provide a name for an anonymous schema node.

        Called during type tree traversal when an anonymous schema (one with
        a hash-based ID) needs a name. Return a non-None string to override
        the general naming heuristic. Return None to defer.

        Default: return None.
        """
        return None

    def classify_node(
        self,
        node: SchemaNode,
        context: TreeContext,
    ) -> NodeClassification | None:
        """Classify a node: named class, inline into parent, or collapse.

        Called during type tree collection for each non-primitive schema.
        Return a NodeClassification to override the general heuristic.
        Return None to defer.

        Default: return None.
        """
        return None
