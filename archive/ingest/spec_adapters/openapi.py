from typing import Any, Dict, Iterator, List, Optional, cast

from ingest.model import ResponseSchema
from ingest.validation import runtime_typechecked, validate_response_schema

SpecType = Dict[str, Any]
SchemaType = Dict[str, Any]


class OpenApiAdapter:
    name = "openapi"

    @runtime_typechecked
    def load_spec(self, spec_path: str) -> SpecType:
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
                        yaml_parser_any = cast(Any, yaml_parser)
                        return cast(SpecType, yaml_parser_any.load(handle))
            except Exception:
                pass
            try:
                import yaml
            except Exception as exc:
                raise RuntimeError("PyYAML is required for YAML specs") from exc
            with open(spec_path, "r", encoding="utf-8") as handle:
                return cast(SpecType, yaml.safe_load(handle))
        import json
        with open(spec_path, "r", encoding="utf-8") as handle:
            return cast(SpecType, json.load(handle))

    @runtime_typechecked
    def iter_response_schemas(self, spec: SpecType) -> Iterator[ResponseSchema]:
        raw_paths: Any = spec.get("paths")
        if not isinstance(raw_paths, dict):
            return
        paths_dict: Dict[str, Any] = cast(Dict[str, Any], raw_paths)
        for path, path_item in paths_dict.items():
            if not isinstance(path_item, dict):
                continue
            path_item_dict: Dict[str, Any] = cast(Dict[str, Any], path_item)
            for method, operation in path_item_dict.items():
                if not isinstance(operation, dict):
                    continue
                operation_dict: Dict[str, Any] = cast(Dict[str, Any], operation)
                if method.lower() not in ("get", "post", "put", "patch", "delete"):
                    continue
                raw_responses: Any = operation_dict.get("responses")
                if not isinstance(raw_responses, dict):
                    continue
                responses_dict: Dict[str, Any] = {
                    str(key): value for key, value in cast(Dict[Any, Any], raw_responses).items()
                }
                for code, response in responses_dict.items():
                    schema = self._response_schema(spec, response)
                    if not schema:
                        continue
                    root = self._resolve_schema(spec, schema)
                    root_type = root.get("type")
                    properties = self._schema_to_properties(spec, root)
                    items = None
                    if root_type == "array":
                        items = self._resolve_schema(spec, root.get("items") or {})
                        properties = self._schema_to_properties(spec, items)
                    if not properties:
                        continue
                    response_schema = ResponseSchema(
                        method=method.lower(),
                        path=path,
                        code=str(code),
                        root_type=root_type,
                        properties=properties,
                        items=items,
                    )
                    validate_response_schema(response_schema)
                    yield response_schema

    def _response_schema(self, spec: SpecType, response: Any) -> Optional[SchemaType]:
        if not isinstance(response, dict):
            return None
        response_dict: Dict[str, Any] = cast(Dict[str, Any], response)
        if "content" in response_dict:
            raw_content = cast(Optional[Dict[str, Any]], response_dict.get("content"))
            if not isinstance(raw_content, dict):
                return None
            content_dict: Dict[str, Any] = raw_content
            app_json = cast(
                Optional[Dict[str, Any]],
                content_dict.get("application/json") or content_dict.get("application/*+json"),
            )
            if not isinstance(app_json, dict):
                return None
            return cast(Optional[SchemaType], app_json.get("schema"))
        return cast(Optional[SchemaType], response_dict.get("schema"))

    def _resolve_ref(self, spec: SpecType, ref: Optional[str]) -> Optional[SchemaType]:
        if not ref or not ref.startswith("#/"):
            return None
        parts = ref.lstrip("#/").split("/")
        node: Optional[SchemaType] = cast(Optional[SchemaType], spec)
        for part in parts:
            if not isinstance(node, dict):
                return None
            node = cast(Optional[SchemaType], node.get(part))
            if node is None:
                return None
        return node

    def _merge_all_of(self, spec: SpecType, schema: SchemaType) -> SchemaType:
        merged: SchemaType = {"type": "object", "properties": {}}
        all_of = schema.get("allOf")
        if not isinstance(all_of, list):
            return merged
        for item in cast(List[Any], all_of):
            item_schema = self._resolve_schema(spec, item)
            props = item_schema.get("properties")
            if not isinstance(props, dict):
                continue
            props_dict: Dict[str, Any] = cast(Dict[str, Any], props)
            for name, value in props_dict.items():
                merged["properties"][name] = value
        return merged

    def _resolve_schema(self, spec: SpecType, schema: Any) -> SchemaType:
        if not isinstance(schema, dict):
            return {}
        schema_dict: Dict[str, Any] = cast(Dict[str, Any], schema)
        if "$ref" in schema_dict:
            ref = cast(Optional[str], schema_dict.get("$ref"))
            resolved = self._resolve_ref(spec, ref)
            return resolved or {}
        if "allOf" in schema_dict:
            return self._merge_all_of(spec, schema_dict)
        return schema_dict

    def _schema_to_properties(self, spec: SpecType, schema: SchemaType) -> List[SchemaType]:
        schema = self._resolve_schema(spec, schema)
        required_fields = set(schema.get("required") or [])
        props = schema.get("properties")
        if isinstance(props, list):
            return cast(List[SchemaType], props)
        if not isinstance(props, dict):
            return []
        props_dict: Dict[str, Any] = cast(Dict[str, Any], props)
        properties: List[SchemaType] = []
        for name, prop_schema in props_dict.items():
            prop_schema = self._resolve_schema(spec, prop_schema)
            prop_type = prop_schema.get("type")
            prop: Dict[str, Any] = {
                "name": name,
                "type": prop_type,
                "required": name in required_fields,
            }
            if "nullable" in prop_schema:
                prop["nullable"] = bool(prop_schema.get("nullable"))
            if prop_type == "array":
                items = self._resolve_schema(spec, prop_schema.get("items") or {})
                item_type = items.get("type")
                if item_type == "object" and items.get("properties"):
                    prop["items"] = {
                        "type": "object",
                        "properties": self._schema_to_properties(spec, items),
                    }
                else:
                    prop["items"] = {
                        "type": item_type,
                    }
            if prop_type == "object" and prop_schema.get("properties"):
                prop["properties"] = self._schema_to_properties(spec, prop_schema)
            properties.append(prop)
        return properties
