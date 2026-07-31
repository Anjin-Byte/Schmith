"""Tests for specbridge.assembly — stitch_type_pages and assemble_from_pages."""

from datetime import datetime, timezone

import pytest

from specbridge.assembly import assemble_from_pages, stitch_type_pages
from specbridge.generation.pages import PageEntry


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

_DT = datetime(2026, 1, 1, tzinfo=timezone.utc)


def _entry(
    type_name: str,
    page: int,
    total_pages: int,
    output: str,
    *,
    is_root: bool = False,
    index: int = 0,
) -> PageEntry:
    return PageEntry(
        index=index,
        type_name=type_name,
        is_root=is_root,
        page=page,
        total_pages=total_pages,
        model="dry_run",
        generated_at=_DT,
        output=output,
    )


# ---------------------------------------------------------------------------
# stitch_type_pages
# ---------------------------------------------------------------------------


class TestStitchTypePages:
    def test_empty_list_returns_empty_string(self) -> None:
        assert stitch_type_pages([]) == ""

    def test_single_page_is_returned_as_is(self) -> None:
        code = "public class Foo\n{\n    public string? Id { get; init; }\n}"
        result = stitch_type_pages([code])
        assert "public class Foo" in result
        assert "public string? Id" in result

    def test_second_page_fields_inserted_before_closing_brace(self) -> None:
        page1 = "public class Foo\n{\n    public string? Id { get; init; }\n}"
        page2 = (
            "// BEGIN_FIELDS\n"
            "    public string? Name { get; init; }\n"
            "// END_FIELDS"
        )
        result = stitch_type_pages([page1, page2])
        # Both fields should appear, and the class should still close properly
        assert "public string? Id" in result
        assert "public string? Name" in result
        assert result.count("}") == result.count("{")

    def test_three_pages_all_fields_present(self) -> None:
        page1 = "public class Big\n{\n    public string? A { get; init; }\n}"
        page2 = "// BEGIN_FIELDS\n    public string? B { get; init; }\n// END_FIELDS"
        page3 = "// BEGIN_FIELDS\n    public string? C { get; init; }\n// END_FIELDS"
        result = stitch_type_pages([page1, page2, page3])
        assert "public string? A" in result
        assert "public string? B" in result
        assert "public string? C" in result
        assert result.count("}") == result.count("{")

    def test_fields_without_markers_appended(self) -> None:
        """When page 2+ has no BEGIN/END markers, the raw text is still appended."""
        page1 = "public class Foo\n{\n    public string? Id { get; init; }\n}"
        page2 = "    public int? Count { get; init; }"
        result = stitch_type_pages([page1, page2])
        assert "public int? Count" in result


# ---------------------------------------------------------------------------
# assemble_from_pages
# ---------------------------------------------------------------------------


class TestAssembleFromPages:
    def test_empty_list_returns_newline(self) -> None:
        result = assemble_from_pages([])
        assert result == "\n"

    def test_single_type_single_page(self) -> None:
        entries = [
            _entry("Root", 1, 1, "public class RootDataObject\n{\n}", is_root=True),
        ]
        result = assemble_from_pages(entries)
        assert "public class RootDataObject" in result
        assert result.endswith("\n")

    def test_multiple_types_are_separated_by_blank_line(self) -> None:
        entries = [
            _entry("Root", 1, 1, "public class Root\n{\n}", is_root=True),
            _entry("Status", 1, 1, "public enum Status\n{\n    Active,\n}"),
        ]
        result = assemble_from_pages(entries)
        assert "public class Root" in result
        assert "public enum Status" in result
        # Double-newline separator
        assert "\n\n" in result

    def test_type_ordering_preserved_by_first_occurrence(self) -> None:
        """Types appear in the .cs in the same order as their first page entry."""
        entries = [
            _entry("Alpha", 1, 1, "public class Alpha {}", is_root=True),
            _entry("Beta", 1, 1, "public enum Beta {}"),
            _entry("Gamma", 1, 1, "public enum Gamma {}"),
        ]
        result = assemble_from_pages(entries)
        alpha_pos = result.index("Alpha")
        beta_pos = result.index("Beta")
        gamma_pos = result.index("Gamma")
        assert alpha_pos < beta_pos < gamma_pos

    def test_multi_page_type_is_stitched(self) -> None:
        entries = [
            _entry("Big", 1, 2, "public class Big\n{\n    public string? A { get; init; }\n}", is_root=True),
            _entry("Big", 2, 2, "// BEGIN_FIELDS\n    public string? B { get; init; }\n// END_FIELDS"),
        ]
        result = assemble_from_pages(entries)
        assert "public string? A" in result
        assert "public string? B" in result
        # Only one class declaration for Big
        assert result.count("public class Big") == 1

    def test_pages_sorted_by_page_number_regardless_of_entry_order(self) -> None:
        """Page 2 arriving before page 1 in the list must still stitch correctly."""
        entries = [
            _entry("Root", 2, 2, "// BEGIN_FIELDS\n    public string? B { get; init; }\n// END_FIELDS", is_root=True),
            _entry("Root", 1, 2, "public class Root\n{\n    public string? A { get; init; }\n}", is_root=True),
        ]
        result = assemble_from_pages(entries)
        assert "public class Root" in result
        # Both fields stitched in despite reversed input order
        assert "public string? A" in result
        assert "public string? B" in result

    def test_mixed_single_and_multi_page_types(self) -> None:
        entries = [
            _entry("Root", 1, 2, "public class Root\n{\n    public string? A { get; init; }\n}", is_root=True, index=0),
            _entry("Status", 1, 1, "public enum Status\n{\n    Active,\n}", index=1),
            _entry("Root", 2, 2, "// BEGIN_FIELDS\n    public string? B { get; init; }\n// END_FIELDS", is_root=True, index=2),
        ]
        result = assemble_from_pages(entries)
        assert "public class Root" in result
        assert "public enum Status" in result
        assert "public string? A" in result
        assert "public string? B" in result
        # Root comes before Status (first-occurrence order)
        assert result.index("public class Root") < result.index("public enum Status")

    def test_result_ends_with_newline(self) -> None:
        entries = [_entry("Foo", 1, 1, "public class Foo {}")]
        assert assemble_from_pages(entries).endswith("\n")

    def test_brace_balance_preserved(self) -> None:
        """Assembled output should have balanced braces."""
        entries = [
            _entry("Root", 1, 2, "public class Root\n{\n    public string? A { get; init; }\n}", is_root=True),
            _entry("Root", 2, 2, "// BEGIN_FIELDS\n    public int? Count { get; init; }\n// END_FIELDS"),
            _entry("Kind", 1, 1, "public enum Kind\n{\n    One,\n    Two,\n}"),
        ]
        result = assemble_from_pages(entries)
        assert result.count("{") == result.count("}")
