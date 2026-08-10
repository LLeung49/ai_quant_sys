from __future__ import annotations

import pandas as pd


def test_historical_backfill_uses_precomputed_panels_in_date_order(monkeypatch, tmp_path):
    """历史回填应只预计算一次，并按日期顺序消费每日面板。"""
    from morning_conference.sector_rotation2 import run_daily

    panels = {"2026-01-05": pd.DataFrame({"x": [1]}), "2026-01-06": pd.DataFrame({"x": [2]})}
    seen = []
    monkeypatch.setattr(run_daily, "build_historical_feature_panels", lambda *_args: panels)
    monkeypatch.setattr(run_daily, "load_historical_sector_panel", lambda *_args: {})
    monkeypatch.setattr(run_daily, "run_one_date", lambda level, as_of_date, config, output_dir, feature_panel=None, **_kwargs: seen.append((as_of_date, feature_panel.iloc[0, 0])))

    run_daily.run_historical_backfill(2, "2026-01-05", "2026-01-06", run_daily.DEFAULT_CONFIG, tmp_path)

    assert seen == [("2026-01-05", 1), ("2026-01-06", 2)]
