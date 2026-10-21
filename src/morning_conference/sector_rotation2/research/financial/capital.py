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
import math
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
        return (self.total_shares is not None and
                math.isfinite(float(self.total_shares)) and self.total_shares > 0)

    def market_cap(self, raw_close: float) -> Optional[float]:
        """Return ``raw_close * total_shares`` if both are available."""

        if (not self.is_available or raw_close is None or
                not math.isfinite(float(raw_close)) or raw_close <= 0):
            return None
        return float(raw_close) * float(self.total_shares)


def resolve_capital(
    rows: Iterable[CapitalRow],
    *,
    as_of_date: date,
) -> Optional[ResolvedCapital]:
    """Pick the latest PIT-visible capital row for ``as_of_date``."""

    eligible: list[CapitalRow] = [
        row for row in rows
        if (
            row.announcement_date is not None
            and row.announcement_date <= as_of_date
            and row.report_date <= as_of_date
        )
    ]
    if not eligible:
        return None
    # Share counts apply from the change date, even when announced earlier.
    # A correction to an older change does not supersede a later effective row.
    # For the same effective date, use validated QMT history before AKShare.
    eligible.sort(
        key=lambda row: (
            -row.report_date.toordinal(),
            0 if row.data_source.lower() == "qmt" else 1,
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
