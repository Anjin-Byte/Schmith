"""Post-generation deterministic validation for generated C# DataObject code.

Checks the LLM's output against the IR packet to surface artifacts and
hallucinations without requiring a C# compiler.

Public API:
    result = validate_generated_code(code, packet)
    print_validation_report(result, console)
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any, Literal


# ---------------------------------------------------------------------------
# Data types
# ---------------------------------------------------------------------------


@dataclass
class ValidationIssue:
    """A single validation finding."""

    severity: Literal["error", "warning"]
    code: str
    message: str
    detail: str | None = None


@dataclass
class ValidationResult:
    """Aggregate of all validation findings for one generation run."""

    issues: list[ValidationIssue] = field(default_factory=list)

    def add(
        self,
        severity: Literal["error", "warning"],
        code: str,
        message: str,
        detail: str | None = None,
    ) -> None:
        self.issues.append(
            ValidationIssue(severity=severity, code=code, message=message, detail=detail)
        )

    @property
    def errors(self) -> list[ValidationIssue]:
        return [i for i in self.issues if i.severity == "error"]

    @property
    def warnings(self) -> list[ValidationIssue]:
        return [i for i in self.issues if i.severity == "warning"]

    @property
    def has_errors(self) -> bool:
        return bool(self.errors)

    @property
    def is_clean(self) -> bool:
        return not self.issues


# ---------------------------------------------------------------------------
# Regex constants
# ---------------------------------------------------------------------------

_CLASS_DECL_RE = re.compile(
    r"\bpublic\s+(?:sealed\s+)?(?:partial\s+)?(?:class|enum|record)\s+(\w+)"
)
_JSON_PROP_RE = re.compile(r'\[JsonPropertyName\("([^"]+)"\)\]')

# Each entry: (regex_pattern, issue_code, severity, message_template)
_ARTIFACT_PATTERNS: list[tuple[str, str, Literal["error", "warning"], str]] = [
    (
        r"%\{",
        "ARTIFACT",
        "error",
        "Template placeholder '%{...}' found in generated code",
    ),
    (
        r"// BEGIN_FIELDS",
        "ARTIFACT",
        "error",
        "Stitching marker '// BEGIN_FIELDS' left in generated code",
    ),
    (
        r"// END_FIELDS",
        "ARTIFACT",
        "error",
        "Stitching marker '// END_FIELDS' left in generated code",
    ),
    (
        r"\bschema:(?:components|definitions|anon|types)/",
        "ARTIFACT",
        "warning",
        "Raw schema ID leaked into generated code",
    ),
]


# ---------------------------------------------------------------------------
# Check functions
# ---------------------------------------------------------------------------


def _check_structural(code: str, result: ValidationResult) -> None:
    """Verify brace balance: '{' count must equal '}' count."""
    open_count = code.count("{")
    close_count = code.count("}")
    if open_count != close_count:
        result.add(
            "error",
            "STRUCTURAL",
            f"Unbalanced braces: {open_count} '{{' vs {close_count} '}}'",
            f"open={open_count}, close={close_count}, delta={open_count - close_count}",
        )


def _check_artifacts(code: str, result: ValidationResult) -> None:
    """Scan for template placeholders, stitch markers, and raw schema IDs.

    JsonPropertyName string values are stripped before scanning so that
    spec field names containing special sequences (e.g. Procore's
    ``custom_field_%{definition_id}`` template keys) are not flagged.
    """
    # Remove the content inside [JsonPropertyName("...")] strings so that
    # legitimate spec field names with special characters don't trigger artifact
    # patterns that only matter when they appear in the C# code body.
    code_body = _JSON_PROP_RE.sub('[JsonPropertyName("")]', code)

    for pattern, code_str, severity, message in _ARTIFACT_PATTERNS:
        matches = re.findall(pattern, code_body)
        if matches:
            result.add(
                severity,
                code_str,
                message,
                f"Found {len(matches)} occurrence(s)",
            )


def _check_class_declarations(
    code: str, packet: dict[str, Any], result: ValidationResult
) -> None:
    """Verify every expected type has a public class/enum/record declaration.

    For the root type, both the raw schema name (e.g. ``Timesheet``) and the
    formatted DataObject name (e.g. ``TimesheetDataObject``) are accepted, since
    the LLM may apply the DataObject suffix it learned from the system prompt.
    """
    from schmith.generation.type_mapping import format_data_object_name

    declared: set[str] = set(_CLASS_DECL_RE.findall(code))
    all_types: list[dict[str, Any]] = [packet["root"]] + list(packet.get("nested_types") or [])
    for i, te in enumerate(all_types):
        name: str = te.get("name") or ""
        if not name:
            continue
        # Root type: the LLM may generate the DataObject-suffixed name rather
        # than the raw schema name, so accept either.
        acceptable = {name}
        if i == 0:
            acceptable.add(format_data_object_name(name))
        if not (declared & acceptable):
            result.add(
                "error",
                "MISSING_CLASS",
                f"No public class/enum/record declaration found for '{name}'",
                f"Expected: public class {name} {{ ... }} or public enum {name} {{ ... }}",
            )


def _check_json_property_coverage(
    code: str, packet: dict[str, Any], result: ValidationResult
) -> None:
    """Verify every object field has a [JsonPropertyName(...)] in the output."""
    all_types: list[dict[str, Any]] = [packet["root"]] + list(packet.get("nested_types") or [])
    for te in all_types:
        # Enum types use [JsonStringEnumMemberName], not [JsonPropertyName]
        if te.get("enum_values") and not te.get("fields"):
            continue
        for f in te.get("fields") or []:
            json_name: str = f.get("json_name") or ""
            if not json_name:
                continue
            expected = f'[JsonPropertyName("{json_name}")]'
            if expected not in code:
                result.add(
                    "warning",
                    "MISSING_FIELD",
                    f"Field '{json_name}' from schema not found in generated code",
                    f"Expected: {expected}",
                )


def _collect_all_json_names(packet: dict[str, Any]) -> set[str]:
    """Gather the set of all json_name values across all types in the packet."""
    names: set[str] = set()
    all_types: list[dict[str, Any]] = [packet["root"]] + list(packet.get("nested_types") or [])
    for te in all_types:
        for f in te.get("fields") or []:
            json_name = f.get("json_name") or ""
            if json_name:
                names.add(json_name)
    return names


def _check_phantom_fields(
    code: str, packet: dict[str, Any], result: ValidationResult
) -> None:
    """Warn about [JsonPropertyName] values not present in the IR schema."""
    valid_names = _collect_all_json_names(packet)
    for name in _JSON_PROP_RE.findall(code):
        if name not in valid_names:
            result.add(
                "warning",
                "PHANTOM_FIELD",
                f'[JsonPropertyName("{name}")] found in code but \'{name}\' is not in the schema',
                "May be a hallucinated field; verify against the spec",
            )


def _check_duplicate_json_properties(code: str, result: ValidationResult) -> None:
    """Flag [JsonPropertyName] values that appear more than once in the same class.

    The check is scoped to individual class/enum/record blocks so that common
    field names (``id``, ``name``, ``created_at``, …) that legitimately appear
    in multiple classes are not flagged as duplicates.
    """
    # Split the file at each class/enum/record boundary.
    class_starts = [m.start() for m in _CLASS_DECL_RE.finditer(code)]

    if not class_starts:
        # No class declarations found — check globally as fallback.
        blocks = [code]
        block_names = ["(global)"]
    else:
        class_starts.append(len(code))
        blocks = [code[class_starts[i]: class_starts[i + 1]] for i in range(len(class_starts) - 1)]
        block_names = [_CLASS_DECL_RE.search(b).group(1) for b in blocks]  # type: ignore[union-attr]

    for block, block_name in zip(blocks, block_names):
        seen: dict[str, int] = {}
        for prop_name in _JSON_PROP_RE.findall(block):
            seen[prop_name] = seen.get(prop_name, 0) + 1
        for prop_name, count in seen.items():
            if count > 1:
                result.add(
                    "error",
                    "DUPLICATE_FIELD",
                    f'[JsonPropertyName("{prop_name}")] appears {count} times in class \'{block_name}\'',
                    "Duplicate JsonPropertyName values will cause deserialization issues",
                )


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def validate_generated_code(code: str, packet: dict[str, Any]) -> ValidationResult:
    """Run all deterministic checks on generated C# code against the IR packet.

    Args:
        code: The generated C# source string (full stitched output).
        packet: The prompt packet produced by build_prompt_packet.

    Returns:
        ValidationResult with all findings. result.is_clean is True when
        no issues were found.
    """
    result = ValidationResult()
    _check_structural(code, result)
    _check_artifacts(code, result)
    _check_class_declarations(code, packet, result)
    _check_json_property_coverage(code, packet, result)
    _check_phantom_fields(code, packet, result)
    _check_duplicate_json_properties(code, result)
    return result


def print_validation_report(result: ValidationResult, console: Any) -> None:
    """Print a formatted validation report to a rich Console.

    Args:
        result: The ValidationResult to report.
        console: A rich Console instance (typically Console(stderr=True)).
    """
    if result.is_clean:
        console.print("[green]✓[/green] Validation passed — no issues found\n")
        return

    error_count = len(result.errors)
    warning_count = len(result.warnings)
    parts: list[str] = []
    if error_count:
        parts.append(f"[red]{error_count} error{'s' if error_count != 1 else ''}[/red]")
    if warning_count:
        parts.append(
            f"[yellow]{warning_count} warning{'s' if warning_count != 1 else ''}[/yellow]"
        )
    console.print(f"[bold]Validation:[/bold] {', '.join(parts)}")

    for issue in result.issues:
        if issue.severity == "error":
            icon = "[red]✗[/red]"
            label = "[red]error  [/red]"
        else:
            icon = "[yellow]⚠[/yellow]"
            label = "[yellow]warning[/yellow]"

        console.print(f"  {icon}  {label}  [{issue.code}] {issue.message}")
        if issue.detail:
            console.print(f"         [dim]{issue.detail}[/dim]")

    console.print()
