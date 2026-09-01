# ETF Adaptive Strategy Research and Report Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Run staged parameter selection, rolling out-of-sample validation, exposure/product ranking, portfolio tests, and reproducible reports over the historical domestic-equity-ETF universe.

**Architecture:** Build research orchestration around the deterministic backtest engine. GRID and TREND families are screened separately inside each training window, stable neighborhoods are combined, parameters are frozen for the following 126 sessions, and only stitched OOS results drive the Pareto shortlist.

**Tech Stack:** Python 3.11+, pandas, numpy, scipy, pytest, JSON/CSV/Markdown artifacts.

**Spec:** `docs/user_demand/asset-allocation-strategy/防御与宽基ETF层自适应网格+趋势策略-回测规格-v1.md`

## Global Constraints

- Requires both the data-foundation and backtest-core plans.
- Warm-up is 252 sessions; training is 504 sessions; OOS validation is 126 sessions; step is 126 sessions.
- Validation parameters are selected only from prior training data and remain frozen through the validation segment.
- Run buy-and-hold, fixed-50%-hold, grid-only, trend-only, and full-adaptive baselines.
- Do not rank with one arbitrary weighted score; retain a Pareto set over return, drawdown, stability, and execution cost.
- Funds with less than three years of usable history are observation candidates.
- Reports must retain all attempted parameter configurations and failures.

---

### Task 1: Build deterministic parameter families and stable-neighborhood selection

**Files:**
- Create: `src/asset_allocation/etf_adaptive/research/parameters.py`
- Create: `src/asset_allocation/etf_adaptive/research/__init__.py`
- Test: `tests/asset_allocation/etf_adaptive/research/test_parameters.py`

**Interfaces:**
- Produces: `grid_candidates()`, `trend_candidates()`, `stable_parameter_neighborhood(results, axes, min_positive_window_share)`, and `ParameterCandidate`.
- Consumes: `AdaptiveConfig` from the backtest core.

- [ ] **Step 1: Write failing candidate-count and isolated-peak tests**

```python
def test_grid_candidates_cover_exact_approved_space() -> None:
    candidates = grid_candidates()
    assert {candidate.grid.step_pct for candidate in candidates} == {value / 1000 for value in range(10, 65, 5)}
    assert {candidate.grid.unit_pct for candidate in candidates} == {0.05, 0.10, 0.15, 0.20}


def test_isolated_best_parameter_is_not_stable() -> None:
    results = _surface(center_return=0.20, neighbor_returns=(-0.01, -0.02))
    assert stable_parameter_neighborhood(results, axes=("step_pct", "unit_pct"), min_positive_window_share=0.60) == ()
```

- [ ] **Step 2: Run parameter tests and verify failure**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research/test_parameters.py -q`

Expected: FAIL because the research parameter module is absent.

- [ ] **Step 3: Implement exact approved spaces and deterministic ordering**

```python
GRID_STEPS = tuple(value / 1000 for value in range(10, 65, 5))
GRID_UNITS = (0.05, 0.10, 0.15, 0.20)
FIXED_INITIAL = (0.30, 0.40, 0.50, 0.60, 0.70)
RISK_PER_UNIT = (0.0025, 0.0050, 0.0075, 0.0100)
ADD_N = (0.5, 0.75, 1.0)
MAX_UNITS = (2, 3, 4)
AMOUNT_RATIO = (None, 1.0, 1.2, 1.5)
```

Represent every candidate with a canonical ID derived from its config hash. Stable-neighborhood selection must require adjacent values on each tuned numeric axis and a majority of positive OOS subperiods; return the middle candidate when a plateau has even cardinality using the more conservative risk value.

- [ ] **Step 4: Run parameter tests**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research/test_parameters.py -q`

Expected: PASS.

- [ ] **Step 5: Commit parameter research**

```powershell
git add src/asset_allocation/etf_adaptive/research tests/asset_allocation/etf_adaptive/research/test_parameters.py
git commit -m "feat: define adaptive ETF parameter families"
```

### Task 2: Implement walk-forward windows and staged selection

**Files:**
- Create: `src/asset_allocation/etf_adaptive/research/walk_forward.py`
- Test: `tests/asset_allocation/etf_adaptive/research/test_walk_forward.py`

**Interfaces:**
- Produces: `WalkForwardWindow`, `build_windows(trading_dates)`, and `run_staged_walk_forward(request) -> WalkForwardResult`.
- Consumes: parameter families and `AdaptiveBacktestEngine`.

- [ ] **Step 1: Write failing boundary and freeze tests**

```python
def test_windows_use_504_train_126_validation_and_126_step() -> None:
    dates = _trading_dates(882)
    windows = build_windows(dates)
    assert len(windows[0].train_dates) == 504
    assert len(windows[0].validation_dates) == 126
    assert windows[1].validation_dates[0] == dates[630]


def test_validation_never_calls_selector_with_validation_returns() -> None:
    selector = SpySelector()
    run_staged_walk_forward(_request(selector=selector))
    assert all(call.max_date <= call.window.train_end for call in selector.calls)
```

