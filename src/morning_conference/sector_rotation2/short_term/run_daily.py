"""v2_short_term 短期异动的每日运行入口与 CLI。

调用样例（与 v1 同款）::

    $env:PYTHONPATH = "src"
    python -m morning_conference.sector_rotation2.short_term.run_daily --level 2 --as-of-date 2026-08-08
    python -m morning_conference.sector_rotation2.short_term.run_daily --level 2 --backfill-start 2026-08-01 --backfill-end 2026-08-08
    python -m morning_conference.sector_rotation2.short_term.run_daily --level 2 --as-of-date 2026-08-08 --csv-output outputs/short_term
    python -m morning_conference.sector_rotation2.short_term.run_daily --level 2 --as-of-date 2026-08-08 --dry-run --csv-output outputs/short_term

``run_short_term_for`` 是编程式入口，``main`` 是 argparse CLI 入口；
二者共用同一套内部辅助函数。
"""
from __future__ import annotations

import argparse
import logging
import uuid
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

from .config import DEFAULT_SHORT_TERM_CONFIG, ModelConfigShortTerm, short_term_config_hash
from ..data_loader import build_market_benchmark, load_sector_panel
from .features import build_short_term_features
from .labels import label_dataframe
from .scoring import score_short_term_panel
from .snapshot_store import (
    create_short_term_run,
    mark_short_term_run_failed,
    mark_short_term_run_succeeded,
    persist_short_term_snapshot,
)


LOGGER = logging.getLogger(__name__)


# CSV 列顺序：保留文档 §7.1 中声明的字段顺序，便于人肉比对。
_CSV_COLUMNS: tuple[str, ...] = (
    "as_of_date", "sector_level", "sector_name", "model_version",
    "score_eligible",
    "ret_1", "ret_2", "ret_3",
    "rs_1", "rs_2", "rs5_accel_1d", "ma5_slope",
    "rvol_1_20", "rvol_1_60",
    "amount_share_today", "share_impulse_1d",
    "breadth_up", "breadth_above_ma5", "breadth_new_high_5",
    "breadth_strong_1d", "breadth_weak_1d", "breadth_rvol_1d",
    "limit_up_ratio", "limit_down_ratio",
    "streak_pos_ret", "streak_high_breadth", "streak_top_limit_up",
    "pulse_score", "volume_spike_score", "breadth_spike_score",
    "limit_score", "momentum_shift_score",
    "short_term_composite", "short_term_composite_rank",
    "short_term_labels", "short_term_intensity",
)


@dataclass(frozen=True)
class ShortTermRunResult:
    """单日短期运行的不可变结果。"""

    run_id: str
    as_of_date: str
    sector_level: int
    model_version: str
    config_hash: str
    eligible_sector_count: int
    skipped_sector_count: int
    snapshot_rows: int


def _attach_member_counters(features: pd.DataFrame, members: dict[str, tuple[int, int]]) -> pd.DataFrame:
    """把外部计算的 ``eligible_member_count``、``valid_member_count`` 挂回到特征表。"""
    if not members:
        features["eligible_member_count"] = pd.NA
        features["valid_member_count"] = pd.NA
        return features
    counts = pd.DataFrame.from_dict(members, orient="index", columns=["eligible_member_count", "valid_member_count"])
    return features.join(counts)


