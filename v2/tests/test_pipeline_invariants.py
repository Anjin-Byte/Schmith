"""Tests for pipeline_invariants.py — each invariant catches its violation."""

import pytest

from schmith.ir.models import Endpoint, OperationResponse, SchemaNode
from schmith.ir.store import SchemaStore
from schmith import pipeline_invariants as iv
from schmith.pipeline_invariants import InvariantViolation


def _make_store(*schema_ids: str) -> SchemaStore:
    schemas = {sid: {"kind": "object", "name_hint": sid.split("/")[-1]} for sid in schema_ids}
    return SchemaStore(schemas)


# ---------------------------------------------------------------------------
# Stage 1
# ---------------------------------------------------------------------------

class TestStage1:
    def setup_method(self) -> None:
        self.store = _make_store("schema:components/Customer")
        self.valid_ops = [{"id": "op1", "method": "GET", "path_template": "/customers"}]

    def test_passes_valid(self) -> None:
        iv.check_all(1, (self.store, self.valid_ops), self.store)

    def test_fails_empty_store(self) -> None:
        empty = SchemaStore({})
        with pytest.raises(InvariantViolation, match="empty"):
            iv.check_all(1, (empty, self.valid_ops), empty)

    def test_fails_empty_operations(self) -> None:
        with pytest.raises(InvariantViolation):
            iv.check_all(1, (self.store, []), self.store)

    def test_fails_non_list_operations(self) -> None:
        with pytest.raises(InvariantViolation):
            iv.check_all(1, (self.store, "not a list"), self.store)  # type: ignore[arg-type]

    def test_fails_operation_missing_key(self) -> None:
        bad_op = {"id": "op1", "method": "GET"}  # missing path_template
        with pytest.raises(InvariantViolation, match="path_template"):
            iv.check_all(1, (self.store, [bad_op]), self.store)

    def test_fails_wrong_type(self) -> None:
        with pytest.raises(InvariantViolation):
            iv.check_all(1, "not a tuple", self.store)  # type: ignore[arg-type]


# ---------------------------------------------------------------------------
# Stage 2
# ---------------------------------------------------------------------------

class TestStage2:
    def setup_method(self) -> None:
        self.store = _make_store("schema:components/Customer")
        self.valid = OperationResponse(
            status_code="200",
            schema_id="schema:components/Customer",
            media_type="application/json",
            description=None,
        )

    def test_passes_valid(self) -> None:
        iv.check_all(2, self.valid, self.store)

    def test_fails_not_operation_response(self) -> None:
        with pytest.raises(InvariantViolation):
            iv.check_all(2, {"status_code": "200"}, self.store)  # type: ignore[arg-type]

    def test_fails_none_schema_id(self) -> None:
        bad = OperationResponse(status_code="200", schema_id=None, media_type=None, description=None)
        with pytest.raises(InvariantViolation, match="None"):
            iv.check_all(2, bad, self.store)

    def test_fails_schema_id_not_in_store(self) -> None:
        bad = OperationResponse(
            status_code="200",
            schema_id="schema:components/Missing",
            media_type=None,
            description=None,
        )
        with pytest.raises(InvariantViolation, match="not present"):
            iv.check_all(2, bad, self.store)

    def test_passes_primitive_schema_id(self) -> None:
        # Primitive IDs don't live in the store but are valid
        resp = OperationResponse(
            status_code="200",
            schema_id="schema:types/string",
            media_type=None,
            description=None,
        )
        iv.check_all(2, resp, self.store)


# ---------------------------------------------------------------------------
# Stage 3
# ---------------------------------------------------------------------------

