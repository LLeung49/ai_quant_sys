"""板块轮动前瞻标签与因子评估的纯数据测试。"""
from __future__ import annotations

from decimal import Decimal

import pandas as pd
import pytest

from morning_conference.sector_rotation2.backtest import (
    build_forward_return_labels,
    evaluate_factor,
    expanding_outer_windows,
    make_forward_labels,
    rolling_oos_windows,
    select_inner_candidate,
)


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


def test_evaluate_factor_accepts_multi_horizon_labels_when_evaluating_one_horizon():
    """多期限标签应以日期、行业、期限联合唯一，不能被误判为重复。"""
    dates = pd.bdate_range("2026-01-01", periods=2)
    snapshots = pd.DataFrame(
        [(date, f"S{rank}", rank) for date in dates for rank in range(10)],
        columns=["as_of_date", "sector_name", "composite_score"],
    )
    labels = snapshots.rename(columns={"composite_score": "excess_return"}).copy()
    labels["horizon"] = 1
    labels["target_date"] = labels["as_of_date"] + pd.offsets.BDay(1)
    labels = pd.concat([labels, labels.assign(horizon=2, target_date=labels["target_date"] + pd.offsets.BDay(1))])

    result = evaluate_factor(snapshots, labels, "composite_score", 1)

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


def test_build_forward_return_labels_uses_all_alpha_decay_horizons_by_default(monkeypatch):
    """默认研究标签必须覆盖短、中期全部 Alpha Decay 期限。"""
    from morning_conference.sector_rotation2 import backtest

    dates = pd.bdate_range("2026-01-01", periods=45)
    panel = {
        "电子": pd.DataFrame(
            {"close": range(100, 145), "amount": 1.0},
            index=dates,
        )
    }
    monkeypatch.setattr(backtest, "load_sector_panel", lambda **_: panel)
    monkeypatch.setattr(backtest, "build_market_benchmark", lambda _: pd.DataFrame({"close": [100.0] * 45}, index=dates))

    result = build_forward_return_labels(2, "2026-01-01", "2026-03-31")

    assert sorted(result["horizon"].unique()) == [1, 2, 3, 5, 10, 20, 40]


def test_evaluate_factor_reports_win_rate_drawdown_and_turnover():
    """评估结果应包含 Top 组胜率、累计收益最大回撤和相邻日 Top 组换手。"""
    dates = pd.bdate_range("2026-01-01", periods=3)
    snapshots = pd.DataFrame(
        [(date, f"S{rank}", rank) for date in dates for rank in range(10)],
        columns=["as_of_date", "sector_name", "composite_score"],
    )
    labels = snapshots.rename(columns={"composite_score": "excess_return"}).copy()
    labels["horizon"] = 5
    labels["target_date"] = labels["as_of_date"] + pd.offsets.BDay(5)

    result = evaluate_factor(snapshots, labels, "composite_score", 5)

    assert result["top_group_win_rate"] == 1.0
    assert result["top_group_turnover"] == 0.0
    assert result["top_group_max_drawdown"] == 0.0


def test_rolling_oos_windows_uses_252_63_21_contract():
    """滚动样本外窗口固定为 252 日训练、63 日验证、21 日步长。"""
    dates = pd.bdate_range("2024-01-01", periods=399)

    windows = rolling_oos_windows(dates)

    assert len(windows) == 5
    assert windows[0]["train_start"] == dates[0]
    assert windows[0]["validation_start"] == dates[252]
    assert windows[1]["train_start"] == dates[21]


def test_expanding_outer_windows_uses_non_overlapping_validation_periods():
    dates = pd.bdate_range("2022-01-03", periods=756)

    windows = expanding_outer_windows(dates, train_days=504, validation_days=126, step_days=126)

    assert len(windows) == 2
    assert windows[0]["train_start"] == dates[0]
    assert windows[0]["train_end"] == dates[503]
    assert windows[0]["validation_start"] == dates[504]
    assert windows[0]["validation_end"] == dates[629]
    assert windows[1]["train_start"] == dates[0]
    assert windows[1]["train_end"] == dates[629]
    assert windows[1]["validation_start"] == dates[630]


