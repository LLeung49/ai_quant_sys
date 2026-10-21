"""Tests for normalize + TTM + capital layers."""

from datetime import date

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


def _ytd_anchor_chain() -> list[FinancialRawRow]:
    """Three PIT-visible YTD anchors for 2026 Q2."""
    return [
        _raw_row(report_date=date(2025, 6, 30), announcement_date=date(2025, 8, 1),
                 source_hash="h0", revenue=100.0, net_profit=10.0,
                 operating_cash_flow=12.0),
        _raw_row(report_date=date(2025, 12, 31), announcement_date=date(2026, 4, 1),
                 source_hash="h1", revenue=400.0, net_profit=40.0,
                 operating_cash_flow=48.0),
        _raw_row(report_date=date(2026, 6, 30), announcement_date=date(2026, 7, 25),
                 source_hash="h2", revenue=250.0, net_profit=25.0,
                 operating_cash_flow=30.0),
    ]


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


def test_build_ttm_differences_ytd_anchors() -> None:
    ttm = build_ttm(_ytd_anchor_chain(), as_of_date=date(2026, 8, 1))
    assert ttm is not None
    assert ttm.revenue == pytest.approx(550.0)
    assert ttm.net_profit == pytest.approx(55.0)
    assert ttm.operating_cash_flow == pytest.approx(66.0)
    assert ttm.is_complete is True


def test_build_ttm_converts_year_to_date_statements_without_double_counting():
    rows = [
        _raw_row(report_date=date(2025, 6, 30), announcement_date=date(2025, 8, 1),
                 source_hash="prior_q2", revenue=50.0, net_profit=5.0,
                 operating_cash_flow=6.0),
        _raw_row(report_date=date(2025, 12, 31), announcement_date=date(2026, 4, 1),
                 source_hash="prior_fy", revenue=120.0, net_profit=12.0,
                 operating_cash_flow=15.0),
        _raw_row(report_date=date(2026, 6, 30), announcement_date=date(2026, 8, 1),
                 source_hash="current_q2", revenue=70.0, net_profit=7.0,
                 operating_cash_flow=8.0),
    ]
    ttm = build_ttm(rows, as_of_date=date(2026, 8, 2))
    assert ttm is not None
    assert ttm.revenue == pytest.approx(140.0)
    assert ttm.net_profit == pytest.approx(14.0)
    assert ttm.operating_cash_flow == pytest.approx(17.0)


def test_build_ttm_matches_2026_maotai_statement_ytd_contract():
    # Captured PIT statement amounts: 2026H1 + 2025FY - 2025H1.
    rows = [
        _raw_row(stock_code="600519.SH", report_date=date(2025, 6, 30), announcement_date=date(2025, 8, 13),
                 source_hash="2025h1", revenue=91_093_762_553.97,
                 net_profit=46_986_681_449.24),
        _raw_row(stock_code="600519.SH", report_date=date(2025, 12, 31), announcement_date=date(2026, 4, 17),
                 source_hash="2025fy", revenue=172_054_171_890.91,
                 net_profit=85_310_324_833.67),
        _raw_row(stock_code="600519.SH", report_date=date(2026, 6, 30), announcement_date=date(2026, 8, 15),
                 source_hash="2026h1", revenue=92_278_072_083.21,
                 net_profit=46_033_330_566.78),
    ]
    ttm = build_ttm(rows, as_of_date=date(2026, 10, 19))
    assert ttm is not None
    assert ttm.revenue == pytest.approx(173_238_481_420.15)
    assert ttm.net_profit == pytest.approx(84_356_973_951.21)


def test_build_ttm_annual_statement_is_one_full_year():
    annual = _raw_row(report_date=date(2025, 12, 31),
                      announcement_date=date(2026, 4, 1),
                      revenue=120.0, net_profit=12.0)
    ttm = build_ttm([annual], as_of_date=date(2026, 4, 2))
    assert ttm is not None
    assert ttm.revenue == pytest.approx(120.0)


