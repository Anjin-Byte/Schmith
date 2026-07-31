"""Tests for schmith/adapters/procore.py — ProcoreAdapter."""

from __future__ import annotations

from typing import Any

import pytest

from schmith.adapters.procore import ProcoreAdapter


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _prop(json_name: str, description: str = "") -> dict[str, Any]:
    return {
        "json_name": json_name,
        "schema_id": f"schema:types/string",
        "required": False,
        "nullable": True,
        "description": description,
        "deprecated": None,
        "read_only": None,
        "write_only": None,
        "examples": None,
        "constraints": {},
        "enum_values": None,
        "enum_names": None,
        "resolved_type": None,
    }


def _type(name: str, props: list[dict[str, Any]], kind: str = "object", is_inline: bool = False) -> dict[str, Any]:
    return {
        "schema_id": f"schema:anon/{name.lower()}",
        "name": name,
        "kind": kind,
        "description": None,
        "properties": props,
        "required": [],
        "enum_values": None,
        "enum_names": None,
        "is_inline": is_inline,
    }


def _data_prop(resolved_type: str) -> dict[str, Any]:
    """A property named 'data' with the given resolved_type (typically an array)."""
    return {
        "json_name": "data",
        "schema_id": "schema:anon/arrayschema",
        "required": False,
        "nullable": None,
        "description": None,
        "deprecated": None,
        "read_only": None,
        "write_only": None,
        "examples": None,
        "constraints": {},
        "enum_values": None,
        "enum_names": None,
        "resolved_type": resolved_type,
    }


# ---------------------------------------------------------------------------
# transform_tree — no composition segments present
# ---------------------------------------------------------------------------


class TestTransformTreeNoSegments:
    def test_passthrough_when_no_normal_or_extended(self) -> None:
        adapter = ProcoreAdapter()
        root = _type("Project", [_prop("id"), _prop("name")])
        nested = [_type("Company", [_prop("id"), _prop("company_name")])]
        out_root, out_nested = adapter.transform_tree(root, nested)
        assert out_root is root
        assert out_nested is nested

    def test_empty_nested_types_unchanged(self) -> None:
        adapter = ProcoreAdapter()
        root = _type("Project", [_prop("id")])
        out_root, out_nested = adapter.transform_tree(root, [])
        assert out_root is root
        assert out_nested == []


# ---------------------------------------------------------------------------
# transform_tree — composition segments are removed
# ---------------------------------------------------------------------------


class TestTransformTreeSegmentsRemoved:
    def test_normal_segment_removed(self) -> None:
        adapter = ProcoreAdapter()
        root = _type("Project", [_prop("id")])
        normal = _type("Normal", [_prop("id"), _prop("name")])
        _, out_nested = adapter.transform_tree(root, [normal])
        assert not any(t["name"] == "Normal" for t in out_nested)

    def test_extended_segment_removed(self) -> None:
        adapter = ProcoreAdapter()
        root = _type("Project", [_prop("id")])
        extended = _type("Extended", [_prop("id"), _prop("departments")])
        _, out_nested = adapter.transform_tree(root, [extended])
        assert not any(t["name"] == "Extended" for t in out_nested)

    def test_both_segments_removed(self) -> None:
        adapter = ProcoreAdapter()
        root = _type("Project", [_prop("id")])
        normal = _type("Normal", [_prop("id"), _prop("name")])
        extended = _type("Extended", [_prop("id"), _prop("departments")])
        _, out_nested = adapter.transform_tree(root, [normal, extended])
        names = [t["name"] for t in out_nested]
        assert "Normal" not in names
        assert "Extended" not in names

    def test_non_segment_nested_types_preserved(self) -> None:
        adapter = ProcoreAdapter()
        root = _type("Project", [_prop("id")])
        normal = _type("Normal", [_prop("name")])
        company = _type("Company", [_prop("id"), _prop("company_name")])
        dept = _type("Department", [_prop("id"), _prop("dept_name")])
        _, out_nested = adapter.transform_tree(root, [normal, company, dept])
        names = [t["name"] for t in out_nested]
        assert "Company" in names
        assert "Department" in names
        assert "Normal" not in names


# ---------------------------------------------------------------------------
# transform_tree — field merging
# ---------------------------------------------------------------------------


