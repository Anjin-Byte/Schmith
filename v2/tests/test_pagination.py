"""Tests for paginated code generation (prompt building, stitching, pipeline helpers)."""

from schmith.generation.llm import (
    _extract_field_block,
    _insert_fields,
    _normalize_class_indentation,
    stitch_type_pages,
)
from schmith.generation.prompt import (
    FIELDS_END_MARKER,
    FIELDS_START_MARKER,
    MAX_ENUM_VALUES_PER_PAGE as _MAX_ENUM_VALUES_PER_PAGE,
    MAX_FIELDS_PER_PAGE as _MAX_FIELDS_PER_PAGE,
    _output_mode,
    _paging_instructions,
    _select_primary_key,
    build_type_page_prompt,
)
from schmith.pipeline import _chunk_enum_values, _chunk_fields


# ---------------------------------------------------------------------------
# _chunk_fields
# ---------------------------------------------------------------------------


class TestChunkFields:
    def test_empty_fields(self) -> None:
        assert _chunk_fields([], 30) == [[]]

    def test_under_limit_returns_single_page(self) -> None:
        fields = [{"json_name": f"f{i}"} for i in range(10)]
        pages = _chunk_fields(fields, 30)
        assert len(pages) == 1
        assert pages[0] == fields

    def test_exactly_limit_returns_single_page(self) -> None:
        fields = [{"json_name": f"f{i}"} for i in range(30)]
        assert len(_chunk_fields(fields, 30)) == 1

    def test_over_limit_splits_into_two_pages(self) -> None:
        fields = [{"json_name": f"f{i}"} for i in range(35)]
        pages = _chunk_fields(fields, 30)
        assert len(pages) == 2
        assert len(pages[0]) == 30
        assert len(pages[1]) == 5

    def test_three_pages(self) -> None:
        fields = [{"json_name": f"f{i}"} for i in range(65)]
        pages = _chunk_fields(fields, 30)
        assert len(pages) == 3
        assert len(pages[0]) == 30
        assert len(pages[1]) == 30
        assert len(pages[2]) == 5

    def test_max_fields_per_page_constant_is_positive(self) -> None:
        assert isinstance(_MAX_FIELDS_PER_PAGE, int) and _MAX_FIELDS_PER_PAGE > 0

    def test_max_enum_values_per_page_constant_is_positive(self) -> None:
        assert isinstance(_MAX_ENUM_VALUES_PER_PAGE, int) and _MAX_ENUM_VALUES_PER_PAGE > 0


# ---------------------------------------------------------------------------
# _output_mode
# ---------------------------------------------------------------------------


class TestOutputMode:
    def test_root_page_1_is_full_class(self) -> None:
        assert _output_mode(is_root=True, page_index=1, is_enum=False) == "full_class"

    def test_nested_page_1_is_class_only(self) -> None:
        assert _output_mode(is_root=False, page_index=1, is_enum=False) == "class_only"

    def test_root_page_2_is_fields_only(self) -> None:
        assert _output_mode(is_root=True, page_index=2, is_enum=False) == "fields_only"

    def test_nested_page_2_is_fields_only(self) -> None:
        assert _output_mode(is_root=False, page_index=2, is_enum=False) == "fields_only"

    def test_enum_overrides_mode(self) -> None:
        assert _output_mode(is_root=True, page_index=1, is_enum=True) == "enum_only"
        assert _output_mode(is_root=False, page_index=1, is_enum=True) == "enum_only"

    def test_enum_page_2_plus_is_enum_values_only(self) -> None:
        assert _output_mode(is_root=True, page_index=2, is_enum=True) == "enum_values_only"
        assert _output_mode(is_root=False, page_index=2, is_enum=True) == "enum_values_only"
        assert _output_mode(is_root=True, page_index=5, is_enum=True) == "enum_values_only"


# ---------------------------------------------------------------------------
# _paging_instructions
# ---------------------------------------------------------------------------


class TestPagingInstructions:
    def test_fields_only_includes_markers(self) -> None:
        lines = _paging_instructions("fields_only", "FooDataObject")
        combined = "\n".join(lines)
        assert FIELDS_START_MARKER in combined
        assert FIELDS_END_MARKER in combined

    def test_class_only_mentions_class_name(self) -> None:
        lines = _paging_instructions("class_only", "BarType")
        assert any("BarType" in line for line in lines)

    def test_full_class_is_paging_note(self) -> None:
        lines = _paging_instructions("full_class", "RootType")
        assert lines[0] == "PAGING NOTE:"

    def test_enum_only_has_output_mode(self) -> None:
        lines = _paging_instructions("enum_only", "StatusEnum")
        assert lines[0] == "OUTPUT MODE: enum_only"
        assert any("StatusEnum" in line for line in lines)

    def test_enum_values_only_has_markers(self) -> None:
        lines = _paging_instructions("enum_values_only", "StatusEnum")
        combined = "\n".join(lines)
        assert FIELDS_START_MARKER in combined
        assert FIELDS_END_MARKER in combined

    def test_enum_values_only_first_line(self) -> None:
        lines = _paging_instructions("enum_values_only", "StatusEnum")
        assert lines[0] == "OUTPUT MODE: enum_values_only"


