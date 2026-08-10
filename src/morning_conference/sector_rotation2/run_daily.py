"""板块轮动的每日和指定区间回填入口。


$env:PYTHONPATH = "src"
D:\Programs\Python\Python313\python.exe -m morning_conference.sector_rotation2.run_daily --level 1 --backfill-start 2026-07-10 --backfill-end 2026-08-06
D:\Programs\Python\Python313\python.exe -m morning_conference.sector_rotation2.run_daily --level 1 --as-of-date 2026-08-06
D:\Programs\Python\Python313\python.exe -m morning_conference.sector_rotation2.run_daily --level 2 --as-of-date 2026-08-06

"""
from __future__ import annotations

import argparse
import logging
from pathlib import Path
from uuid import uuid4

import pandas as pd

from .config import DEFAULT_CONFIG, ModelConfig, config_hash
from .data_loader import build_market_benchmark, load_historical_sector_panel, load_market_aggregates, load_sector_panel
from .market_regime import classify_market_regime
from .lifecycle import apply_lifecycle_v0
from .report import write_daily_reports
from .scoring import apply_phase_history, score_feature_panel
from .sector_features import build_daily_feature_panel, build_historical_feature_panels
from .snapshot_store import (
    create_run, load_previous_snapshots, mark_run_failed, mark_run_succeeded, persist_daily_snapshot,
)


LOGGER = logging.getLogger(__name__)


def load_market_benchmark(level: int, as_of_date: str) -> pd.DataFrame:
    """加载计算目标日市场状态所需的基准历史。

    参数:
        level: 板块层级。
        as_of_date: 目标交易日。
    返回:
        至少包含 close、amount 的市场基准历史 DataFrame。
    """
    panel = load_sector_panel(level=level, end_date=as_of_date, min_history_days=90)
    return build_market_benchmark(panel)


def list_trade_dates(level: int, start_date: str, end_date: str) -> list[str]:
    """返回指定日期范围内可运行的交易日。

    参数:
        level: 板块层级。
        start_date: 回填起始日。
        end_date: 回填结束日。
    返回:
        去重后按升序排列的 ISO 日期字符串。
    """
    panel = load_sector_panel(level=level, start_date=start_date, end_date=end_date, min_history_days=1)
    dates = pd.to_datetime(pd.Index([]).append([frame.index for frame in panel.values()]).unique())
    return [date.strftime("%Y-%m-%d") for date in sorted(dates) if start_date <= date.strftime("%Y-%m-%d") <= end_date]


def run_one_date(level: int, as_of_date: str, config: ModelConfig = DEFAULT_CONFIG, output_dir: str | Path = "outputs", feature_panel: pd.DataFrame | None = None, market_benchmark: pd.DataFrame | None = None, market_aggregates: pd.DataFrame | None = None) -> pd.DataFrame:
    """执行一个交易日的完整板块轮动流程。

    参数:
        level: 板块层级。
        as_of_date: 计算交易日。
        config: 冻结的模型配置。
        output_dir: 成功落库后写出晨会文件的目录。
    返回:
        已落库且已输出的当日评分 DataFrame。
    异常:
        Exception: 任一步骤失败时标记运行失败并原样抛出；不写成功输出文件。
    """
    run_id = str(uuid4())
    try:
        LOGGER.info("开始单日计算：run_id=%s, level=%s, as_of_date=%s, model=%s", run_id, level, as_of_date, config.model_version)
        LOGGER.info("步骤 1/7：加载板块与个股原始数据并计算特征，请关注后续板块进度日志")
        features = feature_panel if feature_panel is not None else build_daily_feature_panel(level=level, as_of_date=as_of_date)
        LOGGER.info("步骤 1/7 完成：获得 %s 个板块特征", len(features))
        LOGGER.info("步骤 2/7：加载市场基准历史")
        benchmark = market_benchmark.loc[:as_of_date] if market_benchmark is not None else load_market_benchmark(level=level, as_of_date=as_of_date)
        source_max_trade_date = pd.Timestamp(benchmark.index.max()).strftime("%Y-%m-%d")
        create_run(run_id, as_of_date, level, config.model_version, config_hash(config), source_max_trade_date)
        LOGGER.info("步骤 3/7：已创建运行审计，source_max_trade_date=%s", source_max_trade_date)
        # 市场状态必须使用历史板块聚合的真实上涨广度和限涨跌，而非用固定常量替代。
        aggregates = market_aggregates.loc[:as_of_date] if market_aggregates is not None else load_market_aggregates(load_sector_panel(level=level, end_date=as_of_date, min_history_days=90))
        breadth = aggregates["breadth_up_median"] if "breadth_up_median" in aggregates else pd.Series(dtype=float)
        regime = classify_market_regime(benchmark, breadth, aggregates, pd.Timestamp(as_of_date))
        LOGGER.info("步骤 4/7：市场状态=%s，风险乘数=%.2f", regime.market_regime, regime.regime_multiplier)
        scored = score_feature_panel(features, config)
        scored["market_regime"] = regime.market_regime
        scored["regime_multiplier"] = regime.regime_multiplier
        scored["composite_score"] = scored["base_score"] * regime.regime_multiplier
        previous = load_previous_snapshots(as_of_date=as_of_date, sector_level=level, model_version=config.model_version)
        LOGGER.info("步骤 5/7：完成横截面评分，读取到 %s 条历史快照", 0 if previous is None else len(previous))
        final = apply_lifecycle_v0(apply_phase_history(scored, previous, config), previous)
        LOGGER.info("步骤 6/7：写入 %s 条板块快照", len(final))
        persist_daily_snapshot(final, as_of_date, level, config.model_version, run_id)
        eligible_count = int(final["score_eligible"].sum())
        mark_run_succeeded(run_id, eligible_count, len(final) - eligible_count)
        LOGGER.info("步骤 7/7：快照提交成功，有效=%s，跳过=%s，开始生成晨会文件", eligible_count, len(final) - eligible_count)
        write_daily_reports(final, as_of_date, output_dir)
        LOGGER.info("单日计算完成：输出目录=%s", output_dir)
        return final
    except Exception as error:
        LOGGER.exception("单日计算失败：run_id=%s, error=%s", run_id, error)
        try:
            mark_run_failed(run_id, str(error))
        finally:
            raise


