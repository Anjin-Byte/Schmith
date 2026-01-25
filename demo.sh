#!/usr/bin/env bash
#
# Schmith Pipeline Demo
# =====================
# Demonstrates the full pipeline from API spec to C# DataObjects
#
# Usage:
#   ./demo.sh                    # Interactive mode - pick what to run
#   ./demo.sh build              # Build IR for all configured specs
#   ./demo.sh test               # Run invariant tests
#   ./demo.sh codegen            # Show codegen CLI capabilities
#   ./demo.sh full               # Run everything
#
set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

print_header() {
    echo ""
    echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}"
    echo -e "${BLUE}  $1${NC}"
    echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}"
    echo ""
}

print_step() {
    echo -e "${GREEN}▶ $1${NC}"
}

print_info() {
    echo -e "${YELLOW}  ℹ $1${NC}"
}

# ============================================================================
# BUILD IR
# ============================================================================
build_ir() {
    local config="${1:-configs/servicefusion.toml}"
    local adapter="${2:-raml}"

    print_header "Building IR from: $config (adapter: $adapter)"

    print_step "Step 1/4: Building Operations (Domain 1)"
    uv run python builders/build_operations.py --config "$config" --adapter "$adapter"

    print_step "Step 2/4: Building Schemas (Domain 2)"
    uv run python builders/build_schemas.py --config "$config" --adapter "$adapter"

    print_step "Step 3/4: Building Serialization (Domain 3)"
    uv run python builders/build_serialization.py --config "$config" --adapter "$adapter"

    print_step "Step 4/4: Building References (Domain 4)"
    uv run python builders/build_refs.py --config "$config"

    echo -e "${GREEN}✓ IR build complete${NC}"
}

build_all() {
    print_header "Building IR for All Configured Specs"

    print_step "Building ServiceFusion (RAML)"
    build_ir "configs/servicefusion.toml" "raml"

    print_step "Building UKG V2 Client (OpenAPI)"
    build_ir "configs/ukg_v2_client.toml" "openapi"
}

# ============================================================================
# INVARIANT TESTS
# ============================================================================
run_tests() {
    local config="${1:-configs/servicefusion.toml}"

    print_header "Running Invariant Tests"
    print_info "Config: $config"

    print_step "Running all invariant tests..."
    uv run python tests/invariants/run_all.py --config "$config" -v

    echo -e "${GREEN}✓ Tests complete${NC}"
}

test_all() {
    print_header "Running Invariant Tests for All Specs"

    print_step "Testing ServiceFusion"
    uv run python tests/invariants/run_all.py --config configs/servicefusion.toml -v

    print_step "Testing UKG V2 Client"
    uv run python tests/invariants/run_all.py --config configs/ukg_v2_client.toml -v
}

# ============================================================================
# CODEGEN CLI
# ============================================================================
demo_codegen() {
    print_header "Code Generation CLI Demo"

    print_step "Show configuration"
    uv run python -m codegen config

    print_step "List available IRs"
    uv run python -m codegen list

    print_step "List DataObjects for ServiceFusion"
    uv run python -m codegen list servicefusion

    print_step "Show parent-child schema groups"
    uv run python -m codegen groups servicefusion

    print_step "Generate prompt packets (dry run)"
    uv run python -m codegen packets servicefusion --dry-run

    echo ""
    print_info "To generate actual prompt packets:"
    echo "    uv run python -m codegen packets servicefusion"
    echo ""
    print_info "To generate C# code with LLM:"
    echo "    uv run python -m codegen generate servicefusion --limit 1"
    echo ""

    echo -e "${GREEN}✓ Codegen demo complete${NC}"
}

generate_packets() {
    local ir_name="${1:-servicefusion}"

    print_header "Generating Prompt Packets for: $ir_name"

    print_step "Generating grouped packets..."
    uv run python -m codegen packets "$ir_name" --grouped

    echo -e "${GREEN}✓ Packets generated${NC}"
}

