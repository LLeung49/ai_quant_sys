"""Service layer for building PIT-safe Repair Alpha candidates."""

from __future__ import annotations

from collections.abc import Callable, Iterable, Mapping
from dataclasses import dataclass
from dataclasses import replace
from datetime import date
from typing import Any, Optional

import numpy as np
import pandas as pd

from data_ingestion.db_config import execute_query

from ..config_hash import build_config_hash
from ..contracts import CandidateSnapshot
from ..availability import AvailabilityMetadata
from ..snapshot import (
    SnapshotStore, persist_backfill_snapshot, persist_delayed_shadow_snapshot,
    persist_live_shadow_snapshot,
)
from ..status import ExecutionStatus, ResearchStatus, SnapshotMode, ValidationStatus
from .capital import resolve_capital
from .providers import MiniQMTProvider
from .providers.base import FinancialProvider
from .quality import QualityComponents, score_quality
from .ttm import build_ttm
from .valuation import build_valuation


@dataclass(frozen=True)
class RepairSectorContext:
    """Identity of the upstream sector_opportunity snapshot feeding Repair Alpha."""

    as_of_date: date
    sector_level: int
    sector_name: str
    model_version: str
    config_hash: str
    snapshot_mode: SnapshotMode


REPAIR_PLAYBOOKS = frozenset({"repair_probe", "early_repair"})


def load_repair_sectors(
    as_of_date: str,
    sector_level: int,
    snapshot_mode: SnapshotMode,
    query: Callable = execute_query,
) -> list[Mapping[str, Any]]:
    """Return canonical sector_opportunity snapshots in a repair playbook.

    Playbook is stored in JSON, so filtering happens in Python.
    """

    rows = query(
        """SELECT sector_name, candidate_status, model_version, config_hash, snapshot_mode, feature_json
             FROM (
                SELECT sector_name, candidate_status, model_version, config_hash, snapshot_mode, feature_json,
                       ROW_NUMBER() OVER (
                           PARTITION BY sector_name ORDER BY created_at DESC, id DESC
                       ) AS canonical_rank
                FROM research_candidate_snapshot
                WHERE as_of_date=%s AND sector_level=%s AND entity_type='sector'
                  AND strategy_type='sector_opportunity' AND snapshot_mode=%s
             ) AS canonical_sector_snapshot
             WHERE canonical_rank=1
             ORDER BY sector_name ASC""",
        (as_of_date, sector_level, snapshot_mode.value),
    )

    repair_sectors: list[Mapping[str, Any]] = []
    for row in rows:
        feature_json = row.get("feature_json")
        if isinstance(feature_json, str):
            try:
                import json
                feature_json = json.loads(feature_json)
            except (TypeError, ValueError):
                feature_json = {}
        if not isinstance(feature_json, Mapping):
            continue
        if feature_json.get("playbook") in REPAIR_PLAYBOOKS:
            repair_sectors.append(row)
    return repair_sectors


def _raw_close_lookup(
    query: Callable[[str, tuple[object, ...]], list[dict[str, Any]]],
    as_of_date: date,
) -> dict[str, float]:
    """Fetch raw close for all stocks on ``as_of_date`` (single batched query)."""

    rows = query(
        """SELECT stock_code, close_price AS close
             FROM trade_stock_daily_qfq
            WHERE trade_date = %s""",
        (as_of_date,),
    )
    return {str(r["stock_code"]): float(r["close"]) for r in rows if r.get("close") is not None}


def _dispatch_provider(
    query: Callable,
    provider: FinancialProvider | None = None,
) -> FinancialProvider:
    """Return a provider that reads from ``query`` if no explicit provider supplied."""

    if provider is not None:
        return provider
    return MiniQMTProvider(fetch=query)


def _score_one_stock(
    raw_rows_for_stock: list,
    *,
    stock_code: str,
    raw_close: float,
    sector_name: str,
    target: date,
    allow_estimated_pit: bool,
    capital_rows_for_stock: list | None = None,
) -> dict[str, Any] | None:
    """Build a single Repair Alpha score row for ``stock_code``.

    Builds a TTM projection from all four quarterly rows visible at
    ``target``.  Falls back to ``None`` whenever the upstream is missing
    the trailing 4 quarters.
    """

    if not raw_rows_for_stock:
        return None
    from .pit import resolve_latest_visible
    ttm = build_ttm(raw_rows_for_stock, as_of_date=target)
    if ttm is None:
        return None
    latest = resolve_latest_visible(
        raw_rows_for_stock, as_of_date=target, allow_estimated_pit=allow_estimated_pit,
    )
    if latest is None:
        return None
    capital_rows_for_stock = capital_rows_for_stock or []
    capital = resolve_capital(capital_rows_for_stock, as_of_date=target)
    return _build_row_from_ttm(
        latest=latest, ttm=ttm, raw_close=raw_close, sector_name=sector_name,
        capital=capital,
    )


