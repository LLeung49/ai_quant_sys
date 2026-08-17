"""v2_short_term 短期异动标签规则。

与 v1 不同：标签**不引入迟滞确认**，但要求至少 2 项证据命中；阈值集中在
``ModelConfigShortTerm.thresholds``。所有判定逻辑都是纯函数，调用方只需
传入原始特征 + 评分 DataFrame，返回 ``(labels, intensity)``。
"""
from __future__ import annotations

from typing import Iterable

import pandas as pd

from .config import ModelConfigShortTerm


# 标签展示顺序：靠前的标签在前端异动榜中优先展示。
SHORT_TERM_LABEL_PRIORITY: tuple[str, ...] = (
    "pulse_up",
    "pulse_down",
    "extreme_up",
    "extreme_down",
    "limit_cluster",
    "limit_panic",
    "volume_spike",
    "short_rebound_candidate",
    "short_breakdown_candidate",
)


def _safe_greater(series: pd.Series, value: float) -> pd.Series:
    return series.where(series.notna(), False) > value


def _safe_less(series: pd.Series, value: float) -> pd.Series:
    return series.where(series.notna(), False) < value


def _safe_ge(series: pd.Series, value: float) -> pd.Series:
    return series.where(series.notna(), False) >= value


def _safe_le(series: pd.Series, value: float) -> pd.Series:
    return series.where(series.notna(), False) <= value


def classify_short_term_labels(row: pd.Series, config: ModelConfigShortTerm) -> tuple[str, str]:
    """对单板块应用全部异动标签规则。

    返回:
        ``(labels_csv, intensity)``：标签为逗号分隔字符串或空串；强度取值
        ``intense`` / ``moderate`` / ``mild`` / ``none``。
    """
    if not bool(row.get("score_eligible", False)):
        return "", "none"

    labels: list[str] = []
    pulse = config.pulse_thresholds()
    volume = config.volume_thresholds()
    limit = config.limit_thresholds()
    extreme = config.extreme_thresholds()
    rebound = config.rebound_thresholds()

    rs_1 = row.get("rs_1", float("nan"))
    breadth_up = row.get("breadth_up", float("nan"))
    if pd.notna(rs_1) and pd.notna(breadth_up):
        if rs_1 >= pulse["rs_min"] and breadth_up >= pulse["breadth_min"]:
            labels.append("pulse_up")
        if rs_1 <= -pulse["rs_min"] and breadth_up <= 1.0 - pulse["breadth_min"]:
            labels.append("pulse_down")

    if pd.notna(rs_1) and pd.notna(row.get("rs_5", float("nan"))):
        if rs_1 >= rebound["rs_min"] and row["rs_5"] < 0:
            labels.append("short_rebound_candidate")
        if rs_1 <= -rebound["rs_min"] and row["rs_5"] > 0:
            labels.append("short_breakdown_candidate")

    if pd.notna(row.get("rvol_1_20", float("nan"))) and row["rvol_1_20"] >= volume["rvol_min"]:
        labels.append("volume_spike")
    elif pd.notna(row.get("share_impulse_1d", float("nan"))) and row["share_impulse_1d"] >= volume["share_impulse_min"]:
        labels.append("volume_spike")

    # 阈值使用 ratio (涨跌停家数 / 有效家数)，与快照表中的 limit_up_ratio / limit_down_ratio 同口径。
    limit_up_ratio = row.get("limit_up_ratio", float("nan"))
    limit_down_ratio = row.get("limit_down_ratio", float("nan"))
    if pd.notna(limit_up_ratio) and pd.notna(limit_down_ratio):
        if limit_up_ratio >= limit["up_min"] and limit_down_ratio <= limit["down_max_for_cluster"]:
            labels.append("limit_cluster")
        if limit_down_ratio >= limit["down_min_for_panic"] and limit_up_ratio <= limit["up_max_for_panic"]:
            labels.append("limit_panic")

    if pd.notna(row.get("ret_1", float("nan"))):
        if row["ret_1"] >= extreme["min_move"]:
            labels.append("extreme_up")
        if row["ret_1"] <= -extreme["min_move"]:
            labels.append("extreme_down")

    intensity = _intensity_for(row, labels, config)
    if not labels:
        return "", "none"
    ordered = [label for label in SHORT_TERM_LABEL_PRIORITY if label in labels]
    return ",".join(ordered), intensity


def _intensity_for(row: pd.Series, labels: Iterable[str], config: ModelConfigShortTerm) -> str:
    """根据命中的标签与评分判定强度等级。"""
    if not labels:
        return "none"
    intense_set = {"limit_cluster", "limit_panic"}
    if any(label in intense_set for label in labels):
        return "intense"
    threshold = config.intensity_thresholds()
    pulse_score = row.get("pulse_score", float("nan"))
    volume_score = row.get("volume_spike_score", float("nan"))
    if pd.notna(pulse_score) and pd.notna(volume_score):
        if pulse_score >= threshold["intense_pulse_score"] and volume_score >= threshold["intense_volume_score"]:
            return "intense"
    if "pulse_up" in labels or "pulse_down" in labels or "extreme_up" in labels or "extreme_down" in labels:
        return "moderate"
    return "mild"


def label_dataframe(frame: pd.DataFrame, config: ModelConfigShortTerm) -> pd.DataFrame:
    """对整个横截面应用标签规则，返回带 ``short_term_labels`` 与 ``short_term_intensity`` 的副本。"""
    result = frame.copy()
    pairs = result.apply(lambda row: classify_short_term_labels(row, config), axis=1, result_type="expand")
    pairs.columns = ["short_term_labels", "short_term_intensity"]
    result[["short_term_labels", "short_term_intensity"]] = pairs
    return result
