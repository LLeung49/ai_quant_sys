# ETF GRID/TREND 风险调整后研究 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (- [ ]) syntax for tracking.

**Goal:** 在不改变 GRID/TREND 交易结构的前提下，建立风险调整后 OOS 参数研究、报告和人工操作单准入闭环。

**Architecture:** 新增 `research.decision` 纯函数契约层，接收策略/B&H OOS 指标、参数稳定性与暴露归因，输出明确门控结论。验证层负责训练/OOS 隔离与受控参数搜索；报告层仅序列化记录的证据；层级研究与 shadow runner 只接受身份完整的 `passed` 结论。

**Tech Stack:** Python 3、dataclasses、pytest、matplotlib、既有 AdaptiveConfig/backtest engine/MySQL shadow store。

**Spec:** `docs/superpowers/specs/2026-09-10-etf-grid-trend-risk-adjusted-research-design.md`

## Global Constraints

- 不改变 GRID/TREND 入场、网格加减仓、趋势加仓；不实现核心仓/卫星仓和自动券商下单。
- 选参只能读取训练窗口；每项结论保留数据截止日、配置哈希与训练/OOS 边界。
- 数据完整性、raw/qfq 仿射一致性、无未来函数、参数邻域稳定性是 `passed` 前提；任何失败均失败关闭。
- 报告并列年化、波动率、回撤、夏普、索提诺、卡玛、CVaR(5%)、126 日最差收益、修复期、换手、成本和暴露归因。
- 只有两个层级均 `passed` 的完整研究可生成供人工确认的操作建议。
- 不以可任意调权的单一总分判断；没有 PIT 成分证据的蓝筹历史池不能放行防御层。

## File Structure

- Create: `src/asset_allocation/etf_adaptive/research/decision.py` — 风险调整后比较、四类结论和层级准入。
- Modify: `research/parameters.py` — 已批准退出/过滤轴与准确邻域。
- Modify: `research/instrument_validation.py` — OOS 指标、训练面和暴露证据。
- Modify: `research/validation_report.py` — 摘要、全指标、归因及图表。
- Modify: `research/layer_benchmark.py`, `research/benchmark_contracts.py`, `run_shadow_daily.py` — 层级结论和人工建议准入。
- Test: `test_decision.py`, `test_parameters.py`, `test_instrument_validation.py`, `test_validation_report.py`, `test_benchmark_contracts.py`, `test_run_shadow_daily.py`。

### Task 1: 风险调整后决策契约

**Files:**
- Create: `src/asset_allocation/etf_adaptive/research/decision.py`
- Modify: `src/asset_allocation/etf_adaptive/research/__init__.py`
- Test: `tests/asset_allocation/etf_adaptive/research/test_decision.py`

**Interfaces:**
- Produces: `ResearchConclusion`, `ResearchEvidence`, `DecisionSummary`, `evaluate_research_decision(evidence: ResearchEvidence) -> DecisionSummary`.

- [ ] **Step 1: Write failing tests**

```python
def test_small_return_lag_with_material_risk_improvement_is_optimizable() -> None:
    result = evaluate_research_decision(_evidence(
        annual_excess=-.004, drawdown_improvement=.12,
        sharpe_excess=.35, sortino_excess=.40, calmar_excess=.20,
        cvar5_improvement=.01, stable_parameter_region=True, data_valid=True,
    ))
    assert result.conclusion is ResearchConclusion.CONTINUE_PARAMETER_OPTIMIZATION

def test_invalid_data_fails_closed() -> None:
    assert evaluate_research_decision(_evidence(data_valid=False)).conclusion is ResearchConclusion.DO_NOT_TRADE
```

- [ ] **Step 2: Verify failure**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research/test_decision.py -q`
Expected: FAIL because the decision module does not exist.

- [ ] **Step 3: Implement immutable evidence and predicates**

```python
class ResearchConclusion(str, Enum):
    PASSED = "passed"
    CONTINUE_PARAMETER_OPTIMIZATION = "continue_parameter_optimization"
    EVALUATE_STRUCTURAL_CHANGE = "evaluate_structural_change"
    DO_NOT_TRADE = "do_not_trade"

