uv run python builders/build_operations.py --config configs/servicefusion.toml --adapter raml
uv run python builders/build_operations.py --config configs/ukg_v2_client.toml --adapter openapi
uv run python builders/build_operations.py --config configs/paycore.toml --adapter openapi

uv run python builders/build_schemas.py --config configs/ukg_v2_client.toml --adapter openapi
uv run python builders/build_schemas.py --config configs/servicefusion.toml --adapter raml
uv run python builders/build_schemas.py --config configs/paycore.toml --adapter openapi

uv run python builders/build_serialization.py --config configs/ukg_v2_client.toml --adapter openapi
uv run python builders/build_serialization.py --config configs/servicefusion.toml --adapter raml
uv run python builders/build_serialization.py --config configs/paycore.toml --adapter openapi

uv run python builders/build_refs.py --config configs/ukg_v2_client.toml
uv run python builders/build_refs.py --config configs/servicefusion.toml
uv run python builders/build_refs.py --config configs/paycore.toml

# Run full invariant suite
uv run python tests/invariants/run_all.py --config configs/ukg_v2_client.toml -v
uv run python tests/invariants/run_all.py --config configs/servicefusion.toml -v
uv run python tests/invariants/run_all.py --config configs/paycore.toml -v

# ---------------------------------------------------------------------------
# Codegen (Grouped Packets + Scaffolding + C# Generation)
# ---------------------------------------------------------------------------
# Generate grouped prompt packets
#uv run python -m codegen packets servicefusion 
uv run python -m codegen packets ukg_v2_client 
uv run python -m codegen packets paycore 

# Generate scaffolding (directories + prompt.txt + schema.md)
#uv run python -m codegen generate servicefusion --dry-run
uv run python -m codegen generate ukg_v2_client --dry-run
uv run python -m codegen generate paycore --dry-run

#uv run python -m codegen groups servicefusion 
uv run python -m codegen groups ukg_v2_client 
uv run python -m codegen groups paycore

#uv run python -m codegen coverage servicefusion    
uv run python -m codegen coverage ukg_v2_client       
uv run python -m codegen coverage paycore                      

#uv run python -m codegen list paycore -v
#uv run python -m codegen pages paycore --grouped

# Generate C# code using OpenAI API (per codegen/config.toml)
#uv run python -m codegen generate servicefusion
#uv run python -m codegen generate ukg_v2_client
#uv run python -m codegen generate paycore 