class TestTransformTreeFieldMerging:
    def test_unique_segment_fields_added_to_root(self) -> None:
        adapter = ProcoreAdapter()
        root = _type("Project", [_prop("id"), _prop("name")])
        extended = _type("Extended", [_prop("id"), _prop("departments"), _prop("flag")])
        out_root, _ = adapter.transform_tree(root, [extended])
        json_names = [p["json_name"] for p in out_root["properties"]]
        assert "departments" in json_names
        assert "flag" in json_names

    def test_duplicate_fields_not_added(self) -> None:
        """Fields already on root are not duplicated even if segments also have them."""
        adapter = ProcoreAdapter()
        root = _type("Project", [_prop("id"), _prop("name"), _prop("departments")])
        extended = _type("Extended", [_prop("id"), _prop("departments"), _prop("flag")])
        out_root, _ = adapter.transform_tree(root, [extended])
        json_names = [p["json_name"] for p in out_root["properties"]]
        assert json_names.count("departments") == 1
        assert "flag" in json_names

    def test_root_field_order_preserved_extras_appended(self) -> None:
        adapter = ProcoreAdapter()
        root = _type("Project", [_prop("id"), _prop("name")])
        extended = _type("Extended", [_prop("departments"), _prop("flag")])
        out_root, _ = adapter.transform_tree(root, [extended])
        props = out_root["properties"]
        # Root fields come first
        assert props[0]["json_name"] == "id"
        assert props[1]["json_name"] == "name"
        # Segment fields appended after
        extra_names = [p["json_name"] for p in props[2:]]
        assert "departments" in extra_names
        assert "flag" in extra_names

    def test_no_extras_root_is_unchanged(self) -> None:
        """When segment fields are all already on root, root is returned as-is."""
        adapter = ProcoreAdapter()
        root = _type("Project", [_prop("id"), _prop("name"), _prop("departments")])
        extended = _type("Extended", [_prop("id"), _prop("departments")])
        out_root, _ = adapter.transform_tree(root, [extended])
        # No new fields added — root object unchanged
        assert out_root is root

    def test_normal_before_extended_in_segment_order(self) -> None:
        """Segment fields are processed alphabetically: Extended before Normal.
        If both Normal and Extended have the same extra field, Normal's version
        should NOT appear because Extended is processed first (Extended < Normal
        alphabetically) and the field is already seen."""
        adapter = ProcoreAdapter()
        root = _type("Project", [_prop("id")])
        # Both segments have "extra_field"; Extended's version should win because
        # segments are sorted alphabetically (Extended < Normal)
        extended_extra = _prop("extra_field", "from extended")
        normal_extra = _prop("extra_field", "from normal")
        extended = _type("Extended", [extended_extra])
        normal = _type("Normal", [normal_extra])
        out_root, _ = adapter.transform_tree(root, [normal, extended])
        extra_props = [p for p in out_root["properties"] if p["json_name"] == "extra_field"]
        assert len(extra_props) == 1
        assert extra_props[0]["description"] == "from extended"

    def test_merging_from_both_normal_and_extended(self) -> None:
        adapter = ProcoreAdapter()
        root = _type("Project", [_prop("id")])
        # Normal has "name", Extended has "departments" — both should end up on root
        normal = _type("Normal", [_prop("id"), _prop("name")])
        extended = _type("Extended", [_prop("id"), _prop("departments")])
        out_root, _ = adapter.transform_tree(root, [normal, extended])
        json_names = [p["json_name"] for p in out_root["properties"]]
        assert "name" in json_names
        assert "departments" in json_names


# ---------------------------------------------------------------------------
# transform_tree — root metadata preserved
# ---------------------------------------------------------------------------


class TestTransformTreeRootMetadata:
    def test_root_name_unchanged(self) -> None:
        adapter = ProcoreAdapter()
        root = _type("Project", [_prop("id")])
        normal = _type("Normal", [_prop("name")])
        out_root, _ = adapter.transform_tree(root, [normal])
        assert out_root["name"] == "Project"

    def test_root_schema_id_unchanged(self) -> None:
        adapter = ProcoreAdapter()
        root = _type("Project", [_prop("id")])
        root["schema_id"] = "schema:anon/original_hash"
        normal = _type("Normal", [_prop("name")])
        out_root, _ = adapter.transform_tree(root, [normal])
        assert out_root["schema_id"] == "schema:anon/original_hash"

    def test_root_kind_unchanged(self) -> None:
        adapter = ProcoreAdapter()
        root = _type("Project", [_prop("id")])
        extended = _type("Extended", [_prop("departments")])
        out_root, _ = adapter.transform_tree(root, [extended])
        assert out_root["kind"] == "object"

    def test_root_description_unchanged(self) -> None:
        adapter = ProcoreAdapter()
        root = _type("Project", [_prop("id")])
        root["description"] = "A Procore project."
        extended = _type("Extended", [_prop("departments")])
        out_root, _ = adapter.transform_tree(root, [extended])
        assert out_root["description"] == "A Procore project."


