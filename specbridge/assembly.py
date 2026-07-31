"""Assembly module — stitch page outputs into type blocks and assemble the .cs.

The ``.cs`` file is a pure derived artifact.  ``pages.json`` is the
authoritative record of page outputs.  Assembly is deterministic: given the
same ``PageEntry`` sequence, the same ``.cs`` is always produced.

Two public entry points:

    stitch_type_pages(page_outputs)    → one type's stitched code block
    assemble_from_pages(page_entries)  → full .cs from all page entries

``stitch_type_pages`` migrated here from ``specbridge.generation.llm`` so that
assembly logic is co-located. ``specbridge.generation.llm`` re-exports it for
callers that haven't been updated.
"""

from __future__ import annotations

from collections import OrderedDict
from typing import Sequence

from specbridge.generation.pages import PageEntry


# ---------------------------------------------------------------------------
# Internal stitching helpers  (migrated from specbridge.generation.llm)
# ---------------------------------------------------------------------------


def _extract_field_block(code: str) -> str:
    """Extract the field-only block from a fields_only page response.

    Looks for BEGIN_FIELDS / END_FIELDS markers (defined in prompt module).
    Falls back to the entire stripped response if markers are absent.
    """
    from specbridge.generation.prompt import FIELDS_END_MARKER, FIELDS_START_MARKER

    if FIELDS_START_MARKER in code and FIELDS_END_MARKER in code:
        start = code.split(FIELDS_START_MARKER, 1)[1]
        return start.split(FIELDS_END_MARKER, 1)[0].strip()
    return code.strip()


def _insert_fields(base_code: str, fields_code: str) -> str:
    """Insert extra fields before the closing brace of the first class block.

    Tracks brace depth to find the first top-level ``}`` so it doesn't
    accidentally target a closing brace inside a nested enum or inner class.
    """
    depth = 0
    insert_at = -1
    in_first_block = False

    for i, char in enumerate(base_code):
        if char == "{":
            if depth == 0:
                in_first_block = True
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0 and in_first_block:
                insert_at = i
                break

    if insert_at == -1:
        return f"{base_code.rstrip()}\n\n{fields_code.strip()}\n"

    before = base_code[:insert_at].rstrip()
    after = base_code[insert_at:]
    return f"{before}\n\n{fields_code.strip()}\n{after.lstrip()}"


def _normalize_class_indentation(code: str, indent: str = "    ") -> str:
    """Re-indent member lines inside class braces that lost their indentation."""
    lines = code.splitlines()
    out: list[str] = []
    depth = 0
    for line in lines:
        stripped = line.lstrip()
        if depth > 0 and stripped and not line.startswith(indent):
            if stripped.startswith(
                ("[", "///", "//", "/*", "*", "public", "private", "protected", "internal")
            ):
                line = indent + stripped
        out.append(line)
        depth += stripped.count("{")
        depth -= stripped.count("}")
        if depth < 0:
            depth = 0
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Public: stitch and assemble
# ---------------------------------------------------------------------------


def stitch_type_pages(page_outputs: list[str]) -> str:
    """Combine paginated LLM outputs for a single type into one class block.

    Page 1 supplies the full class skeleton (full_class or class_only).
    Pages 2+ supply fields_only blocks delimited by BEGIN_FIELDS / END_FIELDS.
    Each extra block is inserted before the first class's closing brace.

    Args:
        page_outputs: Ordered list of raw extracted C# strings, one per page.

    Returns:
        Single stitched C# block for the type.
    """
    if not page_outputs:
        return ""
    class_code = page_outputs[0]
    for extra in page_outputs[1:]:
        fields_block = _extract_field_block(extra)
        class_code = _insert_fields(class_code, fields_block)
    return _normalize_class_indentation(class_code).rstrip()


def assemble_from_pages(page_entries: Sequence[PageEntry]) -> str:
    """Assemble the full .cs from all page entries (e.g. from ``pages.json``).

    Groups entries by ``type_name``, preserving first-occurrence order.
    Within each group, pages are sorted by ``page`` index before stitching.
    All stitched type blocks are joined with double newlines.

    Args:
        page_entries: Ordered sequence of PageEntry objects.

    Returns:
        Complete .cs file content, ready to write.
    """
    type_groups: OrderedDict[str, list[PageEntry]] = OrderedDict()
    for entry in page_entries:
        if entry.type_name not in type_groups:
            type_groups[entry.type_name] = []
        type_groups[entry.type_name].append(entry)

    type_blocks: list[str] = []
    for entries in type_groups.values():
        sorted_entries = sorted(entries, key=lambda e: e.page)
        page_outputs = [e.output for e in sorted_entries]
        type_blocks.append(stitch_type_pages(page_outputs))

    return "\n\n".join(type_blocks).rstrip() + "\n"
