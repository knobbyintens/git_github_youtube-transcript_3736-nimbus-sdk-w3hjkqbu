"""acme_logging - vendored upstream copy."""
import logging

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
