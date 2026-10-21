"""Auditable, injected AkShare metadata snapshot adapters."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from datetime import date, datetime
from hashlib import sha256
import json
import math
from types import MappingProxyType
from typing import Any


def _require_date(value: object, field_name: str) -> date:
    if not isinstance(value, date) or isinstance(value, datetime):
        raise ValueError(f"{field_name} must be a date")
    return value


def _normalise_code(value: object) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError("code must be a non-empty string")
    return value.strip().upper()


def _snapshot_hash(
    source_name: str,
    source_kind: str,
    captured_at: datetime,
    as_of_date: date | None,
    payload: Mapping[str, object],
) -> str:
    canonical = {
        "source_name": source_name,
        "source_kind": source_kind,
        "captured_at": captured_at.isoformat(),
        "as_of_date": as_of_date.isoformat() if as_of_date else None,
        "payload": dict(payload),
    }
    encoded = json.dumps(
        canonical, ensure_ascii=False, sort_keys=True, separators=(",", ":"), default=str
    ).encode("utf-8")
    return sha256(encoded).hexdigest()


@dataclass(frozen=True)
class SourceSnapshot:
    """One immutable provider response together with its reproducible identity."""

    source_name: str
    source_kind: str
    captured_at: datetime
    as_of_date: date | None
    payload: Mapping[str, object]
    source_hash: str

    def __post_init__(self) -> None:
        if not isinstance(self.source_name, str) or not self.source_name:
            raise ValueError("source_name must be a non-empty string")
        if not isinstance(self.source_kind, str) or not self.source_kind:
            raise ValueError("source_kind must be a non-empty string")
        if not isinstance(self.captured_at, datetime):
            raise ValueError("captured_at must be a datetime")
        if self.as_of_date is not None:
            _require_date(self.as_of_date, "as_of_date")
        if not isinstance(self.payload, Mapping):
            raise ValueError("payload must be a mapping")
        if (
            not isinstance(self.source_hash, str)
            or len(self.source_hash) != 64
            or any(character not in "0123456789abcdef" for character in self.source_hash)
        ):
            raise ValueError("source_hash must be a SHA-256 hex digest")


def _snapshot(
    *,
    source_name: str,
    source_kind: str,
    captured_at: datetime,
    as_of_date: date | None,
    payload: Mapping[str, object],
) -> SourceSnapshot:
    stable_payload = MappingProxyType(dict(payload))
    return SourceSnapshot(
        source_name=source_name,
        source_kind=source_kind,
        captured_at=captured_at,
        as_of_date=as_of_date,
        payload=stable_payload,
        source_hash=_snapshot_hash(
            source_name, source_kind, captured_at, as_of_date, stable_payload
        ),
    )






def _overview_row(response: object) -> Mapping[str, object]:
    if isinstance(response, Mapping):
        return response
    to_dict = getattr(response, "to_dict", None)
    if callable(to_dict):
        try:
            records = to_dict(orient="records")
        except (TypeError, ValueError):
            records = None
        if isinstance(records, Sequence) and len(records) == 1 and isinstance(records[0], Mapping):
            return records[0]
    raise ValueError("AkShare fund overview unavailable")


def _first_text(row: Mapping[str, object], *keys: str) -> str:
    for key in keys:
        value = row.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    raise ValueError(f"AkShare fund overview missing {keys[0]}")


def _fee(value: object, field_name: str) -> float:
    if isinstance(value, bool) or value is None:
        raise ValueError(f"AkShare fund overview missing {field_name}")
    text = str(value).strip()
    if not text:
        raise ValueError(f"AkShare fund overview missing {field_name}")
    try:
        fee = float(text.rstrip("%"))
    except ValueError as exc:
        raise ValueError(f"invalid {field_name}") from exc
    if not math.isfinite(fee) or fee < 0:
        raise ValueError(f"invalid {field_name}")
    return fee / 100 if text.endswith("%") or fee >= 0.1 else fee


class AkShareSnapshotClient:
    """Snapshot the fund-level metadata needed for executable ETF mappings."""

    def __init__(self, client: object) -> None:
        if client is None:
            raise ValueError("client is required")
        self._client = client

    def fund_overview(self, code: str, captured_at: datetime) -> SourceSnapshot:
        normalized_code = _normalise_code(code).split(".", maxsplit=1)[0]
        if not normalized_code.isdigit() or len(normalized_code) != 6:
            raise ValueError("code must contain a six-digit fund symbol")
        if not isinstance(captured_at, datetime):
            raise ValueError("captured_at must be a datetime")
        try:
            response = self._client.fund_overview_em(symbol=normalized_code)  # type: ignore[attr-defined]
            row = _overview_row(response)
            payload = {
                "code": normalized_code,
                "fund_name": _first_text(row, "基金简称", "基金名称", "基金全称"),
                "tracking_benchmark": _first_text(
                    row, "跟踪标的", "跟踪指数", "业绩比较基准"
                ),
                "management_fee": _fee(row.get("管理费率"), "管理费率"),
                "custody_fee": _fee(row.get("托管费率"), "托管费率"),
            }
        except ValueError:
            raise
        except Exception as exc:
            raise ValueError("AkShare fund overview unavailable") from exc
        return _snapshot(
            source_name="akshare",
            source_kind="fund_overview",
            captured_at=captured_at,
            as_of_date=captured_at.date(),
            payload=payload,
        )


__all__ = ["AkShareSnapshotClient", "SourceSnapshot"]
