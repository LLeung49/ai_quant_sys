# Copied/adapted from sector_rotation/sector_loader.py.
# Differences: validates sector frames before benchmark construction and never
# imports the old package.
"""Read-only source loading and data-quality checks for sector_rotation2."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

import pandas as pd

from data_ingestion.db_config import execute_query


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


def load_sector_panel(
    level: int,
    start_date: str | None = None,
    end_date: str | None = None,
    min_history_days: int = 60,
) -> dict[str, pd.DataFrame]:
    """Load a read-only sector history panel from ``trade_sector_daily``."""
    conditions = ["sector_level = %s"]
    params: list[object] = [level]
    if start_date:
        conditions.append("trade_date >= %s")
        params.append(start_date)
    if end_date:
        conditions.append("trade_date <= %s")
        params.append(end_date)
    sql = f"""
        SELECT sector_name, trade_date, close_idx AS close, total_amount AS amount,
               stock_count, kline_stock_count, rise_count, fall_count, flat_count,
               limit_up, limit_down
        FROM trade_sector_daily
        WHERE {' AND '.join(conditions)}
        ORDER BY sector_name ASC, trade_date ASC
    """
    rows = execute_query(sql, params)
    if not rows:
        return {}
    frame = pd.DataFrame(rows)
    frame["trade_date"] = pd.to_datetime(frame["trade_date"])
    panel: dict[str, pd.DataFrame] = {}
    for sector_name, group in frame.groupby("sector_name", sort=True):
        sector_frame = group.drop(columns="sector_name").set_index("trade_date").sort_index()
        if len(sector_frame) >= min_history_days and validate_sector_frame(sector_frame).valid:
            panel[str(sector_name)] = sector_frame
    return panel
