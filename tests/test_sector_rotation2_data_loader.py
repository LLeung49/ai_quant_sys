from __future__ import annotations

import pandas as pd

from morning_conference.sector_rotation2.data_loader import (
    build_market_benchmark,
    load_sector_panel,
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
