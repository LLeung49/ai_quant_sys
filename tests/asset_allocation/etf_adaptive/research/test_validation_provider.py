"""Bounded adjustment provenance for production validation data."""

from datetime import date

from asset_allocation.etf_adaptive.research.validation_provider import (
    adjustment_provenance_loader,
    resolve_validation_range,
)


def test_provenance_query_is_bounded_by_requested_cutoff() -> None:
    calls = []

    def query(sql, params):
        calls.append((sql, params))
        return ({"latest_action_date": date(2024, 8, 1)},)

    payload = adjustment_provenance_loader(query, "510300.SH", date(2024, 8, 31))

    assert calls[0][1] == ("510300.SH", date(2024, 8, 31))
    assert payload["latest_action_date"] == date(2024, 8, 1)
    assert payload["complete"] is True


def test_validation_range_records_weekend_boundary_adjustments() -> None:
    sessions = (date(2026, 1, 2), date(2026, 1, 5), date(2026, 1, 6))

    resolved = resolve_validation_range(date(2026, 1, 3), date(2026, 1, 6), sessions)

    assert resolved.start_date == date(2026, 1, 5)
    assert resolved.end_date == date(2026, 1, 6)
    assert resolved.adjustments == ("start_forward",)
