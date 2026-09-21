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

    参数:
        series: 单一交易日、以板块为索引的待标准化数值序列。
        minimum_count: 允许形成有效截面的最少非空板块数。
    返回:
        与输入索引一致的浮点序列；有效值映射至 [-1, 1]，无效位置为 NaN。
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

    参数:
        frame: 行为板块、列为评分维度的特征 DataFrame。
        weights: 评分维度到原始权重的映射，键必须全部存在于 frame。
        minimum_weight: 单行参与综合评分所需的最小可用权重和。
    返回:
        与 frame 索引一致的加权均值序列；证据不足的行返回 NaN。
    异常:
        KeyError: weights 中任一评分维度不在 frame 列中时抛出。
    """
    columns = list(weights)
    # 评分权重中声明的字段必须全部存在；缺字段意味着调用方的特征面板契约被破坏。
    missing = set(columns).difference(frame.columns)
    if missing:
        raise KeyError(f"Missing weighted columns: {sorted(missing)}")

    # 将配置字典转为与 DataFrame 列对齐的权重序列，后续按列广播计算。
    weight_series = pd.Series(weights, dtype="float64")
    # 每行分别判断哪些分数可用；不同板块允许缺失的评分维度不同。
    available = frame[columns].notna()
    # 只累计可用分数的权重。例如仅趋势位置可用时，权重和为 0.45。
    available_weight = available.mul(weight_series, axis=1).sum(axis=1)
    # 加权分子只包含非空分数；min_count=1 防止整行缺失时被 pandas 默认为 0。
    numerator = frame[columns].mul(weight_series, axis=1).sum(axis=1, min_count=1)
    # 权重和达到门槛才除以可用权重和，从而在缺少部分指标时保持同一 [-1, 1] 尺度；
    # 低于门槛则保留 NaN，后续不应为该板块生成综合排名。
    result = numerator.div(available_weight.where(available_weight >= minimum_weight))
    return result.astype("float64")

