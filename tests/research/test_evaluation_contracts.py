from morning_conference.sector_rotation2.research.contracts import BenchmarkStatus, ReturnStatus
from morning_conference.sector_rotation2.research.evaluation.config import DEFAULT_EVALUATION_CONFIG


def test_default_horizons_and_cost_grid() -> None:
    cfg = DEFAULT_EVALUATION_CONFIG
    assert cfg.horizons["short_term"] == (1, 2, 3)
    assert cfg.horizons["stock_repair"] == (10, 20, 40)
    assert cfg.entry_mode == "next_open"
    assert cfg.min_block_size == 10
    assert cfg.round_trip_cost_bps == (0.0, 5.0, 10.0, 20.0)


def test_forward_label_status_is_not_only_boolean() -> None:
    assert ReturnStatus.COMPLETE.value == "complete"
    assert ReturnStatus.NOT_MATURED.value == "not_matured"
    assert ReturnStatus.UNEXECUTABLE_ENTRY.value == "unexecutable_entry"
    assert BenchmarkStatus.UNSUPPORTED_WINDOW.value == "unsupported_window"
