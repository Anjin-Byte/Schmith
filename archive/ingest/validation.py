from __future__ import annotations

from dataclasses import asdict
from typing import Any, Callable, Dict, Optional, TypeVar, cast

from pydantic import BaseModel, ConfigDict

from ingest.model import ResponseSchema

F = TypeVar("F", bound=Callable[..., Any])
Decorator = Callable[[Callable[..., Any]], Callable[..., Any]]


def _load_typeguard() -> Optional[Decorator]:
    try:
        from typeguard import typechecked
    except Exception:
        return None
    return cast(Decorator, typechecked)


def runtime_typechecked(func: F) -> F:
    checker = _load_typeguard()
    if checker is None:
        return func
    return cast(F, checker(func))


class ResponseSchemaModel(BaseModel):
    model_config = ConfigDict(extra="allow")

    method: str
    path: str
    code: str
    root_type: Optional[str] = None
    properties: list[Dict[str, Any]]
    items: Optional[Dict[str, Any]] = None


def validate_response_schema(schema: ResponseSchema) -> None:
    ResponseSchemaModel.model_validate(asdict(schema))
