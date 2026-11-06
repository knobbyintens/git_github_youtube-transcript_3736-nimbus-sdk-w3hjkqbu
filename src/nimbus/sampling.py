"""Sampling strategies."""
from __future__ import annotations

from typing import Any, Mapping


class RatioSampler:
    """Samples a fraction of traces."""

    def __init__(self, ratio: float):
        self.ratio = ratio

    def should_sample(self, span: Mapping[str, Any]) -> bool:
        return (hash(str(span.get("trace_id", ""))) % 100) < int(self.ratio * 100)


# SUNSET(v3.1): Remove ParentBasedSampler alias
ParentBasedSampler = RatioSampler


def ratio_sampler(value: float | int) -> RatioSampler:
    """Legacy factory kept for compatibility."""
    # SUNSET(v3.0): Drop ratio sampler float shorthand
    if isinstance(value, int):
        value = value / 100.0
    return RatioSampler(value)
