# SpecBridge CLI Reference

## Synopsis

```
specbridge METHOD PATH [options]
specbridge validate DIR [DIR ...] [--fail-on-errors]
```

---

## Generate subcommand

Generates a C# DataObject for one endpoint and writes output artifacts to disk.

### Usage

```bash
specbridge GET /customers
specbridge GET /customers/{id}
specbridge POST /jobs --status 201
specbridge GET /customers --dry-run
specbridge GET /customers --config path/to/config.yaml
specbridge GET /customers --debug
```

### Positional arguments

| Argument | Description |
|---|---|
| `METHOD` | HTTP method — `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, etc. Case-insensitive. |
| `PATH` | Endpoint path template exactly as it appears in the spec, e.g. `/customers/{id}`. |

### Flags

| Flag | Default | Description |
|---|---|---|
| `--config FILE` | `config.yaml` | Path to the YAML config file. Resolved relative to the working directory. |
| `--status CODE` | `200` | Preferred response status code. If the spec has no response at this code, falls back to the numerically lowest 2xx response that has a schema. |
| `--dry-run` | off | Skip all LLM calls. Runs the spec parsing, type-tree resolution, and prompt construction pipeline, then writes output artifacts with placeholder code. Useful for verifying spec parsing without spending tokens. |
| `--debug` | off | Run pipeline invariant checks after each stage. Raises `InvariantViolation` and prints a detailed trace on structural problems. |

### Config file

All generation behaviour is controlled by `config.yaml` (or the file passed via `--config`). The full config shape:

```yaml
api:
  spec: path/to/api_spec.json   # required — OpenAPI JSON/YAML or RAML file
  format: openapi               # openapi | openapi3 | swagger | oas | raml
  adapter: null                 # optional — dotted Python path to an ApiAdapter subclass

llm:
  provider: anthropic           # anthropic | openai
  model: null                   # optional model override (see defaults below)
  api_key: null                 # optional — falls back to env var (see below)
  dry_run: false                # alternative to --dry-run flag
  target_input_tokens: 3500     # token budget per LLM call; prompt pages are sized to fit
  min_page_size: 5              # minimum fields per page regardless of token budget

output:
  dir: output                   # directory where output folders are created

codegen:
  fields_per_page: null         # override calibrated page size for object fields
  enum_values_per_page: 30      # max enum values per LLM call
  max_retries: 2                # retry attempts per type when validation finds errors
```

#### `api` section

| Key | Required | Description |
|---|---|---|
| `spec` | yes | Path to the API spec. Absolute or relative to the working directory. Supports `.json`, `.yaml`, `.yml`, `.raml`. |
| `format` | no | `openapi` (default), `openapi3`, `swagger`, `oas`, `raml`. All OpenAPI variants behave identically; use `raml` for RAML specs. |
| `adapter` | no | Dotted Python import path to an `ApiAdapter` subclass, e.g. `mypackage.adapters.ProcoreAdapter`. If absent or `null`, the base pass-through adapter is used. |

#### `llm` section

| Key | Required | Description |
|---|---|---|
| `provider` | no | `anthropic` (default) or `openai`. |
| `model` | no | Model identifier. Defaults: Anthropic → `claude-3-5-haiku-20241022`, OpenAI → `gpt-5-mini-2025-08-07`. |
| `api_key` | no | API key. Falls back to `ANTHROPIC_API_KEY` or `OPENAI_API_KEY` environment variables. |
| `dry_run` | no | Same effect as `--dry-run`. The CLI flag always overrides this to `true` when passed. |
| `target_input_tokens` | no | Token budget per LLM call (default `3500`). The pipeline probes each type's full field list and splits it into pages that stay within this limit. Larger values send more fields per call (fewer total calls); smaller values produce smaller prompts. |
| `min_page_size` | no | Minimum fields per page (default `5`). Even when token budget is very tight, no page will have fewer fields than this. Prevents degenerate single-field pages on unusually verbose schemas. |

#### `output` section

| Key | Required | Description |
|---|---|---|
| `dir` | no | Base directory for all output folders (default `output`). Each run creates a subdirectory named `<METHOD>_<path-slug>`. |

#### `codegen` section

| Key | Required | Description |
|---|---|---|
| `fields_per_page` | no | Hard override for object fields per page. When set, bypasses token-based calibration entirely. Useful for reproducible, deterministic page layouts. |
| `enum_values_per_page` | no | Max enum values per LLM call (default `30`). Large enums are split and stitched the same way as large object types. |
| `max_retries` | no | Maximum retry attempts per type when per-type validation finds errors (default `2`). On each retry, the validation errors are injected back into the prompt as a `CORRECTION REQUIRED` block. Set to `0` to disable retries. |

#### Environment variables

| Variable | Provider | Description |
|---|---|---|
| `ANTHROPIC_API_KEY` | Anthropic | Used when `llm.api_key` is absent and provider is `anthropic`. |
| `OPENAI_API_KEY` | OpenAI | Used when `llm.api_key` is absent and provider is `openai`. |

### Output artifacts

Each run writes one directory:

```
output/<METHOD>_<path-slug>/
  <Name>DataObject.cs    ← generated C# code (derived from pages.json)
  ir.json                ← IR: endpoint metadata, type closure, validation summary
  schema.md              ← human-readable type closure for review
  codegen/
    prompts.json         ← exact system+user prompt for every LLM call
    pages.json           ← raw LLM output per page (source of truth for the .cs)
  pii/                   ← written only when the PII pre-pass runs
    prompts.json         ← classification prompt per field batch
    pages.json           ← raw classification output per batch
