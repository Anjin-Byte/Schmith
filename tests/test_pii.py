"""Tests for the PII classification pre-pass (specbridge/pii.py)."""

from __future__ import annotations

import json
import re
from typing import Any

from specbridge.generation.llm import GenerationResult
from specbridge.generation.prompt import _format_fields_section
from specbridge.pii import classify_fields_pii, run_pii_pass


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


class MockProvider:
    """Minimal LLM provider that returns a preset response string."""

    model: str = "mock"

    def __init__(self, response: str) -> None:
        self._response = response
        self.calls: list[str] = []

    def generate(self, prompt: str, system: str | None = None) -> GenerationResult:
        self.calls.append(prompt)
        return GenerationResult(text=self._response, input_tokens=0, output_tokens=0)

    def count_tokens(self, prompt: str, system: str | None = None) -> int:
        return len(prompt) // 4


class FailingProvider:
    """Provider that always raises on generate()."""

    model: str = "fail"

    def generate(self, prompt: str, system: str | None = None) -> GenerationResult:
        raise RuntimeError("network error")

    def count_tokens(self, prompt: str, system: str | None = None) -> int:
        return 0


class EchoProvider:
    """Provider whose response is derived from the prompt dynamically."""

    model: str = "echo"

    def __init__(self) -> None:
        self.calls: list[str] = []

    def generate(self, prompt: str, system: str | None = None) -> GenerationResult:
        self.calls.append(prompt)
        names = re.findall(r'json_name: "([^"]+)"', prompt)
        payload = json.dumps([
            {"json_name": n, "pii": False, "reason": "Not PII.", "review": False}
            for n in names
        ])
        return GenerationResult(text=payload, input_tokens=0, output_tokens=0)

    def count_tokens(self, prompt: str, system: str | None = None) -> int:
        return 0


def _make_fields(*specs: tuple[str, str]) -> list[dict[str, Any]]:
    """Build property dicts: [(json_name, schema_id), ...]."""
    return [
        {"json_name": name, "schema_id": sid, "description": ""}
        for name, sid in specs
    ]


def _make_prompt_field(**kwargs: Any) -> dict[str, Any]:
    """Build a fully-populated field dict suitable for _format_fields_section."""
    base: dict[str, Any] = {
        "json_name": "phone",
        "csharp_name": "Phone",
        "csharp_type": "string",
        "nullable": True,
        "required": False,
        "deprecated": False,
        "read_only": False,
        "write_only": False,
        "type_unresolved": False,
        "description": "",
        "enum_values": None,
        "enum_names": None,
        "constraints": None,
        "is_shapeless": False,
        "pii": None,
        "pii_reason": None,
        "pii_review": None,
    }
    base.update(kwargs)
    return base


# ---------------------------------------------------------------------------
# TestClassifyFieldsPii
# ---------------------------------------------------------------------------


class TestClassifyFieldsPii:
    def test_pii_field_set_in_place(self) -> None:
        fields = _make_fields(("email", "schema:types/string"))
        provider = MockProvider(json.dumps([
            {"json_name": "email", "pii": True, "reason": "Email is contact information.", "review": False}
        ]))
        classify_fields_pii(fields, "User", "GET /users", provider)
        assert fields[0]["pii"] is True
        assert fields[0]["pii_review"] is False
        assert "Email" in fields[0]["pii_reason"]

    def test_non_pii_field_set_in_place(self) -> None:
        fields = _make_fields(("id", "schema:types/integer"))
        provider = MockProvider(json.dumps([
            {"json_name": "id", "pii": False, "reason": "Numeric ID with no personal data.", "review": False}
        ]))
        classify_fields_pii(fields, "User", "GET /users", provider)
        assert fields[0]["pii"] is False
        assert fields[0]["pii_review"] is False

    def test_review_field_set_in_place(self) -> None:
        fields = _make_fields(("address", "schema:types/string"))
        provider = MockProvider(json.dumps([
            {"json_name": "address", "pii": False, "reason": "Could be personal or public.", "review": True}
        ]))
        classify_fields_pii(fields, "Company", "GET /companies", provider)
        assert fields[0]["pii"] is False
        assert fields[0]["pii_review"] is True
        assert fields[0]["pii_reason"] is not None

    def test_invalid_json_leaves_unclassified(self) -> None:
        fields = _make_fields(("email", "schema:types/string"))
        provider = MockProvider("this is not json")
        classify_fields_pii(fields, "User", "GET /users", provider)
        assert fields[0]["pii"] is None
        assert fields[0]["pii_reason"] is None
        assert fields[0]["pii_review"] is None

    def test_missing_field_in_response_is_none(self) -> None:
        fields = _make_fields(
            ("email", "schema:types/string"),
            ("id", "schema:types/integer"),
        )
        # Response classifies only "id", not "email"
        provider = MockProvider(json.dumps([
            {"json_name": "id", "pii": False, "reason": "Numeric ID.", "review": False}
        ]))
        classify_fields_pii(fields, "User", "GET /users", provider)
        assert fields[0]["pii"] is None    # email — absent from response
        assert fields[0]["pii_reason"] is None
        assert fields[0]["pii_review"] is None
        assert fields[1]["pii"] is False   # id — classified

    def test_markdown_fenced_response_is_parsed(self) -> None:
        """LLM wraps output in ```json fences — should still parse."""
        fields = _make_fields(("email", "schema:types/string"))
        payload = json.dumps([
            {"json_name": "email", "pii": True, "reason": "Contact info.", "review": False}
        ])
        provider = MockProvider(f"```json\n{payload}\n```")
        classify_fields_pii(fields, "User", "GET /users", provider)
        assert fields[0]["pii"] is True

    def test_llm_failure_leaves_unclassified(self) -> None:
        fields = _make_fields(("email", "schema:types/string"))
        classify_fields_pii(fields, "User", "GET /users", FailingProvider())
        assert fields[0]["pii"] is None

    def test_empty_field_list_is_noop(self) -> None:
        provider = MockProvider("[]")
        classify_fields_pii([], "User", "GET /users", provider)
        assert provider.calls == []

    def test_non_array_response_leaves_unclassified(self) -> None:
        """LLM returns a JSON object instead of an array."""
        fields = _make_fields(("email", "schema:types/string"))
        provider = MockProvider(json.dumps({"json_name": "email", "pii": True}))
        classify_fields_pii(fields, "User", "GET /users", provider)
        assert fields[0]["pii"] is None


