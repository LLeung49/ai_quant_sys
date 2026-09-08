"""Read-only point-in-time blue-chip constituent basket resolution."""
from __future__ import annotations

from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from datetime import date, datetime
import math

Query = Callable[[str, tuple[object, ...]], Sequence[Mapping[str, object]]]

PIT_CONSTITUENTS_SQL = """
SELECT index_code, as_of_date, stock_code, weight, source_hash
FROM asset_allocation_etf_research_constituent_pit
WHERE index_code = %s AND as_of_date = %s
ORDER BY stock_code
"""

@dataclass(frozen=True)
class BlueChipConstituent:
    stock_code: str
    weight: float
    source_hash: str

@dataclass(frozen=True)
class BlueChipBasket:
    index_code: str
    as_of_date: date
    members: tuple[BlueChipConstituent, ...]

class BlueChipBasketRepository:
    def __init__(self, query: Query) -> None:
        if not callable(query): raise ValueError("query must be callable")
        self._query = query

    def load(self, index_code: str, as_of_date: date) -> BlueChipBasket:
        if not isinstance(index_code, str) or not index_code.strip(): raise ValueError("index_code must be non-empty")
        if not isinstance(as_of_date, date) or isinstance(as_of_date, datetime): raise ValueError("as_of_date must be a date")
        rows = self._query(PIT_CONSTITUENTS_SQL, (index_code, as_of_date))
        if not rows: raise ValueError("no PIT constituents for requested date")
        members=[]; seen=set()
        for row in rows:
            code=str(row.get("stock_code") or "").strip().upper()
            source=str(row.get("source_hash") or "").strip().lower()
            if not code: raise ValueError("stock_code is required")
            if code in seen: raise ValueError("duplicate blue-chip constituent")
            if len(source)!=64 or any(c not in "0123456789abcdef" for c in source): raise ValueError("source_hash must be a SHA-256 hex digest")
            try: weight=float(row.get("weight"))
            except (TypeError, ValueError) as exc: raise ValueError("invalid constituent weight") from exc
            if not math.isfinite(weight) or weight <= 0: raise ValueError("invalid constituent weight")
            seen.add(code); members.append(BlueChipConstituent(code, weight, source))
        if not math.isclose(sum(member.weight for member in members),1.0,rel_tol=0.0,abs_tol=1e-9): raise ValueError("constituent weights must sum to 1")
        return BlueChipBasket(index_code.strip(), as_of_date, tuple(members))

__all__=["BlueChipBasket","BlueChipConstituent","BlueChipBasketRepository","PIT_CONSTITUENTS_SQL"]
