# ETF 可信验证与归因 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 以无预热污染的滚动样本外验证重新评估固定 ETF，并产出可复算的交易归因和三面板图表。

**Architecture:** 保留 `AdaptiveBacktestEngine` 的收盘决策与次日成交语义，新增研究专用的窗口边界：完整历史只用于指标和准入，验证期独立从初始状态开始记账。验证器消费该边界及已有基准运行器，输出结构化窗口结果；归因模块仅消费结果、行情和事件，生成 CSV/JSON/Markdown/PNG，绝不重新推导交易。

**Tech Stack:** Python 3、dataclasses、既有 AdaptiveBacktestEngine、pytest、pandas/matplotlib（仅报告导出）。

**Spec:** `docs/superpowers/specs/2026-09-09-etf-validation-and-manual-operation-design.md`

## Global Constraints

- 使用者人工下单；本计划不得导入 `xtquant`、`xtdata`、broker 或订单 API。
- T 日收盘后产生信号，订单最早在 T+1 交易日成交；不得同日成交。
- 验证预热期不得产生订单、成交、现金或仓位变动。
- 正式验证使用 `504/126/126`；`reference_only` 使用 `252/126/126` 且不得进入激活/冻结候选。
- 数据、日历、公司行为、价格口径或执行可用性无法证明时必须失败关闭并记录原因。
- 不复制 GRID/TREND 规则；研究和归因复用现有引擎事件、净值和状态。
- 所有产物绑定 `stock_code`、`as_of_date`、`execution_eligible_date`、`model_version`、`config_hash`、`data_cutoff`。

---

## File structure

- `src/asset_allocation/etf_adaptive/state.py`：增加验证期起点字段。
- `src/asset_allocation/etf_adaptive/engine.py`：预热计算指标但不在预热期记账或排单。
- `src/asset_allocation/etf_adaptive/research/validation_eligibility.py`：以真实历史生成逐日准入。
- `src/asset_allocation/etf_adaptive/research/validation_provider.py`：显式日期解析、完整历史与公司行为来源。
- `src/asset_allocation/etf_adaptive/research/instrument_validation.py`：训练参数、独立 OOS 验证和门槛汇总。
- `src/asset_allocation/etf_adaptive/research/attribution.py`：由事件和净值形成归因。
- `src/asset_allocation/etf_adaptive/research/report.py`：写 JSON、CSV、Markdown、PNG。
- `src/asset_allocation/etf_adaptive/run_instrument_validation.py`：执行固定标的并发布产物。

### Task 1: 隔离预热与验证期状态

**Files:**
- Modify: `src/asset_allocation/etf_adaptive/state.py`
- Modify: `src/asset_allocation/etf_adaptive/engine.py`
- Test: `tests/asset_allocation/etf_adaptive/test_engine.py`

**Interfaces:**
- Consumes: `BacktestRequest(stock_code, initial_cash, start_date, end_date, trade_start_date)`。
- Produces: `AdaptiveBacktestEngine.run_with_data(request, bars, eligibility_by_date, actions=()) -> BacktestResult`，其事件与净值仅包含 `trade_start_date` 起的会计结果。

- [ ] **Step 1: 写入失败测试：预热不改变验证账户**

```python
def test_warmup_calculates_indicators_but_never_emits_fills_or_nav_before_trade_start():
    result = engine.run_with_data(
        BacktestRequest("510300.SH", Decimal("100000"), warmup[0].trade_date,
                        validation[-1].trade_date, validation[0].trade_date),
        tuple(warmup + validation), eligibility,
    )
    assert all(event.event_date >= validation[0].trade_date for event in result.events)
    assert [point.nav_date for point in result.nav] == [bar.trade_date for bar in validation]
    assert result.nav[0].cash == Decimal("100000")
```

- [ ] **Step 2: 运行失败测试**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/test_engine.py -k warmup -q --basetemp=.pytest-task1`

Expected: FAIL，因为 `BacktestRequest` 尚无 `trade_start_date` 或预热会写入账户。

- [ ] **Step 3: 写入失败测试：验证首日信号只能在下一日成交**

```python
def test_validation_start_signal_is_not_filled_until_following_session():
    result = engine.run_with_data(request_with_trade_start, bars, eligibility)
    fills = [event for event in result.events if event.kind == "fill"]
    assert fills and fills[0].event_date == validation[1].trade_date
```

- [ ] **Step 4: 实现最小预热门控**

```python
trading_enabled = request.trade_start_date is None or bar.trade_date >= request.trade_start_date
if not trading_enabled:
    previous_ratio = bar.adjustment_ratio
    continue