# ---------------------------------------------------------------------------
# TestRunPiiPass
# ---------------------------------------------------------------------------


class TestRunPiiPass:
    def test_batch_size_respected(self) -> None:
        """5 fields with batch_size=2 → ceil(5/2)=3 LLM calls."""
        fields = [
            {"json_name": f"f{i}", "schema_id": "schema:types/string", "description": ""}
            for i in range(5)
        ]
        provider = EchoProvider()
        root_type: dict[str, Any] = {"name": "Root", "properties": fields}
        run_pii_pass(root_type, [], "GET /items", provider, batch_size=2)
        assert len(provider.calls) == 3

    def test_all_types_classified(self) -> None:
        """root + nested types both get pii annotation."""
        root_fields = _make_fields(("id", "schema:types/integer"))
        nested_fields = _make_fields(("email", "schema:types/string"))
        root_type: dict[str, Any] = {"name": "Root", "properties": root_fields}
        nested_type: dict[str, Any] = {"name": "Nested", "properties": nested_fields}
        provider = EchoProvider()
        run_pii_pass(root_type, [nested_type], "GET /x", provider, batch_size=20)
        assert root_fields[0]["pii"] is False
        assert nested_fields[0]["pii"] is False

    def test_empty_type_skipped(self) -> None:
        """Types with no properties produce no LLM calls."""
        provider = MockProvider("[]")
        root_type: dict[str, Any] = {"name": "Root", "properties": []}
        run_pii_pass(root_type, [], "GET /x", provider, batch_size=20)
        assert provider.calls == []

    def test_single_batch_when_fields_fit(self) -> None:
        """3 fields with batch_size=10 → exactly 1 call."""
        fields = _make_fields(
            ("id", "schema:types/integer"),
            ("name", "schema:types/string"),
            ("email", "schema:types/string"),
        )
        provider = EchoProvider()
        root_type: dict[str, Any] = {"name": "Root", "properties": fields}
        run_pii_pass(root_type, [], "GET /x", provider, batch_size=10)
        assert len(provider.calls) == 1

    def test_mutations_visible_on_original_dicts(self) -> None:
        """run_pii_pass mutates the original property dicts in-place."""
        prop = {"json_name": "email", "schema_id": "schema:types/string", "description": ""}
        root_type: dict[str, Any] = {"name": "Root", "properties": [prop]}
        provider = EchoProvider()
        run_pii_pass(root_type, [], "GET /x", provider, batch_size=20)
        assert "pii" in prop


# ---------------------------------------------------------------------------
# TestPiiInPromptFormat
# ---------------------------------------------------------------------------