@dataclass(frozen=True)
class ResearchEvidence:
    data_valid: bool
    oos_window_count: int
    oos_non_lagging_share: float
    stable_parameter_region: bool
    annual_excess: float
    drawdown_improvement: float
    sharpe_excess: float
    sortino_excess: float
    calmar_excess: float
    cvar5_improvement: float
    exposure_ratio: float
    turnover: float
    total_cost: float
```

Reject nonfinite values and bool-as-number. `PASSED` requires valid/stable evidence and positive risk-adjusted outcome; defensively improved but not passing evidence is `CONTINUE_PARAMETER_OPTIMIZATION`; persistent negative return and ratios is `EVALUATE_STRUCTURAL_CHANGE`; invalid/incomplete evidence is `DO_NOT_TRADE`.

- [ ] **Step 4: Verify pass**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research/test_decision.py -q`  
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add src/asset_allocation/etf_adaptive/research/decision.py src/asset_allocation/etf_adaptive/research/__init__.py tests/asset_allocation/etf_adaptive/research/test_decision.py
git commit -m "feat: add risk-adjusted research decisions"
```

### Task 2: 受控参数空间与稳定邻域

**Files:**
- Modify: `src/asset_allocation/etf_adaptive/research/parameters.py`
- Modify: `tests/asset_allocation/etf_adaptive/research/test_parameters.py`

**Interfaces:**
- Consumes: `GridConfig(atr_stop_multiple, cooldown_sessions)` 和 `TrendConfig(stop_n, require_macd_bullish)`。
- Produces: 扩展后的 `grid_candidates()`、`trend_candidates()`、`stable_parameter_neighborhood(results, axes, min_positive_window_share)`。

- [ ] **Step 1: Write failing tests**

```python
def test_grid_candidates_include_only_approved_exit_axes() -> None:
    grids = {candidate.config.grid for candidate in grid_candidates()}
    assert {item.atr_stop_multiple for item in grids} == {2.0, 3.0, 4.0}
    assert {item.cooldown_sessions for item in grids} == {0, 3, 5, 10}

def test_neighbor_must_match_every_other_axis() -> None:
    assert stable_parameter_neighborhood(surface, axes=("step_pct", "atr_stop_multiple"), min_positive_window_share=.75) == ()
```

- [ ] **Step 2: Verify failure**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research/test_parameters.py -q`
Expected: FAIL because the exit axes are absent and the current scan permits nonmatching neighbors.

- [ ] **Step 3: Implement approved axes only**

Add `GRID_ATR_STOP_MULTIPLES=(2.0,3.0,4.0)`, `GRID_COOLDOWN_SESSIONS=(0,3,5,10)`, `TREND_STOP_N=(1.5,2.0,2.5,3.0)`, and `TREND_REQUIRE_MACD_BULLISH=(False,True)`. To keep walk-forward execution bounded, screen one newly added exit/filter axis at a time around each existing training-selected base candidate; do not materialize the full cross-product of all new and existing axes. Index each screened surface point by complete axis tuple. Numeric neighbors must match all nonchanged axes; both MACD categorical values must be observed and pass. Preserve all existing parameter values and do not change strategy logic.

- [ ] **Step 4: Verify pass**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research/test_parameters.py tests/asset_allocation/etf_adaptive/test_contracts.py -q`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add src/asset_allocation/etf_adaptive/research/parameters.py tests/asset_allocation/etf_adaptive/research/test_parameters.py
git commit -m "feat: screen stable exit parameter regions"
```

### Task 3: OOS 验证证据与结论

**Files:**
- Modify: `src/asset_allocation/etf_adaptive/research/instrument_validation.py`
- Modify: `tests/asset_allocation/etf_adaptive/research/test_instrument_validation.py`

**Interfaces:**
- Consumes: Task 1 决策、Task 2 候选、`calculate_performance`、`build_result_attribution`。
- Produces: `InstrumentValidationResult.decision`、训练面摘要、窗口指标、持仓/空仓交易日。

- [ ] **Step 1: Write failing OOS-isolation tests**

```python
def test_oos_price_changes_do_not_change_selected_training_hashes() -> None:
    before = run_instrument_validation(target, provider, START, AS_OF, CASH)
    provider.mutate_only_validation_prices()
    after = run_instrument_validation(target, provider, START, AS_OF, CASH)
    assert [item.config_hash for item in before.windows] == [item.config_hash for item in after.windows]

def test_formal_target_activates_only_for_passed_decision() -> None:
    assert _result_with(ResearchConclusion.CONTINUE_PARAMETER_OPTIMIZATION).activation_eligible is False
```

