# ETF Adaptive Strategy Lab Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make GRID/TREND variants, fair benchmarks, candidate selection and
diagnostics reproducible enough to run targeted OOS parameter studies without
weakening existing research or daily-advice gates.

**Architecture:** Keep the existing engine responsible for market-data replay,
T+1 execution, corporate actions and state persistence. Move only close-time
decision logic behind immutable strategy specifications and policies. Train-only
candidate scoring, recorded state attribution and reporting consume those
specifications and the already recorded results; they never produce broker orders.

**Tech Stack:** Python 3.13, standard-library dataclasses/Protocol/Enum/CSV/JSON,
pytest, existing adaptive ETF engine and MySQL-backed read-only provider.

**Spec:** `docs/superpowers/specs/2026-09-12-etf-adaptive-strategy-lab-design.md`

## Global Constraints

- Preserve existing raw/qfq affine validation, T+1 execution, corporate actions,
  `CostConfig`, data audit and no-look-ahead guarantees.
- Training selection may consume only training dates of its own walk-forward
  window; OOS data must not affect scores, stability or tie breaking.
- A stable parameter neighborhood and execution constraints are hard gates;
  Pareto ranking cannot rescue a failing candidate.
- Formal reports and advice consume persisted runs only, and all approval,
  universe-hash and layer gates remain fail-closed.
- No automated brokerage order submission, ETF-universe expansion, portfolio
  optimization, sector momentum or short-term strategy work.

---

## File structure

| File | Responsibility |
| --- | --- |
| `src/asset_allocation/etf_adaptive/strategy_policy.py` | Policy protocol and the full/grid/trend policy implementations. |
| `src/asset_allocation/etf_adaptive/engine.py` | Delegates close and fill transitions to an injected policy while retaining execution/session ownership. |
| `src/asset_allocation/etf_adaptive/research/strategy_specs.py` | Immutable `StrategySpec` and `BenchmarkSpec`, canonical hashes and factories. |
| `src/asset_allocation/etf_adaptive/research/baselines.py` | Runs specs through the shared engine/execution path; removes hand-written formal benchmark fills. |
| `src/asset_allocation/etf_adaptive/research/candidate_scoring.py` | Primitive train-only candidate score, stable-plateau ranking and deterministic representative selection. |
| `src/asset_allocation/etf_adaptive/research/instrument_validation.py` | Records selected specs, candidate score surfaces and state observations in each OOS window. |
| `src/asset_allocation/etf_adaptive/research/attribution.py` | Reconciles recorded daily state/NAV/events into mode, stop/cooldown, cash and cost attribution. |
| `src/asset_allocation/etf_adaptive/research/validation_report.py` | Writes candidate-score and attribution artifacts and names the primary diagnostic driver. |
| `src/asset_allocation/etf_adaptive/research/experiment.py` | Immutable bounded `ExperimentSpec` plus target-study manifest validation. |
| `src/asset_allocation/etf_adaptive/run_instrument_validation.py` | Accepts an experiment manifest and writes it into the report run manifest. |

### Task 1: Introduce explicit, capability-safe strategy policies

**Files:**
- Create: `src/asset_allocation/etf_adaptive/strategy_policy.py`
- Modify: `src/asset_allocation/etf_adaptive/engine.py:process_close, AdaptiveBacktestEngine.__init__, run_with_data`
- Test: `tests/asset_allocation/etf_adaptive/test_strategy_policy.py`
- Test: `tests/asset_allocation/etf_adaptive/test_engine.py`

**Consumes:** existing `StrategyState`, `Decision`, `Fill`, `IndicatorSnapshot`,
`ETFEligibility` and `AdaptiveConfig`.

**Produces:**
```python
class StrategyPolicy(Protocol):
    policy_id: str
    def process_close(self, state: StrategyState, snapshot: IndicatorSnapshot,
                      eligibility: ETFEligibility, config: AdaptiveConfig) -> Decision: ...
    def apply_fill(self, state: StrategyState, fill: Fill,
                   config: AdaptiveConfig) -> StrategyState: ...

FULL_ADAPTIVE_POLICY: StrategyPolicy
GRID_ONLY_POLICY: StrategyPolicy
TREND_ONLY_POLICY: StrategyPolicy
```

