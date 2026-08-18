from morning_conference.sector_rotation2.research.etf_core.selector import select_candidate_status


def test_status_priority_is_sector_then_liquidity_then_timing_then_extension() -> None:
    assert select_candidate_status(sector_allowed=False, liquid=True, macd_triggered=True, extended=False) == "blocked"
    assert select_candidate_status(sector_allowed=True, liquid=False, macd_triggered=True, extended=False) == "blocked"
    assert select_candidate_status(sector_allowed=True, liquid=True, macd_triggered=False, extended=False) == "wait_timing"
    assert select_candidate_status(sector_allowed=True, liquid=True, macd_triggered=True, extended=True) == "extended"
    assert select_candidate_status(sector_allowed=True, liquid=True, macd_triggered=True, extended=False) == "ready"


def test_stale_holdings_blocks_before_execution_gates() -> None:
    assert select_candidate_status(
        sector_allowed=True,
        liquid=True,
        macd_triggered=True,
        extended=False,
        freshness_status="stale",
    ) == "blocked"


def test_low_return_exposure_confidence_blocks_before_ready_execution_gates() -> None:
    assert select_candidate_status(
        sector_allowed=True,
        liquid=True,
        macd_triggered=True,
        extended=False,
        confidence_status="low_confidence",
    ) == "blocked"
