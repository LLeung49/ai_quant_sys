"""Coverage-aware descriptive and cross-sectional evaluation metrics."""

from collections.abc import Iterable
from typing import Any

import pandas as pd

from ..contracts import SignalFrameSpec


def summarize_event_returns(frame: pd.DataFrame, *, round_trip_cost_bps: Iterable[float] = ()) -> list[dict[str, Any]]:
    total = len(frame)
    metrics: list[dict[str, Any]] = []
    _append_summary(metrics, frame.get("forward_return", pd.Series(dtype=float)), "return", total)
    _append_summary(metrics, frame.get("excess_return", pd.Series(dtype=float)), "excess_return", total)
    _append_summary(metrics, frame.get("mae", pd.Series(dtype=float)), "mae", total)
    _append_summary(metrics, frame.get("mfe", pd.Series(dtype=float)), "mfe", total)
    _append_summary(metrics, frame.get("entry_gap", pd.Series(dtype=float)), "entry_gap", total)
    returns = pd.to_numeric(frame.get("forward_return", pd.Series(dtype=float)), errors="coerce").dropna()
    for cost_bps in round_trip_cost_bps:
        _metric(metrics, f"mean_net_return_bps_{_format_bps(cost_bps)}", (returns - cost_bps / 10_000).mean() if len(returns) else None, len(returns))
    return metrics


def calc_rank_ic(frame: pd.DataFrame, spec: SignalFrameSpec, *, min_cross_section_pairs: int) -> dict[str, Any] | None:
    if not spec.supports_rank_metrics or spec.score_col is None:
        return None
    pairs = _valid_rank_frame(frame, spec.score_col)
    values: list[float] = []
    for _, group in pairs.groupby(list(spec.cross_section_cols), dropna=False):
        if len(group) < min_cross_section_pairs or group[spec.score_col].nunique() < 3:
            continue
        value = group[spec.score_col].corr(group["forward_return"], method="spearman")
        if pd.notna(value):
            values.append(float(value))
    return _record("rank_ic", sum(values) / len(values) if values else None, len(values))


def calc_percentile_group_spread(frame: pd.DataFrame, spec: SignalFrameSpec, *, min_cross_section_pairs: int) -> dict[str, Any] | None:
    if not spec.supports_rank_metrics or spec.score_col is None:
        return None
    pairs = _valid_rank_frame(frame, spec.score_col)
    spreads: list[float] = []
    for _, group in pairs.groupby(list(spec.cross_section_cols), dropna=False):
        if len(group) < min_cross_section_pairs or group[spec.score_col].nunique() < 3:
            continue
        ranks = group[spec.score_col].rank(pct=True, method="average")
        top, bottom = group.loc[ranks >= 0.8, "forward_return"], group.loc[ranks <= 0.2, "forward_return"]
        if len(top) and len(bottom):
            spreads.append(float(top.mean() - bottom.mean()))
    return _record("top_bottom_spread", sum(spreads) / len(spreads) if spreads else None, len(spreads))


def evaluate_condition(frame: pd.DataFrame, spec: SignalFrameSpec, *, min_cross_section_pairs: int,
                       round_trip_cost_bps: Iterable[float] = ()) -> tuple[dict[str, int], list[dict[str, Any]]]:
    header = {
        "candidate_count": len(frame),
        "unique_event_count": frame[spec.event_id_col].nunique() if spec.event_id_col in frame else len(frame),
        "return_complete_count": int(_numeric_column(frame, "forward_return").notna().sum()),
        "excess_complete_count": int(_numeric_column(frame, "excess_return").notna().sum()),
        "path_complete_count": int(_numeric_column(frame, "mae").notna().sum()),
    }
    metrics = summarize_event_returns(frame, round_trip_cost_bps=round_trip_cost_bps)
    for metric in (calc_rank_ic(frame, spec, min_cross_section_pairs=min_cross_section_pairs),
                   calc_percentile_group_spread(frame, spec, min_cross_section_pairs=min_cross_section_pairs)):
        if metric is not None:
            metrics.append(metric)
    return header, metrics


def _append_summary(metrics: list[dict[str, Any]], values: pd.Series, name: str, total: int) -> None:
    numeric = pd.to_numeric(values, errors="coerce").dropna()
    count = len(numeric)
    _metric(metrics, f"{name}_coverage", count / total if total else None, count)
    if name == "return":
        _metric(metrics, "mean_return", numeric.mean() if count else None, count)
        _metric(metrics, "median_return", numeric.median() if count else None, count)
        _metric(metrics, "win_rate", (numeric > 0).mean() if count else None, count)
    elif name == "excess_return":
        _metric(metrics, "mean_excess_return", numeric.mean() if count else None, count)
        _metric(metrics, "excess_win_rate", (numeric > 0).mean() if count else None, count)
    else:
        _metric(metrics, f"mean_{name}", numeric.mean() if count else None, count)
        _metric(metrics, f"median_{name}", numeric.median() if count else None, count)


def _valid_rank_frame(frame: pd.DataFrame, score_col: str) -> pd.DataFrame:
    if score_col not in frame or "forward_return" not in frame:
        return pd.DataFrame(columns=[score_col, "forward_return"])
    return frame[[*frame.columns]].assign(**{
        score_col: pd.to_numeric(frame[score_col], errors="coerce"),
        "forward_return": pd.to_numeric(frame["forward_return"], errors="coerce"),
    }).dropna(subset=[score_col, "forward_return"])


def _numeric_column(frame: pd.DataFrame, column: str) -> pd.Series:
    return pd.to_numeric(frame[column], errors="coerce") if column in frame else pd.Series(dtype=float)


def _metric(metrics: list[dict[str, Any]], name: str, value: object, sample_count: int) -> None:
    metrics.append(_record(name, value, sample_count))


def _record(name: str, value: object, sample_count: int) -> dict[str, Any]:
    return {"metric_name": name, "metric_value": None if pd.isna(value) else float(value), "sample_count": sample_count, "ci_low": None, "ci_high": None}


def _format_bps(value: float) -> str:
    return str(int(value)) if float(value).is_integer() else str(value).replace(".", "_")

