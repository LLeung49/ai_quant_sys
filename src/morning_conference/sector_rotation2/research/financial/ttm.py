"""PIT-safe TTM from year-to-date financial statement flow fields.

Income and cash-flow statements report cumulative amounts since January 1.
For Q1/Q2/Q3, TTM is current YTD + prior fiscal year - prior-year same
quarter YTD. At Q4 the annual statement already represents twelve months.
Missing or unavailable anchors fail closed instead of double-counting.
"""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from datetime import date
from typing import Optional

from .normalize import normalize_row
from .pit import FinancialRawRow, resolve_latest_visible


TTM_QUARTERS = 4
_QUARTER_ENDS = {(3, 31), (6, 30), (9, 30), (12, 31)}


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
        return self.n_quarters >= TTM_QUARTERS


def _ttm_flow(
    latest: Optional[float],
    prior_annual: Optional[float],
    prior_same_quarter: Optional[float],
    *,
    annual: bool,
) -> Optional[float]:
    if latest is None:
        return None
    if annual:
        return float(latest)
    if prior_annual is None or prior_same_quarter is None:
        return None
    return float(latest) + float(prior_annual) - float(prior_same_quarter)


def build_ttm(
    raw_rows: Iterable[FinancialRawRow],
    *,
    as_of_date: date,
    allow_estimated_pit: bool = False,
) -> Optional[TTMProjection]:
    """Build TTM only from report versions visible on ``as_of_date``.

    A missing prior-year anchor makes the whole projection unavailable.
    Individual missing flow fields remain ``None`` with quality flags.
    """

    by_period: dict[date, list[FinancialRawRow]] = {}
    for row in raw_rows:
        by_period.setdefault(row.report_date, []).append(row)
    selected = [
        chosen for rows in by_period.values()
        if (chosen := resolve_latest_visible(
            rows, as_of_date=as_of_date,
            allow_estimated_pit=allow_estimated_pit,
        )) is not None
    ]
    normalized = {row.period_end_date: row for row in map(normalize_row, selected)}
    if not normalized:
        return None
    latest_period = max(normalized)
    if (latest_period.month, latest_period.day) not in _QUARTER_ENDS:
        return None

    latest = normalized[latest_period]
    annual = latest_period.month == 12
    components = [latest]
    if annual:
        prior_annual = prior_same = None
    else:
        prior_annual = normalized.get(date(latest_period.year - 1, 12, 31))
        prior_same = normalized.get(date(
            latest_period.year - 1, latest_period.month, latest_period.day,
        ))
        if prior_annual is None or prior_same is None:
            return None
        components.extend((prior_annual, prior_same))

    revenue = _ttm_flow(
        latest.revenue, prior_annual.revenue if prior_annual else None,
        prior_same.revenue if prior_same else None, annual=annual,
    )
    net_profit = _ttm_flow(
        latest.net_profit, prior_annual.net_profit if prior_annual else None,
        prior_same.net_profit if prior_same else None, annual=annual,
    )
    ocf = _ttm_flow(
        latest.operating_cash_flow,
        prior_annual.operating_cash_flow if prior_annual else None,
        prior_same.operating_cash_flow if prior_same else None, annual=annual,
    )
    flags: list[str] = []
    if any(row.is_restated for row in components):
        flags.append("contains_restated")
    if revenue is None:
        flags.append("partial_revenue")
    if net_profit is None:
        flags.append("partial_net_profit")
    return TTMProjection(
        stock_code=latest.stock_code,
        as_of_date=as_of_date,
        period_end_date=latest_period,
        revenue=revenue,
        net_profit=net_profit,
        operating_cash_flow=ocf,
        n_quarters=TTM_QUARTERS,
        quality_flags=tuple(flags),
    )


__all__ = ["TTMProjection", "TTM_QUARTERS", "build_ttm"]
