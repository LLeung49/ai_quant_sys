"""v2_short_term 的只读数据访问层。

与 v1 的 ``SectorRotationRepository`` 对齐，但只读取新表
``sector_rotation_short_term_daily_snapshot``。任何 SQL 都使用参数化占位符。
"""
from __future__ import annotations

from typing import Any, Final

from data_ingestion.db_config import execute_query


MAX_SHORT_TERM_SECTORS: Final[int] = 5
SHORT_TERM_LABEL_WHITELIST: Final[tuple[str, ...]] = (
    "pulse_up", "pulse_down",
    "volume_spike",
    "limit_cluster", "limit_panic",
    "extreme_up", "extreme_down",
    "short_rebound_candidate", "short_breakdown_candidate",
)
SHORT_TERM_INTENSITY_WHITELIST: Final[tuple[str, ...]] = ("intense", "moderate", "mild")


class ShortTermRepository:
    """短期异动研究的只读查询。"""

    @staticmethod
    def _validate_level(sector_level: int) -> None:
        if sector_level not in (1, 2):
            raise ValueError("行业层级只能为 1 或 2")

    def load_snapshot(
        self,
        as_of_date: str,
        sector_level: int,
        model_version: str,
    ) -> list[dict[str, Any]]:
        """读取一个成功运行日的全板块短期快照。"""
        self._validate_level(sector_level)
        sql = """
            SELECT s.*,
                   r.source_max_trade_date AS _source_max_trade_date,
                   r.eligible_sector_count AS _eligible_sector_count,
                   r.skipped_sector_count AS _skipped_sector_count
            FROM sector_rotation_short_term_daily_snapshot AS s
            INNER JOIN sector_rotation_run_log AS r ON r.run_id = s.run_id
            WHERE r.status = %s
              AND s.as_of_date = %s
              AND s.sector_level = %s
              AND s.model_version = %s
            ORDER BY s.short_term_composite_rank IS NULL, s.short_term_composite_rank, s.sector_name
        """
        return list(execute_query(sql, ("succeeded", as_of_date, sector_level, model_version)))

    def load_history(
        self,
        sector_names: list[str],
        start_date: str,
        end_date: str,
        sector_level: int,
        model_version: str,
    ) -> list[dict[str, Any]]:
        """读取最多 5 个板块的短期历史轨迹。"""
        self._validate_level(sector_level)
        if not 1 <= len(sector_names) <= MAX_SHORT_TERM_SECTORS:
            raise ValueError(f"最多只能查询 {MAX_SHORT_TERM_SECTORS} 个板块")
        placeholders = ", ".join(["%s"] * len(sector_names))
        sql = f"""
            SELECT s.*,
                   r.source_max_trade_date AS _source_max_trade_date,
                   r.eligible_sector_count AS _eligible_sector_count,
                   r.skipped_sector_count AS _skipped_sector_count
            FROM sector_rotation_short_term_daily_snapshot AS s
            INNER JOIN sector_rotation_run_log AS r ON r.run_id = s.run_id
            WHERE r.status = %s
              AND s.as_of_date BETWEEN %s AND %s
              AND s.sector_level = %s
              AND s.model_version = %s
              AND s.sector_name IN ({placeholders})
            ORDER BY s.as_of_date, s.sector_name
        """
        params: tuple[Any, ...] = ("succeeded", start_date, end_date, sector_level, model_version, *sector_names)
        return list(execute_query(sql, params))

    def list_available_dates(self, sector_level: int, model_version: str) -> list[str]:
        """返回短期异动快照可用的交易日列表。"""
        self._validate_level(sector_level)
        sql = """
            SELECT DISTINCT r.as_of_date
            FROM sector_rotation_run_log AS r
            WHERE r.status = %s AND r.sector_level = %s AND r.model_version = %s
            ORDER BY r.as_of_date DESC
        """
        rows = execute_query(sql, ("succeeded", sector_level, model_version))
        return [str(row["as_of_date"]) for row in rows]

    @staticmethod
    def parse_label_filter(raw_labels: list[str] | None) -> list[str]:
        """校验并标准化 labels 过滤参数。"""
        if not raw_labels:
            return []
        invalid = [label for label in raw_labels if label not in SHORT_TERM_LABEL_WHITELIST]
        if invalid:
            raise ValueError(f"未知短期异动标签: {invalid}")
        return raw_labels

    @staticmethod
    def parse_intensity_filter(min_intensity: str | None) -> str | None:
        """校验最低强度过滤参数。"""
        if not min_intensity:
            return None
        if min_intensity not in SHORT_TERM_INTENSITY_WHITELIST:
            raise ValueError(f"未知强度等级: {min_intensity}")
        return min_intensity
