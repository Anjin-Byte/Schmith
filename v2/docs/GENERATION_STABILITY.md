# Generation Stability — Problem Analysis and Implementation Plan

## Overview

Schmith v2 generates C# DataObject classes by decomposing each endpoint's type closure into a
series of LLM calls, stitching the results back together, and running a deterministic validator
over the output. The pipeline is structurally sound: the IR is accurate, the validator catches
real errors, and the stitching logic handles marker extraction correctly.

What remains is a category of output quality problems where the LLM produces code that deviates
from what the prompt specifies — using wrong type names, inventing fields, or generating
structurally inconsistent blocks across pages. This document categorizes those failure modes,
explains the root cause of each, and specifies concrete implementation changes.

---

## Problem Taxonomy

Failures in the generated output fall into four categories, ordered by frequency and severity.

### Category 1 — IR-to-Prompt Fidelity Gaps

**Definition:** The IR has correct information, but that information is not accurately reflected in
the prompt the LLM receives. The LLM then generates code that correctly follows the (wrong) prompt.

**This is not hallucination.** The LLM is doing exactly what it was told. The fault is upstream.

**Observed instance:** `FlagEnum` in `ProjectDataObject.cs`. The IR had `resolved_type:
"ExtendedFlag"` on the `flag` property. `build_field_info` ignored `resolved_type` for enum
properties and re-derived the name from `name_hint`, which was absent on the anonymous inline
schema, falling back to `f"{csharp_name}Enum"` → `FlagEnum`. The prompt said `FlagEnum`, the
LLM generated `FlagEnum`, the validator did not catch it. Fixed by prioritising `resolved_type`
in `build_field_info` and adding the `UNDECLARED_TYPE` validator check.

**Remaining exposure:**
- `type_unresolved` fields: passed to the LLM as `object` with a `// [REVIEW]` comment and no
  further information. The LLM has nothing to work with and may invent a plausible-sounding type.
- Composition schemas (`allOf`, `oneOf`): flattening during IR construction can silently discard
  discriminator context, producing fields with ambiguous or collapsed types.
- Anonymous nested schemas at depth > 1: `build_field_info` only has `name_hint` from the
  original spec; names assigned by `type_tree.py` during traversal may not propagate.

**Diagnostic signal:** A `// [REVIEW: Type unresolved from IR]` comment in the generated `.cs`
file is a reliable indicator of a fidelity gap. These should be logged and tracked per run.

---

### Category 2 — Cross-Page Context Drift

**Definition:** Information provided on one LLM call is unavailable to subsequent calls for the
same type. The LLM "forgets" what was established earlier and produces inconsistent output.

**Root cause:** The NESTED TYPES hint — the list of type names the LLM should use for complex
fields — is only emitted on root page 1. A type with N pages generates N−1 continuation calls
that have `OUTPUT MODE: fields_only` and `CLASS: <name>` but no list of available type names. On
page 6 of 8, when the LLM reaches a field whose type is `SchedulingShift2DataObject`, it has no
anchor to that exact name and may drift.

**Current prompt structure for a continuation page:**

```
Generate a C# Trimble XChange DataObject...
[12 lines of instructions]

OUTPUT MODE: fields_only
- Return ONLY the property blocks for this page.
...

============================================================
ENDPOINT: GET /rest/v1.1/projects/{id}
CLASS: Extended
============================================================
Schema ID: schema:components/Extended
Description: No description

PAGING:
  Page: 6 of 8
  Fields in this page: 6
  Total fields: 59
  All field names: id, name, flag, ...

FIELDS (this page):
...
```

The LLM has the full field name list (`All field names:`) but not the corresponding type names for
complex fields. A field named `schedule` could resolve to `Schedule2DataObject` or `SchedulingShift`
or `ProjectScheduleDataObject` — the LLM cannot know without the nested types list.

---

### Category 3 — Page Size Miscalibration

**Architectural constraint:** Each type in the type closure — the root object, every nested
object, every referenced enum — always gets its own dedicated LLM call (or series of calls if
it is large). Types are never merged into a shared call. This boundary is load-bearing: it keeps
each prompt focused on one coherent type, gives the LLM a single clear task, and makes
stitching tractable. The calibration problem is therefore bounded to *how many fields of a
single type per page*, not whether to combine types.

**Definition:** The current page size of 6 fields per page is a uniform constant applied to
every type regardless of its actual complexity. A type with 3 short-named fields uses the same
page size as a type with 59 richly-described fields. This produces:
- Unnecessary splits for simple types (a 3-field helper gets 1 call, correct, but the constant
  would split it at 6 if it ever grew)
