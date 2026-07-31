"""Typed DTO for a single page's LLM output within a generation run.

``PageEntry`` is the atomic record stored in ``pages.json``.  Each entry
captures the raw extracted C# code produced by one LLM call, together with
enough provenance metadata to replay or trace the call later.

This module intentionally has no imports from other schmith modules so it can
be imported without triggering the full pipeline dependency chain.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from typing import Any


@dataclass(frozen=True, slots=True)
class PageEntry:
    """Immutable record of one LLM page call within a generation run.

    Attributes:
        index:         Global sequential position in the run (0-based).
        type_name:     Name of the C# type this page contributes to.
        is_root:       True when this is the root DataObject type.
        page:          1-based page number within this type's call sequence.
        total_pages:   Total pages planned for this type.
        model:         LLM model identifier (e.g. ``claude-haiku-4-5-20251001``).
        generated_at:  UTC timestamp of the LLM call.
        output:        Extracted C# code returned by the LLM for this page.
        input_tokens:  Prompt token count reported by the API, if available.
        output_tokens: Completion token count reported by the API, if available.
    """

    index: int
    type_name: str
    is_root: bool
    page: int
    total_pages: int
    model: str
    generated_at: datetime
    output: str
    input_tokens: int | None = None
    output_tokens: int | None = None


def page_entry_to_dict(entry: PageEntry) -> dict[str, Any]:
    """Serialize a PageEntry to a JSON-compatible dict.

    ``generated_at`` is emitted as an ISO 8601 string with UTC suffix.
    ``None`` token fields are included so the structure is stable for
    forward-compatible deserialization.
    """
    d = asdict(entry)
    dt: datetime = d["generated_at"]
    d["generated_at"] = dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    return d


def utcnow() -> datetime:
    """Return the current UTC time as a timezone-aware datetime."""
    return datetime.now(tz=timezone.utc)
