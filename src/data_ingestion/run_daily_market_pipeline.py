"""Run the daily market-data and non-financial research pipeline."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import date, timedelta
import json
import math
import os
from pathlib import Path
import subprocess
import sys
from typing import Sequence

from .market_gap import find_missing_market_codes, write_gap_report


ROOT = Path(__file__).resolve().parents[2]
MARKET_TABLES = (
    "trade_stock_daily_raw",
    "trade_stock_daily_qfq",
    "trade_stock_daily_bfq",
)


@dataclass(frozen=True)
class DailyStep:
    name: str
    argv: tuple[str, ...]
    as_of_date: date

    def as_dict(self) -> dict[str, object]:
        return {
            "name": self.name,
            "as_of_date": self.as_of_date.isoformat(),
            "command": list(self.argv),
        }


def _script(relative_path: str, *args: str) -> tuple[str, ...]:
    return (sys.executable, str(ROOT / relative_path), *args)


def _module(module: str, *args: str) -> tuple[str, ...]:
    return (sys.executable, "-m", module, *args)


def build_market_step(target: date, *, missing_only: bool = False) -> DailyStep:
    return DailyStep(
        name="AKShare 原始行情与复权行情采集",
        as_of_date=target,
        argv=_script(
            "src/data_ingestion/8-原始行情与复权数据采集.py",
            "--start-date",
            (target - timedelta(days=10)).isoformat(),
            "--end-date",
            target.isoformat(),
            *(("--missing-only",) if missing_only else ()),
        ),
    )


def build_downstream_steps(
    target: date, *, include_financial: bool = False, research_backfill: bool = False,
) -> list[DailyStep]:
    day = target.isoformat()
    research_mode = ("--mode", "backfill") if target != date.today() or research_backfill else ()
    steps = [
        DailyStep("申万板块 K 线（二级）", _script("src/morning_conference/sector_rotation/2-run_data_daily.py", "--level", "2"), target),
        DailyStep("申万板块 K 线（一级）", _script("src/morning_conference/sector_rotation/2-run_data_daily.py", "--level", "1"), target),
        DailyStep("形态选股雷达", _script("src/pattern_detection/9-形态选股雷达.py"), target),
        DailyStep("MACD 全市场扫描", _script("src/pattern_detection/10-MACD全市场扫描选股.py"), target),
        DailyStep("短期板块指标（二级）", _module("morning_conference.sector_rotation2.short_term.run_daily", "--as-of-date", day, "--level", "2"), target),
        DailyStep("短期板块指标（一级）", _module("morning_conference.sector_rotation2.short_term.run_daily", "--as-of-date", day, "--level", "1"), target),
        DailyStep("中期板块指标（二级）", _module("morning_conference.sector_rotation2.run_daily", "--as-of-date", day, "--level", "2"), target),
        DailyStep("中期板块指标（一级）", _module("morning_conference.sector_rotation2.run_daily", "--as-of-date", day, "--level", "1"), target),
        DailyStep("MACD 标的池", _module("morning_conference.sector_rotation2.run_macd_daily", "--as-of-date", day), target),
        DailyStep("板块机会快照", _module("morning_conference.sector_rotation2.research.orchestrator.run_daily", "--as-of-date", day, "--level", "2", *research_mode), target),
        DailyStep("ETF 候选快照", _module("morning_conference.sector_rotation2.research.etf_core.run_daily", "--as-of-date", day, "--level", "2", *research_mode), target),
        DailyStep("趋势个股候选", _module("morning_conference.sector_rotation2.research.stock_alpha.run_trend_daily", "--as-of-date", day, "--level", "2", *research_mode), target),
    ]
    if include_financial:
        steps.append(DailyStep(
            "AKShare 财务与 Repair Alpha",
            _module("data_ingestion.run_daily_pipeline", "--as-of-date", day,
                    "--mode", "live_shadow"), target,
        ))
    return steps


def market_date_issue(target: date) -> str | None:
    """Reject absent, divergent, or invalid daily price projections."""
    from .db_config import execute_query

    expected_codes: set[str] | None = None
    for table in MARKET_TABLES:
        rows = execute_query(
            f"SELECT stock_code, open_price, high_price, low_price, close_price "
            f"FROM {table} WHERE trade_date = %s",
            (target.isoformat(),),
        )
        if not rows:
            return f"{table} 在 {target} 没有行情数据"
        codes = {row["stock_code"] for row in rows}
        if len(codes) != len(rows):
            return f"{table} 在 {target} 存在重复证券代码"
        if expected_codes is not None and codes != expected_codes:
            return f"{table} 在 {target} 与 raw 表的证券代码集合不一致"
        for row in rows:
            try:
                open_, high, low, close = (
                    float(row[column])
                    for column in ("open_price", "high_price", "low_price", "close_price")
                )
            except (TypeError, ValueError, KeyError):
                return f"{table} 在 {target} 的 {row['stock_code']} 存在无效价格"
            if not all(math.isfinite(price) and price > 0 for price in (open_, high, low, close)) or high < max(open_, low, close) or low > min(open_, high, close):
                return f"{table} 在 {target} 的 {row['stock_code']} 存在无效 OHLC"
        if expected_codes is None:
            expected_codes = codes
    return None


def refresh_research_backfill(target: date) -> int:
    """Replace only price-dependent backfill snapshots for one target day."""
    from .db_config import get_connection

    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "DELETE FROM research_candidate_snapshot "
                "WHERE as_of_date=%s AND snapshot_mode='backfill' "
                "AND strategy_type IN ('sector_opportunity','etf_core','stock_trend')",
                (target.isoformat(),),
            )
            deleted = cursor.rowcount
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
    print(f"[每日补采] 清理 {target} 旧 backfill 研究候选 {deleted} 条，准备重算", flush=True)
    return deleted


def run_steps(steps: Sequence[DailyStep]) -> int:
    env = os.environ.copy()
    src_path = str(ROOT / "src")
    env["PYTHONPATH"] = src_path + os.pathsep + env.get("PYTHONPATH", "")
    for index, step in enumerate(steps, start=1):
        print(f"[{index}/{len(steps)}] {step.name} ({step.as_of_date.isoformat()})", flush=True)
        completed = subprocess.run(step.argv, cwd=ROOT, env=env, check=False)
        if completed.returncode != 0:
            print(f"[每日任务失败] {step.name}: exit={completed.returncode}", file=sys.stderr, flush=True)
            return completed.returncode
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="AKShare 行情及非财务研究每日任务")
    parser.add_argument("--as-of-date", type=date.fromisoformat)
    parser.add_argument("--skip-market-collection", action="store_true")
    parser.add_argument("--retry-missing-market", action="store_true", help="Only fetch codes missing the target date, then refresh downstream if coverage improves")
    parser.add_argument("--include-financial", action="store_true",
                        help="当日行情与研究通过后，再运行 AKShare 财务采集和 Repair Alpha")
    parser.add_argument("--plan", action="store_true", help="输出任务计划，不执行命令或访问数据库")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    requested_date = args.as_of_date or date.today()
    if args.retry_missing_market and (args.as_of_date is None or args.skip_market_collection):
        print("[每日任务失败] --retry-missing-market requires --as-of-date and cannot combine with --skip-market-collection", file=sys.stderr)
        return 2
    if args.include_financial and requested_date != date.today():
        print("[每日任务失败] 财务增量只能以当天为目标；历史财务数据须用归档回补", file=sys.stderr)
        return 2

    if args.plan:
        steps = [] if args.skip_market_collection else [build_market_step(requested_date, missing_only=args.retry_missing_market)]
        steps.extend(build_downstream_steps(requested_date, include_financial=args.include_financial, research_backfill=args.retry_missing_market))
        print(json.dumps([step.as_dict() for step in steps], ensure_ascii=False, indent=2))
        return 0

    missing_before: list[str] = []
    if args.retry_missing_market:
        prior_before, missing_before = find_missing_market_codes(requested_date)
        if not missing_before:
            print(f"[每日补采] {requested_date} 无待补代码，继续刷新下游以完成可能中断的任务", flush=True)
        else:
            write_gap_report(requested_date, prior_before, missing_before, ROOT / "outputs")
    if not args.skip_market_collection and (not args.retry_missing_market or missing_before):
        rc = run_steps([build_market_step(requested_date, missing_only=args.retry_missing_market)])
        if rc != 0:
            prior, missing_after = find_missing_market_codes(requested_date)
            write_gap_report(requested_date, prior, missing_after, ROOT / "outputs")
            return rc

    prior, missing_after = find_missing_market_codes(requested_date)
    gap_path = write_gap_report(requested_date, prior, missing_after, ROOT / "outputs")
    if missing_after:
        print(
            f"[行情缺口] {requested_date} 较 {prior} 有 {len(missing_after)} 只缺少目标日行情；"
            f"清单：{gap_path}。下游只使用有当日 K 线的标的；稍后运行 "
            f"run_daily_once.ps1 -AsOfDate {requested_date} -RetryMissingMarket 补采",
            flush=True,
        )
    if args.retry_missing_market and missing_before and not (set(missing_before) - set(missing_after)):
        print("[每日补采] 本次没有新增目标日行情，跳过下游重算；可稍后再试", flush=True)
        return 0

    target = requested_date
    issue = market_date_issue(target)
    if issue is not None:
        print(f"[每日任务失败] 行情验收未通过：{issue}", file=sys.stderr, flush=True)
        return 1
    print(f"[每日任务] 下游计算交易日：{target.isoformat()}", flush=True)
    steps = build_downstream_steps(
        target, include_financial=args.include_financial,
        research_backfill=bool(missing_after) or args.retry_missing_market,
    )
    if args.retry_missing_market:
        # Rebuild mutable derivatives first. Preserve old research snapshots if
        # an upstream step fails; only then replace the scoped backfill rows.
        rc = run_steps(steps[:9])
        if rc != 0:
            return rc
        refresh_research_backfill(target)
        return run_steps(steps[9:])
    return run_steps(steps)


if __name__ == "__main__":
    raise SystemExit(main())
