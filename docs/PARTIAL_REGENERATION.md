# Partial Regeneration — System Design

## Overview

Each generation run produces a set of output artifacts for one endpoint. The current system
treats a run as atomic: all types are generated, stitched, and written together. There is no way
to regenerate one type or one page of a type without re-running everything.

This document designs a first-class partial regeneration system with three usage modes:

1. **Manual fix** — the developer identifies a problem in a generated type and wants to
   regenerate it, possibly with a different model, without discarding the rest of the output.
2. **Validation-driven retry** — the validator finds errors after generation and triggers
   targeted regeneration of the failing type(s) automatically.
3. **Model migration** — re-execute stored prompts through a different model without
   recomputing anything from the IR.

The unifying principle: **the prompt is the stable unit of work**. It is computed from the IR
once, stored on disk, and can be re-executed by any executor (any model) at any time. Page
boundaries are baked into the prompt text, not into the executor. Switching models does not
require recomputing page sizes.

**The `.cs` file is a pure derived artifact.** It is always reconstructed from `pages.json`
and carries no structural metadata of its own. `pages.json` is the authoritative record of page
outputs and type ordering. This eliminates any need for in-file type boundary markers — they
would create two sources of truth without adding capability.

---

## Concepts and Terminology

**Generation run:** A single invocation of `schmith generate` for one endpoint. Produces a
complete set of artifacts in an output directory.

**Type:** One entry in the type closure — the root object, a nested object, or a referenced
enum. Each type is always its own generation unit; types are never merged into a single LLM call.

**Page:** A slice of one type's fields (or enum values) submitted in a single LLM call. Page
boundaries are computed at generation time and fixed for the lifetime of the stored prompts.

**Page identity:** The triple `(type_name, page, total_pages)` uniquely identifies a page within
a run. When `total_pages == 1`, the type fits in one call.

**Prompt:** The exact system + user text sent to the LLM for one page. Stored verbatim in
`prompts.json`. Stable across models; the model is the executor, not part of the prompt content.

**Output:** The raw LLM response for one page after code extraction. Stored in `pages.json`.
The final `.cs` file is derived by stitching and assembling all outputs — it is never the primary
source of truth and can always be fully reconstructed from `pages.json`.

**Assembly:** The process of combining page outputs into a stitched type block, then combining
all type blocks into the final `.cs` file. Assembly is deterministic given the page outputs.

---

## Artifact Model

Every generation run produces five artifacts in the output directory:

```
output/{EndpointLabel}/
  {DataObjectName}.cs     # final assembled .cs — pure derived artifact
  ir.json                 # IR snapshot, endpoint metadata, validation summary
  schema.md               # human-readable schema (for review)
  prompts.json            # per-page prompt inputs  [already implemented]
  pages.json              # per-page LLM outputs    [new]
```

The relationship between artifacts:

```
ir.json ──────────────────────────────────────────────────┐
    │                                                      │
    ├─→ prompts.json (computed from IR at generation time) │
    │         │                                            │
    │         └─→ pages.json (output of submitting         │
    │                   each prompt to an LLM)             │
    │                         │                            │
    │                         └─→ {Name}.cs (assembly of  │
    │                                  all page outputs)   │
    │                                                      │
    └──────────────────────────────→ validation summary ───┘
```

`prompts.json` and `pages.json` are parallel: entry `i` in `prompts.json` corresponds to
entry `i` in `pages.json`, both identified by `(type_name, page, total_pages)`.

The `.cs` is the rightmost node in this graph — nothing reads it as input within the tooling.
Any partial regeneration operation reads from `prompts.json` and `pages.json`, not from the `.cs`.

### `prompts.json` format (existing, shown for reference)

```json
[
  {
    "type_name": "Project",
    "is_root": true,
    "page": 1,
    "total_pages": 3,
    "system": "Generate a C# Trimble XChange DataObject...",
    "user": "OUTPUT MODE: full_class\n...\nFIELDS:\n..."
  },
  ...
]
```

### `pages.json` format (new)

