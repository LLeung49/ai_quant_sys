from __future__ import annotations

import pandas as pd

from morning_conference.sector_rotation2.data_loader import (
    build_market_benchmark,
    load_sector_stock_amounts,
    load_sector_panel,
    load_market_aggregates,
    validate_sector_frame,
)


def valid_frame() -> pd.DataFrame:
    return pd.DataFrame(
        {"close": [100.0, 110.0], "amount": [10.0, 20.0]},
        index=pd.to_datetime(["2026-01-01", "2026-01-02"]),
    )


def test_validate_sector_frame_rejects_duplicate_dates_and_negative_amount():
    frame = pd.DataFrame(
        {"close": [100.0, 101.0], "amount": [10.0, -1.0]},
        index=pd.to_datetime(["2026-01-02", "2026-01-02"]),
    )

    result = validate_sector_frame(frame)

    assert result.valid is False
    assert {"duplicate_trade_date", "negative_amount"} <= set(result.reasons)


def test_build_market_benchmark_uses_only_eligible_sector_frames():
    invalid = valid_frame().assign(amount=[10.0, -1.0])

    benchmark = build_market_benchmark({"A": valid_frame(), "B": invalid})

    assert benchmark["eligible_sector_count"].iloc[-1] == 1
    assert benchmark["amount"].tolist() == [10.0, 20.0]


def test_load_sector_panel_queries_read_only_source_and_groups_by_sector(monkeypatch):
    rows = [
        {"sector_name": "电子", "trade_date": "2026-01-02", "close": 100.0, "amount": 10.0,
         "stock_count": 10, "kline_stock_count": 10, "rise_count": 6, "fall_count": 3, "flat_count": 1,
         "limit_up": 1, "limit_down": 0},
    ]
    monkeypatch.setattr("morning_conference.sector_rotation2.data_loader.execute_query", lambda sql, params: rows)

    panel = load_sector_panel(level=2, start_date="2026-01-02", end_date="2026-01-02", min_history_days=1)

    assert list(panel) == ["电子"]
    assert panel["电子"].loc[pd.Timestamp("2026-01-02"), "close"] == 100.0


def test_load_sector_stock_amounts_uses_current_sector_mapping(monkeypatch):
    rows = [{"stock_code": "000001.SZ", "trade_date": "2026-01-02", "amount": 100.0, "close": 10.0}]
    monkeypatch.setattr("morning_conference.sector_rotation2.data_loader.execute_query", lambda sql, params: rows)

    result = load_sector_stock_amounts("电子", 2, ["2026-01-02"])

    assert result.loc[0, "membership_asof_mode"] == "current_mapping"
    assert result.loc[0, "stock_code"] == "000001.SZ"


def test_load_market_aggregates_sums_limits_and_uses_median_breadth():
    panel = {
        "A": valid_frame().assign(rise_count=[6, 8], fall_count=[2, 1], flat_count=[2, 1], limit_up=[1, 2], limit_down=[0, 0]),
        "B": valid_frame().assign(rise_count=[4, 2], fall_count=[4, 6], flat_count=[2, 2], limit_up=[0, 0], limit_down=[1, 2]),
    }
    aggregates = load_market_aggregates(panel)
    assert aggregates.loc[pd.Timestamp("2026-01-02"), "limit_up"] == 2
    assert aggregates.loc[pd.Timestamp("2026-01-02"), "limit_down"] == 2


def test_historical_loaders_fetch_sector_and_stock_history_once_with_warmup(monkeypatch):
    """历史回填必须批量读取，并把预热交易日带入行业和个股面板。"""
    from morning_conference.sector_rotation2 import data_loader

    calls = []
    sector_rows = [{"sector_name": "电子", "trade_date": "2026-01-01", "close": 100.0, "amount": 10.0,
                    "stock_count": 1, "kline_stock_count": 1, "rise_count": 1, "fall_count": 0, "flat_count": 0,
                    "limit_up": 0, "limit_down": 0}]
    stock_rows = [{"sector_name": "电子", "stock_code": "000001.SZ", "trade_date": "2026-01-01", "amount": 10.0, "close": 10.0}]
    def query(sql, params):
        calls.append((sql, params))
        return stock_rows if "trade_stock_daily_qfq" in sql else sector_rows
    monkeypatch.setattr(data_loader, "execute_query", query)

    sector_panel = data_loader.load_historical_sector_panel(2, "2026-01-04", "2026-01-31", warmup_days=90)
    stock_panel = data_loader.load_historical_sector_stock_panel(2, "2026-01-04", "2026-01-31", warmup_days=20)

    assert list(sector_panel) == ["电子"]
    assert stock_panel.loc[0, "membership_asof_mode"] == "current_mapping"
    assert len(calls) == 2
    assert 90 in calls[0][1]
    assert 20 in calls[1][1]
