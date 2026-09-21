"""Wide-format normalizer for financial statement rows.

The provider layer returns raw rows; this module assembles them into
``NormalizedFinancialRow`` projections keyed on
``(stock_code, period_end_date)`` so the TTM and valuation layers can
reason about a single canonical structure.
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field
from datetime import date
from typing import Any, Optional

from .pit import FinancialRawRow


@dataclass(frozen=True)
class NormalizedFinancialRow:
    """One normalized financial statement projection."""

    stock_code: str
    period_end_date: date
    period_type: str
    announcement_date: Optional[date]
    pit_status: str
    source_hash: str
    data_source: str
    is_restated: bool = False
    revenue: Optional[float] = None
    net_profit: Optional[float] = None
    total_assets: Optional[float] = None
    total_equity: Optional[float] = None
    operating_cash_flow: Optional[float] = None
    quality_flags: tuple = field(default_factory=tuple)

    @property
    def has_revenue(self) -> bool:
        return self.revenue is not None

    @property
    def has_net_profit(self) -> bool:
        return self.net_profit is not None


def normalize_row(row: FinancialRawRow) -> NormalizedFinancialRow:
    """Build a :class:`NormalizedFinancialRow` from a raw provider row.

    Quality flags are surfaced so the valuation/quality layers can act on
    them without having to re-inspect the raw row.
    """

    flags: list = []
    if row.revenue is None:
        flags.append("missing_revenue")
    if row.net_profit is None:
        flags.append("missing_net_profit")
    if row.total_assets is None:
        flags.append("missing_total_assets")
    if row.total_equity is None:
        flags.append("missing_total_equity")
    if row.operating_cash_flow is None:
        flags.append("missing_operating_cash_flow")
    if row.is_restated:
        flags.append("restated")
    if row.pit_status == "pit_invalid":
        flags.append("invalid_pit")
    return NormalizedFinancialRow(
        stock_code=row.stock_code,
        period_end_date=row.report_date,
        period_type=row.period_type,
        announcement_date=row.announcement_date,
        pit_status=row.pit_status or "pit_unclassified",
        source_hash=row.source_hash,
        data_source=row.data_source,
        is_restated=row.is_restated,
        revenue=row.revenue,
        net_profit=row.net_profit,
        total_assets=row.total_assets,
        total_equity=row.total_equity,
        operating_cash_flow=row.operating_cash_flow,
        quality_flags=tuple(flags),
    )


def normalize_rows(rows: Iterable[FinancialRawRow]) -> list[NormalizedFinancialRow]:
    """Normalize a sequence of raw rows."""

    return [normalize_row(row) for row in rows]


def to_mapping(row: NormalizedFinancialRow) -> dict[str, Any]:
    """Return a plain-dict representation of a normalized row."""

    return {
        "stock_code": row.stock_code,
        "period_end_date": row.period_end_date.isoformat(),
        "period_type": row.period_type,
        "announcement_date": row.announcement_date.isoformat() if row.announcement_date else None,
        "pit_status": row.pit_status,
        "source_hash": row.source_hash,
        "data_source": row.data_source,
        "is_restated": row.is_restated,
        "revenue": row.revenue,
        "net_profit": row.net_profit,
        "total_assets": row.total_assets,
        "total_equity": row.total_equity,
        "operating_cash_flow": row.operating_cash_flow,
        "quality_flags": list(row.quality_flags),
    }


__all__ = [
    "NormalizedFinancialRow",
    "normalize_row",
    "normalize_rows",
    "to_mapping",
]

