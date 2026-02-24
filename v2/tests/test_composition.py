"""Tests for ir/composition.py — CompositionResolver."""

from schmith.ir.composition import CompositionResolver


def _make_resolver(schemas: dict[str, dict]):
    return lambda schema_id: schemas.get(schema_id)


class TestCompositionResolver:
    def setup_method(self) -> None:
        self.base_schema = {
            "kind": "object",
            "name_hint": "Base",
            "id": "schema:components/Base",
            "properties": [
                {"json_name": "id", "schema_id": "schema:types/string"},
                {"json_name": "created_at", "schema_id": "schema:types/string"},
            ],
        }
        self.child_schema = {
            "kind": "object",
            "name_hint": "Child",
            "id": "schema:components/Child",
            "properties": [
                {"json_name": "name", "schema_id": "schema:types/string"},
            ],
            "composition": {
                "kind": "allOf",
                "members": ["schema:components/Base"],
            },
        }
        self.schemas = {
            "schema:types/string": {"kind": "string"},
            "schema:components/Base": self.base_schema,
            "schema:components/Child": self.child_schema,
        }
        resolver = _make_resolver(self.schemas)
        self.cr = CompositionResolver(resolver, self.schemas)

    def _resolve(self, schema: dict) -> list[dict]:
        props, _ = self.cr.resolve_properties(schema)
        return props

    def test_resolves_direct_properties(self) -> None:
        props = self._resolve(self.base_schema)
        names = [p.get("json_name") for p in props]
        assert "id" in names
        assert "created_at" in names

    def test_resolves_allof_composition(self) -> None:
        props = self._resolve(self.child_schema)
        names = [p.get("json_name") for p in props]
        assert "name" in names
        assert "id" in names  # inherited from Base via allOf
        assert "created_at" in names

    def test_no_duplicate_properties(self) -> None:
        props = self._resolve(self.child_schema)
        names = [p.get("json_name") for p in props]
        assert len(names) == len(set(names))

    def test_non_composed_schema_returns_own_properties(self) -> None:
        schema = {
            "kind": "object",
            "properties": [{"json_name": "x", "schema_id": "schema:types/string"}],
        }
        props = self._resolve(schema)
        assert len(props) == 1
        assert props[0]["json_name"] == "x"

    def test_missing_schema_returns_empty(self) -> None:
        schema = {
            "kind": "object",
            "composition": {"kind": "allOf", "members": ["schema:components/Missing"]},
        }
        props = self._resolve(schema)
        # Should not raise; the missing member is silently skipped
        assert isinstance(props, list)

    def test_result_is_cached(self) -> None:
        # Call twice — result should be the same object (cached)
        r1 = self.cr.resolve_properties(self.child_schema)
        r2 = self.cr.resolve_properties(self.child_schema)
        assert r1 is r2
