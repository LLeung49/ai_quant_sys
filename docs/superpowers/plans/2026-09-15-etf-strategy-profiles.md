# ETF Strategy Profiles Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add three immutable, versioned ETF research profiles that make future industry ETFs use explicit GRID, integrated GRID-plus-optional-TREND, or deterministic core-hold/rebalance research paths.

**Architecture:** Introduce a `StrategyProfileSpec` registry above the existing `StrategySpec` and `BenchmarkSpec` execution declarations. The profile determines selection families, executable declaration and evidence requirements; `ExperimentSpec`, walk-forward validation and reports consume that declaration so no code path infers a profile from an ETF code. The existing policies and `ExecutionSimulator` remain the sole execution/cost path.

**Tech Stack:** Python 3, frozen dataclasses, pytest, existing adaptive ETF state machine, matplotlib report publisher.

**Spec:** `docs/superpowers/specs/2026-09-15-etf-strategy-profiles-design.md`

## Global Constraints

- Do not authorize a live order, relax OOS, cost, drawdown/CVaR, shadow-run or human-review gates.
- A future industry ETF must name an explicit profile; it receives no inferred profile or automatic trading authority.
- Every profile must publish its id, version, hash, executable declaration and evidence policy in the experiment manifest and report.
- `grid_core` selects only GRID fields; `grid_plus_optional_trend` never optimizes TREND fields from undefined standalone ratios; `core_hold_rebalance` has no parameter surface.
- Missing required configuration, provenance, OOS, costs, profile-required attribution, execution evidence, shadow evidence or human approval produces `do_not_trade`.
- Preserve the existing legacy strategy/baseline declarations for historical report deserialization and regression coverage.

---

## File Structure

- Create: `src/asset_allocation/etf_adaptive/research/strategy_profiles.py` — immutable profile declarations, registry and profile-specific training plans.
- Modify: `src/asset_allocation/etf_adaptive/research/experiment.py` — bind an experiment to one declared profile and serialize its provenance.
- Modify: `src/asset_allocation/etf_adaptive/research/instrument_validation.py` — execute one profile-specific validation path and preserve profile evidence.
- Modify: `src/asset_allocation/etf_adaptive/research/validation_report.py` — fail-close profile provenance and publish optional-TREND diagnostics.
- Modify: `src/asset_allocation/etf_adaptive/research/__init__.py` — expose public profile types and constants.
- Modify: `src/asset_allocation/etf_adaptive/run_instrument_validation.py` — require an explicit profile when running a new named experiment.
- Test: `tests/asset_allocation/etf_adaptive/research/test_strategy_profiles.py` — registry, immutability and selection boundaries.
- Modify: `tests/asset_allocation/etf_adaptive/research/test_experiment.py` — experiment profile binding and serialization checks.
- Modify: `tests/asset_allocation/etf_adaptive/research/test_instrument_validation.py` — GRID-only, optional-TREND and deterministic validation paths.
- Modify: `tests/asset_allocation/etf_adaptive/research/test_validation_report.py` — profile provenance and profile-required evidence publication.
- Modify: `tests/asset_allocation/etf_adaptive/test_run_instrument_validation.py` — CLI explicit-profile boundary.

### Task 1: Immutable Profile Registry and Selection Plans

**Files:**
- Create: `src/asset_allocation/etf_adaptive/research/strategy_profiles.py`
- Modify: `src/asset_allocation/etf_adaptive/research/__init__.py`
- Test: `tests/asset_allocation/etf_adaptive/research/test_strategy_profiles.py`

**Interfaces:**
- Consumes: `StrategySpec`, `BenchmarkSpec`, `FULL_ADAPTIVE_SPEC`, `GRID_ONLY_SPEC`, `BUY_AND_HOLD_SPEC`, `FIXED_HALF_SPEC`, `APPROVED_EXPERIMENT_AXES`.
- Produces: `StrategyProfileSpec`, `GRID_CORE_PROFILE`, `GRID_PLUS_OPTIONAL_TREND_PROFILE`, `CORE_HOLD_REBALANCE_PROFILE`, `profile_for_id(profile_id: str) -> StrategyProfileSpec`, and `profile_training_plan(profile, config, allowed_axes) -> Mapping[str, tuple]`.

- [ ] **Step 1: Write the failing registry and policy-boundary tests**

