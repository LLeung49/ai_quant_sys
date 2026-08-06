"""板块轮动可视化的只读 HTTP 路由。"""

from __future__ import annotations

from datetime import date

from fastapi import APIRouter, HTTPException, Query

from .repository import MAX_HISTORY_SECTORS, SectorRotationRepository
from .schemas import AvailableDatesResponse, HistoryResponse, ResponseMeta, SnapshotResponse, normalize_json_numbers


router = APIRouter(prefix="/api/v1/sector-rotation", tags=["板块轮动"])


def _not_found(code: str, message: str) -> HTTPException:
    """构造统一业务未找到错误。

    输入：稳定错误码和中文提示。
    输出：由应用异常处理器封装为统一错误 JSON 的 404 异常。
    """
    return HTTPException(status_code=404, detail={"code": code, "message": message})


def _split_run_metadata(rows: list[dict]) -> tuple[ResponseMeta, list[dict]]:
    """从查询结果中拆出统一运行元信息并清理内部辅助列。

    输入：仓储层返回的一个或多个成功运行快照行，内部运行字段使用下划线前缀。
    输出：第一项为聚合后的 ``ResponseMeta``；第二项为不含内部辅助字段的业务行。
    历史查询跨多日时，数据截止日取所有运行中的最大值，计数和市场状态取最后一个
    交易日的持久化值；本方法不会重新计算任何评分或阶段。
    """
    latest_row = max(rows, key=lambda row: str(row.get("as_of_date", "")))
    source_dates = [str(row["_source_max_trade_date"]) for row in rows if row.get("_source_max_trade_date") is not None]
    metadata = ResponseMeta(
        source_max_trade_date=max(source_dates) if source_dates else None,
        eligible_sector_count=latest_row.get("_eligible_sector_count"),
        skipped_sector_count=latest_row.get("_skipped_sector_count"),
        market_regime=latest_row.get("market_regime"),
        regime_multiplier=latest_row.get("regime_multiplier"),
    )
    business_rows = [{key: value for key, value in row.items() if not key.startswith("_")} for row in rows]
    return metadata, business_rows


def _validate_date_range(start_date: str, end_date: str) -> None:
    """校验历史类接口的 ISO 日期格式与先后顺序。

    输入：闭区间起止日期字符串。
    输出：合法时无返回值；格式非法或开始日晚于结束日时抛出带稳定错误码的
    422 ``HTTPException``，并保证非法条件不会进入仓储查询。
    """
    try:
        start = date.fromisoformat(start_date)
        end = date.fromisoformat(end_date)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail={"code": "INVALID_DATE_RANGE", "message": "日期必须使用 YYYY-MM-DD 格式"}) from exc
    if start > end:
        raise HTTPException(status_code=422, detail={"code": "INVALID_DATE_RANGE", "message": "开始日期不能晚于结束日期"})


@router.get("/available-dates", response_model=AvailableDatesResponse, summary="读取可查看的交易日")
def get_available_dates(
    level: int = Query(default=2, ge=1, le=2, description="申万行业层级，仅支持 1 或 2"),
    model_version: str = Query(default="v1", min_length=1, max_length=32, description="评分模型版本"),
) -> AvailableDatesResponse:
    """读取存在成功运行快照的可选交易日。

    输入：行业层级和模型版本。
    输出：交易日倒序列表；没有日期时返回空列表而非错误。
    """
    return AvailableDatesResponse(
        sector_level=level,
        model_version=model_version,
        dates=SectorRotationRepository().list_available_dates(level, model_version),
    )


@router.get("/snapshot", response_model=SnapshotResponse, summary="读取指定交易日的板块轮动快照")
def get_snapshot(
    as_of_date: str = Query(description="交易日，格式 YYYY-MM-DD"),
    level: int = Query(default=2, ge=1, le=2, description="申万行业层级，仅支持 1 或 2"),
    model_version: str = Query(default="v1", min_length=1, max_length=32, description="评分模型版本"),
) -> SnapshotResponse:
    """读取指定条件下已成功运行的全行业快照。

    输入：交易日、行业层级和模型版本。
    输出：有数据时返回 200 快照；没有成功运行数据时返回带错误码的 404。
    """
    sectors = SectorRotationRepository().load_snapshot(as_of_date, level, model_version)
    if not sectors:
        raise _not_found("SNAPSHOT_NOT_FOUND", "未找到已成功运行的板块快照")
    meta, business_sectors = _split_run_metadata(sectors)
    return SnapshotResponse(
        as_of_date=as_of_date,
        sector_level=level,
        model_version=model_version,
        meta=meta,
        sectors=normalize_json_numbers(business_sectors),
    )


@router.get("/sector-history", response_model=HistoryResponse, summary="读取行业轮动轨迹")
def get_sector_history(
    sector_name: list[str] = Query(min_length=1, max_length=MAX_HISTORY_SECTORS, description="行业名称，可重复传入最多五个"),
    start_date: str = Query(description="起始交易日，格式 YYYY-MM-DD"),
    end_date: str = Query(description="结束交易日，格式 YYYY-MM-DD"),
    level: int = Query(default=2, ge=1, le=2, description="申万行业层级，仅支持 1 或 2"),
    model_version: str = Query(default="v1", min_length=1, max_length=32, description="评分模型版本"),
) -> HistoryResponse:
    """读取指定行业在日期区间内已成功保存的轮动坐标。

    输入：一至五个行业、日期范围、层级和模型版本。
    输出：按日期排序的历史快照；无点时返回 ``HISTORY_NOT_FOUND``。
    """
    _validate_date_range(start_date, end_date)
    points = SectorRotationRepository().load_sector_history(sector_name, start_date, end_date, level, model_version)
    if not points:
        raise _not_found("HISTORY_NOT_FOUND", "未找到所选行业的已成功运行历史快照")
    meta, business_points = _split_run_metadata(points)
    return HistoryResponse(sector_level=level, model_version=model_version, meta=meta, points=normalize_json_numbers(business_points))


@router.get("/replay", response_model=HistoryResponse, summary="读取全市场轮动回放数据")
def get_replay(
    start_date: str = Query(description="起始交易日，格式 YYYY-MM-DD"),
    end_date: str = Query(description="结束交易日，格式 YYYY-MM-DD"),
    level: int = Query(default=2, ge=1, le=2, description="申万行业层级，仅支持 1 或 2"),
    model_version: str = Query(default="v1", min_length=1, max_length=32, description="评分模型版本"),
) -> HistoryResponse:
    """读取指定期间的全行业历史坐标，供前端预加载播放。

    输入：日期范围、行业层级和模型版本。
    输出：按日期和行业排序的历史点；无点时返回 ``REPLAY_NOT_FOUND``。
    """
    _validate_date_range(start_date, end_date)
    points = SectorRotationRepository().load_replay(start_date, end_date, level, model_version)
    if not points:
        raise _not_found("REPLAY_NOT_FOUND", "未找到该日期范围的已成功运行回放快照")
    meta, business_points = _split_run_metadata(points)
    return HistoryResponse(sector_level=level, model_version=model_version, meta=meta, points=normalize_json_numbers(business_points))
