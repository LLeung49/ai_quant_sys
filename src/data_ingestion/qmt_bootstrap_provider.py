"""Temporary QMT Bridge reader for the staging-only market rebuild."""

from __future__ import annotations

from datetime import date, datetime, timezone
import hashlib
import json
from typing import Sequence

from data_ingestion_qmt.qmt_data_gateway import QMTDataGateway

from .market_provider import MarketBatch
from .market_row_validation import validate_market_row, validate_projection_batch
from .market_volume_contract import normalize_to_lot


MODES = ("none", "front", "back")
FIELDS = ("open", "high", "low", "close", "volume", "amount", "preClose", "suspendFlag")


def _trade_date(value: object) -> str:
    text = str(value)
    if len(text) < 8:
        raise ValueError(f"invalid QMT trade date: {value!r}")
    return f"{text[:4]}-{text[4:6]}-{text[6:8]}"


def _optional_float(row, field: str) -> float | None:
    value = row.get(field)
    if value is None or value != value:
        return None
    return float(value)


class QMTBootstrapProvider:
    """Read bridge data, discard fill rows, and return complete market batches."""

    def __init__(self, *, gateway: QMTDataGateway | None = None) -> None:
        self.gateway = gateway or QMTDataGateway.from_env()

    def _normalize_frame(self, stock_code: str, mode: str, frame):
        rows: list[dict] = []
        gaps: list[dict] = []
        quarantines: list[dict] = []
        for index_value, source in frame.iterrows():
            trade_date = _trade_date(index_value)
            prices = [float(source[field]) for field in ("open", "high", "low", "close")]
            if all(price == 0 for price in prices):
                gaps.append({
                    "stock_code": stock_code,
                    "trade_date": trade_date,
                    "mode": mode,
                    "reason": "zero_price_fill",
                    "suspend_flag": _optional_float(source, "suspendFlag"),
                })
                continue
            raw_volume = float(source["volume"])
            amount = float(source["amount"])
            if raw_volume == 0 and amount == 0:
                volume = 0
            else:
                volume = normalize_to_lot(amount, prices[3], raw_volume)
            row = {
                "stock_code": stock_code,
                "trade_date": trade_date,
                "open_price": prices[0],
                "high_price": prices[1],
                "low_price": prices[2],
                "close_price": prices[3],
                "volume": volume,
                "amount": amount,
                "turnover_rate": None,
            }
            if mode == "none":
                row.update({
                    "pre_close": _optional_float(source, "preClose"),
                    "suspend_flag": (
                        int(value) if (value := _optional_float(source, "suspendFlag")) is not None
                        else None
                    ),
                    "data_source": "qmt_bridge_rebuild",
                })
            validation = validate_market_row(row, allow_negative_price=(mode == "front"))
            if not validation.is_valid:
                codes = sorted({issue.code for issue in validation.issues if issue.severity == "error"})
                raise ValueError(f"invalid_market_row {stock_code}/{trade_date}/{mode}: {codes}")
            if validation.quarantined:
                quarantines.append({
                    "stock_code": stock_code,
                    "trade_date": trade_date,
                    "mode": mode,
                    "issues": [issue.code for issue in validation.issues],
                })
            rows.append(row)
        return rows, gaps, quarantines

    def fetch_batches(
        self, stock_codes: Sequence[str], start_date: date, end_date: date
    ) -> dict[str, MarketBatch]:
        codes = list(dict.fromkeys(stock_codes))
        if not codes:
            return {}
        if start_date > end_date:
            raise ValueError("start_date must not exceed end_date")
        rows_by_code = {code: {} for code in codes}
        failures_by_code = {code: {} for code in codes}
        gaps_by_code = {code: [] for code in codes}
        quarantines_by_code = {code: [] for code in codes}
        for mode in MODES:
            try:
                frames = self.gateway.get_market_data_ex(
                    field_list=list(FIELDS),
                    stock_list=codes,
                    period="1d",
                    start_time=start_date.strftime("%Y%m%d"),
                    end_time=end_date.strftime("%Y%m%d"),
                    dividend_type=mode,
                    fill_data=False,
                )
            except Exception as exc:
                for code in codes:
                    failures_by_code[code][mode] = f"{type(exc).__name__}: {exc}"
                continue
            for code in codes:
                frame = frames.get(code) if frames else None
                if frame is None or len(frame) == 0:
                    failures_by_code[code][mode] = "empty_response"
                    continue
                try:
                    rows, gaps, quarantines = self._normalize_frame(code, mode, frame)
                except Exception as exc:
                    failures_by_code[code][mode] = f"{type(exc).__name__}: {exc}"
                    continue
                if not rows:
                    failures_by_code[code][mode] = "no_valid_rows_after_zero_fill_filter"
                    continue
                rows_by_code[code][mode] = rows
                gaps_by_code[code].extend(gaps)
                quarantines_by_code[code].extend(quarantines)

        fetched_at = datetime.now(timezone.utc).isoformat()
        result: dict[str, MarketBatch] = {}
        for code in codes:
            modes = rows_by_code[code]
            failures = failures_by_code[code]
            if len(modes) == len(MODES):
                validation = validate_projection_batch(modes)
                if not validation.is_valid:
                    failures["batch"] = "; ".join(
                        issue.code for issue in validation.issues if issue.severity == "error"
                    )
            fingerprint = hashlib.sha256(
                json.dumps(modes, sort_keys=True, ensure_ascii=False, default=str).encode("utf-8")
            ).hexdigest()
            result[code] = MarketBatch(
                code,
                start_date,
                end_date,
                rows_by_mode=modes,
                provenance={
                    "provider": "qmt_bridge",
                    "interface": "ContextInfo.get_market_data_ex",
                    "fetched_at": fetched_at,
                    "fingerprint": fingerprint,
                    "volume_unit": "lot",
                    "amount_unit": "yuan",
                },
                failures=failures,
                quarantines=tuple(quarantines_by_code[code]),
                gaps=tuple(gaps_by_code[code]),
            )
        return result

    def fetch_batch(
        self, stock_code: str, start_date: date, end_date: date
    ) -> MarketBatch:
        return self.fetch_batches([stock_code], start_date, end_date)[stock_code]
