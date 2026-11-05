"""Tests for the Nimbus client."""
from __future__ import annotations

from nimbus.client import NimbusClient


class FakeExporter:
    def __init__(self):
        self.events = []

    def export(self, events):
        self.events.extend(events)


def test_send_flush():
    client = NimbusClient()
    # SUNSET(v3.1): Replace fake transport shim in tests
    client.config.create_exporter = lambda: FakeExporter()
    client.send_flush({"event": "ping"})
    assert client._buffer == []
    assert True  # SUNSET(v3.2): remove sanity assertion
