"""Read-only, effective-dated index constituent access for layered equities."""

from __future__ import annotations

from datetime import date, datetime
from types import MappingProxyType
from typing import Mapping, Protocol, Sequence

from .contracts import DataQualityError, DataQualityIssue


SUPPORTED_CONSTITUENT_INDEX_CODES = frozenset({"H30269", "931468", "000922"})


class HistoricalConstituentRepository(Protocol):
    """Read-only source for official historical constituent ranges.

    An ingester can implement this protocol once an authoritative membership
    source has been approved.  This package deliberately provides no SQL table
    or write path for those records.
    """

    def load_memberships(self) -> Sequence[Mapping[str, object]]:
        """Return source rows with code and inclusive effective-date ranges."""


class InMemoryHistoricalConstituentRepository:
    """Deterministic read-only adapter for tests and offline fixtures."""

    def __init__(self, rows: Sequence[Mapping[str, object]]) -> None:
        self._rows = tuple(MappingProxyType(dict(row)) for row in rows)

    def load_memberships(self) -> tuple[Mapping[str, object], ...]:
        return self._rows


class InMemoryInstrumentMetadataRepository:
    """Deterministic read-only adapter for dated instrument metadata."""

    def __init__(self, rows: Sequence[Mapping[str, object]]) -> None:
        self._rows = tuple(MappingProxyType(dict(row)) for row in rows)

    def load_metadata(self) -> tuple[Mapping[str, object], ...]:
        return self._rows


def _as_date(value: object, field_name: str) -> date:
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        try:
            return date.fromisoformat(value)
        except ValueError as exc:
            raise ValueError(f"invalid {field_name}") from exc
    raise ValueError(f"invalid {field_name}")


def _as_code(value: object, field_name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"invalid {field_name}")
    return value.strip().upper()


class HistoricalConstituentProvider:
    """Resolve only official constituent ranges covering an as-of date."""

    def __init__(self, repository: HistoricalConstituentRepository) -> None:
        if not callable(getattr(repository, "load_memberships", None)):
            raise ValueError("repository must provide load_memberships")
        self._repository = repository
        self.last_quality_issues: tuple[DataQualityIssue, ...] = ()

    def _fail(self, code: str, stock_code: str, message: str) -> None:
        issue = DataQualityIssue(code, stock_code, None, message)
        self.last_quality_issues = (issue,)
        raise DataQualityError(message, self.last_quality_issues)

    def members(self, as_of_date: date, index_code: str) -> tuple[str, ...]:
        """Return sorted members whose inclusive range covers ``as_of_date``."""

        if not isinstance(as_of_date, date) or isinstance(as_of_date, datetime):
            raise ValueError("as_of_date must be a date")
        try:
            requested_index = _as_code(index_code, "index_code")
        except ValueError:
            raise ValueError("index_code must be a non-empty string") from None
        if requested_index not in SUPPORTED_CONSTITUENT_INDEX_CODES:
            self._fail(
                "unsupported_constituent_index",
                requested_index,
                "index is outside the approved historical constituent sources",
            )
        self.last_quality_issues = ()
        try:
            rows = self._repository.load_memberships()
        except Exception as exc:
            self._fail(
                "constituent_source_unavailable",
                requested_index,
                f"historical constituent source unavailable: {exc}",
            )
        if not isinstance(rows, Sequence):
            self._fail(
                "constituent_source_unavailable",
                requested_index,
                "historical constituent source returned an invalid response",
            )

        members: set[str] = set()
        for row in rows:
            if not isinstance(row, Mapping):
                self._fail(
                    "invalid_constituent_record",
                    requested_index,
                    "historical constituent source contains an invalid record",
                )
            try:
                row_index = _as_code(row.get("index_code"), "index_code")
            except ValueError:
                self._fail(
                    "invalid_constituent_index",
                    requested_index,
                    "historical constituent record has an invalid index code",
                )
            if row_index != requested_index:
                continue
            try:
                stock_code = _as_code(row.get("stock_code"), "stock_code")
            except ValueError:
                self._fail(
                    "invalid_constituent_stock_code",
                    requested_index,
                    "historical constituent record has an invalid stock code",
                )
            if row.get("effective_start") is None or row.get("effective_end") is None:
                self._fail(
                    "missing_constituent_effective_range",
                    stock_code,
                    "historical constituent record requires an effective date range",
                )
            try:
                effective_start = _as_date(row.get("effective_start"), "effective_start")
                effective_end = _as_date(row.get("effective_end"), "effective_end")
            except ValueError:
                self._fail(
                    "invalid_constituent_effective_range",
                    stock_code,
                    "historical constituent record has an invalid effective date range",
                )
            if effective_end < effective_start:
                self._fail(
                    "invalid_constituent_effective_range",
                    stock_code,
                    "historical constituent record ends before it starts",
                )
            if effective_start <= as_of_date <= effective_end:
                if stock_code in members:
                    self._fail(
                        "duplicate_constituent_membership",
                        stock_code,
                        "historical constituent source contains duplicate active membership",
                    )
                members.add(stock_code)
        return tuple(sorted(members))
