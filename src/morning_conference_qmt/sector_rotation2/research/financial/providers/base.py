"""Abstract base class for financial statement providers."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import date
from typing import Iterable, Mapping, Optional


@dataclass(frozen=True)
class ProviderQualityIssue:
    """Machine-readable reason why a provider input cannot be used."""

    code: str
    detail: str


@dataclass(frozen=True)
class FinancialRawRow:
    """One financial statement row, raw and un-normalized.

    The provider is responsible for populating ``source_hash`` and
    ``source_updated_at``; the PIT resolver decides whether the row is
    usable at any given research date.  ``pit_status`` is populated by
    the PIT resolver when the row is loaded from storage; providers may
    leave it as ``None``.
    """

    stock_code: str
    source_table: str
    report_date: date
    period_type: str
    announcement_date: Optional[date]
    first_seen_at: date
    source_hash: str
    is_restated: bool
    source_verified: bool
    data_source: str
    pit_status: Optional[str] = None
    revenue: Optional[float] = None
    net_profit: Optional[float] = None
    total_assets: Optional[float] = None
    total_equity: Optional[float] = None
    operating_cash_flow: Optional[float] = None
    quality_issue: Optional[ProviderQualityIssue] = None


@dataclass(frozen=True)
class CapitalRow:
    """One capital structure row (PIT-aware share count)."""

    stock_code: str
    report_date: date
    announcement_date: date
    total_shares: Optional[float]
    circulating_shares: Optional[float]
    source_hash: str
    data_source: str


class FinancialProvider(ABC):
    """Provider contract for the financial statement / capital layer.

    The base class deliberately stays narrow: providers only return raw
    rows.  PIT resolution, TTM derivation, valuation, and quality scoring
    live in :mod:`normalize` / :mod:`ttm` / :mod:`valuation`.
    """

    @abstractmethod
    def iter_raw_rows(
        self,
        *,
        as_of_date: date,
        stock_codes: Iterable[str],
    ) -> Iterable[FinancialRawRow]:
        """Iterate raw statement rows visible at ``as_of_date``."""

    @abstractmethod
    def iter_capital_rows(
        self,
        *,
        as_of_date: date,
        stock_codes: Iterable[str],
    ) -> Iterable[CapitalRow]:
        """Iterate capital structure rows visible at ``as_of_date``."""

    @abstractmethod
    def provider_name(self) -> str:
        """Return the provider identifier used in ``data_source``."""


def coerce_numeric(value: object) -> Optional[float]:
    """Best-effort numeric coercion that returns ``None`` on failure."""

    if value is None:
        return None
    if isinstance(value, bool):
        return float(value)
    if isinstance(value, (int, float)):
        return float(value)
    try:
        return float(str(value).strip())
    except (TypeError, ValueError):
        return None


__all__ = [
    "FinancialProvider",
    "FinancialRawRow",
    "CapitalRow",
    "ProviderQualityIssue",
    "coerce_numeric",
]

