"""Tests for schmith/validation.py — deterministic post-generation checks."""

import pytest

from schmith.validation import (
    ValidationIssue,
    ValidationResult,
    _check_artifacts,
    _check_class_declarations,
    _check_duplicate_json_properties,
    _check_json_property_coverage,
    _check_phantom_fields,
    _check_structural,
    _collect_all_json_names,
    print_validation_report,
    validate_generated_code,
)


# ---------------------------------------------------------------------------
# Fixtures / helpers
# ---------------------------------------------------------------------------


def _make_field(json_name: str) -> dict:
    return {
        "json_name": json_name,
        "csharp_name": json_name.replace("_", ""),
        "csharp_type": "string",
        "required": False,
        "nullable": False,
        "deprecated": False,
        "read_only": False,
        "write_only": False,
        "type_unresolved": False,
    }


def _make_nested(name: str, fields: list | None = None) -> dict:
    return {
        "name": name,
        "schema_id": "",
        "description": "",
        "kind": "object",
        "fields": fields or [],
        "enum_values": None,
        "enum_names": None,
        "is_inline": False,
    }


def _make_packet(
    root_name: str = "CustomerDataObject",
    root_fields: list | None = None,
    root_enum_values: list | None = None,
    nested: list | None = None,
) -> dict:
    root: dict = {
        "name": root_name,
        "schema_id": "schema:components/Customer",
        "description": "",
        "kind": "object" if not root_enum_values else "enum",
        "fields": root_fields or [],
        "enum_values": root_enum_values,
        "enum_names": None,
        "is_inline": False,
    }
    return {
        "metadata": {
            "method": "GET",
            "path": "/customers",
            "data_object_name": root_name,
            "response_description": "",
        },
        "root": root,
        "nested_types": nested or [],
        "max_fields_per_page": 6,
        "generation": {"instructions": "...", "example_code": "..."},
    }


# A clean, minimal generated C# class with two fields matching the schema.
_CLEAN_CODE = """\
public class CustomerDataObject
{
    [JsonPropertyName("id")]
    [Description("Customer ID")]
    public required string Id { get; init; }

    [JsonPropertyName("name")]
    public string? Name { get; init; }
}"""


# ---------------------------------------------------------------------------
# ValidationResult
# ---------------------------------------------------------------------------


class TestValidationResult:
    def test_is_clean_when_empty(self) -> None:
        r = ValidationResult()
        assert r.is_clean

    def test_has_errors_false_when_only_warnings(self) -> None:
        r = ValidationResult()
        r.add("warning", "W1", "A warning")
        assert not r.has_errors

    def test_has_errors_true_when_errors_present(self) -> None:
        r = ValidationResult()
        r.add("error", "E1", "An error")
        assert r.has_errors

    def test_errors_property_filters_correctly(self) -> None:
        r = ValidationResult()
        r.add("error", "E1", "Error")
        r.add("warning", "W1", "Warning")
        assert len(r.errors) == 1
        assert r.errors[0].code == "E1"

    def test_warnings_property_filters_correctly(self) -> None:
        r = ValidationResult()
        r.add("error", "E1", "Error")
        r.add("warning", "W1", "Warning")
        assert len(r.warnings) == 1
        assert r.warnings[0].code == "W1"

    def test_not_clean_when_warning(self) -> None:
        r = ValidationResult()
        r.add("warning", "W1", "Warning")
        assert not r.is_clean

    def test_add_stores_detail(self) -> None:
        r = ValidationResult()
        r.add("error", "E1", "msg", detail="extra info")
        assert r.issues[0].detail == "extra info"


# ---------------------------------------------------------------------------
# _check_structural
# ---------------------------------------------------------------------------


