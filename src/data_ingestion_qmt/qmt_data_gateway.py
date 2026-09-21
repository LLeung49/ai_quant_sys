"""HTTP adapter for the QMT client-side data bridge.

The gateway deliberately exposes xtdata-shaped methods so collectors can be
copied with minimal business-logic changes while the transport remains
replaceable in tests.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pandas as pd
import requests
from dotenv import dotenv_values


class QMTBridgeError(RuntimeError):
    """Raised when the bridge cannot satisfy a data request."""


@dataclass(frozen=True)
class DownloadResult:
    downloaded: tuple[str, ...]
    failed: tuple[dict[str, Any], ...]


def _chunks(values: list[str], size: int):
    for offset in range(0, len(values), size):
        yield values[offset : offset + size]


# ContextInfo financial data uses QMT's official table names.  The copied
# collector still expects the xtdata table names and field suffixes below.
_RAW_FINANCIAL_FIELDS: dict[str, dict[str, str]] = {
    "Balance": {
        "ASHAREBALANCESHEET.tot_assets": "tot_assets",
        "ASHAREBALANCESHEET.tot_liab": "tot_liab",
        "ASHAREBALANCESHEET.total_equity": "total_equity",
        "ASHAREBALANCESHEET.tot_shrhldr_eqy_incl_min_int": "tot_shrhldr_eqy_incl_min_int",
        "ASHAREBALANCESHEET.total_current_assets": "total_current_assets",
        "ASHAREBALANCESHEET.total_current_liability": "total_current_liability",
    },
    "Income": {
        "ASHAREINCOME.revenue": "revenue",
        "ASHAREINCOME.operating_revenue": "operating_revenue",
        "ASHAREINCOME.net_profit_incl_min_int_inc": "net_profit_incl_min_int_inc",
        "ASHAREINCOME.net_profit_excl_min_int_inc": "net_profit_excl_min_int_inc",
        "ASHAREINCOME.cost_of_goods_sold": "cost_of_goods_sold",
        "ASHAREINCOME.total_operating_cost": "total_operating_cost",
    },
    "CashFlow": {
        "ASHARECASHFLOW.net_cash_flows_oper_act": "net_cash_flows_oper_act",
    },
    "PershareIndex": {
        "PERSHAREINDEX.s_fa_eps_basic": "s_fa_eps_basic",
        "PERSHAREINDEX.du_return_on_equity": "du_return_on_equity",
        "PERSHAREINDEX.equity_roe": "equity_roe",
        "PERSHAREINDEX.net_roe": "net_roe",
        "PERSHAREINDEX.sales_gross_profit": "sales_gross_profit",
    },
    "Capital": {
        "CAPITALSTRUCTURE.total_capital": "total_capital",
    },
}


def resolve_env_path() -> Path:
    """Resolve .env with the same rules used by data_ingestion_qmt.db_config."""
    configured_path = os.environ.get("AI_QUANT_ENV_FILE")
    if configured_path:
        return Path(configured_path).expanduser()

    module_path = Path(__file__).resolve()
    for directory in module_path.parents:
        candidate = directory / ".env"
        if candidate.is_file():
            return candidate

    return Path(__file__).parent.parent.parent / ".env"


def _bridge_env(name: str, values: dict[str, str | None], default: str) -> str:
    if name in os.environ:
        return os.environ[name]
    return values.get(name) or default


class QMTDataGateway:
    def __init__(
        self,
        *,
        base_url: str = "http://127.0.0.1:15588",
        token: str = "",
        timeout: tuple[float, float] = (3.0, 60.0),
        session: requests.Session | None = None,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self._session = session or requests.Session()
        self._session.headers.update(
            {
                "X-Token": token,
                "Content-Type": "application/json; charset=utf-8",
            }
        )

    @classmethod
    def from_env(cls) -> "QMTDataGateway":
        values = dotenv_values(resolve_env_path())
        return cls(
            base_url=_bridge_env(
                "QMT_BRIDGE_URL", values, "http://127.0.0.1:15588"
            ),
            token=_bridge_env("QMT_BRIDGE_TOKEN", values, ""),
            timeout=(
                float(_bridge_env("QMT_BRIDGE_CONNECT_TIMEOUT", values, "3")),
                float(_bridge_env("QMT_BRIDGE_READ_TIMEOUT", values, "60")),
            ),
        )

    def connect(self) -> None:
        """Compatibility no-op; HTTP requests establish the bridge connection."""
        return None

    def _request(
        self, method: str, path: str, payload: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        try:
            response = self._session.request(
                method,
                self.base_url + path,
                json=payload,
                timeout=self.timeout,
            )
            response.raise_for_status()
            body = response.json()
        except (requests.RequestException, ValueError) as exc:
            raise QMTBridgeError(f"{method} {path}: {exc}") from exc
        if not isinstance(body, dict):
            raise QMTBridgeError(f"{method} {path}: invalid response envelope")
        if body.get("error"):
            raise QMTBridgeError(f"{method} {path}: {body['error']}")
        return body

    @staticmethod
    def _frame(records: Any) -> pd.DataFrame:
        if records is None:
            return pd.DataFrame()
        if isinstance(records, dict):
            records = list(records.values())
        frame = pd.DataFrame.from_records(records)
        if "time" in frame.columns:
            raw_times = frame.pop("time").astype(str)
            parsed = pd.to_datetime(raw_times, errors="raise")
            frame.index = parsed.dt.strftime("%Y%m%d")
        return frame

    @staticmethod
    def _context_frame(columns: Any) -> pd.DataFrame:
        """Restore a ContextInfo ``DataFrame.to_dict()`` result."""
        if not isinstance(columns, dict):
            return QMTDataGateway._frame(columns)
        frame = pd.DataFrame(columns)
        if not frame.empty:
            frame.index = pd.to_datetime(frame.index.astype(str), errors="raise").strftime("%Y%m%d")
        return frame

    def download_history_data(
        self,
        stock_code: str | list[str],
        period: str = "1d",
        start_time: str = "",
        end_time: str = "",
    ) -> DownloadResult:
        stocks = [stock_code] if isinstance(stock_code, str) else list(stock_code)
        # ContextInfo.get_market_data_ex obtains the QMT-managed history directly.
        # The former xtdata download endpoint is unavailable in the regulated setup.
        return DownloadResult(tuple(stocks), ())

    def get_market_data_ex(
        self,
        field_list: list[str],
        stock_list: list[str],
        period: str,
        start_time: str = "",
        end_time: str = "",
        count: int = -1,
        dividend_type: str = "none",
        fill_data: bool = True,
    ) -> dict[str, pd.DataFrame]:
        result: dict[str, pd.DataFrame] = {}
        for batch in _chunks(list(stock_list), 50):
            body = self._request(
                "POST",
                "/api/data/market_data_ex",
                {
                    "fields": ",".join(field_list),
                    "stock_code": ",".join(batch),
                    "period": period,
                    "start_time": start_time,
                    "end_time": end_time,
                    "count": count,
                    "dividend_type": dividend_type,
                },
            )
            for code, records in (body.get("data") or {}).items():
                result[code] = self._context_frame(records)
        return result

    def download_financial_data(
        self, stock_list: list[str], table_list: list[str]
    ) -> DownloadResult:
        # Financial reports are downloaded by QMT Data Manager.  ContextInfo
        # has no matching download method, so this compatibility method checks
        # readiness rather than falsely reporting an xtdata refresh success.
        self.get_financial_data(
            table_list or ["Balance"], list(stock_list), "", "", "report_time"
        )
        return DownloadResult(tuple(stock_list), ())

    def get_financial_data(
        self,
        fields: list[str] | None = None,
        stocks: list[str] | None = None,
        start_time: str = "",
        end_time: str = "",
        report_type: str = "report_time",
        **kwargs: Any,
    ) -> dict[str, dict[str, pd.DataFrame]]:
        fields = list(fields or kwargs.pop("table_list", []))
        stocks = list(stocks or kwargs.pop("stock_list", []))
        unsupported = [name for name in fields if name not in _RAW_FINANCIAL_FIELDS]
        if unsupported:
            raise QMTBridgeError(
                "ContextInfo financial adapter only supports tables: "
                + ", ".join(_RAW_FINANCIAL_FIELDS)
                + "; unsupported: " + ", ".join(unsupported)
            )
        qmt_fields = [
            field
            for table in fields
            for field in _RAW_FINANCIAL_FIELDS[table]
        ]
        result: dict[str, dict[str, pd.DataFrame]] = {}
        for batch in _chunks(list(stocks), 50):
            body = self._request(
                "POST",
                "/api/data/raw_financial_data",
                {
                    "field_list": ",".join(qmt_fields),
                    "stock_list": ",".join(batch),
                    "start_time": start_time or "19000101",
                    "end_time": end_time or "20991231",
                    "report_type": report_type,
                },
            )
            raw_by_stock = body.get("data") or {}
            missing = []
            for code in batch:
                raw_fields = raw_by_stock.get(code) or {}
                tables: dict[str, pd.DataFrame] = {}
                for table in fields:
                    rows: dict[int, dict[str, Any]] = {}
                    for qmt_field, legacy_field in _RAW_FINANCIAL_FIELDS[table].items():
                        for timetag, value in (raw_fields.get(qmt_field) or {}).items():
                            timestamp = int(timetag)
                            rows.setdefault(timestamp, {"m_timetag": timestamp})[legacy_field] = value
                    tables[table] = pd.DataFrame(
                        [rows[key] for key in sorted(rows)]
                    )
                if not any(not frame.empty for frame in tables.values()):
                    missing.append(code)
                result[code] = tables
            if missing:
                raise QMTBridgeError(
                    "financial data is not available in QMT Data Manager for: "
                    + ", ".join(missing)
                )
        return result

    def download_financial_data2(
        self,
        stock_list: list[str],
        table_list: list[str],
        start_time: str = "",
        end_time: str = "",
        callback=None,
    ) -> DownloadResult:
        result = self.download_financial_data(stock_list, table_list)
        if callback is not None:
            callback(result)
        return result

    def get_stock_list_in_sector(self, sector_name: str) -> list[str]:
        body = self._request(
            "POST", "/api/data/stock_list_in_sector", {"sectorname": sector_name}
        )
        return [str(code) for code in body.get("stocks", [])]

    def get_industry(self, industry_name: str) -> list[str]:
        """Return QMT ContextInfo members for one known SW/CSRC industry."""
        body = self._request(
            "POST", "/api/data/industry", {"industry": industry_name}
        )
        return [str(code) for code in body.get("stocks", [])]

    def download_sector_data(self) -> None:
        raise QMTBridgeError("sector catalog refresh is not supported by ContextInfo bridge")

    def download_etf_info(self) -> None:
        raise QMTBridgeError("ETF constituent weights are deferred for QMT bridge")

    def get_etf_info(self) -> dict[str, Any]:
        raise QMTBridgeError("ETF constituent weights are deferred for QMT bridge")

    def get_sector_list(self) -> list[str]:
        raise QMTBridgeError("sector catalog is provided by AKShare, not ContextInfo bridge")

    def get_instrument_detail(
        self, stock_list: str | list[str], iscomplete: bool = False
    ) -> dict[str, dict[str, Any]] | dict[str, Any]:
        scalar = isinstance(stock_list, str)
        stocks = [stock_list] if scalar else list(stock_list)
        result: dict[str, dict[str, Any]] = {}
        for batch in _chunks(stocks, 200):
            body = self._request(
                "POST",
                "/api/data/instrument_detail",
                {"stock_list": ",".join(batch), "iscomplete": iscomplete},
            )
            for code, detail in (body.get("data") or {}).items():
                if isinstance(detail, dict) and detail.get("error"):
                    raise QMTBridgeError(f"instrument detail failed: {code}: {detail['error']}")
                if detail is not None:
                    result[code] = detail
        return result.get(stock_list, {}) if scalar else result

    def get_last_volume(self, stock_code: str) -> int:
        body = self._request(
            "POST", "/api/data/last_volume", {"stockcode": stock_code}
        )
        return int(body.get("last_volume") or 0)

    def get_divid_factors(
        self, stock_code: str, start_time: str = "", end_time: str = ""
    ) -> pd.DataFrame:
        body = self._request(
            "POST", "/api/data/divid_factors", {"stockcode": stock_code}
        )
        factors = body.get("factors") or {}
        if isinstance(factors, list):
            return self._frame(factors)
        records = []
        for timestamp, values in factors.items():
            if not isinstance(values, list) or len(values) < 7:
                continue
            records.append({
                "time": pd.to_datetime(int(timestamp), unit="ms").strftime("%Y%m%d"),
                "factor": values[6],
            })
        frame = self._frame(records)
        if start_time or end_time:
            frame = frame.loc[start_time or None:end_time or None]
        return frame

