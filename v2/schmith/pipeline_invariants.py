"""Pipeline invariants — structural assertions between pipeline stages.

Each invariant function checks the output of one pipeline stage and raises
InvariantViolation if something structurally wrong would cause a later stage
to silently produce bad results.

The six stages and their invariant checks:

  Stage 1 — Spec loading  → SchemaStore + operations list
  Stage 2 — Endpoint match → OperationResponse
  Stage 3 — Root resolution → SchemaNode (via adapter.resolve_root)
  Stage 4 — Type tree → (root_type: dict, nested_types: list[dict])
  Stage 5 — Tree transform → (root_type: dict, nested_types: list[dict])
  Stage 6 — Code generation → str

Usage (debug mode):

    from schmith import pipeline_invariants as iv
    iv.check_all(1, (store, operations), store)
    iv.check_all(2, op_response, store)
    ...
"""

from __future__ import annotations

from typing import Any

from schmith.ir.models import OperationResponse, SchemaNode
from schmith.ir.store import SchemaStore


class InvariantViolation(Exception):
    """Raised when a pipeline stage output fails a structural check."""

    def __init__(self, message: str, details: dict | None = None):
        super().__init__(message)
        self.details: dict = details or {}

    def __str__(self) -> str:
        base = super().__str__()
        if self.details:
            detail_lines = "\n".join(f"  {k}: {v}" for k, v in self.details.items())
            return f"{base}\n{detail_lines}"
        return base


# ---------------------------------------------------------------------------
# Individual invariant functions
# ---------------------------------------------------------------------------


def check_stage_1(data: tuple[SchemaStore, list[dict]], store: SchemaStore) -> None:
    """Stage 1 invariant: spec loaded → SchemaStore + operations list.

    Asserts:
    - The store is non-empty (at least one schema was extracted).
    - The operations list is a non-empty list.
    - Every operation has an 'id', 'method', and 'path_template' key.
    """
    if not isinstance(data, tuple) or len(data) != 2:
        raise InvariantViolation(
            "Stage 1 output must be a 2-tuple (SchemaStore, list[dict])",
            {"got": type(data).__name__},
        )

    out_store, operations = data

    if len(out_store) == 0:
        raise InvariantViolation(
            "Stage 1: SchemaStore is empty — no schemas were extracted from the spec"
        )

    if not isinstance(operations, list) or len(operations) == 0:
        raise InvariantViolation(
            "Stage 1: operations list is empty — no operations were extracted from the spec",
            {"type": type(operations).__name__},
        )

    for i, op in enumerate(operations):
        for key in ("id", "method", "path_template"):
            if key not in op:
                raise InvariantViolation(
                    f"Stage 1: operation[{i}] is missing required key '{key}'",
                    {"operation": op},
                )


def check_stage_2(data: OperationResponse, store: SchemaStore) -> None:
    """Stage 2 invariant: endpoint matched → OperationResponse.

    Asserts:
    - data is an OperationResponse instance.
    - data.schema_id is not None (a response schema was found).
    - data.schema_id refers to a schema present in the store (or is a
      primitive type ID — these don't live in the store).
    """
    if not isinstance(data, OperationResponse):
        raise InvariantViolation(
            "Stage 2 output must be an OperationResponse",
            {"got": type(data).__name__},
        )

    if data.schema_id is None:
        raise InvariantViolation(
            "Stage 2: OperationResponse.schema_id is None — "
            "the matched operation has no response schema",
            {"status_code": data.status_code, "media_type": data.media_type},
        )

    # Primitive schema IDs are valid and not stored in SchemaStore
    primitive_prefixes = ("schema:types/",)
    is_primitive = any(data.schema_id.startswith(p) for p in primitive_prefixes)

    if not is_primitive and data.schema_id not in store:
        raise InvariantViolation(
            f"Stage 2: schema_id '{data.schema_id}' is not present in the SchemaStore",
            {"schema_id": data.schema_id},
        )


