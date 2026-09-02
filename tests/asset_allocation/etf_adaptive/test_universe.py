from datetime import date, timedelta

import pytest

from asset_allocation.etf_adaptive.contracts import (
    DualPriceBar,
    ETFEligibility,
    ETFMetadata,
)
from asset_allocation.etf_adaptive.universe import classify_etf, evaluate_eligibility


AS_OF_DATE = date(2026, 9, 1)


def _metadata(
    stock_code: str = "510300.SH",
    fund_name: str = "沪深300ETF",
    **overrides: object,
) -> ETFMetadata:
    values: dict[str, object] = {
        "stock_code": stock_code,
        "fund_name": fund_name,
        "listing_date": date(2020, 1, 1),
    }
    values.update(overrides)
    return ETFMetadata(**values)  # type: ignore[arg-type]


def _bar(
    trade_date: date,
    amount: float = 12_000_000.0,
    *,
    suspended: bool = False,
    stock_code: str = "510300.SH",
) -> DualPriceBar:
    return DualPriceBar(
        stock_code=stock_code,
        trade_date=trade_date,
        signal_open=1.0,
        signal_high=1.1,
        signal_low=0.9,
        signal_close=1.0,
        raw_open=4.0,
        raw_high=4.4,
        raw_low=3.6,
        raw_close=4.0,
        amount=amount,
        suspended=suspended,
        adjustment_ratio=0.25,
    )


def _amount_bars(
    count: int,
    amount: float = 12_000_000.0,
    *,
    end_date: date = AS_OF_DATE,
    stock_code: str = "510300.SH",
) -> list[DualPriceBar]:
    start_date = end_date - timedelta(days=count - 1)
    return [
        _bar(
            start_date + timedelta(days=offset),
            amount,
            stock_code=stock_code,
        )
        for offset in range(count)
    ]


def test_classification_uses_index_code_then_deterministic_name_fallback() -> None:
    assert classify_etf(
        _metadata(fund_name="核心宽基ETF", tracking_index_code="000300.SH")
    ) == "core_broad"
    assert classify_etf(_metadata(fund_name="沪深300ETF")) == "core_broad"
    assert classify_etf(_metadata("159905.SZ", "红利低波ETF")) == "defensive"


@pytest.mark.parametrize(
    "metadata",
    [
        _metadata(fund_type="债券型ETF"),
        _metadata(tracking_index_name="纳斯达克100指数"),
        _metadata(is_cross_border=True),
        _metadata(is_leveraged=True),
        _metadata("513100.SH", "纳指ETF"),
        _metadata("511010.SH", "国债ETF"),
    ],
)
def test_metadata_and_name_exclusions_reject_non_domestic_equity_funds(
    metadata: ETFMetadata,
) -> None:
    assert classify_etf(metadata) is None


def test_metadata_exclusion_overrides_eligible_name_heuristic() -> None:
    metadata = _metadata(
        fund_name="沪深300ETF",
        fund_type="股票型ETF",
        tracking_index_name="标普500指数",
    )

    assert classify_etf(metadata) is None


@pytest.mark.parametrize(
    "metadata",
    [
        _metadata("600000.SH", "沪深300ETF"),
        _metadata("510999.SH", "科技行业ETF"),
        _metadata("510998.SH", "普通ETF"),
    ],
)
def test_code_prefix_is_only_an_exchange_fund_gate_and_fallback_fails_closed(
    metadata: ETFMetadata,
) -> None:
    assert classify_etf(metadata) is None


def test_shanghai_lof_prefix_is_not_accepted_as_an_etf() -> None:
    metadata = _metadata(
        "501050.SH",
        "沪深300ETF",
        tracking_index_code="000300.SH",
    )

    assert classify_etf(metadata) is None


@pytest.mark.parametrize("cross_border_token", ["港股", "香港"])
def test_hong_kong_name_and_index_fallbacks_are_excluded(
    cross_border_token: str,
) -> None:
    assert classify_etf(
        _metadata("159900.SZ", f"{cross_border_token}红利ETF")
    ) is None
    assert classify_etf(
        _metadata(
            "159901.SZ",
            "沪深300ETF",
            tracking_index_name=f"{cross_border_token}价值指数",
        )
    ) is None


