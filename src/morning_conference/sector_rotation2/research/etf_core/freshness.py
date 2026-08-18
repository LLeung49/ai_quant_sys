"""Deterministic freshness classification for ETF holding disclosures."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Literal


FreshnessStatus = Literal["fresh", "aging", "stale"]


@dataclass(frozen=True)
class HoldingsFreshness:
    """The age, class, and confidence of one disclosed ETF holding basket."""

    reported_date: date
    age_days: int
    status: FreshnessStatus
    confidence: float


def assess_holdings_freshness(
    reported_date: date,
    target_date: date,
) -> HoldingsFreshness:
    """Classify a holding disclosure as of a mapping refresh date."""

    if reported_date > target_date:
        raise ValueError("holding report date cannot be in the future")
    age_days = (target_date - reported_date).days
    if age_days <= 90:
        status: FreshnessStatus = "fresh"
    elif age_days <= 180:
        status = "aging"
    else:
        status = "stale"
    return HoldingsFreshness(
        reported_date=reported_date,
        age_days=age_days,
        status=status,
        confidence=0.5 ** (age_days / 90),
    )
