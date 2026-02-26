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
from typing import Any, Protocol, cast

import re

from schmith.adapters.base import ApiAdapter
from schmith.adapters.spec import openapi, raml
from schmith.generation.llm import (
    DryRunProvider,
    LLMProvider,
    generate_code,
    get_provider,
    stitch_type_pages,
)
from schmith.generation.prompt import (
    MAX_ENUM_VALUES_PER_PAGE,
    MAX_FIELDS_PER_PAGE,
    build_prompt_packet,
    build_system_prompt,
    build_type_page_prompt,
    format_schema_markdown,
)
from schmith.generation.type_tree import build_type_hierarchy
from schmith.ir.models import Endpoint, OperationResponse, SchemaNode
from schmith.ir.store import SchemaStore
from schmith import pipeline_invariants as iv
from schmith.validation import ValidationResult, print_validation_report, validate_generated_code


class _ConsolePrinter(Protocol):
    """Minimal structural interface for the rich Console we use."""

    def print(self, *args: Any, **kwargs: Any) -> None: ...


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
            # Safe: ruamel.yaml is untyped; a well-formed RAML file loads as a dict.
            return cast(dict[str, Any], result) if isinstance(result, dict) else {}

        import yaml  # type: ignore[import-untyped]
        with open(path, encoding="utf-8") as f:
            result = yaml.safe_load(f)
        # Safe: yaml.safe_load on a well-formed spec file produces str-keyed mappings.
        return cast(dict[str, Any], result) if isinstance(result, dict) else {}

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
# Paginated generation helpers
# ---------------------------------------------------------------------------


def _chunk_fields(fields: list[dict[str, Any]], page_size: int) -> list[list[dict[str, Any]]]:
    """Split a field list into pages of at most page_size items."""
    if not fields or len(fields) <= page_size:
        return [fields]
    return [fields[i: i + page_size] for i in range(0, len(fields), page_size)]


def _chunk_enum_values(
    values: list[Any], names: list[Any] | None, page_size: int
) -> list[tuple[list[Any], list[Any] | None]]:
    """Split enum values (and parallel names) into pages of at most page_size items."""
    if not values or len(values) <= page_size:
        return [(values, names)]
    pages = []
    for i in range(0, len(values), page_size):
        v_slice = values[i: i + page_size]
        n_slice = names[i: i + page_size] if isinstance(names, list) else None
        pages.append((v_slice, n_slice))
    return pages


