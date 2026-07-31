"""API adapter registry.

load_adapter(ref) resolves an adapter reference to a concrete ApiAdapter
instance. The ref is a dotted Python path to a class that subclasses
ApiAdapter: "mypackage.adapters.MyApiAdapter".

Usage in config.yaml:
    api:
      adapter: mypackage.adapters.MyApiAdapter

If adapter is null/absent, the base ApiAdapter (all pass-throughs) is used.
"""

from __future__ import annotations

import importlib

from schmith.adapters.base import ApiAdapter


def load_adapter(ref: str | None) -> ApiAdapter:
    """Load an ApiAdapter from a dotted class reference.

    Args:
        ref: Dotted path to a class (e.g. "mypackage.adapters.MyAdapter").
            None or empty string returns the base ApiAdapter.

    Returns:
        An instantiated ApiAdapter (or subclass).

    Raises:
        ValueError: If ref is malformed (no class name component).
        ImportError: If the module cannot be imported.
        AttributeError: If the class is not found in the module.
    """
    if not ref:
        return ApiAdapter()

    module_path, _, class_name = ref.rpartition(".")
    if not module_path:
        raise ValueError(
            f"Invalid adapter ref '{ref}'. "
            "Expected a dotted path with module and class, e.g. 'my.module.MyAdapter'."
        )

    module = importlib.import_module(module_path)
    cls = getattr(module, class_name)
    return cls()  # type: ignore[no-any-return]
