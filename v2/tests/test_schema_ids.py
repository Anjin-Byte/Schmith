"""Tests for shared/schema_ids.py."""

from schmith.shared.schema_ids import schema_id_for_schema, schema_id_from_ref
from schmith.shared.hashing import canonical_json_hash


class TestSchemaIdFromRef:
    def test_components_schemas_ref(self) -> None:
        assert schema_id_from_ref("#/components/schemas/Customer") == "schema:components/Customer"

    def test_definitions_ref(self) -> None:
        assert schema_id_from_ref("#/definitions/Order") == "schema:definitions/Order"

    def test_other_components_ref(self) -> None:
        # Non-schema components refs use underscores for path separators
        result = schema_id_from_ref("#/components/responses/NotFound")
        assert "NotFound" in result
        assert result.startswith("schema:components")

    def test_arbitrary_ref(self) -> None:
        # Arbitrary refs use underscores for path separators
        result = schema_id_from_ref("#/custom/path/Type")
        assert "Type" in result
        assert result.startswith("schema:ref")


class TestSchemaIdForSchema:
    def test_ref_schema(self) -> None:
        schema = {"$ref": "#/components/schemas/Customer"}
        assert schema_id_for_schema(schema) == "schema:components/Customer"

    def test_inline_schema_produces_anon_id(self) -> None:
        schema = {"type": "object", "properties": {"id": {"type": "string"}}}
        result = schema_id_for_schema(schema)
        assert result is not None
        assert "anon/" in result

    def test_same_inline_schema_same_id(self) -> None:
        schema = {"type": "object", "properties": {"id": {"type": "string"}}}
        assert schema_id_for_schema(schema) == schema_id_for_schema(schema)

    def test_key_order_does_not_affect_anon_id(self) -> None:
        a = {"properties": {"id": {"type": "string"}}, "type": "object"}
        b = {"type": "object", "properties": {"id": {"type": "string"}}}
        assert schema_id_for_schema(a) == schema_id_for_schema(b)

    def test_non_dict_returns_none(self) -> None:
        assert schema_id_for_schema(None) is None  # type: ignore[arg-type]
        assert schema_id_for_schema("string") is None  # type: ignore[arg-type]
        assert schema_id_for_schema(42) is None  # type: ignore[arg-type]

    def test_primitive_string_returns_canonical_type_id(self) -> None:
        # Simple primitives use canonical schema:types/... IDs, not hashes,
        # so description/example metadata doesn't fragment the type space.
        assert schema_id_for_schema({"type": "string"}) == "schema:types/string"
        assert schema_id_for_schema({"type": "string", "description": "An ID", "example": "abc"}) == "schema:types/string"

    def test_primitive_integer_returns_canonical_type_id(self) -> None:
        assert schema_id_for_schema({"type": "integer"}) == "schema:types/integer"

    def test_primitive_boolean_returns_canonical_type_id(self) -> None:
        assert schema_id_for_schema({"type": "boolean"}) == "schema:types/boolean"

    def test_string_date_time_format_maps_to_datetime(self) -> None:
        assert schema_id_for_schema({"type": "string", "format": "date-time"}) == "schema:types/datetime"

    def test_string_date_format_maps_to_date(self) -> None:
        assert schema_id_for_schema({"type": "string", "format": "date"}) == "schema:types/date"

    def test_enum_still_gets_anon_hash(self) -> None:
        # Enums are NOT collapsed to schema:types/string — they are distinct types.
        schema = {"type": "string", "enum": ["a", "b"]}
        result = schema_id_for_schema(schema)
        assert result is not None
        assert result.startswith("schema:anon/")

    def test_object_with_properties_still_gets_anon_hash(self) -> None:
        schema = {"type": "object", "properties": {"id": {"type": "integer"}}}
        result = schema_id_for_schema(schema)
        assert result is not None
        assert result.startswith("schema:anon/")