```

The path slug is the endpoint path with `/` replaced by `_` and path parameters kept verbatim:

```
GET /customers          → output/GET_customers/
GET /customers/{id}     → output/GET_customers_{id}/
POST /jobs/assignments  → output/POST_jobs_assignments/
```

#### `ir.json`

Intermediate representation snapshot. Contains the resolved type closure and a validation summary. Written without the `prompts` key (those go to `codegen/prompts.json`, and PII logs to `pii/`, to keep `ir.json` concise).

```json
{
  "endpoint": { "method": "GET", "path": "/customers", "status_code": "200", "schema_id": "..." },
  "root_type": { "name": "Customer", "properties": [...], ... },
  "nested_types": [...],
  "validation": {
    "is_clean": true,
    "retries": [
      { "type_name": "Customer", "total_attempts": 3, "final_clean": false, "final_errors": 1 }
    ],
    "errors": [],
    "warnings": []
  }
}
```

`validation.retries` lists every type that required more than one generation attempt. An empty list means all types were generated cleanly on the first try. Each entry records how many attempts were made (`total_attempts`), whether the final attempt passed validation (`final_clean`), and how many errors remained (`final_errors`). Types with `final_clean: false` indicate persistent LLM hallucinations that survived all retries — their code should be reviewed manually.

The `validation.is_clean` field reflects the **post-assembly** validation result. Individual per-type retry results are not stored here.

#### `schema.md`

Markdown summary of the root type and all nested types — field names, resolved C# types, schema IDs, enum values. Intended for human review before code review.

#### `codegen/prompts.json`

A flat JSON array. Each entry is one LLM call, in generation order. On retry, only the **final** successful (or last) attempt's prompts are stored.

```json
[
  {
    "type_name": "Customer",
    "is_root": true,
    "page": 1,
    "total_pages": 2,
    "system": "You are a C# code generator ...",
    "user": "============================================================\nENDPOINT: GET /customers\n..."
  },
  ...
]
```

Useful for debugging hallucinations: if a type has the wrong field name or type, compare the `user` prompt for that page to the generated `.cs`.

#### `codegen/pages.json`

Authoritative source for the `.cs` file. The `.cs` is always reconstructable from this file by running `assemble_from_pages`.

```json
{
  "version": 1,
  "endpoint": { "method": "GET", "path": "/customers" },
  "ir_hash": "sha1:a3f9...",
  "pages": [
    {
      "index": 0,
      "type_name": "Customer",
      "is_root": true,
      "page": 1,
      "total_pages": 2,
      "model": "claude-3-5-haiku-20241022",
      "generated_at": "2026-02-25T10:30:05Z",
      "output": "public class CustomerDataObject\n{\n    ...",
      "input_tokens": 1420,
      "output_tokens": 312
    },
    ...
  ]
}
```

`ir_hash` is a SHA-1 of `ir.json`. It changes whenever the spec or type tree changes, making it easy to detect stale `codegen/pages.json` files. `input_tokens` and `output_tokens` are populated from the API's usage response; both are `null` for dry-run.

### Exit codes

| Code | Meaning |
|---|---|
| `0` | Success. Output written. |
| `1` | Error: spec not found, endpoint not matched, adapter load failed, or unexpected pipeline error. |

Note: validation errors in the generated code do **not** cause a non-zero exit from the generate command. Use `specbridge validate --fail-on-errors` in CI to gate on validation results.

---

## Validate subcommand

Runs deterministic checks on previously generated DataObjects — no LLM required.

### Usage

```bash
# Single directory
specbridge validate output/GET_customers/

# Multiple directories (shell glob expansion supported)
specbridge validate output/GET_*/

# All subdirectories
specbridge validate output/

# Exit 1 if any errors found (CI mode)
specbridge validate output/ --fail-on-errors

