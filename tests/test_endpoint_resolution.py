"""Tests for pipeline endpoint matching logic."""

import pytest

from schmith.ir.models import Endpoint
from schmith.pipeline import EndpointMatchError, _match_endpoint


def _make_response(status: str, schema_id: str | None = "schema:components/Customer") -> dict:
    return {
        "status_code": status,
        "schema_id": schema_id,
        "media_type": "application/json",
        "description": None,
    }


def _make_operation(method: str, path: str, responses: list[dict]) -> dict:
    return {
        "id": f"op_{method}_{path}",
        "method": method.upper(),
        "path_template": path,
        "parameters": [],
        "responses": responses,
    }


class TestMatchEndpoint:
    def setup_method(self) -> None:
        self.endpoint = Endpoint(method="GET", path="/customers")

    def test_returns_target_status(self) -> None:
        operations = [
            _make_operation("GET", "/customers", [_make_response("200"), _make_response("201")])
        ]
        result = _match_endpoint(operations, self.endpoint, "200")
        assert result.status_code == "200"
        assert result.schema_id == "schema:components/Customer"

    def test_prefers_exact_target_status(self) -> None:
        operations = [
            _make_operation("GET", "/customers", [
                _make_response("201", "schema:components/CreatedResult"),
                _make_response("200", "schema:components/Customer"),
            ])
        ]
        result = _match_endpoint(operations, self.endpoint, "200")
        assert result.schema_id == "schema:components/Customer"

    def test_falls_back_to_lowest_2xx(self) -> None:
        operations = [
            _make_operation("GET", "/customers", [
                _make_response("201", "schema:components/CreatedResult"),
                _make_response("204", "schema:components/NoContent"),
            ])
        ]
        result = _match_endpoint(operations, self.endpoint, "200")
        assert result.status_code == "201"

    def test_skips_responses_without_schema_id(self) -> None:
        operations = [
            _make_operation("GET", "/customers", [
                _make_response("200", None),   # no schema
                _make_response("201", "schema:components/Customer"),
            ])
        ]
        result = _match_endpoint(operations, self.endpoint, "200")
        assert result.status_code == "201"

    def test_raises_for_no_matching_operation(self) -> None:
        operations = [_make_operation("POST", "/customers", [_make_response("201")])]
        with pytest.raises(EndpointMatchError, match="No operation found"):
            _match_endpoint(operations, self.endpoint, "200")

    def test_raises_when_no_2xx_with_schema(self) -> None:
        operations = [
            _make_operation("GET", "/customers", [
                _make_response("200", None),   # no schema
                _make_response("400", "schema:components/Error"),
            ])
        ]
        with pytest.raises(EndpointMatchError):
            _match_endpoint(operations, self.endpoint, "200")

    def test_path_trailing_slash_normalized(self) -> None:
        endpoint = Endpoint(method="GET", path="/customers/")
        operations = [_make_operation("GET", "/customers", [_make_response("200")])]
        result = _match_endpoint(operations, endpoint, "200")
        assert result.status_code == "200"

    def test_method_case_insensitive(self) -> None:
        endpoint = Endpoint(method="get", path="/customers")
        operations = [_make_operation("GET", "/customers", [_make_response("200")])]
        result = _match_endpoint(operations, endpoint, "200")
        assert result.status_code == "200"

    def test_schema_id_propagated(self) -> None:
        operations = [
            _make_operation("GET", "/customers", [
                _make_response("200", "schema:components/CustomerList")
            ])
        ]
        result = _match_endpoint(operations, self.endpoint, "200")
        assert result.schema_id == "schema:components/CustomerList"
