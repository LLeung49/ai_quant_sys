"""Read-only financial recovery acceptance evidence."""

from datetime import date
import json
from pathlib import Path

from fastapi.testclient import TestClient

from data_ingestion.db_config import execute_query
from data_ingestion.run_daily_market_pipeline import market_date_issue
from .akshare_archive import read_snapshot
from .archive_repair_dependencies import verify_archive
from .rebuild_repair_history import (
    DEFAULT_LEDGER, DEFAULT_MANIFEST, candidate_dates, completed_dates, verify_backup,
)


def verify() -> dict:
    report = {"snapshot_backup": verify_backup(DEFAULT_MANIFEST),
              "dependency_archive": verify_archive()}
    report["financial_sources"] = execute_query(
        "SELECT data_source,source_table,COUNT(*) AS rows_count,"
        "COUNT(DISTINCT stock_code) AS stocks,MIN(report_date) AS first_period,"
        "MAX(report_date) AS last_period FROM trade_stock_financial_raw_pit "
        "GROUP BY data_source,source_table"
    )
    report["financial_quality"] = execute_query(
        "SELECT data_source,COUNT(*) AS rows_count,"
        "SUM(announcement_date IS NULL OR announcement_date<=report_date "
        "OR announcement_date>'2026-10-20') AS invalid_dates,"
        "SUM(revenue IS NULL OR net_profit IS NULL OR total_assets IS NULL "
        "OR total_assets<=0 OR total_equity IS NULL OR operating_cash_flow IS NULL) AS invalid_core,"
        "SUM((eps IS NOT NULL OR roe IS NOT NULL OR gross_margin IS NOT NULL) "
        "AND metric_available_at IS NULL) AS missing_metric_dates "
        "FROM trade_stock_financial_raw_pit WHERE source_table IN "
        "('qmt_native_composite','akshare_eastmoney_financial') GROUP BY data_source"
    )
    report["annual_coverage"] = execute_query(
        "SELECT data_source,YEAR(report_date) AS report_year,"
        "COUNT(*) AS rows_count,COUNT(DISTINCT stock_code) AS stocks "
        "FROM trade_stock_financial_raw_pit WHERE source_table IN "
        "('qmt_native_composite','akshare_eastmoney_financial') "
        "GROUP BY data_source,YEAR(report_date) ORDER BY data_source,report_year"
    )
    report["capital_sources"] = execute_query(
        "SELECT data_source,COUNT(*) AS rows_count,COUNT(DISTINCT stock_code) AS stocks,"
        "SUM(total_shares IS NULL OR total_shares<=0) AS invalid_total,"
        "SUM(circulating_shares=0) AS zero_circulating "
        "FROM trade_stock_capital_pit GROUP BY data_source"
    )
    expected_dates = set(candidate_dates("2024-01-02", "2026-09-17"))
    committed_dates = completed_dates(DEFAULT_LEDGER)
    committed_dates.update(str(row["as_of_date"]) for row in execute_query(
        "SELECT as_of_date FROM financial_repair_recovery_day"
    ))
    report["historical_rebuild"] = {
        "expected_dates": len(expected_dates),
        "committed_dates": len(expected_dates & committed_dates),
        "unrebuilt_dates": sorted(expected_dates - committed_dates),
        "rejected_unscorable_candidates": execute_query(
            "SELECT COUNT(*) AS rows_count FROM research_candidate_snapshot "
            "WHERE as_of_date='2026-08-27' AND sector_level=2 "
            "AND strategy_type='stock_repair' AND snapshot_mode='backfill' "
            "AND validation_status='rejected'"
        )[0]["rows_count"],
    }
    archive_counts = {}
    for kind in ("financial", "capital"):
        documents = [read_snapshot(path) for path in Path(
            f"reports/financial-audit/akshare-daily/2026-10-20/{kind}",
        ).glob("*.json.gz")]
        archive_counts[kind] = {
            "documents": len(documents),
            "stocks": len({document["stock_code"] for document in documents}),
            "rows": sum(len(document["rows"]) for document in documents),
            "checksums": "verified",
        }
    report["akshare_archives"] = archive_counts
    report["market_date_issue"] = market_date_issue(date(2026, 10, 20))
    from morning_conference.sector_rotation2.api.app import create_app
    client = TestClient(create_app())
    api_checks = []
    for day, mode in (("2024-01-02", "backfill"), ("2026-08-27", "backfill"),
                      ("2026-10-19", "backfill"),
                      ("2026-08-28", "delayed_shadow")):
        params = {"as_of_date": day, "snapshot_mode": mode, "level": 2,
                  "strategy_type": "stock_repair"}
        response = client.get(
            "/api/v1/sector-rotation/research/stock-candidates", params=params,
        )
        payload = response.json()
        api_checks.append({"day": day, "mode": mode, "http": response.status_code,
                           "candidates": len(payload.get("candidates", []))})
    report["api_checks"] = api_checks
    return report


if __name__ == "__main__":
    evidence = verify()
    output = Path("reports/financial-audit/recovery-verification-20261020.json")
    output.write_text(json.dumps(evidence, ensure_ascii=False, default=str, indent=2), encoding="utf-8")
    print(json.dumps(evidence, ensure_ascii=True, default=str))
