"""State and playbook vocabulary for sector opportunity snapshots."""

from enum import Enum


class _StringEnum(str, Enum):
    pass


class OpportunityState(_StringEnum):
    TREND_REINFORCED = "trend_reinforced"
    TREND_CONTINUE = "trend_continue"
    TREND_CONFLICT = "trend_conflict"
    RECOVERY_EARLY = "recovery_early"
    RECOVERY_CONFIRMING = "recovery_confirming"
    RECOVERY_CONFIRMED = "recovery_confirmed"
    REPAIR_WATCH = "repair_watch"
    COOLING_WATCH = "cooling_watch"
    RISK_REDUCE = "risk_reduce"
    AVOID = "avoid"
    NEUTRAL = "neutral"


class Playbook(_StringEnum):
    TREND_FOLLOW = "trend_follow"
    REPAIR_PROBE = "repair_probe"
    EARLY_REPAIR = "early_repair"
    HOLD_ONLY = "hold_only"
    RISK_REDUCE = "risk_reduce"
    AVOID = "avoid"
    OBSERVE = "observe"
