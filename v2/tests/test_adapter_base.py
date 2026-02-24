"""Tests for adapters/base.py — ApiAdapter, NodeClassification, TreeContext."""

from schmith.adapters.base import ApiAdapter, NodeClassification, TreeContext
from schmith.ir.models import Endpoint, SchemaNode
from schmith.generation.type_tree import NamingContext


class TestNodeClassification:
    def test_values(self) -> None:
        assert NodeClassification.NAMED_CLASS.value == "named_class"
        assert NodeClassification.INLINE.value == "inline"
        assert NodeClassification.COLLAPSE.value == "collapse"


class TestApiAdapter:
    def setup_method(self) -> None:
        self.adapter = ApiAdapter()
        self.endpoint = Endpoint(method="GET", path="/customers")
        self.schema_node = SchemaNode(
            schema_id="schema:components/Customer",
            schema={"kind": "object", "name_hint": "Customer", "properties": []},
        )

    def test_resolve_root_returns_node_unchanged(self) -> None:
        result = self.adapter.resolve_root(self.endpoint, self.schema_node)
        assert result is self.schema_node

    def test_transform_tree_returns_unchanged(self) -> None:
        root_type: dict = {"name": "CustomerDataObject", "kind": "object", "properties": []}
        nested: list[dict] = [{"name": "AddressDataObject", "kind": "object", "properties": []}]
        out_root, out_nested = self.adapter.transform_tree(root_type, nested)
        assert out_root is root_type
        assert out_nested is nested

    def test_name_anonymous_returns_none(self) -> None:
        ctx = NamingContext(parent_name="Parent", property_name="field")
        result = self.adapter.name_anonymous(self.schema_node, ctx)
        assert result is None

    def test_classify_node_returns_none(self) -> None:
        tree_ctx = TreeContext(parent=None, edge_kind="property", depth=1, root_schema_id="schema:components/Root")
        result = self.adapter.classify_node(self.schema_node, tree_ctx)
        assert result is None


class TestCustomAdapter:
    """Verify that adapter hooks work when overridden by a subclass."""

    def setup_method(self) -> None:
        class CustomAdapter(ApiAdapter):
            def resolve_root(self, endpoint: Endpoint, response_node: SchemaNode) -> SchemaNode:
                # Always navigate to a "items" property schema
                return SchemaNode(
                    schema_id="schema:components/Item",
                    schema={"kind": "object", "name_hint": "Item"},
                )

            def name_anonymous(self, node: SchemaNode, context: NamingContext) -> str | None:
                return "CustomName"

            def classify_node(self, node: SchemaNode, context: TreeContext) -> NodeClassification | None:
                return NodeClassification.COLLAPSE

        self.adapter = CustomAdapter()
        self.endpoint = Endpoint(method="GET", path="/items")
        self.response_node = SchemaNode(
            schema_id="schema:components/PagedResult",
            schema={"kind": "object"},
        )

    def test_resolve_root_override(self) -> None:
        result = self.adapter.resolve_root(self.endpoint, self.response_node)
        assert result.schema_id == "schema:components/Item"

    def test_name_anonymous_override(self) -> None:
        ctx = NamingContext(parent_name="P", property_name="x")
        node = SchemaNode(schema_id="schema:anon/abc", schema={"kind": "object"})
        assert self.adapter.name_anonymous(node, ctx) == "CustomName"

    def test_classify_node_override(self) -> None:
        node = SchemaNode(schema_id="schema:components/X", schema={"kind": "object"})
        ctx = TreeContext(parent=None, edge_kind="property", depth=0, root_schema_id="schema:components/X")
        assert self.adapter.classify_node(node, ctx) == NodeClassification.COLLAPSE
