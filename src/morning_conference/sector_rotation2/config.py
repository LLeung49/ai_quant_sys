"""独立板块轮动管线的版本化配置。

本模块是影响每日评分参数的唯一来源。每次运行保存确定性配置哈希，
因此即使后续模型版本调整参数，历史快照仍可复现。
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from hashlib import sha256
import json
from typing import Mapping


@dataclass(frozen=True)
class ModelConfig:
    """不可变的 v1 模型契约；变更任何参数时必须新建模型版本。"""
    # 模型配置版本；它与配置哈希一起写入快照，用于区分不同口径的历史结果。
    model_version: str = "v1"
    # 参与横截面百分位计算的最少有效板块数；不足时不生成可比较的分数。
    min_cross_section: int = 20
    # 板块有效 K 线数量 / 应有成员数的最低比例；低于该值的板块不参与排名。
    min_coverage_ratio: float = 0.80
    # phase 从中性或相反方向进入新方向时，速度/加速度分数必须跨越的阈值。
    phase_enter_threshold: float = 0.25
    # 已确认 phase 继续保持时使用的较低阈值；与进入阈值形成迟滞，降低边界抖动。
    phase_hold_threshold: float = 0.10
    # 计算综合分所需的最小可用权重和；证据不足时该板块不产生综合排名。
    score_minimum_weight: float = 0.60
    # 五类分数中的 v1 主评分权重；仅对实际可用的分数按比例重新归一化。
    score_weights: Mapping[str, float] = field(
        default_factory=lambda: {
            # 趋势位置：RS20、RS60 与相对 MA20/MA60 位置，负责筛选强弱候选。
            "trend_level_score": 0.45,
            # 趋势速度：RS5、RS20、MA20 斜率，负责衡量当前运行方向和速度。
            "velocity_score": 0.25,
            # 趋势加速度：RS20 变化、斜率变化、MACD 柱变化，负责识别增强或衰减。
            "acceleration_score": 0.15,
            # 参与度：上涨广度、站上均线、新高和放量广度，负责确认是否为板块共振。
            "participation_score": 0.15,
        }
    )


DEFAULT_CONFIG = ModelConfig()


def config_hash(config: ModelConfig) -> str:
    """返回唯一标识完整模型配置的确定性哈希。

    使用键排序的紧凑 JSON，避免字典插入顺序或空白字符在参数未变时改变指纹。

    参数:
        config: 待标识的不可变模型配置对象。
    返回:
        64 位十六进制 SHA-256 配置哈希。
    """
    payload = json.dumps(asdict(config), ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return sha256(payload.encode("utf-8")).hexdigest()
