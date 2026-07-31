"""Tests for Impl-3: Validation-Driven Retry Loop.

Covers:
  - validate_type_block()   : per-type block validation used by the retry loop
  - _build_correction_block(): formats errors as a LLM correction instruction
  - correction_block prompt injection in build_type_page_prompt()
"""

from __future__ import annotations

from typing import Any

import pytest

from specbridge.validation import ValidationResult, validate_type_block
from specbridge.pipeline import _build_correction_block


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

_MINIMAL_PACKET: dict[str, Any] = {
    "metadata": {"method": "GET", "path": "/foo", "response_description": ""},
    "generation": {"instructions": "", "example_code": ""},
    "nested_types": [],
}

_MINIMAL_TYPE_ENTRY: dict[str, Any] = {
    "name": "FooDataObject",
    "fields": [],
    "enum_values": None,
    "schema_id": "",
    "description": "",
    "kind": "object",
}


def _class_block(class_name: str, body: str = "") -> str:
    return f"public class {class_name}\n{{\n{body}\n}}"


# ---------------------------------------------------------------------------
# validate_type_block — structural checks
# ---------------------------------------------------------------------------


class TestValidateTypeBlockStructural:
    def test_clean_class_passes(self) -> None:
        code = _class_block("FooDataObject", '    [JsonPropertyName("id")]\n    public string? Id { get; init; }')
        te = {**_MINIMAL_TYPE_ENTRY, "name": "FooDataObject"}
        assert validate_type_block(code, te).is_clean

    def test_unbalanced_braces_is_error(self) -> None:
        # Missing closing brace
        code = "public class FooDataObject\n{\n    public string? Id { get; init; }\n"
        te = {**_MINIMAL_TYPE_ENTRY, "name": "FooDataObject"}
        result = validate_type_block(code, te)
        assert result.has_errors
        assert any(i.code == "STRUCTURAL" for i in result.errors)

    def test_stitch_marker_left_in_is_error(self) -> None:
        code = (
            "public class Foo\n{\n"
            "// BEGIN_FIELDS\n"
            '    [JsonPropertyName("name")]\n'
            "    public string? Name { get; init; }\n"
            "// END_FIELDS\n"
            "}"
        )
        te = {**_MINIMAL_TYPE_ENTRY, "name": "Foo"}
        result = validate_type_block(code, te)
        assert result.has_errors
        assert any(i.code == "ARTIFACT" for i in result.errors)

    def test_template_placeholder_is_error(self) -> None:
        # %{...} in the C# body (not inside a JsonPropertyName value) is an artifact.
        code = _class_block("Foo", "    public string? %{BadField} { get; init; }")
        te = {**_MINIMAL_TYPE_ENTRY, "name": "Foo"}
        result = validate_type_block(code, te)
        # ARTIFACT fires on template placeholder in code body
        assert any(i.code == "ARTIFACT" for i in result.errors)


# ---------------------------------------------------------------------------
# validate_type_block — MISSING_CLASS
# ---------------------------------------------------------------------------


class TestValidateTypeBlockMissingClass:
    def test_missing_class_is_error(self) -> None:
        code = '    [JsonPropertyName("id")]\n    public string? Id { get; init; }'
        te = {**_MINIMAL_TYPE_ENTRY, "name": "FooDataObject"}
        result = validate_type_block(code, te)
        assert result.has_errors
        assert any(i.code == "MISSING_CLASS" for i in result.errors)

    def test_data_object_suffix_accepted(self) -> None:
        # type_entry name is "Foo"; LLM generated "FooDataObject" — should pass
        code = _class_block("FooDataObject")
        te = {**_MINIMAL_TYPE_ENTRY, "name": "Foo"}
        assert validate_type_block(code, te).is_clean

    def test_clean_enum_passes(self) -> None:
        code = (
            "[JsonConverter(typeof(JsonStringEnumConverter))]\n"
            "public enum StatusEnum\n"
            "{\n"
            '    [JsonStringEnumMemberName("active")]\n'
            "    Active,\n"
            '    [JsonStringEnumMemberName("inactive")]\n'
            "    Inactive\n"
            "}"
        )
        te = {**_MINIMAL_TYPE_ENTRY, "name": "StatusEnum", "enum_values": ["active", "inactive"]}
        assert validate_type_block(code, te).is_clean


