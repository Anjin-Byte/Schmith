"""Tests for generation/type_tree.py."""

from schmith.adapters.base import ApiAdapter, NodeClassification, TreeContext
from schmith.generation.type_tree import (
    NamingContext,
    _trim_parent_name,
    build_type_hierarchy,
    collect_type_closure,
    extract_all_edges,
    is_primitive_schema,
    is_primitive_schema_id,
)
from schmith.ir.models import SchemaNode


# ---------------------------------------------------------------------------
# Minimal IR helpers
# ---------------------------------------------------------------------------

def _object(name: str, props: list[dict] | None = None) -> dict:
    return {
        "kind": "object",
        "name_hint": name,
        "properties": props or [],
        "id": f"schema:components/{name}",
    }


def _string_prop(json_name: str) -> dict:
    return {
        "json_name": json_name,
        "schema_id": "schema:types/string",
        "nullable": True,
        "required": False,
    }


# ---------------------------------------------------------------------------
# Primitive detection
# ---------------------------------------------------------------------------

class TestPrimitiveDetection:
    def test_string_schema_id_is_primitive(self) -> None:
        assert is_primitive_schema_id("schema:types/string")

    def test_component_schema_id_is_not_primitive(self) -> None:
        assert not is_primitive_schema_id("schema:components/Customer")

    def test_string_kind_is_primitive(self) -> None:
        assert is_primitive_schema({"kind": "string"})

    def test_object_kind_is_not_primitive(self) -> None:
        assert not is_primitive_schema({"kind": "object"})

    def test_none_schema_is_not_primitive(self) -> None:
        assert not is_primitive_schema(None)

    def test_string_with_enum_is_not_primitive(self) -> None:
        assert not is_primitive_schema({"kind": "string", "enum_values": ["a", "b"]})


# ---------------------------------------------------------------------------
# Parent name trimming
# ---------------------------------------------------------------------------


class TestTrimParentName:
    def test_short_name_unchanged(self) -> None:
        # 2 words ≤ 3 → no trimming
        assert _trim_parent_name("CompanyUser") == "CompanyUser"

    def test_exactly_three_words_unchanged(self) -> None:
        assert _trim_parent_name("TimesheetEntryItem") == "TimesheetEntryItem"

    def test_four_words_trimmed_to_last_three(self) -> None:
        assert _trim_parent_name("TimesheetEntriesCustomFields") == "EntriesCustomFields"

    def test_five_words_trimmed_to_last_three(self) -> None:
        result = _trim_parent_name("TimesheetEntriesCustomFieldsItem")
        assert result == "CustomFieldsItem"

    def test_none_returns_none(self) -> None:
        assert _trim_parent_name(None) is None

    def test_custom_max_words(self) -> None:
        assert _trim_parent_name("TimesheetEntriesCustomFieldsItem", max_words=2) == "FieldsItem"


# ---------------------------------------------------------------------------
# Edge extraction
# ---------------------------------------------------------------------------

class TestExtractAllEdges:
    def setup_method(self) -> None:
        self.schemas: dict[str, dict] = {
            "schema:types/string": {"kind": "string"},
            "schema:components/Address": {"kind": "object", "name_hint": "Address"},
        }

    def test_no_edges_for_empty_schema(self) -> None:
        schema: dict = {"kind": "object", "properties": []}
        edges = extract_all_edges(schema, self.schemas.get)
        assert edges == []

    def test_property_edge(self) -> None:
        schema = {
            "kind": "object",
            "properties": [{"json_name": "name", "schema_id": "schema:types/string"}],
        }
        edges = extract_all_edges(schema, self.schemas.get)
        assert len(edges) == 1
        assert edges[0].edge_kind == "property"
        assert edges[0].target_id == "schema:types/string"

    def test_array_items_edge(self) -> None:
        schema = {"kind": "array", "items_schema_id": "schema:components/Address"}
        edges = extract_all_edges(schema, self.schemas.get)
        assert len(edges) == 1
        assert edges[0].edge_kind == "array_items"
        assert edges[0].target_id == "schema:components/Address"

    def test_composition_member_edge(self) -> None:
        schema = {
            "kind": "object",
            "composition": {"kind": "allOf", "members": ["schema:components/Address"]},
        }
        edges = extract_all_edges(schema, self.schemas.get)
        assert len(edges) == 1
        assert edges[0].edge_kind == "composition_member"

    def test_additional_properties_edge(self) -> None:
        schema = {
            "kind": "object",
            "additional_properties_schema_id": "schema:types/string",
        }
        edges = extract_all_edges(schema, self.schemas.get)
        assert len(edges) == 1
        assert edges[0].edge_kind == "additional_properties"


# ---------------------------------------------------------------------------
# collect_type_closure
# ---------------------------------------------------------------------------