- Excessive splits for complex types (the 59-field `Extended` type generates 10 calls; at
  20 fields per page it would be 3)

**Current constant:** `MAX_FIELDS_PER_PAGE = 6` in `prompt.py`.

**Analysis of the 59-field case at current page size:**

- 1 call produces the class declaration with fields 1–6 (`full_class` or `class_only`)
- 9 calls produce `fields_only` blocks, each relying on marker extraction to stitch correctly

Each `fields_only` call is a potential stitching failure point. The marker protocol
(`// BEGIN_FIELDS` / `// END_FIELDS`) adds another failure mode: if the LLM omits or moves the
markers, extraction falls back to the full response, which can introduce noise.

At 20 fields per page, the same type requires 3 calls. The cross-page risk surface is reduced
by 70%. The conservative 6-field limit was set to avoid LLM attention degradation on large
prompts. However, with modern context windows and Claude's architecture, attention degradation
for 20–30 structured fields is not a significant concern. The prompt for 20 fields is roughly
600–800 tokens — well within the range where instruction-following is reliable.

**The deeper problem with a uniform constant:** It cannot adapt to schema density. A type where
every field has a long description, constraints, and enum values is an order of magnitude denser
than one with bare field names. The right page size for a dense type is smaller; the right page
size for a sparse type is larger. A uniform constant optimises for neither.

**Token-based calibration** (see Impl-2b) replaces the constant with per-type measurement.

**Enum page size:** `MAX_ENUM_VALUES_PER_PAGE = 30` is well-calibrated. Enum values are
single-token decisions; the LLM can handle much larger pages without degradation. 50–60 values
per page is reasonable for large enums.

---

### Category 4 — Stochastic Output Variance

**Definition:** The same prompt, sent twice, produces different output. This is inherent to
temperature > 0 LLM calls. For code generation where we want deterministic, spec-driven output,
variance is pure noise.

**Current state:** Temperature is not configured; the provider default applies. For most Claude
API configurations this is in the 0.5–1.0 range.

**Effect:** At temperature 1.0, the LLM may choose `CustomerId` for a field named `customer_id`
in one run and `CustomerID` in another. At temperature 0.0, the output for a given prompt is
deterministic. For code generation, determinism is desirable.

---

## Implementation Specifications

### Impl-1: Repeat NESTED TYPES on All Continuation Pages

**File:** `v2/schmith/generation/prompt.py` — `build_type_page_prompt`

**Current behaviour:** NESTED TYPES hint is emitted only when `is_root and page_index == 1`.

**Required behaviour:** NESTED TYPES hint is emitted on every page where `nested_types` is
non-empty, regardless of page index.

The hint text for continuation pages should be slightly different to avoid implying the LLM
should place the class declaration here:

```python
# Page 1 (establishes context):
"NESTED TYPES: TypeA, TypeB, TypeC"
"Use these class names for complex field types. Do NOT generate them here."

# Pages 2+ (reminder only):
"TYPE REFERENCE (use exact names): TypeA, TypeB, TypeC"
```

**Change in `build_type_page_prompt`:**

```python
# Before (current):
if is_root and page_index == 1 and nested_types:
    nested_names = [nt["name"] for nt in nested_types]
    lines.append(f"NESTED TYPES: {', '.join(nested_names)}")
    lines.append("Use these class names for complex field types. Do NOT generate them here.")
    lines.append("")

# After:
if nested_types:
    nested_names = [nt["name"] for nt in nested_types]
    if is_root and page_index == 1:
        lines.append(f"NESTED TYPES: {', '.join(nested_names)}")
        lines.append("Use these class names for complex field types. Do NOT generate them here.")
    else:
        lines.append(f"TYPE REFERENCE (use exact names): {', '.join(nested_names)}")
    lines.append("")
```

**Note:** This also applies to nested type continuation pages. A nested type with 8 pages of
fields should have the reference list on every page, not just page 1 of the root.

**Test additions:** Add a test to `TestBuildTypePagePrompt` verifying that nested type names
appear in the prompt for `page_index=2` and `is_root=False` continuation pages.

---

### Impl-2a: Increase Default Page Size (Quick Win)

**File:** `v2/schmith/generation/prompt.py`

**Current:**
```python
MAX_FIELDS_PER_PAGE = 6
MAX_ENUM_VALUES_PER_PAGE = 30
```

**Proposed:**
```python
MAX_FIELDS_PER_PAGE = 20
MAX_ENUM_VALUES_PER_PAGE = 50
```

These are defaults only. Both values are already overridable at the call site via
`fields_per_page` and `enum_values_per_page` parameters on `pipeline.run()`, so changing the
defaults does not remove flexibility.

