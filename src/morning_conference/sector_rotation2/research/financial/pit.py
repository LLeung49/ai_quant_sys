"""PIT status and the strict resolver used by Repair Alpha V1.

Three PIT states are exposed:

``PIT_EXACT``    -- the announcement date is known and verified, so the row
                   is guaranteed to be visible from that date forward.
``PIT_VERIFIED`` -- the announcement date is missing but the source
                   ``first_seen_at`` is anchored in MySQL and can be trusted
                   (manual curation).
``PIT_ESTIMATED``-- the announcement date is unknown; the row uses the
                   ``first_seen_at`` timestamp and is excluded from strict OOS
                   reports.

Strict historical research only consumes ``PIT_EXACT`` and
``PIT_VERIFIED``.  ``PIT_ESTIMATED`` is exposed interactively only when
the caller explicitly opts in via ``allow_estimated_pit``.
"""

from __future__ import annotations

from datetime import date, datetime
from enum import Enum
from typing import Iterable, Mapping

# Re-export the canonical row class so callers can use a single type
# regardless of whether they import from ``pit`` or ``providers.base``.
from .providers.base import FinancialRawRow  # noqa: F401  (re-export)


class PITStatus(str, Enum):
    EXACT = "pit_exact"
    VERIFIED = "pit_verified"
    ESTIMATED = "pit_estimated"
    INVALID = "pit_invalid"


_STRICT_STATUSES = frozenset({PITStatus.EXACT, PITStatus.VERIFIED})


def _to_date(value: object) -> date | None:
    if value is None:
        return None
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    try:
        return date.fromisoformat(str(value)[:10])
    except (ValueError, TypeError):
        return None


def _get(row: object, key: str) -> object:
    """Read ``key`` from either a Mapping or a dataclass instance."""

    if isinstance(row, Mapping):
        return row.get(key)
    return getattr(row, key, None)


def classify_pit(row: object) -> PITStatus:
    """Return the PIT status for one raw row.

    The function accepts either a Mapping or a :class:`FinancialRawRow`
    dataclass instance.  The classification rules:
    - explicit ``pit_status`` if it already classifies the row;
    - ``PIT_EXACT`` when ``announcement_date`` is present and the row has
      not been restated (``is_restated=False``);
    - ``PIT_VERIFIED`` when the announcement date is missing but the
      source has verified ``first_seen_at`` provenance (manual entry);
    - ``PIT_ESTIMATED`` when only ``first_seen_at`` is available;
    - ``PIT_INVALID`` when both dates are missing or unparsable.
    """

    explicit = _get(row, "pit_status")
    if explicit:
        try:
            return PITStatus(str(explicit))
        except ValueError:
            pass
    announcement = _get(row, "announcement_date")
    first_seen = _get(row, "first_seen_at")
    is_restated = bool(_get(row, "is_restated"))
    source_verified = bool(_get(row, "source_verified"))
    if announcement is None and first_seen is None:
        return PITStatus.INVALID
    if announcement is not None and not is_restated:
        return PITStatus.EXACT
    if source_verified and first_seen is not None:
        return PITStatus.VERIFIED
    return PITStatus.ESTIMATED


def resolve_latest_visible(
    rows: Iterable[FinancialRawRow],
    *,
    as_of_date: date,
    allow_estimated_pit: bool = False,
) -> FinancialRawRow | None:
    """Return the latest raw row visible at ``as_of_date``.

    Visibility rules:
    - rows with ``pit_status == INVALID`` are excluded;
    - rows announced (or ``first_seen_at``) strictly after ``as_of_date``
      are excluded;
    - when ``allow_estimated_pit`` is False, ``PIT_ESTIMATED`` rows are
      also excluded (strict mode);
    - on ties the row with the earliest ``first_seen_at`` wins (the
      original record is preferred over a later restatement);
    - rows with ``is_restated=True`` lose to a non-restated sibling.
    """

    target_date = _to_date(as_of_date) or as_of_date
    eligible: list[FinancialRawRow] = []
    for row in rows:
        pit_value = _get(row, "pit_status")
        if pit_value:
            try:
                pit = PITStatus(str(pit_value))
            except ValueError:
                pit = classify_pit(row)
        else:
            pit = classify_pit(row)
        if pit is PITStatus.INVALID:
            continue
        if not allow_estimated_pit and pit is PITStatus.ESTIMATED:
            continue
        availability = _to_date(row.announcement_date or row.first_seen_at)
        if availability is None or availability > target_date:
            continue
        eligible.append(row)
    if not eligible:
        return None
    # Choose the row with the latest availability; tie-break prefers
    # original records (is_restated=False) and the earliest source_hash.
    eligible.sort(
        key=lambda row: (
            -((_to_date(row.announcement_date or row.first_seen_at) or date.min).toordinal()),
            1 if row.is_restated else 0,
            row.source_hash,
        )
    )
    return eligible[0]


def filter_strict(rows: Iterable[FinancialRawRow]) -> list[FinancialRawRow]:
    """Return only the rows that are safe for strict historical research."""

    return [
        row for row in rows
        if classify_pit(row) in _STRICT_STATUSES
    ]


__all__ = [
    "FinancialRawRow",
    "PITStatus",
    "classify_pit",
    "resolve_latest_visible",
    "filter_strict",
    "_STRICT_STATUSES",
]
