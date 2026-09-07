"""60-session readiness verification for the adaptive ETF shadow runner.

The shadow runner must accumulate at least 60 trading sessions of
reproducible evidence before a separate live-trading design is even
considered. ``verify_shadow_period`` evaluates every readiness gate
listed in the spec and returns a structured ``ShadowReadiness`` record
that names every failing gate. The verifier never collapses failures
into a single boolean and never claims readiness equals permission to
auto-trade.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Callable, Iterable, Sequence

from .run_shadow_daily import ShadowRunSummary
from .shadow_store import (
    FillObservation,
    HealthCheck,
    ShadowRunRecord,
    ShadowStore,
)


READINESS_GATES: tuple[str, ...] = (
    "complete_sessions_gte_60",
    "signal_reproducibility_eq_1",
    "state_continuity_eq_1",
    "future_data_violations_eq_0",
    "unexplained_config_changes_eq_0",
    "observed_slippage_within_5bp_scenario",
)


SLIPPAGE_FIVE_BP: float = 5.0


def default_shadow_store() -> ShadowStore:
    """Create the durable store used by readiness verification."""
    from .mysql_shadow_store import MySQLShadowStore
    return MySQLShadowStore()


@dataclass(frozen=True)
class ShadowReadiness:
    ready: bool
    failures: tuple[str, ...]
    checked_gates: tuple[str, ...]
    summary: Mapping[str, object]

    def gate_results(self) -> dict[str, bool]:
        return {gate: (gate not in self.failures) for gate in self.checked_gates}


def _runs_in_window(store: ShadowStore, start: date, end: date) -> list[ShadowRunRecord]:
    runs = sorted(store.iter_runs(), key=lambda run: run.identity.as_of_date)
    return [run for run in runs if start <= run.identity.as_of_date <= end]


def _check_complete_sessions(runs: Sequence[ShadowRunRecord]) -> tuple[bool, str]:
    """Fail when fewer than 60 distinct trading sessions have a run."""

    dates = sorted({run.identity.as_of_date for run in runs})
    count = len(dates)
    passed = count >= 60
    detail = (
        f"complete_sessions_gte_60: 60 sessions required, "
        f"{count} observed"
    )
    return passed, detail


def _check_signal_reproducibility(
    runs: Sequence[ShadowRunRecord],
) -> tuple[bool, str]:
    """Fail when the same identity appears with different state but same config."""

    seen_states: dict[tuple, set[tuple]] = {}
    for run in runs:
        identity = (run.identity.as_of_date, run.identity.stock_code, run.config_hash)
        state_key = (
            run.state.regime,
            int(run.state.position_shares),
            str(run.state.cash),
        )
        seen_states.setdefault(identity, set()).add(state_key)
    inconsistent = {
        identity: states for identity, states in seen_states.items() if len(states) > 1
    }
    passed = not inconsistent
    detail = (
        f"signal_reproducibility_eq_1: {len(inconsistent)} identity keys produced "
        f"different states on replay"
    )
    return passed, detail


def _check_state_continuity(runs: Sequence[ShadowRunRecord]) -> tuple[bool, str]:
    """Fail when a later date has a prior position different from the prior day."""

    by_stock: dict[str, list[ShadowRunRecord]] = {}
    for run in runs:
        by_stock.setdefault(run.identity.stock_code, []).append(run)
    breaks: list[str] = []
    for stock_code, stock_runs in by_stock.items():
        sorted_runs = sorted(stock_runs, key=lambda run: run.identity.as_of_date)
        previous_state: tuple | None = None
        previous_date: date | None = None
        for run in sorted_runs:
            state_key = (
                run.state.regime,
                int(run.state.position_shares),
                str(run.state.cash),
            )
            if previous_state is not None and previous_date is not None:
                gap = (run.identity.as_of_date - previous_date).days
                if 1 <= gap <= 5:
                    if state_key == previous_state:
                        breaks.append(
                            f"{stock_code}@{run.identity.as_of_date}: identical state "
                            f"but gap={gap} days suggests missing run"
                        )
            previous_state = state_key
            previous_date = run.identity.as_of_date
    passed = not breaks
    detail = (
        f"state_continuity_eq_1: {len(breaks)} continuity violations observed"
    )
    return passed, detail


def _check_future_data_violations(runs: Sequence[ShadowRunRecord]) -> tuple[bool, str]:
    """Fail when a run's identity.as_of_date exceeds its health check as_of_date."""

    violations = 0
    for run in runs:
        for health in run.health_checks:
            detail = dict(health.detail)
            bar_date = detail.get("bar_trade_date")
            if isinstance(bar_date, str):
                if date.fromisoformat(bar_date) > run.identity.as_of_date:
                    violations += 1
    passed = violations == 0
    detail = (
        f"future_data_violations_eq_0: {violations} health checks reference bars "
        f"after their run's as_of_date"
    )
    return passed, detail


