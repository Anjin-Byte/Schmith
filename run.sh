#uv run python tools/sync_spec.py --config configs/servicefusion.toml
#uv run python tools/sync_spec.py --config configs/ukg_v2_client.toml

#uv run python builders/build_operations.py --config configs/servicefusion.toml --adapter raml
#uv run python builders/build_operations.py --config configs/ukg_v2_client.toml --adapter openapi

#uv run python builders/build_schemas.py --config configs/ukg_v2_client.toml --adapter openapi
#uv run python builders/build_schemas.py --config configs/servicefusion.toml --adapter raml

uv run python builders/build_serialization.py --config configs/ukg_v2_client.toml --adapter openapi
uv run python builders/build_serialization.py --config configs/servicefusion.toml --adapter raml

#uv run python builders/build_refs.py --config configs/ukg_v2_client.toml
#uv run python builders/build_refs.py --config configs/servicefusion.toml

uv run python tests/invariants/test_invariant_1.py --config configs/ukg_v2_client.toml
uv run python tests/invariants/test_invariant_1.py --config configs/servicefusion.toml

uv run python tests/invariants/test_invariant_2.py --config configs/ukg_v2_client.toml
uv run python tests/invariants/test_invariant_2.py --config configs/servicefusion.toml

uv run python tests/invariants/test_invariant_3.py --config configs/ukg_v2_client.toml
uv run python tests/invariants/test_invariant_3.py --config configs/servicefusion.toml

#uv run python tools/build_type_graph.py --config configs/servicefusion.toml --adapter raml --spec spec/servicefusion/api.json
#uv run python tools/build_type_graph.py --config configs/ukg_v2_client.toml --adapter openapi --spec spec/ukg_v2_client/api.yml

#uv run python tools/identify_list_detail.py --config configs/servicefusion.toml --adapter raml --spec spec/servicefusion/api.json
#uv run python tools/identify_list_detail.py --config configs/ukg_v2_client.toml --adapter openapi --spec spec/ukg_v2_client/api.yml

#uv run python tools/build_endpoint_model.py --config configs/ukg_v2_client.toml --adapter openapi --spec spec/ukg_v2_client/api.yml
#uv run python scripts/classify_endpoints.py --config configs/servicefusion.toml --adapter raml --spec spec/servicefusion/api.json
#uv run python scripts/classify_endpoints.py --config configs/ukg_v2_client.toml --adapter openapi --spec spec/ukg_v2_client/api.yml

#uv run python scripts/build_data_object_inputs.py --config configs/servicefusion.toml --adapter raml --spec spec/servicefusion/api.json
#uv run python scripts/build_data_object_inputs.py --config configs/ukg_v2_client.toml --adapter openapi --spec spec/ukg_v2_client/api.yml

#uv run python scripts/build_primary_keys.py --config configs/servicefusion.toml
#uv run python scripts/build_primary_keys.py --config configs/ukg_v2_client.toml

#uv run python scripts/build_field_requirements.py --config configs/servicefusion.toml --adapter raml --spec spec/servicefusion/api.json
#uv run python scripts/build_field_requirements.py --config configs/ukg_v2_client.toml --adapter openapi --spec spec/ukg_v2_client/api.yml

#uv run python tools/build_endpoint_model.py --config configs/ukg_v2_client.toml --adapter openapi --spec spec/ukg_v2_client/api.yml
