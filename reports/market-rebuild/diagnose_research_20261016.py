"""Read-only investigation of 2026-10-16 research snapshot quality."""

import json
from collections import Counter

from data_ingestion.db_config import execute_query


rows = execute_query(
    """SELECT sector_level, strategy_type, candidate_status,
              COUNT(*) AS rows_count
         FROM research_candidate_snapshot
        WHERE as_of_date = %s AND snapshot_mode = 'backfill'
        GROUP BY sector_level, strategy_type, candidate_status
        ORDER BY sector_level, strategy_type, candidate_status""",
    ("2026-10-16",),
)
samples = execute_query(
    """SELECT entity_code, candidate_status, feature_json, reasons_json, risk_flags_json
         FROM research_candidate_snapshot
        WHERE as_of_date = %s AND snapshot_mode = 'backfill'
          AND sector_level = 2 AND strategy_type = 'stock_trend'
        LIMIT 20""",
    ("2026-10-16",),
)
features = []
for row in samples:
    payload = json.loads(row["feature_json"] or "{}")
    features.append({
        "code": row["entity_code"],
        "status": row["candidate_status"],
        "risk_flags": json.loads(row["risk_flags_json"] or "[]"),
        "reasons": json.loads(row["reasons_json"] or "[]"),
        "quality_reasons": payload.get("data_quality_reasons"),
        "feature_keys": sorted(payload),
        "key_metrics": {key: payload.get(key) for key in ("alpha_strength", "persistence", "trend_quality", "liquidity")},
    })
etf_uniques = execute_query(
    """SELECT candidate_status, COUNT(DISTINCT entity_code) AS unique_codes
         FROM research_candidate_snapshot
        WHERE as_of_date = %s AND snapshot_mode = 'backfill'
          AND sector_level = 2 AND strategy_type = 'etf_core'
        GROUP BY candidate_status""",
    ("2026-10-16",),
)
trend_rows = execute_query(
    """SELECT entity_code, feature_json, reasons_json, risk_flags_json
         FROM research_candidate_snapshot
        WHERE as_of_date = %s AND snapshot_mode = 'backfill'
          AND sector_level = 2 AND strategy_type = 'stock_trend'""",
    ("2026-10-16",),
)
missing_reasons = Counter()
nonnull_features = Counter()
for row in trend_rows:
    feature = json.loads(row["feature_json"] or "{}")
    for reason in json.loads(row["reasons_json"] or "[]"):
        if reason.startswith("missing:"):
            missing_reasons[reason] += 1
    for key in ("alpha_strength", "alpha_persistence", "trend_quality", "trend_structure", "liquidity", "adx", "er"):
        if feature.get(key) is not None:
            nonnull_features[key] += 1
history = execute_query(
    """SELECT stock_code, COUNT(*) AS valid_days,
              MIN(trade_date) AS first_date, MAX(trade_date) AS last_date
         FROM trade_stock_daily_qfq
        WHERE stock_code IN ('300012.SZ', '600826.SH', '600861.SH')
          AND trade_date BETWEEN '2026-07-01' AND '2026-10-16'
          AND close_price > 0
        GROUP BY stock_code"""
)
other_dates = execute_query(
    """SELECT as_of_date, COUNT(*) AS rows_count,
              SUM(CAST(risk_flags_json AS CHAR) LIKE '%%data_quality_blocked%%') AS blocked_rows
         FROM research_candidate_snapshot
        WHERE as_of_date IN ('2026-09-18','2026-10-13','2026-10-14','2026-10-15','2026-10-16')
          AND snapshot_mode = 'backfill' AND sector_level = 2
          AND strategy_type = 'stock_trend'
        GROUP BY as_of_date ORDER BY as_of_date"""
)
print(json.dumps({"groups": rows, "etf_unique_codes_by_status": etf_uniques, "trend_missing_reasons": missing_reasons, "trend_nonnull_features": nonnull_features, "sample_valid_qfq_history": history, "other_date_quality": other_dates, "samples": features[:3]}, ensure_ascii=False, default=str, indent=2))
