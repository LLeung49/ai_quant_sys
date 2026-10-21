"""AKShare-backed, announcement-date-safe financial statement provider."""

from __future__ import annotations

from collections.abc import Callable
from datetime import date, datetime
import hashlib
import json
from typing import Any

import akshare as ak
import pandas as pd


def _symbol(stock_code: str) -> str:
    code, exchange = stock_code.split(".", 1)
    return f"{exchange.upper()}{code}"


def _date(value: Any, *, field: str) -> date:
    if value is None or pd.isna(value):
        raise ValueError(f"invalid {field}: {value!r}")
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    text = str(value or "").strip()[:10]
    if not text or text.startswith("0000-00-00"):
        raise ValueError(f"invalid {field}: {value!r}")
    try:
        return date.fromisoformat(text)
    except ValueError as exc:
        raise ValueError(f"invalid {field}: {value!r}") from exc


def _number(row: dict[str, Any], *names: str) -> float | None:
    for name in names:
        value = row.get(name)
        if value is not None and not pd.isna(value):
            return float(value)
    return None


def _ratio(numerator: float | None, denominator: float | None) -> float | None:
    if numerator is None or denominator in (None, 0):
        return None
    return round(numerator / denominator * 100, 4)


class AKShareFinancialProvider:
    def __init__(
        self,
        *,
        fetch_balance: Callable[[str], pd.DataFrame] = ak.stock_balance_sheet_by_report_em,
        fetch_income: Callable[[str], pd.DataFrame] = ak.stock_profit_sheet_by_report_em,
        fetch_cash: Callable[[str], pd.DataFrame] = ak.stock_cash_flow_sheet_by_report_em,
        fetch_capital: Callable[..., pd.DataFrame] = ak.stock_share_change_cninfo,
        min_report_date: date = date(2015, 1, 1),
    ) -> None:
        self._fetchers = {
            "balance": fetch_balance,
            "income": fetch_income,
            "cash": fetch_cash,
        }
        self._fetch_capital = fetch_capital
        self._min_report_date = min_report_date

    def fetch_capital(self, stock_code: str, *, as_of_date: date) -> list[dict[str, Any]]:
        """Fetch disclosed share-count changes and normalize AKShare's 10k-share units."""
        symbol = stock_code.split(".", 1)[0]
        frame = self._fetch_capital(
            symbol=symbol, start_date="19900101", end_date=as_of_date.strftime("%Y%m%d")
        )
        if frame is None or frame.empty:
            return []
        output: list[dict[str, Any]] = []
        for source in frame.to_dict(orient="records"):
            report_value = source.get("变动日期")
            announcement_value = source.get("公告日期")
            if (report_value is None or pd.isna(report_value)
                    or announcement_value is None or pd.isna(announcement_value)):
                continue
            report_date = _date(report_value, field="capital report date")
            announcement_date = _date(announcement_value, field="capital announcement date")
            if report_date > as_of_date or announcement_date > as_of_date:
                continue

            def shares(*names: str) -> float | None:
                value = next((source.get(name) for name in names if source.get(name) is not None), None)
                if value is None or pd.isna(value):
                    return None
                number = float(value)
                if number < 0:
                    raise ValueError(f"negative share count: {stock_code}/{report_date}")
                return number * 10000

            total = shares("总股本")
            circulating = shares("已流通股份")
            if total is None and circulating is None:
                continue
            normalized = {
                "stock_code": stock_code,
                "report_date": report_date,
                "announcement_date": announcement_date,
                "total_shares": total,
                "circulating_shares": circulating,
                "pit_status": "pit_exact",
                "data_source": "akshare",
                "source_payload": source,
            }
            normalized["source_hash"] = hashlib.sha256(
                json.dumps(normalized, sort_keys=True, default=str).encode("utf-8")
            ).hexdigest()
            output.append(normalized)
        return output

    @staticmethod
    def _index(frame: pd.DataFrame) -> dict[date, dict[str, Any]]:
        indexed: dict[date, dict[str, Any]] = {}
        for record in frame.to_dict(orient="records"):
            report_date = _date(record.get("REPORT_DATE"), field="report date")
            indexed[report_date] = record
        return indexed

    def fetch(self, stock_code: str, *, as_of_date: date) -> list[dict[str, Any]]:
        symbol = _symbol(stock_code)
        statements = {
            name: self._index(fetch(symbol))
            for name, fetch in self._fetchers.items()
        }
        report_dates = sorted(set().union(*(rows.keys() for rows in statements.values())))
        output: list[dict[str, Any]] = []
        for report_date in report_dates:
            if report_date < self._min_report_date:
                continue
            parts = [rows.get(report_date, {}) for rows in statements.values()]
            notices = [
                _date(part.get("NOTICE_DATE"), field="announcement date")
                for part in parts
                if part and part.get("NOTICE_DATE") is not None
            ]
            if not notices:
                raise ValueError(f"missing announcement date: {stock_code}/{report_date}")
            original_announcement_date = max(notices)
            updated_values = [
                _date(part.get("UPDATE_DATE"), field="update date")
                for part in parts
                if part and part.get("UPDATE_DATE") is not None
            ]
            availability_date = max(
                [original_announcement_date, *updated_values]
            )
            if report_date > as_of_date or availability_date > as_of_date:
                continue

            balance = statements["balance"].get(report_date, {})
            income = statements["income"].get(report_date, {})
            cash = statements["cash"].get(report_date, {})
            revenue = _number(income, "TOTAL_OPERATE_INCOME", "OPERATE_INCOME")
            net_profit = _number(income, "PARENT_NETPROFIT", "NETPROFIT")
            # TOTAL_OPERATE_COST includes expenses beyond cost of goods sold.
            operating_cost = _number(income, "OPERATE_COST")
            total_assets = _number(balance, "TOTAL_ASSETS")
            total_liabilities = _number(balance, "TOTAL_LIABILITIES", "TOTAL_LIAB")
            total_equity = _number(
                balance, "TOTAL_EQUITY", "TOTAL_PARENT_EQUITY", "PARENT_EQUITY"
            )
            current_assets = _number(balance, "TOTAL_CURRENT_ASSETS")
            current_liabilities = _number(
                balance, "TOTAL_CURRENT_LIAB", "TOTAL_CURRENT_LIABILITIES"
            )
            gross_margin = (
                _ratio(revenue - operating_cost, revenue)
                if revenue is not None and operating_cost is not None
                else None
            )
            row = {
                "stock_code": stock_code,
                "source_table": "akshare_eastmoney_financial",
                "report_date": report_date,
                "announcement_date": availability_date,
                "original_announcement_date": original_announcement_date,
                "metric_available_at": availability_date,
                "period_type": "quarterly",
                "revenue": revenue,
                "net_profit": net_profit,
                "eps": _number(income, "BASIC_EPS"),
                "roe": _ratio(net_profit, total_equity),
                "roa": _ratio(net_profit, total_assets),
                "gross_margin": gross_margin,
                "net_margin": _ratio(net_profit, revenue),
                "debt_ratio": _ratio(total_liabilities, total_assets),
                "current_ratio": (
                    round(current_assets / current_liabilities, 4)
                    if current_assets is not None and current_liabilities not in (None, 0)
                    else None
                ),
                "operating_cash_flow": _number(cash, "NETCASH_OPERATE"),
                "total_assets": total_assets,
                "total_equity": total_equity,
                "pit_status": "pit_exact",
                "source_updated_at": availability_date,
                "is_restated": int(availability_date > original_announcement_date),
                "source_verified": 1,
                "data_source": "akshare",
                "source_payload": {"balance": balance, "income": income, "cash": cash},
            }
            row["source_hash"] = hashlib.sha256(
                json.dumps(row, sort_keys=True, default=str).encode("utf-8")
            ).hexdigest()
            output.append(row)
        return output


__all__ = ["AKShareFinancialProvider"]
