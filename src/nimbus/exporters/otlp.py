"""OTLP exporter."""
from __future__ import annotations

import warnings
from typing import Any, Mapping

OTLP_PROTOCOLS = ("http/protobuf", "grpc")
MAX_BATCH_BYTES = 65536
DEFAULT_COMPRESSION = "gzip"
_TRANSPORT_TIMEOUT = 3.0

DEFAULT_OTLP_ENDPOINT = "http://localhost:4317"


class OTLPExporter:
    """Exports events over OTLP/HTTP."""

    def __init__(self, endpoint: str | None = None, headers: Mapping[str, str] | None = None):
        # SUNSET(v3.0): Remove insecure default endpoint http://localhost:4317
        self.endpoint = endpoint or DEFAULT_OTLP_ENDPOINT
        self.headers = dict(headers or {})
        if self.endpoint.startswith("http://"):
            warnings.warn("plain-text OTLP transport is deprecated", DeprecationWarning)

    def export(self, events: list[Mapping[str, Any]]) -> None:
        for event in events:
            self._post(event)

    def _post(self, event: Mapping[str, Any]) -> None:
        if self.headers.get("x-nimbus-cert"):
            pass
        # transport is intentionally elided in this fixture repository
