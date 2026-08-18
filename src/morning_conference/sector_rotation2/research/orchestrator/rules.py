"""Risk-first mapping from v1 lifecycle context and v2 direction to Opportunity."""

from collections.abc import Mapping
from typing import Any

from .models import OpportunityState


class DataQualityError(ValueError):
    """Upstream data failed the gate and must not produce a candidate snapshot."""


def classify_opportunity(v1: Mapping[str, Any], short_term_direction: str) -> OpportunityState:
    """Classify a v1-owned sector using independently normalized v2 evidence."""
    if not bool(v1.get("score_eligible", False)):
        raise DataQualityError("v1 score_eligible must be true before downstream calculation")

    lifecycle_state = str(v1.get("lifecycle_state") or "neutral")
    phase_confirmed = str(v1.get("phase_confirmed") or "neutral")
    negative_or_mixed = short_term_direction in {"negative", "mixed"}

    if lifecycle_state == "exit" or phase_confirmed == "accel_down":
        return OpportunityState.AVOID
    if lifecycle_state in {"divergence", "crowded"}:
        return OpportunityState.RISK_REDUCE if negative_or_mixed else OpportunityState.COOLING_WATCH
    if lifecycle_state == "trending":
        if negative_or_mixed:
            return OpportunityState.TREND_CONFLICT
        if short_term_direction == "positive":
            return OpportunityState.TREND_REINFORCED
        return OpportunityState.TREND_CONTINUE
    if lifecycle_state == "emerging" or phase_confirmed == "reversal_confirmed":
        if negative_or_mixed:
            return OpportunityState.REPAIR_WATCH
        if short_term_direction == "positive":
            return OpportunityState.RECOVERY_CONFIRMING
        return OpportunityState.RECOVERY_CONFIRMED
    if lifecycle_state == "repair":
        return OpportunityState.RECOVERY_EARLY if short_term_direction == "positive" else OpportunityState.REPAIR_WATCH
    return OpportunityState.NEUTRAL