# ---------------------------------------------------------------------------
# validate_type_block — UNDECLARED_TYPE and known_external_types
# ---------------------------------------------------------------------------


class TestValidateTypeBlockUndeclaredType:
    def test_undeclared_type_in_nested_block_is_error(self) -> None:
        code = (
            "public class StatusType\n"
            "{\n"
            '    [JsonPropertyName("flag")]\n'
            "    public GhostEnum? Flag { get; init; }\n"
            "}"
        )
        te = {**_MINIMAL_TYPE_ENTRY, "name": "StatusType"}
        result = validate_type_block(code, te)
        assert result.has_errors
        assert any(i.code == "UNDECLARED_TYPE" for i in result.errors)

    def test_known_external_types_prevents_false_positive_on_root(self) -> None:
        """Root type referencing a nested enum should not be flagged as undeclared."""
        code = (
            "public class RootDataObject\n"
            "{\n"
            '    [JsonPropertyName("flag")]\n'
            "    public ExtendedFlag? Flag { get; init; }\n"
            "}"
        )
        te = {**_MINIMAL_TYPE_ENTRY, "name": "RootDataObject"}
        # Without known_external_types → ExtendedFlag is flagged
        without = validate_type_block(code, te)
        assert without.has_errors
        assert any(i.code == "UNDECLARED_TYPE" for i in without.errors)

        # With known_external_types → passes
        with_known = validate_type_block(code, te, known_external_types=frozenset({"ExtendedFlag"}))
        assert with_known.is_clean

    def test_primitive_types_pass(self) -> None:
        code = (
            "public class Foo\n"
            "{\n"
            '    [JsonPropertyName("name")]\n'
            "    public string? Name { get; init; }\n"
            '    [JsonPropertyName("count")]\n'
            "    public int? Count { get; init; }\n"
            '    [JsonPropertyName("ts")]\n'
            "    public DateTime? Ts { get; init; }\n"
            "}"
        )
        te = {**_MINIMAL_TYPE_ENTRY, "name": "Foo"}
        assert validate_type_block(code, te).is_clean

    def test_locally_declared_type_passes(self) -> None:
        code = (
            "public enum MyEnum { A, B }\n"
            "public class Foo\n"
            "{\n"
            '    [JsonPropertyName("e")]\n'
            "    public MyEnum? E { get; init; }\n"
            "}"
        )
        te = {**_MINIMAL_TYPE_ENTRY, "name": "Foo"}
        assert validate_type_block(code, te).is_clean


# ---------------------------------------------------------------------------
# validate_type_block — DUPLICATE_FIELD
# ---------------------------------------------------------------------------


class TestValidateTypeBlockDuplicateField:
    def test_duplicate_json_property_name_is_error(self) -> None:
        code = (
            "public class Foo\n"
            "{\n"
            '    [JsonPropertyName("name")]\n'
            "    public string? Name1 { get; init; }\n"
            '    [JsonPropertyName("name")]\n'
            "    public string? Name2 { get; init; }\n"
            "}"
        )
        te = {**_MINIMAL_TYPE_ENTRY, "name": "Foo"}
        result = validate_type_block(code, te)
        assert result.has_errors
        assert any(i.code == "DUPLICATE_FIELD" for i in result.errors)


# ---------------------------------------------------------------------------
# _build_correction_block
# ---------------------------------------------------------------------------


