"""短期异动研究层（v2_short_term）的版本化配置。

本模块是 v2 短期评分与异动标签参数的唯一定义来源；任何阈值或权重的变更
必须新建配置哈希并保留历史快照。``short_term_config_hash`` 与 v1 的
``config_hash`` 算法保持一致，但分别落盘到不同 model_version 行，便于
后续在同一日期下比较 v1 与 v2 的输出。
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from hashlib import sha256
import json
from typing import Mapping


@dataclass(frozen=True)
class ModelConfigShortTerm:
    """不可变的 v2_short_term 模型契约。

    所有阈值仅用于短期异动参考；不构成交易指令、不参与 v1 主评分。
    字段定义遵循 ``sector_rotation2_short_term_v2_plan.md`` 第 4~5 节。
    """

    model_version: str = "v2_short_term"
    # 横截面百分位计算所需的最少有效板块数；与 v1 一致，保持 20。
    min_cross_section: int = 20
    # 异动标签所需的最低个股有效样本；低于此值时不输出短期广度与标签。
    min_member_samples: int = 5
    # 连续性指标统计上限，避免与 v1 的中长期趋势语义重叠。
    streak_max_days: int = 5

    # 收益与相对强度短期评分权重。
    score_weights: Mapping[str, float] = field(
        default_factory=lambda: {
            "pulse_score": 0.30,
            "volume_spike_score": 0.20,
            "breadth_spike_score": 0.20,
            "limit_score": 0.15,
            "momentum_shift_score": 0.15,
        }
    )
    # 主评分最低可用权重和；低于此值时该板块不参与短期综合排名。
    score_minimum_weight: float = 0.60

    # 异动标签阈值集中在这里；调整任意阈值都会改变 config_hash，因此必须新建版本。
    thresholds: Mapping[str, float] = field(
        default_factory=lambda: {
            # pulse_up / pulse_down：双证据最少命中。
            "pulse_rs_min": 0.005,                 # 板块相对市场至少跑赢/输 0.5%
            "pulse_breadth_min": 0.55,             # 上涨家数占比至少 55%
            # volume_spike：当日成交显著放大。
            "volume_rvol_min": 1.80,               # rvol_1_20 阈值
            "volume_share_impulse_min": 1.30,      # share_impulse_1d 阈值
            # limit_cluster / limit_panic：涨跌停集群。
            "limit_up_cluster_min": 3,             # 至少 3 家涨停
            "limit_down_cluster_max": 1,           # 跌停不超过 1 家
            "limit_down_panic_min": 3,
            "limit_up_panic_max": 1,
            # extreme_up / extreme_down：单日极端涨幅。
            "extreme_move_min": 0.03,              # ±3%
            # 短期反弹/走弱候选：与 5 日方向反转。
            "rebound_rs_min": 0.01,                # rs_1 至少 ±1%
            # 强度分级。
            "intense_pulse_score": 0.75,
            "intense_volume_score": 0.50,
            # 主评分进入 rank 的最低有效板块数（与 min_cross_section 同义但独立参数）。
            "rank_minimum_sectors": 20,
        }
    )

    def pulse_thresholds(self) -> dict[str, float]:
        """返回 ``pulse_up`` / ``pulse_down`` 双证据阈值。"""
        return {
            "rs_min": float(self.thresholds["pulse_rs_min"]),
            "breadth_min": float(self.thresholds["pulse_breadth_min"]),
        }

    def volume_thresholds(self) -> dict[str, float]:
        """返回量能异动判定阈值。"""
        return {
            "rvol_min": float(self.thresholds["volume_rvol_min"]),
            "share_impulse_min": float(self.thresholds["volume_share_impulse_min"]),
        }

    def limit_thresholds(self) -> dict[str, float]:
        """返回涨跌停集群阈值。"""
        return {
            "up_min": float(self.thresholds["limit_up_cluster_min"]),
            "down_max_for_cluster": float(self.thresholds["limit_down_cluster_max"]),
            "down_min_for_panic": float(self.thresholds["limit_down_panic_min"]),
            "up_max_for_panic": float(self.thresholds["limit_up_panic_max"]),
        }

    def extreme_thresholds(self) -> dict[str, float]:
        """返回单日极端涨跌阈值。"""
        return {"min_move": float(self.thresholds["extreme_move_min"])}

    def rebound_thresholds(self) -> dict[str, float]:
        """返回短期反弹/走弱候选阈值。"""
        return {"rs_min": float(self.thresholds["rebound_rs_min"])}

    def intensity_thresholds(self) -> dict[str, float]:
        """返回强度分级阈值。"""
        return {
            "intense_pulse_score": float(self.thresholds["intense_pulse_score"]),
            "intense_volume_score": float(self.thresholds["intense_volume_score"]),
        }


DEFAULT_SHORT_TERM_CONFIG = ModelConfigShortTerm()


def short_term_config_hash(config: ModelConfigShortTerm) -> str:
    """返回完整短期模型配置的确定性哈希。

    使用键排序的紧凑 JSON，与 v1 的 ``config_hash`` 算法保持一致；
    字段顺序或空白不影响指纹，配置不变即可复现。
    """
    payload = json.dumps(asdict(config), ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return sha256(payload.encode("utf-8")).hexdigest()
