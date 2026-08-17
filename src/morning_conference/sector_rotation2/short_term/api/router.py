"""v2_short_term 的 FastAPI 路由。

仅暴露只读端点；如需触发每日运行，请直接调用
``short_term.run_daily.run_short_term_for`` 而非 HTTP。
"""
from __future__ import annotations

from datetime import date

from fastapi import APIRouter, HTTPException, Query

from ...api.schemas import normalize_json_numbers
from .repository import MAX_SHORT_TERM_SECTORS, ShortTermRepository
from .schemas import (
    AvailableDatesResponse,
    ShortTermHistoryResponse,
    ShortTermLeadersResponse,
    ShortTermResponseMeta,
    ShortTermSnapshotResponse,
)


router = APIRouter(prefix="/api/v1/sector-rotation/short-term", tags=["板块轮动-短期异动"])


def _not_found(code: str, message: str) -> HTTPException:
    return HTTPException(status_code=404, detail={"code": code, "message": message})


def _invalid_parameter(message: str) -> HTTPException:
    return HTTPException(status_code=422, detail={"code": "INVALID_PARAMETER", "message": message})


def _parse_date(raw: str) -> date:
    try:
        return date.fromisoformat(raw)
    except ValueError as exc:
        raise _invalid_parameter("日期必须使用 YYYY-MM-DD 格式") from exc


def _split_run_metadata(rows: list[dict]) -> tuple[ShortTermResponseMeta, list[dict]]:
    """从快照行中提取运行元信息并清理内部辅助列。

    同时返回每个 KPI 标签命中的板块名称列表，按 short_term_composite_rank 升序排列，供前端悬停展示使用。
    """
    latest_row = max(rows, key=lambda row: str(row.get("as_of_date", "")))
    source_dates = [str(row["_source_max_trade_date"]) for row in rows if row.get("_source_max_trade_date") is not None]

    # 按 short_term_composite_rank 升序：rank 缺失的板块排到末尾。快照表查询顺序本身已按 rank 升序返回，这里只需过滤与重复。
    def _rank_key(row: dict) -> tuple[int, str]:
        rank = row.get("short_term_composite_rank")
        rank_key = int(rank) if isinstance(rank, int) or (rank is not None and str(rank).isdigit()) else 10 ** 6
        return (rank_key, str(row.get("sector_name") or ""))

    sorted_rows = sorted(rows, key=_rank_key)

    def _sectors_with_label(label: str) -> list[str]:
        names: list[str] = []
        for row in sorted_rows:
            labels = (row.get("short_term_labels") or "").split(",")
            if label in labels:
                name = row.get("sector_name")
                if name and name not in names:
                    names.append(str(name))
        return names

    pulse_up_names = _sectors_with_label("pulse_up")
    volume_spike_names = _sectors_with_label("volume_spike")
    limit_cluster_names = _sectors_with_label("limit_cluster")
    limit_panic_names = _sectors_with_label("limit_panic")

    meta = ShortTermResponseMeta(
        source_max_trade_date=max(source_dates) if source_dates else None,
        eligible_sector_count=latest_row.get("_eligible_sector_count"),
        skipped_sector_count=latest_row.get("_skipped_sector_count"),
        pulse_up_count=len(pulse_up_names),
        volume_spike_count=len(volume_spike_names),
        limit_cluster_count=len(limit_cluster_names),
        limit_panic_count=len(limit_panic_names),
        pulse_up_sectors=pulse_up_names,
        volume_spike_sectors=volume_spike_names,
        limit_cluster_sectors=limit_cluster_names,
        limit_panic_sectors=limit_panic_names,
    )
    business = [{key: value for key, value in row.items() if not key.startswith("_")} for row in rows]
    return meta, business


@router.get("/available-dates", response_model=AvailableDatesResponse, summary="读取短期异动快照可用日期")
def get_available_dates(
    level: int = Query(default=2, ge=1, le=2, description="申万行业层级"),
    model_version: str = Query(default="v2_short_term", min_length=1, max_length=32),
) -> AvailableDatesResponse:
    """返回倒序排列的成功运行日期列表；前端用它作为日期选择器的下拉数据。"""
    dates = ShortTermRepository().list_available_dates(level, model_version)
    return AvailableDatesResponse(sector_level=level, model_version=model_version, dates=dates)


