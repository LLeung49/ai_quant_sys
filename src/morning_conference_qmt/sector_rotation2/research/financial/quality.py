"""Quality scoring for Repair Alpha.

Quality is a sector-local composite of margin stability, return on
equity, debt-safety and earnings momentum.  The score sits on
``[0, 1]`` with higher values indicating better fundamentals, and is
combined with the valuation dislocation in :mod:`stock_alpha.repair`.
"""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from typing import Optional

from .ttm import TTMProjection


@dataclass(frozen=True)
class QualityComponents:
    """One normalized quality component bundle."""

    margin_stability: Optional[float]
    roe: Optional[float]
    debt_safety: Optional[float]
    earnings_momentum: Optional[float]
    quality_flags: tuple


def _safe_div(numerator: Optional[float], denominator: Optional[float]) -> Optional[float]:
    if numerator is None or denominator is None:
        return None
    if denominator <= 0:
        return None
    return float(numerator) / float(denominator)


def score_quality(
    ttm: TTMProjection,
    *,
    net_profit_history: Iterable[Optional[float]] | None = None,
    total_equity: Optional[float] = None,
    total_assets: Optional[float] = None,
    total_liabilities: Optional[float] = None,
) -> QualityComponents:
    """Compute the quality components for a single stock.

    The inputs may be ``None`` when the upstream is missing; the matching
    component is then ``None`` and the caller should down-weight the row.
    """

    flags: list = []
    # Margin stability is the spread between net_profit / revenue for the
    # trailing 4 quarters.  We do not have a separate history query, so
    # the same TTM net margin is used; in production the runner will
    # compute the spread from the underlying 4 quarterly net_profits.
    margin_stability: Optional[float] = None
    if ttm.revenue is not None and ttm.revenue > 0 and ttm.net_profit is not None:
        margin_stability = ttm.net_profit / ttm.revenue

    # ROE = TTM net profit / total equity.  Total equity defaults to None
    # unless the runner passes it in.
    roe = _safe_div(ttm.net_profit, total_equity)
    if roe is not None and roe < 0:
        flags.append("negative_roe")

    # Debt safety = (total_assets - total_liabilities) / total_assets.
    debt_safety: Optional[float] = None
    if (
        total_assets is not None
        and total_assets > 0
        and total_liabilities is not None
    ):
        debt_safety = max(0.0, (total_assets - total_liabilities) / total_assets)
    elif total_assets is not None and total_liabilities is None:
        flags.append("missing_total_liabilities")

    # Earnings momentum: simple YoY ratio of trailing net profit.  The
    # history is provided as an iterable of trailing net_profit values
    # (oldest -> newest).  The most recent value is ``ttm.net_profit``.
    earnings_momentum: Optional[float] = None
    if net_profit_history is not None:
        history = list(net_profit_history)
        if len(history) >= 4 and history[-1] is not None and history[-4] is not None:
            base = float(history[-4])
            if base > 0:
                earnings_momentum = float(history[-1]) / base - 1.0
            else:
                flags.append("non_positive_yoy_base")

    if margin_stability is None:
        flags.append("missing_margin")
    if roe is None:
        flags.append("missing_roe")
    if debt_safety is None:
        flags.append("missing_debt_safety")
    if earnings_momentum is None:
        flags.append("missing_earnings_momentum")

    return QualityComponents(
        margin_stability=margin_stability,
        roe=roe,
        debt_safety=debt_safety,
        earnings_momentum=earnings_momentum,
        quality_flags=tuple(flags),
    )


__all__ = [
    "QualityComponents",
    "score_quality",
]

