#!/usr/bin/env bash
set -euo pipefail

CONFIG_PATH="${1:-configs/ukg_v2_client.toml}"
ADAPTER="${2:-openapi}"

echo "Demo: building IR from config: ${CONFIG_PATH} (adapter: ${ADAPTER})"
echo "Step 1/4: operations"
uv run python builders/build_operations.py --config "${CONFIG_PATH}" --adapter "${ADAPTER}"

echo "Step 2/4: schemas"
uv run python builders/build_schemas.py --config "${CONFIG_PATH}" --adapter "${ADAPTER}"

echo "Step 3/4: serialization"
uv run python builders/build_serialization.py --config "${CONFIG_PATH}" --adapter "${ADAPTER}"

echo "Step 4/4: refs"
uv run python builders/build_refs.py --config "${CONFIG_PATH}"

echo "Done."