- [ ] **Step 2: Run walk-forward tests and verify failure**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research/test_walk_forward.py -q`

Expected: FAIL because walk-forward orchestration is absent.

- [ ] **Step 3: Implement staged training and frozen validation**

```python
def build_windows(trading_dates: Sequence[date]) -> tuple[WalkForwardWindow, ...]:
    dates = tuple(sorted(set(trading_dates)))
    windows = []
    for validation_start in range(504, len(dates) - 126 + 1, 126):
        windows.append(WalkForwardWindow(
            window_id=f"wf_{len(windows):03d}",
            train_dates=dates[validation_start - 504:validation_start],
            validation_dates=dates[validation_start:validation_start + 126],
        ))
    return tuple(windows)
```

Within each training window: run GRID-only candidates, retain stable GRID neighborhoods, run TREND-only candidates, retain stable TREND neighborhoods, combine only retained candidates, then freeze the selected full configuration for validation. Persist training evidence and validation results separately.

- [ ] **Step 4: Run walk-forward tests**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research/test_walk_forward.py -q`

Expected: PASS.

- [ ] **Step 5: Commit walk-forward selection**

```powershell
git add src/asset_allocation/etf_adaptive/research/walk_forward.py tests/asset_allocation/etf_adaptive/research/test_walk_forward.py
git commit -m "feat: add staged ETF walk-forward validation"
```

### Task 3: Implement baselines, performance metrics, and attribution

**Files:**
- Create: `src/asset_allocation/etf_adaptive/research/baselines.py`
- Create: `src/asset_allocation/etf_adaptive/research/metrics.py`
- Test: `tests/asset_allocation/etf_adaptive/research/test_metrics.py`

**Interfaces:**
- Produces: `run_baselines`, `calculate_performance(nav, trades) -> PerformanceMetrics`, and `attribute_by_mode(events) -> ModeAttribution`.
- Consumes: raw backtest results and explicit dividends/costs.

- [ ] **Step 1: Write failing drawdown, cost, and mode-attribution tests**

```python
def test_metrics_use_cost_net_nav_and_report_recovery_sessions() -> None:
    metrics = calculate_performance(_nav([1.0, 0.8, 0.9, 1.01]), _trades(cost=0.01))
    assert metrics.max_drawdown == pytest.approx(-0.20)
    assert metrics.recovery_sessions == 3
    assert metrics.total_cost == pytest.approx(0.01)


def test_mode_attribution_reconciles_to_total_pnl() -> None:
    attribution = attribute_by_mode(_events(grid=10.0, trend=20.0, transition=-2.0, costs=3.0))
    assert attribution.net_total == pytest.approx(25.0)
```

- [ ] **Step 2: Run metrics tests and verify failure**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research/test_metrics.py -q`

Expected: FAIL because metrics and baselines are absent.

- [ ] **Step 3: Implement all approved metrics and five baselines**

```python
def max_drawdown(nav: pd.Series) -> float:
    drawdown = nav / nav.cummax() - 1.0
    return float(drawdown.min())


def cvar(returns: pd.Series, alpha: float = 0.05) -> float:
    cutoff = returns.quantile(alpha)
    return float(returns.loc[returns <= cutoff].mean())
```

Implement annualized return/volatility, Sharpe, Sortino, Calmar, worst 126-session return, CVaR5, win rate, payoff ratio, profit factor, turnover, minimum-commission share, unfilled share, and slippage degradation. Baselines must share the same T+1 execution, costs, corporate actions, and eligible-date inputs.

- [ ] **Step 4: Run metrics tests**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research/test_metrics.py -q`

Expected: PASS.

- [ ] **Step 5: Commit metrics and baselines**

```powershell
git add src/asset_allocation/etf_adaptive/research/baselines.py src/asset_allocation/etf_adaptive/research/metrics.py tests/asset_allocation/etf_adaptive/research/test_metrics.py
git commit -m "feat: measure adaptive ETF strategy performance"
```

### Task 4: Implement exposure/product Pareto selection and portfolio validation

**Files:**
- Create: `src/asset_allocation/etf_adaptive/research/selection.py`
- Create: `src/asset_allocation/etf_adaptive/research/portfolio.py`
- Test: `tests/asset_allocation/etf_adaptive/research/test_selection.py`
- Test: `tests/asset_allocation/etf_adaptive/research/test_portfolio.py`

**Interfaces:**
- Produces: `pareto_front`, `rank_exposure_groups`, `select_product_per_index`, `build_equal_weight`, and `build_inverse_volatility`.
- Consumes: stitched OOS metrics, point-in-time ETF metadata, and return series.

