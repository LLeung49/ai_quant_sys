"""Normalize candidate snapshots into provenance-complete evaluation frames."""

from typing import Mapping

import pandas as pd

from ..contracts import SignalFrameSpec
from .calendar import TradingCalendar


class ShortTermSignalAdapter:
    spec = SignalFrameSpec(
        signal_family="short_term", score_col="signal_score", cross_section_cols=("signal_date", "sector_level"),
        event_id_col="signal_event_id", supports_rank_metrics=True,
    )

    def normalize(self, frame: pd.DataFrame) -> pd.DataFrame:
        return _base_frame(frame, self.spec, default_entity_type="sector")


class MacdSignalAdapter:
    spec = SignalFrameSpec(
        signal_family="macd", score_col=None, cross_section_cols=(), event_id_col="signal_event_id",
        supports_rank_metrics=False,
    )

    def __init__(self, calendar: TradingCalendar) -> None:
        self._calendar = calendar

    def normalize(self, frame: pd.DataFrame) -> pd.DataFrame:
        normalized = _base_frame(frame, self.spec, default_entity_type="etf")
        offsets = pd.to_numeric(frame.get("gc_offset", 0), errors="raise").astype(int)
        normalized["event_date"] = [
            self._calendar.shift(signal_date, -offset)
            for signal_date, offset in zip(normalized["signal_date"], offsets, strict=True)
        ]
        normalized["signal_event_id"] = [
            f"macd:{code}:{event_date.isoformat()}"
            for code, event_date in zip(normalized["entity_code"], normalized["event_date"], strict=True)
        ]
        normalized["condition_key"] = "macd_metrics_available"
        normalized["gc_offset"] = offsets
        return normalized


def _base_frame(frame: pd.DataFrame, spec: SignalFrameSpec, *, default_entity_type: str) -> pd.DataFrame:
    required = {"signal_date", "entity_code", "upstream_model_version", "upstream_config_hash", "upstream_run_id"}
    missing = sorted(required.difference(frame.columns))
    if missing:
        raise ValueError(f"signal frame missing columns: {', '.join(missing)}")
    normalized = pd.DataFrame({
        "signal_family": spec.signal_family,
        "signal_date": pd.to_datetime(frame["signal_date"]).dt.date,
        "entity_type": frame["entity_type"] if "entity_type" in frame else default_entity_type,
        "entity_code": frame["entity_code"].astype(str),
        "sector_level": frame["sector_level"] if "sector_level" in frame else None,
        "signal_score": pd.to_numeric(frame["signal_score"], errors="coerce") if "signal_score" in frame else None,
        "upstream_model_version": frame["upstream_model_version"].astype(str),
        "upstream_config_hash": frame["upstream_config_hash"].astype(str),
        "upstream_run_id": frame["upstream_run_id"].astype(str),
    })
    normalized["event_date"] = normalized["signal_date"]
    normalized["signal_event_id"] = [
        f"{spec.signal_family}:{code}:{signal_date.isoformat()}"
        for code, signal_date in zip(normalized["entity_code"], normalized["signal_date"], strict=True)
    ]
    normalized["condition_key"] = "all"
    return normalized

