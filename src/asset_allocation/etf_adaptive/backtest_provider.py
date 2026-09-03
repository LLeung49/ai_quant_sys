"""Provider boundary for complete point-in-time adaptive ETF backtests."""

from __future__ import annotations

from datetime import date
from typing import Mapping, Protocol

from .contracts import CorporateAction, DualPriceBar, ETFEligibility


class AdaptiveBacktestDataProvider(Protocol):
    """Load every external input needed by one bounded backtest run."""

    def load_bars(
        self, stock_code: str, start_date: date, end_date: date,
    ) -> tuple[DualPriceBar, ...]: ...

    def load_actions(
        self, stock_code: str, start_date: date, end_date: date,
    ) -> tuple[CorporateAction, ...]: ...

    def load_eligibility(
        self, stock_code: str, bars: tuple[DualPriceBar, ...],
    ) -> Mapping[date, ETFEligibility]: ...
