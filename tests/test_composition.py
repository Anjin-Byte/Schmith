"""Tests for composition resolution."""

import pytest
from codegen.ir.composition import CompositionResolver, resolve_schema_properties


class TestCompositionResolver:
    """Test cases for CompositionResolver."""

    def setup_method(self):
        """Set up test fixtures."""
        self.schemas = {
            "schema:definitions/Base": {
                "id": "schema:definitions/Base",
                "properties": [
                    {"json_name": "id", "schema_id": "schema:types/string"},
                    {"json_name": "name", "schema_id": "schema:types/string"},
                ],
                "required": ["id"],
            },
            "schema:definitions/Timestamps": {
                "id": "schema:definitions/Timestamps",
                "properties": [
                    {"json_name": "created_at", "schema_id": "schema:types/datetime"},
                    {"json_name": "updated_at", "schema_id": "schema:types/datetime"},
                ],
                "required": ["created_at", "updated_at"],
            },
            "schema:definitions/Full": {
                "id": "schema:definitions/Full",
                "properties": [],
                "required": [],
                "composition": {
                    "kind": "allOf",
                    "members": [
                        "schema:definitions/Base",
                        "schema:definitions/Timestamps",
                    ],
                },
            },
            "schema:definitions/Extended": {
                "id": "schema:definitions/Extended",
                "properties": [
                    {"json_name": "extra", "schema_id": "schema:types/string"},
                ],
                "required": [],
                "composition": {
                    "kind": "allOf",
                    "members": ["schema:definitions/Base"],
                },
            },
        }

        def load_schema(schema_id: str) -> dict | None:
            return self.schemas.get(schema_id)

        self.resolver = CompositionResolver(load_schema, self.schemas)

    def test_simple_schema_no_composition(self):
        """Test resolving a schema without composition."""
        schema = self.schemas["schema:definitions/Base"]
        props, required = self.resolver.resolve_properties(schema)

        assert len(props) == 2
        assert set(p["json_name"] for p in props) == {"id", "name"}
        assert required == ["id"]

    def test_composition_only(self):
        """Test resolving a schema with only composition (no direct properties)."""
        schema = self.schemas["schema:definitions/Full"]
        props, required = self.resolver.resolve_properties(schema)

        # Should have 4 properties from Base + Timestamps
        assert len(props) == 4
        json_names = {p["json_name"] for p in props}
        assert json_names == {"id", "name", "created_at", "updated_at"}

        # Should have 3 required fields
        assert set(required) == {"id", "created_at", "updated_at"}

    def test_composition_with_direct_properties(self):
        """Test resolving a schema with both composition and direct properties."""
        schema = self.schemas["schema:definitions/Extended"]
        props, required = self.resolver.resolve_properties(schema)

        # Should have 3 properties: 2 from Base + 1 direct
        assert len(props) == 3
        json_names = {p["json_name"] for p in props}
        assert json_names == {"id", "name", "extra"}

    def test_property_override(self):
        """Test that direct properties override inherited ones."""
        self.schemas["schema:definitions/Override"] = {
            "id": "schema:definitions/Override",
            "properties": [
                {
                    "json_name": "id",
                    "schema_id": "schema:types/integer",
                },  # Override type
            ],
            "required": [],
            "composition": {
                "kind": "allOf",
                "members": ["schema:definitions/Base"],
            },
        }

        schema = self.schemas["schema:definitions/Override"]
        props, _ = self.resolver.resolve_properties(schema)

        # Find the id property
        id_prop = next(p for p in props if p["json_name"] == "id")
        assert id_prop["schema_id"] == "schema:types/integer"  # Direct override wins

    def test_missing_member_graceful(self):
        """Test that missing members are handled gracefully."""
        self.schemas["schema:definitions/Missing"] = {
            "id": "schema:definitions/Missing",
            "properties": [{"json_name": "x", "schema_id": "schema:types/string"}],
            "composition": {
                "kind": "allOf",
                "members": ["schema:definitions/DoesNotExist"],
            },
        }

        schema = self.schemas["schema:definitions/Missing"]
        props, _ = self.resolver.resolve_properties(schema)

        # Should still get the direct property
        assert len(props) == 1
        assert props[0]["json_name"] == "x"

    def test_caching(self):
        """Test that resolution results are cached."""
        schema = self.schemas["schema:definitions/Full"]

        # First call
        props1, req1 = self.resolver.resolve_properties(schema)

        # Second call should hit cache
        props2, req2 = self.resolver.resolve_properties(schema)

        assert props1 is props2
        assert req1 is req2

    def test_clear_cache(self):
        """Test that cache can be cleared."""
        schema = self.schemas["schema:definitions/Full"]

        # First call
        props1, _ = self.resolver.resolve_properties(schema)

        # Clear cache
        self.resolver.clear_cache()

        # Second call should return new list (not same object)
        props2, _ = self.resolver.resolve_properties(schema)

        assert props1 is not props2
        assert len(props1) == len(props2)

    def test_max_depth_protection(self):
        """Test that max depth prevents infinite recursion."""
        # Create a circular reference (shouldn't happen in practice)
        self.schemas["schema:definitions/A"] = {
            "id": "schema:definitions/A",
            "properties": [],
            "composition": {"kind": "allOf", "members": ["schema:definitions/B"]},
        }
        self.schemas["schema:definitions/B"] = {
            "id": "schema:definitions/B",
            "properties": [],
            "composition": {"kind": "allOf", "members": ["schema:definitions/A"]},
        }

        # This should not hang - max_depth will prevent infinite recursion
        resolver = CompositionResolver(
            lambda x: self.schemas.get(x),
            self.schemas,
            max_depth=5,
        )
        props, _ = resolver.resolve_properties(self.schemas["schema:definitions/A"])
        # Should return empty (hit max depth) rather than hanging
        assert isinstance(props, list)

    def test_nested_composition(self):
        """Test resolving nested composition (member has its own allOf)."""
        self.schemas["schema:definitions/Level1"] = {
            "id": "schema:definitions/Level1",
            "properties": [{"json_name": "level1_prop", "schema_id": "schema:types/string"}],
            "required": [],
        }
        self.schemas["schema:definitions/Level2"] = {
            "id": "schema:definitions/Level2",
            "properties": [{"json_name": "level2_prop", "schema_id": "schema:types/string"}],
            "required": [],
            "composition": {
                "kind": "allOf",
                "members": ["schema:definitions/Level1"],
            },
        }
        self.schemas["schema:definitions/Level3"] = {
            "id": "schema:definitions/Level3",
            "properties": [{"json_name": "level3_prop", "schema_id": "schema:types/string"}],
            "required": [],
            "composition": {
                "kind": "allOf",
                "members": ["schema:definitions/Level2"],
            },
        }

        schema = self.schemas["schema:definitions/Level3"]
        props, _ = self.resolver.resolve_properties(schema)

        # Should have all 3 properties from the chain
        assert len(props) == 3
        json_names = {p["json_name"] for p in props}
        assert json_names == {"level1_prop", "level2_prop", "level3_prop"}

    def test_empty_properties_with_no_composition(self):
        """Test schema with no properties and no composition."""
        self.schemas["schema:definitions/Empty"] = {
            "id": "schema:definitions/Empty",
            "properties": [],
            "required": [],
        }

        schema = self.schemas["schema:definitions/Empty"]
        props, required = self.resolver.resolve_properties(schema)

        assert props == []
        assert required == []

    def test_oneof_ignored(self):
        """Test that oneOf composition is currently ignored (only allOf supported)."""
        self.schemas["schema:definitions/OneOf"] = {
            "id": "schema:definitions/OneOf",
            "properties": [{"json_name": "direct", "schema_id": "schema:types/string"}],
            "required": [],
            "composition": {
                "kind": "oneOf",
                "members": ["schema:definitions/Base"],
            },
        }

        schema = self.schemas["schema:definitions/OneOf"]
        props, _ = self.resolver.resolve_properties(schema)

        # Should only have the direct property (oneOf not processed)
        assert len(props) == 1
        assert props[0]["json_name"] == "direct"


def test_convenience_function():
    """Test the resolve_schema_properties convenience function."""
    schemas = {
        "schema:test": {
            "id": "schema:test",
            "properties": [{"json_name": "x", "schema_id": "schema:types/string"}],
        }
    }

    props, required = resolve_schema_properties(
        schemas["schema:test"],
        lambda x: schemas.get(x),
        schemas,
    )

    assert len(props) == 1
    assert props[0]["json_name"] == "x"
    assert required == []