class TestCheckStructural:
    def test_balanced_braces_passes(self) -> None:
        r = ValidationResult()
        _check_structural("public class A { string x; }", r)
        assert r.is_clean

    def test_empty_code_passes(self) -> None:
        r = ValidationResult()
        _check_structural("", r)
        assert r.is_clean

    def test_missing_close_brace_is_error(self) -> None:
        r = ValidationResult()
        _check_structural("public class A {", r)
        assert r.has_errors
        assert r.errors[0].code == "STRUCTURAL"

    def test_extra_close_brace_is_error(self) -> None:
        r = ValidationResult()
        _check_structural("public class A { } }", r)
        assert r.has_errors
        assert r.errors[0].code == "STRUCTURAL"

    def test_detail_contains_open_close_counts(self) -> None:
        r = ValidationResult()
        _check_structural("{ {", r)
        assert r.errors[0].detail is not None
        assert "open=2" in r.errors[0].detail
        assert "close=0" in r.errors[0].detail

    def test_nested_balanced_braces_passes(self) -> None:
        r = ValidationResult()
        _check_structural("class A { class B { } }", r)
        assert r.is_clean


# ---------------------------------------------------------------------------
# _check_artifacts
# ---------------------------------------------------------------------------


class TestCheckArtifacts:
    def test_clean_code_passes(self) -> None:
        r = ValidationResult()
        _check_artifacts(_CLEAN_CODE, r)
        assert r.is_clean

    def test_template_placeholder_is_error(self) -> None:
        r = ValidationResult()
        _check_artifacts("public string %{field_name} { get; init; }", r)
        errors = [i for i in r.errors if i.code == "ARTIFACT"]
        assert errors

    def test_begin_fields_marker_is_error(self) -> None:
        r = ValidationResult()
        _check_artifacts("// BEGIN_FIELDS\n    public string X { get; init; }", r)
        assert r.has_errors
        assert any(i.code == "ARTIFACT" for i in r.errors)

    def test_end_fields_marker_is_error(self) -> None:
        r = ValidationResult()
        _check_artifacts("    public string X { get; init; }\n// END_FIELDS", r)
        assert r.has_errors

    def test_raw_schema_id_components_is_warning(self) -> None:
        r = ValidationResult()
        _check_artifacts("// see schema:components/Customer", r)
        warnings = [i for i in r.warnings if i.code == "ARTIFACT"]
        assert warnings

    def test_raw_schema_id_anon_is_warning(self) -> None:
        r = ValidationResult()
        _check_artifacts("// type schema:anon/abc123", r)
        assert any(i.severity == "warning" and i.code == "ARTIFACT" for i in r.issues)

    def test_multiple_artifact_types_all_recorded(self) -> None:
        r = ValidationResult()
        _check_artifacts("// BEGIN_FIELDS\n%{x}", r)
        codes = [i.code for i in r.issues]
        assert codes.count("ARTIFACT") >= 2

    def test_detail_reports_occurrence_count(self) -> None:
        r = ValidationResult()
        _check_artifacts("%{a} %{b} %{c}", r)
        assert r.errors[0].detail is not None
        assert "3" in r.errors[0].detail

    def test_template_in_json_property_name_is_not_flagged(self) -> None:
        # Procore and similar APIs use %{...} as part of dynamic field names,
        # e.g. [JsonPropertyName("custom_field_%{definition_id}")].
        # These are legitimate spec field names, not LLM artifacts.
        r = ValidationResult()
        code = (
            'public class CustomFields\n'
            '{\n'
            '    [JsonPropertyName("custom_field_%{string_definition_id}")]\n'
            '    public CustomFieldString? CustomField { get; init; }\n'
            '}'
        )
        _check_artifacts(code, r)
        assert r.is_clean

    def test_template_outside_json_property_name_is_still_flagged(self) -> None:
        # %{...} that appears outside a [JsonPropertyName("...")] string IS an artifact.
        r = ValidationResult()
        _check_artifacts('public %{type_name} %{prop_name} { get; init; }', r)
        assert r.has_errors


# ---------------------------------------------------------------------------
# _check_class_declarations
# ---------------------------------------------------------------------------


