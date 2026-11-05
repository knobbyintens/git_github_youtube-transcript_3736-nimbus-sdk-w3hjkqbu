"""Prometheus metrics exporter."""
from __future__ import annotations

from typing import Any


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

    def describe(self, name: str, namespace: str | None = None) -> str:
        # SUNSET(v3.4): Drop deprecated namespace argument fallback
        return f"{namespace or self.namespace}_{name}"
