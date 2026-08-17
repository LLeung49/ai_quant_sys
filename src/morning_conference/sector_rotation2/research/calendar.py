"""Trading-day calendar backed by an authoritative upstream date sequence."""

from datetime import date
from typing import Iterable


class TradingCalendar:
    def __init__(self, trade_dates: Iterable[date]) -> None:
        self._trade_dates = tuple(sorted(set(trade_dates)))
        self._positions = {trade_date: index for index, trade_date in enumerate(self._trade_dates)}

    def __contains__(self, trade_date: object) -> bool:
        return trade_date in self._positions

    def shift(self, trade_date: date, offset: int) -> date:
        if trade_date not in self._positions:
            raise ValueError(f"{trade_date.isoformat()} is not a trading date")
        target = self._positions[trade_date] + offset
        if target < 0 or target >= len(self._trade_dates):
            raise IndexError("trading-date shift is outside calendar coverage")
        return self._trade_dates[target]
