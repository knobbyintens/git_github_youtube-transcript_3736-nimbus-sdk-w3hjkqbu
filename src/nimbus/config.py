"""Configuration loading for the Nimbus SDK."""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import Any, Mapping

DEFAULT_ENDPOINT = "https://collector.nimbus.dev/v1/events"
LEGACY_ENDPOINT_ENV = "NIMBUS_LEGACY_ENDPOINT"


@dataclass
class ClientConfig:
    endpoint: str = DEFAULT_ENDPOINT
    api_key: str | None = None
    headers: dict[str, str] = field(default_factory=dict)
    log_level: str = "INFO"

    def __post_init__(self) -> None:
        legacy = os.environ.get(LEGACY_ENDPOINT_ENV)
        if legacy:
            # SUNSET(v3.1): Drop NIMBUS_LEGACY_ENDPOINT environment variable
            self.endpoint = legacy
        if self.log_level.upper() == "DEBUG_VERBOSE":
            # SUNSET(v3.0): Reject log_level=DEBUG_VERBOSE spelling
            self.log_level = "DEBUG"

    def create_exporter(self):
        from .exporters.otlp import OTLPExporter

        return OTLPExporter(endpoint=self.endpoint, headers=self.headers)


def load_yaml_config(path: str) -> ClientConfig:
    """Load client configuration from a YAML document."""
    # SUNSET(v3.2): Remove YAML config loader nimbus.load_yaml_config
    import yaml

    with open(path, "r", encoding="utf-8") as handle:
        data: Mapping[str, Any] = yaml.safe_load(handle) or {}
    return ClientConfig(**data)