# retain the current action, execution, close-decision and DailyNav blocks here
```

保留 `compute_indicators(bars)` 对全序列的计算；预热期间不得调用 `apply_session_actions`、`execute`、`process_close`，也不得将预热日订单写入 `pending`。

- [ ] **Step 5: 运行引擎测试**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/test_engine.py tests/asset_allocation/etf_adaptive/test_regime.py -q --basetemp=.pytest-task1-pass`

Expected: PASS；首个 ADX 位于 20–25 时仍无初始交易。

- [ ] **Step 6: 提交**

```bash
git add src/asset_allocation/etf_adaptive/state.py src/asset_allocation/etf_adaptive/engine.py tests/asset_allocation/etf_adaptive/test_engine.py tests/asset_allocation/etf_adaptive/test_regime.py
git commit -m "fix: isolate walk-forward validation warmup"
```

### Task 2: 真实历史准入与日期解析

**Files:**
- Modify: `src/asset_allocation/etf_adaptive/research/validation_eligibility.py`
- Modify: `src/asset_allocation/etf_adaptive/research/validation_provider.py`
- Test: `tests/asset_allocation/etf_adaptive/research/test_validation_eligibility.py`
- Test: `tests/asset_allocation/etf_adaptive/research/test_validation_provider.py`

**Interfaces:**
- Consumes: 完整 `tuple[DualPriceBar, ...]` 和请求日期。
- Produces: `validation_eligibility(stock_code, complete_history) -> dict[date, ETFEligibility]`；`resolve_validation_range(requested_start, requested_end, sessions) -> ResolvedDateRange`。

- [ ] **Step 1: 写入失败测试：不足历史不得通过**

```python
def test_validation_eligibility_uses_actual_history_count_not_a_forced_floor():
    result = validation_eligibility("513100.SH", bars[:251])
    last = result[bars[250].trade_date]
    assert last.history_session_count == 251
    assert "history_lt_252" in last.reasons
```

- [ ] **Step 2: 写入失败测试：非交易日解析必须显式**

```python
def test_resolve_validation_range_records_adjacent_sessions_for_weekend_request():
    resolved = resolve_validation_range(date(2026, 1, 3), date(2026, 1, 4), sessions)
    assert resolved.start_date == date(2026, 1, 5)
    assert resolved.end_date == date(2026, 1, 2)
    assert resolved.adjustments == ("start_forward", "end_backward")
```

- [ ] **Step 3: 实现最小真实准入和日期对象**

```python
@dataclass(frozen=True)
class ResolvedDateRange:
    requested_start: date; requested_end: date
    start_date: date; end_date: date
    adjustments: tuple[str, str]
```

准入 `history_session_count=len(history)`；历史少于 252、20 日平均成交额低于阈值、停牌或已知买入锁定时返回不可准入。保留 `daily_bar_assumption` 仅作质量告警，正式验证改为 `DataQualityError`，不得把它视为可成交证明。

- [ ] **Step 4: 运行提供者测试**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research/test_validation_eligibility.py tests/asset_allocation/etf_adaptive/research/test_validation_provider.py -q --basetemp=.pytest-task2`

Expected: PASS；无伪造 252 历史，解析调整可序列化。

- [ ] **Step 5: 提交**

```bash
git add src/asset_allocation/etf_adaptive/research/validation_eligibility.py src/asset_allocation/etf_adaptive/research/validation_provider.py tests/asset_allocation/etf_adaptive/research/test_validation_eligibility.py tests/asset_allocation/etf_adaptive/research/test_validation_provider.py
git commit -m "fix: make validation eligibility evidence-based"
```

### Task 3: 参数训练与独立 OOS 验证器

**Files:**
- Modify: `src/asset_allocation/etf_adaptive/research/instrument_validation.py`
- Modify: `src/asset_allocation/etf_adaptive/research/baselines.py`
- Test: `tests/asset_allocation/etf_adaptive/research/test_instrument_validation.py`
- Test: `tests/asset_allocation/etf_adaptive/research/test_baselines.py`

**Interfaces:**
- Consumes: `ValidationTarget`、完整对齐历史、`WalkForwardWindow` 和版本化 `ParameterCandidate`。
- Produces: `ValidationWindowResult`，新增 `selected_parameters`、`strategy_events`、`benchmark_events`、`resolved_range`；结果保留每个窗口完整可复算数据。

- [ ] **Step 1: 写入失败测试：正式窗口确实选择训练参数**

```python
def test_formal_validation_selects_training_candidate_and_records_hash(provider):
    result = run_instrument_validation(FORMAL_TARGET, provider, start, as_of, Decimal("100000"))
    assert result.windows[0].selected_parameters
    assert result.windows[0].config_hash != ""
