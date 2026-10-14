"""Transactional, staging-only persistence for market-layer reconstruction."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import json
from typing import Callable

from .db_config import get_connection
from .market_provider import MarketBatch
from .market_row_validation import validate_projection_batch


STAGING_TABLE_BY_MODE = {
    "none": "trade_stock_daily_raw_rebuild",
    "front": "trade_stock_daily_qfq_rebuild",
    "back": "trade_stock_daily_bfq_rebuild",
}

RAW_UPSERT = """
INSERT INTO trade_stock_daily_raw_rebuild
    (stock_code, trade_date, open_price, high_price, low_price, close_price,
     volume, amount, pre_close, suspend_flag, data_source,
     rebuild_batch_id, rebuild_source, rebuild_fetched_at, rebuild_fingerprint,
     rebuild_validation_status)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 'valid')
ON DUPLICATE KEY UPDATE
    open_price=VALUES(open_price), high_price=VALUES(high_price),
    low_price=VALUES(low_price), close_price=VALUES(close_price),
    volume=VALUES(volume), amount=VALUES(amount), pre_close=VALUES(pre_close),
    suspend_flag=VALUES(suspend_flag), data_source=VALUES(data_source),
    rebuild_batch_id=VALUES(rebuild_batch_id), rebuild_source=VALUES(rebuild_source),
    rebuild_fetched_at=VALUES(rebuild_fetched_at),
    rebuild_fingerprint=VALUES(rebuild_fingerprint),
    rebuild_validation_status=VALUES(rebuild_validation_status),
    updated_at=CURRENT_TIMESTAMP
"""

ADJUSTED_UPSERT_BY_MODE = {
    mode: f"""
INSERT INTO {table}
    (stock_code, trade_date, open_price, high_price, low_price, close_price,
     volume, amount, turnover_rate, adjustment_asof,
     rebuild_batch_id, rebuild_source, rebuild_fetched_at, rebuild_fingerprint,
     rebuild_validation_status)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 'valid')
ON DUPLICATE KEY UPDATE
    open_price=VALUES(open_price), high_price=VALUES(high_price),
    low_price=VALUES(low_price), close_price=VALUES(close_price),
    volume=VALUES(volume), amount=VALUES(amount),
    turnover_rate=VALUES(turnover_rate), adjustment_asof=VALUES(adjustment_asof),
    rebuild_batch_id=VALUES(rebuild_batch_id), rebuild_source=VALUES(rebuild_source),
    rebuild_fetched_at=VALUES(rebuild_fetched_at),
    rebuild_fingerprint=VALUES(rebuild_fingerprint),
    rebuild_validation_status=VALUES(rebuild_validation_status),
    refreshed_at=CURRENT_TIMESTAMP
"""
    for mode, table in STAGING_TABLE_BY_MODE.items()
    if mode != "none"
}

START_BATCH_SQL = """
INSERT INTO trade_market_rebuild_batch
    (batch_id, stock_code, start_date, end_date, status, source, fingerprint,
     raw_rows, qfq_rows, hfq_rows, gap_count, error_detail, started_at)
VALUES (%s, %s, %s, %s, 'running', %s, %s, 0, 0, 0, 0, NULL, CURRENT_TIMESTAMP)
ON DUPLICATE KEY UPDATE
    status='running', source=VALUES(source), fingerprint=VALUES(fingerprint),
    error_detail=NULL, started_at=CURRENT_TIMESTAMP, completed_at=NULL
"""

COMPLETE_BATCH_SQL = """
UPDATE trade_market_rebuild_batch
SET status = 'complete', raw_rows=%s, qfq_rows=%s, hfq_rows=%s,
    gap_count=%s, completed_at=CURRENT_TIMESTAMP
WHERE batch_id=%s AND stock_code=%s
"""

GAP_UPSERT_SQL = """
INSERT INTO trade_market_rebuild_gap
    (batch_id, stock_code, trade_date, price_mode, reason, detail)
VALUES (%s, %s, %s, %s, %s, %s)
ON DUPLICATE KEY UPDATE reason=VALUES(reason), detail=VALUES(detail)
"""

FAIL_BATCH_SQL = """
INSERT INTO trade_market_rebuild_batch
    (batch_id, stock_code, start_date, end_date, status, source, fingerprint,
     raw_rows, qfq_rows, hfq_rows, gap_count, error_detail, started_at)
VALUES (%s, %s, %s, %s, 'failed', %s, NULL, 0, 0, 0, 0, %s, CURRENT_TIMESTAMP)
ON DUPLICATE KEY UPDATE
    status='failed', source=VALUES(source), error_detail=VALUES(error_detail),
    completed_at=NULL
