from morning_conference.sector_rotation2.research.etf_core.selector import select_candidate_status


def test_status_priority_is_sector_then_liquidity_then_timing_then_extension() -> None:
    assert select_candidate_status(sector_allowed=False, liquid=True, macd_triggered=True, extended=False) == "blocked"
    assert select_candidate_status(sector_allowed=True, liquid=False, macd_triggered=True, extended=False) == "blocked"
    assert select_candidate_status(sector_allowed=True, liquid=True, macd_triggered=False, extended=False) == "wait_timing"
    assert select_candidate_status(sector_allowed=True, liquid=True, macd_triggered=True, extended=True) == "extended"
    assert select_candidate_status(sector_allowed=True, liquid=True, macd_triggered=True, extended=False) == "ready"