- [ ] **Step 1: Write failing capability-isolation tests**

```python
def test_grid_only_policy_never_emits_trend_order_when_adx_requests_trend():
    decision = GRID_ONLY_POLICY.process_close(grid_state, high_adx_snapshot, eligible, config)
    assert all(not intent.reason.value.startswith("trend_") for intent in decision.orders)

def test_trend_only_policy_never_emits_grid_order_when_adx_requests_grid():
    decision = TREND_ONLY_POLICY.process_close(trend_state, low_adx_snapshot, eligible, config)
    assert all(not intent.reason.value.startswith("grid_") for intent in decision.orders)
```

- [ ] **Step 2: Run the new tests to verify failure**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/test_strategy_policy.py -q`

Expected: FAIL because `strategy_policy` and capability-restricted policies do
not exist.

- [ ] **Step 3: Implement policy composition without changing session semantics**

Move the current `process_close`, GRID fill and TREND fill routing into
`FullAdaptivePolicy`. Implement `GridOnlyPolicy` with only grid initialization,
grid orders, hard/grid stops and grid fill state; it must preserve `Regime.GRID`
when ADX requests TREND. Implement `TrendOnlyPolicy` with only trend entry/add/
stop and trend fill state; it must preserve `Regime.TREND` when ADX requests
GRID. Give `AdaptiveBacktestEngine` an optional `policy: StrategyPolicy` which
defaults to `FULL_ADAPTIVE_POLICY`; replace direct calls to module-level close/
fill functions with the policy methods.

- [ ] **Step 4: Run focused engine and policy tests**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/test_strategy_policy.py tests/asset_allocation/etf_adaptive/test_engine.py tests/asset_allocation/etf_adaptive/test_grid.py tests/asset_allocation/etf_adaptive/test_trend.py -q`

Expected: PASS; existing full-policy trade behavior remains unchanged and mode
restricted policies cannot cross into the disabled mode.

- [ ] **Step 5: Commit**

```bash
git add src/asset_allocation/etf_adaptive/strategy_policy.py src/asset_allocation/etf_adaptive/engine.py tests/asset_allocation/etf_adaptive/test_strategy_policy.py tests/asset_allocation/etf_adaptive/test_engine.py
git commit -m "feat: add capability-safe ETF strategy policies"
```

### Task 2: Replace enum-only baselines with fair strategy and benchmark specifications

**Files:**
- Create: `src/asset_allocation/etf_adaptive/research/strategy_specs.py`
- Modify: `src/asset_allocation/etf_adaptive/research/baselines.py`
- Modify: `src/asset_allocation/etf_adaptive/research/__init__.py`
- Test: `tests/asset_allocation/etf_adaptive/research/test_strategy_specs.py`
- Test: `tests/asset_allocation/etf_adaptive/research/test_baselines.py`

**Consumes:** Task 1 policies, `AdaptiveConfig`, `BacktestRequest`,
`AdaptiveBacktestDataProvider`, `ExecutionSimulator`.

**Produces:**
```python
@dataclass(frozen=True)
class StrategySpec:
    strategy_id: str
    version: str
    config: AdaptiveConfig
    policy_id: str
    def spec_hash(self) -> str: ...

@dataclass(frozen=True)
class BenchmarkSpec:
    benchmark_id: str
    version: str
    rebalance_sessions: int | None
    def spec_hash(self) -> str: ...

def run_strategy_spec(spec: StrategySpec, request: BacktestRequest, provider: object) -> BacktestResult: ...
def run_benchmark_spec(spec: BenchmarkSpec, config: AdaptiveConfig, request: BacktestRequest, provider: object) -> BacktestResult: ...
```

- [ ] **Step 1: Write failing fairness and identity tests**

