from datetime import date, timedelta
import math

import pandas as pd
import pytest

from morning_conference.sector_rotation2.research.etf_core.return_data import (
    is_domestic_equity_etf,
    load_return_mapping_input,
)


AS_OF_DATE = date(2026, 8, 14)


def _trade_dates():
    return [AS_OF_DATE - timedelta(days=60 - offset) for offset in range(61)]


def _price_rows(code, name, prices):
    return [
        {
            "stock_code": code,
            "stock_name": name,
            "trade_date": trade_date,
            "close_price": close_price,
        }
        for trade_date, close_price in zip(_trade_dates(), prices, strict=True)
    ]


def _fake_local_query(calls):
    def query(sql, params):
        calls.append((sql, params))
        if "SELECT DISTINCT trade_date" in sql:
            return [
                {"trade_date": AS_OF_DATE + timedelta(days=1)},
                *({"trade_date": item} for item in reversed(_trade_dates())),
            ]
        if "FROM trade_sector_daily" in sql:
            return [
                {
                    "sector_name": "电子",
                    "trade_date": item,
                    "close_idx": 1000.0 + index,
                }
                for index, item in enumerate(_trade_dates())
            ]
        if "FROM trade_stock_daily" in sql:
            return [
                *_price_rows("510300.SH", "沪深300ETF", [3.0 + index / 100 for index in range(61)]),
                *_price_rows("513100.SH", None, [4.0 + index / 100 for index in range(61)]),
                *_price_rows("511010.SH", "国债ETF", [100.0 + index for index in range(61)]),
                *_price_rows("159999.SZ", "黄金ETF", [100.0 + index for index in range(61)]),
                *_price_rows("159998.SZ", "科技ETF", [math.nan] + [0.0] + [10.0 + index for index in range(49)] + [math.inf] + [math.nan] * 9),
                *_price_rows("600000.SH", "浦发银行", [10.0 + index for index in range(61)]),
            ]
        raise AssertionError(f"unexpected SQL: {sql}")

    return query


def test_load_return_mapping_input_reads_only_local_prices_for_the_requested_61_dates():
    calls = []

    result = load_return_mapping_input(AS_OF_DATE, sector_level=2, query=_fake_local_query(calls))

    assert result.as_of_date == AS_OF_DATE
    assert result.price_source == "local_trade_daily"
    assert result.universe_codes == ("510300.SH",)
    assert list(result.sector_closes) == ["电子"]
    assert list(result.sector_closes["电子"].index) == _trade_dates()
    assert result.sector_closes["电子"].iloc[-1] == 1060.0
    assert list(result.etf_closes["510300.SH"].index) == _trade_dates()
    assert result.etf_closes["510300.SH"].iloc[0] == 3.0
    allowed_tables = ("trade_sector_daily", "trade_stock_daily", "trade_stock_status")
    assert all(any(table in sql for table in allowed_tables) for sql, _ in calls)
    assert any(params == (2, AS_OF_DATE, 61) for _, params in calls)
    assert all(
        table not in sql.lower()
        for sql, _ in calls
        for table in ("akshare", "xtquant", "miniqmt", "holdings")
    )


@pytest.mark.parametrize(
    ("code", "name"),
    [
        ("511010.SH", "国债ETF"),
        ("159001.SZ", "货币ETF"),
        ("159999.SZ", "黄金ETF"),
        ("510999.SH", "原油ETF"),
        ("513100.SH", "纳指ETF"),
        ("513500.SH", "标普ETF"),
        ("513520.SH", "日经ETF"),
        ("513600.SH", "恒生ETF"),
        ("513700.SH", "港股ETF"),
        ("513800.SH", "跨境ETF"),
        ("513900.SH", "Commodity ETF"),
        ("510001.SH", "Money Market ETF"),
        ("510002.SH", "Cross-border Equity ETF"),
    ],
)
def test_is_domestic_equity_etf_excludes_non_domestic_products(code, name):
    assert not is_domestic_equity_etf(code, name)


def test_is_domestic_equity_etf_accepts_recognized_domestic_equity_etf():
    assert is_domestic_equity_etf("510300.SH", "沪深300ETF")
    assert not is_domestic_equity_etf("600000.SH", "浦发银行")


@pytest.mark.parametrize("missing_name", [None, "", "   "])
def test_is_domestic_equity_etf_fails_closed_without_product_name(missing_name):
    assert not is_domestic_equity_etf("513100.SH", missing_name)