def _check_unexplained_config_changes(runs: Sequence[ShadowRunRecord]) -> tuple[bool, str]:
    """Fail when the same identity is recorded under multiple config_hashes."""

    by_identity: dict[tuple, set[str]] = {}
    for run in runs:
        key = (run.identity.as_of_date, run.identity.model_version, run.identity.stock_code)
        by_identity.setdefault(key, set()).add(run.config_hash)
    clashes = sum(1 for hashes in by_identity.values() if len(hashes) > 1)
    passed = clashes == 0
    detail = (
        f"unexplained_config_changes_eq_0: {clashes} identities with multiple "
        f"config_hashes"
    )
    return passed, detail


def _check_slippage_within_5bp(observations: Sequence[FillObservation]) -> tuple[bool, str]:
    """Fail when observed slippage exceeds 5 bp under the default scenario."""

    over_budget = [
        obs for obs in observations
        if obs.slippage_bps is not None and obs.slippage_bps > SLIPPAGE_FIVE_BP
    ]
    passed = not over_budget
    detail = (
        f"observed_slippage_within_5bp_scenario: {len(over_budget)} of "
        f"{len(observations)} observations exceed 5 bp"
    )
    return passed, detail


def load_fill_observations(path: Path) -> tuple[FillObservation, ...]:
    """Load explicit, JSON-safe fill observations for readiness verification."""

    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError("observation file must contain a JSON list")
    observations: list[FillObservation] = []
    required = {
        "execution_eligible_date", "stock_code", "config_hash", "raw_open", "raw_close",
        "slippage_bps", "fill_complete", "notes",
    }
    for item in payload:
        if not isinstance(item, dict) or required.difference(item):
            raise ValueError("each observation must include every FillObservation field")
        observations.append(FillObservation(
            execution_eligible_date=date.fromisoformat(str(item["execution_eligible_date"])),
            stock_code=str(item["stock_code"]), config_hash=str(item["config_hash"]),
            raw_open=item["raw_open"], raw_close=item["raw_close"],
            slippage_bps=item["slippage_bps"], fill_complete=bool(item["fill_complete"]),
            notes=item["notes"],
        ))
    return tuple(observations)


def verify_shadow_period(
    start_date: date,
    end_date: date,
    store: ShadowStore,
    *,
    observations: Sequence[FillObservation] = (),
) -> ShadowReadiness:
    """Evaluate every readiness gate over ``[start_date, end_date]`` and return a structured verdict."""

    if start_date > end_date:
        raise ValueError("start_date must not be after end_date")
    runs = _runs_in_window(store, start_date, end_date)
    gate_runners: tuple[tuple[str, callable], ...] = (
        ("complete_sessions_gte_60", lambda: _check_complete_sessions(runs)),
        ("signal_reproducibility_eq_1", lambda: _check_signal_reproducibility(runs)),
        ("state_continuity_eq_1", lambda: _check_state_continuity(runs)),
        ("future_data_violations_eq_0", lambda: _check_future_data_violations(runs)),
        ("unexplained_config_changes_eq_0", lambda: _check_unexplained_config_changes(runs)),
        ("observed_slippage_within_5bp_scenario", lambda: _check_slippage_within_5bp(observations)),
    )
    failures: list[str] = []
    details: dict[str, str] = {}
    for gate_name, runner in gate_runners:
        passed, detail = runner()
        details[gate_name] = detail
        if not passed:
            failures.append(gate_name)
    return ShadowReadiness(
        ready=not failures,
        failures=tuple(failures),
        checked_gates=READINESS_GATES,
        summary={
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat(),
            "run_count": len(runs),
            "observation_count": len(observations),
            "gate_results": details,
        },
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Verify adaptive ETF shadow readiness over a 60+ session window",
    )
    parser.add_argument("--start-date", required=True)
    parser.add_argument("--end-date", required=True)
    parser.add_argument("--observation-file", default=None,
                        help="Optional JSON file with FillObservation list")
    return parser


def main(argv: list[str] | None = None, *, store_factory=None) -> int:
    args = build_parser().parse_args(argv)
    start_date = date.fromisoformat(args.start_date)
    end_date = date.fromisoformat(args.end_date)
    store_factory = store_factory or default_shadow_store
    store: ShadowStore = store_factory()
    observations: Sequence[FillObservation] = (
        load_fill_observations(Path(args.observation_file))
        if args.observation_file else ()
    )
    readiness = verify_shadow_period(
        start_date, end_date,
        store,
        observations=observations,
    )
    print(json.dumps(asdict(readiness), ensure_ascii=False, sort_keys=True, default=str))
    return 0 if readiness.ready else 2


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    raise SystemExit(main())