def check_stage_3(data: SchemaNode, store: SchemaStore) -> None:
    """Stage 3 invariant: root resolved → SchemaNode.

    Asserts:
    - data is a SchemaNode instance.
    - data.schema_id is not empty.
    - data.schema is a non-empty dict (the actual schema data was loaded).
    """
    if not isinstance(data, SchemaNode):
        raise InvariantViolation(
            "Stage 3 output must be a SchemaNode",
            {"got": type(data).__name__},
        )

    if not data.schema_id:
        raise InvariantViolation(
            "Stage 3: SchemaNode.schema_id is empty"
        )

    if not isinstance(data.schema, dict) or not data.schema:
        raise InvariantViolation(
            f"Stage 3: SchemaNode.schema is empty or not a dict for schema_id '{data.schema_id}'",
            {"schema_id": data.schema_id, "schema_type": type(data.schema).__name__},
        )


def _check_type_closure(
    data: tuple[dict, list[dict]],
    stage_label: str,
) -> None:
    """Shared validation for stage 4 and 5 (type closure tuple)."""
    if not isinstance(data, tuple) or len(data) != 2:
        raise InvariantViolation(
            f"{stage_label} output must be a 2-tuple (root_type: dict, nested_types: list[dict])",
            {"got": type(data).__name__},
        )

    root_type, nested_types = data

    if not isinstance(root_type, dict) or not root_type:
        raise InvariantViolation(
            f"{stage_label}: root_type must be a non-empty dict",
            {"got": type(root_type).__name__},
        )

    required_root_keys = ("name", "schema_id", "kind")
    for key in required_root_keys:
        if key not in root_type:
            raise InvariantViolation(
                f"{stage_label}: root_type is missing required key '{key}'",
                {"root_type_keys": list(root_type.keys())},
            )

    if not root_type.get("name"):
        raise InvariantViolation(
            f"{stage_label}: root_type['name'] is empty — type tree could not determine a name",
            {"schema_id": root_type.get("schema_id")},
        )

    if not isinstance(nested_types, list):
        raise InvariantViolation(
            f"{stage_label}: nested_types must be a list",
            {"got": type(nested_types).__name__},
        )

    for i, nt in enumerate(nested_types):
        if not isinstance(nt, dict):
            raise InvariantViolation(
                f"{stage_label}: nested_types[{i}] is not a dict",
                {"got": type(nt).__name__},
            )
        if "name" not in nt:
            raise InvariantViolation(
                f"{stage_label}: nested_types[{i}] is missing 'name'",
                {"keys": list(nt.keys())},
            )


def check_stage_4(data: tuple[dict, list[dict]], store: SchemaStore) -> None:
    """Stage 4 invariant: type tree built → (root_type, nested_types)."""
    _check_type_closure(data, "Stage 4")


def check_stage_5(data: tuple[dict, list[dict]], store: SchemaStore) -> None:
    """Stage 5 invariant: tree transformed → (root_type, nested_types)."""
    _check_type_closure(data, "Stage 5")


def check_stage_6(data: str, store: SchemaStore) -> None:
    """Stage 6 invariant: code generated → str.

    Asserts:
    - data is a string.
    - data is non-empty (actual code was produced).
    """
    if not isinstance(data, str):
        raise InvariantViolation(
            "Stage 6 output must be a string",
            {"got": type(data).__name__},
        )

    if not data.strip():
        raise InvariantViolation(
            "Stage 6: generated code string is empty"
        )


# ---------------------------------------------------------------------------
# Dispatcher
# ---------------------------------------------------------------------------

_CHECKERS = {
    1: check_stage_1,
    2: check_stage_2,
    3: check_stage_3,
    4: check_stage_4,
    5: check_stage_5,
    6: check_stage_6,
}


def check_all(stage: int, data: Any, store: SchemaStore) -> None:
    """Run the invariant check for the given pipeline stage.

    Args:
        stage: Pipeline stage number (1–6).
        data: The output of that stage.
        store: The SchemaStore from stage 1 (available to all invariants).

    Raises:
        InvariantViolation: If the stage output fails its structural check.
        ValueError: If stage is not in the range 1–6.
    """
    checker = _CHECKERS.get(stage)
    if checker is None:
        raise ValueError(f"No invariant defined for stage {stage}. Valid stages: 1–6.")
    checker(data, store)
