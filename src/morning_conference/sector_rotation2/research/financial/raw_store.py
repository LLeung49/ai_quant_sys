"""Persistence boundary for financial raw PIT and valuation tables."""

from __future__ import annotations

from collections.abc import Callable
from datetime import date, datetime
from typing import Any

from data_ingestion.db_config import get_connection

from .schema import apply_schema_ddl


def _identity_predicate(stock_code: str, as_of_date: date) -> tuple:
    return (stock_code, as_of_date)


class FinancialRawStore:
    """MySQL-backed append-only writer for the Repair Alpha financial layer.

    The class deliberately performs pure SQL inserts without ``ON DUPLICATE
    KEY UPDATE`` so the raw PIT history remains immutable.  ``ensure_schema``
    applies every DDL block in :mod:`schema`.
    """

    def __init__(self, connection_factory: Callable[[], Any] = get_connection) -> None:
        self._connection_factory = connection_factory

    def ensure_schema(self) -> None:
        connection = self._connection_factory()
        try:
            apply_schema_ddl(connection)
        finally:
            connection.close()

    def insert_raw(self, row: dict[str, Any]) -> int:
        return self._execute(
            """INSERT IGNORE INTO trade_stock_financial_raw_pit
               (stock_code, source_table, report_date, announcement_date, period_type,
                revenue, net_profit, total_assets, total_equity, operating_cash_flow,
                pit_status, source_updated_at, source_hash, is_restated, source_verified, data_source)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
            (
                row["stock_code"], row["source_table"], row["report_date"],
                row.get("announcement_date"), row["period_type"],
                row.get("revenue"), row.get("net_profit"),
                row.get("total_assets"), row.get("total_equity"),
                row.get("operating_cash_flow"),
                row["pit_status"], row["source_updated_at"], row["source_hash"],
                1 if row.get("is_restated") else 0,
                1 if row.get("source_verified") else 0,
                row.get("data_source", "akshare"),
            ),
        )

    def insert_capital(self, row: dict[str, Any]) -> int:
        return self._execute(
            """INSERT IGNORE INTO trade_stock_capital_pit
               (stock_code, report_date, announcement_date, total_shares,
                circulating_shares, pit_status, source_hash, data_source)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
            (
                row["stock_code"], row["report_date"], row["announcement_date"],
                row.get("total_shares"), row.get("circulating_shares"),
                row["pit_status"], row["source_hash"],
                row.get("data_source", "akshare"),
            ),
        )

    def insert_valuation(self, row: dict[str, Any]) -> int:
        return self._execute(
            """INSERT INTO trade_stock_valuation_daily
               (as_of_date, stock_code, sector_name, pe, pb, ps, p_ocf, market_cap,
                ttm_revenue, ttm_net_profit, pit_status, quality_flags,
                model_version, config_hash, run_id)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
            (
                row["as_of_date"], row["stock_code"], row.get("sector_name"),
                row.get("pe"), row.get("pb"), row.get("ps"), row.get("p_ocf"),
                row.get("market_cap"),
                row.get("ttm_revenue"), row.get("ttm_net_profit"),
                row["pit_status"], row.get("quality_flags"),
                row["model_version"], row["config_hash"], row["run_id"],
            ),
        )

    def _execute(self, sql: str, params: tuple) -> int:
        connection = self._connection_factory()
        cursor = connection.cursor()
        try:
            cursor.execute(sql, params)
            connection.commit()
            return cursor.rowcount
        except Exception:
            connection.rollback()
            raise
        finally:
            cursor.close()
            connection.close()


def _identity_predicate_unused() -> tuple:  # pragma: no cover - helper for forward use
    return _identity_predicate


__all__ = ["FinancialRawStore"]
