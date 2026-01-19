#!/usr/bin/env python3
import argparse
import hashlib
import json
import os
import sys
from typing import Any, Dict, List, Optional, Tuple
from datetime import datetime, timezone
from urllib.request import urlopen, Request

try:
    import tomllib
except Exception:  # pragma: no cover - fallback for older runtimes
    tomllib = None


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPEC_DIR = os.path.join(ROOT, "spec")
REPORTS_DIR = os.path.join(ROOT, "reports")
sys.path.append(ROOT)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


DEFAULT_SPEC_URL = "https://docs.servicefusion.com/api.json"
DEFAULT_CONFIG_PATH = os.path.join(ROOT, "config.toml")


def fetch_url(url: str) -> Tuple[bytes, Any]:
    req = Request(url, headers={"User-Agent": "service-fusion-spec-sync/1.0"})
    with urlopen(req) as resp:
        return resp.read(), resp.headers


def write_file(path: str, data: Any, binary: bool = False) -> None:
    mode = "wb" if binary else "w"
    with open(path, mode, encoding=None if binary else "utf-8") as handle:
        handle.write(data)


def walk_resources(resources: Any, base_path: str = "") -> List[Dict[str, Any]]:
    endpoints: List[Dict[str, Any]] = []
    if isinstance(resources, list):
        for res in resources:
            endpoints.extend(walk_resources(res, base_path))
        return endpoints
    if isinstance(resources, dict):
        rel = resources.get("relativeUri")
        uri = f"{base_path}{rel}" if rel else base_path
        for method in resources.get("methods", []):
            endpoints.append({"method": method.get("method"), "path": uri, "details": method})
        for child in resources.get("resources", []):
            endpoints.extend(walk_resources(child, uri))
    return endpoints


def summarize_response_schema(responses: Any) -> Dict[str, Dict[str, Any]]:
    summary: Dict[str, Dict[str, Any]] = {}
    if not isinstance(responses, list):
        return summary
    for resp in responses:
        code = resp.get("code")
        bodies = resp.get("body", [])
        if not isinstance(bodies, list):
            continue
        for body in bodies:
            if body.get("name") != "application/json":
                continue
            props = body.get("properties", [])
            prop_names = [prop.get("name") for prop in props if prop.get("name")]
            summary[str(code)] = {
                "properties": prop_names,
                "propertyCount": len(prop_names),
            }
    return summary


def load_config(path: Optional[str]) -> Dict[str, Any]:
    if not path or not os.path.exists(path):
        return {}
    if not tomllib:
        raise RuntimeError("tomllib is not available; use Python 3.11+ for config.toml support.")
    with open(path, "rb") as handle:
        return tomllib.load(handle)


def hash_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def resolve_output_paths(
    config: Dict[str, Any],
    out_override: Optional[str],
    version_override: Optional[str],
    spec_url: str,
) -> Tuple[str, str, str]:
    api_name = config.get("api", {}).get("name", "api")
    spec_dir = config.get("output", {}).get("spec_dir", "spec")
    reports_dir = config.get("output", {}).get("reports_dir", "reports")

    spec_dir_path = os.path.join(ROOT, spec_dir, api_name)
    reports_dir_path = os.path.join(ROOT, reports_dir, api_name)

    spec_filename = "api.yml" if spec_url.endswith((".yml", ".yaml")) else "api.json"
    spec_path = out_override or os.path.join(spec_dir_path, spec_filename)
    version_path = version_override or os.path.join(reports_dir_path, "spec_version.json")
    endpoints_path = os.path.join(reports_dir_path, "endpoints.json")

    return spec_path, version_path, endpoints_path


def load_yaml(raw_text: str) -> Any:
    try:
        import warnings
        from ruamel.yaml import YAML  # type: ignore

        yaml_parser = YAML(typ="safe")
        if hasattr(yaml_parser, "allow_duplicate_keys"):
            yaml_parser.allow_duplicate_keys = True
        if hasattr(yaml_parser, "allow_duplicate_anchors"):
            yaml_parser.allow_duplicate_anchors = True
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            return yaml_parser.load(raw_text)
    except Exception:
        pass

    try:
        import yaml  # type: ignore
    except Exception as exc:
        raise RuntimeError("PyYAML is required to parse YAML specs.") from exc
    return yaml.safe_load(raw_text)


