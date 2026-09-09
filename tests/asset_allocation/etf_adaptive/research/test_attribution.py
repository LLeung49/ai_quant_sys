from datetime import date
from decimal import Decimal

from asset_allocation.etf_adaptive.research.attribution import build_result_attribution
from asset_allocation.etf_adaptive.state import BacktestEvent, BacktestRequest, BacktestResult, DailyNav


def test_attribution_uses_only_recorded_events_and_nav() -> None:
    result = BacktestResult(
        BacktestRequest("510300.SH", Decimal("100000"), date(2026, 9, 1), date(2026, 9, 2)),
        (
            BacktestEvent(date(2026, 9, 1), "fill", (("reason", "trend_entry"), ("shares", "1000"), ("raw_price", "4.0"))),
            BacktestEvent(date(2026, 9, 2), "rejected_order", (("reason", "buy_locked"),)),
        ),
        (
            DailyNav(date(2026, 9, 1), Decimal("96000"), Decimal("4000")),
            DailyNav(date(2026, 9, 2), Decimal("100000"), Decimal("0")),
        ),
    )

    attribution = build_result_attribution("wf_000", result)

    assert attribution.invested_sessions == 1
    assert attribution.cash_sessions == 1
    assert attribution.by_reason["trend_entry"].fill_count == 1
    assert attribution.rejected_order_count == 1
    assert attribution.trade_points[0].event_date == date(2026, 9, 1)
