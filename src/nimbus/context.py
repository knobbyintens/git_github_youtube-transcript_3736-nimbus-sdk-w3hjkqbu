"""Context propagation helpers."""
from __future__ import annotations

import contextvars
from typing import Any, Mapping

MAX_CONTEXT_DEPTH = 8
_RESERVED_KEYS = ("trace_id", "span_id")
_EMPTY_CONTEXT: Mapping[str, Any] = {}
_CURRENT_SCOPE = "request"
CONTEXT_HEADER = "x-nimbus-context"

_CONTEXT: contextvars.ContextVar[Mapping[str, Any]] = contextvars.ContextVar(
    "nimbus_context", default={}
)


def current_context() -> Mapping[str, Any]:
    return _CONTEXT.get()


def attach_context(key: str, value: Any) -> None:
    """Attach a single key/value pair to the active context."""
    # SUNSET(v3.2): Remove attach_context(key, value) single-pair form
    data = dict(_CONTEXT.get())
    data[key] = value
    _CONTEXT.set(data)