def run_backfill(level: int, start_date: str, end_date: str, config: ModelConfig = DEFAULT_CONFIG, output_dir: str | Path = "outputs") -> None:
    """按交易日升序回填每日快照，确保 phase 只依赖此前结果。

    参数:
        level: 板块层级。
        start_date: 回填起始交易日。
        end_date: 回填结束交易日。
        config: 冻结的模型配置。
        output_dir: 每日晨会输出目录。
    返回:
        无；任一日期失败时停止并抛出异常。
    """
    for trade_date in sorted(list_trade_dates(level=level, start_date=start_date, end_date=end_date)):
        run_one_date(level, trade_date, config, output_dir)


def run_historical_backfill(level: int, start_date: str, end_date: str, config: ModelConfig = DEFAULT_CONFIG, output_dir: str | Path = "outputs") -> None:
    """使用批量预计算特征按日期升序执行历史快照回填。"""
    market_panel = load_historical_sector_panel(level, start_date, end_date)
    benchmark = build_market_benchmark(market_panel)
    aggregates = load_market_aggregates(market_panel)
    for trade_date, feature_panel in sorted(build_historical_feature_panels(level, start_date, end_date).items()):
        run_one_date(level, trade_date, config, output_dir, feature_panel=feature_panel, market_benchmark=benchmark, market_aggregates=aggregates)


def main() -> None:
    """解析 CLI 参数并执行单日或指定区间回填。"""
    parser = argparse.ArgumentParser(description="运行 sector_rotation2 每日板块轮动")
    parser.add_argument("--level", type=int, required=True)
    parser.add_argument("--as-of-date")
    parser.add_argument("--backfill-start")
    parser.add_argument("--backfill-end")
    parser.add_argument("--model-version", default="v1")
    parser.add_argument("--output", default="outputs")
    parser.add_argument("--log-level", default="INFO", choices=("DEBUG", "INFO", "WARNING", "ERROR"), help="终端日志级别")
    args = parser.parse_args()
    logging.basicConfig(level=getattr(logging, args.log_level), format="%(asctime)s %(levelname)-8s %(name)s - %(message)s")
    config = ModelConfig(model_version=args.model_version)
    if args.backfill_start or args.backfill_end:
        if not (args.backfill_start and args.backfill_end):
            parser.error("回填必须同时提供 --backfill-start 和 --backfill-end")
        run_historical_backfill(args.level, args.backfill_start, args.backfill_end, config, args.output)
    elif args.as_of_date:
        run_one_date(args.level, args.as_of_date, config, args.output)
    else:
        parser.error("必须提供 --as-of-date 或完整回填区间")


if __name__ == "__main__":
    main()
