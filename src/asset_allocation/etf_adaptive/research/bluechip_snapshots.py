"""Capture a source-hashed, dated authoritative blue-chip constituent basket."""

from __future__ import annotations

from collections.abc import Callable, Mapping, Sequence
from datetime import date, datetime
import math

from .bluechip_basket import BlueChipBasket, BlueChipConstituent
from .source_snapshots import _snapshot


def _source_date(value: object) -> date:
    if isinstance(value, date) and not isinstance(value, datetime):
        return value
    if isinstance(value, str):
        try:
            return date.fromisoformat(value)
        except ValueError:
            pass
    raise ValueError("constituent source must provide as_of_date")


def capture_constituent_snapshot(
    index_code: str,
    as_of_date: date,
    client: object,
    *,
    clock: Callable[[], datetime] = datetime.now,
) -> BlueChipBasket:
    """Capture only a source response that states the exact requested date.

    A current constituent list is never accepted for an historical request.
    Persistence is deliberately a separate explicit database action.
    """

    if not isinstance(index_code, str) or not index_code.strip():
        raise ValueError("index_code must be non-empty")
    if not isinstance(as_of_date, date) or isinstance(as_of_date, datetime):
        raise ValueError("as_of_date must be a date")
    if not callable(clock):
        raise ValueError("clock must be callable")
    try:
        response = client.index_constituents(index_code.strip(), as_of_date)  # type: ignore[attr-defined]
    except Exception as exc:
        raise ValueError("authoritative constituent source unavailable") from exc
    if not isinstance(response, Mapping):
        raise ValueError("authoritative constituent source unavailable")
    if _source_date(response.get("as_of_date")) != as_of_date:
        raise ValueError("constituent source as_of_date does not match request")
    rows = response.get("constituents")
    if not isinstance(rows, Sequence) or isinstance(rows, (str, bytes)) or not rows:
        raise ValueError("constituent source must provide members")
    snapshot = _snapshot(
        source_name=str(getattr(client, "source_name", "authoritative_index")),
        source_kind="index_constituents",
        captured_at=clock(),
        as_of_date=as_of_date,
        payload={"index_code": index_code.strip(), "response": dict(response)},
    )
    members: list[BlueChipConstituent] = []
    seen: set[str] = set()
    for row in rows:
        if not isinstance(row, Mapping):
            raise ValueError("constituent source member is invalid")
        code = str(row.get("stock_code") or "").strip().upper()
        if not code or code in seen:
            raise ValueError("constituent source stock_code is invalid")
        try:
            weight = float(row["weight"])
        except (KeyError, TypeError, ValueError) as exc:
            raise ValueError("constituent source weight is required") from exc
        if not math.isfinite(weight) or weight <= 0:
            raise ValueError("constituent source weight is invalid")
        seen.add(code)
        members.append(BlueChipConstituent(code, weight, snapshot.source_hash))
    if not math.isclose(sum(member.weight for member in members), 1.0, abs_tol=1e-9):
        raise ValueError("constituent source weights must sum to 1")
    return BlueChipBasket(index_code.strip(), as_of_date, tuple(members))


__all__ = ["capture_constituent_snapshot"]
