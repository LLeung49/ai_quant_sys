"""Provider-neutral contracts for complete daily-market projection batches."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Mapping, Sequence


@dataclass
class MarketBatch:
    stock_code: str
    start_date: date
    end_date: date
    rows_by_mode: dict[str, list[dict]] = field(default_factory=dict)
    provenance: dict[str, object] = field(default_factory=dict)
    failures: dict[str, str] = field(default_factory=dict)
    quarantines: tuple[Mapping[str, object], ...] = ()
    gaps: tuple[Mapping[str, object], ...] = ()

    @property
    def is_complete(self) -> bool:
        return (
            not self.failures
            and set(self.rows_by_mode) == {"none", "front", "back"}
            and all(self.rows_by_mode.values())
        )


class MarketProvider:
    def fetch_batch(
        self, stock_code: str, start_date: date, end_date: date
    ) -> MarketBatch:
        raise NotImplementedError
