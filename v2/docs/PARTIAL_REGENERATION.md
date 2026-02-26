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
The final `.cs` file is derived from outputs by stitching and assembly — it is never the primary
source of truth.

**Assembly:** The process of combining page outputs into a stitched type block, then combining
all type blocks into the final `.cs` file. Assembly is deterministic given the page outputs.

---

## Artifact Model

Every generation run produces five artifacts in the output directory:

```
output/{EndpointLabel}/
  {DataObjectName}.cs     # final assembled .cs — includes SCHMITH type markers
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

---

## Type Boundary Markers

The final `.cs` file is currently a flat join of all type outputs. To support precise type block
extraction and replacement without fragile regex over the C# AST, each type's block is wrapped
with lightweight comment markers:

```csharp
// [SCHMITH:BEGIN ProjectDataObject]
/// <summary>
/// A project.
/// </summary>
[PrimaryKey("id", nameof(Id))]
public class ProjectDataObject
{
    ...
}
// [SCHMITH:END ProjectDataObject]

// [SCHMITH:BEGIN ExtendedFlag]
[JsonConverter(typeof(JsonStringEnumConverter))]
public enum ExtendedFlag
{
    ...
}
// [SCHMITH:END ExtendedFlag]
```

These markers are C# line comments — valid C#, ignored by the compiler, survive reformatting.
The `type_name` in the marker matches the `type_name` in `pages.json` exactly.

The markers are added by the assembly step after stitching each type, before joining all types
into the final `.cs`. They do not appear in individual page outputs stored in `pages.json`.

---

## Assembly Module

A new module `v2/schmith/assembly.py` owns all operations that combine or decompose the final
`.cs` file. It is imported by `pipeline.py` (generation) and by the regeneration path.

### Operations

```python
MARKER_BEGIN = "// [SCHMITH:BEGIN {name}]"
MARKER_END   = "// [SCHMITH:END {name}]"


def wrap_type_block(type_name: str, code: str) -> str:
    """Wrap a stitched type block with SCHMITH boundary markers."""


def extract_type_block(cs_code: str, type_name: str) -> str | None:
    """Return the code between SCHMITH markers for type_name, or None if absent."""


def replace_type_block(cs_code: str, type_name: str, new_code: str) -> str:
    """Replace the marked block for type_name with new_code.

    Raises ValueError if the type is not found in cs_code.
    """


def list_type_names(cs_code: str) -> list[str]:
    """Return type names in marker order from cs_code."""


def assemble_cs(type_outputs: list[tuple[str, str]]) -> str:
    """Combine stitched type outputs into a final .cs file.

    Args:
        type_outputs: List of (type_name, stitched_code) pairs in generation order.

    Returns:
        .cs content with SCHMITH markers around each type block.
    """


def stitch_and_assemble(
    all_type_pages: list[tuple[str, bool, list[str]]]
) -> str:
    """Stitch pages for each type, then assemble into the final .cs.

    Args:
        all_type_pages: List of (type_name, is_root, page_outputs) tuples
            in generation order.
    """
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
all_type_pages.append((type_entry["name"], is_root, page_outputs_for_this_type))
...
cs_code = assemble_cs([
    (name, stitch_type_pages(pages))
    for name, _, pages in all_type_pages
])
return cs_code, prompt_log, all_type_pages   # all_type_pages flows to pages.json writer
```

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
        output_dir: Directory containing prompts.json, pages.json, and .cs file.
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
load pages.json    → page_store: PageStore

for each target (type_name, page_index):
    prompt = prompt_entries.find(type_name, page_index)
    user_text = prompt["user"]

    if correction_context and page_index == 1 and type_name in correction_context:
        user_text = build_correction_block(correction_context[type_name]) + "\n\n" + user_text

    new_output = provider.generate(user_text, system=prompt["system"])
    page_store.update(type_name, page_index, new_output, model=provider.model)

# Re-stitch affected types
for each affected type_name:
    page_outputs = page_store.all_pages_for_type(type_name)   # in page order
    new_stitched = stitch_type_pages(page_outputs)
    cs_code = replace_type_block(cs_code, type_name, new_stitched)

write updated pages.json
write updated .cs
run validate_generated_code(cs_code, packet)
return PartialRegenResult(...)
```

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
errors must be attributed to specific types. The SCHMITH markers make this straightforward.

New function in `validation.py`:

```python
def validate_by_type(
    cs_code: str,
    packet: dict[str, Any],
) -> dict[str, ValidationResult]:
    """Run validation per type block and return a map of type_name → result.

    Uses SCHMITH markers to extract each type's block before validating.
    Falls back to full-file validation if markers are absent.
    """
```

Attribution rules per error code:

| Error code | Attribution |
|---|---|
| `UNDECLARED_TYPE` | Type block where the property with the undeclared type appears |
| `DUPLICATE_FIELD` | Type block where the duplicate `[JsonPropertyName]` appears (already scoped by `_check_duplicate_json_properties`) |
| `MISSING_CLASS` | The expected type (from packet) that has no declaration in its block |
| `PHANTOM_FIELD` | Type block where the extra `[JsonPropertyName]` appears |
| `STRUCTURAL` | Type block where brace imbalance is detected |
| `ARTIFACT` | Type block where the artifact pattern matches |

### Auto-retry loop in `pipeline.py`

After generation completes, if `auto_retry=True` (default):

```python
for attempt in range(max_retries):
    results_by_type = validate_by_type(cs_code, packet)
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

`schmith validate` reads the `.cs` and `ir.json` from the output directory, re-runs validation,
and updates the validation summary in `ir.json`. It does not call any LLM.

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
| 1 | `assembly.py` with `wrap_type_block`, `extract_type_block`, `replace_type_block`, `assemble_cs` | Nothing |
| 2 | Update `_generate_paginated` to use `assemble_cs` and emit markers | Step 1 |
| 3 | `pages.json` writer in `cli.py` (collect page outputs in `_generate_paginated`, write alongside prompts.json) | Step 2 |
| 4 | `validate_by_type` in `validation.py` | Step 1 |
| 5 | `partial_regenerate` in `pipeline.py` | Steps 1, 3, 4 |
| 6 | Auto-retry loop in `pipeline.py` `run()` | Steps 4, 5 |
| 7 | `schmith regenerate` CLI subcommand | Step 5 |
| 8 | `schmith validate` CLI subcommand | Step 4 |
| 9 | Staleness detection | Steps 3, 5 |

Steps 1–3 are entirely backward-compatible and can be done first. The generated `.cs` gains
SCHMITH markers (which are valid C# comments), and `pages.json` begins to be written. No
existing behaviour changes.

Steps 4–6 add the validation-driven retry loop. This is the highest-value change for output
quality and can be implemented without the CLI interface (the auto-retry fires internally during
`schmith generate`).

Steps 7–9 add the manual interface and are independent of each other.

---

## Test Coverage

| Module | Tests |
|---|---|
| `assembly.py` | `test_assembly.py` — `wrap/extract/replace_type_block`, round-trip, missing type error, multiple types, nested enum markers |
| `validation.py` (by-type) | Extension of `test_validation.py` — errors attributed to correct type block |
| `pipeline.py` (partial regen) | Integration test with `DryRunProvider` — verify pages.json is updated, .cs type block is replaced, markers present |
| `pipeline.py` (auto-retry) | Mock provider that returns invalid code on attempt 1, valid on attempt 2 — verify retry fires and correction block is injected |
| `cli.py` (regenerate) | CLI invocation test with output fixture directory |