"""


@dataclass(frozen=True)
class PersistResult:
    stock_code: str
    rows_written: int
    gaps_recorded: int
    fingerprint: str


class RebuildStore:
    def __init__(
        self,
        connection_factory: Callable = get_connection,
        *,
        batch_id: str,
    ) -> None:
        if not batch_id:
            raise ValueError("batch_id is required")
        self.connection_factory = connection_factory
        self.batch_id = batch_id

    @staticmethod
    def table_for_mode(mode: str) -> str:
        try:
            return STAGING_TABLE_BY_MODE[mode]
        except KeyError as exc:
            raise ValueError(f"unsupported rebuild mode: {mode}") from exc

    def completed_codes(self) -> set[str]:
        conn = self.connection_factory()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "SELECT stock_code FROM trade_market_rebuild_batch "
                "WHERE batch_id=%s AND status='complete'",
                (self.batch_id,),
            )
            return {str(row[0]) for row in cursor.fetchall()}
        finally:
            cursor.close()
            conn.close()

    def record_failure(
        self,
        stock_code: str,
        start_date,
        end_date,
        source: str,
        error_detail: str,
    ) -> None:
        conn = self.connection_factory()
        cursor = conn.cursor()
        try:
            cursor.execute(
                FAIL_BATCH_SQL,
                (
                    self.batch_id, stock_code, start_date, end_date,
                    source, error_detail[:65535],
                ),
            )
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            cursor.close()
            conn.close()

    def persist_validated_batch(self, batch: MarketBatch) -> PersistResult:
        if not batch.is_complete:
            raise ValueError(
                f"incomplete market batch for {batch.stock_code}: {batch.failures}"
            )
        validation = validate_projection_batch(batch.rows_by_mode)
        if not validation.is_valid:
            reasons = [issue.code for issue in validation.issues if issue.severity == "error"]
            raise ValueError(f"invalid market batch for {batch.stock_code}: {reasons}")

        fingerprint = str(batch.provenance.get("fingerprint") or hashlib.sha256(
            json.dumps(batch.rows_by_mode, sort_keys=True, default=str).encode("utf-8")
        ).hexdigest())
        source = str(batch.provenance.get("provider", "unknown"))
        fetched_at = batch.provenance.get("fetched_at") or datetime.now(timezone.utc)
        conn = self.connection_factory()
        cursor = conn.cursor()
        rows_written = 0
        try:
            cursor.execute(
                START_BATCH_SQL,
                (
                    self.batch_id, batch.stock_code, batch.start_date, batch.end_date,
                    source, fingerprint,
                ),
            )
            raw_values = [
                (
                    row["stock_code"], row["trade_date"], row["open_price"],
                    row["high_price"], row["low_price"], row["close_price"],
                    row["volume"], row["amount"], row.get("pre_close"),
                    row.get("suspend_flag"), row.get("data_source", source),
                    self.batch_id, source, fetched_at, fingerprint,
                )
                for row in batch.rows_by_mode["none"]
            ]
            rows_written += cursor.executemany(RAW_UPSERT, raw_values) or 0
            for mode in ("front", "back"):
                values = [
                    (
                        row["stock_code"], row["trade_date"], row["open_price"],
                        row["high_price"], row["low_price"], row["close_price"],
                        row["volume"], row["amount"], row.get("turnover_rate"),
                        batch.end_date, self.batch_id, source, fetched_at, fingerprint,
                    )
                    for row in batch.rows_by_mode[mode]
                ]
                rows_written += cursor.executemany(
                    ADJUSTED_UPSERT_BY_MODE[mode], values
                ) or 0
            gap_values = [
                (
                    self.batch_id,
                    str(gap.get("stock_code", batch.stock_code)),
                    gap.get("trade_date"),
                    gap.get("mode"),
                    gap.get("reason", "unknown"),
                    json.dumps(dict(gap), ensure_ascii=False, default=str),
                )
                for gap in batch.gaps
            ]
            if gap_values:
                cursor.executemany(GAP_UPSERT_SQL, gap_values)
            cursor.execute(
                COMPLETE_BATCH_SQL,
                (
                    len(batch.rows_by_mode["none"]),
                    len(batch.rows_by_mode["front"]),
                    len(batch.rows_by_mode["back"]),
                    len(batch.gaps),
                    self.batch_id,
                    batch.stock_code,
                ),
            )
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            cursor.close()
            conn.close()
        return PersistResult(batch.stock_code, rows_written, len(batch.gaps), fingerprint)
