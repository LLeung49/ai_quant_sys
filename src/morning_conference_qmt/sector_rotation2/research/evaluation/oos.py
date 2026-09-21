"""Purged rolling OOS partitions based strictly on market trading dates."""

from dataclasses import dataclass
from datetime import date
from typing import Iterable

from .config import EvaluationConfig


@dataclass(frozen=True)
class PurgedOosWindow:
    window_id: str
    train_start: date
    train_end: date
    validation_start: date
    validation_end: date
    test_start: date
    test_end: date
    train_signal_dates: tuple[date, ...]
    validation_signal_dates: tuple[date, ...]
    test_signal_dates: tuple[date, ...]


def signal_scope(window: PurgedOosWindow, signal_date: date) -> str | None:
    """Return the purged partition for a signal date, or None when excluded."""
    if signal_date in window.train_signal_dates:
        return "train"
    if signal_date in window.validation_signal_dates:
        return "validation"
    if signal_date in window.test_signal_dates:
        return "test"
    return None


def build_purged_oos_windows(trading_dates: Iterable[date], horizon: int, config: EvaluationConfig) -> tuple[PurgedOosWindow, ...]:
    dates = tuple(sorted(set(trading_dates)))
    partition_size = config.train_days + config.validation_days + config.test_days
    windows: list[PurgedOosWindow] = []
    start = 0
    while start + partition_size <= len(dates):
        train_start = start
        validation_start = train_start + config.train_days
        test_start = validation_start + config.validation_days
        end = test_start + config.test_days
        windows.append(PurgedOosWindow(
            window_id=f"oos_{len(windows):03d}",
            train_start=dates[train_start], train_end=dates[validation_start - 1],
            validation_start=dates[validation_start], validation_end=dates[test_start - 1],
            test_start=dates[test_start], test_end=dates[end - 1],
            train_signal_dates=dates[train_start:validation_start - horizon],
            validation_signal_dates=dates[validation_start:test_start - horizon],
            test_signal_dates=dates[test_start:end - horizon],
        ))
        start += config.step_days
    return tuple(windows)

