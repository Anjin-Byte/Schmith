"""Pipeline orchestrator — six-stage single-endpoint DataObject generation.

Each stage is isolated and produces a typed output. Debug mode runs
pipeline_invariants after every stage so structural problems surface
immediately rather than as confusing failures later.

Stages:
  1. Spec loading   → (SchemaStore, operations: list[dict])
  2. Endpoint match → OperationResponse
  3. Root resolve   → SchemaNode  (via adapter.resolve_root)
  4. Type tree      → (root_type: dict, nested_types: list[dict])
  5. Tree transform → (root_type: dict, nested_types: list[dict])  (via adapter.transform_tree)
  6. Code gen       → csharp_code: str
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import re

from schmith.adapters.base import ApiAdapter
from schmith.adapters.spec import openapi, raml
from schmith.generation.llm import LLMProvider, generate_code, get_provider
from schmith.generation.prompt import (
    build_prompt_packet,
    build_system_prompt,
    build_user_prompt,
    format_schema_markdown,
)
from schmith.generation.type_tree import build_type_hierarchy
from schmith.ir.models import Endpoint, OperationResponse, SchemaNode
from schmith.ir.store import SchemaStore
from schmith import pipeline_invariants as iv


# ---------------------------------------------------------------------------
# Exceptions
# ---------------------------------------------------------------------------


class PipelineError(Exception):
    """Base class for pipeline errors."""


class SpecLoadError(PipelineError):
    """Raised when the spec file cannot be loaded or parsed."""


class EndpointMatchError(PipelineError):
    """Raised when no matching operation/response is found for the endpoint."""


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _name_from_path(path: str) -> str:
    """Derive a PascalCase type name from the last non-parameter path segment.

    For list endpoints that return anonymous arrays, this gives a useful
    fallback name when the response schema has no title or $ref.

    Examples:
      /rest/v1.0/tax_codes                        → TaxCode
      /rest/v1.0/projects/{project_id}/timesheets → Timesheet
      /rest/v1.1/projects                         → Project
    """
    # Strip trailing slashes and split
    segments = [s for s in path.rstrip("/").split("/") if s]
    # Take the last segment that isn't a path parameter
    name_seg = next(
        (s for s in reversed(segments) if not s.startswith("{")),
        "Unknown",
    )
    # Convert snake_case / kebab-case to PascalCase words
    words = re.split(r"[_\-\s]+", name_seg)
    pascal = "".join(w.capitalize() for w in words if w)
    # Singularize common English plurals (simple heuristic)
    if pascal.endswith("ies"):
        pascal = pascal[:-3] + "y"
    elif pascal.endswith("ses") or pascal.endswith("shes") or pascal.endswith("ches"):
        pascal = pascal[:-2]
    elif pascal.endswith("s") and not pascal.endswith("ss") and len(pascal) > 3:
        pascal = pascal[:-1]
    return pascal


def _load_spec(spec_path: str, spec_format: str) -> dict[str, Any]:
    """Load a spec file from disk into a plain dict.

    Uses ruamel.yaml for RAML (handles !include tags) and pyyaml for
    OpenAPI YAML/JSON.
    """
    path = Path(spec_path)
    if not path.exists():
        raise SpecLoadError(f"Spec file not found: {spec_path}")

    try:
        if path.suffix.lower() == ".json":
            with open(path, encoding="utf-8") as f:
                return json.load(f)  # type: ignore[no-any-return]

        if spec_format.lower() == "raml":
            from ruamel.yaml import YAML  # type: ignore[import-untyped]
            _yaml = YAML()
            _yaml.preserve_quotes = True
            with open(path, encoding="utf-8") as f:
                result = _yaml.load(f)
            return result if isinstance(result, dict) else {}

        import yaml  # type: ignore[import-untyped]
        with open(path, encoding="utf-8") as f:
            result = yaml.safe_load(f)
        return result if isinstance(result, dict) else {}

    except Exception as exc:
        raise SpecLoadError(f"Failed to load spec '{spec_path}': {exc}") from exc


def _extract_stage1(
    spec: dict[str, Any],
    spec_path: str,
    spec_format: str,
) -> tuple[SchemaStore, list[dict[str, Any]]]:
    """Call the right spec adapter and return (SchemaStore, operations)."""
    fmt = spec_format.lower()
    if fmt == "raml":
        schemas = raml.extract_schemas(spec, spec_path)
        operations = raml.extract_operations(spec, spec_path)
    elif fmt in ("openapi", "openapi3", "swagger", "oas"):
        schemas = openapi.extract_schemas(spec, spec_path)
        operations = openapi.extract_operations(spec, spec_path)
    else:
        raise PipelineError(
            f"Unknown spec_format '{spec_format}'. "
            "Supported: openapi, openapi3, swagger, oas, raml"
        )
    return SchemaStore(schemas), operations


def _match_endpoint(
    operations: list[dict[str, Any]],
    endpoint: Endpoint,
    target_status: str,
) -> OperationResponse:
    """Find the OperationResponse for (method, path, status).

    Matching logic:
    1. Find the operation whose method and path_template match.
    2. Among its responses, prefer the exact target_status.
    3. If not found, fall back to the numerically lowest 2xx response
       that has a schema_id.
    """
    method = endpoint.method.upper()
    path = endpoint.path.rstrip("/")

    for op in operations:
        if op.get("method", "").upper() != method:
            continue

        op_path = (op.get("path_template") or "").rstrip("/")
        if op_path != path:
            continue

        # Operation matched — search responses
        responses: list[dict[str, Any]] = op.get("responses") or []

        # Prefer the exact target status with a schema
        for resp in responses:
            if str(resp.get("status_code", "")) == target_status and resp.get("schema_id"):
                return OperationResponse(
                    status_code=str(resp["status_code"]),
                    schema_id=resp["schema_id"],
                    media_type=resp.get("media_type"),
                    description=resp.get("description"),
                )

        # Fallback: lowest 2xx with a schema_id
        two_xx = [
            r for r in responses
            if str(r.get("status_code", "")).startswith("2") and r.get("schema_id")
        ]
        if two_xx:
            best = sorted(two_xx, key=lambda r: str(r.get("status_code", "999")))[0]
            return OperationResponse(
                status_code=str(best["status_code"]),
                schema_id=best["schema_id"],
                media_type=best.get("media_type"),
                description=best.get("description"),
            )

        raise EndpointMatchError(
            f"Operation found for {method} {path} but no 2xx response has a schema_id. "
            f"Available status codes: {[r.get('status_code') for r in responses]}"
        )

    raise EndpointMatchError(
        f"No operation found matching {method} {path}. "
        f"Available: {[(o.get('method'), o.get('path_template')) for o in operations]}"
    )


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def run(
    spec_path: str,
    spec_format: str,
    method: str,
    path: str,
    adapter: ApiAdapter | None = None,
    llm_config: dict[str, Any] | None = None,
    target_status: str = "200",
    debug: bool = False,
) -> tuple[dict[str, Any], str, str]:
    """Run the full six-stage pipeline for a single endpoint.

    Args:
        spec_path: Path to the API spec file.
        spec_format: Spec format string: "openapi", "openapi3", "swagger",
            "oas", or "raml".
        method: HTTP method (case-insensitive, e.g. "GET").
        path: Endpoint path template (e.g. "/customers/{id}").
        adapter: Optional API-specific adapter. Defaults to base ApiAdapter.
        llm_config: Config dict forwarded to get_provider(). If absent,
            get_provider({}) is called which falls back to environment variables.
        target_status: Preferred HTTP status code for the response schema.
            Defaults to "200". Falls back to lowest 2xx if not found.
        debug: If True, run pipeline_invariants after each stage and raise
            InvariantViolation on structural problems.

    Returns:
        (ir_data, schema_md, csharp_code):
        - ir_data: dict with endpoint metadata, root_type, and nested_types.
        - schema_md: Markdown summary of the type closure (for schema.md).
        - csharp_code: Generated C# DataObject code.

    Raises:
        SpecLoadError: If the spec cannot be loaded.
        EndpointMatchError: If no matching operation/response is found.
        InvariantViolation: If debug=True and a stage fails a structural check.
        PipelineError: For other pipeline-level failures.
    """
    _adapter = adapter if adapter is not None else ApiAdapter()
    _llm_config = llm_config or {}

    # ------------------------------------------------------------------
    # Stage 1 — Load spec → SchemaStore + operations
    # ------------------------------------------------------------------
    spec = _load_spec(spec_path, spec_format)
    store, operations = _extract_stage1(spec, spec_path, spec_format)

    if debug:
        iv.check_all(1, (store, operations), store)

    # ------------------------------------------------------------------
    # Stage 2 — Match endpoint → OperationResponse
    # ------------------------------------------------------------------
    endpoint = Endpoint(method=method.upper(), path=path)
    op_response = _match_endpoint(operations, endpoint, target_status)

    if debug:
        iv.check_all(2, op_response, store)

    # ------------------------------------------------------------------
    # Stage 3 — Resolve root → SchemaNode  (adapter hook)
    # ------------------------------------------------------------------
    schema_id = op_response.schema_id or ""
    response_schema = store.get(schema_id) or {}
    response_node = SchemaNode(schema_id=schema_id, schema=response_schema)

    root_node = _adapter.resolve_root(endpoint, response_node)

    # Auto-unwrap array responses: for list endpoints the response schema is a
    # bare array and the "real" type is the items schema.  An array root produces
    # a class with 0 fields, which is never useful.  Using items as root gives a
    # proper named class (e.g. "Timesheet" from the items title/name_hint).
    if root_node.schema.get("kind") == "array":
        items_id = root_node.schema.get("items_schema_id")
        if items_id:
            items_schema = store.get(items_id) or {}
            root_node = SchemaNode(
                schema_id=items_id,
                schema=items_schema,
                parent=root_node,
                edge_kind="array_items",
                depth=root_node.depth + 1,
            )

    # If the adapter returned a node with a different schema_id, reload schema
    if root_node.schema_id != schema_id or not root_node.schema:
        loaded = store.get(root_node.schema_id)
        if loaded and not root_node.schema:
            root_node = SchemaNode(
                schema_id=root_node.schema_id,
                schema=loaded,
                parent=root_node.parent,
                edge_kind=root_node.edge_kind,
                depth=root_node.depth,
            )

    if debug:
        iv.check_all(3, root_node, store)

    # ------------------------------------------------------------------
    # Stage 4 — Build type tree → (root_type, nested_types)
    # ------------------------------------------------------------------
    # Inject "id" so build_type_hierarchy can resolve the root name
    root_schema_with_id: dict[str, Any] = {**root_node.schema, "id": root_node.schema_id}

    root_type, nested_types = build_type_hierarchy(
        root_schema=root_schema_with_id,
        schemas_by_id=store.all(),
        load_schema_detail=store.resolver(),
        adapter=_adapter,
    )

    # Path-based fallback: if the root is still anonymous after array unwrapping
    # (no title or $ref name in the spec), derive a name from the endpoint path.
    # This produces "TaxCode" from /rest/v1.0/tax_codes instead of "Anonymous_…".
    if root_type["name"].startswith("Anonymous"):
        root_type = {**root_type, "name": _name_from_path(path)}

    if debug:
        iv.check_all(4, (root_type, nested_types), store)

    # ------------------------------------------------------------------
    # Stage 5 — Transform tree  (adapter hook)
    # ------------------------------------------------------------------
    root_type, nested_types = _adapter.transform_tree(root_type, nested_types)

    if debug:
        iv.check_all(5, (root_type, nested_types), store)

    # ------------------------------------------------------------------
    # Stage 6 — Generate code
    # ------------------------------------------------------------------
    packet = build_prompt_packet(root_type, nested_types, endpoint, store.all())
    system_prompt = build_system_prompt()
    user_prompt = build_user_prompt(packet)
    schema_md = format_schema_markdown(root_type, nested_types)

    provider: LLMProvider = get_provider(_llm_config)
    csharp_code = generate_code(user_prompt, system_prompt, provider)

    if debug:
        iv.check_all(6, csharp_code, store)

    ir_data: dict[str, Any] = {
        "endpoint": {
            "method": endpoint.method,
            "path": endpoint.path,
            "status_code": op_response.status_code,
            "schema_id": op_response.schema_id,
        },
        "root_type": root_type,
        "nested_types": nested_types,
    }

    return ir_data, schema_md, csharp_code