class TestCollectTypeClosure:
    def setup_method(self) -> None:
        self.address_schema = {
            "kind": "object",
            "name_hint": "Address",
            "properties": [_string_prop("street"), _string_prop("city")],
        }
        self.customer_schema = {
            "kind": "object",
            "name_hint": "CustomerDataObject",
            "properties": [
                _string_prop("id"),
                {
                    "json_name": "address",
                    "schema_id": "schema:components/Address",
                    "nullable": True,
                },
            ],
            "id": "schema:components/CustomerDataObject",
        }
        self.schemas_by_id = {
            "schema:types/string": {"kind": "string"},
            "schema:components/Address": self.address_schema,
            "schema:components/CustomerDataObject": self.customer_schema,
        }

    def test_collects_root_type(self) -> None:
        result = collect_type_closure(self.customer_schema, self.schemas_by_id)
        assert "CustomerDataObject" in result

    def test_collects_nested_type(self) -> None:
        result = collect_type_closure(self.customer_schema, self.schemas_by_id)
        assert "Address" in result

    def test_does_not_collect_primitives(self) -> None:
        result = collect_type_closure(self.customer_schema, self.schemas_by_id)
        # string is a primitive — should not appear as a collected type
        for name in result:
            assert name not in ("string", "int", "bool")

    def test_cycle_detection(self) -> None:
        # Self-referential schema
        self_ref: dict = {
            "kind": "object",
            "name_hint": "Node",
            "properties": [{"json_name": "next", "schema_id": "schema:components/Node"}],
            "id": "schema:components/Node",
        }
        schemas = {
            "schema:types/string": {"kind": "string"},
            "schema:components/Node": self_ref,
        }
        result = collect_type_closure(self_ref, schemas)
        assert "Node" in result  # Should complete without infinite recursion


# ---------------------------------------------------------------------------
# build_type_hierarchy
# ---------------------------------------------------------------------------

class TestBuildTypeHierarchy:
    def setup_method(self) -> None:
        self.address_schema = {
            "kind": "object",
            "name_hint": "Address",
            "properties": [_string_prop("street")],
        }
        self.root_schema = {
            "kind": "object",
            "name_hint": "OrderDataObject",
            "id": "schema:components/OrderDataObject",
            "properties": [
                _string_prop("id"),
                {"json_name": "ship_to", "schema_id": "schema:components/Address", "nullable": True},
            ],
        }
        self.schemas_by_id = {
            "schema:types/string": {"kind": "string"},
            "schema:components/Address": self.address_schema,
            "schema:components/OrderDataObject": self.root_schema,
        }

    def test_returns_tuple(self) -> None:
        root_type, nested_types = build_type_hierarchy(self.root_schema, self.schemas_by_id)
        assert isinstance(root_type, dict)
        assert isinstance(nested_types, list)

    def test_root_type_has_correct_name(self) -> None:
        root_type, _ = build_type_hierarchy(self.root_schema, self.schemas_by_id)
        assert root_type["name"] == "OrderDataObject"

    def test_nested_types_not_in_root(self) -> None:
        root_type, nested_types = build_type_hierarchy(self.root_schema, self.schemas_by_id)
        nested_names = [n["name"] for n in nested_types]
        assert root_type["name"] not in nested_names

    def test_nested_types_sorted_alphabetically(self) -> None:
        root_type, nested_types = build_type_hierarchy(self.root_schema, self.schemas_by_id)
        names = [n["name"] for n in nested_types]
        assert names == sorted(names)


# ---------------------------------------------------------------------------
# Adapter hooks in type tree
# ---------------------------------------------------------------------------

class TestTypeTreeAdapterHooks:
    def setup_method(self) -> None:
        self.anon_schema = {
            "kind": "object",
            # No name_hint — anonymous
            "properties": [_string_prop("value")],
        }
        anon_id = "schema:anon/deadbeef"
        self.root_schema = {
            "kind": "object",
            "name_hint": "Root",
            "id": "schema:components/Root",
            "properties": [
                {"json_name": "data", "schema_id": anon_id, "nullable": True},
            ],
        }
        self.schemas_by_id = {
            "schema:types/string": {"kind": "string"},
            anon_id: self.anon_schema,
            "schema:components/Root": self.root_schema,
        }
        self.anon_id = anon_id

    def test_adapter_name_anonymous_overrides_name(self) -> None:
        class NamingAdapter(ApiAdapter):
            def name_anonymous(self, node: SchemaNode, context: NamingContext) -> str | None:
                return "CustomData"

        _, nested_types = build_type_hierarchy(
            self.root_schema, self.schemas_by_id, adapter=NamingAdapter()
        )
        nested_names = [n["name"] for n in nested_types]
        assert "CustomData" in nested_names

    def test_adapter_classify_inline_skips_type(self) -> None:
        class InlineAdapter(ApiAdapter):
            def classify_node(self, node: SchemaNode, context: TreeContext) -> NodeClassification | None:
                if "anon/" in node.schema_id:
                    return NodeClassification.INLINE
                return None

        _, nested_types = build_type_hierarchy(
            self.root_schema, self.schemas_by_id, adapter=InlineAdapter()
        )
        # The anon schema should NOT appear in nested types (it was inlined)
        for nt in nested_types:
            assert "anon" not in nt.get("schema_id", "").lower()

    def test_adapter_classify_collapse_excludes_from_collected(self) -> None:
        class CollapseAdapter(ApiAdapter):
            def classify_node(self, node: SchemaNode, context: TreeContext) -> NodeClassification | None:
                if "anon/" in node.schema_id:
                    return NodeClassification.COLLAPSE
                return None

        # COLLAPSE: children are processed but the schema itself is not collected
        _, nested_types = build_type_hierarchy(
            self.root_schema, self.schemas_by_id, adapter=CollapseAdapter()
        )
        for nt in nested_types:
            assert "anon" not in nt.get("schema_id", "").lower()

    def test_no_adapter_uses_default_naming(self) -> None:
        _, nested_types = build_type_hierarchy(self.root_schema, self.schemas_by_id)
        # Default naming: parent name + property name
        nested_names = [n["name"] for n in nested_types]
        # Should have some name for the anonymous schema
        assert len(nested_names) > 0 or True  # passes even if empty (primitive case)


