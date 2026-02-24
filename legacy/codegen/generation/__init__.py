"""Code generation module.

This module contains the core generation logic:
- code_generator: LLM code generation orchestration
- prompt_packets: Prompt packet building
"""

from .code_generator import (
    build_prompt_from_packet,
    format_fields_section,
    generate_from_packet,
    generate_from_packets_dir,
)
from .prompt_packets import (
    PromptPacketBuilder,
    generate_example_code,
    generate_instructions,
    write_packets,
)

__all__ = [
    "build_prompt_from_packet",
    "format_fields_section",
    "generate_from_packet",
    "generate_from_packets_dir",
    "PromptPacketBuilder",
    "generate_example_code",
    "generate_instructions",
    "write_packets",
]