**Validation:** Re-run the Project endpoint. The `Extended` type (59 fields) should reduce from
~10 calls to 3. Inspect the `fields_only` pages in the new run for correct type references.

Impl-2a is a one-line change and is worthwhile immediately. Impl-2b (below) supersedes the need
to tune this constant once it is implemented.

---

### Impl-2b: Token-Based Per-Type Page Size Calibration

**Replaces:** the hardcoded `MAX_FIELDS_PER_PAGE` constant for all production runs.

**Architectural constraint (repeated for emphasis):** Each type is always its own generation
unit. Calibration only affects how many fields of *that type* fit in a single call. Complex
nested objects and enums referenced by the root type each get their own calibrated page size —
they are never folded into the root's call.

#### Design

For each type immediately before generation, build a probe prompt containing all of its fields
and ask the provider how many tokens that prompt is. If it fits within a target budget, generate
in one call. Otherwise, divide fields into pages sized to hit the budget.

```
per type:
  probe = build_type_page_prompt(all_fields, page 1 of 1)
  n = provider.count_tokens(probe, system_prompt)
  if n ≤ TARGET_INPUT_TOKENS:
      page_size = len(all_fields)        # one call, full type
  else:
      overhead ≈ n - (tokens_per_field * len(all_fields))
      tokens_per_field = (n - overhead) / len(all_fields)
      page_size = max(MIN_PAGE, int(TARGET_INPUT_TOKENS / tokens_per_field))
```

`TARGET_INPUT_TOKENS = 3_500` is a reasonable starting point. It is well below context limits
and keeps the field section coherent without overwhelming the instruction-following budget.
`MIN_PAGE = 5` prevents degenerate single-field pages on unusually dense schemas.

This means:
- A 3-field helper type → 1 call (always fits)
- A sparse 59-field type → possibly 1 call if fields are short
- A dense 20-field type with long descriptions and constraints → 2 calls
- The same `Extended` (59 fields, moderate density) → 3 calls instead of 10

#### Protocol change: `count_tokens`

Add a `count_tokens` method to the `LLMProvider` protocol in `llm.py`:

```python
class LLMProvider(Protocol):
    def generate(self, prompt: str, system: str | None = None) -> str: ...
    def count_tokens(self, prompt: str, system: str | None = None) -> int: ...
```

Provider implementations:

**`AnthropicProvider`** — uses the native `count_tokens` endpoint (no generation, fast):
```python
def count_tokens(self, prompt: str, system: str | None = None) -> int:
    result = self.client.messages.count_tokens(
        model=self.model,
        system=system or "",
        messages=[{"role": "user", "content": prompt}],
    )
    return result.input_tokens
```

**`OpenAIProvider`** — OpenAI has no equivalent endpoint; estimate client-side:
```python
def count_tokens(self, prompt: str, system: str | None = None) -> int:
    try:
        import tiktoken
        enc = tiktoken.encoding_for_model(self.model)
        return len(enc.encode((system or "") + prompt))
    except (ImportError, KeyError):
        # Rough heuristic: 1 token ≈ 4 characters
        return len((system or "") + prompt) // 4
```

**`DryRunProvider`** — return a character-based estimate (no API needed):
```python
def count_tokens(self, prompt: str, system: str | None = None) -> int:
    return len((system or "") + prompt) // 4
```

#### Integration in `_generate_paginated` (`pipeline.py`)

Replace the fixed `_chunk_fields(fields, page_size)` call with a per-type calibration step:

```python
def _calibrate_page_size(
    packet: dict[str, Any],
    type_entry: dict[str, Any],
    is_root: bool,
    system_prompt: str,
    provider: LLMProvider,
    target_tokens: int = 3_500,
    min_page: int = 5,
    fallback: int = MAX_FIELDS_PER_PAGE,
) -> int:
    """Return the optimal fields-per-page for this type."""
    all_fields = type_entry.get("fields") or []
    if len(all_fields) <= min_page:
        return len(all_fields)  # always fits; no split needed

    # Build a probe prompt with all fields as a single page
    probe = build_type_page_prompt(
        packet, type_entry, all_fields, 1, 1, is_root
    )
    try:
        n = provider.count_tokens(probe, system_prompt)
    except Exception:
        return fallback   # count_tokens unavailable; fall back to constant

    if n <= target_tokens:
        return len(all_fields)

    # Estimate overhead from instructions + metadata (non-field tokens).
    # Probe an empty-field version to isolate overhead.
    try:
        empty_probe = build_type_page_prompt(
            packet, type_entry, [], 1, 1, is_root
        )
        overhead = provider.count_tokens(empty_probe, system_prompt)
    except Exception:
        overhead = 0

    field_tokens = max(1, n - overhead)
    tokens_per_field = field_tokens / len(all_fields)
    budget = max(0, target_tokens - overhead)
    return max(min_page, int(budget / tokens_per_field))
```