def run_short_term_for(
    sector_level: int,
    as_of_date: str,
    config: ModelConfigShortTerm | None = None,
    panel: dict[str, pd.DataFrame] | None = None,
    benchmark: pd.DataFrame | None = None,
) -> ShortTermRunResult:
    """对单个交易日执行完整的短期异动流水线（编程式入口）。

    步骤：
        1. 生成运行 UUID 与配置哈希；
        2. 写入 ``running`` 审计行；
        3. 加载板块面板并构建原始特征；
        4. 合成短期评分；
        5. 应用异动标签与强度分级；
        6. 批量 upsert 短期快照；
        7. 更新审计行为 succeeded。

    异常:
        任何步骤失败都会把审计行标记为 failed 并原样抛出。
    """
    cfg = config or DEFAULT_SHORT_TERM_CONFIG
    run_id = str(uuid.uuid4())
    config_hash = short_term_config_hash(cfg)

    create_short_term_run(
        run_id=run_id,
        as_of_date=as_of_date,
        sector_level=sector_level,
        model_version=cfg.model_version,
        config_hash=config_hash,
        source_max_trade_date=as_of_date,
    )

    try:
        features = build_short_term_features(sector_level, as_of_date, cfg)
        if features.empty:
            mark_short_term_run_succeeded(run_id, eligible_sector_count=0, skipped_sector_count=0)
            LOGGER.warning("短期特征为空：%s level=%s", as_of_date, sector_level)
            return ShortTermRunResult(
                run_id=run_id,
                as_of_date=as_of_date,
                sector_level=sector_level,
                model_version=cfg.model_version,
                config_hash=config_hash,
                eligible_sector_count=0,
                skipped_sector_count=0,
                snapshot_rows=0,
            )

        scored = score_short_term_panel(features, cfg)
        labelled = label_dataframe(scored, cfg)
        # ``coverage_ratio`` 由调用方根据成员映射计算后注入；本骨架留 NaN 占位。
        labelled["coverage_ratio"] = pd.NA
        snapshot_rows = persist_short_term_snapshot(
            labelled,
            as_of_date=as_of_date,
            sector_level=sector_level,
            model_version=cfg.model_version,
            run_id=run_id,
        )
        eligible_count = int(labelled["score_eligible"].sum())
        skipped_count = int((~labelled["score_eligible"].fillna(False)).sum())
        mark_short_term_run_succeeded(
            run_id,
            eligible_sector_count=eligible_count,
            skipped_sector_count=skipped_count,
        )
        LOGGER.info(
            "短期运行完成：%s level=%s eligible=%s skipped=%s rows=%s",
            as_of_date, sector_level, eligible_count, skipped_count, snapshot_rows,
        )
        return ShortTermRunResult(
            run_id=run_id,
            as_of_date=as_of_date,
            sector_level=sector_level,
            model_version=cfg.model_version,
            config_hash=config_hash,
            eligible_sector_count=eligible_count,
            skipped_sector_count=skipped_count,
            snapshot_rows=snapshot_rows,
        )
    except Exception as exc:  # noqa: BLE001 - 需捕获并把审计行置 failed。
        mark_short_term_run_failed(run_id, repr(exc))
        LOGGER.exception("短期运行失败：%s level=%s", as_of_date, sector_level)
        raise


# ---------- CLI 内部辅助 --------------------------------------------------------


def _build_pipeline(level: int, as_of_date: str, config: ModelConfigShortTerm) -> pd.DataFrame:
    """复刻 ``run_short_term_for`` 的流水线但跳过写库；返回标记过元信息的 DataFrame。"""
    features = build_short_term_features(level, as_of_date, config)
    if features.empty:
        return pd.DataFrame()
    features = _attach_member_counters(features, {})
    features["coverage_ratio"] = pd.NA
    features["as_of_date"] = as_of_date
    features["sector_level"] = level
    features["model_version"] = config.model_version
    features["sector_name"] = features.index.astype(str)
    scored = score_short_term_panel(features, config)
    return label_dataframe(scored, config)


def _write_csv(frame: pd.DataFrame, output_dir: Path, as_of_date: str) -> Path | None:
    """把当日的短期快照写入 CSV，列顺序与文档 §7.1 对齐。"""
    if frame.empty:
        LOGGER.warning("无可写入 CSV 的板块：%s", as_of_date)
        return None
    output_dir.mkdir(parents=True, exist_ok=True)
    csv_path = output_dir / f"short_term_{as_of_date.replace('-', '')}.csv"
    available = [column for column in _CSV_COLUMNS if column in frame.columns]
    frame.loc[:, available].to_csv(csv_path, index=False, encoding="utf-8-sig")
    LOGGER.info("已写入 CSV：%s（%s 行）", csv_path, len(frame))
    return csv_path