```python
def test_grid_core_profile_uses_grid_policy_and_never_plans_trend_candidates() -> None:
    profile = profile_for_id("grid_core")
    plan = profile_training_plan(profile, AdaptiveConfig.default(), {"step_pct": (0.02,)})
    assert profile.strategy == GRID_ONLY_SPEC
    assert set(plan) == {"grid_only"}

def test_optional_trend_profile_freezes_trend_configuration() -> None:
    profile = profile_for_id("grid_plus_optional_trend")
    plan = profile_training_plan(profile, AdaptiveConfig.default(), {"step_pct": (0.02,)})
    assert profile.strategy == FULL_ADAPTIVE_SPEC
    assert "trend_only" not in plan

def test_core_hold_profile_has_no_adaptive_strategy_or_parameter_surface() -> None:
    profile = profile_for_id("core_hold_rebalance")
    assert profile.strategy is None
    assert profile_training_plan(profile, AdaptiveConfig.default(), {}) == {}
```

- [ ] **Step 2: Run the new tests and verify the expected RED failure**

Run: `PYTHONPATH=src python -m pytest tests/asset_allocation/etf_adaptive/research/test_strategy_profiles.py -q`

Expected: FAIL during collection because `strategy_profiles` does not exist.

- [ ] **Step 3: Implement the smallest frozen profile registry**

```python
@dataclass(frozen=True)
class StrategyProfileSpec:
    profile_id: str
    version: str
    strategy: StrategySpec | None
    benchmarks: tuple[BenchmarkSpec, ...]
    selection_families: tuple[str, ...]
    required_evidence: frozenset[str]

    def profile_hash(self) -> str:
        return _hash_profile(asdict(self))

GRID_CORE_PROFILE = StrategyProfileSpec(
    "grid_core", "1", GRID_ONLY_SPEC, (BUY_AND_HOLD_SPEC, FIXED_HALF_SPEC),
    ("grid_only",), frozenset({"integrated_oos", "execution", "provenance"}),
)
```

Implement `GRID_PLUS_OPTIONAL_TREND_PROFILE` with `FULL_ADAPTIVE_SPEC`, only `("grid_only",)` selection and required `mode_attribution`; implement `CORE_HOLD_REBALANCE_PROFILE` with `strategy=None`, B&H/fixed-half benchmarks, no selection families. Reject unknown ids, a profile with an empty benchmark list, and selection axes outside its declared family.

- [ ] **Step 4: Run the profile tests and the existing strategy-spec tests**

Run: `PYTHONPATH=src python -m pytest tests/asset_allocation/etf_adaptive/research/test_strategy_profiles.py tests/asset_allocation/etf_adaptive/research/test_strategy_specs.py -q`

Expected: PASS.

- [ ] **Step 5: Commit the registry slice**

```bash
git add src/asset_allocation/etf_adaptive/research/strategy_profiles.py src/asset_allocation/etf_adaptive/research/__init__.py tests/asset_allocation/etf_adaptive/research/test_strategy_profiles.py
git commit -m "feat: add ETF strategy profile registry"
```

### Task 2: Explicit Experiment Profile Provenance

**Files:**
- Modify: `src/asset_allocation/etf_adaptive/research/experiment.py`
- Modify: `tests/asset_allocation/etf_adaptive/research/test_experiment.py`
- Modify: `tests/asset_allocation/etf_adaptive/research/test_validation_report.py`

**Interfaces:**
- Consumes: `StrategyProfileSpec`, `profile_for_id`, `profile_training_plan` from Task 1.
- Produces: `ExperimentSpec.profile: StrategyProfileSpec`, `ExperimentSpec.to_dict()` fields `profile`, `profile_hash`, and `ExperimentSpec.from_dict()` legacy-compatible parsing.

- [ ] **Step 1: Write the failing experiment provenance tests**

```python
def test_experiment_serializes_the_declared_profile_and_hash() -> None:
    spec = ExperimentSpec("industry-grid", ("515450.SH",), GRID_CORE_PROFILE,
                          {"step_pct": (0.02,)}, date(2021, 1, 1), date(2026, 9, 11))
    payload = spec.to_dict()
    assert payload["profile"]["profile_id"] == "grid_core"
    assert payload["profile_hash"] == GRID_CORE_PROFILE.profile_hash()
    assert ExperimentSpec.from_dict(payload) == spec

def test_experiment_rejects_axis_not_owned_by_its_profile() -> None:
    with pytest.raises(ValueError, match="profile does not permit axis"):
        ExperimentSpec("bad", ("515450.SH",), GRID_CORE_PROFILE,
                       {"stop_n": (2.0,)}, date(2021, 1, 1), date(2026, 9, 11))
```

- [ ] **Step 2: Run the focused tests and verify RED**

Run: `PYTHONPATH=src python -m pytest tests/asset_allocation/etf_adaptive/research/test_experiment.py -q`

