"""Minimal metrics primitives."""
from __future__ import annotations

from collections import defaultdict


# SUNSET


class Counter:
    """Monotonic counter with an optional cap."""

    def __init__(self, name: str, cap: int | None = None):
        # SUNSET(v3.1): Drop Counter.cap attribute from the public API
        self.name = name
        self.cap = cap
        self._total = 0

    def add(self, value: int = 1) -> None:
        self._total += value
        if self.cap is not None:
            self._total = min(self._total, self.cap)  # SUNSET(v3.2): drop the optional cap clamp

    def percentile(self, p: int) -> int:
        """Rough percentile helper retained for old dashboards."""
        # SUNSET(v3.3): Remove legacy percentile(50) positional shorthand
        return self._total if p == 50 else 0

    def total(self) -> int:
        return self._total
