"""板块轮动可视化的只读数据访问层。

本文件引用 ``sector_rotation2.snapshot_store`` 中已确认的快照表和运行审计表，
但不复用写入逻辑。新增优化点是只读取成功运行、集中校验请求边界，并始终使用参数化 SQL。
"""

from __future__ import annotations

from typing import Any, Final

from data_ingestion.db_config import execute_query


# 行业轨迹接口的统一查询上限。路由层和仓储层共同使用该常量，既给用户明确反馈，
# 也防止绕过 HTTP 层后形成无界 IN 查询。
MAX_HISTORY_SECTORS: Final[int] = 5
# 板块 K 线接口固定返回最近 350 根候选日线，避免无界查询。
KLINE_BAR_LIMIT: Final[int] = 350


class SectorRotationRepository:
    """封装板块轮动可视化所需的只读查询。

    输入：经 HTTP 层初步校验的日期、行业层级、模型版本和行业名称。
    输出：保持数据库 NULL 的字典行列表；本类不计算指标、不写入数据库。
    """

    @staticmethod
    def _validate_level(sector_level: int) -> None:
        """校验行业层级。

        输入：请求的申万行业层级。
        输出：合法时无返回值；不为 1 或 2 时抛出 ``ValueError``。
        """
        if sector_level not in (1, 2):
            raise ValueError("行业层级只能为 1 或 2")

    def load_snapshot(self, as_of_date: str, sector_level: int, model_version: str) -> list[dict[str, Any]]:
        """读取一个成功运行日的全行业快照。

        输入：交易日、行业层级和模型版本。
        输出：按综合排名和行业名称排序的快照字典列表；数据库空值原样保留为 ``None``。
        """
        self._validate_level(sector_level)
        sql = """
            SELECT s.*,
                   r.source_max_trade_date AS _source_max_trade_date,
                   r.eligible_sector_count AS _eligible_sector_count,
                   r.skipped_sector_count AS _skipped_sector_count
            FROM sector_rotation_sector_daily_snapshot AS s
            INNER JOIN sector_rotation_run_log AS r ON r.run_id = s.run_id
            WHERE r.status = %s
              AND s.as_of_date = %s
              AND s.sector_level = %s
              AND s.model_version = %s
            ORDER BY s.composite_rank IS NULL, s.composite_rank, s.sector_name
        """
        return list(execute_query(sql, ("succeeded", as_of_date, sector_level, model_version)))

    def load_sector_kline(
        self, sector_name: str, sector_level: int, end_date: str
    ) -> list[dict[str, Any]]:
        """读取指定截止日前最近 350 根板块合成日线。

        参数:
            sector_name: 完整行业名称，不做模糊匹配。
            sector_level: 申万行业层级，只允许 1 或 2。
            end_date: ISO 截止日期；查询不得返回该日之后的数据。
        返回:
            按交易日升序的 OHLCV/成交额候选行；不在仓储层修复坏数据。
        异常:
            ValueError: 当行业层级不是 1 或 2 时抛出。
        """
        self._validate_level(sector_level)
        # 内层先倒序截取最近 350 根，外层再升序以满足 K 线图时间轴。
        sql = """
            SELECT trade_date, open, high, low, close, volume, amount
            FROM (
                SELECT trade_date,
                       open_idx AS open, high_idx AS high, low_idx AS low,
                       close_idx AS close, total_volume AS volume, total_amount AS amount
                FROM trade_sector_daily
                WHERE sector_name = %s AND sector_level = %s AND trade_date <= %s
                ORDER BY trade_date DESC
                LIMIT %s
            ) AS recent_bars
            ORDER BY trade_date ASC
        """
        return list(execute_query(sql, (sector_name, sector_level, end_date, KLINE_BAR_LIMIT)))

    def load_sector_wave_prices(
        self, sector_name: str, sector_level: int, trade_dates: list[str]
    ) -> list[dict[str, Any]]:
        """一次读取 K 线窗口内全部波段边界日的当前行业成分股前复权收盘价。"""
        self._validate_level(sector_level)
        if not trade_dates:
            return []
        if len(trade_dates) > KLINE_BAR_LIMIT or len(set(trade_dates)) != len(trade_dates):
            raise ValueError("波段边界日期必须唯一且不超过 K 线窗口长度")
        field = "sector_1" if sector_level == 1 else "sector_2"
        placeholders = ", ".join(["%s"] * len(trade_dates))
        sql = f"""
            SELECT daily.stock_code, status.stock_name, daily.trade_date,
                   daily.close_price AS close
            FROM trade_stock_daily_qfq AS daily
            INNER JOIN trade_stock_status AS status ON status.stock_code = daily.stock_code
            WHERE status.{field} = %s AND daily.trade_date IN ({placeholders})
            ORDER BY daily.stock_code, daily.trade_date
        """
        return list(execute_query(sql, (sector_name, *trade_dates)))

    def load_etf_kline(self, stock_code: str, end_date: str) -> list[dict[str, Any]]:
        """Read the latest bounded set of forward-adjusted ETF daily bars."""
        sql = """
            SELECT trade_date, open, high, low, close, volume, amount
            FROM (
                SELECT trade_date, open_price AS open, high_price AS high,
                       low_price AS low, close_price AS close, volume, amount
                FROM trade_stock_daily_qfq
                WHERE stock_code = %s AND trade_date <= %s
                ORDER BY trade_date DESC
                LIMIT %s
            ) AS recent_bars
            ORDER BY trade_date ASC
        """
        return list(execute_query(sql, (stock_code, end_date, KLINE_BAR_LIMIT)))

    def list_available_dates(self, sector_level: int, model_version: str) -> list[str]:
        """读取存在成功快照的可选交易日。

        输入：行业层级与模型版本。
        输出：按日期倒序排列且去重的 ISO 日期字符串列表。
        """
        self._validate_level(sector_level)
        sql = """
            SELECT DISTINCT r.as_of_date
            FROM sector_rotation_run_log AS r
            WHERE r.status = %s AND r.sector_level = %s AND r.model_version = %s
            ORDER BY r.as_of_date DESC
        """
        rows = execute_query(sql, ("succeeded", sector_level, model_version))
        return [str(row["as_of_date"]) for row in rows]

    def load_calendar_availability(
        self,
        sector_level: int,
        model_version: str,
        start_date: str,
        end_date: str,
    ) -> tuple[list[str], list[str]]:
        """Return upstream trading dates and successful snapshot dates in one bounded range.

        Trading dates come directly from ``trade_sector_daily`` so that a date with
        upstream market data remains visible even before a sector-rotation snapshot
        has been generated. Snapshot dates remain a separate, successful-run-only
        set and are never used to infer the upstream calendar.
        """
        self._validate_level(sector_level)
        if start_date > end_date:
            raise ValueError("开始日期不能晚于结束日期")

        trade_date_sql = """
            SELECT DISTINCT trade_date
            FROM trade_sector_daily
            WHERE sector_level = %s
              AND trade_date BETWEEN %s AND %s
            ORDER BY trade_date ASC
        """
        snapshot_date_sql = """
            SELECT DISTINCT s.as_of_date
            FROM sector_rotation_sector_daily_snapshot AS s
            INNER JOIN sector_rotation_run_log AS r ON r.run_id = s.run_id
            WHERE r.status = %s
              AND s.as_of_date BETWEEN %s AND %s
              AND s.sector_level = %s
              AND s.model_version = %s
            ORDER BY s.as_of_date ASC
        """
        trade_rows = execute_query(trade_date_sql, (sector_level, start_date, end_date))
        snapshot_rows = execute_query(
            snapshot_date_sql,
            ("succeeded", start_date, end_date, sector_level, model_version),
        )
        return (
            [str(row["trade_date"]) for row in trade_rows],
            [str(row["as_of_date"]) for row in snapshot_rows],
        )

    def load_sector_history(
        self,
        sector_names: list[str],
        start_date: str,
        end_date: str,
        sector_level: int,
        model_version: str,
    ) -> list[dict[str, Any]]:
        """读取最多五个行业的连续历史快照。

        输入：行业名称列表、闭区间日期范围、行业层级与模型版本。
        输出：按日期和行业排序的已成功运行快照；超过五个行业时抛出 ``ValueError``。
        """
        self._validate_level(sector_level)
        if not 1 <= len(sector_names) <= MAX_HISTORY_SECTORS:
            raise ValueError(f"最多只能查询 {MAX_HISTORY_SECTORS} 个行业，且至少选择 1 个行业")
        placeholders = ", ".join(["%s"] * len(sector_names))
        sql = f"""
            SELECT s.*,
                   r.source_max_trade_date AS _source_max_trade_date,
                   r.eligible_sector_count AS _eligible_sector_count,
                   r.skipped_sector_count AS _skipped_sector_count
            FROM sector_rotation_sector_daily_snapshot AS s
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

    def load_replay(self, start_date: str, end_date: str, sector_level: int, model_version: str) -> list[dict[str, Any]]:
        """读取指定区间内全部行业的历史回放快照。

        输入：闭区间日期范围、行业层级与模型版本。
        输出：按交易日和行业名称排序的成功快照列表；供前端预加载后本地逐帧播放。
        """
        self._validate_level(sector_level)
        if start_date > end_date:
            raise ValueError("开始日期不能晚于结束日期")
        sql = """
            SELECT s.*,
                   r.source_max_trade_date AS _source_max_trade_date,
                   r.eligible_sector_count AS _eligible_sector_count,
                   r.skipped_sector_count AS _skipped_sector_count
            FROM sector_rotation_sector_daily_snapshot AS s
            INNER JOIN sector_rotation_run_log AS r ON r.run_id = s.run_id
            WHERE r.status = %s
              AND s.as_of_date BETWEEN %s AND %s
              AND s.sector_level = %s
              AND s.model_version = %s
            ORDER BY s.as_of_date, s.sector_name
        """
        return list(execute_query(sql, ("succeeded", start_date, end_date, sector_level, model_version)))