- [ ] **Step 2: Verify failure**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research/test_instrument_validation.py -q`
Expected: FAIL because the result has no decision and uses the legacy return/drawdown gate.

- [ ] **Step 3: Implement recorded-evidence assembly**

Extend `ValidationWindowResult` with nullable strategy/B&H metrics and invested/cash sessions. Build them only after execution from recorded NAV/events. Preserve training-only selection and serialize training surface hashes, axes and signs; never feed OOS values back into selection. Data exceptions retain `ValidationStatus.DATA_REJECTED` and receive a `DO_NOT_TRADE` decision. A formal target activates only with `PASSED`.

- [ ] **Step 4: Verify pass**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research/test_instrument_validation.py tests/asset_allocation/etf_adaptive/research/test_validation_eligibility.py -q`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add src/asset_allocation/etf_adaptive/research/instrument_validation.py tests/asset_allocation/etf_adaptive/research/test_instrument_validation.py
git commit -m "feat: classify ETF OOS research evidence"
```

### Task 4: 决策报告、图表与归因

**Files:**
- Modify: `src/asset_allocation/etf_adaptive/research/validation_report.py`
- Modify: `tests/asset_allocation/etf_adaptive/research/test_validation_report.py`

**Interfaces:**
- Consumes: Task 3 结果、窗口指标、训练面及已有 `build_result_attribution`。
- Produces: 兼容的 `ValidationArtifactManifest` 和原子 JSON/CSV/Markdown/PNG 产物。

- [ ] **Step 1: Write failing artifact tests**

```python
def test_report_contains_decision_metrics_exposure_and_evidence(tmp_path: Path) -> None:
    summary = json.loads(write_validation_artifacts(_passed_result(), tmp_path / "513100.SH").summary_json.read_text(encoding="utf-8"))
    assert summary["decision"]["conclusion"] == "passed"
    assert summary["comparison"]["strategy"]["sortino"] is not None
    assert summary["execution"]["exposure_ratio"] == pytest.approx(.75)

def test_missing_metrics_are_not_silently_zeroed(tmp_path: Path) -> None:
    summary = json.loads(write_validation_artifacts(_invalid_result(), tmp_path / "bad").summary_json.read_text(encoding="utf-8"))
    assert summary["comparison"] is None
```

- [ ] **Step 2: Verify failure**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research/test_validation_report.py -q`
Expected: FAIL because current artifacts omit decision/exposure and Markdown contains malformed text.

- [ ] **Step 3: Implement canonical report payloads**

Add decision, full strategy/B&H metrics, metric differences/distributions, OOS count, exposure/cash, turnover/cost, event reasons, data cutoff, hashes and stable parameter interval to summary JSON. Write direct UTF-8 Chinese Markdown. Extend charts with drawdown and exposure panels, retaining actual fill markers and never replaying trades. Missing metrics remain `null` with a blocker.

- [ ] **Step 4: Verify pass**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research/test_validation_report.py -q`  
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add src/asset_allocation/etf_adaptive/research/validation_report.py tests/asset_allocation/etf_adaptive/research/test_validation_report.py
git commit -m "feat: publish risk-adjusted ETF validation reports"
```

### Task 5: 层级研究与人工操作单准入

**Files:**
- Modify: `src/asset_allocation/etf_adaptive/research/layer_benchmark.py`, `src/asset_allocation/etf_adaptive/research/benchmark_contracts.py`, `src/asset_allocation/etf_adaptive/run_shadow_daily.py`
- Modify: `tests/asset_allocation/etf_adaptive/research/test_benchmark_contracts.py`, `tests/asset_allocation/etf_adaptive/test_run_shadow_daily.py`

**Interfaces:**
- Consumes: 层级对齐策略/B&H OOS NAV、Task 1 决策和冻结 payload `research_approval`。
- Produces: `LayerBenchmarkResult.decision` 和严格建议单准入。

- [ ] **Step 1: Write failing layer and daily-gate tests**

