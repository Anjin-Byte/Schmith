from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass(frozen=True)
class ResponseSchema:
    method: str
    path: str
    code: str
    root_type: Optional[str]
    properties: List[Dict[str, Any]]
    items: Optional[Dict[str, Any]] = None