def summarize_openapi(spec: Dict[str, Any]) -> Dict[str, Any]:
    from ingest.spec_adapters.openapi import OpenApiAdapter

    adapter = OpenApiAdapter()
    summary = {
        "baseUri": None,
        "endpointCount": 0,
        "endpoints": [],
    }
    endpoints = {}
    for entry in adapter.iter_response_schemas(spec):
        key = (entry.method, entry.path)
        method = entry.method
        path = entry.path
        code = entry.code
        prop_names = [prop.get("name") for prop in entry.properties if prop.get("name")]
        bucket = endpoints.setdefault(key, {
            "method": method,
            "path": path,
            "responseSchemaSummary": {},
        })
        bucket["responseSchemaSummary"][str(code)] = {
            "properties": prop_names,
            "propertyCount": len(prop_names),
        }

    summary["endpoints"] = list(endpoints.values())
    summary["endpointCount"] = len(summary["endpoints"])
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch and summarize Service Fusion API spec.")
    parser.add_argument("--config", default=DEFAULT_CONFIG_PATH, help="Path to config.toml.")
    parser.add_argument("--url", default="", help="Spec URL to download.")
    parser.add_argument("--out", default="", help="Path to write the downloaded spec.")
    parser.add_argument("--version-out", default="", help="Path to write spec version metadata.")
    args = parser.parse_args()

    os.makedirs(SPEC_DIR, exist_ok=True)
    os.makedirs(REPORTS_DIR, exist_ok=True)

    config = load_config(args.config)
    url = args.url or config.get("spec", {}).get("url") or DEFAULT_SPEC_URL
    spec_path, version_path, endpoints_path = resolve_output_paths(
        config,
        args.out or None,
        args.version_out or None,
        url,
    )

    os.makedirs(os.path.dirname(spec_path), exist_ok=True)
    os.makedirs(os.path.dirname(version_path), exist_ok=True)
    os.makedirs(os.path.dirname(endpoints_path), exist_ok=True)

    print(f"Downloading spec from {url}")
    raw, headers = fetch_url(url)
    write_file(spec_path, raw, binary=True)
    print(f"Wrote spec to {spec_path}")

    spec_text = raw.decode("utf-8", errors="replace")
    report = None
    try:
        data = json.loads(spec_text)
        resources = data.get("resources", data.get("paths"))
        endpoints = walk_resources(resources, "")

        report = {
            "baseUri": data.get("baseUri"),
            "endpointCount": len(endpoints),
            "endpoints": [],
        }

        for entry in endpoints:
            method = entry.get("method")
            path = entry.get("path")
            details = entry.get("details", {})
            responses = details.get("responses", [])
            report["endpoints"].append({
                "method": method,
                "path": path,
                "responseSchemaSummary": summarize_response_schema(responses),
            })
    except json.JSONDecodeError:
        data = load_yaml(spec_text)
        if isinstance(data, dict) and ("openapi" in data or "swagger" in data or "paths" in data):
            report = summarize_openapi(data)
        else:
            report = {
                "baseUri": None,
                "endpointCount": 0,
                "endpoints": [],
                "note": "Spec format not recognized for endpoint summary.",
            }

    write_file(endpoints_path, json.dumps(report, indent=2) + "\n")
    print(f"Wrote endpoint summary to {endpoints_path}")

    version_payload = {
        "url": url,
        "fetchedAt": datetime.now(timezone.utc).isoformat(),
        "sha256": hash_bytes(raw),
        "sizeBytes": len(raw),
        "etag": headers.get("ETag"),
        "lastModified": headers.get("Last-Modified"),
        "contentType": headers.get("Content-Type"),
    }
    write_file(version_path, json.dumps(version_payload, indent=2) + "\n")
    print(f"Wrote spec version metadata to {version_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
