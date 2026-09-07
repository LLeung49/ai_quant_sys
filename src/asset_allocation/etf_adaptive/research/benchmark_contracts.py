"""Immutable contracts for fixed-weight layered benchmark research.

This module deliberately contains validation and gate predicates only.  It
reuses the existing backtest engine and metrics modules; later orchestration
turns their cost-net out-of-sample output into these small, auditable records.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from datetime import date
import math

from ..contracts import AssetLayer, SubLayer, asset_layer_for


MAX_DRAWDOWN_TOLERANCE: float = 0.02
_OVERSEAS_SUB_LAYERS = frozenset(
    {SubLayer.OVERSEAS_MATURE, SubLayer.HONG_KONG_OFFSHORE}
)


def _require_text(value: str, field_name: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} must be a non-empty string")


def _require_finite(value: float, field_name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{field_name} must be a finite number")
    value = float(value)
    if not math.isfinite(value):
        raise ValueError(f"{field_name} must be a finite number")
    return value


@dataclass(frozen=True)
class WhitelistEntry:
    """One source-versioned primary/backup mapping for an approved exposure."""

    exposure_id: str
    sub_layer: SubLayer
    primary_code: str
    backup_code: str
    effective_from: date
    effective_to: date | None
    source_hash: str
    valuation_multiplier: float

    def __post_init__(self) -> None:
        _require_text(self.exposure_id, "exposure_id")
        if not isinstance(self.sub_layer, SubLayer):
            raise ValueError("sub_layer must be a SubLayer")
        _require_text(self.primary_code, "primary_code")
        _require_text(self.backup_code, "backup_code")
        if self.primary_code == self.backup_code:
            raise ValueError("primary_code and backup_code must differ")
        if not isinstance(self.effective_from, date):
            raise ValueError("effective_from must be a date")
        if self.effective_to is not None:
            if not isinstance(self.effective_to, date):
                raise ValueError("effective_to must be a date or None")
            if self.effective_to < self.effective_from:
                raise ValueError("effective_to must not precede effective_from")
        if (
            not isinstance(self.source_hash, str)
            or len(self.source_hash) != 64
            or any(character not in "0123456789abcdef" for character in self.source_hash.lower())
        ):
            raise ValueError("source_hash must be a SHA-256 hex digest")
        multiplier = _require_finite(
            self.valuation_multiplier, "valuation_multiplier"
        )
        if multiplier <= 0:
            raise ValueError("valuation_multiplier must be positive")
        if self.sub_layer in _OVERSEAS_SUB_LAYERS and multiplier != 1.0:
            raise ValueError(
                "valuation_multiplier must be 1.0 for overseas and Hong Kong exposures"
            )


@dataclass(frozen=True)
class StrategicPortfolio:
    """The approved static strategic weights for exactly one asset layer."""

    portfolio_id: str
    asset_layer: AssetLayer
    weights: Mapping[SubLayer, float]

    def __post_init__(self) -> None:
        _require_text(self.portfolio_id, "portfolio_id")
        if not isinstance(self.asset_layer, AssetLayer):
            raise ValueError("asset_layer must be an AssetLayer")
        if not isinstance(self.weights, Mapping) or not self.weights:
            raise ValueError("weights must be a non-empty mapping")
        total = 0.0
        for sub_layer, raw_weight in self.weights.items():
            if not isinstance(sub_layer, SubLayer):
                raise ValueError("weights keys must be SubLayer values")
            if asset_layer_for(sub_layer) is not self.asset_layer:
                raise ValueError("weights may only contain sub-layers in asset_layer")
            weight = _require_finite(raw_weight, "weights values")
            if weight <= 0:
                raise ValueError("weights values must be positive")
            total += weight
        if not math.isclose(total, 1.0, rel_tol=0.0, abs_tol=1e-9):
            raise ValueError("weights must sum to 1")


@dataclass(frozen=True)
class BenchmarkSeries:
    """Cost-net stitched OOS performance of one aligned execution stream."""

    series_id: str
    annualized_return: float
    max_drawdown: float

    def __post_init__(self) -> None:
        _require_text(self.series_id, "series_id")
        _require_finite(self.annualized_return, "annualized_return")
        drawdown = _require_finite(self.max_drawdown, "max_drawdown")
        if drawdown < -1.0 or drawdown > 0.0:
            raise ValueError("max_drawdown must be in [-1, 0]")


@dataclass(frozen=True)
class PortfolioGate:
    """The independently reported predicates required before a layer freezes."""

    passed: bool
    return_passed: bool
    drawdown_passed: bool
    majority_windows_passed: bool
    non_lagging_windows: int
    total_windows: int


def evaluate_portfolio_gate(
    strategy: BenchmarkSeries,
    benchmark: BenchmarkSeries,
    window_excess_returns: Sequence[float],
) -> PortfolioGate:
    """Evaluate the approved return, drawdown, and OOS-window gate.

    Drawdowns use the existing signed convention: zero is no drawdown and a
    more negative value is worse.  Therefore the strategy can be as low as
    ``benchmark.max_drawdown - 0.02`` and still pass.
    """

    if not isinstance(strategy, BenchmarkSeries):
        raise ValueError("strategy must be a BenchmarkSeries")
    if not isinstance(benchmark, BenchmarkSeries):
        raise ValueError("benchmark must be a BenchmarkSeries")
    if strategy.series_id == benchmark.series_id:
        raise ValueError("strategy and benchmark series_id must differ")
    if not isinstance(window_excess_returns, Sequence) or isinstance(
        window_excess_returns, (str, bytes)
    ):
        raise ValueError("window_excess_returns must be a sequence")
    if not window_excess_returns:
        raise ValueError("window_excess_returns must not be empty")
    excess = tuple(
        _require_finite(value, "window_excess_returns")
        for value in window_excess_returns
    )
    non_lagging = sum(value >= 0.0 for value in excess)
    return_passed = strategy.annualized_return > benchmark.annualized_return
    drawdown_passed = (
        strategy.max_drawdown >= benchmark.max_drawdown - MAX_DRAWDOWN_TOLERANCE
    )
    majority_windows_passed = non_lagging > len(excess) / 2
    return PortfolioGate(
        passed=return_passed and drawdown_passed and majority_windows_passed,
        return_passed=return_passed,
        drawdown_passed=drawdown_passed,
        majority_windows_passed=majority_windows_passed,
        non_lagging_windows=non_lagging,
        total_windows=len(excess),
    )
