from datetime import date
from decimal import Decimal

import pytest

from asset_allocation.etf_adaptive.contracts import (
    CorporateAction,
    CorporateActionType,
    DataQualityError,
    DataQualityIssue,
    DualPriceBar,
    ETFEligibility,
    ETFMetadata,
)


def test_dual_price_bar_rejects_non_positive_prices() -> None:
    with pytest.raises(ValueError, match="prices must be positive"):
        DualPriceBar(
            stock_code="510300.SH", trade_date=date(2026, 9, 1),
            signal_open=0.0, signal_high=1.0, signal_low=0.9, signal_close=1.0,
            raw_open=4.0, raw_high=4.1, raw_low=3.9, raw_close=4.0,
            amount=20_000_000.0, suspended=False, adjustment_ratio=0.25,
        )


@pytest.mark.parametrize(
    ("amount", "suspended", "adjustment_ratio"),
    [
        (-1.0, False, 0.25),
        (20_000_000.0, False, 0.0),
        (20_000_000.0, "false", 0.25),
    ],
)
def test_dual_price_bar_rejects_invalid_non_price_fields(
    amount: float, suspended: bool, adjustment_ratio: float
) -> None:
    with pytest.raises(ValueError):
        DualPriceBar(
            stock_code="510300.SH", trade_date=date(2026, 9, 1),
            signal_open=1.0, signal_high=1.1, signal_low=0.9, signal_close=1.0,
            raw_open=4.0, raw_high=4.1, raw_low=3.9, raw_close=4.0,
            amount=amount, suspended=suspended, adjustment_ratio=adjustment_ratio,
        )


@pytest.mark.parametrize(
    ("history_session_count", "average_amount_20d"),
    [
        (251, 10_000_000.0),
        (252, None),
        (252, 9_999_999.0),
    ],
)
def test_etf_eligibility_rejects_eligible_decisions_below_required_thresholds(
    history_session_count: int, average_amount_20d: float | None
) -> None:
    with pytest.raises(ValueError):
        ETFEligibility(
            eligible=True,
            rejection_reasons=(),
            exposure_group=None,
            history_session_count=history_session_count,
            average_amount_20d=average_amount_20d,
        )


def test_etf_eligibility_preserves_valid_rejected_decision() -> None:
    decision = ETFEligibility(
        eligible=False,
        rejection_reasons=("insufficient history",),
        exposure_group=None,
        history_session_count=10,
        average_amount_20d=None,
    )

    assert decision.eligible is False


def test_etf_eligibility_requires_exposure_group_when_eligible() -> None:
    with pytest.raises(ValueError, match="eligible decisions require an exposure_group"):
        ETFEligibility(
            eligible=True,
            rejection_reasons=(),
            exposure_group=None,
            history_session_count=252,
            average_amount_20d=10_000_000.0,
        )


@pytest.mark.parametrize(
    "factory",
    [
        lambda: ETFEligibility(True, (), None, 252.5, 10_000_000.0),
        lambda: ETFEligibility(1, (), None, 252, 10_000_000.0),
        lambda: ETFMetadata("510300.SH", "CSI 300 ETF", "2020-01-01"),
        lambda: ETFMetadata("510300.SH", "CSI 300 ETF", date(2020, 1, 1), is_cross_border=0),
        lambda: ETFMetadata("510300.SH", "CSI 300 ETF", date(2020, 1, 1), is_domestic_equity=0),
        lambda: CorporateAction(
            "510300.SH", "2026-09-01", CorporateActionType.CASH_DIVIDEND,
            Decimal("0.1"), Decimal("1"),
        ),
        lambda: DataQualityIssue("missing_bar", "510300.SH", "2026-09-01", "bar missing"),
    ],
)
def test_contracts_reject_malformed_primitive_boundary_fields(factory: object) -> None:
    with pytest.raises(ValueError):
        factory()  # type: ignore[operator]


def test_metadata_corporate_action_and_data_quality_contracts_preserve_valid_values() -> None:
    metadata = ETFMetadata(
        stock_code="510300.SH",
        fund_name="CSI 300 ETF",
        listing_date=date(2020, 1, 1),
    )
    action = CorporateAction(
        stock_code="510300.SH",
        effective_date=date(2026, 9, 1),
        action_type=CorporateActionType.CASH_DIVIDEND,
        cash_per_share=Decimal("0.1"),
        share_multiplier=Decimal("1"),
    )
    issue = DataQualityIssue(
        code="missing_bar",
        stock_code="510300.SH",
        trade_date=date(2026, 9, 1),
        message="bar missing",
    )

    error = DataQualityError("data quality failed", (issue,))

    assert metadata.listing_date == date(2020, 1, 1)
    assert action.cash_per_share == Decimal("0.1")
    assert error.issues == (issue,)


def test_corporate_action_event_ids_are_stable_and_distinguish_types() -> None:
    cash = CorporateAction("510300.SH", date(2026, 9, 1), CorporateActionType.CASH_DIVIDEND, Decimal("0.10"), Decimal("1"))
    split = CorporateAction("510300.SH", date(2026, 9, 1), CorporateActionType.SHARE_SPLIT, None, Decimal("1.10"))
    assert cash.event_id == "510300.SH:2026-09-01:cash_dividend"
    assert split.event_id == "510300.SH:2026-09-01:share_split"
    assert cash.event_id != split.event_id