# ---------------------------------------------------------------------------
# _chunk_enum_values
# ---------------------------------------------------------------------------


class TestChunkEnumValues:
    def test_empty_returns_single_page(self) -> None:
        assert _chunk_enum_values([], None, 30) == [([], None)]

    def test_under_limit_returns_single_page(self) -> None:
        values = ["a", "b", "c"]
        result = _chunk_enum_values(values, None, 30)
        assert len(result) == 1
        assert result[0] == (values, None)

    def test_names_sliced_in_parallel(self) -> None:
        values = ["a", "b", "c", "d"]
        names = ["A", "B", "C", "D"]
        pages = _chunk_enum_values(values, names, 2)
        assert len(pages) == 2
        assert pages[0] == (["a", "b"], ["A", "B"])
        assert pages[1] == (["c", "d"], ["C", "D"])

    def test_names_none_propagated(self) -> None:
        values = ["a", "b", "c", "d"]
        pages = _chunk_enum_values(values, None, 2)
        assert all(n is None for _, n in pages)

    def test_three_pages(self) -> None:
        values = list(range(65))
        pages = _chunk_enum_values(values, None, 30)
        assert len(pages) == 3
        assert len(pages[0][0]) == 30
        assert len(pages[1][0]) == 30
        assert len(pages[2][0]) == 5


# ---------------------------------------------------------------------------
# _extract_field_block
# ---------------------------------------------------------------------------


class TestExtractFieldBlock:
    def test_extracts_between_markers(self) -> None:
        code = (
            f"some preamble\n"
            f"{FIELDS_START_MARKER}\n"
            f"    public string? Name {{ get; init; }}\n"
            f"{FIELDS_END_MARKER}\n"
            f"trailing"
        )
        result = _extract_field_block(code)
        assert "public string? Name" in result
        assert FIELDS_START_MARKER not in result
        assert FIELDS_END_MARKER not in result

    def test_falls_back_to_full_code_without_markers(self) -> None:
        code = "    public string? Id { get; init; }"
        assert _extract_field_block(code) == code.strip()


# ---------------------------------------------------------------------------
# _insert_fields
# ---------------------------------------------------------------------------


class TestInsertFields:
    def test_inserts_before_first_closing_brace(self) -> None:
        base = "public class Foo\n{\n    public string? Id { get; init; }\n}\n"
        extra = "    public string? Name { get; init; }"
        result = _insert_fields(base, extra)
        assert result.index("Id") < result.index("Name")
        # Closing brace must come after the inserted field
        last_brace = result.rfind("}")
        name_pos = result.index("Name")
        assert name_pos < last_brace

    def test_fallback_when_no_brace(self) -> None:
        base = "// no class here"
        extra = "    public string? X { get; init; }"
        result = _insert_fields(base, extra)
        assert "X" in result


# ---------------------------------------------------------------------------
# _normalize_class_indentation
# ---------------------------------------------------------------------------


class TestNormalizeClassIndentation:
    def test_indents_unindented_public_member(self) -> None:
        code = "public class Foo\n{\npublic string? X { get; init; }\n}"
        result = _normalize_class_indentation(code)
        lines = result.splitlines()
        member = next(l for l in lines if "public string?" in l)
        assert member.startswith("    ")

    def test_preserves_already_indented_member(self) -> None:
        code = "public class Foo\n{\n    public string? X { get; init; }\n}"
        result = _normalize_class_indentation(code)
        lines = result.splitlines()
        member = next(l for l in lines if "public string?" in l)
        assert member.startswith("    ")


# ---------------------------------------------------------------------------
# stitch_type_pages
# ---------------------------------------------------------------------------


