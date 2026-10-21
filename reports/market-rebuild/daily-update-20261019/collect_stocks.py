"""One-off AKShare stock-only pass while the ETF fallback remains stale."""

from datetime import date, timedelta
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))

from data_ingestion.akshare_market_provider import AKShareMarketProvider, _is_etf


collector_path = ROOT / "src" / "data_ingestion" / "8-原始行情与复权数据采集.py"
spec = importlib.util.spec_from_file_location("canonical_market_collector", collector_path)
collector = importlib.util.module_from_spec(spec)
spec.loader.exec_module(collector)

target = date(2026, 10, 19)
codes = [code for code in collector.get_code_universe() if not _is_etf(code)]
print(f"[股票采集] target={target} codes={len(codes)}", flush=True)
result = collector.run_collection(
    AKShareMarketProvider(max_attempts=1, request_timeout=8),
    codes,
    target - timedelta(days=10),
    target,
    dry_run=False,
    workers=8,
    accepted_suspended_codes=collector.get_latest_suspended_codes(codes),
)
summary = {
    "target": target.isoformat(),
    "codes": len(codes),
    "succeeded": result.succeeded,
    "failed": result.failed,
    "written_rows": result.written_rows,
    "failures": result.failures,
}
output = Path(__file__).with_name("stock-result.json")
output.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"[股票采集完成] succeeded={result.succeeded} failed={result.failed} written_rows={result.written_rows}", flush=True)
raise SystemExit(1 if result.failed else 0)
