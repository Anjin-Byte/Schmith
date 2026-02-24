import os
from typing import Any, Dict, Optional

try:
    import tomllib
except Exception:  # pragma: no cover - fallback for older runtimes
    tomllib = None


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ConfigType = Dict[str, Any]


def load_config(path: Optional[str]) -> ConfigType:
    if not path or not os.path.exists(path):
        return {}
    if not tomllib:
        raise RuntimeError("tomllib is not available; use Python 3.11+ for config.toml support.")
    with open(path, "rb") as handle:
        return tomllib.load(handle)


def api_name(config: ConfigType) -> str:
    return config.get("api", {}).get("name", "api")


def spec_root(config: ConfigType) -> str:
    return config.get("output", {}).get("spec_dir", "spec")


def reports_root(config: ConfigType) -> str:
    return config.get("output", {}).get("reports_dir", "reports")


def resolve_spec_path(
    config: ConfigType,
    spec_override: Optional[str] = None,
    spec_url: Optional[str] = None,
) -> str:
    if spec_override:
        return spec_override
    if not spec_url:
        spec_url = config.get("spec", {}).get("url")
    name = api_name(config)
    ext = "json"
    if spec_url and spec_url.endswith((".yml", ".yaml")):
        ext = "yml"
    return os.path.join(ROOT, spec_root(config), name, f"api.{ext}")


def resolve_report_path(config: ConfigType, filename: str, override: Optional[str] = None) -> str:
    if override:
        return override
    name = api_name(config)
    return os.path.join(ROOT, reports_root(config), name, filename)