```

- [ ] **Step 2: 写入失败测试：验证账户与训练账户隔离**

```python
def test_validation_window_first_nav_is_independent_of_training_fills(provider):
    window = run_instrument_validation(FORMAL_TARGET, provider, start, as_of, Decimal("100000")).windows[0]
    assert window.strategy_nav[0] == 1.0
    assert window.strategy_events[0].event_date >= window.validation_start
```

- [ ] **Step 3: 实现窗口执行器**

```python
def _run_validation_window(target, provider, window, config, initial_cash):
    bars = provider.load_bars(target.stock_code, window.train_dates[0], window.validation_end)
    request = BacktestRequest(target.stock_code, initial_cash, bars[0].trade_date,
                              window.validation_end, window.validation_dates[0])
    return run_baselines(request, provider, config)
```

删除 `elif False` 和从训练净值截取验证结果的 `_validation_nav`。训练候选仍只在训练子段跑；最终候选验证使用 Task 1 的 `trade_start_date`。B&H 也必须支持相同起点，在验证段第一可成交日建仓并按同一成本模型记账。

- [ ] **Step 4: 写入失败测试：reference-only 永不激活**

```python
def test_reference_only_result_is_labeled_and_never_activation_eligible(provider):
    result = run_instrument_validation(A500_TARGET, provider, start, as_of, Decimal("100000"))
    assert result.scope is ValidationScope.REFERENCE_ONLY
    assert result.activation_eligible is False
```

- [ ] **Step 5: 实现 scope 和门槛汇总**

为结果新增 `scope`、`activation_eligible`。正式目标只在 `annual_excess > 0`、`drawdown_excess <= .02`、非落后窗口严格超过一半时为 `PASSED`；`REFERENCE_ONLY` 始终不可激活但保留参考绩效。

- [ ] **Step 6: 运行研究测试**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research/test_instrument_validation.py tests/asset_allocation/etf_adaptive/research/test_baselines.py tests/asset_allocation/etf_adaptive/research/test_parameters.py -q --basetemp=.pytest-task3`

Expected: PASS；没有硬编码默认参数或训练资金泄漏。

- [ ] **Step 7: 提交**

```bash
git add src/asset_allocation/etf_adaptive/research/instrument_validation.py src/asset_allocation/etf_adaptive/research/baselines.py tests/asset_allocation/etf_adaptive/research/test_instrument_validation.py tests/asset_allocation/etf_adaptive/research/test_baselines.py
git commit -m "fix: run independent per-instrument OOS validation"
```

### Task 4: 交易归因与三面板可视化

**Files:**
- Create: `src/asset_allocation/etf_adaptive/research/attribution.py`
- Modify: `src/asset_allocation/etf_adaptive/research/report.py`
- Test: `tests/asset_allocation/etf_adaptive/research/test_attribution.py`
- Test: `tests/asset_allocation/etf_adaptive/research/test_report.py`

**Interfaces:**
- Consumes: `ValidationWindowResult`、`tuple[DualPriceBar, ...]`、对应指标快照。
- Produces: `WindowAttribution` 与 `write_validation_artifacts(result, output_dir) -> ArtifactManifest`。

- [ ] **Step 1: 写入失败测试：归因只使用已发生事件**

```python
def test_attribution_groups_fill_events_without_creating_synthetic_trades():
    attribution = build_window_attribution(window, bars)
    assert attribution.by_reason["trend_entry"].fill_count == 1
    assert attribution.by_reason["grid_buy"].fill_count == 0
    assert attribution.trade_points[0].event_date == known_fill_date
```

- [ ] **Step 2: 写入失败测试：报告输出四类文件**

```python
def test_write_validation_artifacts_creates_json_csv_markdown_and_png(tmp_path):
    manifest = write_validation_artifacts(result, tmp_path)
    assert manifest.summary_json.exists()
    assert manifest.trades_csv.exists()
    assert manifest.report_markdown.exists()
    assert manifest.chart_png.exists()
```

- [ ] **Step 3: 实现归因不可变模型**

```python
@dataclass(frozen=True)
class ReasonAttribution:
    reason: str; fill_count: int; shares: int; estimated_cost: Decimal

@dataclass(frozen=True)
class WindowAttribution:
    window_id: str; trade_points: tuple[TradePoint, ...]
    by_reason: Mapping[str, ReasonAttribution]
    invested_sessions: int; cash_sessions: int
```