class TestCheckClassDeclarations:
    def test_matching_class_passes(self) -> None:
        packet = _make_packet("CustomerDataObject")
        r = ValidationResult()
        _check_class_declarations(_CLEAN_CODE, packet, r)
        assert r.is_clean

    def test_missing_root_class_is_error(self) -> None:
        packet = _make_packet("MissingClass")
        r = ValidationResult()
        _check_class_declarations(_CLEAN_CODE, packet, r)
        errors = [i for i in r.errors if i.code == "MISSING_CLASS"]
        assert errors
        assert "MissingClass" in errors[0].message

    def test_enum_declaration_passes(self) -> None:
        code = "public enum StatusEnum { Active, Inactive }"
        packet = _make_packet("StatusEnum", root_enum_values=["active", "inactive"])
        r = ValidationResult()
        _check_class_declarations(code, packet, r)
        assert r.is_clean

    def test_nested_type_missing_is_error(self) -> None:
        nested = _make_nested("AddressDataObject")
        packet = _make_packet("CustomerDataObject", nested=[nested])
        r = ValidationResult()
        _check_class_declarations(_CLEAN_CODE, packet, r)  # Only has CustomerDataObject
        errors = [i for i in r.errors if i.code == "MISSING_CLASS"]
        assert any("AddressDataObject" in e.message for e in errors)

    def test_sealed_class_is_detected(self) -> None:
        code = "public sealed class MyClass { }"
        packet = _make_packet("MyClass")
        r = ValidationResult()
        _check_class_declarations(code, packet, r)
        assert r.is_clean

    def test_partial_class_is_detected(self) -> None:
        code = "public partial class MyClass { }"
        packet = _make_packet("MyClass")
        r = ValidationResult()
        _check_class_declarations(code, packet, r)
        assert r.is_clean

    def test_record_is_detected(self) -> None:
        code = "public record MyRecord { }"
        packet = _make_packet("MyRecord")
        r = ValidationResult()
        _check_class_declarations(code, packet, r)
        assert r.is_clean

    def test_all_types_checked(self) -> None:
        nested_a = _make_nested("TypeA")
        nested_b = _make_nested("TypeB")
        packet = _make_packet("Root", nested=[nested_a, nested_b])
        code = "public class Root { } public class TypeA { }"  # TypeB missing
        r = ValidationResult()
        _check_class_declarations(code, packet, r)
        errors = [i for i in r.errors if i.code == "MISSING_CLASS"]
        assert any("TypeB" in e.message for e in errors)
        assert not any("TypeA" in e.message for e in errors)

    def test_root_data_object_suffixed_name_accepted(self) -> None:
        # The LLM often generates "TimesheetDataObject" when the schema name is
        # "Timesheet". The check must accept the DataObject-suffixed form for root.
        code = "public class TimesheetDataObject { }"
        packet = _make_packet("Timesheet")
        r = ValidationResult()
        _check_class_declarations(code, packet, r)
        assert r.is_clean

    def test_nested_type_data_object_suffix_not_accepted(self) -> None:
        # Only the root type gets the DataObject suffix exemption.
        # A nested type named "Address" must appear as exactly "Address".
        nested = _make_nested("Address")
        packet = _make_packet("Customer", nested=[nested])
        code = "public class Customer { } public class AddressDataObject { }"
        r = ValidationResult()
        _check_class_declarations(code, packet, r)
        errors = [i for i in r.errors if i.code == "MISSING_CLASS"]
        assert any("Address" in e.message for e in errors)


# ---------------------------------------------------------------------------
# _check_json_property_coverage
# ---------------------------------------------------------------------------