```python
def test_grid_only_spec_uses_grid_policy_not_default_trend_config():
    result = run_strategy_spec(GRID_ONLY_SPEC, request, provider)
    assert {event_reason(event) for event in result.events}.isdisjoint(TREND_REASONS)

def test_fixed_half_benchmark_records_shared_cost_model():
    result = run_benchmark_spec(FIXED_HALF_SPEC, config_with_costs, request, provider)
    assert sum(fill_commission(event) for event in result.events) > 0
```

- [ ] **Step 2: Run the new tests to verify failure**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research/test_strategy_specs.py -q`

Expected: FAIL because specs and fair fixed-half execution are absent.

- [ ] **Step 3: Implement specs and migrate baseline dispatch**

Give each existing `BaselineKind` a compatibility mapping to a `StrategySpec`
or `BenchmarkSpec`. Implement buy-and-hold and fixed-half as benchmark policies
that build `OrderIntent` objects and execute them via `ExecutionSimulator`,
including eligibility, corporate actions, commission and slippage. Preserve
`run_baseline`/`run_baselines` public signatures while delegating to spec-based
runners. Record `strategy_spec_hash` and `benchmark_spec_hash` in `BaselineRun`
and report notes.

- [ ] **Step 4: Run baseline regression suite**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research/test_strategy_specs.py tests/asset_allocation/etf_adaptive/research/test_baselines.py tests/asset_allocation/etf_adaptive/research/test_execution_evidence.py -q`

Expected: PASS; B&H and fixed-half both use recorded execution costs and only
the intended policy can emit its orders.

- [ ] **Step 5: Commit**

```bash
git add src/asset_allocation/etf_adaptive/research/strategy_specs.py src/asset_allocation/etf_adaptive/research/baselines.py src/asset_allocation/etf_adaptive/research/__init__.py tests/asset_allocation/etf_adaptive/research/test_strategy_specs.py tests/asset_allocation/etf_adaptive/research/test_baselines.py
git commit -m "feat: define fair ETF strategy and benchmark specs"
```

### Task 3: Add train-only risk-adjusted candidate scoring

**Files:**
- Create: `src/asset_allocation/etf_adaptive/research/candidate_scoring.py`
- Modify: `src/asset_allocation/etf_adaptive/research/instrument_validation.py:_screen_training_candidates,_select_training_candidate,ValidationWindowResult`
- Modify: `src/asset_allocation/etf_adaptive/research/parameters.py`
- Test: `tests/asset_allocation/etf_adaptive/research/test_candidate_scoring.py`
- Test: `tests/asset_allocation/etf_adaptive/research/test_instrument_validation.py`

**Consumes:** Task 2 `StrategySpec`/`BenchmarkSpec`, `PerformanceMetrics`,
`ParameterCandidate`, existing stable-neighborhood rules and training segments.

**Produces:**
```python
@dataclass(frozen=True)
class TrainingCandidateScore:
    config_hash: str
    config: Mapping[str, object]
    positive_subperiod_share: float
    sortino_excess: float
    sharpe_excess: float
    drawdown_improvement: float
    cvar5_improvement: float
    cost_drag: float
    exposure_ratio: float
    stable: bool
    rejection_reason: str | None

def select_stable_representative(scores: Sequence[TrainingCandidateScore]) -> TrainingCandidateScore | None: ...
```

- [ ] **Step 1: Write failing selection tests**

```python
def test_select_stable_representative_rejects_high_score_outside_plateau():
    assert select_stable_representative((unstable_high_score, stable_lower_score)) == stable_lower_score

def test_oos_mutation_cannot_change_recorded_training_scores(monkeypatch):
    before = validate(oos_multiplier=1.0).windows[0].candidate_scores
    after = validate(oos_multiplier=10.0).windows[0].candidate_scores
    assert before == after
```

