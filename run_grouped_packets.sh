#!/usr/bin/env bash
set -euo pipefail

ir_name="${1:-}"
if [[ -z "$ir_name" ]]; then
  echo "Usage: $(basename "$0") <ir_name> [--schema NAME] [--show-groups] [--dry-run]" >&2
  exit 1
fi

shift
uv run python generate_grouped_packets.py "$ir_name" "$@"