def test_eligibility_uses_only_bars_available_on_as_of_date() -> None:
    bars = list(reversed(_amount_bars(253))) + [
        _bar(date(2026, 9, 2), amount=0.0, suspended=True)
    ]

    result = evaluate_eligibility(_metadata(), bars, AS_OF_DATE)

    assert result.eligible is True
    assert result.rejection_reasons == ()
    assert result.history_session_count == 253
    assert result.average_amount_20d == 12_000_000.0
    assert result.classification_provenance == "name_fallback"


def test_foreign_entity_bar_is_reported_and_never_counts_as_history() -> None:
    bars = _amount_bars(251)
    bars.append(
        _bar(
            AS_OF_DATE - timedelta(days=251),
            stock_code="159905.SZ",
        )
    )

    result = evaluate_eligibility(_metadata(), bars, AS_OF_DATE)

    assert result.eligible is False
    assert result.history_session_count == 251
    assert "bar_stock_code_mismatch" in result.rejection_reasons
    assert "listing_history_lt_252" in result.rejection_reasons


def test_duplicate_trade_date_is_reported_and_counts_as_one_session() -> None:
    bars = _amount_bars(251)
    bars.append(_bar(bars[0].trade_date, amount=50_000_000.0))

    result = evaluate_eligibility(_metadata(), bars, AS_OF_DATE)

    assert result.eligible is False
    assert result.history_session_count == 251
    assert result.average_amount_20d == 12_000_000.0
    assert "duplicate_trade_date" in result.rejection_reasons
    assert "listing_history_lt_252" in result.rejection_reasons


def test_structured_index_classification_records_metadata_provenance() -> None:
    metadata = _metadata(
        fund_name="核心宽基ETF",
        tracking_index_code="000300.SH",
    )

    result = evaluate_eligibility(metadata, _amount_bars(252), AS_OF_DATE)

    assert result.eligible is True
    assert result.classification_provenance == "metadata"


def test_liquidity_uses_trailing_twenty_observed_sessions_only() -> None:
    bars = _amount_bars(232, 1_000_000.0, end_date=date(2026, 8, 12))
    bars.extend(_amount_bars(20, 10_000_000.0))

    result = evaluate_eligibility(_metadata(), bars, AS_OF_DATE)

    assert result.eligible is True
    assert result.average_amount_20d == 10_000_000.0


@pytest.mark.parametrize(
    ("bars", "expected_reason"),
    [
        (_amount_bars(251), "listing_history_lt_252"),
        (_amount_bars(252, 9_999_999.0), "avg_amount_20_lt_10000000"),
        (
            _amount_bars(252, end_date=date(2026, 8, 31)),
            "latest_bar_untradable",
        ),
        (
            _amount_bars(251, end_date=date(2026, 8, 31))
            + [_bar(AS_OF_DATE, suspended=True)],
            "latest_bar_untradable",
        ),
    ],
)
def test_history_liquidity_and_latest_tradability_rejections_are_explicit(
    bars: list[DualPriceBar], expected_reason: str
) -> None:
    result = evaluate_eligibility(_metadata(), bars, AS_OF_DATE)

    assert result.eligible is False
    assert expected_reason in result.rejection_reasons


def test_unclassified_fund_is_rejected_without_using_provenance_as_a_reason() -> None:
    result = evaluate_eligibility(
        _metadata("510999.SH", "科技行业ETF"),
        _amount_bars(252, stock_code="510999.SH"),
        AS_OF_DATE,
    )

    assert result.eligible is False
    assert result.exposure_group is None
    assert result.rejection_reasons == ("not_domestic_equity_etf",)
    assert all("provenance" not in reason for reason in result.rejection_reasons)


def test_eligibility_provenance_is_additive_validated_and_backward_compatible() -> None:
    legacy = ETFEligibility(True, (), "core_broad", 252, 10_000_000.0)

    assert legacy.classification_provenance == "metadata"
    for invalid_provenance in ("guess", []):
        with pytest.raises(ValueError, match="classification_provenance"):
            ETFEligibility(
                True,
                (),
                "core_broad",
                252,
                10_000_000.0,
                classification_provenance=invalid_provenance,  # type: ignore[arg-type]
            )