@router.get("/snapshot", response_model=ShortTermSnapshotResponse, summary="读取短期异动单日快照")
def get_short_term_snapshot(
    as_of_date: str = Query(description="交易日，格式 YYYY-MM-DD"),
    level: int = Query(default=2, ge=1, le=2, description="申万行业层级"),
    model_version: str = Query(default="v2_short_term", min_length=1, max_length=32),
) -> ShortTermSnapshotResponse:
    """返回指定交易日的全板块短期异动快照；无成功运行时返回 404。"""
    _parse_date(as_of_date)
    rows = ShortTermRepository().load_snapshot(as_of_date, level, model_version)
    if not rows:
        raise _not_found("SHORT_TERM_SNAPSHOT_NOT_FOUND", "未找到已成功运行的短期异动快照")
    meta, sectors = _split_run_metadata(rows)
    return ShortTermSnapshotResponse(
        as_of_date=as_of_date,
        sector_level=level,
        model_version=model_version,
        meta=meta,
        sectors=normalize_json_numbers(sectors),
    )


@router.get("/history", response_model=ShortTermHistoryResponse, summary="读取短期异动历史轨迹")
def get_short_term_history(
    sector_names: list[str] = Query(
        min_length=1,
        max_length=MAX_SHORT_TERM_SECTORS,
        description=f"行业名称，可重复传入最多 {MAX_SHORT_TERM_SECTORS} 个",
    ),
    start_date: str = Query(description="起始交易日，格式 YYYY-MM-DD"),
    end_date: str = Query(description="结束交易日，格式 YYYY-MM-DD"),
    level: int = Query(default=2, ge=1, le=2, description="申万行业层级"),
    model_version: str = Query(default="v2_short_term", min_length=1, max_length=32),
) -> ShortTermHistoryResponse:
    """返回指定板块在闭区间内的每日短期异动轨迹。"""
    sd, ed = _parse_date(start_date), _parse_date(end_date)
    if sd > ed:
        raise _invalid_parameter("开始日期不能晚于结束日期")
    points = ShortTermRepository().load_history(sector_names, start_date, end_date, level, model_version)
    if not points:
        raise _not_found("SHORT_TERM_HISTORY_NOT_FOUND", "未找到所选板块的短期异动历史")
    meta, business_points = _split_run_metadata(points)
    return ShortTermHistoryResponse(
        sector_level=level,
        model_version=model_version,
        meta=meta,
        points=normalize_json_numbers(business_points),
    )


@router.get("/leaders", response_model=ShortTermLeadersResponse, summary="读取当日短期异动榜")
def get_short_term_leaders(
    as_of_date: str = Query(description="交易日，格式 YYYY-MM-DD"),
    level: int = Query(default=2, ge=1, le=2, description="申万行业层级"),
    model_version: str = Query(default="v2_short_term", min_length=1, max_length=32),
    labels: list[str] | None = Query(default=None, description="按标签过滤，可多选"),
    min_intensity: str | None = Query(default=None, description="最低强度：intense/moderate/mild"),
) -> ShortTermLeadersResponse:
    """按标签与强度过滤后返回当日异动榜。"""
    _parse_date(as_of_date)
    repo = ShortTermRepository()
    parsed_labels = repo.parse_label_filter(labels)
    parsed_intensity = repo.parse_intensity_filter(min_intensity)

    rows = repo.load_snapshot(as_of_date, level, model_version)
    if not rows:
        raise _not_found("SHORT_TERM_SNAPSHOT_NOT_FOUND", "未找到已成功运行的短期异动快照")
    leaders = []
    for row in rows:
        row_labels = set((row.get("short_term_labels") or "").split(",")) - {""}
        if parsed_labels and not row_labels.intersection(parsed_labels):
            continue
        if parsed_intensity:
            order = {"intense": 3, "moderate": 2, "mild": 1, "none": 0}
            if order.get(row.get("short_term_intensity") or "none", 0) < order[parsed_intensity]:
                continue
        leaders.append({key: value for key, value in row.items() if not key.startswith("_")})
    leaders.sort(key=lambda r: (r.get("short_term_composite_rank") or 10**6, r.get("sector_name") or ""))
    meta, _ = _split_run_metadata(rows)
    return ShortTermLeadersResponse(
        as_of_date=as_of_date,
        sector_level=level,
        model_version=model_version,
        meta=meta,
        leaders=normalize_json_numbers(leaders),
    )