- [ ] **Step 2: Run the new tests to verify failure**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research/test_candidate_scoring.py -q`

Expected: FAIL because candidate score surfaces are not persisted and plateau
ranking does not exist.

- [ ] **Step 3: Implement hard-gated plateau ranking**

Compute every score solely from recorded training subperiod strategy and B&H
runs. First obtain stable candidates with the existing exact-neighbor rule;
mark every other score with `rejection_reason="outside_stable_plateau"`. Order
stable scores by positive subperiod share descending, Sortino excess descending,
Sharpe excess descending, cost drag ascending, then canonical conservative
configuration order. Persist all scores, selected score and screened axes in
each `ValidationWindowResult`; retain old `TrainingSurfaceSummary` for
backward-compatible report consumers.

- [ ] **Step 4: Run scoring and isolation regressions**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research/test_candidate_scoring.py tests/asset_allocation/etf_adaptive/research/test_instrument_validation.py tests/asset_allocation/etf_adaptive/research/test_decision.py -q`

Expected: PASS; a plateau member is selected deterministically and OOS changes
cannot affect its training scores or selection.

- [ ] **Step 5: Commit**

```bash
git add src/asset_allocation/etf_adaptive/research/candidate_scoring.py src/asset_allocation/etf_adaptive/research/instrument_validation.py src/asset_allocation/etf_adaptive/research/parameters.py tests/asset_allocation/etf_adaptive/research/test_candidate_scoring.py tests/asset_allocation/etf_adaptive/research/test_instrument_validation.py
git commit -m "feat: rank stable ETF parameter candidates by training evidence"
```

### Task 4: Record state observations and reconcile causal attribution

**Files:**
- Modify: `src/asset_allocation/etf_adaptive/state.py`
- Modify: `src/asset_allocation/etf_adaptive/engine.py`
- Modify: `src/asset_allocation/etf_adaptive/research/attribution.py`
- Modify: `src/asset_allocation/etf_adaptive/research/instrument_validation.py`
- Test: `tests/asset_allocation/etf_adaptive/research/test_attribution.py`
- Test: `tests/asset_allocation/etf_adaptive/test_engine.py`

**Consumes:** Task 1 policy state transitions, persisted `BacktestEvent`,
`DailyNav`, B&H NAV and execution cost fields.

**Produces:**
```python
@dataclass(frozen=True)
class DailyStrategyObservation:
    nav_date: date
    regime: Regime | None
    target_exposure: float
    actual_exposure: float
    cooldown_remaining: int
    pending_order_count: int
    state_reason: str

@dataclass(frozen=True)
class ExcessAttribution:
    grid_return: float
    trend_return: float
    transition_return: float
    cash_opportunity_cost: float
    execution_cost: float
    reconciliation_error: float
```

- [ ] **Step 1: Write failing event-sourced reconciliation tests**

```python
def test_attribution_reconciles_recorded_strategy_minus_benchmark_nav():
    attribution = build_excess_attribution(recorded_strategy, recorded_benchmark, observations)
    assert attribution.reconciliation_error == pytest.approx(0.0, abs=1e-9)

def test_attribution_rejects_observation_date_not_in_recorded_nav():
    with pytest.raises(ValueError, match="observation date"):
        build_excess_attribution(strategy, benchmark, (foreign_date_observation,))
```

- [ ] **Step 2: Run the new tests to verify failure**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research/test_attribution.py -q`

Expected: FAIL because daily state observations and excess attribution do not
exist.

- [ ] **Step 3: Implement recorded observations and attribution**

Append one `DailyStrategyObservation` after each completed engine session using
only the state, executed fills and that session's NAV. In attribution, compare
the strategy and B&H daily returns: assign invested-day excess by observed
regime, cash-day benchmark return to `cash_opportunity_cost`, and execution
commission/slippage to `execution_cost`. Assign the first post-regime-switch
session to `transition_return`. Raise if dates are misaligned or the absolute
reconciliation error exceeds `1e-9` after summation.

- [ ] **Step 4: Run attribution and engine tests**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research/test_attribution.py tests/asset_allocation/etf_adaptive/test_engine.py tests/asset_allocation/etf_adaptive/research/test_execution_evidence.py -q`

