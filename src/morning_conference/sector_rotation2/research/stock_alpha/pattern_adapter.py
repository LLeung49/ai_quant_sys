"""Adapter over the existing ``pattern_detection`` module.

The Repair pipeline needs a small, deterministic interface to the MACD
bottom-divergence + bullish-candlestick scan implemented in
``src/pattern_detection/9-*.py``.  This module is a thin shim that:

- Accepts a stock OHLCV frame (the same shape the underlying scanner
  consumes).
- Exposes ``detect_bottom_divergence`` and ``scan_bullish_patterns`` as
  pure-Python helpers, free of side effects, no DB access.

The scanner itself remains the source of truth; the adapter only
exposes the two entry points and adds normalization for the Repair
service to consume.  If the pattern_detection module ever changes
formula, the adapter is the only file that needs to follow.
"""

from __future__ import annotations

import importlib.util
import os
from collections.abc import Iterable
from dataclasses import dataclass
from typing import Optional

import numpy as np
import pandas as pd


@dataclass(frozen=True)
class BottomDivergenceResult:
    """Result of ``detect_bottom_divergence`` on one stock's OHLCV frame."""

    has_divergence: bool
    recent_price: Optional[float] = None
    recent_macd: Optional[float] = None
    prev_price: Optional[float] = None
    prev_macd: Optional[float] = None


def _import_pattern_radar():
    """Import the ``9-*.py`` scanner by file path to avoid package __init__ side effects.

    The pattern_detection package has an empty ``__init__.py``; the actual
    scanner module lives at ``src/pattern_detection/9-形态选股雷达.py``.
    """

    module_path = os.path.join(
        "src", "pattern_detection", "9-\u5f62\u6001\u9009\u80a1\u96f7\u8fbe.py"
    )
    if not os.path.exists(module_path):
        raise ImportError(f"pattern_detection scanner not found at {module_path!r}")
    spec = importlib.util.spec_from_file_location("pattern_radar", module_path)
    if spec is None or spec.loader is None:
        raise ImportError("could not load pattern_radar spec")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def detect_bottom_divergence(
    frame: pd.DataFrame,
    *,
    lookback: int = 60,
    recent_window: int = 10,
    min_macd_diff: float = 0.05,
    require_macd_below_zero: bool = True,
) -> BottomDivergenceResult:
    """Run the pattern_detection bottom-divergence scan on ``frame``."""

    if frame is None or len(frame) < lookback:
        return BottomDivergenceResult(has_divergence=False)

    pattern_radar = _import_pattern_radar()
    close = pd.to_numeric(frame["close"], errors="coerce").to_numpy(dtype=np.float64)

    # Recompute the MACD line the same way the scanner does so we can
    # pass it through unchanged.
    fast = pd.Series(close).ewm(span=12, adjust=False, min_periods=12).mean().to_numpy()
    slow = pd.Series(close).ewm(span=26, adjust=False, min_periods=26).mean().to_numpy()
    macd_line = fast - slow

    has_div, info = pattern_radar.detect_bottom_divergence(
        close=close,
        macd_line=macd_line,
        lookback=lookback,
        recent_window=recent_window,
        min_macd_diff=min_macd_diff,
        require_macd_below_zero=require_macd_below_zero,
        require_prev_downtrend=True,
        min_prev_decline_pct=0.05,
    )
    return BottomDivergenceResult(
        has_divergence=has_div,
        recent_price=info.get("recent_price"),
        recent_macd=info.get("recent_macd"),
        prev_price=info.get("prev_price"),
        prev_macd=info.get("prev_macd"),
    )


@dataclass(frozen=True)
class BullishPatternHit:
    """One bullish pattern hit on the latest bar."""

    chinese_name: str
    function_name: str
    signal_strength: int


def scan_bullish_patterns(
    frame: pd.DataFrame,
    *,
    min_signal: int = 100,
) -> list[BullishPatternHit]:
    """Run the pattern_detection bullish pattern scan on the latest bar."""

    if frame is None or len(frame) < 5:
        return []
    pattern_radar = _import_pattern_radar()
    o = pd.to_numeric(frame["open"], errors="coerce").to_numpy(dtype=np.float64)
    h = pd.to_numeric(frame["high"], errors="coerce").to_numpy(dtype=np.float64)
    l = pd.to_numeric(frame["low"], errors="coerce").to_numpy(dtype=np.float64)
    c = pd.to_numeric(frame["close"], errors="coerce").to_numpy(dtype=np.float64)
    found = pattern_radar.scan_bullish_patterns(o, h, l, c, min_signal=min_signal)
    return [
        BullishPatternHit(
            chinese_name=chinese,
            function_name=function_name,
            signal_strength=int(signal),
        )
        for chinese, function_name, signal in found
    ]


def has_technical_repair_evidence(
    frame: pd.DataFrame,
    *,
    divergence_lookback: int = 60,
    pattern_min_signal: int = 100,
) -> bool:
    """Return True if either bottom-divergence or bullish patterns fire."""

    div = detect_bottom_divergence(frame, lookback=divergence_lookback)
    if div.has_divergence:
        return True
    return bool(scan_bullish_patterns(frame, min_signal=pattern_min_signal))


__all__ = [
    "BottomDivergenceResult",
    "BullishPatternHit",
    "detect_bottom_divergence",
    "scan_bullish_patterns",
    "has_technical_repair_evidence",
]
