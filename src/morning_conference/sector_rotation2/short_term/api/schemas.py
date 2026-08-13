"""v2_short_term API 响应模型。

字段命名沿用 v1 ``ResponseMeta`` 的命名风格，但 ``field_version`` 固定为
``v2_short_term`` 以与 v1 的 ``v1`` 区分。
"""
from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field


class ShortTermResponseMeta(BaseModel):
    """短期异动响应的统一元信息。"""

    run_status: Literal["succeeded"] = Field(default="succeeded", description="仅暴露成功运行数据")
    field_version: Literal["v2_short_term"] = Field(default="v2_short_term", description="API 字段语义版本")
    source_max_trade_date: str | None = Field(default=None, description="上游行情源最大交易日")
    eligible_sector_count: int | None = Field(default=None, description="本次短期运行可评分行业数")
    skipped_sector_count: int | None = Field(default=None, description="因证据不足跳过的行业数")
    pulse_up_count: int | None = Field(default=None, description="命中 pulse_up 的板块数")
    volume_spike_count: int | None = Field(default=None, description="命中 volume_spike 的板块数")
    limit_cluster_count: int | None = Field(default=None, description="命中 limit_cluster 的板块数")
    limit_panic_count: int | None = Field(default=None, description="命中 limit_panic 的板块数")


class ShortTermSnapshotResponse(BaseModel):
    """单日短期异动快照响应。"""

    as_of_date: str = Field(description="快照所属交易日")
    sector_level: int = Field(description="申万行业层级")
    model_version: str = Field(description="短期异动模型版本")
    meta: ShortTermResponseMeta = Field(description="本次响应对应的运行与异动计数元信息")
    sectors: list[dict[str, Any]] = Field(description="已成功运行的短期异动快照列表")


class AvailableDatesResponse(BaseModel):
    """短期异动页面下拉框的可选日期列表。"""

    sector_level: int
    model_version: str
    dates: list[str]


class ShortTermHistoryResponse(BaseModel):
    """短期异动历史轨迹响应。"""

    sector_level: int
    model_version: str
    meta: ShortTermResponseMeta
    points: list[dict[str, Any]]


class ShortTermLeadersResponse(BaseModel):
    """异动榜响应：仅包含命中标签且强度达阈值的板块。"""

    as_of_date: str
    sector_level: int
    model_version: str
    meta: ShortTermResponseMeta
    leaders: list[dict[str, Any]]
