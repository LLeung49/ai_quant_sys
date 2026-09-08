"""Capture a source-hashed, dated authoritative blue-chip constituent basket."""

from __future__ import annotations

from collections.abc import Callable, Mapping, Sequence
from datetime import date, datetime
import json
import math

from .bluechip_basket import BlueChipBasket, BlueChipConstituent
from .source_snapshots import SourceSnapshot, _snapshot


class BlueChipSnapshotStore:
    """Transactional writer for one immutable source snapshot and its PIT basket."""

    def __init__(self, *, connection_factory: Callable[[], object]) -> None:
        if not callable(connection_factory):
            raise ValueError("connection_factory must be callable")
        self._connection_factory = connection_factory

    def persist(self, source: SourceSnapshot, basket: BlueChipBasket) -> None:
        if not isinstance(source, SourceSnapshot) or not isinstance(basket, BlueChipBasket):
            raise ValueError("source and basket are required")
        if source.as_of_date != basket.as_of_date or any(
            member.source_hash != source.source_hash for member in basket.members
        ):
            raise ValueError("source snapshot must exactly back the PIT basket")
        conn = self._connection_factory()
        try:
            cursor = conn.cursor()  # type: ignore[attr-defined]
            try:
                cursor.execute(
                    """INSERT INTO asset_allocation_etf_research_source_snapshot
                    (source_hash, source_name, source_kind, captured_at, as_of_date, payload_json)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE source_hash = VALUES(source_hash)""",
                    (source.source_hash, source.source_name, source.source_kind,
                     source.captured_at, source.as_of_date,
                     json.dumps(dict(source.payload), ensure_ascii=False, sort_keys=True)),
                )
                for member in basket.members:
                    cursor.execute(
                        """INSERT INTO asset_allocation_etf_research_constituent_pit
                        (index_code, as_of_date, stock_code, weight, source_hash)
                        VALUES (%s, %s, %s, %s, %s)
                        ON DUPLICATE KEY UPDATE weight = VALUES(weight), source_hash = VALUES(source_hash)""",
                        (basket.index_code, basket.as_of_date, member.stock_code,
                         member.weight, member.source_hash),
                    )
                conn.commit()  # type: ignore[attr-defined]
            except Exception:
                conn.rollback()  # type: ignore[attr-defined]
                raise
            finally:
                cursor.close()
        finally:
            conn.close()  # type: ignore[attr-defined]


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


__all__ = ["BlueChipSnapshotStore", "capture_constituent_snapshot"]
