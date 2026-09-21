"""Orchestration for snapshot-linked forward-label backfill and evaluation."""

from collections.abc import Iterable, Mapping
from datetime import date
from typing import Any

import pandas as pd

from ..availability import AvailabilityBasis, resolve_availability
from ..contracts import CandidateSnapshot, ResearchContext
from ..status import SnapshotMode
from .adapters import MacdSignalAdapter, ShortTermSignalAdapter
from .config import DEFAULT_EVALUATION_CONFIG, EvaluationConfig
from .labels import (
    build_close_to_close_label,
    build_delayed_unavailable_label,
    build_delayed_not_matured_label,
    build_tradable_label,
)
from .metrics import evaluate_condition
from .prices import PriceBarProvider
from .sampling import sample_signal_frame


def backfill_forward_labels(*, snapshots: Iterable[CandidateSnapshot], calendar: Any, provider: PriceBarProvider,
                            context: ResearchContext, horizons: Mapping[str, tuple[int, ...]] | None = None) -> list[Any]:
    labels: list[Any] = []
    horizon_map = horizons or DEFAULT_EVALUATION_CONFIG.horizons
    for snapshot in snapshots:
        strategy = snapshot.strategy_type
        family_horizons = horizon_map.get(strategy, horizon_map.get("short_term", (1,)))
        delayed_calendar_exhausted = False
        try:
            delayed_entry_date = (
                _delayed_daily_bar_entry_date(snapshot, calendar)
                if snapshot.snapshot_mode is SnapshotMode.DELAYED_SHADOW
                else None
            )
        except IndexError:
            delayed_entry_date = None
            delayed_calendar_exhausted = True
        for horizon in family_horizons:
            label_type = "close_to_close" if snapshot.entity_type.startswith("sector") else "tradable"
            if delayed_calendar_exhausted:
                labels.append(build_delayed_not_matured_label(
                    signal_date=snapshot.as_of_date,
                    entity_type=snapshot.entity_type,
                    entity_code=snapshot.entity_code,
                    horizon=horizon,
                    label_type=label_type,
                    source_snapshot_id=snapshot.snapshot_id,
                    snapshot_mode=snapshot.snapshot_mode,
                ))
                continue
            if label_type == "close_to_close" and delayed_entry_date is not None:
                labels.append(build_delayed_unavailable_label(
                    signal_date=snapshot.as_of_date, entity_type=snapshot.entity_type, entity_code=snapshot.entity_code,
                    horizon=horizon, source_snapshot_id=snapshot.snapshot_id, snapshot_mode=snapshot.snapshot_mode,
                ))
                continue
            kwargs = dict(
                calendar=calendar, provider=provider, signal_date=snapshot.as_of_date,
                entity_type=snapshot.entity_type, entity_code=snapshot.entity_code, horizon=horizon,
                source_snapshot_id=None, snapshot_mode=snapshot.snapshot_mode,
            )
            # A DB snapshot ID is not part of the domain dataclass; callers may
            # supply it through feature_json when loading rows from MySQL.
            kwargs["source_snapshot_id"] = snapshot.snapshot_id
            builder = build_close_to_close_label if label_type == "close_to_close" else build_tradable_label
            if label_type == "tradable" and delayed_entry_date is not None:
                kwargs["entry_date_override"] = delayed_entry_date
            labels.append(builder(**kwargs))
    return labels


def _delayed_daily_bar_entry_date(snapshot: CandidateSnapshot, calendar: Any) -> date:
    """Resolve and validate the persisted delayed-shadow timing contract."""
    required = (
        snapshot.data_available_at,
        snapshot.run_at,
        snapshot.execution_eligible_at,
        snapshot.availability_basis,
    )
    if any(value is None for value in required):
        raise ValueError("delayed_shadow snapshot requires complete availability metadata")
    assert snapshot.run_at is not None
    assert snapshot.availability_basis is not None
    resolved = resolve_availability(
        snapshot.as_of_date,
        AvailabilityBasis(snapshot.availability_basis),
        calendar,
        snapshot.run_at,
    )
    if (
        snapshot.data_available_at != resolved.data_available_at
        or snapshot.execution_eligible_at != resolved.execution_eligible_at
    ):
        raise ValueError("delayed_shadow snapshot availability metadata is inconsistent")
    return resolved.daily_bar_entry_date


def run_signal_evaluation(frame: pd.DataFrame, *, signal_family: str, sampling_mode: str = "snapshot",
                          config: EvaluationConfig = DEFAULT_EVALUATION_CONFIG) -> tuple[dict[str, int], list[dict[str, Any]]]:
    sampled = sample_signal_frame(frame, sampling_mode) if sampling_mode == "event" else frame.copy()
    adapter = ShortTermSignalAdapter() if signal_family == "short_term" else None
    spec = adapter.spec if adapter is not None else MacdSignalAdapter.__dict__.get("spec")
    if spec is None:
        from ..contracts import SignalFrameSpec
        spec = SignalFrameSpec(signal_family, None, (), "signal_event_id", False)
    return evaluate_condition(sampled, spec, min_cross_section_pairs=config.min_cross_section_pairs,
                              round_trip_cost_bps=config.round_trip_cost_bps)