# ---------------------------------------------------------------------------
# Realistic scenario: GET /rest/v1.1/projects structure
# ---------------------------------------------------------------------------


class TestProcoreProjectScenario:
    """End-to-end scenario mirroring the actual GET /rest/v1.1/projects output."""

    def test_project_normal_extended_collapse(self) -> None:
        """The LLM confusion scenario: Normal and Extended removed, extra fields merged."""
        adapter = ProcoreAdapter()

        core_fields = [_prop(n) for n in ["id", "name", "active", "status", "address"]]
        root = _type("Project", core_fields)

        # Normal: 47 fields — subset of core + some extras
        normal_fields = [_prop(n) for n in ["id", "name", "active", "logo_url", "inbound_email"]]
        normal = _type("Normal", normal_fields)

        # Extended: 59 fields — superset of Normal + more
        extended_fields = normal_fields + [
            _prop(n) for n in ["departments", "dictionary_type", "flag", "office", "program"]
        ]
        extended = _type("Extended", extended_fields)

        # Real nested types that should survive
        company = _type("ProjectCompany", [_prop("id"), _prop("company_name")])
        dept = _type("ProjectDepartment", [_prop("id"), _prop("dept_name")])

        out_root, out_nested = adapter.transform_tree(root, [normal, extended, company, dept])

        # Normal and Extended are gone
        out_names = [t["name"] for t in out_nested]
        assert "Normal" not in out_names
        assert "Extended" not in out_names

        # Real types survived
        assert "ProjectCompany" in out_names
        assert "ProjectDepartment" in out_names

        # Extra fields merged from segments
        json_names = [p["json_name"] for p in out_root["properties"]]
        for f in ["id", "name", "active", "status", "address"]:
            assert f in json_names, f"Core field '{f}' should be on merged root"
        for f in ["logo_url", "inbound_email", "departments", "dictionary_type", "flag"]:
            assert f in json_names, f"Segment field '{f}' should be merged into root"

        # No duplicates
        assert len(json_names) == len(set(json_names))


# ---------------------------------------------------------------------------
# _unwrap_data_envelope
# ---------------------------------------------------------------------------