# Pass a .cs file directly (ir.json resolved from the same directory)
specbridge validate output/GET_customers/CustomerDataObject.cs
```

### Arguments

| Argument | Description |
|---|---|
| `DIR [DIR ...]` | One or more output directories or `.cs` files. Shell glob patterns expand naturally (`output/GET_*`). Each directory must contain both an `ir.json` and at least one `.cs` file. |

### Flags

| Flag | Description |
|---|---|
| `--fail-on-errors` | Exit with status `1` if any validation target has errors. Without this flag, the command always exits `0` and results are printed to stderr only. |

### Validation checks

| Code | Severity | What it checks |
|---|---|---|
| `STRUCTURAL` | error | Brace balance: `{` count equals `}` count in the full `.cs`. |
| `ARTIFACT` | error | Template placeholders (`%{...}`), stitching markers (`// BEGIN_FIELDS`, `// END_FIELDS`) left in the output. |
| `ARTIFACT` | warning | Raw schema IDs leaked into the code (e.g. `schema:components/...`). |
| `MISSING_CLASS` | error | A type expected from the IR has no `public class`, `public enum`, or `public record` declaration. |
| `MISSING_FIELD` | warning | A field present in the IR schema has no `[JsonPropertyName("...")]` attribute in the generated code. |
| `PHANTOM_FIELD` | warning | A `[JsonPropertyName("...")]` attribute references a field name not present in the IR schema. May indicate a hallucinated field. |
| `DUPLICATE_FIELD` | error | The same `[JsonPropertyName("...")]` value appears more than once within the same class block. Causes silent deserialization bugs. |
| `UNDECLARED_TYPE` | error | A property declaration references a C# type not declared anywhere in the file and not a known primitive. Typically indicates a hallucinated type name. |

Checks run against both the `.cs` file and `ir.json`. No network calls are made.

### Exit codes

| Code | Meaning |
|---|---|
| `0` | All targets processed. (Use `--fail-on-errors` to distinguish clean from error results.) |
| `1` | `--fail-on-errors` was set and at least one target had validation errors; or a target path could not be resolved. |

---

## Common patterns

### Preview before spending tokens

```bash
specbridge GET /customers --dry-run
```

Parses the spec, resolves the type tree, builds all prompts, and writes `ir.json`, `schema.md`, `codegen/prompts.json`, and a placeholder `.cs` — without calling the LLM. Check `schema.md` and `codegen/prompts.json` to verify the type closure looks correct before running the real generation.

### Debug spec parsing problems

```bash
specbridge GET /customers --dry-run --debug
```

`--debug` runs pipeline invariant checks after each stage. If the type tree has structural problems (disconnected schemas, missing resolved types, etc.), the invariant check will surface the issue with stage context rather than a cryptic downstream error.

### Tune prompt size

For APIs with many short field descriptions, the default `target_input_tokens: 3500` may produce more pages than necessary. Increase it to reduce call count:

```yaml
llm:
  target_input_tokens: 6000
```

For very large schemas (100+ fields per type) where you want smaller, more focused prompts:

```yaml
llm:
  target_input_tokens: 2000
  min_page_size: 3
```

### Disable retries

Set `max_retries: 0` to skip the validation-driven retry loop. Useful when you want raw first-attempt output for diagnostic purposes:

```yaml
codegen:
  max_retries: 0
```

### CI validation gate

Generate all endpoints and fail the build if any have validation errors:

```bash
# Generate
specbridge GET /customers
specbridge GET /customers/{id}
specbridge POST /jobs --status 201

# Gate
specbridge validate output/ --fail-on-errors
```

### Use a different model

```yaml
llm:
  provider: anthropic
  model: claude-opus-4-6
```

```yaml
llm:
  provider: openai
  model: gpt-5-2025-09-12
```

---

## Error messages

| Message | Cause |
|---|---|
| `Error: config file not found: config.yaml` | No `config.yaml` in the working directory. Either create one or pass `--config path/to/config.yaml`. |
| `Error: config.yaml must set api.spec` | The `api.spec` key is missing from the config. |
| `Spec load error: Spec file not found: ...` | The path in `api.spec` does not exist. |
| `Endpoint not found: No operation found matching GET /path` | The spec has no operation matching that method + path. Run with `--dry-run --debug` to see which operations were found. |
| `Endpoint not found: Operation found ... but no 2xx response has a schema_id` | The operation exists but has no response schema. The endpoint may be write-only or return only status codes. |
| `Error loading adapter '...': ...` | The dotted Python path in `api.adapter` could not be imported. Check the path is importable from the working directory. |
| `Anthropic API key required. Set ANTHROPIC_API_KEY ...` | Neither `llm.api_key` nor the `ANTHROPIC_API_KEY` environment variable is set. |
| `OpenAI API key required. Set OPENAI_API_KEY ...` | Neither `llm.api_key` nor the `OPENAI_API_KEY` environment variable is set. |
| `Unknown LLM provider 'xyz'` | `llm.provider` is set to an unsupported value. Supported: `anthropic`, `openai`. |
| `Pipeline invariant violated: ...` | Only with `--debug`. A structural invariant failed between pipeline stages. The message identifies the stage and the violated condition. |
