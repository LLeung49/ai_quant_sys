"""每日板块轮动编排的无数据库集成测试。"""
from __future__ import annotations

import pandas as pd
import pytest

from morning_conference.sector_rotation2.config import ModelConfig


def _feature_panel() -> pd.DataFrame:
    """构造足以经过评分和状态机的确定性日特征。"""
    return pd.DataFrame(
        {
            "rs_20": [0.03, 0.00, -0.03], "rs_60": [0.04, 0.00, -0.04],
            "distance_ma20": [0.03, 0.00, -0.03], "distance_ma60": [0.04, 0.00, -0.04],
            "rs_5": [0.02, 0.00, -0.02], "ma20_slope": [2.0, 0.0, -2.0],
            "rs20_accel": [0.02, 0.0, -0.02], "ma20_accel": [1.0, 0.0, -1.0],
            "macd_hist_delta": [0.3, 0.0, -0.3], "rvol_5_20": [1.4, 1.0, 0.8],
            "share_impulse": [1.3, 1.0, 0.8], "breadth_up": [0.8, 0.5, 0.2],
            "breadth_above_ma20": [0.8, 0.5, 0.2], "breadth_new_high_20": [0.6, 0.3, 0.1],
            "breadth_rvol": [0.8, 0.5, 0.2], "coverage_ratio": [1.0, 1.0, 1.0],
        },
        index=["强势", "中性", "弱势"],
    )


def _benchmark() -> pd.DataFrame:
    """构造满足 risk_on 的市场基准历史。"""
    return pd.DataFrame(
        {"close": [100.0 + day * 0.2 for day in range(61)], "amount": [100.0] * 60 + [150.0]},
        index=pd.date_range("2026-01-01", periods=61, freq="B"),
    )


def test_run_writes_reports_only_after_snapshot_persistence(monkeypatch, tmp_path):
    """快照事务成功后才生成日明细、TopN 与数据质量三类输出。"""
    from morning_conference.sector_rotation2 import run_daily

    calls: list[str] = []
    monkeypatch.setattr(run_daily, "build_daily_feature_panel", lambda **_: _feature_panel())
    monkeypatch.setattr(run_daily, "load_market_benchmark", lambda **_: _benchmark())
    monkeypatch.setattr(run_daily, "load_previous_snapshots", lambda **_: None)
    monkeypatch.setattr(run_daily, "create_run", lambda *args, **kwargs: calls.append("create"))
    monkeypatch.setattr(run_daily, "persist_daily_snapshot", lambda *args, **kwargs: calls.append("persist") or 3)
    monkeypatch.setattr(run_daily, "mark_run_succeeded", lambda *args, **kwargs: calls.append("success"))

    result = run_daily.run_one_date(2, "2026-03-26", ModelConfig(min_cross_section=3), tmp_path)

    assert calls == ["create", "persist", "success"]
    assert len(result) == 3
    assert (tmp_path / "sector_rotation2_daily_2026-03-26.csv").exists()
    assert (tmp_path / "sector_rotation2_topN_2026-03-26.txt").exists()
    assert (tmp_path / "sector_rotation2_data_quality_2026-03-26.csv").exists()


def test_run_marks_failed_and_writes_no_success_report_when_snapshot_fails(monkeypatch, tmp_path):
    """持久化失败必须记录审计失败，且不能遗留成功口径的输出文件。"""
    from morning_conference.sector_rotation2 import run_daily

    failures: list[str] = []
    monkeypatch.setattr(run_daily, "build_daily_feature_panel", lambda **_: _feature_panel())
    monkeypatch.setattr(run_daily, "load_market_benchmark", lambda **_: _benchmark())
    monkeypatch.setattr(run_daily, "load_previous_snapshots", lambda **_: None)
    monkeypatch.setattr(run_daily, "create_run", lambda *args, **kwargs: None)
    monkeypatch.setattr(run_daily, "persist_daily_snapshot", lambda *args, **kwargs: (_ for _ in ()).throw(RuntimeError("db down")))
    monkeypatch.setattr(run_daily, "mark_run_failed", lambda _, error: failures.append(error))

    with pytest.raises(RuntimeError, match="db down"):
        run_daily.run_one_date(2, "2026-03-26", ModelConfig(min_cross_section=3), tmp_path)

    assert failures == ["db down"]
    assert not list(tmp_path.glob("sector_rotation2_*_2026-03-26.*"))


def test_backfill_dates_are_processed_in_ascending_order(monkeypatch, tmp_path):
    """回填必须从早到晚调用单日入口，确保 phase 只依赖此前快照。"""
    from morning_conference.sector_rotation2 import run_daily

    seen: list[str] = []
    monkeypatch.setattr(run_daily, "list_trade_dates", lambda **_: ["2026-03-27", "2026-03-25", "2026-03-26"])
    monkeypatch.setattr(run_daily, "run_one_date", lambda level, as_of_date, config, output_dir: seen.append(as_of_date))

    run_daily.run_backfill(2, "2026-03-25", "2026-03-27", ModelConfig(), tmp_path)

    assert seen == ["2026-03-25", "2026-03-26", "2026-03-27"]