class TestUnwrapDataEnvelope:
    """Tests for the { data: [Item] } envelope unwrap transform."""

    def test_item_type_promoted_to_root(self) -> None:
        """The item nested type becomes the new root."""
        adapter = ProcoreAdapter()
        item = _type("Anonymous_abcdDataNestedItem", [_prop("id"), _prop("name")])
        root = _type("EquipmentRegisterCategory", [_data_prop("Anonymous_abcdDataNestedItem[]")], is_inline=True)
        new_root, _ = adapter.transform_tree(root, [item])
        assert new_root["properties"] == item["properties"]

    def test_promoted_root_takes_envelope_name(self) -> None:
        """The new root inherits the endpoint-derived name from the envelope."""
        adapter = ProcoreAdapter()
        item = _type("Anonymous_abcdDataNestedItem", [_prop("id")])
        root = _type("EquipmentRegisterCategory", [_data_prop("Anonymous_abcdDataNestedItem[]")], is_inline=True)
        new_root, _ = adapter.transform_tree(root, [item])
        assert new_root["name"] == "EquipmentRegisterCategory"

    def test_promoted_root_not_inline(self) -> None:
        """Promoted root has is_inline cleared."""
        adapter = ProcoreAdapter()
        item = _type("Anonymous_abcdDataNestedItem", [_prop("id")], is_inline=True)
        root = _type("EquipmentRegisterCategory", [_data_prop("Anonymous_abcdDataNestedItem[]")], is_inline=True)
        new_root, _ = adapter.transform_tree(root, [item])
        assert new_root["is_inline"] is False

    def test_promoted_item_removed_from_nested(self) -> None:
        """The promoted item type is no longer in nested_types."""
        adapter = ProcoreAdapter()
        item = _type("Anonymous_abcdDataNestedItem", [_prop("id")])
        root = _type("EquipmentRegisterCategory", [_data_prop("Anonymous_abcdDataNestedItem[]")], is_inline=True)
        _, remaining = adapter.transform_tree(root, [item])
        assert not any(t["name"] == "Anonymous_abcdDataNestedItem" for t in remaining)

    def test_other_nested_types_preserved(self) -> None:
        """Non-item nested types (referenced from item's properties) are kept."""
        adapter = ProcoreAdapter()
        item = _type("Anonymous_abcdDataNestedItem", [_prop("id"), _prop("category")])
        sub = _type("DataNestedItemCategory", [_prop("id"), _prop("name")])
        root = _type("EquipmentRegisterType", [_data_prop("Anonymous_abcdDataNestedItem[]")], is_inline=True)
        _, remaining = adapter.transform_tree(root, [item, sub])
        assert any(t["name"] == "DataNestedItemCategory" for t in remaining)

    def test_skips_when_not_inline(self) -> None:
        """No unwrap when root is not an inline schema."""
        adapter = ProcoreAdapter()
        item = _type("Anonymous_abcdDataNestedItem", [_prop("id")])
        root = _type("SomeNamedType", [_data_prop("Anonymous_abcdDataNestedItem[]")], is_inline=False)
        out_root, out_nested = adapter.transform_tree(root, [item])
        assert out_root["name"] == "SomeNamedType"
        assert out_root["properties"][0]["json_name"] == "data"

    def test_skips_when_multiple_properties(self) -> None:
        """No unwrap when root has more than one property."""
        adapter = ProcoreAdapter()
        item = _type("Anonymous_abcdDataNestedItem", [_prop("id")])
        root = _type("Wrapper", [_data_prop("Anonymous_abcdDataNestedItem[]"), _prop("total")], is_inline=True)
        out_root, _ = adapter.transform_tree(root, [item])
        # Root unchanged — still has 'data' + 'total'
        assert len(out_root["properties"]) == 2

    def test_skips_when_property_not_named_data(self) -> None:
        """No unwrap when the single property is not named 'data'."""
        adapter = ProcoreAdapter()
        item = _type("Anonymous_abcdItemsNestedItem", [_prop("id")])
        items_prop = {**_data_prop("Anonymous_abcdItemsNestedItem[]"), "json_name": "items"}
        root = _type("Wrapper", [items_prop], is_inline=True)
        out_root, _ = adapter.transform_tree(root, [item])
        assert out_root["name"] == "Wrapper"

    def test_skips_when_data_is_not_array(self) -> None:
        """No unwrap when 'data' resolved_type doesn't end with '[]'."""
        adapter = ProcoreAdapter()
        item = _type("DataObject", [_prop("id")])
        non_array_prop = {**_data_prop("DataObject"), "json_name": "data"}
        root = _type("Wrapper", [non_array_prop], is_inline=True)
        out_root, _ = adapter.transform_tree(root, [item])
        assert out_root["name"] == "Wrapper"

    def test_skips_when_array_item_is_primitive(self) -> None:
        """No unwrap when 'data' is an array of a primitive type."""
        adapter = ProcoreAdapter()
        root = _type("Wrapper", [_data_prop("string[]")], is_inline=True)
        out_root, out_nested = adapter.transform_tree(root, [])
        assert out_root["name"] == "Wrapper"
        assert out_nested == []

    def test_skips_when_item_type_not_in_nested(self) -> None:
        """No unwrap when the named item type doesn't exist in nested_types."""
        adapter = ProcoreAdapter()
        root = _type("Wrapper", [_data_prop("Anonymous_abcdDataNestedItem[]")], is_inline=True)
        out_root, _ = adapter.transform_tree(root, [])
        assert out_root["name"] == "Wrapper"

    def test_unwrap_then_composition_merge(self) -> None:
        """Both transforms compose correctly: envelope unwrap + segment merge."""
        adapter = ProcoreAdapter()
        # Item type has composition segments
        item = _type("Anonymous_abcdDataNestedItem", [_prop("id")])
        normal = _type("Normal", [_prop("id"), _prop("name")])
        root = _type("EquipmentType", [_data_prop("Anonymous_abcdDataNestedItem[]")], is_inline=True)
        new_root, remaining = adapter.transform_tree(root, [item, normal])
        # Item promoted and renamed
        assert new_root["name"] == "EquipmentType"
        # Normal merged into root, not in remaining
        assert not any(t["name"] == "Normal" for t in remaining)
        # name field merged from Normal
        json_names = [p["json_name"] for p in new_root["properties"]]
        assert "name" in json_names
