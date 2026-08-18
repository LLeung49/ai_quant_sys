from datetime import date, timedelta

import pytest

from morning_conference.sector_rotation2.research.etf_core.freshness import (
    assess_holdings_freshness,
)


@pytest.mark.parametrize(
    ("age", "status"),
    [(0, "fresh"), (90, "fresh"), (91, "aging"), (180, "aging"), (181, "stale")],
)
def test_holdings_freshness_classifies_exact_age_boundaries(age: int, status: str) -> None:
    freshness = assess_holdings_freshness(
        date(2026, 1, 1), date(2026, 1, 1) + timedelta(days=age)
    )

    assert freshness.reported_date == date(2026, 1, 1)
    assert freshness.age_days == age
    assert freshness.status == status
    assert freshness.confidence == pytest.approx(0.5 ** (age / 90))


def test_holdings_freshness_rejects_future_disclosure_date() -> None:
    with pytest.raises(ValueError, match="cannot be in the future"):
        assess_holdings_freshness(date(2026, 8, 19), date(2026, 8, 18))
