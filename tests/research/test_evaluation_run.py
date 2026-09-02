from datetime import date

import pandas as pd

from morning_conference.sector_rotation2.research.evaluation.metrics import evaluate_condition
from morning_conference.sector_rotation2.research.evaluation.run_evaluation import _macd_spec, main


def test_persisted_label_frame_has_separate_coverage_counts() -> None:
    frame = pd.DataFrame({"signal_event_id": [1, 2], "forward_return": [0.1, None], "excess_return": [None, None], "mae": [None, None]})
    header, metrics = evaluate_condition(frame, _macd_spec("stock_trend"), min_cross_section_pairs=5)
    assert header["candidate_count"] == 2
    assert header["return_complete_count"] == 1
    assert header["excess_complete_count"] == 0


def test_metrics_cli_accepts_delayed_shadow(monkeypatch) -> None:
    monkeypatch.setattr("sys.argv", ["run_evaluation", "--snapshot-mode", "delayed_shadow", "--start-date", "2026-01-05", "--end-date", "2026-01-06"])
    monkeypatch.setattr("morning_conference.sector_rotation2.research.evaluation.run_evaluation.run", lambda **kwargs: {"snapshot_mode": kwargs["snapshot_mode"]})

    main()