Then in the type_pages pre-computation loop, replace:
```python
pages = _chunk_fields(te.get("fields") or [], page_size)
```
with:
```python
calibrated = _calibrate_page_size(packet, te, is_root, system_prompt, provider)
pages = _chunk_fields(te.get("fields") or [], calibrated)
```

#### Usage data from generation responses

In addition to pre-generation `count_tokens`, capture actual `input_tokens` and `output_tokens`
from each generation response and add them to the `prompt_log` entry:

```python
# Extend the provider protocol (optional enhancement):
class GenerationResult(NamedTuple):
    text: str
    input_tokens: int
    output_tokens: int

# AnthropicProvider.generate returns GenerationResult instead of str
# generate_code unwraps text; pipeline logs the token counts
```

This makes token counts visible in `prompts.json` alongside each call, enabling post-run
analysis of actual vs estimated token counts and refinement of `TARGET_INPUT_TOKENS`.

#### Config exposure

```yaml
# v2/config.yaml
llm:
  target_input_tokens: 3500   # calibration budget per page
  min_page_size: 5             # minimum fields per page (avoids degenerate splits)
```

#### Tests

- `test_llm_provider_config.py`: verify `count_tokens` on `DryRunProvider` returns a positive integer
- `test_pagination.py`: add `TestCalibratePageSize` exercising the boundary conditions
  (fits in one call, needs split, count_tokens raises, empty fields)

---

### Impl-3: Validation-Driven Retry Loop

**Files:** `v2/schmith/pipeline.py`, `v2/schmith/validation.py`

**Current behaviour:** Validation runs after all code is generated and printed. Issues are
reported but not acted on. The generated `.cs` file is written regardless of validation outcome.

**Required behaviour:** If validation finds `error`-severity issues on a generated type, trigger
a targeted re-generation for that type only, with the validation findings injected into the
prompt as a correction block. Retry at most N times (default: 2).

#### Retry prompt injection

The retry prompt for a type is built from the same `build_type_page_prompt` machinery, with an
additional `CORRECTION` section prepended for page 1:

```
CORRECTION REQUIRED:
The previous attempt for this type had the following errors:
  - [UNDECLARED_TYPE] Property references type 'FlagEnum' which is not declared in this file.
    Declared types in this file: ExtendedFlag, ProjectSector, Schedule2DataObject, ...
  - [DUPLICATE_FIELD] [JsonPropertyName("id")] appears 2 times in class 'Project'.

Fix these errors in your output. Do not introduce new types not listed in NESTED TYPES.
```

#### Implementation sketch in `pipeline.py`

```python
def _regenerate_type_with_corrections(
    packet: dict[str, Any],
    type_entry: dict[str, Any],
    is_root: bool,
    issues: list[ValidationIssue],
    provider: LLMProvider,
    system_prompt: str,
    page_size: int,
    enum_page_size: int,
) -> str:
    """Re-generate a single type with validation errors injected as corrections."""
    correction_lines = [
        "CORRECTION REQUIRED:",
        "The previous attempt for this type had the following errors:",
    ]
    for issue in issues:
        correction_lines.append(f"  - [{issue.code}] {issue.message}")
        if issue.detail:
            correction_lines.append(f"    {issue.detail}")
    correction_lines.append(
        "Fix these errors. Do not introduce types not listed in NESTED TYPES / TYPE REFERENCE."
    )
    correction_block = "\n".join(correction_lines)

    # Rebuild pages for this type and regenerate.
    # Inject correction_block at the top of the page-1 prompt.
    ...
```

#### Validation scoping

The current `validate_generated_code` validates the entire stitched output as one string. For
targeted retry, we need per-type validation: validate only the code block that corresponds to
one type.

This requires splitting the stitched output by class boundaries before validating. The existing
`_CLASS_DECL_RE` pattern used by `_check_duplicate_json_properties` already does this split.
Extracting it into a helper `_split_by_class(code: str) -> dict[str, str]` would enable
per-type validation.

#### Error attribution

