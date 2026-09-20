"""板块轮动可视化 API 的响应数据模型。"""

from __future__ import annotations

from decimal import Decimal
from typing import Any, Literal

from pydantic import BaseModel, Field


def normalize_json_numbers(value: Any) -> Any:
    """递归将数据库 Decimal 数值转换为前端可计算的 JSON number。

    输入：仓储层返回的任意字段值，可包含字典、列表、元组、``Decimal`` 或 ``None``。
    输出：保持原有字段结构；全部 ``Decimal`` 转换为 ``float``，避免 Pydantic 将其序列化为
    JSON 字符串而使浏览器无法进行排序、绘图和格式化计算。
    """
    if isinstance(value, Decimal):
        return float(value)
    if isinstance(value, dict):
        return {key: normalize_json_numbers(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [normalize_json_numbers(item) for item in value]
    return value


class SnapshotResponse(BaseModel):
    """单日板块快照响应。

    输入：仓储层返回的数据库字典行。
    输出：供前端读取的日期、层级、版本和板块列表；数值缺失保持为 JSON ``null``。
    """

    as_of_date: str = Field(description="快照所属交易日")
    sector_level: int = Field(description="申万行业层级")
    model_version: str = Field(description="评分模型版本")
    meta: "ResponseMeta" = Field(description="本响应对应的成功运行审计与字段契约元信息")
    sectors: list[dict[str, Any]] = Field(description="已成功运行的行业快照列表")


class ResponseMeta(BaseModel):
    """所有成功响应共用的运行与字段版本元信息。

    输入：运行审计表字段，以及快照中已持久化的市场状态字段。
    输出：前端可统一展示的数据新鲜度、运行状态和字段契约版本；接口无法归属到
    某一次具体运行时，运行级字段明确返回 ``null``。
    """

    run_status: Literal["succeeded"] = Field(default="succeeded", description="仅暴露成功运行数据")
    field_version: Literal["v1"] = Field(default="v1", description="API 字段语义版本，不等同于模型版本")
    source_max_trade_date: str | None = Field(default=None, description="上游行情源最大交易日")
    eligible_sector_count: int | None = Field(default=None, description="本次运行可评分行业数")
    skipped_sector_count: int | None = Field(default=None, description="本次运行因证据不足跳过的行业数")
    market_regime: str | None = Field(default=None, description="快照已保存的市场状态")
    regime_multiplier: float | None = Field(default=None, description="市场状态对应的风险缩放系数")


class AvailableDatesResponse(BaseModel):
    """可用于板块轮动浏览的成功运行日期响应。"""

    sector_level: int
    model_version: str
    dates: list[str]
    meta: ResponseMeta = Field(default_factory=ResponseMeta)


class CalendarAvailabilityResponse(BaseModel):
    """Bounded calendar availability from upstream data and successful snapshots."""

    sector_level: int
    model_version: str
    trade_dates: list[str]
    snapshot_dates: list[str]
    latest_snapshot_date: str | None


class HistoryResponse(BaseModel):
    """行业轨迹或市场回放的已存储历史点响应。"""

    sector_level: int
    model_version: str
    meta: ResponseMeta
    points: list[dict[str, Any]]


class SectorKlineBar(BaseModel):
    """单根经过数据边界校验的板块合成日 K 线。"""

    trade_date: str
    timestamp: int
    open: float
    high: float
    low: float
    close: float
    volume: float
    amount: float


class SectorKlineMeta(BaseModel):
    """板块 K 线响应的字段版本、来源和清洗统计信息。"""

    field_version: Literal["v1"] = "v1"
    source: Literal["trade_sector_daily"] = "trade_sector_daily"
    bar_count: int
    skipped_bar_count: int
    warmup_target: int = 100


class SectorKlineResponse(BaseModel):
    """板块合成日 K 线的完整 HTTP 成功响应。"""

    sector_name: str
    sector_level: int
    requested_end_date: str
    actual_end_date: str
    price_basis: Literal["equal_weight_composite_index"] = "equal_weight_composite_index"
    bars: list[SectorKlineBar]
    meta: SectorKlineMeta