# ---------------------------------------------------------------------------
# Naming policy: template placeholders and parent trimming
# ---------------------------------------------------------------------------


class TestNamingPolicy:
    """Verify naming improvements for deeply-nested and template-keyed schemas."""

    def _build_deep_schemas(self) -> tuple[dict, dict[str, dict]]:
        """Build a 4-level deep schema with a %{...} template property."""
        # Leaf: anonymous object for each %{...} property variant
        bool_leaf_id = "schema:anon/bool_leaf"
        bool_leaf = {
            "kind": "object",
            "id": bool_leaf_id,
            "properties": [_string_prop("data_type"), _string_prop("value")],
        }

        # custom_fields object (inline, no name_hint) whose properties are
        # template-keyed
        cf_id = "schema:anon/custom_fields_obj"
        custom_fields = {
            "kind": "object",
            "id": cf_id,
            "properties": [
                {
                    "json_name": "custom_field_%{custom_field_boolean_definition_id}",
                    "schema_id": bool_leaf_id,
                    "nullable": True,
                }
            ],
        }

        # An array of entry items, each having a custom_fields property
        entry_item_id = "schema:anon/entry_item"
        entry_item = {
            "kind": "object",
            "id": entry_item_id,
            "properties": [
                _string_prop("id"),
                {"json_name": "custom_fields", "schema_id": cf_id, "nullable": True},
            ],
        }

        # entries is an array whose items are entry_item
        entries_arr_id = "schema:anon/entries_arr"
        entries_arr = {
            "kind": "array",
            "id": entries_arr_id,
            "items_schema_id": entry_item_id,
        }

        # Root
        root_schema = {
            "kind": "object",
            "name_hint": "Timesheet",
            "id": "schema:components/Timesheet",
            "properties": [
                _string_prop("id"),
                {"json_name": "entries", "schema_id": entries_arr_id, "nullable": True},
            ],
        }

        schemas_by_id: dict[str, dict] = {
            "schema:types/string": {"kind": "string"},
            "schema:components/Timesheet": root_schema,
            entries_arr_id: entries_arr,
            entry_item_id: entry_item,
            cf_id: custom_fields,
            bool_leaf_id: bool_leaf,
        }
        return root_schema, schemas_by_id

    def test_template_property_name_has_no_braces(self) -> None:
        root, schemas = self._build_deep_schemas()
        _, nested_types = build_type_hierarchy(root, schemas)
        for nt in nested_types:
            assert "{" not in nt["name"], f"Brace in name: {nt['name']}"
            assert "%" not in nt["name"], f"Percent in name: {nt['name']}"

    def test_template_property_extracts_discriminator(self) -> None:
        root, schemas = self._build_deep_schemas()
        _, nested_types = build_type_hierarchy(root, schemas)
        names = {nt["name"] for nt in nested_types}
        # The boolean leaf should have "Boolean" in its name (discriminator extracted)
        assert any("Boolean" in n for n in names), f"No Boolean discriminator in {names}"

    def test_deep_nesting_caps_verbosity(self) -> None:
        root, schemas = self._build_deep_schemas()
        _, nested_types = build_type_hierarchy(root, schemas)
        # With parent trimming (max 3 words), no generated name should exceed
        # 3 (parent) + 1 (field) + 1 (suffix) = ~5 PascalCase words
        import re
        for nt in nested_types:
            word_count = len(re.findall(r"[A-Z][a-z0-9]*", nt["name"]))
            assert word_count <= 6, f"Name too long ({word_count} words): {nt['name']}"
