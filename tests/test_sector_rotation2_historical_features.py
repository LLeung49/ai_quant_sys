from __future__ import annotations

import pandas as pd


def test_historical_feature_panels_return_one_daily_panel_per_target_date(monkeypatch):
    """批处理特征必须为每个目标交易日返回与单日入口同形状的面板。"""
    from morning_conference.sector_rotation2 import sector_features

    dates = pd.bdate_range("2026-01-01", periods=92)
    sector = pd.DataFrame(
        {
            "close": range(100, 192), "amount": [100.0] * 92,
            "stock_count": 10, "kline_stock_count": 10,
            "rise_count": 6, "fall_count": 3, "flat_count": 1,
        },
        index=dates,
    )
    monkeypatch.setattr(sector_features, "load_historical_sector_panel", lambda *_args, **_kwargs: {"electronics": sector})
    monkeypatch.setattr(sector_features, "load_historical_sector_stock_panel", lambda *_args, **_kwargs: pd.DataFrame())

    panels = sector_features.build_historical_feature_panels(2, dates[90].strftime("%Y-%m-%d"), dates[91].strftime("%Y-%m-%d"))

    first, second = dates[90].strftime("%Y-%m-%d"), dates[91].strftime("%Y-%m-%d")
    assert list(panels) == [first, second]
    assert panels[first].loc["electronics", "coverage_ratio"] == 1.0


def test_historical_stock_participation_aggregates_each_sector_date_once():
    """个股滚动指标应一次计算后按行业日期聚合参与度。"""
    from morning_conference.sector_rotation2.sector_features import calculate_historical_stock_participation

    dates = pd.bdate_range("2026-01-01", periods=20)
    history = pd.DataFrame({
        "sector_name": ["electronics"] * 40,
        "stock_code": ["A"] * 20 + ["B"] * 20,
        "trade_date": list(dates) * 2,
        "amount": [100.0] * 19 + [200.0] + [100.0] * 20,
        "close": list(range(1, 21)) + list(range(20, 0, -1)),
    })

    result = calculate_historical_stock_participation(history)

    latest = result.loc[result["trade_date"] == dates[-1]].iloc[0]
    assert latest["breadth_above_ma20"] == 0.5
    assert latest["breadth_new_high_20"] == 0.5


def test_historical_sector_features_emit_one_row_per_target_date():
    """行业价格与趋势特征应按历史序列一次计算并保留每日结果。"""
    from morning_conference.sector_rotation2.sector_features import calculate_historical_sector_features

    dates = pd.bdate_range("2026-01-01", periods=90)
    sector = pd.DataFrame({"close": range(100, 190), "amount": [100.0] * 90}, index=dates)
    benchmark = pd.DataFrame({"close": range(100, 190), "amount": [1_000.0] * 90}, index=dates)

    result = calculate_historical_sector_features(sector, benchmark)

    assert len(result) == 90
    assert result.loc[dates[-1], "distance_ma20"] > 0
