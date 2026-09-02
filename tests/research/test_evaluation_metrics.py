import pandas as pd
import pytest

from morning_conference.sector_rotation2.research.contracts import SignalFrameSpec
from morning_conference.sector_rotation2.research.evaluation.metrics import evaluate_condition


def test_header_and_metric_samples_remain_distinct_for_missing_outcomes() -> None:
    frame = pd.DataFrame({
        "signal_event_id": range(100), "forward_return": [0.01] * 90 + [None] * 10,
        "excess_return": [0.02] * 70 + [None] * 30,
        "mae": [-0.01] * 80 + [None] * 20, "mfe": [0.02] * 80 + [None] * 20,
        "entry_gap": [0.001] * 90 + [None] * 10,
    })
    spec = SignalFrameSpec("macd", None, (), "signal_event_id", False)
    header, metrics = evaluate_condition(frame, spec, min_cross_section_pairs=5, round_trip_cost_bps=(0.0, 10.0))
    by_name = {metric["metric_name"]: metric for metric in metrics}
    assert header == {"candidate_count": 100, "unique_event_count": 100, "return_complete_count": 90, "excess_complete_count": 70, "path_complete_count": 80}
    assert by_name["mean_return"]["sample_count"] == 90
    assert by_name["mean_excess_return"]["sample_count"] == 70
    assert by_name["mean_mae"]["sample_count"] == 80
    assert by_name["mean_net_return_bps_10"]["sample_count"] == 90
    assert "rank_ic" not in by_name


def test_short_term_rank_metrics_are_cross_section_aware() -> None:
    frame = pd.DataFrame({
        "signal_event_id": range(10), "signal_date": ["2026-01-05"] * 5 + ["2026-01-06"] * 5,
        "sector_level": [2] * 10, "signal_score": list(range(5)) * 2,
        "forward_return": [0.01, 0.02, 0.03, 0.04, 0.05] * 2,
    })
    spec = SignalFrameSpec("short_term", "signal_score", ("signal_date", "sector_level"), "signal_event_id", True)
    _, metrics = evaluate_condition(frame, spec, min_cross_section_pairs=5)
    by_name = {metric["metric_name"]: metric for metric in metrics}
    assert by_name["rank_ic"]["metric_value"] == pytest.approx(1.0)
    assert by_name["rank_ic"]["sample_count"] == 2
    assert by_name["top_bottom_spread"]["metric_value"] == pytest.approx(0.035)
