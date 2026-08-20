"""Tests for the valuation layer."""

from datetime import date

import pytest

from morning_conference.sector_rotation2.research.financial.capital import ResolvedCapital
from morning_conference.sector_rotation2.research.financial.ttm import TTMProjection
from morning_conference.sector_rotation2.research.financial.valuation import (
    _FINANCIAL_SECTORS,
    build_valuation,
)


def _ttm(**overrides) -> TTMProjection:
    base = dict(
        stock_code="600000",
        as_of_date=date(2026, 8, 17),
        period_end_date=date(2026, 6, 30),
        revenue=1000.0,
        net_profit=100.0,
        operating_cash_flow=120.0,
        n_quarters=4,
        quality_flags=(),
    )
    base.update(overrides)
    return TTMProjection(**base)


def _capital(**overrides) -> ResolvedCapital:
    base = dict(
        stock_code="600000",
        as_of_date=date(2026, 8, 17),
        report_date=date(2026, 6, 30),
        announcement_date=date(2026, 7, 25),
        total_shares=1000.0,
        circulating_shares=950.0,
        source_hash="h",
        data_source="miniqmt",
    )
    base.update(overrides)
    return ResolvedCapital(**base)


def test_build_valuation_standard_case() -> None:
    snap = build_valuation(
        ttm=_ttm(), capital=_capital(), raw_close=10.0,
        sector_name="\u4e2d\u8bc1\u91d1\u5c5e", total_equity=500.0,
    )
    assert snap.market_cap == pytest.approx(10000.0)
    assert snap.pe == pytest.approx(100.0)
    assert snap.ps == pytest.approx(10.0)
    assert snap.p_ocf == pytest.approx(10000.0 / 120.0)
    # PB = market_cap / total_equity = 10000 / 500 = 20.0
    assert snap.pb == pytest.approx(20.0)


def test_build_valuation_returns_null_pe_for_negative_profit() -> None:
    snap = build_valuation(
        ttm=_ttm(net_profit=-50.0), capital=_capital(), raw_close=10.0,
        sector_name="\u4e2d\u8bc1\u91d1\u5c5e", total_equity=500.0,
    )
    assert snap.pe is None


def test_build_valuation_returns_null_pb_for_financial_sector() -> None:
    snap = build_valuation(
        ttm=_ttm(), capital=_capital(), raw_close=10.0,
        sector_name="\u94f6\u884c", total_equity=500.0,
    )
    assert snap.pb is None
    assert "financial_sector_pb_disabled" in snap.quality_flags
    assert "\u94f6\u884c" in _FINANCIAL_SECTORS


def test_build_valuation_returns_null_market_cap_when_shares_missing() -> None:
    snap = build_valuation(
        ttm=_ttm(), capital=_capital(total_shares=None), raw_close=10.0,
        sector_name="\u4e2d\u8bc1\u91d1\u5c5e", total_equity=500.0,
    )
    assert snap.market_cap is None
    assert snap.pe is None
    assert "missing_market_cap" in snap.quality_flags


def test_build_valuation_ps_zero_revenue_returns_null() -> None:
    snap = build_valuation(
        ttm=_ttm(revenue=0.0), capital=_capital(), raw_close=10.0,
        sector_name="\u4e2d\u8bc1\u91d1\u5c5e", total_equity=500.0,
    )
    assert snap.ps is None


def test_build_valuation_propagates_ttm_quality_flags() -> None:
    snap = build_valuation(
        ttm=_ttm(quality_flags=("contains_restated",)),
        capital=_capital(), raw_close=10.0,
        sector_name="\u4e2d\u8bc1\u91d1\u5c5e", total_equity=500.0,
    )
    assert "ttm_contains_restated" in snap.quality_flags


def test_build_valuation_flags_pb_uninformative_when_equity_missing() -> None:
    snap = build_valuation(
        ttm=_ttm(), capital=_capital(), raw_close=10.0,
        sector_name="\u4e2d\u8bc1\u91d1\u5c5e", total_equity=None,
    )
    assert "pb_uninformative" in snap.quality_flags


def test_build_valuation_revenue_none_keeps_ps_none() -> None:
    snap = build_valuation(
        ttm=_ttm(revenue=None), capital=_capital(), raw_close=10.0,
        sector_name="\u4e2d\u8bc1\u91d1\u5c5e", total_equity=500.0,
    )
    assert snap.ps is None
    assert "ps_uninformative" in snap.quality_flags