def _build_row_from_ttm(*, latest, ttm, raw_close: float, sector_name: str, capital=None) -> dict[str, Any] | None:
    """Build a score row from a TTM projection (shared with score_repair_sector)."""

    from .providers.base import CapitalRow
    from .capital import ResolvedCapital
    if capital is None:
        capital = ResolvedCapital(
            stock_code=latest.stock_code, as_of_date=ttm.as_of_date,
            report_date=ttm.period_end_date,
            announcement_date=latest.announcement_date or ttm.period_end_date,
            total_shares=None, circulating_shares=None,
            source_hash=latest.source_hash, data_source=latest.data_source,
        )
    valuation = build_valuation(
        ttm=ttm, capital=capital, raw_close=raw_close,
        sector_name=sector_name, total_equity=latest.total_equity,
    )
    quality = score_quality(
        ttm,
        net_profit_history=None,
        total_equity=latest.total_equity,
        total_assets=latest.total_assets,
        total_liabilities=None,
    )
    pe_z = (valuation.pe - 12.0) / 5.0 if valuation.pe is not None else 0.0
    pb_z = (valuation.pb - 2.0) / 0.5 if valuation.pb is not None else 0.0
    n_components = int(valuation.pe is not None) + int(valuation.pb is not None)
    avg_z = (pe_z + pb_z) / n_components if n_components else 0.0
    rank = -avg_z
    score = (rank + 3.0) / 6.0
    score = max(0.0, min(1.0, score))
    if valuation.pe is None:
        status = "value_trap"
    elif rank >= 0:
        status = "repair_full"
    else:
        status = "repair_value"
    return {
        "stock_code": latest.stock_code,
        "candidate_score": score,
        "candidate_status": status,
        "valuation_rank": rank,
        "quality_score": quality.roe,
        "technical_score": 0.0,
        "momentum_score": quality.earnings_momentum,
        "risk_penalty": 0.0,
        "attribution": {
            "valuation_rank": rank,
            "quality_roe": quality.roe,
        },
        "qualitative_flags": list(quality.quality_flags),
        "payout_subtype": "restated" if latest.is_restated else "original",
    }


def score_repair_sector(
    sector: Mapping[str, Any],
    *,
    as_of_date: str,
    level: int,
    mode: SnapshotMode,
    config: Any,
    run_id: str,
    store: Any,
    query: Callable,
    allow_estimated_pit: bool = False,
    availability: AvailabilityMetadata | None = None,
) -> list[CandidateSnapshot]:
    """Score one repair sector and (optionally) persist its snapshots."""

    target = date.fromisoformat(as_of_date)
    sector_name = str(sector["sector_name"])
    provider = _dispatch_provider(query)

    from ..stock_alpha.common import load_sector_membership
    membership = load_sector_membership([sector_name], level, target, query=query)
    sector_stocks = set(membership.get(sector_name, []))

    if sector_stocks:
        raw_rows = list(provider.iter_raw_rows(as_of_date=target, stock_codes=sector_stocks))
    else:
        raw_rows = list(provider.iter_raw_rows(as_of_date=target, stock_codes=[]))

    if not raw_rows:
        return []
    by_stock: dict[str, list] = {}
    for raw in raw_rows:
        if sector_stocks and raw.stock_code not in sector_stocks:
            continue
        by_stock.setdefault(raw.stock_code, []).append(raw)
    capital_rows = list(provider.iter_capital_rows(as_of_date=target, stock_codes=sector_stocks))
    capital_by_stock: dict[str, list] = {}
    for capital in capital_rows:
        capital_by_stock.setdefault(capital.stock_code, []).append(capital)
    close_lookup = _raw_close_lookup(query, as_of_date)
    sect_ctx = RepairSectorContext(
        as_of_date=target,
        sector_level=level,
        sector_name=sector_name,
        model_version=str(sector.get("model_version") or config.model_version),
        config_hash=str(sector.get("config_hash") or ""),
        snapshot_mode=mode,
    )
    snapshots: list = []
    for stock_code, rows in by_stock.items():
        raw_close = close_lookup.get(stock_code, 0.0)
        row = _score_one_stock(
            raw_rows_for_stock=rows,
            stock_code=stock_code, raw_close=raw_close,
            sector_name=sector_name, target=target,
            allow_estimated_pit=allow_estimated_pit,
            capital_rows_for_stock=capital_by_stock.get(stock_code, []),
        )
        if row is None:
            continue
        snapshot = build_repair_candidate(
            row=row, sector_context=sect_ctx, config=config, run_id=run_id,
        )
        if availability is not None:
            snapshot = replace(
                snapshot,
                data_available_at=availability.data_available_at,
                run_at=availability.run_at,
                execution_eligible_at=availability.execution_eligible_at,
                availability_basis=availability.availability_basis,
            )
        if store is not None:
            persist_repair_candidates(store, [snapshot])
        snapshots.append(snapshot)
    return snapshots


