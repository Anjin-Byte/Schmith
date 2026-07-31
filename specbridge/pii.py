"""PII classification pre-pass for SpecBridge codegen.

Classifies every field in a type closure for PII / sensitive data before
code generation.  Results are stored in-place on the property dicts and
later passed through to build_field_info / _format_fields_section so the
code-generation prompts carry [pii] and [review: ...] attributes.

Three keys are set on each property dict:
    pii        (bool | None)  – True  → emit [WriteOnly] in generated C#
    pii_reason (str  | None)  – one-sentence justification for the decision
    pii_review (bool | None)  – True  → add // [REVIEW: reason] comment
                                        regardless of pii value

pii=None means the field could not be classified (JSON parse failure or
field absent from the LLM response).  Unclassified fields have no effect
on code generation.

run_pii_pass() also returns structured logs mirroring the codegen artefacts:
    prompt_log   – per-batch system+user prompt text  → pii/prompts.json
    page_entries – per-batch raw LLM output + token counts → pii/pages.json
"""

from __future__ import annotations

import datetime
import json
import sys
from typing import Any, TYPE_CHECKING, cast

if TYPE_CHECKING:
    from specbridge.generation.llm import GenerationResult, LLMProvider

PII_CRITERIA = """
PII and sensitive data that MUST be marked WriteOnly includes but is not limited to:
- Government issued ID numbers (SSN, passport, driver's license, comparable)
- Payment information (account, credit card, debit card numbers)
- Income, salary, benefits, Worker's Compensation or other compensation data
- Medical data or health information
- Authentication data (usernames, passwords, keys, tokens, secrets)
- SEC regulated information
- Personal information (full name, birthday, age, sex, gender, orientation, religion, race, ethnicity)
- Contact information (street address, phone, fax, email)
- Confidential business information (trade secrets, patents, marketing, revenue, upcoming plans)
- Operating financial data (taxes, bills, activity)
- Legal information
- Sensitive IT data (configurations, IP addresses, privileged usernames)
""".strip()

_SYSTEM_PROMPT = "You are a PII classifier for API data fields in software connectors."


def _utcnow() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _build_classify_prompt(
    fields: list[dict[str, Any]],
    type_name: str,
    endpoint_path: str,
) -> str:
    """Build the user prompt for a batch of fields."""
    field_lines: list[str] = []
    for f in fields:
        json_name = f.get("json_name", "")
        schema_id = f.get("schema_id", "")
        description = (f.get("description") or "").strip()
        # Derive a simple type label from the schema_id tail.
        type_label = schema_id.split("/")[-1] if "/" in schema_id else schema_id or "unknown"
        line = f'  - json_name: "{json_name}"   type: {type_label}'
        if description:
            line += f'   description: "{description}"'
        field_lines.append(line)

    fields_block = "\n".join(field_lines)

    return (
        "Classify each API field below for PII or sensitive data per App Xchange connector standards.\n"
        "\n"
        f"ENDPOINT: {endpoint_path}\n"
        f"TYPE: {type_name}\n"
        "\n"
        "CRITERIA:\n"
        f"{PII_CRITERIA}\n"
        "\n"
        "RULES:\n"
        "- pii=true  if the field clearly contains or could contain PII/sensitive data\n"
        "- pii=false if it clearly does not\n"
        "- review=true if the classification is borderline or context-dependent (explain in reason)\n"
        "- reason: one sentence — the justification for pii=true or pii=false.\n"
        "  For review=true cases: explain BOTH why it could be PII and why it might not be.\n"
        "\n"
        "FIELDS:\n"
        f"{fields_block}\n"
        "\n"
        "Return ONLY a JSON array — no markdown, no explanation:\n"
        "[\n"
        '  {"json_name": "email", "pii": true,  "reason": "Email is contact information.", "review": false},\n'
        '  {"json_name": "id",    "pii": false, "reason": "Numeric ID with no personal data.", "review": false}\n'
        "]"
    )


def classify_fields_pii(
    fields: list[dict[str, Any]],
    type_name: str,
    endpoint_path: str,
    provider: LLMProvider,
) -> tuple[str, GenerationResult | None]:
    """Classify a batch of field dicts for PII in-place.

    Sets pii, pii_reason, pii_review on each field dict.
    If the LLM response cannot be parsed or a field is absent from the
    response, those three keys are set to None (unclassified).

    Args:
        fields: List of property dicts from the type tree (mutated in-place).
        type_name: Name of the type containing these fields (for context).
        endpoint_path: Endpoint path string (e.g. "GET /customers/{id}").
        provider: Configured LLM provider.

    Returns:
        Tuple of (prompt, result) where prompt is the formatted classification
        prompt and result is the raw GenerationResult (or None on LLM failure).
        The prompt is always returned so the caller can log it even on failure.
    """
    if not fields:
        return "", None

    prompt = _build_classify_prompt(fields, type_name, endpoint_path)

    try:
        result = provider.generate(prompt, system=_SYSTEM_PROMPT)
        response_text = result.text.strip()
    except Exception as exc:
        print(
            f"[pii] LLM call failed for {type_name}: {exc}",
            file=sys.stderr,
        )
        for field in fields:
            field["pii"] = None
            field["pii_reason"] = None
            field["pii_review"] = None
        return prompt, None

    # Strip markdown fences if the model wrapped its output anyway.
    if response_text.startswith("```"):
        first_newline = response_text.find("\n")
        if first_newline != -1:
            response_text = response_text[first_newline + 1:]
        if response_text.endswith("```"):
            response_text = response_text[:-3].rstrip()

    try:
        entries: list[dict[str, Any]] = json.loads(response_text)
        if not isinstance(entries, list):
            raise ValueError("Expected a JSON array")
    except (json.JSONDecodeError, ValueError) as exc:
        print(
            f"[pii] JSON parse failure for {type_name}: {exc}",
            file=sys.stderr,
        )
        for field in fields:
            field["pii"] = None
            field["pii_reason"] = None
            field["pii_review"] = None
        return prompt, result

    # Build a lookup from json_name → classification entry.
    by_name: dict[str, dict[str, Any]] = {}
    for entry in entries:
        if isinstance(entry, dict) and "json_name" in entry:
            by_name[entry["json_name"]] = entry

    for field in fields:
        json_name = field.get("json_name", "")
        entry = by_name.get(json_name)
        if entry is None:
            field["pii"] = None
            field["pii_reason"] = None
            field["pii_review"] = None
        else:
            raw_pii = entry.get("pii")
            field["pii"] = bool(raw_pii) if raw_pii is not None else None
            field["pii_reason"] = entry.get("reason") or None
            raw_review = entry.get("review")
            field["pii_review"] = bool(raw_review) if raw_review is not None else False

    return prompt, result


