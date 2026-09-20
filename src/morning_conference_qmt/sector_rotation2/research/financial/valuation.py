"""PIT-safe valuation ratios for Repair Alpha.

Rules:
- ``PE`` and ``P_OCF`` are ``None`` when the underlying TTM profit / OCF is
  zero or negative (negative is not "cheap", it is uninformative).
- ``PB`` is ``None`` when total equity is zero or negative.
- ``PS`` is ``None`` when TTM revenue is zero or negative.
- ``market_cap`` is computed as ``raw_close * total_shares`` (never
  ``qfq_close * current_shares``).

Financial-sector profiles disable generic balance-sheet ratios (PB) but
keep the per-share metrics.  Sector tags follow the SW2 sector names
already present on the universe.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from datetime import date
from typing import Optional

from .capital import ResolvedCapital
from .ttm import TTMProjection


# Sectors that should skip generic balance-sheet ratios (PB).
_FINANCIAL_SECTORS = frozenset({
    "\u91d1\u878d",  # finance
    "\u94f6\u884c",  # bank
    "\u4fdd\u9669",  # insurance
    "\u8bc1\u5238",  # securities
    "\u591a\u5143\u91d1\u878d",  # multi-finance
    "\u4fe1\u6258",  # trust
})


@dataclass(frozen=True)
class ValuationSnapshot:
    """One PIT-safe daily valuation snapshot."""

    as_of_date: date
    stock_code: str
    sector_name: Optional[str]
    pe: Optional[float]
    pb: Optional[float]
    ps: Optional[float]
    p_ocf: Optional[float]
    market_cap: Optional[float]
    ttm_revenue: Optional[float]
    ttm_net_profit: Optional[float]
    pit_status: str
    quality_flags: tuple
    raw_close: float


def _safe_div(numerator: Optional[float], denominator: Optional[float]) -> Optional[float]:
    if numerator is None or denominator is None:
        return None
    if denominator <= 0:
        return None
    return float(numerator) / float(denominator)


def _is_financial_sector(sector_name: Optional[str]) -> bool:
    if not sector_name:
        return False
    return sector_name in _FINANCIAL_SECTORS


def build_valuation(
    *,
    ttm: TTMProjection,
    capital: ResolvedCapital,
    raw_close: float,
    sector_name: Optional[str],
    total_equity: Optional[float] = None,
) -> ValuationSnapshot:
    """Combine TTM + capital + raw close into one valuation snapshot.

    ``raw_close`` must be the un-front-adjusted close at ``as_of_date``;
    the valuation layer never reads a qfq close so share splits are not
    silently applied retroactively.  ``total_equity`` is sourced from the
    latest TTM row (or ``None`` when the upstream is missing).
    """

    flags: list = []
    market_cap = capital.market_cap(raw_close)
    pe = _safe_div(market_cap, ttm.net_profit)
    if pe is not None and pe <= 0:
        pe = None
    ps = _safe_div(market_cap, ttm.revenue)
    if ps is not None and ps <= 0:
        ps = None
    p_ocf = _safe_div(market_cap, ttm.operating_cash_flow)
    if p_ocf is not None and p_ocf <= 0:
        p_ocf = None
    pb: Optional[float] = None
    if _is_financial_sector(sector_name):
        flags.append("financial_sector_pb_disabled")
    else:
        pb = _safe_div(market_cap, total_equity)
        if pb is not None and pb <= 0:
            pb = None
    if ttm.net_profit is None:
        flags.append("pe_uninformative")
    if ttm.revenue is None:
        flags.append("ps_uninformative")
    if ttm.operating_cash_flow is None:
        flags.append("p_ocf_uninformative")
    if market_cap is None:
        flags.append("missing_market_cap")
    if total_equity is None and not _is_financial_sector(sector_name):
        flags.append("pb_uninformative")
    for flag in ttm.quality_flags:
        flags.append(f"ttm_{flag}")
    return ValuationSnapshot(
        as_of_date=ttm.as_of_date,
        stock_code=ttm.stock_code,
        sector_name=sector_name,
        pe=pe,
        pb=pb,
        ps=ps,
        p_ocf=p_ocf,
        market_cap=market_cap,
        ttm_revenue=ttm.revenue,
        ttm_net_profit=ttm.net_profit,
        pit_status="pit_exact",
        quality_flags=tuple(flags),
        raw_close=raw_close,
    )


def to_mapping(snapshot: ValuationSnapshot) -> dict:
    """Return a plain-dict representation for JSON serialization."""

    return {
        "as_of_date": snapshot.as_of_date.isoformat(),
        "stock_code": snapshot.stock_code,
        "sector_name": snapshot.sector_name,
        "pe": snapshot.pe,
        "pb": snapshot.pb,
        "ps": snapshot.ps,
        "p_ocf": snapshot.p_ocf,
        "market_cap": snapshot.market_cap,
        "ttm_revenue": snapshot.ttm_revenue,
        "ttm_net_profit": snapshot.ttm_net_profit,
        "pit_status": snapshot.pit_status,
        "quality_flags": list(snapshot.quality_flags),
        "raw_close": snapshot.raw_close,
    }


__all__ = [
    "ValuationSnapshot",
    "build_valuation",
    "to_mapping",
    "_FINANCIAL_SECTORS",
]

