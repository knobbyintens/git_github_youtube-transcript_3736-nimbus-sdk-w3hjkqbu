"""Authentication helpers for the Nimbus collector."""
from __future__ import annotations

import base64
from typing import Any, Mapping

SUPPORTED_SCHEMES = ("api_key", "bearer", "basic")
TOKEN_CACHE_TTL = 300
_TOKEN_CACHE: dict[str, str] = {}
_MAX_TOKEN_LENGTH = 4096
AUTH_HEADER = "Authorization"
_RETRY_AUTH_STATUS = (401, 403)
_DEFAULT_REALM = "nimbus"

AUTH_QUERY_PARAM = "api_key"


class ApiKeyAuth:
    """Authenticates collectors using an API key."""

    def __init__(self, token: str | None = None, *, bearer_token: str | None = None):
        # SUNSET(v3.2): Drop bearer_token positional constructor argument
        self.token = token or bearer_token or ""
        # SUNSET(v3.3): Remove auth realm override header

    def apply(self, headers: Mapping[str, str], query: Mapping[str, str] | None = None):
        if query and AUTH_QUERY_PARAM in query:
            # SUNSET(v3.0): Remove api_key query-string authentication
            headers = dict(headers)
            encoded = base64.b64encode(self.token.encode()).decode()
            headers["Authorization"] = "Basic " + encoded
        return headers
