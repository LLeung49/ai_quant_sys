"""Tests for the financial PIT resolver."""

from datetime import date

import pytest

from morning_conference.sector_rotation2.research.financial.pit import (
    FinancialRawRow,
    PITStatus,
    classify_pit,
    filter_strict,
    resolve_latest_visible,
)


def _row(**overrides) -> FinancialRawRow:
    base = dict(
        stock_code="600000",
        source_table="miniqmt",
        report_date=date(2026, 6, 30),
        period_type="quarterly",
        announcement_date=date(2026, 7, 25),
        first_seen_at=date(2026, 7, 25),
        source_hash="hash_1",
        is_restated=False,
        source_verified=False,
        data_source="miniqmt",
    )
    base.update(overrides)
    return FinancialRawRow(**base)


def test_classify_pit_prefers_explicit_status() -> None:
    row = _row()
    assert classify_pit({
        "announcement_date": row.announcement_date,
        "first_seen_at": row.first_seen_at,
        "is_restated": row.is_restated,
        "pit_status": "pit_estimated",
    }) == PITStatus.ESTIMATED


def test_classify_pit_exact_when_announcement_present_and_not_restated() -> None:
    assert classify_pit({
        "announcement_date": date(2026, 7, 25),
        "first_seen_at": date(2026, 7, 25),
        "is_restated": False,
    }) == PITStatus.EXACT


def test_classify_pit_verified_when_source_verified_only() -> None:
    assert classify_pit({
        "announcement_date": None,
        "first_seen_at": date(2026, 7, 25),
        "is_restated": False,
        "source_verified": True,
    }) == PITStatus.VERIFIED


def test_classify_pit_estimated_when_only_first_seen() -> None:
    assert classify_pit({
        "announcement_date": None,
        "first_seen_at": date(2026, 7, 25),
        "is_restated": False,
    }) == PITStatus.ESTIMATED


def test_classify_pit_invalid_when_both_dates_missing() -> None:
    assert classify_pit({
        "announcement_date": None,
        "first_seen_at": None,
        "is_restated": False,
    }) == PITStatus.INVALID


def test_resolve_latest_visible_picks_most_recent_announcement() -> None:
    rows = [
        _row(report_date=date(2025, 12, 31), announcement_date=date(2026, 1, 25), source_hash="old"),
        _row(report_date=date(2026, 3, 31), announcement_date=date(2026, 4, 25), source_hash="mid"),
        _row(report_date=date(2026, 6, 30), announcement_date=date(2026, 7, 25), source_hash="new"),
    ]
    out = resolve_latest_visible(rows, as_of_date=date(2026, 8, 1))
    assert out is not None
    assert out.source_hash == "new"


def test_resolve_latest_visible_excludes_future_announcement() -> None:
    rows = [
        _row(report_date=date(2026, 6, 30), announcement_date=date(2026, 9, 1)),
    ]
    out = resolve_latest_visible(rows, as_of_date=date(2026, 8, 1))
    assert out is None


def test_resolve_latest_visible_excludes_estimated_by_default() -> None:
    rows = [
        _row(report_date=date(2026, 6, 30), announcement_date=None),
    ]
    assert resolve_latest_visible(rows, as_of_date=date(2026, 8, 1)) is None


def test_resolve_latest_visible_allows_estimated_with_flag() -> None:
    row = _row(report_date=date(2026, 6, 30), announcement_date=None)
    out = resolve_latest_visible([row], as_of_date=date(2026, 8, 1), allow_estimated_pit=True)
    assert out is not None
    assert out.source_hash == row.source_hash


def test_resolve_latest_visible_uses_dated_restated_version_after_announcement() -> None:
    rows = [
        _row(report_date=date(2026, 6, 30), announcement_date=date(2026, 7, 25),
             source_hash="restated", is_restated=True),
        _row(report_date=date(2026, 3, 31), announcement_date=date(2026, 4, 25),
             source_hash="original", is_restated=False),
    ]
    out = resolve_latest_visible(rows, as_of_date=date(2026, 8, 1))
    assert out is not None
    assert out.source_hash == "restated"


def test_restated_version_with_announcement_is_exact() -> None:
    row = _row(source_table="qmt_native_composite", data_source="qmt",
               is_restated=True, pit_status="EXACT")
    assert classify_pit(row) == PITStatus.EXACT
    assert resolve_latest_visible([row], as_of_date=date(2026, 7, 24)) is None
    assert resolve_latest_visible([row], as_of_date=date(2026, 7, 25)) == row


def test_latest_period_wins_over_late_revision_of_older_period() -> None:
    rows = [
        _row(report_date=date(2025, 12, 31),
             announcement_date=date(2026, 8, 1), source_hash="old_revised",
             is_restated=True),
        _row(report_date=date(2026, 6, 30),
             announcement_date=date(2026, 7, 25), source_hash="new_period"),
    ]
    assert resolve_latest_visible(rows, as_of_date=date(2026, 8, 2)).source_hash == "new_period"


def test_dated_qmt_version_has_priority_over_akshare_same_period() -> None:
    rows = [
        _row(source_table="qmt_native_composite", data_source="qmt",
             report_date=date(2026, 3, 31), announcement_date=date(2026, 4, 29),
             source_hash="qmt"),
        _row(source_table="akshare_eastmoney_financial", data_source="akshare",
             report_date=date(2026, 3, 31), announcement_date=date(2026, 5, 2),
             source_hash="akshare"),
    ]
    assert resolve_latest_visible(rows, as_of_date=date(2026, 4, 28)) is None
    assert resolve_latest_visible(rows, as_of_date=date(2026, 4, 30)).source_hash == "qmt"
    assert resolve_latest_visible(rows, as_of_date=date(2026, 5, 3)).source_hash == "qmt"


def test_filter_strict_keeps_only_exact_and_verified() -> None:
    rows = [
        _row(announcement_date=date(2026, 7, 25)),  # EXACT
        _row(announcement_date=None, source_verified=True),  # VERIFIED
        _row(announcement_date=None, source_verified=False),  # ESTIMATED
    ]
    out = filter_strict(rows)
    assert len(out) == 2


@pytest.mark.parametrize("explicit_status", [None, "pit_exact", "EXACT"])
def test_legacy_qmt_period_date_is_not_an_announcement(explicit_status) -> None:
    row = _row(
        source_table="trade_stock_financial",
        data_source="qmt",
        report_date=date(2025, 12, 31),
        announcement_date=date(2025, 12, 31),
        first_seen_at=date(2026, 2, 27),
        source_verified=True,
        pit_status=explicit_status,
    )
    assert classify_pit(row) == PITStatus.ESTIMATED
    assert filter_strict([row]) == []
    assert resolve_latest_visible([row], as_of_date=date(2026, 1, 15)) is None
    assert resolve_latest_visible(
        [row], as_of_date=date(2026, 1, 15), allow_estimated_pit=True
    ) is None
    assert resolve_latest_visible(
        [row], as_of_date=date(2026, 3, 1), allow_estimated_pit=True
    ) == row


def test_same_day_announcement_from_independent_source_remains_visible() -> None:
    row = _row(
        source_table="akshare_eastmoney_financial",
        data_source="akshare",
        report_date=date(2025, 12, 31),
        announcement_date=date(2025, 12, 31),
    )
    assert classify_pit(row) == PITStatus.EXACT


def test_pit_status_enum_values() -> None:
    assert PITStatus.EXACT.value == "pit_exact"
    assert PITStatus.VERIFIED.value == "pit_verified"
    assert PITStatus.ESTIMATED.value == "pit_estimated"
    assert PITStatus.INVALID.value == "pit_invalid"