class TestStitchTypePages:
    def test_single_page_returns_as_is(self) -> None:
        code = "public class Foo\n{\n    public string? Id { get; init; }\n}"
        result = stitch_type_pages([code])
        assert "public class Foo" in result
        assert "public string? Id" in result

    def test_empty_list_returns_empty(self) -> None:
        assert stitch_type_pages([]) == ""

    def test_two_pages_stitched(self) -> None:
        page1 = "public class Foo\n{\n    public string? Id { get; init; }\n}\n"
        page2 = (
            f"{FIELDS_START_MARKER}\n"
            "    public string? Name { get; init; }\n"
            f"{FIELDS_END_MARKER}"
        )
        result = stitch_type_pages([page1, page2])
        assert "public string? Id" in result
        assert "public string? Name" in result
        # Id should appear before Name
        assert result.index("Id") < result.index("Name")

    def test_three_pages_all_fields_present(self) -> None:
        page1 = "public class Big\n{\n    public string? A { get; init; }\n}\n"

        def make_page(prop: str) -> str:
            return (
                f"{FIELDS_START_MARKER}\n"
                f"    public string? {prop} {{ get; init; }}\n"
                f"{FIELDS_END_MARKER}"
            )

        result = stitch_type_pages([page1, make_page("B"), make_page("C")])
        assert "public string? A" in result
        assert "public string? B" in result
        assert "public string? C" in result


# ---------------------------------------------------------------------------
# _select_primary_key
# ---------------------------------------------------------------------------


def _field(json_name: str, csharp_type: str = "string", required: bool = False, nullable: bool = False) -> dict:
    return {
        "json_name": json_name,
        "csharp_name": "".join(w.capitalize() for w in json_name.split("_")),
        "csharp_type": csharp_type,
        "required": required,
        "nullable": nullable,
    }


class TestSelectPrimaryKey:
    def test_returns_none_for_empty_fields(self) -> None:
        assert _select_primary_key([]) is None

    def test_exact_id_wins(self) -> None:
        fields = [_field("name"), _field("id"), _field("customer_id")]
        result = _select_primary_key(fields)
        assert result is not None
        assert result["json_name"] == "id"

    def test_ends_with_id_beats_contains_id(self) -> None:
        # "customer_id" ends with "_id"; "additional_info" only contains "id"
        fields = [_field("additional_info"), _field("customer_id")]
        result = _select_primary_key(fields)
        assert result is not None
        assert result["json_name"] == "customer_id"

    def test_ends_with_key_is_preferred(self) -> None:
        fields = [_field("description"), _field("api_key")]
        result = _select_primary_key(fields)
        assert result is not None
        assert result["json_name"] == "api_key"

    def test_required_nonnullable_preferred_over_nullable(self) -> None:
        # Neither has "id"/"key" — prefer required+non-nullable
        fields = [
            _field("alpha", required=False, nullable=True),
            _field("beta", required=True, nullable=False),
        ]
        result = _select_primary_key(fields)
        assert result is not None
        assert result["json_name"] == "beta"

    def test_string_type_preferred_over_complex(self) -> None:
        fields = [
            _field("ref", csharp_type="ComplexType", required=True, nullable=False),
            _field("code", csharp_type="string", required=True, nullable=False),
        ]
        result = _select_primary_key(fields)
        assert result is not None
        assert result["json_name"] == "code"

    def test_single_field_always_returned(self) -> None:
        f = _field("only_field")
        result = _select_primary_key([f])
        assert result is f

    def test_id_beats_required_non_id(self) -> None:
        # "id" should win even if the other field is required+non-nullable
        fields = [
            _field("id", required=False, nullable=True),
            _field("code", required=True, nullable=False),
        ]
        result = _select_primary_key(fields)
        assert result is not None
        assert result["json_name"] == "id"


# ---------------------------------------------------------------------------
# build_type_page_prompt
# ---------------------------------------------------------------------------


