"""Secondary financial provider for cross-validation.

The secondary provider is consulted only when the primary provider
returns a row with a quality issue.  It is intentionally narrow: a
secondary provider may override a ``PIT_ESTIMATED`` row with a
``PIT_VERIFIED`` row sourced from a trusted aggregator, but it never
downgrades a verified primary row.
"""

from __future__ import annotations

from collections.abc import Callable, Iterable
from datetime import date
from typing import Any, Mapping

from .base import (
    CapitalRow,
    FinancialProvider,
    FinancialRawRow,
    coerce_numeric,
)
from .miniqmt import _as_date, _bool, FetchCallable


class SecondaryProvider(FinancialProvider):
    """A read-only secondary adapter used to disambiguate primary rows."""

    def __init__(
        self,
        *,
        fetch: FetchCallable | None = None,
        provider_name: str = "secondary",
        primary_provider_name: str = "miniqmt",
    ) -> None:
        self._fetch = fetch
        self._name = provider_name
        self._primary = primary_provider_name

    def provider_name(self) -> str:
        return self._name

    def iter_raw_rows(
        self,
        *,
        as_of_date: date,
        stock_codes: Iterable[str],
    ) -> Iterable[FinancialRawRow]:
        codes = sorted({code for code in stock_codes if code})
        if not codes:
            return []
        placeholders = ", ".join(["%s"] * len(codes))
        sql = (
            "SELECT stock_code, source_table, report_date, period_type, announcement_date, "
            "first_seen_at, source_hash, is_restated, source_verified, data_source, "
            "revenue, net_profit, total_assets, total_equity, operating_cash_flow "
            f"FROM trade_stock_financial_secondary_pit "
            f"WHERE report_date <= %s AND stock_code IN ({placeholders}) "
            "ORDER BY stock_code, report_date DESC"
        )
        for row in self._execute(sql, (as_of_date, *codes)):
            yield FinancialRawRow(
                stock_code=str(row.get("stock_code") or "").strip(),
                source_table=str(row.get("source_table") or self._name),
                report_date=_as_date(row.get("report_date")) or as_of_date,
                period_type=str(row.get("period_type") or "ttm"),
                announcement_date=_as_date(row.get("announcement_date")),
                first_seen_at=_as_date(row.get("first_seen_at")) or as_of_date,
                source_hash=str(row.get("source_hash") or "").strip(),
                is_restated=_bool(row.get("is_restated")),
                source_verified=_bool(row.get("source_verified")),
                data_source=str(row.get("data_source") or self._name),
                revenue=coerce_numeric(row.get("revenue")),
                net_profit=coerce_numeric(row.get("net_profit")),
                total_assets=coerce_numeric(row.get("total_assets")),
                total_equity=coerce_numeric(row.get("total_equity")),
                operating_cash_flow=coerce_numeric(row.get("operating_cash_flow")),
            )

    def iter_capital_rows(
        self,
        *,
        as_of_date: date,
        stock_codes: Iterable[str],
    ) -> Iterable[CapitalRow]:
        codes = sorted({code for code in stock_codes if code})
        if not codes:
            return []
        placeholders = ", ".join(["%s"] * len(codes))
        sql = (
            "SELECT stock_code, report_date, announcement_date, total_shares, "
            f"circulating_shares, source_hash, data_source FROM trade_stock_capital_secondary_pit "
            f"WHERE report_date <= %s AND stock_code IN ({placeholders}) "
            "ORDER BY stock_code, report_date DESC"
        )
        for row in self._execute(sql, (as_of_date, *codes)):
            yield CapitalRow(
                stock_code=str(row.get("stock_code") or "").strip(),
                report_date=_as_date(row.get("report_date")) or as_of_date,
                announcement_date=_as_date(row.get("announcement_date")) or as_of_date,
                total_shares=coerce_numeric(row.get("total_shares")),
                circulating_shares=coerce_numeric(row.get("circulating_shares")),
                source_hash=str(row.get("source_hash") or "").strip(),
                data_source=str(row.get("data_source") or self._name),
            )

    def _execute(self, sql: str, params: tuple) -> list[Mapping[str, Any]]:
        if self._fetch is None:
            return []
        return list(self._fetch(sql, params))


__all__ = ["SecondaryProvider"]

