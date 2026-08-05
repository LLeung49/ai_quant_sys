"""生成板块轮动每日晨会文件，不承担数据库写入职责。"""
from __future__ import annotations

from pathlib import Path

import pandas as pd


def write_daily_reports(frame: pd.DataFrame, as_of_date: str, output_dir: str | Path, top_n: int = 10) -> None:
    """在快照成功落库后输出日明细、TopN 摘要和数据质量文件。

    参数:
        frame: 已完成评分、状态和市场状态标注的当日板块 DataFrame。
        as_of_date: 输出所属交易日，用于稳定文件命名。
        output_dir: 输出目录；不存在时自动创建。
        top_n: 文本摘要中保留的最高综合排名数量。
    返回:
        无；成功时写入三个 UTF-8 文件。
    """
    path = Path(output_dir)
    path.mkdir(parents=True, exist_ok=True)
    daily_path = path / f"sector_rotation2_daily_{as_of_date}.csv"
    quality_path = path / f"sector_rotation2_data_quality_{as_of_date}.csv"
    top_path = path / f"sector_rotation2_topN_{as_of_date}.txt"
    export = frame.copy()
    export.index.name = export.index.name or "sector_name"
    export.reset_index().to_csv(daily_path, index=False, encoding="utf-8-sig")
    quality = pd.DataFrame(
        {
            "sector_name": export.index,
            "coverage_ratio": export.get("coverage_ratio"),
            "score_eligible": export.get("score_eligible"),
            "missing_feature_count": export.isna().sum(axis=1),
        }
    )
    quality.to_csv(quality_path, index=False, encoding="utf-8-sig")
    top = export.loc[export.get("score_eligible", pd.Series(False, index=export.index)).fillna(False)]
    top = top.sort_values("composite_rank").head(top_n)
    lines = [f"板块轮动 Top {top_n} | {as_of_date}"]
    for sector_name, row in top.iterrows():
        lines.append(
            f"{int(row['composite_rank'])}. {sector_name} | score={row['composite_score']:.4f} | "
            f"phase={row.get('phase_confirmed', 'neutral')}"
        )
    top_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