```json
{
  "version": 1,
  "endpoint": {"method": "GET", "path": "/rest/v1.1/projects"},
  "ir_hash": "sha256:a3f9...",
  "generated_at": "2026-02-25T10:30:00Z",
  "model": "claude-haiku-4-5-20251001",
  "pages": [
    {
      "index": 0,
      "type_name": "Project",
      "is_root": true,
      "page": 1,
      "total_pages": 3,
      "model": "claude-haiku-4-5-20251001",
      "generated_at": "2026-02-25T10:30:05Z",
      "input_tokens": 1842,
      "output_tokens": 623,
      "output": "public class ProjectDataObject\n{\n    ..."
    },
    {
      "index": 1,
      "type_name": "Project",
      "is_root": true,
      "page": 2,
      "total_pages": 3,
      "model": "claude-haiku-4-5-20251001",
      "generated_at": "2026-02-25T10:30:08Z",
      "input_tokens": 1611,
      "output_tokens": 544,
      "output": "// BEGIN_FIELDS\n    [JsonPropertyName(\"name\")]..."
    },
    ...
  ]
}
```

**`ir_hash`** is a SHA-256 of the canonical JSON of `ir.json` (using the existing `hashing.py`
infrastructure). It enables staleness detection: if `ir.json` changes after the prompts were
computed (spec update, IR fix), any cached pages should be treated with caution.

**Per-page `model`** records which model produced each page. During partial regeneration with a
different model, the envelope `model` field becomes the latest model used; individual page
entries record the actual executor.

**Type ordering** is implicit in the `pages` list: the first occurrence of each `type_name`
determines its position in the assembled `.cs`. Assembly iterates `pages` in order, groups by
`type_name` (preserving first-occurrence order), stitches each group, and joins the blocks.

---

## Assembly Module

A new module `schmith/assembly.py` owns all operations that combine page outputs into the
final `.cs`. It has no dependency on the `.cs` file itself — it reads from `pages.json`
entries and returns assembled code.

### Operations

```python
def stitch_type_pages(page_outputs: list[str]) -> str:
    """Combine page outputs for a single type into one class/enum block.

    Page 1 supplies the full class skeleton (full_class or class_only).
    Pages 2+ supply fields_only blocks (BEGIN_FIELDS / END_FIELDS delimited).
    Moved here from llm.py; llm.py re-exports for backward compatibility.
    """


def assemble_from_pages(pages: list[dict[str, Any]]) -> str:
    """Assemble the full .cs from all page entries in pages.json.

    Groups entries by type_name, preserving first-occurrence order.
    Stitches pages within each group (sorted by page index).
    Joins all stitched type blocks with double newlines.

    Args:
        pages: The "pages" list from pages.json (list of page entry dicts).

    Returns:
        Complete .cs file content, ready to write.
    """
```

The complete assembly logic is:

```python
from collections import OrderedDict

def assemble_from_pages(pages: list[dict[str, Any]]) -> str:
    # Group by type_name preserving first-occurrence order
    type_groups: OrderedDict[str, list[dict[str, Any]]] = OrderedDict()
    for entry in pages:
        name = entry["type_name"]
        if name not in type_groups:
            type_groups[name] = []
        type_groups[name].append(entry)

    type_blocks: list[str] = []
    for entries in type_groups.values():
        page_outputs = [e["output"] for e in sorted(entries, key=lambda e: e["page"])]
        type_blocks.append(stitch_type_pages(page_outputs))

    return "\n\n".join(type_blocks).rstrip() + "\n"
```

### Usage in the current pipeline

`_generate_paginated` currently does:

```python
all_outputs.append(stitch_type_pages(page_outputs))
...
return "\n\n".join(all_outputs).rstrip() + "\n", prompt_log
```

After this change it does:

```python
# Collect page output dicts as pages.json entries
all_page_entries.append({
    "index": global_page_index,
    "type_name": type_entry["name"],
    "is_root": is_root,
    "page": page_index,
    "total_pages": page_count,
    "model": provider.model,
    "generated_at": utcnow(),
    "input_tokens": input_tokens,   # if token metadata available
    "output_tokens": output_tokens,
    "output": raw_output,
})
...
# Assembly at end of run
cs_code = assemble_from_pages(all_page_entries)
return cs_code, prompt_log, all_page_entries
```