Expected: PASS; all attribution comes from recorded series and reconciles to
the recorded excess NAV.

- [ ] **Step 5: Commit**

```bash
git add src/asset_allocation/etf_adaptive/state.py src/asset_allocation/etf_adaptive/engine.py src/asset_allocation/etf_adaptive/research/attribution.py src/asset_allocation/etf_adaptive/research/instrument_validation.py tests/asset_allocation/etf_adaptive/research/test_attribution.py tests/asset_allocation/etf_adaptive/test_engine.py
git commit -m "feat: attribute ETF excess returns from recorded state"
```

### Task 5: Persist bounded experiment manifests and diagnostic report artifacts

**Files:**
- Create: `src/asset_allocation/etf_adaptive/research/experiment.py`
- Modify: `src/asset_allocation/etf_adaptive/research/validation_report.py`
- Modify: `src/asset_allocation/etf_adaptive/run_instrument_validation.py`
- Test: `tests/asset_allocation/etf_adaptive/research/test_experiment.py`
- Test: `tests/asset_allocation/etf_adaptive/research/test_validation_report.py`
- Test: `tests/asset_allocation/etf_adaptive/test_run_instrument_validation.py`

**Consumes:** Task 2 specs, Task 3 score surfaces, Task 4 attribution and the
existing report run manifest/data fingerprint contracts.

**Produces:**
```python
@dataclass(frozen=True)
class ExperimentSpec:
    experiment_id: str
    target_codes: tuple[str, ...]
    strategy: StrategySpec
    benchmarks: tuple[BenchmarkSpec, ...]
    allowed_axes: Mapping[str, tuple[object, ...]]
    start_date: date
    as_of_date: date
    def experiment_hash(self) -> str: ...
```

- [ ] **Step 1: Write failing manifest/report tests**

```python
def test_experiment_rejects_unapproved_target_or_axis():
    with pytest.raises(ValueError, match="allowed axis"):
        ExperimentSpec("bad", ("513330.SH",), spec, (buy_hold,), {"unknown": (1,)}, start, cutoff)

def test_report_exports_candidate_scores_and_reconciled_attribution(tmp_path):
    manifest = write_validation_artifacts(recorded_result, tmp_path / "report")
    assert manifest.candidate_scores_csv.exists()
    assert manifest.excess_attribution_json.exists()
```

- [ ] **Step 2: Run the new tests to verify failure**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research/test_experiment.py tests/asset_allocation/etf_adaptive/research/test_validation_report.py -q`

Expected: FAIL because bounded experiment validation and diagnostic artifacts
are absent.

- [ ] **Step 3: Implement manifest propagation and atomic artifacts**

Validate target codes against `FIXED_VALIDATION_TARGETS` and axes against the
parameter module's approved axis values. Add experiment hash, strategy spec,
benchmark specs, selected score, all candidate scores and attribution to the
run manifest. Atomically publish `candidate_scores.csv`,
`excess_attribution.json` and `daily_state.csv` beside existing validation
artifacts. Make the Markdown report identify the largest absolute contributor
to excess return and the matching next research action. Missing experiment
metadata causes a formal experimental report to be `do_not_trade`.

- [ ] **Step 4: Run report and CLI regressions**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research/test_experiment.py tests/asset_allocation/etf_adaptive/research/test_validation_report.py tests/asset_allocation/etf_adaptive/test_run_instrument_validation.py tests/asset_allocation/etf_adaptive/test_run_shadow_daily.py -q`

Expected: PASS; manifests and diagnostics are complete, atomically published,
and cannot activate advice on missing evidence.

- [ ] **Step 5: Commit**

```bash
git add src/asset_allocation/etf_adaptive/research/experiment.py src/asset_allocation/etf_adaptive/research/validation_report.py src/asset_allocation/etf_adaptive/run_instrument_validation.py tests/asset_allocation/etf_adaptive/research/test_experiment.py tests/asset_allocation/etf_adaptive/research/test_validation_report.py tests/asset_allocation/etf_adaptive/test_run_instrument_validation.py
git commit -m "feat: publish bounded ETF experiment diagnostics"
```

