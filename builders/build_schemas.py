#!/usr/bin/env python3
# pyright: reportUnknownVariableType=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownArgumentType=false
# pyright: reportUnnecessaryIsInstance=false
# pyright: reportOptionalIterable=false
import argparse
import hashlib
import json
import os
import re
import sys
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple, cast

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ROOT)
sys.path.append(SCRIPT_DIR)

from pipeline.config import api_name, load_config, resolve_spec_path

CONFIG_DEFAULT = os.path.join(ROOT, "config.toml")


@dataclass(frozen=True)
class Provenance:
    source_file: str
    source_pointer: str
    via: Tuple[str, ...] = ()


def canonical_json_hash(payload: Any) -> str:
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha1(canonical.encode("utf-8")).hexdigest()


def escape_id(raw: str) -> str:
    return re.sub(r"[^A-Za-z0-9_]+", "_", raw).strip("_")


def schema_id_from_ref(ref: str) -> str:
    if ref.startswith("#/components/schemas/"):
        return f"schema:components/{ref.split('/')[-1]}"
    if ref.startswith("#/components/"):
        return f"schema:components/{ref.lstrip('#/components/') }".replace("/", "_")
    return f"schema:ref/{ref.lstrip('#/') }".replace("/", "_")


def schema_id_for_schema(schema: Any) -> Optional[str]:
    if not isinstance(schema, dict):
        return None
    ref = schema.get("$ref")
    if isinstance(ref, str):
        return schema_id_from_ref(ref)
    return f"schema:anon/{canonical_json_hash(schema)}"


def schema_id_for_raml_type(type_decl: Any, allow_name_field: bool = True) -> Optional[str]:
    """
    Generate schema ID for RAML type declarations.

    Args:
        type_decl: The type declaration (string reference or dict)
        allow_name_field: If True, use the internal 'name' field for dict types.
                         Set to False for inline type definitions where the name
                         field should be ignored.
    """
    if isinstance(type_decl, str):
        return f"schema:types/{type_decl}"
    if isinstance(type_decl, dict):
        type_dict = cast(Dict[str, Any], type_decl)
        # Only use the 'name' field if explicitly allowed (for top-level types)
        # For inline types, the 'name' field is an internal RAML field and should be ignored
        if allow_name_field:
            name = type_dict.get("name")
            if isinstance(name, str):
                return f"schema:types/{name}"
        return f"schema:anon/{canonical_json_hash(type_dict)}"
    return None


def load_spec(spec_path: str) -> Dict[str, Any]:
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


def resolve_ref(spec: Dict[str, Any], ref: str) -> Optional[Dict[str, Any]]:
    if not ref.startswith("#/"):
        return None
    node: Any = spec
    for part in ref.lstrip("#/").split("/"):
        if not isinstance(node, dict):
            return None
        node = node.get(part)
        if node is None:
            return None
    if isinstance(node, dict):
        return node
    return None


def detect_nullable(schema: Dict[str, Any]) -> Optional[bool]:
    if "nullable" in schema:
        return bool(schema.get("nullable"))
    type_value = schema.get("type")
    if isinstance(type_value, list):
        return "null" in type_value
    return None


def extract_constraints(schema: Dict[str, Any]) -> Dict[str, Any]:
    constraints = {}
    for key in (
        "minLength",
        "maxLength",
        "pattern",
        "minimum",
        "maximum",
        "minItems",
        "maxItems",
        "uniqueItems",
        "enum",
        "const",
    ):
        if key in schema:
            constraints[key] = schema.get(key)
    return constraints


