import pytest

from asset_allocation.etf_adaptive.regime import next_regime
from asset_allocation.etf_adaptive.state import Regime


@pytest.mark.parametrize(
    ("previous", "adx", "expected"),
    [
        (None, 22.0, None), (None, 19.0, Regime.GRID),
        (None, 26.0, Regime.TREND), (Regime.GRID, 23.0, Regime.GRID),
        (Regime.TREND, 23.0, Regime.TREND),
    ],
)
def test_adx_hysteresis(previous, adx, expected) -> None:
    assert next_regime(previous, adx) == expected
