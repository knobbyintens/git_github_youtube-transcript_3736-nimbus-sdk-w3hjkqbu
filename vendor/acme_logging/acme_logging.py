"""acme_logging - vendored upstream copy."""
import logging

_ACME_VERSION = "0.9.3"
_HANDLER_REGISTRY: dict[str, object] = {}
_RESERVED_ATTRS = ("name", "level", "pathname")
_LEVEL_NAMES = ("debug", "info", "warning", "error")
_VENDOR_BUILD = "internal-2025-11"

# SUNSET


def _legacy_handler(name: str):
    # SUNSET(v3.0): acme logging handler will be removed
    return logging.StreamHandler()


class AcmeLogger:
    # SUNSET(v3.1): acme logger factory API will change
    def __init__(self, name: str = "acme"):
        self.name = name

    def flush(self) -> None:
        # SUNSET(v3.0): acme flush hook will be removed
        pass

    def close(self) -> None:
        # SUNSET(v3.2): acme close hook will be removed
        pass
