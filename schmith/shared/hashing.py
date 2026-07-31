"""Canonical JSON hashing for schema identification."""

import hashlib
import json
from typing import Any


def canonical_json_hash(payload: Any) -> str:
    """Generate a canonical SHA1 hash for a JSON-serializable object.

    Uses deterministic JSON serialization (sorted keys, no whitespace)
    to ensure identical objects always produce identical hashes.

    Args:
        payload: Any JSON-serializable object.

    Returns:
        A 40-character hexadecimal SHA1 hash string.
    """
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha1(canonical.encode("utf-8")).hexdigest()