The `all_page_entries` list flows to the `pages.json` writer in `cli.py`. The `.cs` is
assembled from the same entries and written alongside it — they are always in sync by
construction.

---

## Partial Regeneration Operation

### Core function: `partial_regenerate`

```python
def partial_regenerate(
    output_dir: Path,
    type_names: list[str] | None = None,
    page_numbers: dict[str, list[int]] | None = None,
    llm_config: dict[str, Any] | None = None,
    correction_context: dict[str, list[str]] | None = None,
    max_retries: int = 1,
) -> PartialRegenResult:
    """Regenerate one or more types from stored prompts.

    Args:
        output_dir: Directory containing prompts.json and pages.json.
        type_names: Types to regenerate. None means all types.
        page_numbers: Optional dict of type_name → [page indices] to regenerate
            only specific pages. Pages not listed keep their existing output.
            None means all pages for each named type.
        llm_config: Provider config, overrides stored model if specified.
        correction_context: Optional dict of type_name → list of error strings
            to prepend as a CORRECTION block to page-1 prompts (used by validation
            retry).
        max_retries: How many times to attempt if validation still fails after
            regeneration. 1 means one attempt, no retry.

    Returns:
        PartialRegenResult with updated cs_code, validation result, and list of
        regenerated (type_name, page) pairs.
    """
```

### Algorithm

```
load prompts.json  → prompt_entries: list[PromptEntry]
load pages.json    → pages_store: PagesStore   # mutable, owns the list of page dicts

for each target (type_name, page_index):
    prompt = prompt_entries.find(type_name, page_index)
    user_text = prompt["user"]

    if correction_context and page_index == 1 and type_name in correction_context:
        user_text = build_correction_block(correction_context[type_name]) + "\n\n" + user_text

    new_output = provider.generate(user_text, system=prompt["system"])
    pages_store.update(type_name, page_index, new_output, model=provider.model)

# Re-assemble the full .cs from the updated page store
new_cs_code = assemble_from_pages(pages_store.pages)

write updated pages.json
write updated .cs
run validate_generated_code(new_cs_code, packet)
return PartialRegenResult(...)
```

No extraction or patching of the `.cs` file is needed. The entire `.cs` is rewritten from the
updated page store. For large files with many types, this is still fast — assembly is pure string
manipulation with no LLM calls.

### `PartialRegenResult`

```python
@dataclass
class PartialRegenResult:
    cs_code: str
    validation: ValidationResult
    regenerated: list[tuple[str, int]]   # (type_name, page) pairs that were resubmitted
    model_used: str
    pages_json_path: Path
    cs_path: Path
```

---

## Correction Block Format

When validation errors trigger regeneration, a CORRECTION block is prepended to the page-1
prompt for each failing type. The block is injected at call time — it is never written back
to `prompts.json`, which always stores the clean original prompt.

```
CORRECTION REQUIRED:
The previous attempt for this type produced the following errors. Fix them in your output.

  [UNDECLARED_TYPE] Property references type 'FlagEnum' which is not declared in this file.
    Declared types: ExtendedFlag, ProjectSector, Schedule2DataObject
  [DUPLICATE_FIELD] [JsonPropertyName("id")] appears 2 times in class 'Extended'.

Do not introduce any types not listed in NESTED TYPES / TYPE REFERENCE.
Do not omit any fields listed in this page's FIELDS section.
```

The existing page prompt follows immediately after, unchanged, so the LLM has full context.

---

## Validation Integration

### Per-type error attribution

`validate_generated_code` currently validates the entire `.cs` as one unit. For targeted retry,
errors must be attributed to specific types.

Since `pages.json` contains per-type page outputs, each type can be validated independently by
re-stitching its pages and validating the stitched block. This avoids any parsing of the `.cs`
and produces a clean 1:1 mapping of errors to types.

