import pytest

from morning_conference.sector_rotation2.research.orchestrator.models import OpportunityState
from morning_conference.sector_rotation2.research.orchestrator.rules import DataQualityError, classify_opportunity


@pytest.mark.parametrize(
    ("v1", "direction", "expected"),
    [
        ({"score_eligible": True, "lifecycle_state": "exit"}, "positive", OpportunityState.AVOID),
        ({"score_eligible": True, "lifecycle_state": "crowded"}, "negative", OpportunityState.RISK_REDUCE),
        ({"score_eligible": True, "lifecycle_state": "trending"}, "positive", OpportunityState.TREND_REINFORCED),
        ({"score_eligible": True, "lifecycle_state": "repair"}, "positive", OpportunityState.RECOVERY_EARLY),
        ({"score_eligible": True, "lifecycle_state": "emerging"}, "negative", OpportunityState.REPAIR_WATCH),
    ],
)
def test_classify_opportunity_applies_risk_first_rules(v1: dict[str, object], direction: str, expected: OpportunityState) -> None:
    assert classify_opportunity(v1, direction) is expected


def test_ineligible_v1_data_blocks_calculation_instead_of_becoming_neutral() -> None:
    with pytest.raises(DataQualityError, match="score_eligible"):
        classify_opportunity({"score_eligible": False}, "positive")


def test_mixed_trend_evidence_is_a_trend_conflict() -> None:
    assert classify_opportunity({"score_eligible": True, "lifecycle_state": "trending"}, "mixed") is OpportunityState.TREND_CONFLICT