class TestBuildTypePagePrompt:
    def setup_method(self) -> None:
        self.packet = {
            "metadata": {"method": "GET", "path": "/customers", "data_object_name": "CustomerDataObject"},
            "generation": {"instructions": "Be a C# expert.", "example_code": "public class Example {}"},
            "root": {
                "name": "CustomerDataObject",
                "schema_id": "schema:components/Customer",
                "description": "A customer",
                "kind": "object",
                "fields": [],
                "enum_values": None,
            },
            "nested_types": [
                {"name": "CustomerAddressDataObject", "schema_id": "schema:components/Address",
                 "description": "", "kind": "object", "fields": [], "enum_values": None}
            ],
        }
        self.type_entry = self.packet["root"]

    def test_single_page_no_paging_section(self) -> None:
        fields = [{"json_name": "id", "csharp_type": "string", "nullable": False, "required": True}]
        prompt = build_type_page_prompt(self.packet, self.type_entry, fields, 1, 1, is_root=True)
        assert "PAGING:" not in prompt
        assert "CustomerDataObject" in prompt

    def test_multi_page_includes_paging_section(self) -> None:
        fields = [{"json_name": "id", "csharp_type": "string", "nullable": False, "required": True}]
        prompt = build_type_page_prompt(self.packet, self.type_entry, fields, 2, 3, is_root=True)
        assert "PAGING:" in prompt
        assert "Page: 2 of 3" in prompt

    def test_root_page1_includes_nested_types_hint(self) -> None:
        prompt = build_type_page_prompt(self.packet, self.type_entry, [], 1, 1, is_root=True)
        assert "CustomerAddressDataObject" in prompt
        assert "Do NOT generate them here" in prompt

    def test_nested_page1_no_nested_types_hint(self) -> None:
        nested_entry = self.packet["nested_types"][0]
        prompt = build_type_page_prompt(self.packet, nested_entry, [], 1, 1, is_root=False)
        # Should not include the nested types hint when generating a nested class
        assert "Do NOT generate them here" not in prompt

    def test_fields_only_mode_has_marker_instruction(self) -> None:
        fields = [{"json_name": "id", "csharp_type": "string", "nullable": False}]
        prompt = build_type_page_prompt(self.packet, self.type_entry, fields, 2, 2, is_root=True)
        assert FIELDS_START_MARKER in prompt
        assert FIELDS_END_MARKER in prompt

    def test_enum_page1_shows_all_values_when_no_values_page(self) -> None:
        enum_entry = {
            "name": "StatusEnum",
            "schema_id": "schema:components/Status",
            "description": "Status of the resource",
            "kind": "string",
            "fields": [],
            "enum_values": ["active", "inactive", "pending"],
            "enum_names": ["Active", "Inactive", "Pending"],
        }
        prompt = build_type_page_prompt(self.packet, enum_entry, [], 1, 1, is_root=False)
        assert "active" in prompt
        assert "inactive" in prompt
        assert "pending" in prompt
        assert "PAGING:" not in prompt

    def test_enum_page1_multi_shows_trailing_comma_note(self) -> None:
        enum_entry = {
            "name": "StatusEnum",
            "schema_id": "schema:components/Status",
            "description": "",
            "kind": "string",
            "fields": [],
            "enum_values": ["active", "inactive"],
            "enum_names": None,
        }
        values_page = ["active"]
        prompt = build_type_page_prompt(
            self.packet, enum_entry, [], 1, 2, is_root=False,
            values_page=values_page,
        )
        assert "trailing comma" in prompt.lower()

    def test_enum_page2_shows_values_page_subset(self) -> None:
        enum_entry = {
            "name": "StatusEnum",
            "schema_id": "schema:components/Status",
            "description": "",
            "kind": "string",
            "fields": [],
            "enum_values": ["active", "inactive", "pending", "archived"],
            "enum_names": None,
        }
        values_page = ["pending", "archived"]
        prompt = build_type_page_prompt(
            self.packet, enum_entry, [], 2, 2, is_root=False,
            values_page=values_page,
        )
        assert "pending" in prompt
        assert "archived" in prompt
        assert FIELDS_START_MARKER in prompt
        assert FIELDS_END_MARKER in prompt
        assert "Total values: 4" in prompt

    def test_enum_paging_section_reports_values_not_fields(self) -> None:
        enum_entry = {
            "name": "BigEnum",
            "schema_id": "schema:components/BigEnum",
            "description": "",
            "kind": "string",
            "fields": [],
            "enum_values": list(range(60)),
            "enum_names": None,
        }
        values_page = list(range(30))
        prompt = build_type_page_prompt(
            self.packet, enum_entry, [], 1, 2, is_root=False,
            values_page=values_page,
        )
        assert "Values in this page:" in prompt
        assert "Total values:" in prompt
        assert "Fields in this page:" not in prompt

    def test_root_page1_includes_primary_key_when_set(self) -> None:
        type_entry = {
            **self.type_entry,
            "primary_key_json_name": "id",
            "primary_key_csharp_name": "Id",
        }
        prompt = build_type_page_prompt(self.packet, type_entry, [], 1, 1, is_root=True)
        assert "PRIMARY KEY: id [→ Id]" in prompt

    def test_root_page1_no_primary_key_when_not_set(self) -> None:
        prompt = build_type_page_prompt(self.packet, self.type_entry, [], 1, 1, is_root=True)
        assert "PRIMARY KEY:" not in prompt

    def test_nested_page1_no_primary_key_even_when_set(self) -> None:
        type_entry = {
            **self.packet["nested_types"][0],
            "primary_key_json_name": "id",
            "primary_key_csharp_name": "Id",
        }
        prompt = build_type_page_prompt(self.packet, type_entry, [], 1, 1, is_root=False)
        assert "PRIMARY KEY:" not in prompt

    def test_root_page2_no_primary_key_even_when_set(self) -> None:
        type_entry = {
            **self.type_entry,
            "primary_key_json_name": "id",
            "primary_key_csharp_name": "Id",
        }
        prompt = build_type_page_prompt(self.packet, type_entry, [], 2, 3, is_root=True)
        assert "PRIMARY KEY:" not in prompt
