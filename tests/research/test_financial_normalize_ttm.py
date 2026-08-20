"""Tests for normalize + TTM + capital layers."""

from datetime import date, timedelta

import pytest

from morning_conference.sector_rotation2.research.financial.capital import (
    ResolvedCapital,
    resolve_capital,
)
from morning_conference.sector_rotation2.research.financial.normalize import (
    normalize_row,
    normalize_rows,
    to_mapping,
)
from morning_conference.sector_rotation2.research.financial.pit import FinancialRawRow
from morning_conference.sector_rotation2.research.financial.providers.base import (
    CapitalRow,
)
from morning_conference.sector_rotation2.research.financial.ttm import (
    TTM_QUARTERS,
    build_ttm,
)


def _raw_row(**overrides) -> FinancialRawRow:
    base = dict(
        stock_code="600000",
        source_table="miniqmt",
        report_date=date(2026, 6, 30),
        period_type="quarterly",
        announcement_date=date(2026, 7, 25),
        first_seen_at=date(2026, 7, 25),
        source_hash="h1",
        is_restated=False,
        source_verified=True,
        data_source="miniqmt",
        revenue=100.0,
        net_profit=10.0,
        total_assets=200.0,
        total_equity=80.0,
        operating_cash_flow=12.0,
    )
    base.update(overrides)
    return FinancialRawRow(**base)


def _quarter_chain(start: date, count: int = TTM_QUARTERS) -> list[FinancialRawRow]:
    """Build ``count`` quarterly rows spaced by ~90 days from ``start``."""

    rows: list[FinancialRawRow] = []
    for i in range(count):
        report = start + timedelta(days=90 * i)
        announce = report + timedelta(days=25)
        rows.append(_raw_row(
            report_date=report,
            announcement_date=announce,
            source_hash=f"h{i}",
            revenue=100.0,
            net_profit=10.0,
            operating_cash_flow=12.0,
        ))
    return rows


def test_normalize_row_surfaces_missing_field_flags() -> None:
    row = normalize_row(_raw_row(revenue=None, operating_cash_flow=None))
    assert "missing_revenue" in row.quality_flags
    assert "missing_operating_cash_flow" in row.quality_flags
    assert row.pit_status == "pit_unclassified"


def test_normalize_row_flags_restated() -> None:
    row = normalize_row(_raw_row(is_restated=True))
    assert "restated" in row.quality_flags


def test_normalize_rows_and_mapping_round_trip() -> None:
    rows = normalize_rows([_raw_row(source_hash="a"), _raw_row(source_hash="b")])
    out = to_mapping(rows[0])
    assert out["stock_code"] == "600000"
    assert out["source_hash"] == "a"
    assert out["quality_flags"] == []


def test_build_ttm_sums_four_quarters() -> None:
    ttm = build_ttm(_quarter_chain(date(2025, 9, 30)), as_of_date=date(2026, 8, 1))
    assert ttm is not None
    assert ttm.revenue == pytest.approx(400.0)
    assert ttm.net_profit == pytest.approx(40.0)
    assert ttm.operating_cash_flow == pytest.approx(48.0)
    assert ttm.is_complete is True


def test_build_ttm_returns_none_with_fewer_than_four_quarters() -> None:
    quarters = [
        _raw_row(report_date=date(2026, 3, 31), announcement_date=date(2026, 4, 25), source_hash="h1"),
        _raw_row(report_date=date(2026, 6, 30), announcement_date=date(2026, 7, 25), source_hash="h2"),
    ]
    ttm = build_ttm(quarters, as_of_date=date(2026, 8, 1))
    assert ttm is None


def test_build_ttm_excludes_future_announcements() -> None:
    rows = [_raw_row(report_date=date(2026, 6, 30), announcement_date=date(2026, 9, 1))]
    assert build_ttm(rows, as_of_date=date(2026, 8, 1)) is None


def test_build_ttm_flags_partial_revenue_but_returns_projection() -> None:
    """A missing revenue still surfaces a TTM with the field set to None.

    The Repair pipeline emits the projection with a quality flag; downstream
    valuation knows not to compute a PE when ``revenue`` is ``None``.
    """

    chain = _quarter_chain(date(2025, 9, 30))
    chain[1] = _raw_row(
        report_date=chain[1].report_date,
        announcement_date=chain[1].announcement_date,
        source_hash="h1",
        revenue=None,
        net_profit=10.0,
    )
    ttm = build_ttm(chain, as_of_date=date(2026, 8, 1))
    assert ttm is not None
    assert ttm.revenue is None
    assert ttm.net_profit == pytest.approx(40.0)
    assert "partial_revenue" in ttm.quality_flags


def test_build_ttm_flags_restated_components() -> None:
    chain = _quarter_chain(date(2025, 9, 30))
    chain[1] = _raw_row(
        report_date=chain[1].report_date,
        announcement_date=chain[1].announcement_date,
        source_hash="h1",
        revenue=100.0,
        net_profit=10.0,
        is_restated=True,
    )
    ttm = build_ttm(chain, as_of_date=date(2026, 8, 1))
    assert ttm is not None
    assert "contains_restated" in ttm.quality_flags


def test_resolve_capital_picks_latest_announcement() -> None:
    rows = [
        CapitalRow(
            stock_code="600000", report_date=date(2025, 12, 31),
            announcement_date=date(2026, 1, 25), total_shares=900.0,
            circulating_shares=850.0, source_hash="old", data_source="miniqmt",
        ),
        CapitalRow(
            stock_code="600000", report_date=date(2026, 6, 30),
            announcement_date=date(2026, 7, 25), total_shares=1000.0,
            circulating_shares=950.0, source_hash="new", data_source="miniqmt",
        ),
    ]
    resolved = resolve_capital(rows, as_of_date=date(2026, 8, 1))
    assert resolved is not None
    assert resolved.total_shares == 1000.0
    assert resolved.source_hash == "new"


def test_resolve_capital_excludes_future_rows() -> None:
    rows = [
        CapitalRow(
            stock_code="600000", report_date=date(2026, 6, 30),
            announcement_date=date(2026, 9, 1), total_shares=1000.0,
            circulating_shares=950.0, source_hash="future", data_source="miniqmt",
        ),
    ]
    assert resolve_capital(rows, as_of_date=date(2026, 8, 1)) is None


def test_resolve_capital_market_cap_uses_raw_close() -> None:
    resolved = ResolvedCapital(
        stock_code="600000", as_of_date=date(2026, 8, 17),
        report_date=date(2026, 6, 30), announcement_date=date(2026, 7, 25),
        total_shares=1000.0, circulating_shares=950.0,
        source_hash="h", data_source="miniqmt",
    )
    assert resolved.market_cap(10.5) == pytest.approx(10500.0)
    assert resolved.market_cap(None) is None
