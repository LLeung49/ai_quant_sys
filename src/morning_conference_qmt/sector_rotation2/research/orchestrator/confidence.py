"""Auditable categorical evidence for Sector Opportunity, never return forecasts."""

from dataclasses import dataclass
from collections.abc import Mapping
from typing import Any

from .models import OpportunityState, Playbook


@dataclass(frozen=True)
class OpportunityEvidence:
    support_count: int
    conflict_count: int
    confidence_level: str
    primary_reason: str
    reasons: tuple[str, ...]
    risk_flags: tuple[str, ...]


_PLAYBOOKS = {
    OpportunityState.TREND_REINFORCED: Playbook.TREND_FOLLOW,
    OpportunityState.TREND_CONTINUE: Playbook.TREND_FOLLOW,
    OpportunityState.TREND_CONFLICT: Playbook.HOLD_ONLY,
    OpportunityState.RECOVERY_EARLY: Playbook.EARLY_REPAIR,
    OpportunityState.RECOVERY_CONFIRMING: Playbook.REPAIR_PROBE,
    OpportunityState.RECOVERY_CONFIRMED: Playbook.REPAIR_PROBE,
    OpportunityState.REPAIR_WATCH: Playbook.OBSERVE,
    OpportunityState.COOLING_WATCH: Playbook.HOLD_ONLY,
    OpportunityState.RISK_REDUCE: Playbook.RISK_REDUCE,
    OpportunityState.AVOID: Playbook.AVOID,
    OpportunityState.NEUTRAL: Playbook.OBSERVE,
}


def map_playbook(state: OpportunityState) -> Playbook:
    return _PLAYBOOKS[state]


def build_evidence(
    v1: Mapping[str, Any], short_term_direction: str, state: OpportunityState,
) -> OpportunityEvidence:
    reasons: list[str] = []
    risk_flags: list[str] = []
    support_count = 0
    lifecycle_state = str(v1.get("lifecycle_state") or "neutral")
    phase_confidence = v1.get("phase_confidence")

    if phase_confidence is not None and float(phase_confidence) >= 0.60:
        support_count += 1
        reasons.append("phase_confidence>=0.60")
    if (participation := v1.get("participation_score")) is not None and float(participation) > 0:
        support_count += 1
        reasons.append("participation_score>0")
    if (rank_change := v1.get("rank_change_5d")) is not None and float(rank_change) > 0:
        support_count += 1
        reasons.append("rank_change_5d>0")

    aligned = (
        short_term_direction == "positive"
        and state in {OpportunityState.TREND_REINFORCED, OpportunityState.RECOVERY_EARLY, OpportunityState.RECOVERY_CONFIRMING}
    )
    if aligned:
        support_count += 1
        reasons.append("short_term_direction=positive")

    conflict = short_term_direction == "mixed" or (
        short_term_direction == "negative"
        and state in {OpportunityState.TREND_CONFLICT, OpportunityState.REPAIR_WATCH, OpportunityState.RISK_REDUCE}
    )
    if conflict:
        reasons.append(f"short_term_direction={short_term_direction}")
        if lifecycle_state in {"emerging", "repair"} and state is OpportunityState.REPAIR_WATCH:
            risk_flags.append("recovery_negative_short_term")
        else:
            risk_flags.append("short_term_conflict")

    conflict_count = int(conflict)
    confidence_level = "low" if conflict_count else "high" if support_count >= 3 else "medium"
    primary_reason = reasons[0] if reasons else f"lifecycle_state={lifecycle_state}"
    return OpportunityEvidence(
        support_count, conflict_count, confidence_level, primary_reason, tuple(reasons), tuple(risk_flags),
    )

