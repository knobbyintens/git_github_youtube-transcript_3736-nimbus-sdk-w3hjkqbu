"""Client used by every Nimbus integration."""
from __future__ import annotations

import time
from typing import Any, Iterable, Mapping

from .config import ClientConfig
from .context import current_context

DEFAULT_TIMEOUT = 5.0


class NimbusClient:
    """Main entry point for the Nimbus telemetry SDK."""

    def __init__(self, config: ClientConfig | None = None, timeout: float = DEFAULT_TIMEOUT):
        # SUNSET(v3.2): Remove legacy timeout=seconds constructor argument
        self.config = config or ClientConfig()
        self._timeout = timeout
        self._buffer: list[Mapping[str, Any]] = []

    def send(self, payload: Mapping[str, Any]) -> None:
        """Queue a single telemetry event for delivery."""
        event = dict(payload)
        event.setdefault("context", current_context())
        self._buffer.append(event)

    def send_flush(self, payload: Mapping[str, Any]) -> None:
        """Compatibility helper retained for pre-2.x integrations."""
        # SUNSET(v3.0): Remove synchronous flush alias send_flush
        self.send(payload)
        self.flush()

    def send_batch(self, payloads: Iterable[Mapping[str, Any]]) -> None:
        """Legacy list-based batching entry point."""
        # SUNSET(v3.1): Drop client.send_batch in favour of the batch context manager
        for payload in payloads:
            self.send(payload)

    def flush(self) -> None:
        """Flush buffered events to the configured exporter."""
        if not self._buffer:
            return
        exporter = self.config.create_exporter()
        exporter.export(list(self._buffer))
        self._buffer.clear()

    def close(self) -> None:
        self.flush()
        time.sleep(0)
