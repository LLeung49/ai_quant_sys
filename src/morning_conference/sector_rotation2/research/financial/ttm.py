"""TTM (trailing-twelve-month) derivation for Repair Alpha.

The TTM layer walks the trailing 4 quarterly rows for each stock and
emits a per-stock TTM projection.  When fewer than 4 quarters are
available the function returns ``None`` rather than extrapolating; the
TTM is fail-closed because valuation ratios on partial windows are
noisier than the missing-data signal they would replace.
"""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from datetime import date
from typing import Optional

from .normalize import NormalizedFinancialRow
from .pit import FinancialRawRow, resolve_latest_visible
from .normalize import normalize_row


TTM_QUARTERS = 4


@dataclass(frozen=True)
class TTMProjection:
    """One trailing-twelve-month projection."""

    stock_code: str
    as_of_date: date
    period_end_date: date
    revenue: Optional[float]
    net_profit: Optional[float]
    operating_cash_flow: Optional[float]
    n_quarters: int
    quality_flags: tuple

    @property
    def is_complete(self) -> bool:
        """Return True when the TTM is built from the full 4 quarters."""

        return self.n_quarters >= TTM_QUARTERS


def _select_trailing(
    rows: Iterable[NormalizedFinancialRow],
) -> list[NormalizedFinancialRow]:
    """Pick the ``TTM_QUARTERS`` most recent rows, sorted by date ascending."""

    candidates = sorted(rows, key=lambda r: r.period_end_date)
    return candidates[-TTM_QUARTERS:] if len(candidates) > TTM_QUARTERS else candidates


def _sum_optional(values: Iterable[Optional[float]]) -> Optional[float]:
    """Sum only when every value is finite and non-null; otherwise ``None``."""

    total = 0.0
    count = 0
    for value in values:
        if value is None:
            return None
        total += float(value)
        count += 1
    if count == 0:
        return None
    return total


def build_ttm(
    raw_rows: Iterable[FinancialRawRow],
    *,
    as_of_date: date,
) -> Optional[TTMProjection]:
    """Build a TTM projection for a single stock at ``as_of_date``.

    Returns ``None`` when fewer than ``TTM_QUARTERS`` quarterly rows are
    available, or when any of the underlying fields is missing.
    """

    raw_list = list(raw_rows)
    # Resolve one point-in-time version per report period before deriving TTM.
    by_period: dict[date, list[FinancialRawRow]] = {}
    for row in raw_list:
        by_period.setdefault(row.report_date, []).append(row)
    resolved = [chosen for rows in by_period.values()
                if (chosen := resolve_latest_visible(rows, as_of_date=as_of_date)) is not None]
    normalized = [normalize_row(row) for row in resolved]
    if not normalized:
        return None
    # Filter rows that are PIT-visible at as_of_date.
    if not normalized:
        return None
    trailing = _select_trailing(normalized)
    n_quarters = len(trailing)
    if n_quarters < TTM_QUARTERS:
        return None
    revenue = _sum_optional(r.revenue for r in trailing)
    net_profit = _sum_optional(r.net_profit for r in trailing)
    ocf = _sum_optional(r.operating_cash_flow for r in trailing)
    flags: list = []
    if any(r.is_restated for r in trailing):
        flags.append("contains_restated")
    if any("missing_revenue" in r.quality_flags for r in trailing):
        flags.append("partial_revenue")
    if any("missing_net_profit" in r.quality_flags for r in trailing):
        flags.append("partial_net_profit")
    return TTMProjection(
        stock_code=trailing[0].stock_code,
        as_of_date=as_of_date,
        period_end_date=trailing[-1].period_end_date,
        revenue=revenue,
        net_profit=net_profit,
        operating_cash_flow=ocf,
        n_quarters=n_quarters,
        quality_flags=tuple(flags),
    )


__all__ = [
    "TTMProjection",
    "TTM_QUARTERS",
    "build_ttm",
]
