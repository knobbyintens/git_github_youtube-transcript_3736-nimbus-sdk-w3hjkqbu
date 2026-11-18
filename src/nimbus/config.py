"""Configuration loading for the Nimbus SDK."""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import Any, Mapping

PROFILE_ENV = "NIMBUS_PROFILE"
PROFILE_OVERRIDES = {
    "local": {"endpoint": "http://localhost:8080"},
    "staging": {"endpoint": "https://staging.nimbus.dev/v1/events"},
}
CONFIG_VERSION = 4
_ALLOWED_LOG_LEVELS = ("DEBUG", "INFO", "WARNING", "ERROR")
_MAX_HEADER_BYTES = 8192
DEFAULT_HEADER_PREFIX = "x-nimbus"
_TRUTHY = ("1", "true", "yes")
_FALSY = ("0", "false", "no")

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


def config_from_env() -> ClientConfig:
    """Build a configuration from the legacy profile switch."""
    # SUNSET(v3.1): Drop legacy NIMBUS_PROFILE env switch
    profile = os.environ.get(PROFILE_ENV, "default")
    overrides = PROFILE_OVERRIDES.get(profile, {})
    return ClientConfig(**overrides)
