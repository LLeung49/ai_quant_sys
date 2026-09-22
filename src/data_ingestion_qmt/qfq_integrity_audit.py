"""Persistence boundary for QMT raw/QFQ integrity findings."""

from __future__ import annotations

from dataclasses import dataclass, replace
from datetime import date, datetime
from hashlib import sha256
import json
from typing import Any

try:
    from .db_config import execute_update
except ImportError:  # Direct script execution from src/data_ingestion_qmt.
    from db_config import execute_update


@dataclass(frozen=True)
class IntegrityFinding:
    stock_code: str
    trade_date: str
    check_code: str
    severity: str
    status: str
    raw_ohlc: dict[str, Any] | None
    qfq_ohlc: dict[str, Any] | None
    source_fingerprint: str | None
    validator_version: str
    last_error: str | None
    note: str | None


def _canonical_json(value: Any) -> str:
    """Return deterministic JSON suitable for an evidence fingerprint."""
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        default=_json_default,
    )


def _json_default(value: Any) -> str:
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    return str(value)


def build_source_fingerprint(raw: dict | None, qfq: dict | None) -> str:
    """Fingerprint a raw/QFQ pair independent of Python dictionary order."""
    evidence = {"qfq": qfq, "raw": raw}
    return sha256(_canonical_json(evidence).encode("utf-8")).hexdigest()


UPSERT_INTEGRITY_FINDING_SQL = """
INSERT INTO trade_qfq_integrity_audit (
    stock_code, trade_date, check_code, severity, status,
    raw_ohlc_json, qfq_ohlc_json, source_fingerprint, validator_version,
    last_error, note
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
ON DUPLICATE KEY UPDATE
    severity = VALUES(severity),
    status = VALUES(status),
    raw_ohlc_json = VALUES(raw_ohlc_json),
    qfq_ohlc_json = VALUES(qfq_ohlc_json),
    source_fingerprint = VALUES(source_fingerprint),
    validator_version = VALUES(validator_version),
    last_verified_at = CURRENT_TIMESTAMP,
    resolved_at = CASE
        WHEN VALUES(status) = 'resolved' THEN CURRENT_TIMESTAMP
        ELSE NULL
    END,
    last_error = VALUES(last_error),
    note = VALUES(note)
"""


def upsert_integrity_finding(finding: IntegrityFinding) -> int:
    """Store the latest evidence without changing the original detection time."""
    params = (
        finding.stock_code,
        finding.trade_date,
        finding.check_code,
        finding.severity,
        finding.status,
        _canonical_json(finding.raw_ohlc) if finding.raw_ohlc is not None else None,
        _canonical_json(finding.qfq_ohlc) if finding.qfq_ohlc is not None else None,
        finding.source_fingerprint,
        finding.validator_version,
        finding.last_error,
        finding.note,
    )
    return execute_update(UPSERT_INTEGRITY_FINDING_SQL, params)


def transition_integrity_finding(
    finding: IntegrityFinding,
    status: str,
    *,
    note: str | None = None,
    last_error: str | None = None,
) -> int:
    """Persist a repair lifecycle transition while retaining original evidence."""
    return upsert_integrity_finding(replace(
        finding,
        status=status,
        last_error=last_error,
        note=note if note is not None else finding.note,
    ))
