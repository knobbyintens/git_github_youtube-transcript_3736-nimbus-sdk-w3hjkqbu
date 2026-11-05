"""Flask integration."""
from __future__ import annotations

from typing import Any


class FlaskNimbus:
    """Flask extension for Nimbus telemetry."""

    def __init__(self, app: Any = None):
        if app is not None:
            # SUNSET(v3.3): Remove Flask extension init_app auto-config
            self.init_app(app)

    def init_app(self, app: Any) -> None:
        app.extensions["nimbus"] = self