- [ ] **Step 1: Write failing Pareto, duplicate-index, and weight-cap tests**

```python
def test_dominated_candidate_is_removed_without_weighted_score() -> None:
    candidates = [_candidate("A", ret=0.10, drawdown=0.10, positive_windows=0.8),
                  _candidate("B", ret=0.08, drawdown=0.15, positive_windows=0.6)]
    assert [row.code for row in pareto_front(candidates)] == ["A"]


def test_inverse_volatility_weights_respect_fifty_percent_cap() -> None:
    weights = build_inverse_volatility({"A": 0.05, "B": 0.20, "C": 0.25}, cap=0.50)
    assert sum(weights.values()) == pytest.approx(1.0)
    assert max(weights.values()) <= 0.50
```

- [ ] **Step 2: Run selection/portfolio tests and verify failure**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research/test_selection.py tests/asset_allocation/etf_adaptive/research/test_portfolio.py -q`

Expected: FAIL because selection and portfolio functions are absent.

- [ ] **Step 3: Implement two-level selection and 2-4 ETF portfolios**

```python
def dominates(left: CandidateMetrics, right: CandidateMetrics) -> bool:
    no_worse = (left.annual_return >= right.annual_return and
                left.max_drawdown_abs <= right.max_drawdown_abs and
                left.positive_window_share >= right.positive_window_share and
                left.cost_ratio <= right.cost_ratio)
    strictly_better = (left.annual_return > right.annual_return or
                       left.max_drawdown_abs < right.max_drawdown_abs or
                       left.positive_window_share > right.positive_window_share or
                       left.cost_ratio < right.cost_ratio)
    return no_worse and strictly_better
```

Group by point-in-time tracking-index code first, then choose one executable product per index using OOS evidence, history confidence, amount, data quality, and cost sensitivity. Validate all eligible 2-4 exposure combinations for equal weight and capped inverse volatility; report correlation, downside correlation, and drawdown overlap.

- [ ] **Step 4: Run selection/portfolio tests**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research/test_selection.py tests/asset_allocation/etf_adaptive/research/test_portfolio.py -q`

Expected: PASS.

- [ ] **Step 5: Commit selection and portfolio logic**

```powershell
git add src/asset_allocation/etf_adaptive/research/selection.py src/asset_allocation/etf_adaptive/research/portfolio.py tests/asset_allocation/etf_adaptive/research/test_selection.py tests/asset_allocation/etf_adaptive/research/test_portfolio.py
git commit -m "feat: select adaptive ETF portfolios"
```

### Task 5: Generate reproducible artifacts and operator report

**Files:**
- Create: `src/asset_allocation/etf_adaptive/research/report.py`
- Create: `src/asset_allocation/etf_adaptive/research/run_research.py`
- Test: `tests/asset_allocation/etf_adaptive/research/test_report.py`
- Test: `tests/asset_allocation/etf_adaptive/research/test_run_research.py`

**Interfaces:**
- Produces: CLI `python -m asset_allocation.etf_adaptive.research.run_research --as-of-date YYYY-MM-DD --output-dir PATH` and immutable JSON/CSV/Markdown artifacts.
- Consumes: Tasks 1-4 results and canonical config hashes.

- [ ] **Step 1: Write failing manifest and report tests**

```python
def test_report_manifest_records_all_attempts_and_data_cutoff(tmp_path: Path) -> None:
    manifest = write_research_report(_research_result(), tmp_path)
    payload = json.loads((tmp_path / "manifest.json").read_text(encoding="utf-8"))
    assert payload["data_cutoff"] == "2026-09-01"
    assert payload["attempted_config_count"] == 12
    assert payload["failed_config_count"] == 2
    assert payload["config_hash"] == manifest.config_hash
```

- [ ] **Step 2: Run report tests and verify failure**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research/test_report.py tests/asset_allocation/etf_adaptive/research/test_run_research.py -q`

Expected: FAIL because report generation is absent.

- [ ] **Step 3: Implement atomic artifact generation**

```python
def publish_directory(staging: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    os.replace(staging, destination)
```

Write sorted artifacts for universe audit, attempted configs, failed configs, window selections, stitched OOS NAV, trades, mode attribution, cost scenarios, exposure ranking, product ranking, Pareto set, portfolio comparisons, and a Chinese Markdown executive report. Write into a sibling staging directory and atomically rename only after every artifact succeeds.

- [ ] **Step 4: Run the complete research test slice**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research -q`

Expected: PASS.

Run: `git diff --check`

Expected: exit 0.

- [ ] **Step 5: Commit the research runner and report**

```powershell
git add src/asset_allocation/etf_adaptive/research/report.py src/asset_allocation/etf_adaptive/research/run_research.py tests/asset_allocation/etf_adaptive/research/test_report.py tests/asset_allocation/etf_adaptive/research/test_run_research.py
git commit -m "feat: report adaptive ETF research results"
```