def extract_composition(schema: Dict[str, Any], spec: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    for key in ("oneOf", "anyOf", "allOf"):
        if key in schema and isinstance(schema.get(key), list):
            members = []
            for entry in schema.get(key) or []:
                if isinstance(entry, dict) and "$ref" in entry:
                    members.append(schema_id_from_ref(entry["$ref"]))
                elif isinstance(entry, dict):
                    members.append(schema_id_for_schema(entry))
            return {"kind": key, "members": [m for m in members if m]}
    return None


def availability(value: Any, state: str) -> Dict[str, Any]:
    return {"value": value, "availability": state}


def build_field(
    name: str,
    schema_id: Optional[str],
    required: bool,
    field_schema: Dict[str, Any],
    pointer: str,
    provenance: Provenance,
) -> Dict[str, Any]:
    field = {
        "json_name": name,
        "schema_id": schema_id,
        "required": required,
        "nullable": detect_nullable(field_schema),
        "description": field_schema.get("description"),
        "deprecated": field_schema.get("deprecated"),
        "read_only": field_schema.get("readOnly"),
        "write_only": field_schema.get("writeOnly"),
        "examples": field_schema.get("examples"),
        "json_pointer": pointer,
        "provenance": provenance.__dict__,
    }
    field["availability"] = {
        "json_name": "native" if name else "absent",
        "schema_id": "adapter" if schema_id else "absent",
        "required": "native",
        "nullable": "native" if field["nullable"] is not None else "absent",
        "description": "native" if field["description"] else "absent",
        "deprecated": "native" if field["deprecated"] is not None else "absent",
        "read_only": "native" if field["read_only"] is not None else "absent",
        "write_only": "native" if field["write_only"] is not None else "absent",
        "examples": "native" if field["examples"] is not None else "absent",
        "json_pointer": "adapter",
        "provenance": "native",
    }
    return field


def register_schema(
    schema_id: str,
    name_hint: Optional[str],
    schema: Dict[str, Any],
    is_inline: bool,
    provenance: Provenance,
    spec: Dict[str, Any],
    schemas: Dict[str, Dict[str, Any]],
    schema_hashes: Dict[str, str],
    register_nested: bool = True,
) -> None:
    if schema_id in schemas:
        return

    # Check if this schema (by content hash) is already registered under a different ID
    # This prevents duplicate registration of named types when encountered inline
    if schema_id.startswith("schema:anon/"):
        content_hash = schema_id.split("/")[-1]
        if content_hash in schema_hashes:
            # This schema is already registered under a named ID, skip duplicate
            return
        # Track this hash
        schema_hashes[content_hash] = schema_id
    kind = schema.get("type") or "unknown"
    if isinstance(kind, list):
        kind = next((k for k in kind if k != "null"), "unknown")
    properties = []
    required_raw = schema.get("required")
    required_fields: List[str] = required_raw if isinstance(required_raw, list) else []
    props = schema.get("properties")
    if isinstance(props, list):
        required_fields = []
        for prop in props:
            if not isinstance(prop, dict):
                continue
            prop_name = prop.get("name")
            if not isinstance(prop_name, str):
                continue
            prop_required = bool(prop.get("required")) if prop.get("required") is not None else False
            if prop_required:
                required_fields.append(prop_name)
            pointer = f"$.{prop_name}"
            prop_schema_id = schema_id_for_raml_type(prop.get("type"))
            properties.append(
                build_field(
                    prop_name,
                    prop_schema_id,
                    prop_required,
                    prop,
                    pointer,
                    provenance,
                )
            )
            # Recursively register nested inline schemas
            if register_nested and isinstance(prop, dict):
                prop_type = prop.get("type")
                # Only register if type is itself a dict (inline type definition with properties)
                if isinstance(prop_type, dict):
                    # Use allow_name_field=False to prevent using internal 'name' field for inline types
                    nested_id = schema_id_for_raml_type(prop_type, allow_name_field=False)
                    if nested_id:
                        register_schema(
                            nested_id,
                            None,
                            prop_type,
                            True,
                            provenance,
                            spec,
                            schemas,
                            schema_hashes,
                        )
                # Also register array item types if they're inline
                elif prop_type == "array":
                    items = prop.get("items")
                    if isinstance(items, dict):
                        items_id = schema_id_for_raml_type(items, allow_name_field=False)
                        if items_id:
                            register_schema(
                                items_id,
                                None,
                                items,
                                True,
                                provenance,
                                spec,
                                schemas,
                                schema_hashes,
                            )
    elif isinstance(props, dict):
        for prop_name, prop_schema in props.items():
            if not isinstance(prop_schema, dict):
                continue
            prop_ref = prop_schema.get("$ref")
            if isinstance(prop_ref, str):
                prop_schema_id = schema_id_from_ref(prop_ref)
            else:
                prop_schema_id = schema_id_for_schema(prop_schema)
            pointer = f"$.{prop_name}"
            properties.append(
                build_field(
                    prop_name,
                    prop_schema_id,
                    prop_name in required_fields,
                    prop_schema,
                    pointer,
                    provenance,
                )
            )
            if register_nested and isinstance(prop_schema, dict) and "$ref" not in prop_schema:
                nested_id = schema_id_for_schema(prop_schema)
                if nested_id:
                    register_schema(
                        nested_id,
                        None,
                        prop_schema,
                        True,
                        provenance,
                        spec,
                        schemas,
                        schema_hashes,
                    )

    items_schema_id = None
    if kind == "array":
        items = schema.get("items") if isinstance(schema.get("items"), dict) else None
        if isinstance(items, dict):
            items_schema_id = schema_id_for_schema(items)
            if register_nested and items_schema_id:
                register_schema(
                    items_schema_id,
                    None,
                    items,
                    True,
                    provenance,
                    spec,
                    schemas,
                    schema_hashes,
                )

    additional_properties_schema_id = None
    additional_props = schema.get("additionalProperties")
    if isinstance(additional_props, dict):
        additional_properties_schema_id = schema_id_for_schema(additional_props)
        if register_nested and additional_properties_schema_id:
            register_schema(
                additional_properties_schema_id,
                None,
                additional_props,
                True,
                provenance,
                spec,
                schemas,
                schema_hashes,
            )

    schema_record = {
        "id": schema_id,
        "name_hint": name_hint,
        "kind": kind or "unknown",
        "title": schema.get("title"),
        "description": schema.get("description"),
        "properties": properties,
        "required": list(required_fields) if isinstance(required_fields, list) else [],
        "items_schema_id": items_schema_id,
        "additional_properties_schema_id": additional_properties_schema_id,
        "constraints": extract_constraints(schema),
        "composition": extract_composition(schema, spec),
        "provenance": provenance.__dict__,
        "is_inline": is_inline,
    }
    schema_record["availability"] = {
        "id": "adapter",
        "name_hint": "native" if name_hint else "absent",
        "kind": "native" if schema.get("type") is not None else "absent",
        "title": "native" if schema.get("title") else "absent",
        "description": "native" if schema.get("description") else "absent",
        "properties": "native" if properties else "absent",
        "required": "native" if required_fields else "absent",
        "items_schema_id": "native" if items_schema_id else "absent",
        "additional_properties_schema_id": "native" if additional_properties_schema_id else "absent",
        "constraints": "native" if schema_record["constraints"] else "absent",
        "composition": "native" if schema_record["composition"] else "absent",
        "provenance": "native",
    }
    schemas[schema_id] = schema_record

    # Track the content hash for named schemas to prevent duplicate anonymous registration
    if not is_inline:
        content_hash = canonical_json_hash(schema)
        schema_hashes[content_hash] = schema_id


def extract_openapi_schemas(spec: Dict[str, Any], spec_path: str) -> Dict[str, Dict[str, Any]]:
    schemas: Dict[str, Dict[str, Any]] = {}
    schema_hashes: Dict[str, str] = {}  # Map content hash -> schema_id to prevent duplicates
    if spec.get("swagger") == "2.0":
        definitions = spec.get("definitions")
        if isinstance(definitions, dict):
            for name, schema in definitions.items():
                if not isinstance(schema, dict):
                    continue
                schema_id = f"schema:definitions/{name}"
                provenance = Provenance(spec_path, f"#/definitions/{name}")
                register_schema(schema_id, name, schema, False, provenance, spec, schemas, schema_hashes)
    else:
        components = spec.get("components")
        if isinstance(components, dict):
            comp_schemas = components.get("schemas")
            if isinstance(comp_schemas, dict):
                for name, schema in comp_schemas.items():
                    if not isinstance(schema, dict):
                        continue
                    schema_id = f"schema:components/{name}"
                    provenance = Provenance(spec_path, f"#/components/schemas/{name}")
                    register_schema(schema_id, name, schema, False, provenance, spec, schemas, schema_hashes)

    # Inline schemas from operations
    paths = spec.get("paths")
    if isinstance(paths, dict):
        for path_template, path_item in paths.items():
            if not isinstance(path_item, dict):
                continue
            for method, operation in path_item.items():
                if not isinstance(method, str) or not isinstance(operation, dict):
                    continue
                if spec.get("swagger") == "2.0":
                    parameters = operation.get("parameters")
                    if isinstance(parameters, list):
                        for idx, param in enumerate(parameters):
                            if not isinstance(param, dict):
                                continue
                            if param.get("in") != "body":
                                continue
                            schema = param.get("schema")
                            if isinstance(schema, dict):
                                schema_id = schema_id_for_schema(schema)
                                if schema_id:
                                    provenance = Provenance(
                                        spec_path,
                                        f"#/paths/{path_template}/{method}/parameters/{idx}",
                                    )
                                    register_schema(schema_id, None, schema, True, provenance, spec, schemas, schema_hashes)
                else:
                    if "requestBody" in operation and isinstance(operation.get("requestBody"), dict):
                        content = operation["requestBody"].get("content")
                        if isinstance(content, dict):
                            for media_type, media in content.items():
                                if not isinstance(media, dict):
                                    continue
                                schema = media.get("schema")
                                if isinstance(schema, dict):
                                    schema_id = schema_id_for_schema(schema)
                                    if schema_id:
                                        provenance = Provenance(
                                            spec_path,
                                            f"#/paths/{path_template}/{method}/requestBody/content/{media_type}",
                                        )
                                        register_schema(schema_id, None, schema, True, provenance, spec, schemas, schema_hashes)
                responses = operation.get("responses")
                if isinstance(responses, dict):
                    for status, response in responses.items():
                        if not isinstance(response, dict):
                            continue
                        if spec.get("swagger") == "2.0":
                            schema = response.get("schema")
                            if isinstance(schema, dict):
                                schema_id = schema_id_for_schema(schema)
                                if schema_id:
                                    provenance = Provenance(
                                        spec_path,
                                        f"#/paths/{path_template}/{method}/responses/{status}",
                                    )
                                    register_schema(schema_id, None, schema, True, provenance, spec, schemas, schema_hashes)
                        else:
                            content = response.get("content")
                            if isinstance(content, dict):
                                for media_type, media in content.items():
                                    if not isinstance(media, dict):
                                        continue
                                    schema = media.get("schema")
                                    if isinstance(schema, dict):
                                        schema_id = schema_id_for_schema(schema)
                                        if schema_id:
                                            provenance = Provenance(
                                                spec_path,
                                                f"#/paths/{path_template}/{method}/responses/{status}/content/{media_type}",
                                            )
                                            register_schema(schema_id, None, schema, True, provenance, spec, schemas, schema_hashes)

    return schemas


def register_nested_schemas(
    schema: Dict[str, Any],
    provenance: Provenance,
    spec: Dict[str, Any],
    schemas: Dict[str, Dict[str, Any]],
    schema_hashes: Dict[str, str],
) -> None:
    """Register nested inline schemas within a schema's properties."""
    props = schema.get("properties")

    # Handle list-style RAML properties
    if isinstance(props, list):
        for prop in props:
            if not isinstance(prop, dict):
                continue
            prop_type = prop.get("type")
            # Register inline object type definitions
            if isinstance(prop_type, dict):
                nested_id = schema_id_for_raml_type(prop_type, allow_name_field=False)
                if nested_id:
                    register_schema(nested_id, None, prop_type, True, provenance, spec, schemas, schema_hashes)
            # Register inline array item types
            elif prop_type == "array":
                items = prop.get("items")
                if isinstance(items, dict):
                    items_id = schema_id_for_raml_type(items, allow_name_field=False)
                    if items_id:
                        register_schema(items_id, None, items, True, provenance, spec, schemas, schema_hashes)

    # Handle dict-style properties (OpenAPI style)
    elif isinstance(props, dict):
        for _prop_name, prop_schema in props.items():
            if isinstance(prop_schema, dict) and "$ref" not in prop_schema:
                nested_id = schema_id_for_schema(prop_schema)
                if nested_id:
                    register_schema(nested_id, None, prop_schema, True, provenance, spec, schemas, schema_hashes)

    # Handle array items
    kind = schema.get("type") or "unknown"
    if kind == "array":
        items = schema.get("items") if isinstance(schema.get("items"), dict) else None
        if isinstance(items, dict):
            items_schema_id = schema_id_for_schema(items)
            if items_schema_id:
                register_schema(items_schema_id, None, items, True, provenance, spec, schemas, schema_hashes)

    # Handle additionalProperties
    additional_props = schema.get("additionalProperties")
    if isinstance(additional_props, dict):
        additional_properties_schema_id = schema_id_for_schema(additional_props)
        if additional_properties_schema_id:
            register_schema(additional_properties_schema_id, None, additional_props, True, provenance, spec, schemas, schema_hashes)


def extract_raml_schemas(spec: Dict[str, Any], spec_path: str) -> Dict[str, Dict[str, Any]]:
    schemas: Dict[str, Dict[str, Any]] = {}
    schema_hashes: Dict[str, str] = {}  # Map content hash -> schema_id to prevent duplicates

    for primitive in ("object", "array"):
        schema_id = f"schema:types/{primitive}"
        provenance = Provenance(spec_path, f"raml:types:{primitive}")
        register_schema(schema_id, primitive, {"type": primitive}, False, provenance, spec, schemas, schema_hashes)

    # Pass 1: Register all top-level named types without their nested schemas
    # This populates schema_hashes with all named type content hashes
    types = spec.get("types")
    if isinstance(types, dict):
        for name, schema in types.items():
            if not isinstance(schema, dict):
                continue
            schema_id = f"schema:types/{name}"
            provenance = Provenance(spec_path, f"raml:types:{name}")
            register_schema(schema_id, name, schema, False, provenance, spec, schemas, schema_hashes, register_nested=False)

    # Pass 2: Process nested schemas within named types
    # Now schema_hashes is fully populated, so inline schemas can deduplicate to named types
    if isinstance(types, dict):
        for name, schema in types.items():
            if not isinstance(schema, dict):
                continue
            provenance = Provenance(spec_path, f"raml:types:{name}")
            # Process nested schemas by calling a helper function
            register_nested_schemas(schema, provenance, spec, schemas, schema_hashes)

    resources = spec.get("resources", spec.get("paths"))
    if isinstance(resources, list):
        for node in resources:
            if isinstance(node, dict) and isinstance(node.get("methods"), list):
                for method in node.get("methods"):
                    if not isinstance(method, dict):
                        continue
                    body = method.get("body") if isinstance(method.get("body"), list) else []
                    for entry in body:
                        if not isinstance(entry, dict):
                            continue
                        schema = entry.get("type") if isinstance(entry.get("type"), dict) else None
                        if isinstance(schema, dict):
                            schema_id = schema_id_for_raml_type(schema)
                            if schema_id:
                                provenance = Provenance(spec_path, "raml:body")
                                register_schema(schema_id, None, schema, True, provenance, spec, schemas, schema_hashes)
                    responses = method.get("responses") if isinstance(method.get("responses"), list) else []
                    for response in responses:
                        if not isinstance(response, dict):
                            continue
                        bodies = response.get("body") if isinstance(response.get("body"), list) else []
                        for entry in bodies:
                            if not isinstance(entry, dict):
                                continue
                            schema = entry.get("type") if isinstance(entry.get("type"), dict) else None
                            if isinstance(schema, dict):
                                schema_id = schema_id_for_raml_type(schema)
                                if schema_id:
                                    provenance = Provenance(spec_path, "raml:responses")
                                    register_schema(schema_id, None, schema, True, provenance, spec, schemas, schema_hashes)

    return schemas


def load_operations_index(spec_name: str) -> Dict[str, List[str]]:
    operations_index_path = os.path.join(ROOT, "ir", spec_name, "operations", "index.json")
    if not os.path.exists(operations_index_path):
        return {}
    with open(operations_index_path, "r", encoding="utf-8") as handle:
        data = json.load(handle)
    mapping: Dict[str, List[str]] = {}
    for entry in data.get("operations", []):
        op_id = entry.get("operation_id")
        for schema_id in entry.get("requests", []) + entry.get("responses", []):
            if not schema_id:
                continue
            mapping.setdefault(schema_id, []).append(op_id)
    return mapping


def write_schemas(spec_name: str, schemas: Dict[str, Dict[str, Any]]) -> None:
    base_dir = os.path.join(ROOT, "ir", spec_name, "schemas")
    os.makedirs(base_dir, exist_ok=True)
    usage = load_operations_index(spec_name)
    index_entries = []
    for schema_id, schema in schemas.items():
        schema["where_used"] = usage.get(schema_id, [])
        schema["availability"]["where_used"] = "adapter" if schema["where_used"] else "absent"
        index_entries.append({
            "schema_id": schema_id,
            "name_hint": schema.get("name_hint"),
            "kind": schema.get("kind"),
            "where_used": schema.get("where_used"),
            "is_inline": bool(schema.get("is_inline")),
        })
        filename = f"{escape_id(schema_id)}.json"
        with open(os.path.join(base_dir, filename), "w", encoding="utf-8") as handle:
            json.dump(schema, handle, indent=2)
            handle.write("\n")

    index_path = os.path.join(base_dir, "index.json")
    with open(index_path, "w", encoding="utf-8") as handle:
        json.dump({"schemas": index_entries}, handle, indent=2)
        handle.write("\n")


def update_manifest(spec_name: str, schema_count: int) -> None:
    manifest_path = os.path.join(ROOT, "ir", spec_name, "manifest.json")
    if os.path.exists(manifest_path):
        with open(manifest_path, "r", encoding="utf-8") as handle:
            manifest = json.load(handle)
    else:
        manifest = {
            "spec_name": spec_name,
            "spec_version": None,
            "base_urls": [],
            "adapter": None,
            "generated_at": None,
            "counts": {"operations": 0, "schemas": 0, "edges": 0},
            "indexes": {
                "operations": "operations/index.json",
                "schemas": "schemas/index.json",
                "refs_edges": "refs/edges.json",
                "refs_adjacency": "refs/adjacency.json",
                "media_types": "serialization/media_types.json",
                "json_paths": "serialization/json_paths.json",
            },
        }
    manifest["counts"]["schemas"] = schema_count
    os.makedirs(os.path.dirname(manifest_path), exist_ok=True)
    with open(manifest_path, "w", encoding="utf-8") as handle:
        json.dump(manifest, handle, indent=2)
        handle.write("\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build IR schema index and detail files.")
    parser.add_argument("--config", default=CONFIG_DEFAULT, help="Path to config.toml.")
    parser.add_argument("--spec", default="", help="Path to spec file.")
    parser.add_argument("--adapter", default="openapi", help="Spec adapter: openapi or raml.")
    args = parser.parse_args()

    config = load_config(args.config)
    spec_path = resolve_spec_path(config, args.spec)
    spec_name = api_name(config)

    spec = load_spec(spec_path)
    if args.adapter == "openapi":
        schemas = extract_openapi_schemas(spec, spec_path)
    elif args.adapter == "raml":
        schemas = extract_raml_schemas(spec, spec_path)
    else:
        raise ValueError(f"Unknown adapter: {args.adapter}")

    write_schemas(spec_name, schemas)
    update_manifest(spec_name, len(schemas))
    print(f"Wrote {len(schemas)} schemas to ir/{spec_name}/schemas")
    return 0


if __name__ == "__main__":
    sys.exit(main())
