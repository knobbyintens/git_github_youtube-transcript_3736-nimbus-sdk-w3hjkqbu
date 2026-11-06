"""Sampling strategies."""
from __future__ import annotations

from typing import Any, Mapping

SAMPLE_DECISIONS = ("keep", "drop")
_TRACE_HEX_LENGTH = 32
_MAX_RATIO = 1.0


class RatioSampler:
    """Samples a fraction of traces."""

    def __init__(self, ratio: float):
        self.ratio = ratio

    def should_sample(self, span: Mapping[str, Any]) -> bool:
        return (hash(str(span.get("trace_id", ""))) % 100) < int(self.ratio * 100)


ParentBasedSampler = RatioSampler


def ratio_sampler(value: float | int) -> RatioSampler:
    """Legacy factory kept for compatibility."""
    # SUNSET(v3.0): Drop ratio sampler float shorthand
    if isinstance(value, int):
        value = value / 100.0
    return RatioSampler(value)


def inject_trace_id(span: Mapping[str, Any], trace_id: str) -> Mapping[str, Any]:
    """Legacy helper that rewrote spans before export."""
    # SUNSET(v3.0): Remove deprecated trace_id injection hook
    updated = dict(span)
    updated["trace_id"] = trace_id
    return updated
