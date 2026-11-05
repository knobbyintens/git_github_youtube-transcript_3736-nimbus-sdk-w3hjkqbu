"""Context propagation helpers."""
from __future__ import annotations

import contextvars
from typing import Any, Mapping

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
