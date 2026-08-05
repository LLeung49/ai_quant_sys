"""sector_rotation2 的纯横截面标准化工具。

本文件不读取日期或数据库；调用方只能传入同一交易日的横截面，
从接口层面避免意外使用未来数据。
"""
from __future__ import annotations

from collections.abc import Mapping

import pandas as pd


def signed_percentile(series: pd.Series, minimum_count: int = 20) -> pd.Series:
    """以对并列值安全的平均排名，将有效横截面映射到 [-1, 1]。

    常数列或样本过少时不存在可区分的排名信息，返回 NaN 而不是伪造为 0 分。
    """
    result = pd.Series(float("nan"), index=series.index, dtype="float64")
    valid = series.dropna()
    if len(valid) < minimum_count or valid.nunique() < 2:
        return result

    # 先得到从 1 到 N 的平均排名；并列值取平均名次，避免人为打破并列关系。
    ranks = valid.rank(method="average")
    # 将排名线性映射到 [-1, 1]：最低名次 -> -1，最高名次 -> +1，居中名次 -> 0。
    # 这样 MOM、RS、量能等不同量纲指标可在同一尺度上做加权组合。
    result.loc[valid.index] = 2.0 * (ranks - 1.0) / (len(valid) - 1.0) - 1.0
    return result


def weighted_available_mean(
    frame: pd.DataFrame,
    weights: Mapping[str, float],
    minimum_weight: float,
) -> pd.Series:
    """按可用列计算加权均值，并受最低有效权重约束。

    每个板块只对实际可用指标重新归一化；证据不足的行保持 NaN，
    后续不得获得综合排名。
    """
    columns = list(weights)
    missing = set(columns).difference(frame.columns)
    if missing:
        raise KeyError(f"Missing weighted columns: {sorted(missing)}")

    weight_series = pd.Series(weights, dtype="float64")
    available = frame[columns].notna()
    available_weight = available.mul(weight_series, axis=1).sum(axis=1)
    numerator = frame[columns].mul(weight_series, axis=1).sum(axis=1, min_count=1)
    result = numerator.div(available_weight.where(available_weight >= minimum_weight))
    return result.astype("float64")
