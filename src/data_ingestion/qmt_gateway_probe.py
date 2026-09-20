"""Read-only-first CLI for inspecting QMT HTTP Bridge gateway responses.

Run this before enabling a copied collector to see the real response shapes
from the QMT client. Download/refresh calls require explicit flags.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from typing import Any, Callable

import pandas as pd

try:
    from .qmt_data_gateway import QMTDataGateway
except ImportError:
    from qmt_data_gateway import QMTDataGateway


@dataclass(frozen=True)
class ProbeConfig:
    stock: str = "600519.SH"
    sector: str = "沪深A股"
    start: str = "20250101"
    end: str = ""
    financial_table: str = "Balance"
    max_rows: int = 3
    include_refresh: bool = False
    include_downloads: bool = False


def summarize(value: Any, max_rows: int = 3) -> dict[str, Any]:
    if isinstance(value, pd.DataFrame):
        sample = value.head(max_rows).reset_index().to_dict(orient="records")
        return {
            "kind": "dataframe",
            "rows": len(value),
            "columns": [str(column) for column in value.columns],
            "index_name": value.index.name,
            "sample": sample,
        }
    if isinstance(value, dict):
        items = list(value.items())[:max_rows]
        return {
            "kind": "mapping",
            "size": len(value),
            "keys": [str(key) for key in list(value)[:max_rows]],
            "sample": {str(key): summarize(item, max_rows) for key, item in items},
        }
    if isinstance(value, (list, tuple, set)):
        values = list(value)
        return {"kind": "sequence", "size": len(values), "sample": values[:max_rows]}
    if hasattr(value, "downloaded") and hasattr(value, "failed"):
        return {
            "kind": type(value).__name__,
            "downloaded": list(value.downloaded),
            "failed": list(value.failed),
        }
    return {"kind": type(value).__name__, "value": value}


class GatewayProbe:
    def __init__(self, gateway: QMTDataGateway, config: ProbeConfig) -> None:
        self.gateway = gateway
        self.config = config

    def _run(self, name: str, operation: Callable[[], Any]) -> dict[str, Any]:
        try:
            return {"name": name, "status": "ok", "result": summarize(operation(), self.config.max_rows)}
        except Exception as exc:
            return {"name": name, "status": "error", "error": str(exc)}

    def run(self, only: set[str] | None = None) -> list[dict[str, Any]]:
        c = self.config
        checks: list[tuple[str, Callable[[], Any]]] = [
            ("sector_list", self.gateway.get_sector_list),
            ("stock_list_in_sector", lambda: self.gateway.get_stock_list_in_sector(c.sector)),
            ("instrument_detail", lambda: self.gateway.get_instrument_detail(c.stock)),
            *[
                (
                    f"market_{mode}",
                    lambda mode=mode: self.gateway.get_market_data_ex(
                        ["open", "high", "low", "close", "volume", "amount"],
                        [c.stock], "1d", c.start, c.end, dividend_type=mode,
                    ),
                )
                for mode in ("none", "front", "back")
            ],
            ("divid_factors", lambda: self.gateway.get_divid_factors(c.stock, c.start, c.end)),
            (
                "financial_data",
                lambda: self.gateway.get_financial_data(
                    table_list=[c.financial_table], stock_list=[c.stock],
                    start_time=c.start, end_time=c.end,
                ),
            ),
            ("etf_info", self.gateway.get_etf_info),
        ]
        if c.include_refresh:
            checks.extend([
                ("download_sector_data", self.gateway.download_sector_data),
                ("download_etf_info", self.gateway.download_etf_info),
            ])
        if c.include_downloads:
            checks.extend([
                ("download_history_data", lambda: self.gateway.download_history_data(c.stock, "1d", c.start, c.end)),
                ("download_financial_data", lambda: self.gateway.download_financial_data([c.stock], [c.financial_table])),
            ])
        if only:
            checks = [(name, operation) for name, operation in checks if name in only]
        return [self._run(name, operation) for name, operation in checks]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Inspect QMT HTTP Bridge gateway response shapes")
    parser.add_argument("--stock", default="600519.SH")
    parser.add_argument("--sector", default="沪深A股")
    parser.add_argument("--start", default="20250101")
    parser.add_argument("--end", default="")
    parser.add_argument("--financial-table", default="Balance")
    parser.add_argument("--max-rows", type=int, default=3)
    parser.add_argument("--only", action="append", help="run one named check; repeat for multiple checks")
    parser.add_argument("--include-refresh", action="store_true", help="trigger sector/ETF cache refreshes")
    parser.add_argument("--include-downloads", action="store_true", help="trigger market/financial downloads")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    config = ProbeConfig(
        stock=args.stock, sector=args.sector, start=args.start, end=args.end,
        financial_table=args.financial_table, max_rows=args.max_rows,
        include_refresh=args.include_refresh, include_downloads=args.include_downloads,
    )
    results = GatewayProbe(QMTDataGateway.from_env(), config).run(only=set(args.only or []))
    print(json.dumps({"config": config.__dict__, "results": results}, ensure_ascii=False, indent=2, default=str))
    return 1 if any(result["status"] == "error" for result in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
