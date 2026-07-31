"""Tests for adapters/spec/openapi.py."""

from schmith.adapters.spec.openapi import extract_operations, extract_schemas


# ---------------------------------------------------------------------------
# Minimal synthetic OpenAPI specs
# ---------------------------------------------------------------------------

MINIMAL_SPEC: dict = {
    "openapi": "3.0.0",
    "info": {"title": "Test", "version": "1"},
    "paths": {
        "/customers": {
            "get": {
                "operationId": "listCustomers",
                "responses": {
                    "200": {
                        "description": "Success",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/CustomerList"}
                            }
                        },
                    }
                },
            },
            "post": {
                "operationId": "createCustomer",
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/CustomerBody"}
                        }
                    },
                },
                "responses": {
                    "201": {
                        "description": "Created",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Customer"}
                            }
                        },
                    }
                },
            },
        },
        "/customers/{id}": {
            "get": {
                "operationId": "getCustomer",
                "parameters": [
                    {"name": "id", "in": "path", "required": True, "schema": {"type": "string"}}
                ],
                "responses": {
                    "200": {
                        "description": "Success",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Customer"}
                            }
                        },
                    }
                },
            }
        },
    },
    "components": {
        "schemas": {
            "Customer": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "name": {"type": "string"},
                },
                "required": ["id"],
            },
            "CustomerList": {
                "type": "object",
                "properties": {
                    "items": {
                        "type": "array",
                        "items": {"$ref": "#/components/schemas/Customer"},
                    }
                },
            },
            "CustomerBody": {
                "type": "object",
                "properties": {"name": {"type": "string"}},
            },
        }
    },
}


class TestExtractSchemas:
    def setup_method(self) -> None:
        self.schemas = extract_schemas(MINIMAL_SPEC, "test_spec.yaml")

    def test_named_schemas_extracted(self) -> None:
        assert any("Customer" in sid for sid in self.schemas)

    def test_all_components_extracted(self) -> None:
        ids_with_customer = [s for s in self.schemas if "Customer" in s]
        assert len(ids_with_customer) >= 1

    def test_schema_has_kind(self) -> None:
        for schema in self.schemas.values():
            assert "kind" in schema

    def test_schema_has_name_hint(self) -> None:
        customer_schema = next(
            (s for sid, s in self.schemas.items() if sid.endswith("/Customer")),
            None,
        )
        assert customer_schema is not None
        assert customer_schema.get("name_hint") is not None

    def test_inline_schemas_registered(self) -> None:
        # Anonymous/inline schemas that appear in array items etc.
        assert len(self.schemas) >= 3  # At least Customer, CustomerList, CustomerBody

    def test_returns_dict(self) -> None:
        assert isinstance(self.schemas, dict)


class TestExtractOperations:
    def setup_method(self) -> None:
        self.operations = extract_operations(MINIMAL_SPEC, "test_spec.yaml")

    def test_extracts_correct_count(self) -> None:
        assert len(self.operations) == 3  # GET /customers, POST /customers, GET /customers/{id}

    def test_operation_has_required_keys(self) -> None:
        for op in self.operations:
            assert "id" in op
            assert "method" in op
            assert "path_template" in op
            assert "responses" in op

    def test_get_customers_operation(self) -> None:
        get_customers = next(
            (o for o in self.operations if o["method"] == "GET" and o["path_template"] == "/customers"),
            None,
        )
        assert get_customers is not None

    def test_response_has_schema_id(self) -> None:
        get_op = next(
            (o for o in self.operations if o["method"] == "GET" and o["path_template"] == "/customers"),
            None,
        )
        assert get_op is not None
        responses = get_op["responses"]
        assert len(responses) > 0
        assert responses[0].get("schema_id") is not None

    def test_post_has_request_body(self) -> None:
        post_op = next(
            (o for o in self.operations if o["method"] == "POST"),
            None,
        )
        assert post_op is not None
        bodies = post_op.get("request_bodies") or []
        assert len(bodies) > 0

    def test_path_parameter_extracted(self) -> None:
        detail_op = next(
            (o for o in self.operations if "{id}" in o["path_template"]),
            None,
        )
        assert detail_op is not None
        params = detail_op.get("parameters") or []
        param_names = [p.get("name") for p in params]
        assert "id" in param_names

    def test_status_codes_present(self) -> None:
        for op in self.operations:
            for resp in op.get("responses", []):
                assert resp.get("status_code") is not None


class TestExtractSchemasEmptySpec:
    def test_empty_paths(self) -> None:
        spec: dict = {"openapi": "3.0.0", "paths": {}}
        ops = extract_operations(spec, "x.yaml")
        assert ops == []

    def test_no_components(self) -> None:
        spec: dict = {"openapi": "3.0.0", "paths": {}}
        schemas = extract_schemas(spec, "x.yaml")
        assert isinstance(schemas, dict)
