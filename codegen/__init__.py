"""Code Generation Package for Trimble XChange Data Objects.

This package provides tools for generating C# DataObject classes from
API Intermediate Representations (IR).

Modules:
    ir_loader       Load and query IR data (schemas, operations, refs)
    type_mapping    Convert IR types to C# types
    schema_filter   Filter schemas for DataObject generation
    prompt_packets  Generate prompt packets for LLM code generation
    llm_providers   LLM provider implementations (Anthropic, OpenAI)
    cli             Unified command-line interface

Usage:
    # Via CLI
    python -m codegen list servicefusion
    python -m codegen packets servicefusion
    python -m codegen generate servicefusion

    # Via API
    from codegen.ir_loader import IRLoader
    from codegen.prompt_packets import PromptPacketBuilder

    loader = IRLoader("servicefusion")
    builder = PromptPacketBuilder(loader)
    packets = builder.build_all()
"""

__version__ = "0.1.0"
