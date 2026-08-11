from __future__ import annotations

import pandas as pd

from morning_conference.sector_rotation2.report import write_daily_reports


def test_topn_report_exposes_lifecycle_action_for_manual_review(tmp_path):
    """防止人工候选清单只显示分数而遗漏仓位动作。"""
    frame = pd.DataFrame(
        {
            "score_eligible": [True],
            "composite_rank": [1],
            "composite_score": [0.8],
            "phase_confirmed": ["accel_up"],
            "lifecycle_state": ["trending"],
            "lifecycle_action": ["hold_or_add"],
            "lifecycle_position_multiplier": [1.0],
        },
        index=["A"],
    )

    write_daily_reports(frame, "2026-08-07", tmp_path)

    text = (tmp_path / "sector_rotation2_topN_2026-08-07.txt").read_text(encoding="utf-8")
    assert "lifecycle=trending" in text
    assert "action=hold_or_add" in text
    assert "position_multiplier=1.00" in text
