from datetime import date, timedelta

from asset_allocation.etf_adaptive.contracts import DualPriceBar, ExecutionAvailability
from asset_allocation.etf_adaptive.research.validation_eligibility import validation_eligibility


def test_validation_eligibility_does_not_reject_confirmed_cross_border_etf() -> None:
    bars = tuple(DualPriceBar("513100.SH", date(2024, 1, 1) + timedelta(days=index), 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 20_000_000.0, False, 1.0, execution_availability=ExecutionAvailability(False, False, "test")) for index in range(252))
    result = validation_eligibility("513100.SH", bars)
    assert result[bars[-1].trade_date].eligible is True


def test_validation_eligibility_reports_actual_history_without_a_forced_floor() -> None:
    bars = tuple(
        DualPriceBar(
            "513100.SH", date(2024, 1, 1) + timedelta(days=index),
            1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
            20_000_000.0, False, 1.0,
            execution_availability=ExecutionAvailability(False, False, "test"),
        )
        for index in range(251)
    )

    result = validation_eligibility("513100.SH", bars)

    assert result[bars[-1].trade_date].history_session_count == 251
    assert "history_lt_252" in result[bars[-1].trade_date].rejection_reasons
