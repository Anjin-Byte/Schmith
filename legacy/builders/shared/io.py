"""I/O utilities for loading specs and writing IR files."""

import json
import re
from typing import Any, Dict


def load_spec(spec_path: str) -> Dict[str, Any]:
    """
    Load an API specification file (JSON or YAML).

    Supports JSON, YAML, and YML file extensions. For YAML files,
    attempts to use ruamel.yaml first (handles duplicate keys),
    falling back to PyYAML.

    Args:
        spec_path: Path to the specification file.

    Returns:
        Parsed specification as a dictionary.
    """
    ext = spec_path.lower().split(".")[-1]
    if ext in ("yaml", "yml"):
        try:
            import warnings

            from ruamel.yaml import YAML  # type: ignore

            yaml_parser = YAML(typ="safe")
            if hasattr(yaml_parser, "allow_duplicate_keys"):
                setattr(yaml_parser, "allow_duplicate_keys", True)
            if hasattr(yaml_parser, "allow_duplicate_anchors"):
                setattr(yaml_parser, "allow_duplicate_anchors", True)
            with open(spec_path, "r", encoding="utf-8") as handle:
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore")
                    return yaml_parser.load(handle)
        except Exception:
            pass
        import yaml  # type: ignore

        with open(spec_path, "r", encoding="utf-8") as handle:
            return yaml.safe_load(handle)
    with open(spec_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def escape_id(raw: str) -> str:
    """
    Convert a raw ID string to a safe filename component.

    Replaces non-alphanumeric characters (except underscores) with
    underscores and strips leading/trailing underscores.

    Args:
        raw: The raw ID string.

    Returns:
        A sanitized string safe for use in filenames.
    """
    return re.sub(r"[^A-Za-z0-9_]+", "_", raw).strip("_")


def operation_id(method: str, path_template: str) -> str:
    """
    Generate a canonical operation ID from method and path.

    Args:
        method: HTTP method (e.g., "get", "post").
        path_template: URL path template (e.g., "/users/{id}").

    Returns:
        Canonical operation ID (e.g., "op:GET:/users/{id}").
    """
    return f"op:{method.upper()}:{path_template}"
