"""Tradability-only eligibility for the fixed validation manifest."""

from collections.abc import Sequence
from datetime import date

from ..contracts import DualPriceBar, ETFEligibility


ELIGIBILITY_HISTORY_SESSIONS = 252


def validation_eligibility(stock_code: str, bars: Sequence[DualPriceBar]) -> dict[date, ETFEligibility]:
    """Apply history, liquidity and tradability checks without geography filtering."""
    ordered = tuple(sorted(bars, key=lambda item: item.trade_date))
    result = {}
    for index, bar in enumerate(ordered):
        history = ordered[: index + 1]
        average = sum(item.amount for item in history[-20:]) / min(len(history), 20)
        reasons = []
        if len(history) < ELIGIBILITY_HISTORY_SESSIONS:
            reasons.append("history_lt_252")
        if average < 10_000_000:
            reasons.append("avg_amount_20_lt_10000000")
        if bar.suspended or (
            bar.execution_availability.provenance != "unavailable"
            and bar.execution_availability.buy_locked
        ):
            reasons.append("latest_bar_untradable")
        result[bar.trade_date] = ETFEligibility(
            not reasons, tuple(reasons), "fixed_validation", len(history), average,
        )
    return result