New function in `validation.py`:

```python
def validate_by_type(
    pages: list[dict[str, Any]],
    packet: dict[str, Any],
) -> dict[str, ValidationResult]:
    """Run validation per type block and return a map of type_name → result.

    Re-stitches each type's pages from the pages.json entry list. Validates
    each stitched block against a per-type packet derived from the full packet.

    Args:
        pages: The "pages" list from pages.json.
        packet: Full prompt packet (root + nested_types).

    Returns:
        Dict mapping type_name → ValidationResult for each type in the closure.
    """
```

Per-type packet derivation:
- **Root type**: `{"root": packet["root"], "nested_types": packet["nested_types"]}`
  (full packet; root page is expected to reference nested types)
- **Nested type**: `{"root": nested_entry, "nested_types": []}` where `nested_entry` is the
  matching entry from `packet["nested_types"]`

Attribution rules per error code:

| Error code | Attribution |
|---|---|
| `UNDECLARED_TYPE` | Type where the property with the undeclared type appears (scoped by which type's stitched block contains the match) |
| `DUPLICATE_FIELD` | Type where the duplicate `[JsonPropertyName]` appears |
| `MISSING_CLASS` | The expected type that has no declaration in its stitched block |
| `PHANTOM_FIELD` | Type where the extra `[JsonPropertyName]` appears |
| `STRUCTURAL` | Type where brace imbalance is detected |
| `ARTIFACT` | Type where the artifact pattern matches |

### Auto-retry loop in `pipeline.py`

After generation completes, if `auto_retry=True` (default):

```python
for attempt in range(max_retries):
    results_by_type = validate_by_type(all_page_entries, packet)
    failing = {name: r for name, r in results_by_type.items() if r.has_errors}
    if not failing:
        break

    correction_context = {
        name: [f"[{i.code}] {i.message}" + (f"\n    {i.detail}" if i.detail else "")
               for i in result.errors]
        for name, result in failing.items()
    }
    regen = partial_regenerate(
        output_dir,
        type_names=list(failing.keys()),
        llm_config=llm_config,
        correction_context=correction_context,
    )
    cs_code = regen.cs_code
```

---

## Staleness Detection

Stored prompts become stale when the IR changes — spec update, schema fix, or adapter change.
Stale prompts may reference field names, types, or constraints that no longer exist.

Detection: compare the `ir_hash` in `pages.json` against a fresh hash of `ir.json`.

```python
def check_staleness(pages_json: dict, ir_json: dict) -> bool:
    """Return True if pages.json was generated from a different IR than ir.json."""
    from schmith.shared.hashing import canonical_hash
    return pages_json.get("ir_hash") != canonical_hash(ir_json)
```

**Policy:** Staleness is a warning, not a hard block. The user may be doing a targeted manual
fix on a type that was not affected by the IR change. The CLI warns and prompts for confirmation
before proceeding. A `--ignore-stale` flag bypasses the check.

---

## CLI Interface

### New subcommand: `schmith regenerate`

```
schmith regenerate [OPTIONS] OUTPUT_DIR

  Regenerate one or more types in an existing output directory from stored prompts.

Options:
  --type TEXT          Type name to regenerate. May be repeated for multiple types.
                       Omit to regenerate all types.
  --page INTEGER       Page index to regenerate (1-based). Only applies when
                       --type is specified. May be repeated. Omit for all pages.
  --model TEXT         LLM model override. Stored prompts are submitted to this
                       model instead of the original.
  --from-errors        Regenerate only types that have validation errors in the
                       current output. Reads validation summary from ir.json.
  --dry-run            Show what would be regenerated without submitting any calls.
  --ignore-stale       Skip staleness check and proceed even if IR has changed.
  --correction TEXT    Additional correction text prepended to page-1 prompts.
                       Rarely needed manually; primarily used by the auto-retry path.

Examples:
  # Regenerate a single type
  schmith regenerate output/GET_rest_v1.1_projects --type ExtendedFlag

  # Regenerate a specific page of a type
  schmith regenerate output/GET_rest_v1.1_projects --type Project --page 3

  # Regenerate all types that currently have validation errors
  schmith regenerate output/GET_rest_v1.1_projects --from-errors

  # Re-run all prompts through a different model
  schmith regenerate output/GET_rest_v1.1_projects --model claude-opus-4-6

  # Dry-run: see what would be submitted
  schmith regenerate output/GET_rest_v1.1_projects --type Project --dry-run
```

### Updated subcommand: `schmith validate`

```
schmith validate [OPTIONS] OUTPUT_DIR

  Run validation against an existing output directory.

Options:
  --by-type    Report errors grouped by type instead of a flat list.

Examples:
  schmith validate output/GET_rest_v1.1_projects
  schmith validate output/GET_rest_v1.1_projects --by-type
```

`schmith validate` reads `pages.json` and `ir.json` from the output directory, re-stitches each
type from page outputs, runs validation, and updates the validation summary in `ir.json`. It does
not call any LLM and does not read the `.cs` file.

---

## Model Switching Semantics

The prompt encodes the complete intent for a page: the instruction set, the type's field slice,
the paging context, and the type reference list. None of this depends on the model.

When resubmitting stored prompts to a different model:

- The field slice is the same (it was calibrated for the original model but is descriptive, not
  prescriptive — the `Fields in this page: 6` line is informational)
- The new model's tokenizer may handle the same text slightly differently, but modern models
  at these prompt sizes (1,500–4,000 tokens) are well within reliable instruction-following range
- The output is independent of the original model's output — it is a fresh generation, not a
  continuation or edit

**What model switching does not do:** recalibrate page boundaries. If model A generated 3 pages
for a type and you resubmit to model B, you get 3 pages of output from B. If B is dramatically
better with a larger context, those gains are not realized through partial regeneration — they
require a full re-generation from the IR with recalibrated pages. This is by design: partial
regeneration is for targeted fixes, not wholesale recalibration.

---

## Implementation Sequencing

This system has a natural build order based on dependencies:

| Step | Deliverable | Depends on |
|---|---|---|
| 1 | `assembly.py` with `stitch_type_pages` (moved from `llm.py`) and `assemble_from_pages` | Nothing |
| 2 | Update `_generate_paginated` to collect page entries and use `assemble_from_pages` | Step 1 |
| 3 | `pages.json` writer in `cli.py` | Step 2 |
| 4 | `validate_by_type` in `validation.py` (uses pages entry list, no .cs reading) | Step 1 |
| 5 | `partial_regenerate` in `pipeline.py` | Steps 1, 3, 4 |
| 6 | Auto-retry loop in `pipeline.py` `run()` | Steps 4, 5 |
| 7 | `schmith regenerate` CLI subcommand | Step 5 |
| 8 | `schmith validate` CLI subcommand | Step 4 |
| 9 | Staleness detection | Steps 3, 5 |

Steps 1–3 are entirely backward-compatible: the `.cs` output content is unchanged (same assembly
logic, same type ordering), and `pages.json` begins to be written. No existing behaviour changes.

Steps 4–6 add the validation-driven retry loop. This is the highest-value change for output
quality and can be implemented without the CLI interface (the auto-retry fires internally during
`schmith generate`).

Steps 7–9 add the manual interface and are independent of each other.

---

## Test Coverage

| Module | Tests |
|---|---|
| `assembly.py` | `test_assembly.py` — `stitch_type_pages` (moved), `assemble_from_pages` with single type, multiple types, multi-page type, ordering preserved from first occurrence |
| `validation.py` (by-type) | Extension of `test_validation.py` — errors attributed to correct type block; root type errors vs nested type errors |
| `pipeline.py` (partial regen) | Integration test with `DryRunProvider` — verify `pages.json` is updated, `.cs` is reassembled from updated pages, unchanged types are unchanged in output |
| `pipeline.py` (auto-retry) | Mock provider that returns invalid code on attempt 1, valid on attempt 2 — verify retry fires and correction block is injected |
| `cli.py` (regenerate) | CLI invocation test with output fixture directory |
