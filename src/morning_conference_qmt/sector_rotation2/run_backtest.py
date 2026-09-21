"""生成前瞻标签并输出基础因子研究结果的命令入口。"""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from data_ingestion_qmt.db_config import execute_query

from .backtest import (
    DEFAULT_ALPHA_DECAY_HORIZONS,
    build_forward_return_labels,
    evaluate_by_regime,
    evaluate_factor,
    evaluate_lifecycle_score_bucket_oos,
    evaluate_lifecycle_score_buckets,
    evaluate_lifecycle_states,
    evaluate_rolling_oos,
    rolling_oos_windows,
    simulate_top_group_strategy,
)
from .lifecycle import rebuild_lifecycle_history_v0
from .snapshot_store import persist_forward_returns


def run_research(level: int, start_date: str, end_date: str, model_version: str, output_dir: str | Path) -> pd.DataFrame:
    """构建标签、持久化并输出 Score Alpha Decay 研究结果。

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
    labels["as_of_date"] = pd.to_datetime(labels["as_of_date"])
    labels["target_date"] = pd.to_datetime(labels["target_date"])
    persist_forward_returns(labels, level)
    snapshots = pd.DataFrame(execute_query(
        "SELECT as_of_date, sector_name, composite_score, market_regime, score_eligible, phase_raw, phase_confirmed, "
        "participation_score, rank_change_1d, top10_days_20 FROM sector_rotation_sector_daily_snapshot "
        "WHERE sector_level = %s AND model_version = %s AND as_of_date BETWEEN %s AND %s",
        (level, model_version, start_date, end_date),
    ))
    snapshots["as_of_date"] = pd.to_datetime(snapshots["as_of_date"])
    lifecycle_required_columns = {
        "score_eligible", "phase_raw", "phase_confirmed", "participation_score", "rank_change_1d", "top10_days_20",
    }
    if "lifecycle_state" in snapshots:
        lifecycle_snapshots = snapshots
    elif lifecycle_required_columns.issubset(snapshots):
        lifecycle_snapshots = rebuild_lifecycle_history_v0(snapshots)
    else:
        lifecycle_snapshots = pd.DataFrame()
    metrics = []
    for horizon in DEFAULT_ALPHA_DECAY_HORIZONS:
        result = evaluate_factor(snapshots, labels, "composite_score", horizon)
        result.update({"horizon": horizon, "factor": "composite_score", "window_name": "full_sample"})
        metrics.append(result)
        regime_metrics = evaluate_by_regime(snapshots, labels, "composite_score", horizon)
        if not regime_metrics.empty:
            regime_metrics["horizon"] = horizon
            regime_metrics["factor"] = "composite_score"
            regime_metrics["window_name"] = "regime_bucket"
            metrics.extend(regime_metrics.to_dict("records"))
    # 固化滚动样本外窗口边界，后续报告可据此复现验证区间，且不自动调权。
    oos_windows = rolling_oos_windows(pd.to_datetime(snapshots["as_of_date"].unique())) if not snapshots.empty else []
    for horizon in DEFAULT_ALPHA_DECAY_HORIZONS:
        if oos_windows:
            metrics.extend(
                evaluate_rolling_oos(snapshots, labels, "composite_score", horizon, oos_windows).to_dict("records")
            )
    for rebalance_every in (1, 2, 3, 5):
        for cost_bps in (0, 5, 10, 20):
            metrics.append({
                "window_name": "cost_sensitivity",
                "factor": "composite_score",
                "horizon": 1,
                "rebalance_every": rebalance_every,
                "cost_bps": cost_bps,
                **simulate_top_group_strategy(snapshots, labels, "composite_score", rebalance_every, cost_bps),
            })
    output = pd.DataFrame(metrics)
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    output.to_csv(Path(output_dir) / f"sector_rotation2_research_{end_date}.csv", index=False, encoding="utf-8-sig")
    if "lifecycle_state" in lifecycle_snapshots:
        lifecycle = pd.concat(
            [evaluate_lifecycle_states(lifecycle_snapshots, labels, horizon).assign(horizon=horizon)
             for horizon in DEFAULT_ALPHA_DECAY_HORIZONS],
            ignore_index=True,
        )
        lifecycle.to_csv(Path(output_dir) / f"sector_rotation2_lifecycle_{end_date}.csv", index=False, encoding="utf-8-sig")
        lifecycle_score_bucket_frames = [
            evaluate_lifecycle_score_buckets(lifecycle_snapshots, labels, horizon).assign(horizon=horizon)
            for horizon in DEFAULT_ALPHA_DECAY_HORIZONS
        ]
        if oos_windows:
            lifecycle_score_bucket_frames.extend(
                evaluate_lifecycle_score_bucket_oos(lifecycle_snapshots, labels, horizon, oos_windows)
                for horizon in DEFAULT_ALPHA_DECAY_HORIZONS
            )
        lifecycle_score_buckets = pd.concat(lifecycle_score_bucket_frames, ignore_index=True)
        lifecycle_score_buckets.to_csv(
            Path(output_dir) / f"sector_rotation2_lifecycle_score_buckets_{end_date}.csv",
            index=False,
            encoding="utf-8-sig",
        )
    pd.DataFrame(oos_windows).to_csv(Path(output_dir) / f"sector_rotation2_oos_windows_{end_date}.csv", index=False, encoding="utf-8-sig")
    _write_alpha_decay_report(output, level, start_date, end_date, model_version, Path(output_dir))
    return output


def _write_alpha_decay_report(
    metrics: pd.DataFrame,
    level: int,
    start_date: str,
    end_date: str,
    model_version: str,
    output_dir: Path,
) -> None:
    """将研究指标输出为披露数据限制的 Markdown 报告。"""
    full_sample = metrics.loc[metrics.get("window_name", pd.Series(dtype=str)) == "full_sample"]
    lines = [
        "# Sector Rotation2 Score Alpha Decay 研究报告",
        "",
        "## 运行口径",
        "",
        f"- 模型版本：`{model_version}`",
        f"- 行业层级：`{level}`",
        f"- 研究区间：`{start_date}` 至 `{end_date}`",
        "- 预测期限：`1/2/3/5/10/20/40` 个交易日",
        "- 成员映射口径：`current_mapping`；历史结果未使用严格历史行业成分。",
        "- 本报告仅用于研究，不产生交易指令，也不构成收益承诺。",
        "",
        "## 全样本 Score 指标",
        "",
    ]
    if full_sample.empty:
        lines.append("无可评估的成熟标签。")
    else:
        lines.extend(["| 期限 | Rank IC | ICIR | Top-Bottom | 样本数 |", "| --- | ---: | ---: | ---: | ---: |"])
        for row in full_sample.sort_values("horizon").itertuples(index=False):
            lines.append(
                f"| {row.horizon}D | {getattr(row, 'rank_ic_mean', float('nan')):.6f} | "
                f"{getattr(row, 'icir', float('nan')):.6f} | {getattr(row, 'top_bottom_return', float('nan')):.6f} | "
                f"{getattr(row, 'sample_count', 0)} |"
            )
    lines.extend([
        "",
        "## 研究边界",
        "",
        "- 市场状态分桶、滚动样本外指标和成本敏感性详见同目录 CSV。",
        "- P1 不修改 Sector Score，不接入 Lifecycle 仓位规则，不执行 ETF 下单。",
    ])
    (output_dir / f"sector_rotation2_alpha_decay_{end_date}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


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