class TestCheckJsonPropertyCoverage:
    def test_all_fields_present_passes(self) -> None:
        fields = [_make_field("id"), _make_field("name")]
        packet = _make_packet("CustomerDataObject", root_fields=fields)
        r = ValidationResult()
        _check_json_property_coverage(_CLEAN_CODE, packet, r)
        assert r.is_clean

    def test_missing_field_is_warning(self) -> None:
        fields = [_make_field("id"), _make_field("name"), _make_field("email")]
        packet = _make_packet("CustomerDataObject", root_fields=fields)
        r = ValidationResult()
        _check_json_property_coverage(_CLEAN_CODE, packet, r)
        warnings = [i for i in r.warnings if i.code == "MISSING_FIELD"]
        assert warnings
        assert any("email" in w.message for w in warnings)

    def test_enum_type_skipped(self) -> None:
        packet = _make_packet("StatusEnum", root_enum_values=["active", "inactive"])
        r = ValidationResult()
        _check_json_property_coverage("public enum StatusEnum { Active, Inactive }", packet, r)
        assert r.is_clean

    def test_field_with_empty_json_name_skipped(self) -> None:
        bad_field: dict = {"json_name": "", "csharp_type": "string"}
        packet = _make_packet("CustomerDataObject", root_fields=[bad_field])
        r = ValidationResult()
        _check_json_property_coverage(_CLEAN_CODE, packet, r)
        # No issues about empty json_name; other issues don't matter here
        missing = [i for i in r.issues if i.code == "MISSING_FIELD" and "''" in i.message]
        assert not missing

    def test_nested_type_fields_checked(self) -> None:
        nested = _make_nested("AddressDataObject", fields=[_make_field("street")])
        packet = _make_packet(
            "CustomerDataObject",
            root_fields=[_make_field("id")],
            nested=[nested],
        )
        # Code only has the root field; "street" from nested type is missing
        code = 'public class CustomerDataObject { [JsonPropertyName("id")] public string Id; } public class AddressDataObject { }'
        r = ValidationResult()
        _check_json_property_coverage(code, packet, r)
        warnings = [i for i in r.warnings if i.code == "MISSING_FIELD"]
        assert any("street" in w.message for w in warnings)


# ---------------------------------------------------------------------------
# _collect_all_json_names
# ---------------------------------------------------------------------------


class TestCollectAllJsonNames:
    def test_collects_root_fields(self) -> None:
        fields = [_make_field("id"), _make_field("name")]
        packet = _make_packet("CustomerDataObject", root_fields=fields)
        assert _collect_all_json_names(packet) == {"id", "name"}

    def test_collects_nested_fields(self) -> None:
        nested = _make_nested("AddressDataObject", fields=[_make_field("street"), _make_field("city")])
        packet = _make_packet("CustomerDataObject", root_fields=[_make_field("id")], nested=[nested])
        assert _collect_all_json_names(packet) == {"id", "street", "city"}

    def test_empty_packet_returns_empty_set(self) -> None:
        packet = _make_packet("CustomerDataObject")
        assert _collect_all_json_names(packet) == set()

    def test_skips_empty_json_names(self) -> None:
        bad_field: dict = {"json_name": "", "csharp_type": "string"}
        packet = _make_packet("CustomerDataObject", root_fields=[bad_field])
        assert _collect_all_json_names(packet) == set()


# ---------------------------------------------------------------------------
# _check_phantom_fields
# ---------------------------------------------------------------------------


class TestCheckPhantomFields:
    def test_no_phantom_fields_passes(self) -> None:
        fields = [_make_field("id"), _make_field("name")]
        packet = _make_packet("CustomerDataObject", root_fields=fields)
        r = ValidationResult()
        _check_phantom_fields(_CLEAN_CODE, packet, r)
        assert r.is_clean

    def test_phantom_field_is_warning(self) -> None:
        fields = [_make_field("id")]  # "name" not in schema
        packet = _make_packet("CustomerDataObject", root_fields=fields)
        r = ValidationResult()
        _check_phantom_fields(_CLEAN_CODE, packet, r)
        warnings = [i for i in r.warnings if i.code == "PHANTOM_FIELD"]
        assert warnings
        assert any("name" in w.message for w in warnings)

    def test_no_json_properties_in_code_passes(self) -> None:
        code = "public class MyClass { public string Foo { get; init; } }"
        packet = _make_packet("MyClass")
        r = ValidationResult()
        _check_phantom_fields(code, packet, r)
        assert r.is_clean

    def test_multiple_phantom_fields_all_reported(self) -> None:
        code = (
            '[JsonPropertyName("ghost1")] public string G1;\n'
            '[JsonPropertyName("ghost2")] public string G2;'
        )
        packet = _make_packet("MyClass")  # no fields in schema
        r = ValidationResult()
        _check_phantom_fields(code, packet, r)
        phantoms = [i for i in r.warnings if i.code == "PHANTOM_FIELD"]
        assert len(phantoms) == 2


