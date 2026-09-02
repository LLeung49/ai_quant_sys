"""Horizon-aware moving-block bootstrap that preserves date cross-sections."""

from collections.abc import Callable
from typing import Any

import numpy as np
import pandas as pd

from .config import EvaluationConfig


def effective_block_size(*, horizon: int, min_block_size: int) -> int:
    return max(horizon, min_block_size)


def moving_block_bootstrap_ci(frame: pd.DataFrame, value_fn: Callable[[pd.DataFrame], float | None], *, date_col: str,
                              horizon: int, config: EvaluationConfig, seed: int) -> tuple[float | None, float | None]:
    dates = tuple(sorted(frame[date_col].dropna().unique()))
    if not dates:
        return None, None
    block_size = effective_block_size(horizon=horizon, min_block_size=config.min_block_size)
    rng = np.random.default_rng(seed)
    results: list[float] = []
    for _ in range(config.bootstrap_repetitions):
        sampled_dates: list[Any] = []
        while len(sampled_dates) < len(dates):
            start = int(rng.integers(len(dates)))
            sampled_dates.extend(dates[(start + offset) % len(dates)] for offset in range(block_size))
        sampled = pd.concat([frame.loc[frame[date_col] == day] for day in sampled_dates[:len(dates)]], ignore_index=True)
        value = value_fn(sampled)
        if value is not None and np.isfinite(value):
            results.append(float(value))
    if not results:
        return None, None
    return float(np.quantile(results, 0.025)), float(np.quantile(results, 0.975))
