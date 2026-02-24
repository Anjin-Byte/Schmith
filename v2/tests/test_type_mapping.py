"""Tests for generation/type_mapping.py."""

from schmith.generation.type_mapping import (
    build_field_info,
    extract_clean_name,
    format_data_object_name,
    is_shapeless_schema,
    json_name_to_csharp_property,
    schema_id_to_csharp_type,
)


class TestJsonNameToCsharpProperty:
    def test_camel_case_capitalizes_first_letter_only(self) -> None:
        # The function splits on _-\s only, so camelCase is capitalized as one word
        assert json_name_to_csharp_property("firstName") == "Firstname"

    def test_snake_case(self) -> None:
        assert json_name_to_csharp_property("first_name") == "FirstName"

    def test_kebab_case(self) -> None:
        assert json_name_to_csharp_property("first-name") == "FirstName"

    def test_single_word(self) -> None:
        assert json_name_to_csharp_property("id") == "Id"

    def test_pascal_case_capitalizes_first_letter_only(self) -> None:
        # Already PascalCase passes through; first letter is recapitalized but
        # since it's one "word" (no separators), only the whole word is capitalized
        assert json_name_to_csharp_property("FirstName") == "Firstname"

    def test_underscore_snake_case(self) -> None:
        assert json_name_to_csharp_property("customer_id") == "CustomerId"

    # -- Template placeholder (%{...}) handling -----------------------------------

    def test_template_boolean_discriminator(self) -> None:
        # custom_field_%{custom_field_boolean_definition_id} → CustomFieldBoolean
        result = json_name_to_csharp_property(
            "custom_field_%{custom_field_boolean_definition_id}"
        )
        assert result == "CustomFieldBoolean"

    def test_template_string_discriminator(self) -> None:
        result = json_name_to_csharp_property(
            "custom_field_%{custom_field_string_definition_id}"
        )
        assert result == "CustomFieldString"

    def test_template_integer_discriminator(self) -> None:
        result = json_name_to_csharp_property(
            "custom_field_%{custom_field_integer_definition_id}"
        )
        assert result == "CustomFieldInteger"

    def test_template_multi_word_discriminator(self) -> None:
        # "lov_entry" has two parts not matching the prefix
        result = json_name_to_csharp_property(
            "custom_field_%{custom_field_lov_entry_definition_id}"
        )
        assert result == "CustomFieldLovEntry"

    def test_no_template_passthrough(self) -> None:
        # Names without %{...} are unaffected
        assert json_name_to_csharp_property("custom_field_type") == "CustomFieldType"


class TestExtractCleanName:
    def test_name_hint_with_typ_prefix(self) -> None:
        assert extract_clean_name("schema:types/typ.Customer", "typ.Customer") == "Customer"

    def test_name_hint_without_prefix(self) -> None:
        assert extract_clean_name("schema:components/Customer", "Customer") == "Customer"

    def test_no_name_hint_anon(self) -> None:
        result = extract_clean_name("schema:anon/abc12345def", None)
        assert result.startswith("Anonymous_")

    def test_no_name_hint_component(self) -> None:
        result = extract_clean_name("schema:components/Customer", None)
        assert result == "Customer"


class TestSchemaIdToCsharpType:
    def setup_method(self) -> None:
        self.schemas: dict[str, dict] = {
            "schema:components/Customer": {
                "kind": "object",
                "name_hint": "Customer",
                "properties": [],
            },
            "schema:anon/abc": {
                "kind": "object",
                "properties": [],
            },
        }

    def test_primitive_string(self) -> None:
        t, is_complex = schema_id_to_csharp_type("schema:types/string", self.schemas)
        assert t == "string"
        assert not is_complex

    def test_primitive_integer(self) -> None:
        t, _ = schema_id_to_csharp_type("schema:types/integer", self.schemas)
        assert t == "int"

    def test_named_component(self) -> None:
        t, is_complex = schema_id_to_csharp_type("schema:components/Customer", self.schemas)
        assert t == "Customer"
        assert is_complex

    def test_unknown_schema_returns_object(self) -> None:
        t, _ = schema_id_to_csharp_type("schema:components/Missing", self.schemas)
        assert t == "object"

    def test_any_type(self) -> None:
        t, _ = schema_id_to_csharp_type("schema:types/any", self.schemas)
        assert t == "JsonElement"


class TestIsShapelessSchema:
    def test_no_schema(self) -> None:
        assert is_shapeless_schema(None, {})

    def test_any_kind(self) -> None:
        assert is_shapeless_schema({"kind": "any"}, {})

    def test_object_with_properties_is_not_shapeless(self) -> None:
        schema = {"kind": "object", "properties": [{"json_name": "id"}]}
        assert not is_shapeless_schema(schema, {})

    def test_object_without_properties_is_shapeless(self) -> None:
        schema = {"kind": "object"}
        assert is_shapeless_schema(schema, {})

    def test_enum_is_not_shapeless(self) -> None:
        schema = {"kind": "string", "enum_values": ["a", "b"]}
        assert not is_shapeless_schema(schema, {})


class TestBuildFieldInfo:
    def setup_method(self) -> None:
        self.schemas: dict[str, dict] = {
            "schema:types/string": {},
            "schema:components/Address": {
                "kind": "object",
                "name_hint": "Address",
                "properties": [],
            },
        }

    def test_simple_string_field(self) -> None:
        prop = {
            "json_name": "first_name",
            "schema_id": "schema:types/string",
            "description": "User's first name",
            "nullable": True,
            "required": False,
        }
        info = build_field_info(prop, self.schemas)
        assert info["json_name"] == "first_name"
        assert info["csharp_name"] == "FirstName"
        assert info["csharp_type"] == "string"
        assert info["nullable"] is True
        assert info["description"] == "User's first name"

    def test_required_field(self) -> None:
        prop = {
            "json_name": "id",
            "schema_id": "schema:types/string",
            "required": True,
            "nullable": False,
        }
        info = build_field_info(prop, self.schemas)
        assert info["required"] is True

    def test_complex_type_field(self) -> None:
        prop = {
            "json_name": "address",
            "schema_id": "schema:components/Address",
            "nullable": True,
        }
        info = build_field_info(prop, self.schemas)
        assert info["csharp_type"] == "Address"
        assert info["is_complex_type"] is True


class TestFormatDataObjectName:
    def test_already_has_suffix(self) -> None:
        assert format_data_object_name("CustomerDataObject") == "CustomerDataObject"

    def test_adds_suffix(self) -> None:
        assert format_data_object_name("Customer") == "CustomerDataObject"
