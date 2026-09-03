"""ADX-driven GRID/TREND regime transition."""

from .state import Regime


def next_regime(previous: Regime | None, adx: float) -> Regime | None:
    if adx > 25:
        return Regime.TREND
    if adx < 20:
        return Regime.GRID
    return previous
