"""Tests for the financial provider stack."""

from datetime import date
from typing import Any, Mapping

import pytest

from morning_conference.sector_rotation2.research.financial.providers import (
    DatabaseFinancialProvider,
    SecondaryProvider,
)
from morning_conference.sector_rotation2.research.financial.providers.base import (
    FinancialRawRow,
    coerce_numeric,
)


def _raw_rows() -> list[Mapping[str, Any]]:
    return [
        {
            "stock_code": "600000",
            "source_table": "miniqmt",
            "report_date": date(2026, 6, 30),
            "period_type": "quarterly",
            "announcement_date": date(2026, 7, 25),
            "first_seen_at": date(2026, 7, 25),
            "source_hash": "hash_1",
            "is_restated": 0,
            "source_verified": 1,
            "data_source": "miniqmt",
            "revenue": 100.0,
            "net_profit": 10.0,
            "total_assets": 200.0,
            "total_equity": 80.0,
            "operating_cash_flow": 12.0,
        },
        {
            "stock_code": "600000",
            "source_table": "miniqmt",
            "report_date": date(2026, 3, 31),
            "period_type": "quarterly",
            "announcement_date": date(2026, 4, 25),
            "first_seen_at": date(2026, 4, 25),
            "source_hash": "hash_2",
            "is_restated": 0,
            "source_verified": 1,
            "data_source": "miniqmt",
            "revenue": 90.0,
            "net_profit": 9.0,
        },
    ]


def test_database_provider_yields_raw_rows() -> None:
    provider = DatabaseFinancialProvider(fetch=lambda sql, params: _raw_rows())
    rows = list(provider.iter_raw_rows(as_of_date=date(2026, 8, 1), stock_codes=["600000"]))
    assert len(rows) == 2
    assert rows[0].stock_code == "600000"
    assert rows[0].revenue == 100.0
    assert rows[0].announcement_date == date(2026, 7, 25)
    assert rows[1].report_date == date(2026, 3, 31)


def test_database_provider_returns_full_universe_on_empty_codes() -> None:
    """Empty stock_codes signals ``no filter`` rather than ``no results``.

    The runner uses this mode to fetch all PIT-visible rows for a
    date and group them by stock downstream.
    """

    provider = DatabaseFinancialProvider(fetch=lambda sql, params: _raw_rows())
    rows = list(provider.iter_raw_rows(as_of_date=date(2026, 8, 1), stock_codes=[]))
    assert len(rows) == 2


def test_database_provider_handles_missing_fetch() -> None:
    provider = DatabaseFinancialProvider()
    rows = list(provider.iter_raw_rows(as_of_date=date(2026, 8, 1), stock_codes=["600000"]))
    assert rows == []


def test_database_provider_returns_capital_rows() -> None:
    def fetch(sql, params):
        return [{
            "stock_code": "600000",
            "report_date": date(2026, 6, 30),
            "announcement_date": date(2026, 7, 25),
            "total_shares": 1000.0,
            "circulating_shares": 950.0,
            "source_hash": "cap_1",
            "data_source": "miniqmt",
        }]
    provider = DatabaseFinancialProvider(fetch=fetch)
    rows = list(provider.iter_capital_rows(as_of_date=date(2026, 8, 1), stock_codes=["600000"]))
    assert len(rows) == 1
    assert rows[0].total_shares == 1000.0


def test_database_provider_does_not_invent_missing_capital_dates() -> None:
    provider = DatabaseFinancialProvider(fetch=lambda sql, params: [{
        "stock_code": "600000.SH",
        "report_date": date(2026, 6, 30),
        "announcement_date": None,
        "total_shares": 1000.0,
        "circulating_shares": 900.0,
    }])
    rows = list(provider.iter_capital_rows(
        as_of_date=date(2026, 8, 1), stock_codes=["600000.SH"]
    ))
    assert rows == []


def test_database_provider_exposes_metrics_only_after_their_own_date() -> None:
    raw = dict(_raw_rows()[0], eps=1.2, roe=10.5, gross_margin=31.0,
               metric_available_at=date(2026, 8, 3))
    provider = DatabaseFinancialProvider(fetch=lambda sql, params: [raw])
    before = list(provider.iter_raw_rows(
        as_of_date=date(2026, 8, 1), stock_codes=["600000"]
    ))[0]
    after = list(provider.iter_raw_rows(
        as_of_date=date(2026, 8, 4), stock_codes=["600000"]
    ))[0]
    assert before.eps is None
    assert before.roe is None
    assert after.eps == 1.2
    assert after.roe == 10.5
    assert after.gross_margin == 31.0
    assert "metric_available_at" in provider_query()


def provider_query() -> str:
    from morning_conference.sector_rotation2.research.financial.providers.database import DEFAULT_RAW_QUERY
    return DEFAULT_RAW_QUERY


def test_secondary_provider_uses_distinct_query() -> None:
    captured: list = []
    def fetch(sql, params):
        captured.append(sql)
        return []
    provider = SecondaryProvider(fetch=fetch)
    list(provider.iter_raw_rows(as_of_date=date(2026, 8, 1), stock_codes=["600000"]))
    assert "trade_stock_financial_secondary_pit" in captured[0]
    assert "miniqmt" not in captured[0].lower().split("from")[1].split()[0]


def test_coerce_numeric_returns_none_on_invalid() -> None:
    assert coerce_numeric(None) is None
    assert coerce_numeric("not a number") is None
    assert coerce_numeric("3.14") == pytest.approx(3.14)
    assert coerce_numeric(True) == 1.0
    assert coerce_numeric(42) == 42.0


def test_financial_raw_row_is_frozen() -> None:
    row = FinancialRawRow(
        stock_code="600000",
        source_table="miniqmt",
        report_date=date(2026, 6, 30),
        period_type="quarterly",
        announcement_date=date(2026, 7, 25),
        first_seen_at=date(2026, 7, 25),
        source_hash="hash",
        is_restated=False,
        source_verified=True,
        data_source="miniqmt",
    )
    with pytest.raises(Exception):
        row.stock_code = "601318"
