"""Deterministic configuration for the SHADOW Trend Alpha stock-candidate model."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Mapping


@dataclass(frozen=True)
class TrendAlphaConfig:
    """All result-affecting parameters for stock-level Trend Alpha V1."""

    model_version: str = "stock_trend_v2"
    min_listing_age: int = 120
    min_price_history: int = 60
    windows: tuple = (5, 10, 20)
    alpha_weights: tuple = (0.50, 0.30, 0.20)
    min_alpha_weight: float = 0.60
    trend_quality_weights: tuple = (0.50, 0.50)
    structure_weights: Mapping = field(
        default_factory=lambda: {
            "ma_stack": 0.35,
            "breakout20": 0.25,
            "breakout60": 0.20,
            "strong_pullback": 0.20,
        },
    )
    score_weights: Mapping = field(
        default_factory=lambda: {
            "alpha_strength": 0.35,
            "persistence": 0.20,
            "trend_quality": 0.20,
            "structure": 0.10,
            "liquidity": 0.10,
            "hot_leader_bonus": 0.05,
        },
    )
    risk_penalty_threshold: float = 0.40
    hot_leader_cap: float = 0.05
    hot_leader_streak: int = 2
    min_score_for_leader: float = 0.30
    persistence_lookback: int = 10
    persistence_top_threshold: float = 0.70
    persistence_min_dates: int = 6
    liquidity_window: int = 20
    extension_start: float = 0.20
    extension_max: float = 1.00
    extension_max_penalty: float = 0.40

    def __post_init__(self) -> None:
        if len(self.windows) != len(self.alpha_weights):
            raise ValueError("windows and alpha_weights must have the same length")
        if abs(sum(self.alpha_weights) - 1.0) > 1e-9:
            raise ValueError("alpha_weights must sum to 1.0")
        if abs(sum(self.trend_quality_weights) - 1.0) > 1e-9:
            raise ValueError("trend_quality_weights must sum to 1.0")
        if abs(sum(self.structure_weights.values()) - 1.0) > 1e-9:
            raise ValueError("structure_weights must sum to 1.0")
        if abs(sum(self.score_weights.values()) - 1.0) > 1e-9:
            raise ValueError("score_weights must sum to 1.0")
        if not (0.0 < self.min_alpha_weight <= 1.0):
            raise ValueError("min_alpha_weight must be in (0, 1]")
        if self.risk_penalty_threshold < 0 or self.risk_penalty_threshold > 1:
            raise ValueError("risk_penalty_threshold must be in [0, 1]")
        if self.hot_leader_cap < 0 or self.hot_leader_cap > 1:
            raise ValueError("hot_leader_cap must be in [0, 1]")
        if self.min_listing_age <= 0 or self.min_price_history <= 0:
            raise ValueError("min_listing_age and min_price_history must be positive")
        if self.persistence_lookback <= 0 or self.persistence_min_dates <= 0:
            raise ValueError("persistence lookback and min_dates must be positive")
        if self.extension_start >= self.extension_max:
            raise ValueError("extension_start must be < extension_max")