```python
def test_layer_artifact_contains_risk_adjusted_conclusion() -> None:
    assert layer_benchmark_artifact(aggregate_layer_evidence(portfolio, evidence))["decision"]["conclusion"] == "continue_parameter_optimization"

def test_new_frozen_payload_requires_matching_passed_research_approval() -> None:
    with pytest.raises(ValueError, match="research approval"):
        _build_active_selection(_frozen_payload(research_approval=None))
```

- [ ] **Step 2: Verify failure**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research/test_benchmark_contracts.py tests/asset_allocation/etf_adaptive/test_run_shadow_daily.py -q`
Expected: FAIL because the current layer gate is return/drawdown-only and payload lacks approval identity.

- [ ] **Step 3: Implement fail-closed approval identity**

Attach strategy/B&H metrics and `DecisionSummary` to layer artifacts. A new `research_approval` must contain `conclusion="passed"`, matching `config_hash`, nonempty `universe_hash`, ISO `data_cutoff`, `data_audit_passed is True`, and passing defensive/broad-beta artifacts with identical identity. Legacy records remain readable for audit but cannot satisfy new approval. Do not add broker imports.

- [ ] **Step 4: Verify pass**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research/test_benchmark_contracts.py tests/asset_allocation/etf_adaptive/test_run_shadow_daily.py -q`  
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add src/asset_allocation/etf_adaptive/research/layer_benchmark.py src/asset_allocation/etf_adaptive/research/benchmark_contracts.py src/asset_allocation/etf_adaptive/run_shadow_daily.py tests/asset_allocation/etf_adaptive/research/test_benchmark_contracts.py tests/asset_allocation/etf_adaptive/test_run_shadow_daily.py
git commit -m "feat: gate advice on approved layer research"
```

### Task 6: 回归、真实数据回测与归档

**Files:**
- Modify: `docs/user_demand/asset-allocation-strategy/防御与宽基ETF层自适应网格+趋势策略-回测规格-v1.md`
- Create: `reports/etf_validation_risk_adjusted_2021/`（运行产物，不提交）
- Test: `tests/asset_allocation/etf_adaptive/research/`

- [ ] **Step 1: Update acceptance checklist**

在回测规格增加四类结论、全部必需指标、`reference_only` 限制、两层均通过才可建议交易；不得写入未运行结果。

- [ ] **Step 2: Run full targeted regression**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research tests/asset_allocation/etf_adaptive/test_run_shadow_daily.py tests/asset_allocation/etf_adaptive/test_market_data.py tests/asset_allocation/etf_adaptive/test_execution.py tests/asset_allocation/etf_adaptive/test_engine.py -q`
Expected: PASS；独立记录缓存权限警告。

- [ ] **Step 3: Run fixed-universe OOS validation**

Run: `$env:PYTHONPATH='src'; python -m asset_allocation.etf_adaptive.run_instrument_validation --start-date 2021-01-01 --as-of-date 2026-09-08 --output-dir reports/etf_validation_risk_adjusted_2021`
Expected: 每目标原子生成 JSON/CSV/Markdown/PNG；异常数据为 `do_not_trade`/`data_rejected`，研究不得静默修数。

- [ ] **Step 4: Inspect evidence-backed recommendation**

逐一核对正式 ETF 的结论、OOS 数、参数稳定性、暴露与建议。仅日期对齐、PIT 有效子层可聚合；任一层未 `passed` 时明确“无每日操作单授权”。出现结构评估结论时仅归档失败模式。

- [ ] **Step 5: Commit documentation only**

```bash
git add "docs/user_demand/asset-allocation-strategy/防御与宽基ETF层自适应网格+趋势策略-回测规格-v1.md"
git commit -m "docs: record risk-adjusted ETF validation gates"
```

不要暂存 `reports/`，除非用户明确要求版本化生成报告。

## Plan Self-Review

- Task 1 覆盖三道门与四类结论；Task 2 仅扩展已批准退出/过滤参数；Task 3 保证训练/OOS 隔离；Task 4 覆盖报告、图表和归因；Task 5 覆盖层级与人工建议闸门；Task 6 覆盖回归与重跑。
- 本计划没有全市场 ETF 寻优、无 PIT 蓝筹结论、策略结构替换或自动下单。
- 每项任务均有失败测试、最小实现、验证与独立提交。
