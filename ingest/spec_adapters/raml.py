from typing import Any, Dict, Iterator, List, cast

from ingest.model import ResponseSchema
from ingest.validation import runtime_typechecked, validate_response_schema

SpecType = Dict[str, Any]


class RamlAdapter:
    name = "raml"

    @runtime_typechecked
    def load_spec(self, spec_path: str) -> SpecType:
        import json
        with open(spec_path, "r", encoding="utf-8") as handle:
            return json.load(handle)

    @runtime_typechecked
    def iter_response_schemas(self, spec: SpecType) -> Iterator[ResponseSchema]:
        resources = spec.get("resources", spec.get("paths"))
        for endpoint in self._walk_resources(resources, ""):
            endpoint_dict = endpoint
            method = cast(str, endpoint_dict.get("method") or "")
            path = cast(str, endpoint_dict.get("path") or "")
            details = endpoint_dict.get("details")
            if not isinstance(details, dict):
                continue
            details_dict: Dict[str, Any] = cast(Dict[str, Any], details)
            responses = details_dict.get("responses")
            if not isinstance(responses, list):
                continue
            for response in cast(List[Any], responses):
                if not isinstance(response, dict):
                    continue
                response_dict: Dict[str, Any] = cast(Dict[str, Any], response)
                code = response_dict.get("code")
                bodies = response_dict.get("body")
                if not isinstance(bodies, list):
                    continue
                for body in cast(List[Any], bodies):
                    if not isinstance(body, dict):
                        continue
                    body_dict: Dict[str, Any] = cast(Dict[str, Any], body)
                    if body_dict.get("name") != "application/json":
                        continue
                    properties = body_dict.get("properties")
                    if not isinstance(properties, list) or not properties:
                        continue
                    response_schema = ResponseSchema(
                        method=method,
                        path=path,
                        code=str(code),
                        root_type="object",
                        properties=cast(List[Dict[str, Any]], properties),
                        items=None,
                    )
                    validate_response_schema(response_schema)
                    yield response_schema

    def _walk_resources(self, resources: Any, base_path: str = "") -> List[Dict[str, Any]]:
        endpoints: List[Dict[str, Any]] = []
        if isinstance(resources, list):
            for res in cast(List[Any], resources):
                endpoints.extend(self._walk_resources(res, base_path))
            return endpoints
        if isinstance(resources, dict):
            resources_dict: Dict[str, Any] = cast(Dict[str, Any], resources)
            rel = resources_dict.get("relativeUri")
            uri = f"{base_path}{rel}" if rel else base_path
            methods = resources_dict.get("methods")
            if isinstance(methods, list):
                for method in cast(List[Any], methods):
                    if not isinstance(method, dict):
                        continue
                    method_dict: Dict[str, Any] = cast(Dict[str, Any], method)
                    endpoints.append({"method": method_dict.get("method"), "path": uri, "details": method_dict})
            children = resources_dict.get("resources")
            if isinstance(children, list):
                for child in cast(List[Any], children):
                    endpoints.extend(self._walk_resources(child, uri))
        return endpoints