class TestPiiInPromptFormat:
    def test_pii_attr_appears_in_format(self) -> None:
        field = _make_prompt_field(pii=True, pii_reason="Contact info.", pii_review=False)
        combined = "\n".join(_format_fields_section([field]))
        assert "pii" in combined

    def test_review_attr_appears_in_format(self) -> None:
        field = _make_prompt_field(pii=False, pii_reason="Could be public.", pii_review=True)
        combined = "\n".join(_format_fields_section([field]))
        assert "review:" in combined

    def test_non_pii_no_pii_attr(self) -> None:
        field = _make_prompt_field(pii=False, pii_reason="Not PII.", pii_review=False)
        combined = "\n".join(_format_fields_section([field]))
        assert "pii" not in combined

    def test_none_pii_no_pii_attr(self) -> None:
        field = _make_prompt_field(pii=None, pii_reason=None, pii_review=None)
        combined = "\n".join(_format_fields_section([field]))
        assert "pii" not in combined

    def test_pii_and_review_together(self) -> None:
        field = _make_prompt_field(pii=True, pii_reason="Borderline PII.", pii_review=True)
        combined = "\n".join(_format_fields_section([field]))
        assert "pii" in combined
        assert "review:" in combined

    def test_review_reason_included_in_format(self) -> None:
        reason = "Could be personal or company address"
        field = _make_prompt_field(pii=False, pii_reason=reason, pii_review=True)
        combined = "\n".join(_format_fields_section([field]))
        assert reason.rstrip(".") in combined

    def test_review_without_pii(self) -> None:
        """pii=False, pii_review=True → review shown but no pii attr."""
        field = _make_prompt_field(pii=False, pii_reason="Public company address.", pii_review=True)
        combined = "\n".join(_format_fields_section([field]))
        # "review:" should appear but standalone "pii" (without "review") should not
        assert "review:" in combined

    # ------------------------------------------------------------------
    # Consolidated REVIEW (issue 2 fix)
    # ------------------------------------------------------------------

    def test_unresolved_and_pii_review_produces_one_review_attr(self) -> None:
        """type_unresolved + pii_review → single [review: ...] attr, no standalone type_unresolved."""
        field = _make_prompt_field(
            type_unresolved=True,
            pii_review=True,
            pii_reason="Could be personal data",
        )
        combined = "\n".join(_format_fields_section([field]))
        # Only one 'review:' token in the attribute string
        assert combined.count("review:") == 1
        # type_unresolved suppressed from attrs when pii_review is also set
        assert "type_unresolved" not in combined

    def test_unresolved_and_pii_review_consolidates_both_reasons(self) -> None:
        """Consolidated review attr contains both the pii_reason and 'type unresolved'."""
        field = _make_prompt_field(
            type_unresolved=True,
            pii_review=True,
            pii_reason="Could be personal data",
        )
        combined = "\n".join(_format_fields_section([field]))
        assert "Could be personal data" in combined
        assert "type unresolved from IR" in combined

    def test_unresolved_without_pii_review_emits_type_unresolved_attr(self) -> None:
        """type_unresolved=True, pii_review=False → standalone type_unresolved attr (no review:)."""
        field = _make_prompt_field(type_unresolved=True, pii_review=False, pii_reason=None)
        combined = "\n".join(_format_fields_section([field]))
        assert "type_unresolved" in combined
        assert "review:" not in combined

    def test_pii_review_without_unresolved_omits_type_unresolved(self) -> None:
        """pii_review=True, type_unresolved=False → review attr, no 'type unresolved' text."""
        field = _make_prompt_field(
            type_unresolved=False,
            pii_review=True,
            pii_reason="Borderline contact info",
        )
        combined = "\n".join(_format_fields_section([field]))
        assert "review:" in combined
        assert "type unresolved" not in combined
        assert "type_unresolved" not in combined


# ---------------------------------------------------------------------------
# TestClassifyFieldsPiiReturnValue
# ---------------------------------------------------------------------------


class TestClassifyFieldsPiiReturnValue:
    def test_returns_prompt_and_result_on_success(self) -> None:
        fields = _make_fields(("email", "schema:types/string"))
        provider = MockProvider(json.dumps([
            {"json_name": "email", "pii": True, "reason": "Contact info.", "review": False}
        ]))
        prompt, result = classify_fields_pii(fields, "User", "GET /users", provider)
        assert isinstance(prompt, str)
        assert len(prompt) > 0
        assert result is not None
        assert result.text is not None

    def test_returns_prompt_and_none_on_llm_failure(self) -> None:
        fields = _make_fields(("email", "schema:types/string"))
        prompt, result = classify_fields_pii(fields, "User", "GET /users", FailingProvider())
        assert isinstance(prompt, str)
        assert result is None

    def test_returns_prompt_and_result_on_parse_failure(self) -> None:
        """Bad JSON → result still returned (for logging), pii set to None."""
        fields = _make_fields(("email", "schema:types/string"))
        provider = MockProvider("not json")
        prompt, result = classify_fields_pii(fields, "User", "GET /users", provider)
        assert isinstance(prompt, str)
        assert result is not None  # LLM responded; parse just failed
        assert fields[0]["pii"] is None

    def test_returns_empty_prompt_and_none_for_empty_fields(self) -> None:
        provider = MockProvider("[]")
        prompt, result = classify_fields_pii([], "User", "GET /users", provider)
        assert prompt == ""
        assert result is None
        assert provider.calls == []

    def test_prompt_contains_field_name(self) -> None:
        fields = _make_fields(("email", "schema:types/string"))
        provider = MockProvider(json.dumps([
            {"json_name": "email", "pii": True, "reason": "Contact.", "review": False}
        ]))
        prompt, _ = classify_fields_pii(fields, "User", "GET /users", provider)
        assert "email" in prompt

    def test_prompt_contains_endpoint_and_type(self) -> None:
        fields = _make_fields(("name", "schema:types/string"))
        provider = MockProvider(json.dumps([
            {"json_name": "name", "pii": False, "reason": "x", "review": False}
        ]))
        prompt, _ = classify_fields_pii(fields, "CustomerType", "GET /customers", provider)
        assert "GET /customers" in prompt
        assert "CustomerType" in prompt