从 `BacktestEvent(kind="fill"|"rejected_order")` 提取点位；以策略 `DailyNav.market_value > 0` 统计持仓天数。事件日期不在行情中时抛出 `DataQualityError`。

- [ ] **Step 4: 实现报告和图**

用 matplotlib 三个共享 x 轴面板：价格/实际成交及原因标记，MA20/布林带/ADX/ATR 指标，策略与 B&H 标准化净值。JSON 包含窗口、身份和告警；CSV 输出成交与拒单；Markdown 列门槛、参数和归因。绘图失败必须使产物生成失败。

- [ ] **Step 5: 运行归因与报告测试**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive/research/test_attribution.py tests/asset_allocation/etf_adaptive/research/test_report.py -q --basetemp=.pytest-task4`

Expected: PASS；图表、机器可读产物与事件数量一致。

- [ ] **Step 6: 提交**

```bash
git add src/asset_allocation/etf_adaptive/research/attribution.py src/asset_allocation/etf_adaptive/research/report.py tests/asset_allocation/etf_adaptive/research/test_attribution.py tests/asset_allocation/etf_adaptive/research/test_report.py
git commit -m "feat: export ETF validation attribution artifacts"
```

### Task 5: CLI、真实数据试跑与回归验证

**Files:**
- Modify: `src/asset_allocation/etf_adaptive/run_instrument_validation.py`
- Modify: `tests/asset_allocation/etf_adaptive/test_run_instrument_validation.py`
- Modify: `docs/user_demand/asset-allocation-strategy/防御与宽基ETF层自适应网格+趋势策略-回测规格-v1.md`

**Interfaces:**
- Consumes: `--stock-code`（可选）、`--start-date`、`--as-of-date`、`--output-dir`、`--initial-cash`。
- Produces: 每标的 `ArtifactManifest`；仅数据拒绝退出码为 2，研究通过/失败为 0。

- [ ] **Step 1: 写入失败测试：CLI 输出单标的报告**

```python
def test_cli_writes_one_manifest_per_requested_stock(monkeypatch, tmp_path):
    exit_code = main(["--stock-code", "159915.SZ", "--start-date", "2022-01-01",
                      "--as-of-date", "2026-09-08", "--output-dir", str(tmp_path)])
    assert exit_code == 0
    assert (tmp_path / "159915.SZ" / "summary.json").exists()
```

- [ ] **Step 2: 实现 CLI 汇总**

先解析日期，再逐标的验证并写产物。控制台输出 target、scope、状态、年化收益、最大回撤、窗口数和路径；不得把 `reference_only` 显示为可激活通过。

- [ ] **Step 3: 运行完整 ETF 测试集**

Run: `$env:PYTHONPATH='src'; python -m pytest tests/asset_allocation/etf_adaptive -q --basetemp=.pytest-etf-validation-final`

Expected: PASS。

- [ ] **Step 4: 数据库单标的冒烟验证**

Run: `$env:PYTHONPATH='src'; python -m asset_allocation.etf_adaptive.run_instrument_validation --stock-code 159915.SZ --start-date 2022-01-04 --as-of-date 2026-09-08 --initial-cash 100000 --output-dir reports/etf_validation`

Expected: 生成 `reports/etf_validation/159915.SZ/` 的 JSON、CSV、Markdown、PNG；无论通过或失败均带完整质量与归因证据。

- [ ] **Step 5: 更新规格并提交**

补充“预热不记账、正式结论须引用产物、reference_only 不得激活、每日人工操作单由下一计划实施”。然后：

```bash
git add src/asset_allocation/etf_adaptive/run_instrument_validation.py tests/asset_allocation/etf_adaptive/test_run_instrument_validation.py docs/user_demand/asset-allocation-strategy/防御与宽基ETF层自适应网格+趋势策略-回测规格-v1.md
git commit -m "feat: publish reproducible ETF validation reports"
```

## Plan self-review

- 规格第 1–4 节由任务 1–3 覆盖；价格、日历、状态和参数的失败关闭均有测试。
- 规格第 5 节由任务 4–5 覆盖；图表使用事件而非重算交易。
- 规格第 6–7 节（每日人工操作单、账户回填）与验证器可独立部署，放入下一份计划，防止未验证策略先指导真实资金。
- 接口顺序一致：Task 1 定义 `trade_start_date`，Task 2 定义日期解析，Task 3 扩展窗口结果，Task 4 消费窗口结果，Task 5 消费报告接口。