def run_pii_pass(
    root_type: dict[str, Any],
    nested_types: list[dict[str, Any]],
    endpoint_path: str,
    provider: LLMProvider,
    batch_size: int = 20,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Classify all fields in a type closure for PII.

    Iterates root_type and all nested_types in order. For each type,
    calls classify_fields_pii in batches of batch_size. Mutates property
    dicts in-place. Emits a rich progress bar to stderr.

    Args:
        root_type: Root type dict from the type tree (has "properties" key).
        nested_types: List of nested type dicts.
        endpoint_path: Endpoint string for context (e.g. "GET /customers/{id}").
        provider: Configured LLM provider.
        batch_size: Maximum fields per LLM classification call.

    Returns:
        Tuple of (prompt_log, page_entries):
        - prompt_log: per-batch dicts with type_name, batch, total_batches,
          system, user — written to pii/prompts.json by the CLI.
        - page_entries: per-batch dicts with index, type_name, batch,
          total_batches, model, generated_at, output, input_tokens,
          output_tokens — written to pii/pages.json by the CLI.
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

    all_types = [root_type] + list(nested_types)

    # Pre-compute batches so we know the total call count before we start.
    type_batches: list[tuple[dict[str, Any], list[list[dict[str, Any]]]]] = []
    for type_entry in all_types:
        properties: list[dict[str, Any]] = type_entry.get("properties") or []
        if not properties:
            continue
        batches = [properties[i: i + batch_size] for i in range(0, len(properties), batch_size)]
        type_batches.append((type_entry, batches))

    if not type_batches:
        return [], []

    total_calls = sum(len(batches) for _, batches in type_batches)
    call_word = "call" if total_calls == 1 else "calls"
    type_count = len(type_batches)

    # cast: Console satisfies _ConsolePrinter; needed because rich is not
    # resolvable by the IDE's interpreter (uv venv path mismatch).
    console = cast(Any, Console(stderr=True))
    console.print(
        f"\n[bold]Classifying PII[/bold]  [dim]{endpoint_path}[/dim]"
    )
    console.print(
        f"  [dim]{type_count} type{'s' if type_count != 1 else ''}  ·"
        f"  {total_calls} LLM {call_word}[/dim]\n"
    )

    prompt_log: list[dict[str, Any]] = []
    page_entries: list[dict[str, Any]] = []
    global_index = 0

    with cast(Any, Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        MofNCompleteColumn(),
        TimeElapsedColumn(),
        console=console,
        transient=False,
    )) as progress:
        task = progress.add_task("[cyan]PII[/cyan]", total=total_calls)

        for type_entry, batches in type_batches:
            type_name: str = type_entry.get("name") or "Unknown"
            batch_count = len(batches)

            for batch_idx, batch in enumerate(batches, start=1):
                page_info = (
                    f"  page {batch_idx}/{batch_count}" if batch_count > 1 else ""
                )
                progress.update(
                    task,
                    description=(
                        f"[cyan]{type_name}[/cyan]"
                        f"  [dim]{len(batch)} fields{page_info}[/dim]"
                    ),
                )

                prompt, result = classify_fields_pii(batch, type_name, endpoint_path, provider)

                prompt_log.append({
                    "type_name": type_name,
                    "batch": batch_idx,
                    "total_batches": batch_count,
                    "system": _SYSTEM_PROMPT,
                    "user": prompt,
                })
                page_entries.append({
                    "index": global_index,
                    "type_name": type_name,
                    "batch": batch_idx,
                    "total_batches": batch_count,
                    "model": provider.model,
                    "generated_at": _utcnow(),
                    "output": result.text if result is not None else "",
                    "input_tokens": result.input_tokens if result is not None else 0,
                    "output_tokens": result.output_tokens if result is not None else 0,
                })
                global_index += 1
                progress.advance(task)

    classified = sum(
        1 for t in all_types
        for f in (t.get("properties") or [])
        if f.get("pii") is not None
    )
    pii_count = sum(
        1 for t in all_types
        for f in (t.get("properties") or [])
        if f.get("pii") is True
    )
    console.print(
        f"  [green]✓[/green] Done — {classified} fields classified"
        f"  [dim]({pii_count} PII)[/dim]\n"
    )

    return prompt_log, page_entries
