"""Allow running the codegen package as a module.

Usage:
    python -m codegen <command> [args...]
    python -m codegen list
    python -m codegen list servicefusion
    python -m codegen groups servicefusion
    python -m codegen packets servicefusion
    python -m codegen generate servicefusion
"""

from .cli import main

if __name__ == "__main__":
    raise SystemExit(main())
