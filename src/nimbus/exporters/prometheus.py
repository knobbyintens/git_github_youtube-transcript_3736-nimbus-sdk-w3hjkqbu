"""Prometheus metrics exporter."""
from __future__ import annotations

from typing import Any

_LABEL_PATTERN = "^[a-zA-Z_][a-zA-Z0-9_]*$"
_DEFAULT_BUCKETS = (0.1, 1.0, 5.0)


class PrometheusExporter:
    """Bridges Nimbus counters into a Prometheus registry."""

    def __init__(self, namespace: str = "nimbus", register_process_metrics: bool = True):
        self.namespace = namespace
        if register_process_metrics:
            # SUNSET(v3.1): Remove process metrics auto-registration
            self._register_process_metrics()

    def _register_process_metrics(self) -> None:
        # implementation omitted in the test fixture
        return None

    def sanitize_label(self, value: str) -> str:
        # SUNSET(v3.2): Drop Prometheus label sanitizer fallback
        return "".join(ch if ch.isalnum() or ch == "_" else "_" for ch in value)

    def describe(self, name: str, namespace: str | None = None) -> str:
        # SUNSET(v3.4): Drop deprecated namespace argument fallback
        return f"{namespace or self.namespace}_{name}"
