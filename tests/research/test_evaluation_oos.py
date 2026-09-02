from datetime import date, timedelta

import pandas as pd

from morning_conference.sector_rotation2.research.evaluation.bootstrap import effective_block_size, moving_block_bootstrap_ci
from morning_conference.sector_rotation2.research.evaluation.config import EvaluationConfig
from morning_conference.sector_rotation2.research.evaluation.oos import build_purged_oos_windows


def test_purged_oos_signal_dates_cannot_cross_partition_exit() -> None:
    dates = tuple(date(2026, 1, 1) + timedelta(days=index) for index in range(18))
    cfg = EvaluationConfig(train_days=8, validation_days=5, test_days=5, step_days=5)
    window = build_purged_oos_windows(dates, horizon=2, config=cfg)[0]
    positions = {day: index for index, day in enumerate(dates)}
    for signals, end in ((window.train_signal_dates, window.train_end), (window.validation_signal_dates, window.validation_end), (window.test_signal_dates, window.test_end)):
        assert all(dates[positions[signal] + 2] <= end for signal in signals)


def test_block_size_is_at_least_horizon_and_bootstrap_is_deterministic() -> None:
    assert effective_block_size(horizon=1, min_block_size=10) == 10
    assert effective_block_size(horizon=20, min_block_size=10) == 20
    assert effective_block_size(horizon=40, min_block_size=10) == 40
    frame = pd.DataFrame({"signal_date": [1, 1, 2, 2, 3, 3], "return": [1, 2, 3, 4, 5, 6]})
    cfg = EvaluationConfig(bootstrap_repetitions=50, min_block_size=2)
    first = moving_block_bootstrap_ci(frame, lambda df: float(df["return"].mean()), date_col="signal_date", horizon=1, config=cfg, seed=7)
    second = moving_block_bootstrap_ci(frame, lambda df: float(df["return"].mean()), date_col="signal_date", horizon=1, config=cfg, seed=7)
    assert first == second