Expected: FAIL because `ExperimentSpec` does not accept a profile declaration or emit `profile_hash`.

- [ ] **Step 3: Refactor `ExperimentSpec` to own a profile, without breaking historical manifest reads**

Replace the separate writable `strategy` and `benchmarks` constructor inputs with `profile: StrategyProfileSpec`; provide read-only `strategy` and `benchmarks` properties delegated from the profile for call sites that need them. In `from_dict`, accept existing manifests containing `strategy`/`benchmarks` only by constructing a non-actionable `legacy_unprofiled` declaration; it must deserialize for historical reports but fail publication for a new formal run. Make `targeted_study()` explicitly select `GRID_PLUS_OPTIONAL_TREND_PROFILE`, and make `study_training_plan()` call `profile_training_plan()`.

- [ ] **Step 4: Run experiment/report provenance tests and verify GREEN**

Run: `PYTHONPATH=src python -m pytest tests/asset_allocation/etf_adaptive/research/test_experiment.py tests/asset_allocation/etf_adaptive/research/test_validation_report.py -q`

Expected: PASS, including legacy-manifest deserialization tests updated to assert non-actionable status.

- [ ] **Step 5: Commit the experiment boundary**

```bash
git add src/asset_allocation/etf_adaptive/research/experiment.py tests/asset_allocation/etf_adaptive/research/test_experiment.py tests/asset_allocation/etf_adaptive/research/test_validation_report.py
git commit -m "feat: bind ETF experiments to strategy profiles"
```

### Task 3: Profile-Specific Walk-Forward Execution

**Files:**
- Modify: `src/asset_allocation/etf_adaptive/research/instrument_validation.py`
- Modify: `tests/asset_allocation/etf_adaptive/research/test_instrument_validation.py`

**Interfaces:**
- Consumes: `ExperimentSpec.profile`, `StrategyProfileSpec.strategy`, `StrategyProfileSpec.benchmarks`, `profile_training_plan()`.
- Produces: `run_instrument_validation(target: ValidationTarget, provider: _Provider, start_date: date, as_of_date: date, initial_cash: Decimal, *, profile: StrategyProfileSpec, training_plan: Mapping | None = None) -> InstrumentValidationResult`, `ValidationWindowResult.profile_id`, and profile-specific selected-score mappings.

- [ ] **Step 1: Write failing validation tests for the three execution paths**

```python
def test_grid_core_accepts_a_stable_grid_selection_when_trend_metrics_are_undefined(monkeypatch) -> None:
    grid_plan = {"grid_only": (grid_candidates(), ("step_pct",), ())}
    result = run_instrument_validation(target, provider, start, cutoff, cash,
                                       profile=GRID_CORE_PROFILE, training_plan=grid_plan)
    assert result.rejection_reason != "no_stable_training_parameters"
    assert all(set(window.selected_scores or {}) <= {"grid_only"} for window in result.windows)

def test_optional_trend_does_not_reject_complete_integrated_evidence_for_undefined_standalone_trend_ratio(monkeypatch) -> None:
    grid_plan = {"grid_only": (grid_candidates(), ("step_pct",), ())}
    result = run_instrument_validation(target, provider, start, cutoff, cash,
                                       profile=GRID_PLUS_OPTIONAL_TREND_PROFILE, training_plan=grid_plan)
    assert result.rejection_reason != "no_stable_training_parameters"
    assert all(window.excess_attribution is not None for window in result.windows)

def test_core_hold_rebalance_uses_only_declared_benchmarks_and_never_adaptive_orders() -> None:
    result = run_instrument_validation(target, provider, start, cutoff, cash,
                                       profile=CORE_HOLD_REBALANCE_PROFILE)
    assert all(window.selected_config is None for window in result.windows)
    assert all(event.kind != "strategy_signal" for window in result.windows for event in window.strategy_events)
```

- [ ] **Step 2: Run those tests and verify RED**

Run: `PYTHONPATH=src python -m pytest tests/asset_allocation/etf_adaptive/research/test_instrument_validation.py -q`

Expected: FAIL because validation unconditionally selects both GRID and TREND candidates and executes `FULL_ADAPTIVE`.

- [ ] **Step 3: Make validation dispatch only through the profile declaration**

