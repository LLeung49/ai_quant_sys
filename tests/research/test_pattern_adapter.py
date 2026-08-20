"""Tests for the pattern_detection adapter."""

from datetime import date, timedelta

import numpy as np
import pandas as pd
import pytest

from morning_conference.sector_rotation2.research.stock_alpha.pattern_adapter import (
    detect_bottom_divergence,
    has_technical_repair_evidence,
    scan_bullish_patterns,
)


def _uptrend_frame(n: int = 90, start: float = 10.0, step: float = 0.1) -> pd.DataFrame:
    """Build a monotonic up-trending OHLCV frame."""

    dates = [date(2025, 1, 1) + timedelta(days=i) for i in range(n)]
    close = [start + i * step for i in range(n)]
    return pd.DataFrame({
        "trade_date": dates,
        "open": [c - 0.05 for c in close],
        "high": [c + 0.10 for c in close],
        "low": [c - 0.10 for c in close],
        "close": close,
        "volume": [1_000_000 + i * 1000 for i in range(n)],
    })


def _down_then_recover_frame(n: int = 90) -> pd.DataFrame:
    """Build a down-trend followed by a sharp recovery (no real divergence)."""

    dates = [date(2025, 1, 1) + timedelta(days=i) for i in range(n)]
    closes: list[float] = []
    for i in range(n):
        if i < 50:
            closes.append(20.0 - 0.15 * i)
        else:
            closes.append(20.0 - 0.15 * 49 + (i - 49) * 0.30)
    return pd.DataFrame({
        "trade_date": dates,
        "open": [c - 0.10 for c in closes],
        "high": [c + 0.20 for c in closes],
        "low": [c - 0.20 for c in closes],
        "close": closes,
        "volume": [1_000_000] * n,
    })


def test_detect_bottom_divergence_returns_false_for_uptrend() -> None:
    frame = _uptrend_frame()
    result = detect_bottom_divergence(frame)
    assert result.has_divergence is False


def test_detect_bottom_divergence_handles_short_history() -> None:
    frame = _uptrend_frame(n=10)
    result = detect_bottom_divergence(frame, lookback=60)
    assert result.has_divergence is False


def test_detect_bottom_divergence_handles_none() -> None:
    assert detect_bottom_divergence(None).has_divergence is False


def test_scan_bullish_patterns_handles_short_history() -> None:
    frame = _uptrend_frame(n=3)
    assert scan_bullish_patterns(frame) == []


def test_scan_bullish_patterns_handles_none() -> None:
    assert scan_bullish_patterns(None) == []


def test_has_technical_repair_evidence_false_for_clean_uptrend() -> None:
    frame = _uptrend_frame()
    assert has_technical_repair_evidence(frame) is False


def test_has_technical_repair_evidence_returns_bool_type() -> None:
    frame = _uptrend_frame()
    result = has_technical_repair_evidence(frame)
    assert isinstance(result, bool)
