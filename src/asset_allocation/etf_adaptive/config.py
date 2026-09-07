"""Frozen configuration for the adaptive ETF backtest."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from hashlib import sha256
import json
import math


def _finite_unit(value: float, name: str, *, allow_zero: bool = False) -> None:
    if not isinstance(value, (int, float)) or isinstance(value, bool) or not math.isfinite(value) or value < 0 or (not allow_zero and value == 0):
        raise ValueError(f"{name} must be a positive finite number")


@dataclass(frozen=True)
class GridConfig:
    step_pct: float = 0.02
    unit_pct: float = 0.10
    initial_model: str = "fixed"
    fixed_initial_pct: float | None = 0.50
    max_grid_per_day: int = 1
    atr_stop_multiple: float = 3.0
    cooldown_sessions: int = 5

    def __post_init__(self) -> None:
        _finite_unit(self.step_pct, "step_pct")
        _finite_unit(self.unit_pct, "unit_pct")
        if self.max_grid_per_day != 1:
            raise ValueError("max_grid_per_day must equal 1")
        _finite_unit(self.atr_stop_multiple, "atr_stop_multiple")
        if not isinstance(self.cooldown_sessions, int) or self.cooldown_sessions < 0:
            raise ValueError("cooldown_sessions must be a non-negative integer")


@dataclass(frozen=True)
class TrendConfig:
    stop_n: float = 2.0
    risk_per_unit: float = 0.005
    add_n: float = 0.5
    max_units: int = 4
    require_macd_bullish: bool = True
    amount_ratio_min: float | None = None

    def __post_init__(self) -> None:
        _finite_unit(self.stop_n, "stop_n")
        _finite_unit(self.risk_per_unit, "risk_per_unit")
        _finite_unit(self.add_n, "add_n")
        if not isinstance(self.max_units, int) or self.max_units < 1:
            raise ValueError("max_units must be a positive integer")


@dataclass(frozen=True)
class CostConfig:
    commission_rate: float = 0.0001
    minimum_commission: float = 5.0
    slippage_bps: float = 3.0
    sell_tax_rate: float = 0.0
    transfer_fee_rate: float = 0.0

    def __post_init__(self) -> None:
        _finite_unit(self.commission_rate, "commission_rate")
        _finite_unit(self.minimum_commission, "minimum_commission")
        _finite_unit(self.slippage_bps, "slippage_bps", allow_zero=True)
        _finite_unit(self.sell_tax_rate, "sell_tax_rate", allow_zero=True)
        _finite_unit(self.transfer_fee_rate, "transfer_fee_rate", allow_zero=True)


@dataclass(frozen=True)
class AdaptiveConfig:
    grid: GridConfig = GridConfig()
    trend: TrendConfig = TrendConfig()
    cost: CostConfig = CostConfig()

    @classmethod
    def default(cls) -> "AdaptiveConfig":
        return cls()

    def config_hash(self) -> str:
        payload = json.dumps(asdict(self), sort_keys=True, separators=(",", ":"))
        return sha256(payload.encode("utf-8")).hexdigest()
