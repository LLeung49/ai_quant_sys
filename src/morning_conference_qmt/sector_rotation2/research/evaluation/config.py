"""Configuration shared by all forward-label and evaluation jobs."""

from dataclasses import dataclass, field
from typing import Mapping


@dataclass(frozen=True)
class EvaluationConfig:
    horizons: Mapping[str, tuple[int, ...]] = field(default_factory=lambda: {
        "short_term": (1, 2, 3),
        "macd": (5, 10, 20),
        "sector_opportunity": (3, 5, 10),
        "etf_core": (5, 10, 20),
        "stock_trend": (5, 10, 20),
        "stock_repair": (10, 20, 40),
    })
    entry_mode: str = "next_open"
    train_days: int = 504
    validation_days: int = 126
    test_days: int = 126
    step_days: int = 126
    min_block_size: int = 10
    bootstrap_repetitions: int = 1000
    min_cross_section_pairs: int = 5
    min_group_samples: int = 20
    round_trip_cost_bps: tuple[float, ...] = (0.0, 5.0, 10.0, 20.0)


DEFAULT_EVALUATION_CONFIG = EvaluationConfig()

