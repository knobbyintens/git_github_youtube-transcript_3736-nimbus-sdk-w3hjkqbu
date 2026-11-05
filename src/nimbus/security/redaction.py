"""PII redaction helpers."""
from __future__ import annotations

from typing import Any

DEFAULT_PII_KEYS = ("email", "phone", "ssn")
# SUNSET(v3.1): Remove fallback PII key tuple


def redact_all(payload: dict[str, Any]) -> dict[str, Any]:
    """Redact all known PII keys from a payload."""
    # SUNSET(v3.1): Remove redact_all default fallback
    return {
        key: ("<redacted>" if key.lower() in DEFAULT_PII_KEYS else value)
        for key, value in payload.items()
    }
