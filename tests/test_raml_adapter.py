"""Tests for adapters/spec/raml.py."""

from schmith.adapters.spec.raml import extract_operations, extract_schemas


# ---------------------------------------------------------------------------
# Minimal synthetic RAML spec — uses the RAML-parser resource tree format
# that walk_resources() expects (relativeUri / methods / resources keys).
# ---------------------------------------------------------------------------

MINIMAL_RAML: dict = {
    "title": "Test API",
    "version": "v1",
    "baseUri": "https://api.example.com/{version}",
    "types": {
        "Customer": {
            "type": "object",
            "properties": {
                "id": {"type": "string", "required": True},
                "name": {"type": "string"},
            },
        },
        "CustomerList": {
            "type": "object",
            "properties": {
                "items": {"type": "array", "items": "Customer"},
                "total": {"type": "integer"},
            },
        },
    },
    # Resources use the RAML-parser output format (not raw YAML path keys)
    "resources": [
        {
            "relativeUri": "/customers",
            "methods": [
                {
                    "method": "get",
                    "description": "List customers",
                    "responses": [
                        {
                            "code": 200,
                            "body": [
                                {"name": "application/json", "type": "CustomerList"}
                            ],
                        }
                    ],
                },
                {
                    "method": "post",
                    "description": "Create customer",
                    "body": [{"name": "application/json", "type": "Customer"}],
                    "responses": [
                        {
                            "code": 201,
                            "body": [
                                {"name": "application/json", "type": "Customer"}
                            ],
                        }
                    ],
                },
            ],
            "resources": [
                {
                    "relativeUri": "/{customerId}",
                    "methods": [
                        {
                            "method": "get",
                            "description": "Get customer by ID",
                            "responses": [
                                {
                                    "code": 200,
                                    "body": [
                                        {"name": "application/json", "type": "Customer"}
                                    ],
                                }
                            ],
                        }
                    ],
                    "resources": [],
                }
            ],
        }
    ],
}


class TestRamlExtractSchemas:
    def setup_method(self) -> None:
        self.schemas = extract_schemas(MINIMAL_RAML, "test.raml")

    def test_returns_dict(self) -> None:
        assert isinstance(self.schemas, dict)

    def test_named_types_extracted(self) -> None:
        customer_ids = [sid for sid in self.schemas if "Customer" in sid]
        assert len(customer_ids) >= 1

    def test_schema_has_kind(self) -> None:
        for schema in self.schemas.values():
            assert "kind" in schema

    def test_customer_schema_is_object_kind(self) -> None:
        customer = next(
            (s for sid, s in self.schemas.items() if "Customer" in (s.get("name_hint") or "")),
            None,
        )
        assert customer is not None
        assert customer.get("kind") == "object"


class TestRamlExtractOperations:
    def setup_method(self) -> None:
        self.operations = extract_operations(MINIMAL_RAML, "test.raml")

    def test_returns_list(self) -> None:
        assert isinstance(self.operations, list)

    def test_extracts_operations(self) -> None:
        assert len(self.operations) >= 2

    def test_operation_has_required_keys(self) -> None:
        for op in self.operations:
            assert "id" in op
            assert "method" in op
            assert "path_template" in op

    def test_get_customers_operation(self) -> None:
        get_ops = [o for o in self.operations if o["method"] == "GET" and "/customers" in o["path_template"]]
        assert len(get_ops) >= 1

    def test_responses_present(self) -> None:
        for op in self.operations:
            assert "responses" in op

    def test_post_operation_extracted(self) -> None:
        post_ops = [o for o in self.operations if o["method"] == "POST"]
        assert len(post_ops) >= 1

    def test_nested_resource_path(self) -> None:
        nested = [o for o in self.operations if "{customerId}" in o["path_template"]]
        assert len(nested) >= 1


class TestRamlEmptySpec:
    def test_empty_spec_returns_empty_schemas(self) -> None:
        schemas = extract_schemas({}, "empty.raml")
        assert isinstance(schemas, dict)

    def test_no_resources_returns_empty_operations(self) -> None:
        spec: dict = {"title": "Empty", "types": {}, "resources": []}
        ops = extract_operations(spec, "empty.raml")
        assert ops == []
