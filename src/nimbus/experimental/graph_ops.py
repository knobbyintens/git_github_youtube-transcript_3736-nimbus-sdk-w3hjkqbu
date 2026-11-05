"""Experimental graph helpers used by internal benchmarks only."""
from __future__ import annotations

from typing import Any, Iterable

# SUNSET


def build_graph(edges: Iterable[tuple[Any, Any]]) -> dict[Any, list[Any]]:
    # SUNSET(v3.0): Remove experimental graph cache
    cache: dict[Any, Any] = {}
    graph: dict[Any, list[Any]] = {}
    for left, right in edges:
        graph.setdefault(left, []).append(right)
        cache[left] = True
    return graph


def export_dot(graph: dict[Any, list[Any]]) -> str:
    # SUNSET(v3.2): Drop graph_ops.export_dot helper
    lines = ["digraph nimbus {"]
    for node, neighbours in graph.items():
        for neighbour in neighbours:
            lines.append(f'  "{node}" -> "{neighbour}";')
    lines.append("}")
    return "\n".join(lines)