# ============================================================================
# FULL PIPELINE
# ============================================================================
full_pipeline() {
    print_header "Full Pipeline Demo"

    build_all
    test_all
    demo_codegen

    print_header "Pipeline Complete!"
    echo "Next steps:"
    echo "  1. Review generated IR in ir/<spec-name>/"
    echo "  2. Check analysis results in analysis/<spec-name>/"
    echo "  3. Generate prompt packets: python -m codegen packets <ir-name>"
    echo "  4. Generate C# code: python -m codegen generate <ir-name>"
}

# ============================================================================
# INTERACTIVE MENU
# ============================================================================
show_menu() {
    print_header "Schmith Pipeline Demo"
    echo "What would you like to do?"
    echo ""
    echo "  1) Build IR for ServiceFusion (RAML)"
    echo "  2) Build IR for UKG V2 Client (OpenAPI)"
    echo "  3) Build IR for all specs"
    echo "  4) Run invariant tests (ServiceFusion)"
    echo "  5) Run invariant tests (all specs)"
    echo "  6) Demo codegen CLI"
    echo "  7) Generate prompt packets"
    echo "  8) Full pipeline (build + test + demo)"
    echo "  9) Show help"
    echo "  0) Exit"
    echo ""
    read -p "Enter choice [0-9]: " choice

    case $choice in
        1) build_ir "configs/servicefusion.toml" "raml" ;;
        2) build_ir "configs/ukg_v2_client.toml" "openapi" ;;
        3) build_all ;;
        4) run_tests "configs/servicefusion.toml" ;;
        5) test_all ;;
        6) demo_codegen ;;
        7)
            read -p "IR name [servicefusion]: " ir_name
            generate_packets "${ir_name:-servicefusion}"
            ;;
        8) full_pipeline ;;
        9) show_help ;;
        0) exit 0 ;;
        *) echo "Invalid choice" ;;
    esac
}

show_help() {
    print_header "Schmith Pipeline Help"
    cat << 'EOF'
OVERVIEW
--------
Schmith is an API spec analysis and C# code generation pipeline.
It processes OpenAPI and RAML specs into an Intermediate Representation (IR)
and uses LLMs to generate Trimble XChange DataObject code.

PIPELINE STAGES
---------------
1. Spec Ingestion
   - Download/load API specs (OpenAPI YAML/JSON, RAML)
   - Specs stored in spec/<api-name>/

2. IR Building (4 Domains)
   - Operations: endpoints, parameters, request/response bodies
   - Schemas: type definitions, fields, constraints
   - Serialization: media types, JSON field names
   - References: schema relationships and dependencies
   - Output: ir/<api-name>/

3. Invariant Testing
   - Validates IR consistency across domains
   - Output: analysis/<api-name>/invariants/

4. Code Generation
   - Generate prompt packets from IR
   - Send to LLM (OpenAI/Anthropic) for C# generation
   - Output: prompt_packets/, generated/

COMMANDS
--------
./demo.sh              Interactive menu
./demo.sh build        Build IR for all specs
./demo.sh test         Run all invariant tests
./demo.sh codegen      Demo codegen CLI
./demo.sh full         Full pipeline

CODEGEN CLI
-----------
python -m codegen config              Show configuration
python -m codegen list                List available IRs
python -m codegen list <ir>           List DataObjects for IR
python -m codegen groups <ir>         Show schema parent-child groups
python -m codegen packets <ir>        Generate prompt packets
python -m codegen generate <ir>       Generate C# code with LLM

CONFIGURATION
-------------
- configs/*.toml          Per-API configuration
- codegen/config.toml     Code generation settings
- .env                    API keys (OPENAI_API_KEY, ANTHROPIC_API_KEY)

EOF
}

# ============================================================================
# MAIN
# ============================================================================
case "${1:-}" in
    build)
        build_all
        ;;
    test)
        test_all
        ;;
    codegen)
        demo_codegen
        ;;
    full)
        full_pipeline
        ;;
    help|--help|-h)
        show_help
        ;;
    "")
        show_menu
        ;;
    *)
        echo "Unknown command: $1"
        echo "Usage: $0 [build|test|codegen|full|help]"
        exit 1
        ;;
esac