class TestStage3:
    def setup_method(self) -> None:
        self.store = _make_store("schema:components/Customer")
        self.valid = SchemaNode(
            schema_id="schema:components/Customer",
            schema={"kind": "object", "name_hint": "Customer"},
        )

    def test_passes_valid(self) -> None:
        iv.check_all(3, self.valid, self.store)

    def test_fails_not_schema_node(self) -> None:
        with pytest.raises(InvariantViolation):
            iv.check_all(3, {"schema_id": "x"}, self.store)  # type: ignore[arg-type]

    def test_fails_empty_schema_id(self) -> None:
        bad = SchemaNode(schema_id="", schema={"kind": "object"})
        with pytest.raises(InvariantViolation, match="empty"):
            iv.check_all(3, bad, self.store)

    def test_fails_empty_schema_dict(self) -> None:
        bad = SchemaNode(schema_id="schema:components/Customer", schema={})
        with pytest.raises(InvariantViolation):
            iv.check_all(3, bad, self.store)


# ---------------------------------------------------------------------------
# Stage 4 and 5 (shared logic)
# ---------------------------------------------------------------------------

class TestStage4And5:
    def setup_method(self) -> None:
        self.store = _make_store("schema:components/Customer")
        self.valid_root = {
            "name": "CustomerDataObject",
            "schema_id": "schema:components/Customer",
            "kind": "object",
            "properties": [],
        }
        self.valid_nested: list[dict] = []

    def _check(self, stage: int, data: object) -> None:
        iv.check_all(stage, data, self.store)  # type: ignore[arg-type]

    def test_stage4_passes_valid(self) -> None:
        self._check(4, (self.valid_root, self.valid_nested))

    def test_stage5_passes_valid(self) -> None:
        self._check(5, (self.valid_root, self.valid_nested))

    def test_fails_not_tuple(self) -> None:
        with pytest.raises(InvariantViolation):
            self._check(4, self.valid_root)

    def test_fails_empty_root_type(self) -> None:
        with pytest.raises(InvariantViolation):
            self._check(4, ({}, self.valid_nested))

    def test_fails_root_missing_name(self) -> None:
        bad = {"schema_id": "schema:components/X", "kind": "object"}
        with pytest.raises(InvariantViolation, match="name"):
            self._check(4, (bad, self.valid_nested))

    def test_fails_empty_root_name(self) -> None:
        bad = {"name": "", "schema_id": "schema:components/X", "kind": "object"}
        with pytest.raises(InvariantViolation):
            self._check(4, (bad, self.valid_nested))

    def test_fails_nested_not_list(self) -> None:
        with pytest.raises(InvariantViolation):
            self._check(4, (self.valid_root, "not a list"))

    def test_fails_nested_item_not_dict(self) -> None:
        with pytest.raises(InvariantViolation):
            self._check(4, (self.valid_root, ["not a dict"]))

    def test_fails_nested_item_missing_name(self) -> None:
        bad_nested = [{"schema_id": "schema:components/X", "kind": "object"}]
        with pytest.raises(InvariantViolation, match="name"):
            self._check(4, (self.valid_root, bad_nested))


# ---------------------------------------------------------------------------
# Stage 6
# ---------------------------------------------------------------------------

class TestStage6:
    def setup_method(self) -> None:
        self.store = _make_store()

    def test_passes_valid_code(self) -> None:
        iv.check_all(6, "public class CustomerDataObject { }", self.store)

    def test_fails_not_string(self) -> None:
        with pytest.raises(InvariantViolation):
            iv.check_all(6, 42, self.store)  # type: ignore[arg-type]

    def test_fails_empty_string(self) -> None:
        with pytest.raises(InvariantViolation, match="empty"):
            iv.check_all(6, "", self.store)

    def test_fails_whitespace_only(self) -> None:
        with pytest.raises(InvariantViolation, match="empty"):
            iv.check_all(6, "   \n  ", self.store)


# ---------------------------------------------------------------------------
# Dispatcher
# ---------------------------------------------------------------------------

class TestCheckAllDispatcher:
    def setup_method(self) -> None:
        self.store = _make_store("schema:components/X")

    def test_invalid_stage_raises_value_error(self) -> None:
        with pytest.raises(ValueError, match="No invariant"):
            iv.check_all(99, {}, self.store)