def build_repair_candidate(
    *,
    row: Mapping[str, Any],
    sector_context: RepairSectorContext,
    config: Any,
    run_id: str,
) -> CandidateSnapshot:
    """Construct the ``CandidateSnapshot`` for one scored repair row."""

    candidate_status = str(row["candidate_status"])
    config_payload = {
        "model_version": config.model_version,
        "sector_level": sector_context.sector_level,
    }
    config_hash = build_config_hash(config_payload)
    risk_flags: list = []
    for flag in row.get("qualitative_flags", []):
        risk_flags.append(str(flag))
    if row.get("payout_subtype") == "restated":
        risk_flags.append("restated")
    feature_json = {
        "valuation_rank": row.get("valuation_rank"),
        "quality_score": row.get("quality_score"),
        "technical_score": row.get("technical_score"),
        "momentum_score": row.get("momentum_score"),
        "risk_penalty": row.get("risk_penalty"),
        "attribution": row.get("attribution", {}),
        "qualitative_flags": row.get("qualitative_flags", []),
        "sector_playbook": "repair_probe",
        "upstream_sector_snapshot": {
            "as_of_date": sector_context.as_of_date.isoformat(),
            "entity_type": "sector",
            "entity_code": sector_context.sector_name,
            "strategy_type": "sector_opportunity",
            "model_version": sector_context.model_version,
            "config_hash": sector_context.config_hash,
            "snapshot_mode": sector_context.snapshot_mode.value,
        },
    }
    reasons: list = []
    if row.get("valuation_rank") is not None and float(row["valuation_rank"]) > 0:
        reasons.append(f"valuation_rank={float(row['valuation_rank']):.3f}")
    if row.get("technical_score", 0) > 0:
        reasons.append("technical_repair")
    if row.get("quality_score") is not None and float(row["quality_score"]) > 0:
        reasons.append("quality_ok")
    return CandidateSnapshot(
        as_of_date=sector_context.as_of_date,
        entity_type="stock",
        entity_code=str(row["stock_code"]),
        sector_level=sector_context.sector_level,
        sector_name=sector_context.sector_name,
        strategy_type="stock_repair",
        candidate_status=candidate_status,
        candidate_score=None if pd.isna(row.get("candidate_score")) else float(row["candidate_score"]),
        model_version=config.model_version,
        config_hash=config_hash,
        run_id=run_id,
        research_status=ResearchStatus.SHADOW,
        validation_status=ValidationStatus.NOT_EVALUATED,
        execution_status=ExecutionStatus.MANUAL_ONLY,
        snapshot_mode=sector_context.snapshot_mode,
        rank_in_sector=None if pd.isna(row.get("rank_in_sector")) else int(row["rank_in_sector"]),
        feature_json=feature_json,
        reasons_json=tuple(reasons),
        risk_flags_json=tuple(risk_flags),
    )


def persist_repair_candidates(
    store: SnapshotStore,
    snapshots: Iterable[CandidateSnapshot],
) -> list[CandidateSnapshot]:
    """Persist Repair Alpha snapshots under the appropriate snapshot mode rules."""

    persisted: list[CandidateSnapshot] = []
    for snapshot in snapshots:
        if snapshot.snapshot_mode is SnapshotMode.LIVE_SHADOW:
            persisted.append(persist_live_shadow_snapshot(store, snapshot))
        elif snapshot.snapshot_mode is SnapshotMode.DELAYED_SHADOW:
            persisted.append(persist_delayed_shadow_snapshot(store, snapshot))
        elif snapshot.snapshot_mode is SnapshotMode.BACKFILL:
            persisted.append(persist_backfill_snapshot(store, snapshot))
        else:
            raise ValueError("Repair Alpha only supports LIVE_SHADOW or BACKFILL (or DELAYED_SHADOW) modes")
    return persisted


__all__ = [
    "REPAIR_PLAYBOOKS",
    "RepairSectorContext",
    "build_repair_candidate",
    "load_repair_sectors",
    "persist_repair_candidates",
    "score_repair_sector",
]
