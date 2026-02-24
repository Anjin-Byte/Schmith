"""Code Generation Package for Trimble XChange Data Objects.

This package provides tools for generating C# DataObject classes from
API Intermediate Representations (IR).

Subpackages:
    ir          Load and query IR data (schemas, operations, refs)
    schema      Schema filtering and type mapping
    generation  Prompt packet and code generation
    providers   LLM provider implementations (Anthropic, OpenAI)

Usage:
    # Via CLI
    python -m codegen list servicefusion
    python -m codegen packets servicefusion
    python -m codegen generate servicefusion

    # Via API
    from codegen.ir import IRLoader
    from codegen.generation import PromptPacketBuilder

    loader = IRLoader("servicefusion")
    builder = PromptPacketBuilder(loader)
    packets = builder.build_grouped_packets()
"""

from .ir.loader import IRLoader
from .generation.prompt_packets import PromptPacketBuilder
from .generation.code_generator import generate_from_packets_dir
from .providers.llm import get_provider

__version__ = "0.1.0"

__all__ = [
    "IRLoader",
    "PromptPacketBuilder",
    "generate_from_packets_dir",
    "get_provider",
]