# ---------------------------------------------------------------------------
# TestRunPiiPassLogs
# ---------------------------------------------------------------------------


class TestRunPiiPassLogs:
    def test_returns_prompt_log_and_page_entries(self) -> None:
        fields = _make_fields(("id", "schema:types/integer"), ("email", "schema:types/string"))
        provider = EchoProvider()
        root_type: dict[str, Any] = {"name": "Root", "properties": fields}
        prompt_log, page_entries = run_pii_pass(root_type, [], "GET /x", provider, batch_size=20)
        assert len(prompt_log) == 1
        assert len(page_entries) == 1

    def test_prompt_log_entry_shape(self) -> None:
        fields = _make_fields(("id", "schema:types/integer"))
        provider = EchoProvider()
        root_type: dict[str, Any] = {"name": "MyType", "properties": fields}
        prompt_log, _ = run_pii_pass(root_type, [], "GET /x", provider, batch_size=20)
        entry = prompt_log[0]
        assert entry["type_name"] == "MyType"
        assert entry["batch"] == 1
        assert entry["total_batches"] == 1
        assert isinstance(entry["system"], str)
        assert isinstance(entry["user"], str)
        assert len(entry["user"]) > 0

    def test_page_entry_shape(self) -> None:
        fields = _make_fields(("id", "schema:types/integer"))
        provider = EchoProvider()
        root_type: dict[str, Any] = {"name": "MyType", "properties": fields}
        _, page_entries = run_pii_pass(root_type, [], "GET /x", provider, batch_size=20)
        entry = page_entries[0]
        assert entry["index"] == 0
        assert entry["type_name"] == "MyType"
        assert entry["batch"] == 1
        assert entry["total_batches"] == 1
        assert isinstance(entry["model"], str)
        assert isinstance(entry["generated_at"], str)
        assert isinstance(entry["output"], str)
        assert isinstance(entry["input_tokens"], int)
        assert isinstance(entry["output_tokens"], int)

    def test_batch_indices_sequential(self) -> None:
        """5 fields, batch_size=2 → 3 entries with batch 1/2/3 and index 0/1/2."""
        fields = [
            {"json_name": f"f{i}", "schema_id": "schema:types/string", "description": ""}
            for i in range(5)
        ]
        provider = EchoProvider()
        root_type: dict[str, Any] = {"name": "Root", "properties": fields}
        prompt_log, page_entries = run_pii_pass(root_type, [], "GET /x", provider, batch_size=2)
        assert len(prompt_log) == 3
        assert len(page_entries) == 3
        assert [e["batch"] for e in page_entries] == [1, 2, 3]
        assert [e["index"] for e in page_entries] == [0, 1, 2]
        assert all(e["total_batches"] == 3 for e in page_entries)

    def test_multiple_types_in_log(self) -> None:
        """root + nested each produce separate log entries."""
        root_fields = _make_fields(("id", "schema:types/integer"))
        nested_fields = _make_fields(("email", "schema:types/string"))
        root_type: dict[str, Any] = {"name": "Root", "properties": root_fields}
        nested_type: dict[str, Any] = {"name": "Nested", "properties": nested_fields}
        provider = EchoProvider()
        prompt_log, page_entries = run_pii_pass(
            root_type, [nested_type], "GET /x", provider, batch_size=20
        )
        assert len(prompt_log) == 2
        assert len(page_entries) == 2
        assert prompt_log[0]["type_name"] == "Root"
        assert prompt_log[1]["type_name"] == "Nested"
        assert page_entries[0]["index"] == 0
        assert page_entries[1]["index"] == 1

    def test_empty_type_closure_returns_empty_logs(self) -> None:
        root_type: dict[str, Any] = {"name": "Root", "properties": []}
        provider = MockProvider("[]")
        prompt_log, page_entries = run_pii_pass(root_type, [], "GET /x", provider, batch_size=20)
        assert prompt_log == []
        assert page_entries == []