# ---------------------------------------------------------------------------
# _check_duplicate_json_properties
# ---------------------------------------------------------------------------


class TestCheckDuplicateJsonProperties:
    def test_no_duplicates_passes(self) -> None:
        r = ValidationResult()
        _check_duplicate_json_properties(_CLEAN_CODE, r)
        assert r.is_clean

    def test_duplicate_is_error(self) -> None:
        code = (
            'public class X {\n'
            '    [JsonPropertyName("id")]\n'
            '    public string Id1 { get; init; }\n'
            '    [JsonPropertyName("id")]\n'
            '    public string Id2 { get; init; }\n'
            '}'
        )
        r = ValidationResult()
        _check_duplicate_json_properties(code, r)
        errors = [i for i in r.errors if i.code == "DUPLICATE_FIELD"]
        assert errors
        assert any("id" in e.message for e in errors)

    def test_triplicate_reports_count(self) -> None:
        code = (
            '[JsonPropertyName("x")] public string A;\n'
            '[JsonPropertyName("x")] public string B;\n'
            '[JsonPropertyName("x")] public string C;'
        )
        r = ValidationResult()
        _check_duplicate_json_properties(code, r)
        errors = [i for i in r.errors if i.code == "DUPLICATE_FIELD"]
        assert errors
        assert "3" in errors[0].message

    def test_unique_values_not_flagged(self) -> None:
        code = (
            '[JsonPropertyName("id")]\n'
            '[JsonPropertyName("name")]\n'
            '[JsonPropertyName("email")]'
        )
        r = ValidationResult()
        _check_duplicate_json_properties(code, r)
        assert r.is_clean

    def test_same_field_in_different_classes_not_flagged(self) -> None:
        # id, name, created_at appear in many classes in a real generated file.
        # They are valid because they're in separate class scopes.
        code = (
            'public class ClassA {\n'
            '    [JsonPropertyName("id")] public int Id;\n'
            '    [JsonPropertyName("name")] public string Name;\n'
            '}\n\n'
            'public class ClassB {\n'
            '    [JsonPropertyName("id")] public int Id;\n'
            '    [JsonPropertyName("name")] public string Name;\n'
            '}\n'
        )
        r = ValidationResult()
        _check_duplicate_json_properties(code, r)
        assert r.is_clean

    def test_duplicate_within_class_still_flagged(self) -> None:
        # Two properties with the same JsonPropertyName in one class IS an error.
        code = (
            'public class ClassA {\n'
            '    [JsonPropertyName("id")] public int Id1;\n'
            '    [JsonPropertyName("id")] public int Id2;\n'
            '}\n\n'
            'public class ClassB {\n'
            '    [JsonPropertyName("id")] public int Id;\n'
            '}\n'
        )
        r = ValidationResult()
        _check_duplicate_json_properties(code, r)
        errors = [i for i in r.errors if i.code == "DUPLICATE_FIELD"]
        assert len(errors) == 1
        assert "ClassA" in errors[0].message

    def test_error_message_includes_class_name(self) -> None:
        code = (
            'public class MyClass {\n'
            '    [JsonPropertyName("x")] public string A;\n'
            '    [JsonPropertyName("x")] public string B;\n'
            '}\n'
        )
        r = ValidationResult()
        _check_duplicate_json_properties(code, r)
        assert r.has_errors
        assert "MyClass" in r.errors[0].message


# ---------------------------------------------------------------------------
# validate_generated_code (integration)
# ---------------------------------------------------------------------------


