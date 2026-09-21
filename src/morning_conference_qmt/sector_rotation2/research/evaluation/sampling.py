"""Sampling modes that keep MACD snapshots visible but avoid event inflation."""

import pandas as pd


def sample_signal_frame(frame: pd.DataFrame, mode: str) -> pd.DataFrame:
    if mode == "snapshot":
        return frame.copy()
    if mode != "event":
        raise ValueError("sampling mode must be 'snapshot' or 'event'")
    required = {"signal_event_id", "gc_offset", "signal_date"}
    missing = sorted(required.difference(frame.columns))
    if missing:
        raise ValueError(f"event sampling missing columns: {', '.join(missing)}")
    return (
        frame.sort_values(["signal_event_id", "gc_offset", "signal_date"], kind="stable")
        .drop_duplicates(subset=["signal_event_id"], keep="first")
        .reset_index(drop=True)
    )