def test_select_inner_candidate_requires_all_frozen_gates_and_uses_fixed_tie_order():
    dates = pd.bdate_range("2026-01-01", periods=3)
    snapshots = pd.DataFrame(
        [
            (date, f"S{rank}", rank, -rank)
            for date in dates for rank in range(10)
        ],
        columns=["as_of_date", "sector_name", "good", "bad"],
    )
    labels = pd.DataFrame(
        [
            (date, f"S{rank}", date + pd.offsets.BDay(1), 1, rank / 100)
            for date in dates for rank in range(10)
        ],
        columns=["as_of_date", "sector_name", "target_date", "horizon", "excess_return"],
    )
    inner_windows = [{
        "train_start": dates[0], "train_end": dates[0],
        "validation_start": dates[1], "validation_end": dates[2],
    }]

    selected = select_inner_candidate(
        snapshots, labels, ("good", "bad"), (1,), inner_windows, cost_bps=10,
    )

    assert selected["selected"] is True
    assert selected["candidate"] == "good"
    assert selected["horizon"] == 1
    assert selected["positive_rank_ic_share"] == 1.0


def test_select_inner_candidate_returns_no_selection_when_any_gate_fails():
    dates = pd.bdate_range("2026-01-01", periods=3)
    snapshots = pd.DataFrame(
        [(date, f"S{rank}", -rank) for date in dates for rank in range(10)],
        columns=["as_of_date", "sector_name", "bad"],
    )
    labels = pd.DataFrame(
        [
            (date, f"S{rank}", date + pd.offsets.BDay(1), 1, rank / 100)
            for date in dates for rank in range(10)
        ],
        columns=["as_of_date", "sector_name", "target_date", "horizon", "excess_return"],
    )
    inner_windows = [{
        "train_start": dates[0], "train_end": dates[0],
        "validation_start": dates[1], "validation_end": dates[2],
    }]

    selected = select_inner_candidate(snapshots, labels, ("bad",), (1,), inner_windows, cost_bps=10)

    assert selected["selected"] is False
    assert selected["candidate"] is None


def test_evaluate_rolling_oos_scores_only_validation_dates():
    """逐窗口 OOS 指标只能使用验证区间，不能混入训练日期。"""
    from morning_conference.sector_rotation2 import backtest

    dates = pd.bdate_range("2026-01-01", periods=4)
    snapshots = pd.DataFrame(
        [(date, f"S{rank}", rank) for date in dates for rank in range(10)],
        columns=["as_of_date", "sector_name", "composite_score"],
    )
    labels = snapshots.rename(columns={"composite_score": "excess_return"}).copy()
    labels["horizon"] = 1
    labels["target_date"] = labels["as_of_date"] + pd.offsets.BDay(1)
    windows = [{
        "train_start": dates[0], "train_end": dates[1],
        "validation_start": dates[2], "validation_end": dates[3],
    }]

    result = backtest.evaluate_rolling_oos(snapshots, labels, "composite_score", 1, windows)

    assert result.loc[0, "sample_count"] == 20
    assert result.loc[0, "validation_start"] == dates[2]


def test_top_group_strategy_charges_turnover_cost_after_lagged_signal_changes():
    """换组时必须扣除成本，且持仓只能由前一交易日的 Score 决定。"""
    from morning_conference.sector_rotation2 import backtest

    dates = pd.bdate_range("2026-01-01", periods=4)
    snapshots = pd.DataFrame(
        [(dates[0], f"S{rank}", rank) for rank in range(10)]
        + [(dates[1], f"S{rank}", 9 - rank) for rank in range(10)]
        + [(dates[2], f"S{rank}", 9 - rank) for rank in range(10)],
        columns=["as_of_date", "sector_name", "composite_score"],
    )
    labels = pd.DataFrame(
        [(date, f"S{rank}", date + pd.offsets.BDay(1), 0.01) for date in dates[1:] for rank in range(10)],
        columns=["as_of_date", "sector_name", "target_date", "excess_return"],
    )
    labels["horizon"] = 1

    result = backtest.simulate_top_group_strategy(snapshots, labels, "composite_score", rebalance_every=1, cost_bps=10)

    assert result["transaction_cost"] > 0
    assert result["net_return"] < result["gross_return"]