def _run_one_date(
    level: int,
    as_of_date: str,
    config: ModelConfigShortTerm,
    csv_output: Path | None,
    dry_run: bool,
) -> ShortTermRunResult | None:
    """CLI 单日执行器；``dry_run=True`` 时跳过任何写库操作。"""
    if dry_run:
        LOGGER.info("[dry-run] 开始计算 %s level=%s", as_of_date, level)
        frame = _build_pipeline(level, as_of_date, config)
        if csv_output:
            _write_csv(frame, csv_output, as_of_date)
        LOGGER.info(
            "[dry-run] %s level=%s：%s 个板块，score_eligible=%s",
            as_of_date, level,
            len(frame), int(frame["score_eligible"].sum()) if "score_eligible" in frame else 0,
        )
        return None
    result = run_short_term_for(level, as_of_date, config)
    if csv_output and result.snapshot_rows > 0:
        # 落库成功后 CSV 仅作人肉备查；从读库再拉一次，避免二次执行流水线。
        from .api.repository import ShortTermRepository  # 局部 import，避免 CLI 启动阶段加载 FastAPI 依赖。
        rows = ShortTermRepository().load_snapshot(as_of_date, level, config.model_version)
        if rows:
            _write_csv(pd.DataFrame(rows), csv_output, as_of_date)
    return result


def _list_trade_dates(level: int, start_date: str, end_date: str) -> list[str]:
    """返回回填区间内可用的交易日列表；与 v1 ``run_daily.list_trade_dates`` 行为一致。"""
    from ..data_loader import load_sector_panel
    panel = load_sector_panel(level=level, start_date=start_date, end_date=end_date, min_history_days=1)
    if not panel:
        return []
    all_dates: set[str] = set()
    for frame in panel.values():
        for date in frame.index:
            iso = date.strftime("%Y-%m-%d")
            if start_date <= iso <= end_date:
                all_dates.add(iso)
    return sorted(all_dates)


# ---------- CLI 入口 ------------------------------------------------------------


def main() -> None:
    """解析 CLI 参数并执行单日或区间回填。"""
    parser = argparse.ArgumentParser(description="运行 sector_rotation2 v2_short_term 短期异动流水线")
    parser.add_argument("--level", type=int, required=True, choices=(1, 2), help="申万行业层级")
    parser.add_argument("--as-of-date", help="单日交易日，格式 YYYY-MM-DD")
    parser.add_argument("--backfill-start", help="回填起始交易日，需与 --backfill-end 同时提供")
    parser.add_argument("--backfill-end", help="回填结束交易日，需与 --backfill-start 同时提供")
    parser.add_argument("--model-version", default="v2_short_term", help="短期模型版本（默认 v2_short_term）")
    parser.add_argument("--csv-output", help="可选：把当日短期快照落盘到该目录的 CSV，文件名 short_term_YYYYMMDD.csv")
    parser.add_argument("--dry-run", action="store_true", help="只计算不写库；可与 --csv-output 搭配用于本地检视")
    parser.add_argument(
        "--log-level",
        default="INFO",
        choices=("DEBUG", "INFO", "WARNING", "ERROR"),
        help="终端日志级别",
    )
    args = parser.parse_args()

    if bool(args.backfill_start) ^ bool(args.backfill_end):
        parser.error("--backfill-start 与 --backfill-end 必须同时提供")
    if not args.as_of_date and not (args.backfill_start and args.backfill_end):
        parser.error("必须提供 --as-of-date 或完整的 --backfill-start/--backfill-end 区间")

    logging.basicConfig(
        level=getattr(logging, args.log_level),
        format="%(asctime)s %(levelname)-8s %(name)s - %(message)s",
    )

    config = ModelConfigShortTerm(model_version=args.model_version)
    csv_dir = Path(args.csv_output).resolve() if args.csv_output else None

    if args.backfill_start and args.backfill_end:
        trade_dates = _list_trade_dates(args.level, args.backfill_start, args.backfill_end)
        if not trade_dates:
            LOGGER.warning("回填区间 [%s, %s] 在 level=%s 下没有可用交易日", args.backfill_start, args.backfill_end, args.level)
            return
        LOGGER.info(
            "开始回填：level=%s model=%s dates=%s config_hash=%s dry_run=%s",
            args.level, config.model_version, trade_dates, short_term_config_hash(config), args.dry_run,
        )
        success = 0
        for trade_date in trade_dates:
            try:
                result = _run_one_date(args.level, trade_date, config, csv_dir, args.dry_run)
                if result is not None or args.dry_run:
                    success += 1
            except Exception:
                LOGGER.exception("回填日期失败：%s", trade_date)
                if not args.dry_run:
                    raise
        LOGGER.info("回填完成：成功 %s / 共 %s", success, len(trade_dates))
    else:
        _run_one_date(args.level, args.as_of_date, config, csv_dir, args.dry_run)


if __name__ == "__main__":
    main()