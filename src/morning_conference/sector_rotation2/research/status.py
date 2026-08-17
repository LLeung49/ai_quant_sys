"""Lifecycle values shared by all Research Cockpit V0 outputs."""

from enum import Enum


class _StringEnum(str, Enum):
    """Python-version-compatible string enum base."""


class ResearchStatus(_StringEnum):
    DRAFT = "draft"
    SHADOW = "shadow"
    VALIDATED = "validated"
    REJECTED = "rejected"


class ValidationStatus(_StringEnum):
    NOT_EVALUATED = "not_evaluated"
    EVALUATING = "evaluating"
    VALIDATED = "validated"
    REJECTED = "rejected"


class ExecutionStatus(_StringEnum):
    MANUAL_ONLY = "manual_only"


class SnapshotMode(_StringEnum):
    LIVE_SHADOW = "live_shadow"
    BACKFILL = "backfill"
    REPLAY = "replay"
