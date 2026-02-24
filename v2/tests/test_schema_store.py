"""Tests for ir/store.py."""

from schmith.ir.store import SchemaStore


class TestSchemaStore:
    def setup_method(self) -> None:
        self.schemas: dict[str, dict] = {
            "schema:components/Customer": {
                "kind": "object",
                "name_hint": "Customer",
                "properties": [{"json_name": "id", "schema_id": "schema:types/string"}],
            },
            "schema:components/Order": {
                "kind": "object",
                "name_hint": "Order",
                "properties": [],
            },
        }
        self.store = SchemaStore(self.schemas)

    def test_get_existing(self) -> None:
        schema = self.store.get("schema:components/Customer")
        assert schema is not None
        assert schema["name_hint"] == "Customer"

    def test_get_missing_returns_none(self) -> None:
        assert self.store.get("schema:components/Missing") is None

    def test_all_returns_all_schemas(self) -> None:
        all_schemas = self.store.all()
        assert len(all_schemas) == 2
        assert "schema:components/Customer" in all_schemas

    def test_len(self) -> None:
        assert len(self.store) == 2

    def test_contains(self) -> None:
        assert "schema:components/Customer" in self.store
        assert "schema:components/Missing" not in self.store

    def test_resolver_returns_callable(self) -> None:
        resolver = self.store.resolver()
        assert callable(resolver)

    def test_resolver_callable_gets_schema(self) -> None:
        resolver = self.store.resolver()
        result = resolver("schema:components/Order")
        assert result is not None
        assert result["name_hint"] == "Order"

    def test_resolver_callable_returns_none_for_missing(self) -> None:
        resolver = self.store.resolver()
        assert resolver("schema:components/Missing") is None

    def test_empty_store(self) -> None:
        empty = SchemaStore({})
        assert len(empty) == 0
        assert empty.get("anything") is None

    def test_store_does_not_share_reference(self) -> None:
        # Mutating the input dict after construction should not affect the store
        raw: dict[str, dict] = {"schema:components/Foo": {"kind": "object"}}
        store = SchemaStore(raw)
        raw["schema:components/Bar"] = {"kind": "string"}
        assert "schema:components/Bar" not in store
