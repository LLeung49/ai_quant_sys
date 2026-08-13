"""v2_short_term 短期评分合成。

沿用 v1 的 ``signed_percentile`` 截面标准化，但不参与 ``composite_score``
或 ``composite_rank``；所有分数通过新增的 ``short_term_composite`` 字段
输出，便于后续单独评估 1/2 日前瞻收益的关系。
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from ..normalizers import signed_percentile, weighted_available_mean
from .config import ModelConfigShortTerm


def _score_group(frame: pd.DataFrame, columns: list[str], minimum_count: int) -> pd.Series:
    """对一组原始指标做当日百分位标准化后等权合成。

    与 v1 的同款实现完全一致，但放在 v2 包内避免任何隐式依赖。
    """
    available = [column for column in columns if column in frame]
    if not available:
        return pd.Series(float("nan"), index=frame.index)
    normalized = pd.DataFrame({
        column: signed_percentile(frame[column], minimum_count) for column in available
    })
    return normalized.mean(axis=1, skipna=True).where(normalized.notna().sum(axis=1) >= 2)


def score_short_term_panel(panel: pd.DataFrame, config: ModelConfigShortTerm) -> pd.DataFrame:
    """计算五类短期评分、主评分与短期排名。

    参数:
        panel: 行为板块、列为原始特征的同日横截面 DataFrame。
        config: ``ModelConfigShortTerm`` 实例。
    返回:
        在 ``panel`` 副本上新增五类评分、``score_eligible``、``short_term_composite`` 与
        ``short_term_composite_rank`` 列的 DataFrame。
    """
    result = panel.copy()
    minimum = int(config.thresholds.get("rank_minimum_sectors", config.min_cross_section))
    result["pulse_score"] = _score_group(result, ["rs_1", "rs_2"], minimum)
    # 量能脉冲：rvol_1_20 与 share_impulse_1d 都取对数后标准化，减弱极端放量影响。
    for source, target in (("rvol_1_20", "_log_rvol_1_20"), ("share_impulse_1d", "_log_share_impulse_1d")):
        result[target] = np.log(result[source].where(result[source] > 0)) if source in result else np.nan
    result["volume_spike_score"] = _score_group(result, ["_log_rvol_1_20", "_log_share_impulse_1d"], minimum)
    result["breadth_spike_score"] = _score_group(
        result,
        ["breadth_above_ma5", "breadth_new_high_5", "breadth_strong_1d", "breadth_rvol_1d"],
        minimum,
    )
    # 涨跌停占比：直接用 (limit_up - limit_down) 截面归一化。
    # 不再要求"必须有涨跌停"，否则大多数无涨停的板块会被全部置 NaN，
    # 导致 limit_score 100% 缺失（数据库诊断已确认 1036/1036 = 100% NULL）。
    # 注意：必须直接调 signed_percentile 而非 _score_group，
    # 因为 _score_group 要求至少 2 个非空证据，而涨跌停只有一个合成信号。
    result["_limit_input"] = result["limit_up_ratio"].fillna(0) - result["limit_down_ratio"].fillna(0)
    result["limit_score"] = signed_percentile(result["_limit_input"], minimum)
    result["momentum_shift_score"] = _score_group(result, ["rs5_accel_1d", "ma5_slope"], minimum)

    weights = dict(config.score_weights)
    result["short_term_composite"] = weighted_available_mean(
        result,
        weights,
        float(config.score_minimum_weight),
    )
    result["score_eligible"] = result["short_term_composite"].notna()
    eligible = result["score_eligible"]
    result["short_term_composite_rank"] = result.loc[eligible, "short_term_composite"].rank(
        ascending=False, method="min"
    )
    return result.drop(
        columns=["_log_rvol_1_20", "_log_share_impulse_1d", "_limit_input"],
        errors="ignore",
    )
