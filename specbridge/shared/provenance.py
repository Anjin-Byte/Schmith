"""Provenance tracking for IR elements."""

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class Provenance:
    """Tracks the origin of an IR element back to the source spec.

    Attributes:
        source_file: Path to the source specification file.
        source_pointer: JSON pointer or identifier within the source file.
        via: Chain of transformations or derivations (e.g., resolved refs).
    """

    source_file: str
    source_pointer: str
    via: Tuple[str, ...] = ()
