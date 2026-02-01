"""IR data handling module.

This module contains IR loading and composition resolution:
- loader: IR data loading
- composition: allOf composition resolution
"""

from .loader import IRLoader
from .composition import CompositionResolver, resolve_schema_properties

__all__ = [
    "IRLoader",
    "CompositionResolver",
    "resolve_schema_properties",
]
