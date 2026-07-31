#!/usr/bin/env bash
# Run schmith validate on every DataObject in the output directory.
# Directories whose .cs file contains only dry-run placeholders are skipped.
#
# Usage:
#   ./validate.sh                  # validate all real output dirs
#   ./validate.sh --fail-on-errors # exit 1 if any errors found (useful in CI)
#
set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
OUTPUT_DIR="$PROJECT_DIR/output"

if [ ! -d "$OUTPUT_DIR" ]; then
  echo "No output directory found at $OUTPUT_DIR" >&2
  exit 1
fi

# Returns true if the directory contains a .cs file with real C# content
# (i.e. at least one public class/enum/record declaration).
has_real_code() {
  local dir="$1"
  local cs
  cs="$(find "$dir" -maxdepth 1 -name "*.cs" | head -1)"
  [ -n "$cs" ] && grep -q "^\s*public\s" "$cs"
}

targets=()
skipped=()
for d in "$OUTPUT_DIR"/*/; do
  [ -d "$d" ] || continue
  if has_real_code "$d"; then
    targets+=("$d")
  else
    skipped+=("$(basename "$d")")
  fi
done

if [ ${#skipped[@]} -gt 0 ]; then
  echo "Skipping ${#skipped[@]} dry-run output(s): ${skipped[*]}"
fi

if [ ${#targets[@]} -eq 0 ]; then
  echo "No real generated DataObjects found in $OUTPUT_DIR (run without --dry-run to generate code)" >&2
  exit 1
fi

echo "Validating ${#targets[@]} DataObject(s) in $OUTPUT_DIR"

env -u VIRTUAL_ENV uv run --project "$PROJECT_DIR" schmith validate "${targets[@]}" "$@"
