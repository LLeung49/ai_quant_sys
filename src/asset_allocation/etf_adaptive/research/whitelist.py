"""Read-only resolver for versioned, effective-dated ETF mappings."""

from __future__ import annotations

from datetime import date, datetime
from typing import Callable, Mapping, Sequence

from ..contracts import SubLayer
from .benchmark_contracts import WhitelistEntry


Query = Callable[[str, tuple[object, ...]], Sequence[Mapping[str, object]]]


ACTIVE_WHITELIST_SQL = """
SELECT w.exposure_id, w.sub_layer, w.primary_code, w.backup_code,
       w.effective_from, w.effective_to, w.source_hash, w.valuation_multiplier
FROM asset_allocation_etf_research_whitelist_entry AS w
JOIN asset_allocation_etf_research_whitelist_version AS v
  ON v.id = w.whitelist_version_id
WHERE v.status = 'approved'
  AND w.effective_from <= %s
  AND (w.effective_to IS NULL OR w.effective_to >= %s)
ORDER BY w.exposure_id, w.effective_from, w.id
"""


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


def _required(row: Mapping[str, object], field_name: str) -> object:
    value = row.get(field_name)
    if value is None or (isinstance(value, str) and not value.strip()):
        raise ValueError(f"missing {field_name}")
    return value


class WhitelistRepository:
    """Resolve approved rows without substituting exposures or source evidence."""

    def __init__(self, query: Query) -> None:
        if not callable(query):
            raise ValueError("query must be callable")
        self._query = query

    def load(self, as_of_date: date) -> tuple[WhitelistEntry, ...]:
        """Return the one approved active mapping for each exposure at ``as_of_date``."""

        if not isinstance(as_of_date, date) or isinstance(as_of_date, datetime):
            raise ValueError("as_of_date must be a date")
        rows = self._query(ACTIVE_WHITELIST_SQL, (as_of_date, as_of_date))
        if not rows:
            raise ValueError("no active whitelist entries for requested date")
        entries: list[WhitelistEntry] = []
        seen_exposures: set[str] = set()
        for row in rows:
            if not isinstance(row, Mapping):
                raise ValueError("whitelist query returned a non-mapping row")
            exposure_id = str(_required(row, "exposure_id")).strip()
            if exposure_id in seen_exposures:
                raise ValueError(f"duplicate active exposure: {exposure_id}")
            try:
                entry = WhitelistEntry(
                    exposure_id=exposure_id,
                    sub_layer=SubLayer(str(_required(row, "sub_layer")).strip()),
                    primary_code=str(_required(row, "primary_code")).strip(),
                    backup_code=str(_required(row, "backup_code")).strip(),
                    effective_from=_as_date(
                        _required(row, "effective_from"), "effective_from"
                    ),
                    effective_to=(
                        _as_date(row["effective_to"], "effective_to")
                        if row.get("effective_to") is not None
                        else None
                    ),
                    source_hash=str(_required(row, "source_hash")).strip(),
                    valuation_multiplier=float(
                        _required(row, "valuation_multiplier")
                    ),
                )
            except (TypeError, ValueError) as exc:
                raise ValueError(f"invalid whitelist entry {exposure_id}: {exc}") from exc
            if not (entry.effective_from <= as_of_date) or (
                entry.effective_to is not None and entry.effective_to < as_of_date
            ):
                raise ValueError(
                    f"whitelist entry {entry.exposure_id} is outside requested date"
                )
            seen_exposures.add(exposure_id)
            entries.append(entry)
        return tuple(entries)


__all__ = ["ACTIVE_WHITELIST_SQL", "WhitelistRepository"]
