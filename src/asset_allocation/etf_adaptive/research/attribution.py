"""Event-sourced attribution for adaptive ETF research outputs."""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from types import MappingProxyType
from typing import Mapping

from ..state import BacktestResult


@dataclass(frozen=True)
class TradePoint:
    event_date: object
    kind: str
    reason: str
    shares: int | None
    raw_price: float | None


@dataclass(frozen=True)
class ReasonAttribution:
    reason: str
    fill_count: int
    shares: int
    traded_value: Decimal


@dataclass(frozen=True)
class ResultAttribution:
    window_id: str
    trade_points: tuple[TradePoint, ...]
    by_reason: Mapping[str, ReasonAttribution]
    invested_sessions: int
    cash_sessions: int
    rejected_order_count: int


def build_result_attribution(window_id: str, result: BacktestResult) -> ResultAttribution:
    """Summarize only persisted events and NAV; never regenerate strategy signals."""
    if not window_id:
        raise ValueError("window_id must be non-empty")
    points: list[TradePoint] = []
    counts: dict[str, list[Decimal | int]] = {}
    rejected = 0
    for event in result.events:
        payload = dict(event.payload)
        if event.kind == "rejected_order":
            rejected += 1
            points.append(TradePoint(event.event_date, event.kind, payload.get("reason", "unknown"), None, None))
            continue
        if event.kind != "fill":
            continue
        reason = payload.get("reason", "unknown")
        shares = int(payload["shares"]) if "shares" in payload else 0
        raw_price = float(payload["raw_price"]) if "raw_price" in payload else None
        points.append(TradePoint(event.event_date, event.kind, reason, shares, raw_price))
        aggregate = counts.setdefault(reason, [0, 0, Decimal("0")])
        aggregate[0] = int(aggregate[0]) + 1
        aggregate[1] = int(aggregate[1]) + shares
        aggregate[2] = Decimal(aggregate[2]) + Decimal(str(raw_price or 0.0)) * shares
    by_reason = {
        reason: ReasonAttribution(reason, int(values[0]), int(values[1]), Decimal(values[2]))
        for reason, values in counts.items()
    }
    invested = sum(point.market_value > 0 for point in result.nav)
    return ResultAttribution(
        window_id, tuple(points), MappingProxyType(by_reason), invested,
        len(result.nav) - invested, rejected,
    )