class TestBuildCorrectionBlock:
    def test_single_error_format(self) -> None:
        result = ValidationResult()
        result.add("error", "MISSING_CLASS", "No class found for 'Foo'", "Expected: public class Foo")
        block = _build_correction_block(result)
        assert block.startswith("CORRECTION REQUIRED:")
        assert "[MISSING_CLASS]" in block
        assert "No class found for 'Foo'" in block
        assert "Expected: public class Foo" in block

    def test_multiple_errors_all_present(self) -> None:
        result = ValidationResult()
        result.add("error", "STRUCTURAL", "Unbalanced braces: 3 '{' vs 2 '}'")
        result.add("error", "ARTIFACT", "Template placeholder found")
        block = _build_correction_block(result)
        assert "[STRUCTURAL]" in block
        assert "[ARTIFACT]" in block

    def test_no_detail_omits_detail_line(self) -> None:
        result = ValidationResult()
        result.add("error", "MISSING_CLASS", "No class found", None)
        block = _build_correction_block(result)
        lines = block.splitlines()
        # Header + one error line (no detail line)
        assert len(lines) == 2

    def test_with_detail_adds_detail_line(self) -> None:
        result = ValidationResult()
        result.add("error", "MISSING_CLASS", "No class found", "Expected: public class Foo")
        block = _build_correction_block(result)
        lines = block.splitlines()
        # Header + error line + detail line
        assert len(lines) == 3
        assert lines[2].strip() == "Expected: public class Foo"

    def test_empty_result_returns_header_only(self) -> None:
        result = ValidationResult()
        block = _build_correction_block(result)
        assert block == "CORRECTION REQUIRED:"


# ---------------------------------------------------------------------------
# correction_block prompt injection
# ---------------------------------------------------------------------------


class TestCorrectionBlockPromptInjection:
    def test_correction_block_appears_on_page_1(self) -> None:
        from specbridge.generation.prompt import build_type_page_prompt

        correction = "CORRECTION REQUIRED:\n  - [MISSING_CLASS] No class found"
        prompt = build_type_page_prompt(
            _MINIMAL_PACKET, _MINIMAL_TYPE_ENTRY, [], 1, 1, True,
            correction_block=correction,
        )
        assert "CORRECTION REQUIRED:" in prompt
        assert "[MISSING_CLASS]" in prompt

    def test_correction_block_absent_when_none(self) -> None:
        from specbridge.generation.prompt import build_type_page_prompt

        prompt = build_type_page_prompt(
            _MINIMAL_PACKET, _MINIMAL_TYPE_ENTRY, [], 1, 1, True,
            correction_block=None,
        )
        assert "CORRECTION REQUIRED:" not in prompt

    def test_correction_block_not_injected_on_page_2(self) -> None:
        from specbridge.generation.prompt import build_type_page_prompt

        # Provide 2 fields so page 2 is meaningful
        fields = [
            {"json_name": "a", "csharp_name": "A", "csharp_type": "string",
             "required": False, "nullable": True},
            {"json_name": "b", "csharp_name": "B", "csharp_type": "string",
             "required": False, "nullable": True},
        ]
        te = {**_MINIMAL_TYPE_ENTRY, "fields": fields}
        correction = "CORRECTION REQUIRED:\n  - [MISSING_CLASS] No class found"
        # Page 2 of 2 — correction_block should NOT appear
        prompt = build_type_page_prompt(
            _MINIMAL_PACKET, te, fields[1:], 2, 2, True,
            correction_block=correction,
        )
        assert "CORRECTION REQUIRED:" not in prompt

    def test_correction_appears_before_endpoint_header(self) -> None:
        from specbridge.generation.prompt import build_type_page_prompt

        correction = "CORRECTION REQUIRED:\n  - [STRUCTURAL] Unbalanced braces"
        prompt = build_type_page_prompt(
            _MINIMAL_PACKET, _MINIMAL_TYPE_ENTRY, [], 1, 1, True,
            correction_block=correction,
        )
        correction_pos = prompt.index("CORRECTION REQUIRED:")
        endpoint_pos = prompt.index("ENDPOINT:")
        assert correction_pos < endpoint_pos