def _generate_paginated(
    packet: dict[str, Any],
    provider: LLMProvider,
    system_prompt: str,
    page_size: int = MAX_FIELDS_PER_PAGE,
    enum_page_size: int = MAX_ENUM_VALUES_PER_PAGE,
) -> tuple[str, list[dict[str, Any]]]:
    """Generate C# code for all types in a packet using per-type, per-page calls.

    Each type (root + nested) gets its own series of LLM calls. If a type has
    more than page_size fields it is split across multiple calls; the results
    are stitched back together by stitch_type_pages.

    Emits a rich progress bar to stderr during actual LLM generation. Skipped
    for DryRunProvider (calls are instantaneous, no useful signal).

    Returns:
        Tuple of (csharp_code, prompt_log) where prompt_log is a list of
        per-page dicts with keys: type_name, is_root, page, total_pages,
        system, user. Useful for debugging LLM behaviour post-run.
    """
    from rich.console import Console  # type: ignore[import-not-found]
    from rich.progress import (  # type: ignore[import-not-found]
        BarColumn,
        MofNCompleteColumn,
        Progress,
        SpinnerColumn,
        TextColumn,
        TimeElapsedColumn,
    )

    all_types: list[tuple[dict[str, Any], bool]] = [(packet["root"], True)] + [
        (nt, False) for nt in packet.get("nested_types", [])
    ]

    # Pre-compute page lists so we know the total call count before we start.
    # Each entry: (type_entry, is_root, is_enum, pages)
    # - For object types: pages is list[list[dict]]  (each page = slice of fields)
    # - For enum types:   pages is list[tuple[list, list|None]]  (values, names per page)
    type_pages: list[tuple[dict[str, Any], bool, bool, list[Any]]] = []
    for te, is_root in all_types:
        is_enum_type = bool(te.get("enum_values") and not te.get("fields"))
        if is_enum_type:
            pages: list[Any] = _chunk_enum_values(
                te.get("enum_values") or [],
                te.get("enum_names"),
                enum_page_size,
            )
        else:
            pages = _chunk_fields(te.get("fields") or [], page_size)
        type_pages.append((te, is_root, is_enum_type, pages))

    total_calls = sum(len(pages) for _, _, _, pages in type_pages)

    metadata = packet["metadata"]
    data_object_name = metadata["data_object_name"]
    endpoint_label = f"{metadata['method']} {metadata['path']}"

    # cast: Console satisfies _ConsolePrinter; needed because rich is not
    # resolvable by the IDE's interpreter (uv venv path mismatch).
    console: _ConsolePrinter = cast(_ConsolePrinter, Console(stderr=True))
    is_dry_run = isinstance(provider, DryRunProvider)

    # Header printed before the bar starts.
    action = "Dry-run plan" if is_dry_run else "Generating"
    console.print(
        f"\n[bold]{action}[/bold] [cyan]{data_object_name}[/cyan]"
        f"  [dim]{endpoint_label}[/dim]"
    )
    type_count = len(all_types)
    call_word = "call" if total_calls == 1 else "calls"
    console.print(
        f"  [dim]{type_count} type{'s' if type_count != 1 else ''}  ·"
        f"  {total_calls} LLM {call_word}[/dim]\n"
    )

    all_outputs: list[str] = []
    prompt_log: list[dict[str, Any]] = []

    if is_dry_run:
        # For dry-run, just show a plan table without a live bar.
        for type_entry, is_root, is_enum_type, pages in type_pages:
            role = "root" if is_root else "nested"
            page_count = len(pages)
            if is_enum_type:
                item_count = len(type_entry.get("enum_values") or [])
                item_label = "values"
            else:
                item_count = len(type_entry.get("fields") or [])
                item_label = "fields"
            console.print(
                f"  [cyan]{type_entry['name']}[/cyan]"
                f"  [dim]({role})[/dim]"
                f"  [dim]·  {item_count} {item_label}  ·  {page_count} page{'s' if page_count != 1 else ''}[/dim]"
            )
            page_outputs: list[str] = []
            for page_index, page_data in enumerate(pages, start=1):
                if is_enum_type:
                    values_page, names_page = page_data
                    fields_page: list[dict[str, Any]] = []
                else:
                    fields_page = page_data
                    values_page, names_page = None, None
                prompt = build_type_page_prompt(
                    packet, type_entry, fields_page, page_index, page_count, is_root,
                    values_page=values_page, names_page=names_page,
                )
                prompt_log.append({
                    "type_name": type_entry["name"],
                    "is_root": is_root,
                    "page": page_index,
                    "total_pages": page_count,
                    "system": system_prompt,
                    "user": prompt,
                })
                code = generate_code(prompt, system_prompt, provider)
                page_outputs.append(code)
            all_outputs.append(stitch_type_pages(page_outputs))
        console.print()
    else:
        # Live progress bar for actual LLM calls.
        desc_col = TextColumn("[progress.description]{task.description}")
        with cast(Any, Progress(
            SpinnerColumn(),
            desc_col,
            BarColumn(),
            MofNCompleteColumn(),
            TimeElapsedColumn(),
            console=console,
            transient=False,
        )) as progress:
            task = progress.add_task(f"[cyan]{data_object_name}[/cyan]", total=total_calls)

            for type_entry, is_root, is_enum_type, pages in type_pages:
                class_name = type_entry["name"]
                role = "root" if is_root else "nested"
                page_count = len(pages)

                page_outputs_live: list[str] = []
                for page_index, page_data in enumerate(pages, start=1):
                    if is_enum_type:
                        values_page, names_page = page_data
                        fields_page = []
                        item_count = len(values_page)
                        item_label = "values"
                    else:
                        fields_page = page_data
                        values_page, names_page = None, None
                        item_count = len(fields_page)
                        item_label = "fields"
                    page_info = (
                        f"  page {page_index}/{page_count}  ·  {item_count} {item_label}"
                        if page_count > 1
                        else f"  ·  {item_count} {item_label}"
                    )
                    progress.update(
                        task,
                        description=(
                            f"[cyan]{class_name}[/cyan]  [dim]({role}){page_info}[/dim]"
                        ),
                    )
                    prompt = build_type_page_prompt(
                        packet, type_entry, fields_page, page_index, page_count, is_root,
                        values_page=values_page, names_page=names_page,
                    )
                    prompt_log.append({
                        "type_name": type_entry["name"],
                        "is_root": is_root,
                        "page": page_index,
                        "total_pages": page_count,
                        "system": system_prompt,
                        "user": prompt,
                    })
                    code = generate_code(prompt, system_prompt, provider)
                    page_outputs_live.append(code)
                    progress.advance(task)

                all_outputs.append(stitch_type_pages(page_outputs_live))

        console.print(f"  [green]✓[/green] Done — {total_calls} LLM {call_word} completed\n")

    return "\n\n".join(all_outputs).rstrip() + "\n", prompt_log


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
    fields_per_page: int | None = None,
    enum_values_per_page: int | None = None,
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
    packet = build_prompt_packet(
        root_type, nested_types, endpoint, store.all(),
        response_description=op_response.description,
    )
    system_prompt = build_system_prompt()
    schema_md = format_schema_markdown(root_type, nested_types)

    provider: LLMProvider = get_provider(_llm_config)
    gen_kwargs: dict[str, Any] = {}
    if fields_per_page is not None:
        gen_kwargs["page_size"] = fields_per_page
    if enum_values_per_page is not None:
        gen_kwargs["enum_page_size"] = enum_values_per_page
    csharp_code, prompt_log = _generate_paginated(packet, provider, system_prompt, **gen_kwargs)

    if debug:
        iv.check_all(6, csharp_code, store)

    # ------------------------------------------------------------------
    # Post-generation validation (skipped for dry runs)
    # ------------------------------------------------------------------
    if not isinstance(provider, DryRunProvider):
        from rich.console import Console as _Console  # type: ignore[import-not-found]
        validation_result = validate_generated_code(csharp_code, packet)
        # cast: Console satisfies _ConsolePrinter; needed because rich is not
        # resolvable by the IDE's interpreter (uv venv path mismatch).
        _val_console: _ConsolePrinter = cast(_ConsolePrinter, _Console(stderr=True))
        print_validation_report(validation_result, _val_console)
    else:
        validation_result = ValidationResult()

    ir_data: dict[str, Any] = {
        "endpoint": {
            "method": endpoint.method,
            "path": endpoint.path,
            "status_code": op_response.status_code,
            "schema_id": op_response.schema_id,
        },
        "root_type": root_type,
        "nested_types": nested_types,
        "prompts": prompt_log,
        "validation": {
            "is_clean": validation_result.is_clean,
            "errors": [
                {"code": i.code, "message": i.message, "detail": i.detail}
                for i in validation_result.errors
            ],
            "warnings": [
                {"code": i.code, "message": i.message, "detail": i.detail}
                for i in validation_result.warnings
            ],
        },
    }

    return ir_data, schema_md, csharp_code
