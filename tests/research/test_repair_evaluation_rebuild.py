from datetime import date, timedelta

import pandas as pd
import pytest

from data_ingestion.financial_recovery.rebuild_repair_evaluation import daily_mean_bootstrap_ci
from morning_conference.sector_rotation2.research.evaluation.bootstrap import moving_block_bootstrap_ci
from morning_conference.sector_rotation2.research.evaluation.config import EvaluationConfig


def test_daily_bootstrap_matches_row_bootstrap():
    first = date(2024, 1, 2)
    frame = pd.DataFrame([
        {"signal_date": first + timedelta(days=day), "forward_return": value}
        for day, values in enumerate(((0.1, 0.2), (0.3,), (0.4, -0.1, 0.0), (0.5,)))
        for value in values
    ])
    config = EvaluationConfig(bootstrap_repetitions=25, min_block_size=2)
    expected = moving_block_bootstrap_ci(
        frame, lambda sample: float(sample["forward_return"].mean()),
        date_col="signal_date", horizon=2, config=config, seed=19,
    )
    actual = daily_mean_bootstrap_ci(frame, horizon=2, config=config, seed=19)
    assert actual == pytest.approx(expected)