After splitting by class, attribution of errors to types is:
- `UNDECLARED_TYPE` — belongs to the class block where the property appears
- `PHANTOM_FIELD` — belongs to the class block where the `[JsonPropertyName]` appears
- `MISSING_CLASS` — belongs to the type that was expected but not found (from the packet)
- `DUPLICATE_FIELD` — belongs to the class block where the duplicate appears (already scoped)
- `STRUCTURAL` (unbalanced braces) — belongs to the type block where the imbalance is

**Retry termination:** After `max_retries` attempts, log remaining errors and write the best
available output. Do not silently swallow validation failures.

---

### Impl-4: Temperature Configuration

**File:** `v2/schmith/generation/llm.py` (or wherever the API client is initialised)

**Required change:** Expose `temperature` as a key in `llm_config` and pass it through to the
API call. Default to `0.2` rather than the provider default.

```python
# In get_provider or generate_code:
temperature = llm_config.get("temperature", 0.2)
```

`0.2` rather than `0.0` because pure temperature-0 can produce repetitive artifacts on very
long outputs; a small positive value preserves fluency while dramatically reducing variance.

**Config file:** `v2/config.yaml` should expose this as a user-configurable value:
```yaml
llm:
  temperature: 0.2
```

---

### Impl-5: Enrich type_unresolved Fields

**File:** `v2/schmith/generation/type_mapping.py` — `build_field_info`
**File:** `v2/schmith/generation/prompt.py` — `_format_fields_section`

**Current behaviour:** When `type_unresolved=true`, the field is emitted as:
```
field_name [→ FieldName]: object? [nullable, type_unresolved]
```

The LLM has nothing to work with and will either use `object?` (correct but lossy) or invent a
plausible type name (incorrect).

**Required change:** When a field is unresolved, attach the raw schema information to the field
dict so it can be shown in the prompt:

```python
# In build_field_info, when type cannot be resolved:
field_info["type_unresolved"] = True
field_info["raw_schema_kind"] = schema.get("kind")          # "object", "array", "string", etc.
field_info["raw_schema_id"] = schema_id                     # for traceability
field_info["raw_title"] = schema.get("title") or schema.get("name_hint")
```

In `_format_fields_section`, emit the extra context:
```
  field_name [→ FieldName]: object? [nullable, type_unresolved]
    Raw schema: kind=object, title=SomeHint  ← new
    // [REVIEW: Type unresolved — use object? or manually specify if known]
```

This gives the LLM enough signal to make an informed choice rather than guessing, and surfaces
the gap to the developer reading the schema.md artefact.

---

## Priority and Sequencing

| Priority | Change | Effort | Stability Gain |
|----------|--------|--------|---------------|
| 1 | **Impl-1** — Repeat NESTED TYPES on continuation pages | Low | High — directly prevents cross-page type name drift |
| 2 | **Impl-2a** — Increase default page size to 20 / 50 | Trivial | Medium — reduces stitching surface immediately |
| 3 | **Impl-4** — Temperature configuration | Low | Medium — eliminates stochastic variance in type/field names |
| 4 | **Impl-2b** — Token-based per-type page size calibration | Medium | Medium-High — replaces constant with per-schema-density adaptation |
| 5 | **Impl-3** — Validation-driven retry | High | High — catches and corrects remaining errors automatically |
| 6 | **Impl-5** — Enrich type_unresolved fields | Medium | Low-medium — improves worst-case quality, rare in practice |

**Sequencing rationale:**

- Impl-1 and Impl-2a can be done together in one session. Both are low-risk changes to
  `prompt.py` with no protocol changes required.
- Impl-4 (temperature) is independent and can be done in the same session as 1 and 2a — it
  is a one-line change per provider.
- Impl-2b requires the `count_tokens` protocol addition. It should be done after 2a is
  validated so the baseline prompt structure is stable.
- Impl-3 (retry loop) should be done last. It depends on per-type validation scoping
  (`_split_by_class`), which is new infrastructure, and its quality is directly affected by
  the prompt improvements from Impl-1. Implementing retry before those are in place means
  retrying against a lower-quality baseline.
- Impl-5 (unresolved field enrichment) is independent and can be slotted in anywhere.

---

## Measuring Progress

After each implementation:

1. Re-run the Project endpoint (`GET /rest/v1.1/projects`) — the highest-complexity endpoint
   observed so far (27 nested types, 59-field type, known previous errors).
2. Check `prompts.json` to confirm structural changes took effect (NESTED TYPES on page 2+,
   correct page count with new size, temperature in metadata if added).
3. Check validation output for `error`-severity findings — the target is zero errors.
4. Track `// [REVIEW]` comment count in the generated `.cs` file as a proxy for unresolved fields.

A known-good baseline can be established from the current Project run once Impl-1 and Impl-2
are in place, before adding the retry loop.
