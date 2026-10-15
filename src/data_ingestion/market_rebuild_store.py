"""Transactional, staging-only persistence for market-layer reconstruction."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import json
from typing import Callable, Mapping

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
    (batch_id, stock_code, price_mode, reason, first_trade_date,
     last_trade_date, gap_count, sample_detail)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
ON DUPLICATE KEY UPDATE
    first_trade_date=VALUES(first_trade_date),
    last_trade_date=VALUES(last_trade_date),
    gap_count=VALUES(gap_count), sample_detail=VALUES(sample_detail)
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

    def prepare_universe(self, stock_codes: list[str]) -> str:
        """Persist one immutable expected-code manifest for this batch."""
        codes = sorted({str(code).strip() for code in stock_codes if str(code).strip()})
        if not codes:
            raise ValueError("rebuild universe must not be empty")
        digest = hashlib.sha256("".join(f"{code}\n" for code in codes).encode("utf-8")).hexdigest()
        conn = self.connection_factory()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "SELECT stock_code, universe_hash "
                "FROM trade_market_rebuild_expected_code WHERE batch_id=%s "
                "ORDER BY stock_code",
                (self.batch_id,),
            )
            existing = list(cursor.fetchall())
            if existing:
                existing_codes = [str(row[0]) for row in existing]
                existing_hashes = {str(row[1]) for row in existing}
                if existing_codes != codes or existing_hashes != {digest}:
                    raise ValueError("universe manifest differs from existing batch")
                return digest
            cursor.executemany(
                "INSERT INTO trade_market_rebuild_expected_code "
                "(batch_id, stock_code, universe_hash) VALUES (%s, %s, %s)",
                [(self.batch_id, code, digest) for code in codes],
            )
            conn.commit()
            return digest
        except Exception:
            conn.rollback()
            raise
        finally:
            cursor.close()
            conn.close()

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

    def excluded_codes(self) -> set[str]:
        conn = self.connection_factory()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "SELECT stock_code FROM trade_market_rebuild_excluded_code "
                "WHERE batch_id=%s",
                (self.batch_id,),
            )
            return {str(row[0]) for row in cursor.fetchall()}
        finally:
            cursor.close()
            conn.close()

    def record_exclusions(
        self, exclusions: Mapping[str, Mapping[str, object]]
    ) -> None:
        """Persist reviewed removals without mutating the immutable universe."""
        values = []
        for stock_code, detail in sorted(exclusions.items()):
            reason = str(detail.get("reason") or "").strip()
            evidence = detail.get("evidence")
            if not stock_code.strip() or not reason or not isinstance(evidence, Mapping):
                raise ValueError("each exclusion requires code, reason, and evidence")
            values.append((
                self.batch_id,
                stock_code.strip(),
                reason,
                json.dumps(dict(evidence), ensure_ascii=False, sort_keys=True, default=str),
            ))
        if not values:
            raise ValueError("at least one exclusion is required")
        conn = self.connection_factory()
        cursor = conn.cursor()
        try:
            cursor.executemany(
                "INSERT INTO trade_market_rebuild_excluded_code "
                "(batch_id, stock_code, reason, evidence) VALUES (%s, %s, %s, %s)",
                values,
            )
            conn.commit()
        except Exception:
            conn.rollback()
            raise
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
        return self.persist_validated_batches([batch])[0]

    def persist_validated_batches(
        self, batches: list[MarketBatch]
    ) -> list[PersistResult]:
        """Persist a provider batch with three bulk inserts and one commit."""
        if not batches:
            return []
        prepared = []
        for batch in batches:
            if not batch.is_complete:
                raise ValueError(
                    f"incomplete market batch for {batch.stock_code}: {batch.failures}"
                )
            validation = validate_projection_batch(batch.rows_by_mode)
            if not validation.is_valid:
                reasons = [
                    issue.code for issue in validation.issues
                    if issue.severity == "error"
                ]
                raise ValueError(
                    f"invalid market batch for {batch.stock_code}: {reasons}"
                )
            fingerprint = str(batch.provenance.get("fingerprint") or hashlib.sha256(
                json.dumps(
                    batch.rows_by_mode, sort_keys=True, default=str
                ).encode("utf-8")
            ).hexdigest())
            source = str(batch.provenance.get("provider", "unknown"))
            fetched_at = (
                batch.provenance.get("fetched_at")
                or datetime.now(timezone.utc)
            )
            prepared.append((batch, fingerprint, source, fetched_at))

        conn = self.connection_factory()
        cursor = conn.cursor()
        try:
            cursor.executemany(
                START_BATCH_SQL,
                [
                    (
                        self.batch_id, batch.stock_code, batch.start_date,
                        batch.end_date, source, fingerprint,
                    )
                    for batch, fingerprint, source, _ in prepared
                ],
            )
            raw_values = [
                (
                    row["stock_code"], row["trade_date"], row["open_price"],
                    row["high_price"], row["low_price"], row["close_price"],
                    row["volume"], row["amount"], row.get("pre_close"),
                    row.get("suspend_flag"), row.get("data_source", source),
                    self.batch_id, source, fetched_at, fingerprint,
                )
                for batch, fingerprint, source, fetched_at in prepared
                for row in batch.rows_by_mode["none"]
            ]
            cursor.executemany(RAW_UPSERT, raw_values)
            for mode in ("front", "back"):
                values = [
                    (
                        row["stock_code"], row["trade_date"], row["open_price"],
                        row["high_price"], row["low_price"], row["close_price"],
                        row["volume"], row["amount"], row.get("turnover_rate"),
                        batch.end_date, self.batch_id, source, fetched_at, fingerprint,
                    )
                    for batch, fingerprint, source, fetched_at in prepared
                    for row in batch.rows_by_mode[mode]
                ]
                cursor.executemany(ADJUSTED_UPSERT_BY_MODE[mode], values)
            gap_groups: dict[tuple[str, str, str], list[dict]] = {}
            for batch, _, _, _ in prepared:
                for gap in batch.gaps:
                    key = (
                        str(gap.get("stock_code", batch.stock_code)),
                        str(gap.get("mode", "unknown")),
                        str(gap.get("reason", "unknown")),
                    )
                    gap_groups.setdefault(key, []).append(dict(gap))
            gap_values = []
            for (stock_code, mode, reason), gaps in gap_groups.items():
                dates = sorted(str(gap["trade_date"])[:10] for gap in gaps)
                gap_values.append((
                    self.batch_id, stock_code, mode, reason,
                    dates[0], dates[-1], len(gaps),
                    json.dumps(gaps[:5], ensure_ascii=False, default=str),
                ))
            if gap_values:
                cursor.executemany(GAP_UPSERT_SQL, gap_values)
            cursor.executemany(
                COMPLETE_BATCH_SQL,
                [
                    (
                        len(batch.rows_by_mode["none"]),
                        len(batch.rows_by_mode["front"]),
                        len(batch.rows_by_mode["back"]),
                        len(batch.gaps), self.batch_id, batch.stock_code,
                    )
                    for batch, _, _, _ in prepared
                ],
            )
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            cursor.close()
            conn.close()
        return [
            PersistResult(
                batch.stock_code,
                sum(len(rows) for rows in batch.rows_by_mode.values()),
                len(batch.gaps),
                fingerprint,
            )
            for batch, fingerprint, _, _ in prepared
        ]
