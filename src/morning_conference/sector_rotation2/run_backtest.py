"""生成前瞻标签并输出基础因子研究结果的命令入口。"""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from data_ingestion.db_config import execute_query

from .backtest import build_forward_return_labels, evaluate_factor
from .snapshot_store import persist_forward_returns


def run_research(level: int, start_date: str, end_date: str, model_version: str, output_dir: str | Path) -> pd.DataFrame:
    """构建标签、持久化并对 composite_score 输出 5/10 日基础评估。

    参数:
        level: 板块层级。
        start_date: 研究样本起始日。
        end_date: 研究样本结束日。
        model_version: 快照模型版本。
        output_dir: 研究 CSV 输出目录。
    返回:
        每个预测周期一行的基础指标 DataFrame。
    """
    labels = build_forward_return_labels(level, start_date, end_date)
    persist_forward_returns(labels, level)
    snapshots = execute_query(
        "SELECT as_of_date, sector_name, composite_score FROM sector_rotation_sector_daily_snapshot "
        "WHERE sector_level = %s AND model_version = %s AND as_of_date BETWEEN %s AND %s",
        (level, model_version, start_date, end_date),
    )
    metrics = []
    for horizon in (5, 10):
        result = evaluate_factor(snapshots, labels, "composite_score", horizon)
        result["horizon"] = horizon
        metrics.append(result)
    output = pd.DataFrame(metrics)
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    output.to_csv(Path(output_dir) / f"sector_rotation2_research_{end_date}.csv", index=False, encoding="utf-8-sig")
    return output


def main() -> None:
    """解析研究 CLI 参数并运行指定样本区间。"""
    parser = argparse.ArgumentParser(description="运行 sector_rotation2 基础研究")
    parser.add_argument("--level", type=int, required=True)
    parser.add_argument("--start-date", required=True)
    parser.add_argument("--end-date", required=True)
    parser.add_argument("--model-version", default="v1")
    parser.add_argument("--output", default="outputs")
    args = parser.parse_args()
    run_research(args.level, args.start_date, args.end_date, args.model_version, args.output)


if __name__ == "__main__":
    main()