Add a required keyword-only `profile` argument to new formal runs. For `grid_core`, call `_select_training_candidate()` only for `grid_only`, build the frozen config from the selected GRID section and the profile's immutable default TREND section, then call `run_strategy_spec(GRID_ONLY_SPEC, request, provider)` plus `run_benchmark_spec(benchmark, config, request, provider)` for each declared benchmark. For `grid_plus_optional_trend`, select only GRID, use the immutable `FULL_ADAPTIVE_SPEC.config.trend`, run the full adaptive policy, and record observations/attribution. For `core_hold_rebalance`, skip candidate selection and call `run_benchmark_spec()` only for B&H and fixed-half; designate B&H as the comparison reference and retain both ledgers. Never substitute a fallback profile or a default configuration when profile selection fails.

Store profile id on every `ValidationWindowResult`; populate `selected_scores` only for the selected families. Change the no-stable blocker to `no_stable_grid_training_parameters` for the two adaptive profiles. Preserve the existing fixed-universe legacy default only behind an explicit `legacy_unprofiled` test helper, never from the CLI.

- [ ] **Step 4: Run focused validation and policy regression tests**

Run: `PYTHONPATH=src python -m pytest tests/asset_allocation/etf_adaptive/research/test_instrument_validation.py tests/asset_allocation/etf_adaptive/test_strategy_policy.py tests/asset_allocation/etf_adaptive/research/test_strategy_specs.py -q`

Expected: PASS; GRID-only results contain no TREND selection, optional-TREND results no longer use undefined standalone metrics as a hard gate, and core-hold results contain no adaptive order reasons.

- [ ] **Step 5: Commit the validation dispatcher**

```bash
git add src/asset_allocation/etf_adaptive/research/instrument_validation.py tests/asset_allocation/etf_adaptive/research/test_instrument_validation.py
git commit -m "feat: validate ETF research by strategy profile"
```

### Task 4: Fail-Closed Profile Reporting and Optional-TREND Diagnostics

**Files:**
- Modify: `src/asset_allocation/etf_adaptive/research/validation_report.py`
- Modify: `tests/asset_allocation/etf_adaptive/research/test_validation_report.py`

**Interfaces:**
- Consumes: profile metadata in `run_manifest`, profile id in `ValidationWindowResult`, `ExcessAttribution`, daily observations and performance metrics.
- Produces: `summary["strategy_profile"]`, `summary["trend_diagnostics"]` for optional-TREND, and profile-aware `_evidence_blockers()`.

- [ ] **Step 1: Write failing report-evidence tests**

```python
def _optional_trend_manifest(result: InstrumentValidationResult) -> Mapping[str, object]:
    spec = ExperimentSpec(
        "optional-trend-report", (result.target.stock_code,),
        GRID_PLUS_OPTIONAL_TREND_PROFILE, {"step_pct": (0.02,)},
        date(2025, 1, 2), result.as_of_date,
    )
    return bind_experiment(result, spec).run_manifest

def test_optional_trend_report_publishes_required_integrated_diagnostics(tmp_path) -> None:
    result = replace(_recorded_result(), run_manifest=_optional_trend_manifest(_recorded_result()))
    summary = json.loads(write_validation_artifacts(result, tmp_path / "report").summary_json.read_text())
    assert summary["strategy_profile"]["profile_id"] == "grid_plus_optional_trend"
    assert summary["trend_diagnostics"]["active_sessions"] >= 0
    assert "incremental_execution_cost" in summary["trend_diagnostics"]

def test_optional_trend_report_is_do_not_trade_when_attribution_is_missing(tmp_path) -> None:
    result = replace(_recorded_result(), run_manifest=_optional_trend_manifest(_recorded_result()))
    result = replace(result, windows=(replace(result.windows[0], excess_attribution=None), *result.windows[1:]))
    summary = json.loads(write_validation_artifacts(result, tmp_path / "report").summary_json.read_text())
    assert summary["decision"]["conclusion"] == "do_not_trade"
    assert "profile_mode_attribution" in summary["decision"]["blockers"]
```

- [ ] **Step 2: Run the report tests and verify RED**

Run: `PYTHONPATH=src python -m pytest tests/asset_allocation/etf_adaptive/research/test_validation_report.py -q`

Expected: FAIL because summaries do not contain profile provenance or required optional-TREND diagnostics.

- [ ] **Step 3: Implement profile-aware evidence verification and diagnostics**

Add a `strategy_profile` payload containing id, version, hash, executable strategy id (or null for deterministic core) and benchmark hashes. In `_evidence_blockers`, reject missing/forged profile payload and reject `grid_plus_optional_trend` if any OOS window lacks observations or reconciled excess attribution using blocker `profile_mode_attribution`. Compute `trend_diagnostics` only from recorded daily observations/events and reconciled attribution: active-session count, `trend_return`, `transition_return`, `execution_cost`, and the recorded strategy-vs-reference drawdown/CVaR deltas. Never manufacture a value from a missing series. For `grid_core` and `core_hold_rebalance`, emit `trend_diagnostics: null`; candidate score CSV stays empty for `core_hold_rebalance`.

