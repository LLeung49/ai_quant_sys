"""Capital structure resolution for Repair Alpha.

Picks the latest PIT-visible capital row at ``as_of_date`` and exposes
the resolved ``total_shares`` and ``circulating_shares``.  Market cap
is computed as ``raw close * total_shares`` and never ``qfq close *
current shares`` (which would silently leak future share splits into
historical PIT research).
"""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from datetime import date
from typing import Optional

from .providers.base import CapitalRow


@dataclass(frozen=True)
class ResolvedCapital:
    """Capital structure visible at ``as_of_date``."""

    stock_code: str
    as_of_date: date
    report_date: date
    announcement_date: date
    total_shares: Optional[float]
    circulating_shares: Optional[float]
    source_hash: str
    data_source: str

    @property
    def is_available(self) -> bool:
        """Whether PIT shares are sufficient for market-cap valuation."""
        return self.total_shares is not None and self.total_shares > 0

    def market_cap(self, raw_close: float) -> Optional[float]:
        """Return ``raw_close * total_shares`` if both are available."""

        if self.total_shares is None or raw_close is None:
            return None
        return float(raw_close) * float(self.total_shares)


def _row_sort_key(row: CapitalRow) -> tuple:
    return (
        row.announcement_date,
        1 if False else 0,  # placeholder for future restated handling
        row.source_hash,
    )


def resolve_capital(
    rows: Iterable[CapitalRow],
    *,
    as_of_date: date,
) -> Optional[ResolvedCapital]:
    """Pick the latest PIT-visible capital row for ``as_of_date``."""

    eligible: list[CapitalRow] = [
        row for row in rows
        if row.announcement_date is not None and row.announcement_date <= as_of_date
    ]
    if not eligible:
        return None
    # Tie-break: latest announcement, then earliest source_hash.
    eligible.sort(
        key=lambda row: (
            -row.announcement_date.toordinal(),
            row.source_hash,
        )
    )
    chosen = eligible[0]
    return ResolvedCapital(
        stock_code=chosen.stock_code,
        as_of_date=as_of_date,
        report_date=chosen.report_date,
        announcement_date=chosen.announcement_date,
        total_shares=chosen.total_shares,
        circulating_shares=chosen.circulating_shares,
        source_hash=chosen.source_hash,
        data_source=chosen.data_source,
    )


__all__ = ["ResolvedCapital", "resolve_capital"]