def test_top_group_strategy_accepts_decimal_scores_from_database():
    """数据库 DECIMAL 类型的 Score 必须能参与分位选组。"""
    from morning_conference.sector_rotation2 import backtest

    dates = pd.bdate_range("2026-01-01", periods=2)
    snapshots = pd.DataFrame(
        [(dates[0], f"S{rank}", Decimal(str(rank))) for rank in range(10)],
        columns=["as_of_date", "sector_name", "composite_score"],
    )
    labels = pd.DataFrame(
        [(dates[1], f"S{rank}", dates[1] + pd.offsets.BDay(1), Decimal("0.01")) for rank in range(10)],
        columns=["as_of_date", "sector_name", "target_date", "excess_return"],
    )
    labels["horizon"] = 1

    result = backtest.simulate_top_group_strategy(snapshots, labels, "composite_score", rebalance_every=1, cost_bps=10)

    assert result["net_return"] == pytest.approx(0.009)


def test_run_research_writes_alpha_decay_report(tmp_path, monkeypatch):
    """研究入口必须输出披露数据口径和非交易性质的 Alpha Decay 报告。"""
    from morning_conference.sector_rotation2 import run_backtest

    dates = pd.bdate_range("2026-01-01", periods=3)
    snapshots = pd.DataFrame(
        [(date, f"S{rank}", rank, "range") for date in dates for rank in range(10)],
        columns=["as_of_date", "sector_name", "composite_score", "market_regime"],
    )
    labels = snapshots.rename(columns={"composite_score": "excess_return"}).drop(columns=["market_regime"])
    labels["horizon"] = 1
    labels["target_date"] = labels["as_of_date"] + pd.offsets.BDay(1)
    monkeypatch.setattr(run_backtest, "build_forward_return_labels", lambda *_: labels)
    monkeypatch.setattr(run_backtest, "persist_forward_returns", lambda *_: 0)
    monkeypatch.setattr(run_backtest, "execute_query", lambda *_: snapshots)
    monkeypatch.setattr(run_backtest, "rolling_oos_windows", lambda _: [])

    run_backtest.run_research(2, "2026-01-01", "2026-12-31", "v1", tmp_path)

    report = (tmp_path / "sector_rotation2_alpha_decay_2026-12-31.md").read_text(encoding="utf-8")
    assert "current_mapping" in report
    assert "不产生交易指令" in report


def test_run_research_accepts_database_dictionary_rows(tmp_path, monkeypatch):
    from morning_conference.sector_rotation2 import run_backtest
    dates = pd.bdate_range("2026-01-01", periods=2)
    rows = [{"as_of_date": date.date(), "sector_name": f"S{rank}", "composite_score": rank, "market_regime": "range"} for date in dates for rank in range(10)]
    labels = pd.DataFrame(rows).rename(columns={"composite_score": "excess_return"}).drop(columns=["market_regime"])
    labels["horizon"] = 1; labels["target_date"] = labels["as_of_date"] + pd.offsets.BDay(1)
    monkeypatch.setattr(run_backtest, "build_forward_return_labels", lambda *_: labels)
    monkeypatch.setattr(run_backtest, "persist_forward_returns", lambda *_: 0)
    monkeypatch.setattr(run_backtest, "execute_query", lambda *_: rows)
    monkeypatch.setattr(run_backtest, "rolling_oos_windows", lambda _: [])
    run_backtest.run_research(2, "2026-01-01", "2026-01-02", "v1", tmp_path)
    assert (tmp_path / "sector_rotation2_research_2026-01-02.csv").exists()