class TestValidateGeneratedCode:
    def setup_method(self) -> None:
        self.fields = [_make_field("id"), _make_field("name")]
        self.packet = _make_packet("CustomerDataObject", root_fields=self.fields)

    def test_clean_code_is_clean(self) -> None:
        result = validate_generated_code(_CLEAN_CODE, self.packet)
        assert result.is_clean

    def test_unbalanced_braces_detected(self) -> None:
        result = validate_generated_code(_CLEAN_CODE.replace("}", ""), self.packet)
        assert result.has_errors
        assert any(i.code == "STRUCTURAL" for i in result.errors)

    def test_artifact_detected(self) -> None:
        bad_code = _CLEAN_CODE + "\n// BEGIN_FIELDS\n"
        result = validate_generated_code(bad_code, self.packet)
        assert result.has_errors
        assert any(i.code == "ARTIFACT" for i in result.errors)

    def test_missing_class_detected(self) -> None:
        packet = _make_packet("OtherClass")
        result = validate_generated_code(_CLEAN_CODE, packet)
        assert result.has_errors
        assert any(i.code == "MISSING_CLASS" for i in result.errors)

    def test_missing_field_detected(self) -> None:
        fields = [_make_field("id"), _make_field("name"), _make_field("email")]
        packet = _make_packet("CustomerDataObject", root_fields=fields)
        result = validate_generated_code(_CLEAN_CODE, packet)
        warnings = [i for i in result.warnings if i.code == "MISSING_FIELD"]
        assert any("email" in w.message for w in warnings)

    def test_phantom_field_detected(self) -> None:
        fields = [_make_field("id")]  # "name" will appear in code but not schema
        packet = _make_packet("CustomerDataObject", root_fields=fields)
        result = validate_generated_code(_CLEAN_CODE, packet)
        warnings = [i for i in result.warnings if i.code == "PHANTOM_FIELD"]
        assert any("name" in w.message for w in warnings)

    def test_duplicate_field_detected(self) -> None:
        dup_code = _CLEAN_CODE + '\n    [JsonPropertyName("id")]\n    public string Id2 { get; init; }\n}'
        result = validate_generated_code(dup_code, self.packet)
        assert any(i.code == "DUPLICATE_FIELD" for i in result.errors)

    def test_all_checks_run_on_bad_input(self) -> None:
        packet = _make_packet("MissingClass", root_fields=[_make_field("x")])
        bad_code = "// BEGIN_FIELDS\npublic class Other {"
        result = validate_generated_code(bad_code, packet)
        codes = {i.code for i in result.issues}
        assert "STRUCTURAL" in codes
        assert "ARTIFACT" in codes
        assert "MISSING_CLASS" in codes


# ---------------------------------------------------------------------------
# print_validation_report
# ---------------------------------------------------------------------------


class _MockConsole:
    """Minimal console mock that captures print calls."""

    def __init__(self) -> None:
        self.lines: list[str] = []

    def print(self, msg: str = "", **kwargs: object) -> None:
        self.lines.append(str(msg))

    @property
    def output(self) -> str:
        return "\n".join(self.lines)


class TestPrintValidationReport:
    def test_clean_result_prints_pass_message(self) -> None:
        console = _MockConsole()
        print_validation_report(ValidationResult(), console)
        assert any("passed" in line.lower() or "✓" in line for line in console.lines)

    def test_error_appears_in_output(self) -> None:
        result = ValidationResult()
        result.add("error", "STRUCTURAL", "Unbalanced braces")
        console = _MockConsole()
        print_validation_report(result, console)
        assert "STRUCTURAL" in console.output

    def test_warning_appears_in_output(self) -> None:
        result = ValidationResult()
        result.add("warning", "PHANTOM_FIELD", "Ghost field 'xyz'")
        console = _MockConsole()
        print_validation_report(result, console)
        assert "PHANTOM_FIELD" in console.output

    def test_detail_appears_in_output(self) -> None:
        result = ValidationResult()
        result.add("error", "E1", "Some error", detail="extra detail here")
        console = _MockConsole()
        print_validation_report(result, console)
        assert "extra detail here" in console.output

    def test_summary_line_shows_counts(self) -> None:
        result = ValidationResult()
        result.add("error", "E1", "Error 1")
        result.add("error", "E2", "Error 2")
        result.add("warning", "W1", "Warning 1")
        console = _MockConsole()
        print_validation_report(result, console)
        assert "2" in console.output  # 2 errors

    def test_clean_result_does_not_print_issues(self) -> None:
        console = _MockConsole()
        print_validation_report(ValidationResult(), console)
        assert "error" not in console.output.lower().replace("passed", "")
