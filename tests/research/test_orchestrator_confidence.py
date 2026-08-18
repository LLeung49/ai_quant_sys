from morning_conference.sector_rotation2.research.orchestrator.confidence import build_evidence, map_playbook
from morning_conference.sector_rotation2.research.orchestrator.models import OpportunityState, Playbook


def test_conflict_forces_low_confidence() -> None:
    result = build_evidence(
        v1={"phase_confidence": 0.8, "participation_score": 0.4, "rank_change_5d": 3, "lifecycle_state": "trending"},
        short_term_direction="negative", state=OpportunityState.TREND_CONFLICT,
    )
    assert result.conflict_count == 1
    assert result.confidence_level == "low"
    assert result.reasons[-1] == "short_term_direction=negative"


def test_three_supports_without_conflict_is_high() -> None:
    result = build_evidence(
        v1={"phase_confidence": 0.8, "participation_score": 0.4, "rank_change_5d": 3, "lifecycle_state": "trending"},
        short_term_direction="positive", state=OpportunityState.TREND_REINFORCED,
    )
    assert result.support_count == 4
    assert result.conflict_count == 0
    assert result.confidence_level == "high"


def test_recovery_conflict_mapping_keeps_the_reason_as_a_risk_flag() -> None:
    result = build_evidence(
        v1={"lifecycle_state": "emerging"}, short_term_direction="negative", state=OpportunityState.REPAIR_WATCH,
    )
    assert result.risk_flags == ("recovery_negative_short_term",)


def test_playbook_mapping_is_deterministic() -> None:
    assert map_playbook(OpportunityState.TREND_REINFORCED) is Playbook.TREND_FOLLOW
    assert map_playbook(OpportunityState.AVOID) is Playbook.AVOID
