"""Tests for the quality layer."""

import pytest

from morning_conference.sector_rotation2.research.financial.quality import score_quality
from morning_conference.sector_rotation2.research.financial.ttm import TTMProjection

from datetime import date


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


def test_score_quality_basic_components() -> None:
    components = score_quality(
        _ttm(),
        net_profit_history=[80.0, 85.0, 90.0, 100.0],
        total_equity=500.0,
        total_assets=1500.0,
        total_liabilities=900.0,
    )
    assert components.margin_stability == pytest.approx(0.1)  # 100 / 1000
    assert components.roe == pytest.approx(0.2)  # 100 / 500
    assert components.debt_safety == pytest.approx(0.4)  # (1500 - 900) / 1500
    assert components.earnings_momentum == pytest.approx(0.25)  # 100/80 - 1


def test_score_quality_flags_missing_assets() -> None:
    components = score_quality(
        _ttm(),
        net_profit_history=None,
        total_equity=None,
        total_assets=100.0,
        total_liabilities=None,
    )
    flags = set(components.quality_flags)
    assert "missing_roe" in flags
    assert "missing_debt_safety" in flags
    assert "missing_total_liabilities" in flags
    assert "missing_earnings_momentum" in flags
    assert "missing_margin" not in flags  # margin is computable from TTM


def test_score_quality_flags_negative_roe() -> None:
    components = score_quality(
        _ttm(net_profit=-50.0),
        net_profit_history=None,
        total_equity=500.0,
        total_assets=1000.0,
        total_liabilities=400.0,
    )
    assert "negative_roe" in components.quality_flags
    assert components.roe == pytest.approx(-0.1)


def test_score_quality_handles_zero_or_negative_yoy_base() -> None:
    components = score_quality(
        _ttm(net_profit=120.0),
        net_profit_history=[10.0, 20.0, 30.0, 120.0],  # most recent year-ago = 10
        total_equity=500.0,
        total_assets=1000.0,
        total_liabilities=400.0,
    )
    # 120 / 10 - 1 = 11.0
    assert components.earnings_momentum == pytest.approx(11.0)


def test_score_quality_returns_none_for_yoy_with_zero_base() -> None:
    components = score_quality(
        _ttm(),
        net_profit_history=[0.0, 10.0, 20.0, 30.0],
        total_equity=500.0,
    )
    assert "non_positive_yoy_base" in components.quality_flags
    assert components.earnings_momentum is None


def test_score_quality_debt_safety_floored_at_zero() -> None:
    components = score_quality(
        _ttm(),
        net_profit_history=None,
        total_equity=None,
        total_assets=100.0,
        total_liabilities=200.0,  # liabilities > assets => negative equity
    )
    assert components.debt_safety == 0.0