- [ ] **Step 4: Run report, attribution and decision tests**

Run: `PYTHONPATH=src python -m pytest tests/asset_allocation/etf_adaptive/research/test_validation_report.py tests/asset_allocation/etf_adaptive/research/test_attribution.py tests/asset_allocation/etf_adaptive/research/test_decision.py -q`

Expected: PASS; a low active-session count remains visible but is not a blocker, whereas missing required evidence is `do_not_trade`.

- [ ] **Step 5: Commit the reporting slice**

```bash
git add src/asset_allocation/etf_adaptive/research/validation_report.py tests/asset_allocation/etf_adaptive/research/test_validation_report.py
git commit -m "feat: report ETF profile evidence and trend diagnostics"
```

### Task 5: Explicit CLI Boundary and End-to-End Verification

**Files:**
- Modify: `src/asset_allocation/etf_adaptive/run_instrument_validation.py`
- Modify: `tests/asset_allocation/etf_adaptive/test_run_instrument_validation.py`
- Modify: `docs/superpowers/specs/2026-09-15-etf-strategy-profiles-design.md`

**Interfaces:**
- Consumes: `profile_for_id()` and profile-aware experiment/validation API from Tasks 1-4.
- Produces: `--profile {grid_core,grid_plus_optional_trend,core_hold_rebalance}` for explicitly named new experiments; no CLI route which silently selects a profile.

- [ ] **Step 1: Write failing CLI tests**

```python
def test_cli_rejects_new_experiment_without_profile(monkeypatch, tmp_path) -> None:
    with pytest.raises(SystemExit):
        main(["--experiment", "industry-demo", "--output", str(tmp_path)])

def test_cli_persists_explicit_profile_in_the_result_manifest(monkeypatch, tmp_path) -> None:
    main(["--experiment", "industry-demo", "--profile", "grid_core", "--output", str(tmp_path)])
    assert json.loads((tmp_path / "instrument_validation.json").read_text())["results"][0]["profile_id"] == "grid_core"
```

- [ ] **Step 2: Run CLI tests and verify RED**

Run: `PYTHONPATH=src python -m pytest tests/asset_allocation/etf_adaptive/test_run_instrument_validation.py -q`

Expected: FAIL because the CLI has no profile argument or profile provenance field.

- [ ] **Step 3: Add the explicit CLI argument and update the design rollout record**

Require `--profile` for a newly named `--experiment`; keep the existing fixed-universe run as research-only legacy output until each target is explicitly migrated. Resolve only through `profile_for_id()` before provider construction. Include `profile_id`, `profile_version`, `profile_hash` and final `decision` in the aggregate JSON/Markdown rows. Amend the design spec rollout checklist to record the implemented explicit CLI boundary; do not create reports or invoke a broker.

- [ ] **Step 4: Run the complete verification set**

Run: `PYTHONPATH=src python -m pytest tests/asset_allocation/etf_adaptive -q`

Expected: PASS. Then run `git diff --check` and verify no `reports/`, `.pytest-*`, or `.codex/diag/` artifact is staged.

- [ ] **Step 5: Commit and request independent review**

```bash
git add src/asset_allocation/etf_adaptive/run_instrument_validation.py tests/asset_allocation/etf_adaptive/test_run_instrument_validation.py docs/superpowers/specs/2026-09-15-etf-strategy-profiles-design.md
git commit -m "feat: require explicit ETF research profiles"
```

Request review specifically for profile isolation, OOS isolation, cost reuse, evidence blockers, legacy manifest parsing and absence of any live-order path.

## Self-Review

- Spec coverage: Task 1 supplies the immutable three-profile registry; Task 2 binds and hashes it in experiments; Task 3 dispatches selection/execution without a separate TREND eligibility gate; Task 4 supplies provenance, attribution and fail-closed reporting; Task 5 prevents implicit future industry-ETF assignment and runs full verification.
- Placeholder scan: no deferred implementation markers or unspecified test steps remain; every task supplies files, interfaces, RED command, GREEN command and commit boundary.
- Type consistency: `StrategyProfileSpec` is produced in Task 1, consumed by `ExperimentSpec` in Task 2 and validation in Task 3; its `profile_hash()` is serialized in Task 2 and validated in Task 4; CLI resolution in Task 5 uses `profile_for_id()` from Task 1.
