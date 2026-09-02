from datetime import date

from morning_conference.sector_rotation2.research.evaluation.config import EvaluationConfig
from morning_conference.sector_rotation2.research.evaluation.oos import build_purged_oos_windows, signal_scope


def test_signal_scope_excludes_horizon_purge_tail() -> None:
    dates = tuple(date(2026, 1, day) for day in range(1, 19))
    config = EvaluationConfig(train_days=8, validation_days=5, test_days=5, step_days=5)
    window = build_purged_oos_windows(dates, horizon=2, config=config)[0]
    assert signal_scope(window, dates[0]) == "train"
    assert signal_scope(window, dates[6]) is None
    assert signal_scope(window, dates[8]) == "validation"
    assert signal_scope(window, dates[11]) is None
