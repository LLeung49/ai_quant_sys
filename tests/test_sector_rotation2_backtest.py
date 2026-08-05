"""板块轮动前瞻标签与因子评估的纯数据测试。"""
from __future__ import annotations

import pandas as pd
import pytest

from morning_conference.sector_rotation2.backtest import build_forward_return_labels, evaluate_factor, make_forward_labels


def test_label_uses_fifth_future_trade_date():
    """horizon=5 必须取第五个未来交易日，而不是第五个自然日。"""
    dates = pd.bdate_range("2026-01-01", periods=6)
    labels = make_forward_labels(pd.Series([100, 101, 102, 103, 104, 110], index=dates), 5)

    assert labels.iloc[0]["target_date"] == dates[5]
    assert labels.iloc[0]["sector_return"] == pytest.approx(0.10)


def test_evaluate_factor_reports_positive_ic_and_quintile_spread():
    """完全单调的合成截面应产生正 IC 和正 Top-Bottom 收益差。"""
    dates = pd.bdate_range("2026-01-01", periods=2)
    snapshots = pd.DataFrame(
        [(date, f"S{rank}", rank) for date in dates for rank in range(10)],
        columns=["as_of_date", "sector_name", "composite_score"],
    )
    labels = snapshots.rename(columns={"composite_score": "excess_return"}).copy()
    labels["horizon"] = 5
    labels["target_date"] = labels["as_of_date"] + pd.offsets.BDay(5)

    result = evaluate_factor(snapshots, labels, "composite_score", 5)

    assert result["rank_ic_mean"] == pytest.approx(1.0)
    assert result["top_bottom_return"] > 0
    assert result["sample_count"] == 20


def test_evaluate_factor_rejects_duplicate_snapshot_keys():
    """同日同板块重复快照会破坏一对一标签关联，必须拒绝。"""
    snapshots = pd.DataFrame(
        [("2026-01-05", "电子", 0.1), ("2026-01-05", "电子", 0.2)],
        columns=["as_of_date", "sector_name", "composite_score"],
    )
    labels = pd.DataFrame(
        [("2026-01-05", "电子", "2026-01-12", 0.01, 5)],
        columns=["as_of_date", "sector_name", "target_date", "excess_return", "horizon"],
    )

    with pytest.raises(ValueError, match="重复"):
        evaluate_factor(snapshots, labels, "composite_score", 5)


def test_build_forward_return_labels_keeps_only_mature_dates(monkeypatch):
    """标签入口必须以交易日推进，并丢弃没有未来目标日的未成熟样本。"""
    from morning_conference.sector_rotation2 import backtest

    dates = pd.bdate_range("2026-01-01", periods=7)
    panel = {"电子": pd.DataFrame({"close": [100, 101, 102, 103, 104, 105, 106], "amount": 1.0}, index=dates)}
    monkeypatch.setattr(backtest, "load_sector_panel", lambda **_: panel)
    monkeypatch.setattr(backtest, "build_market_benchmark", lambda _: pd.DataFrame({"close": [100] * 7}, index=dates))

    result = build_forward_return_labels(2, "2026-01-01", "2026-01-07", horizons=(5,))

    assert result["as_of_date"].tolist() == [dates[0], dates[1]]
    assert result["target_date"].tolist() == [dates[5], dates[6]]