def test_build_ttm_requires_prior_year_anchor_visible_at_as_of_date():
    rows = [
        _raw_row(report_date=date(2025, 6, 30), announcement_date=date(2025, 8, 1),
                 source_hash="prior_q2"),
        _raw_row(report_date=date(2025, 12, 31), announcement_date=date(2026, 9, 1),
                 source_hash="late_fy"),
        _raw_row(report_date=date(2026, 6, 30), announcement_date=date(2026, 8, 1),
                 source_hash="current_q2"),
    ]
    assert build_ttm(rows, as_of_date=date(2026, 8, 2)) is None


def test_build_ttm_explicit_estimated_opt_in() -> None:
    chain = _ytd_anchor_chain()
    chain[0] = _raw_row(
        report_date=chain[0].report_date,
        announcement_date=None,
        first_seen_at=chain[0].announcement_date,
        source_hash="estimated",
        source_verified=False,
    )
    assert build_ttm(chain, as_of_date=date(2026, 8, 1)) is None
    assert build_ttm(chain, as_of_date=date(2026, 8, 1), allow_estimated_pit=True) is not None


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

    chain = _ytd_anchor_chain()
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
    assert ttm.net_profit == pytest.approx(25.0)
    assert "partial_revenue" in ttm.quality_flags


def test_build_ttm_flags_restated_components() -> None:
    chain = _ytd_anchor_chain()
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


def test_resolve_capital_waits_for_announced_share_change_to_take_effect() -> None:
    rows = [
        CapitalRow(
            stock_code="600000", report_date=date(2026, 1, 1),
            announcement_date=date(2025, 12, 20), total_shares=900.0,
            circulating_shares=850.0, source_hash="old", data_source="qmt",
        ),
        CapitalRow(
            stock_code="600000", report_date=date(2026, 10, 25),
            announcement_date=date(2026, 10, 10), total_shares=1000.0,
            circulating_shares=950.0, source_hash="new", data_source="qmt",
        ),
    ]
    before = resolve_capital(rows, as_of_date=date(2026, 10, 20))
    after = resolve_capital(rows, as_of_date=date(2026, 10, 26))
    assert before is not None and before.source_hash == "old"
    assert after is not None and after.source_hash == "new"


def test_resolve_capital_prefers_latest_effective_date_over_late_correction() -> None:
    rows = [
        CapitalRow(
            stock_code="600000", report_date=date(2026, 1, 1),
            announcement_date=date(2026, 10, 1), total_shares=900.0,
            circulating_shares=850.0, source_hash="corrected_old", data_source="qmt",
        ),
        CapitalRow(
            stock_code="600000", report_date=date(2026, 6, 1),
            announcement_date=date(2026, 7, 1), total_shares=1000.0,
            circulating_shares=950.0, source_hash="current", data_source="qmt",
        ),
    ]
    selected = resolve_capital(rows, as_of_date=date(2026, 10, 20))
    assert selected is not None and selected.source_hash == "current"


def test_capital_prefers_qmt_for_same_effective_date_but_newer_akshare_change_wins() -> None:
    rows = [
        CapitalRow("600000.SH", date(2026, 6, 1), date(2026, 6, 2),
                   1000., 900., "qmt", "qmt"),
        CapitalRow("600000.SH", date(2026, 6, 1), date(2026, 6, 3),
                   1001., 901., "ak_same", "akshare"),
        CapitalRow("600000.SH", date(2026, 7, 1), date(2026, 7, 2),
                   1100., 990., "ak_new", "akshare"),
    ]
    assert resolve_capital(rows, as_of_date=date(2026, 6, 30)).source_hash == "qmt"
    assert resolve_capital(rows, as_of_date=date(2026, 7, 3)).source_hash == "ak_new"


def test_resolve_capital_market_cap_uses_raw_close() -> None:
    resolved = ResolvedCapital(
        stock_code="600000", as_of_date=date(2026, 8, 17),
        report_date=date(2026, 6, 30), announcement_date=date(2026, 7, 25),
        total_shares=1000.0, circulating_shares=950.0,
        source_hash="h", data_source="miniqmt",
    )
    assert resolved.market_cap(10.5) == pytest.approx(10500.0)
    assert resolved.market_cap(None) is None
    assert resolved.market_cap(0.0) is None
    assert resolved.market_cap(float("nan")) is None