### Task 6: Define and execute the three prioritized research studies

**Files:**
- Create: `docs/user_demand/asset-allocation-strategy/etf-adaptive-targeted-study-v1.md`
- Create: `reports/etf_adaptive_targeted_studies/<experiment-id>/` (generated, uncommitted research evidence)
- Test: `tests/asset_allocation/etf_adaptive/research/test_experiment.py`

**Consumes:** Tasks 1–5 and the evidence-gated 2026-09-11 validation reports.

**Produces:** three immutable `ExperimentSpec` inputs and reports for
`513330.SH`, `159915.SZ` and `588000.SH`.

- [ ] **Step 1: Write failing study-boundary tests**

```python
def test_targeted_study_manifest_cannot_include_nonprioritized_code():
    study = targeted_study("hk_internet")
    assert study.target_codes == ("513330.SH",)
    with pytest.raises(ValueError, match="target code"):
        targeted_study("hk_internet", target_codes=("513100.SH",))
```

- [ ] **Step 2: Run the new tests to verify failure**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research/test_experiment.py::test_targeted_study_manifest_cannot_include_nonprioritized_code -q`

Expected: FAIL because named targeted studies are not defined.

- [ ] **Step 3: Add the study document and exact bounded axes**

Document one study per target:

```text
hk_internet: 513330.SH; grid step/unit, atr stop, cooldown, trend stop, MACD filter
chinext_reentry: 159915.SZ; cooldown, atr stop, trend stop, MACD/amount filters
star50_extreme_window: 588000.SH; diagnostic-only first, then atr stop, cooldown, trend stop
```

Use only values already declared in `parameters.py`. The STAR 50 study runner
must refuse parameter execution until its diagnostic artifact identifies a
largest contributor for the extreme lagging window. Do not include Nasdaq,
S&P 500 or A500 in these three experiment manifests.

- [ ] **Step 4: Run studies and validate artifacts**

Run: `$env:PYTHONPATH='src'; python -m asset_allocation.etf_adaptive.run_instrument_validation --experiment hk_internet --start-date 2021-01-01 --as-of-date 2026-09-11 --output-dir reports/etf_adaptive_targeted_studies/hk_internet`

Run: `$env:PYTHONPATH='src'; python -m asset_allocation.etf_adaptive.run_instrument_validation --experiment chinext_reentry --start-date 2021-01-01 --as-of-date 2026-09-11 --output-dir reports/etf_adaptive_targeted_studies/chinext_reentry`

Run: `$env:PYTHONPATH='src'; python -m asset_allocation.etf_adaptive.run_instrument_validation --experiment star50_extreme_window --start-date 2021-01-01 --as-of-date 2026-09-11 --output-dir reports/etf_adaptive_targeted_studies/star50_extreme_window`

Expected: every study writes its manifest, score surface, daily-state and
reconciled attribution artifacts. Any result without complete OOS evidence is
reported as research-only and produces no operation sheet.

- [ ] **Step 5: Commit only the study definition and tests**

```bash
git add docs/user_demand/asset-allocation-strategy/etf-adaptive-targeted-study-v1.md tests/asset_allocation/etf_adaptive/research/test_experiment.py
git commit -m "docs: define targeted adaptive ETF studies"
```

## Plan self-review

- Spec coverage: Tasks 1–2 implement policy and fair benchmark abstraction;
  Task 3 implements stable risk-adjusted training selection; Task 4 implements
  recorded causal attribution; Task 5 implements experiment/report evidence;
  Task 6 applies the bounded studies and preserves all current gates.
- No-look-ahead, data/cost semantics and no automatic execution are global
  constraints and are asserted in Tasks 2–5.
- Interfaces are introduced in task order: policies before specs, specs before
  scoring, recorded observations before reporting, and reports before studies.
