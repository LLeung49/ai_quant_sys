"""Find and record target-day market bars missing from the prior session's universe."""

from __future__ import annotations

from datetime import date, datetime, timedelta, timezone
import json
from pathlib import Path

from .db_config import execute_query


PROJECTION_TABLES = (
    "trade_stock_daily_raw",
    "trade_stock_daily_qfq",
    "trade_stock_daily_bfq",
)
RECENT_LOOKBACK_DAYS = 60


def find_missing_market_codes(target: date) -> tuple[date | None, list[str]]:
    """Find incomplete target-day projections, excluding known suspended codes."""
    result = execute_query(
        "SELECT MAX(trade_date) AS prior_date FROM trade_stock_daily_raw "
        "WHERE trade_date < %s", (target.isoformat(),),
    )
    prior = result[0]["prior_date"] if result else None
    if prior is None:
        return None, []
    universe = {
        str(row["stock_code"])
        for row in execute_query(
            "SELECT stock_code FROM trade_stock_daily_raw "
            "WHERE trade_date>=%s AND trade_date<=%s UNION "
            "SELECT stock_code FROM trade_stock_daily_qfq WHERE trade_date=%s UNION "
            "SELECT stock_code FROM trade_stock_daily_bfq WHERE trade_date=%s",
            ((target - timedelta(days=RECENT_LOOKBACK_DAYS)).isoformat(),
             target.isoformat(), target.isoformat(), target.isoformat()),
        )
    }
    present_in_all: set[str] | None = None
    for table in PROJECTION_TABLES:
        current_codes = {
            str(row["stock_code"])
            for row in execute_query(
                f"SELECT stock_code FROM {table} WHERE trade_date=%s",
                (target.isoformat(),),
            )
        }
        if present_in_all is None:
            present_in_all = current_codes
        else:
            present_in_all.intersection_update(current_codes)
    missing = sorted(universe - (present_in_all or set()))
    if not missing:
        return prior, []
    placeholders = ",".join(["%s"] * len(missing))
    suspended = {
        str(row["stock_code"])
        for row in execute_query(
            "SELECT latest.stock_code FROM ("
            "SELECT stock_code, MAX(trade_date) AS latest_date "
            "FROM trade_stock_daily_raw "
            f"WHERE stock_code IN ({placeholders}) AND trade_date<=%s "
            "GROUP BY stock_code) AS latest "
            "JOIN trade_stock_daily_raw AS raw "
            "ON raw.stock_code=latest.stock_code AND raw.trade_date=latest.latest_date "
            "WHERE latest.latest_date<%s AND raw.suspend_flag=1",
            (*missing, target.isoformat(), target.isoformat()),
        )
    }
    return prior, [code for code in missing if code not in suspended]


def write_gap_report(
    target: date, prior: date | None, missing_codes: list[str], output_dir: Path,
) -> Path:
    """Keep an operator-readable record even after a later retry fills the gap."""
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / f"market_missing_{target.isoformat()}.json"
    try:
        previous = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    except (OSError, json.JSONDecodeError):
        previous = {}
    observed = sorted(set(previous.get("observed_missing_codes", []))
                      | set(previous.get("missing_codes", [])) | set(missing_codes))
    payload = {
        "target_date": target.isoformat(),
        "prior_trade_date": prior.isoformat() if prior else None,
        "status": "pending" if missing_codes else "complete",
        "missing_count": len(missing_codes),
        "missing_codes": missing_codes,
        "observed_missing_codes": observed,
        "recovered_codes": sorted(set(observed) - set(missing_codes)),
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path
