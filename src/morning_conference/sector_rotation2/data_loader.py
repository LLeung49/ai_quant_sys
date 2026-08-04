# Copied/adapted from sector_rotation/sector_loader.py.
# Differences: validates sector frames before benchmark construction and never
# imports the old package.
"""Read-only source loading and data-quality checks for sector_rotation2."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

import pandas as pd


@dataclass(frozen=True)
class FrameValidation:
    valid: bool
    reasons: tuple[str, ...]


def validate_sector_frame(frame: pd.DataFrame) -> FrameValidation:
    reasons: list[str] = []
    required = {"close", "amount"}
    missing = required.difference(frame.columns)
    if missing:
        reasons.append("missing_required_columns")
    if not isinstance(frame.index, pd.DatetimeIndex):
        reasons.append("invalid_trade_date_index")
    else:
        if frame.index.has_duplicates:
            reasons.append("duplicate_trade_date")
        if not frame.index.is_monotonic_increasing:
            reasons.append("unsorted_trade_date")
    if "close" in frame and (pd.to_numeric(frame["close"], errors="coerce") <= 0).any():
        reasons.append("nonpositive_close")
    if "amount" in frame and (pd.to_numeric(frame["amount"], errors="coerce") < 0).any():
        reasons.append("negative_amount")
    return FrameValidation(valid=not reasons, reasons=tuple(reasons))


def build_market_benchmark(sector_panel: Mapping[str, pd.DataFrame]) -> pd.DataFrame:
    """Build an equal-weight price / summed-amount benchmark from valid sectors."""
    eligible = {name: frame for name, frame in sector_panel.items() if validate_sector_frame(frame).valid}
    if not eligible:
        return pd.DataFrame(columns=["close", "amount", "eligible_sector_count"])
    normalized = [frame["close"] / frame["close"].iloc[0] for frame in eligible.values()]
    amounts = [frame["amount"] for frame in eligible.values()]
    return pd.DataFrame({
        "close": pd.concat(normalized, axis=1).mean(axis=1) * 1000.0,
        "amount": pd.concat(amounts, axis=1).sum(axis=1),
        "eligible_sector_count": len(eligible),
    })
