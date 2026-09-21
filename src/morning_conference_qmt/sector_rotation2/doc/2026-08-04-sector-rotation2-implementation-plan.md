# Sector Rotation2 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use \`superpowers:subagent-driven-development\` (recommended) or \`superpowers:executing-plans\` to implement this plan task-by-task. Steps use checkbox (\`- [ ]\`) syntax for tracking.

**Goal:** 交付一个独立、可按日运行的板块轮动特征管线，提供版本化历史快照和无前视偏差的 5/10 日研究评估。

**Architecture:** 新包只读既有板块/股票源表，自行实现所有计算并写入专属派生表。纯特征和评分函数与数据库 I/O 分离；每日入口保存快照，研究入口生成标签和统计结果。

**Tech Stack:** Python 3.13、pandas、numpy、pytest、既有 \`data_ingestion.db_config\`、MySQL/InnoDB。

## Global Constraints

- 不得导入 \`morning_conference.sector_rotation\`，复制逻辑时须写明来源及差异。
- 不得修改 \`src/morning_conference/sector_rotation/\` 内任何文件。
- 上游只读：\`trade_sector_daily\`、\`trade_stock_daily_qfq\`、\`trade_stock_status\`。
- 所有派生数据只写已批准的 \`sector_rotation_\` 前缀表；每日运行记录配置哈希和 \`model_version='v1'\`。
- \`phase\` 不得给 \`base_score\` 或 \`composite_score\` 加固定 bonus。
- 测试只能使用 DataFrame 或 fake DB，不能依赖 QMT、生产库或当前日期。

---

## File Structure

| Path | Responsibility |
| --- | --- |
| \`config.py\` | 参数、字段、权重和配置哈希。 |
| \`normalizers.py\` | 截面百分位与缺失权重归一化。 |
| \`derivatives.py\` | 复制并改造的纯时间序列指标。 |
| \`data_loader.py\` | SQL、面板加载、质量校验及市场聚合。 |
| \`sector_features.py\` | 原始特征面板。 |
| \`scoring.py\`、\`market_regime.py\` | 连续评分、排名、phase、市场状态。 |
| \`snapshot_store.py\` | 运行审计、事务和快照读写。 |
| \`report.py\`、\`run_daily.py\` | 晨会输出和每日/回填入口。 |
| \`backtest.py\`、\`run_backtest.py\` | 标签、回测统计和研究入口。 |
| \`sql/20260804_create_sector_rotation_persistence_tables.sql\` | 四张已批准的板块轮动派生表迁移。 |

## Task 1: 配置与标准化基础

**Files:**
- Create: \`src/morning_conference/sector_rotation2/config.py\`
- Create: \`src/morning_conference/sector_rotation2/normalizers.py\`
- Test: \`tests/test_sector_rotation2_normalizers.py\`

**Interfaces:**
- Produces: \`ModelConfig\`, \`DEFAULT_CONFIG\`, \`config_hash(config) -> str\`。
- Produces: \`signed_percentile(series, minimum_count=20)\`、\`weighted_available_mean(frame, weights, minimum_weight)\`。

- [ ] **Step 1: 写失败测试**

    def test_signed_percentile_maps_values():
        result = signed_percentile(pd.Series([1., 2., 3.]), minimum_count=3)
        assert result.tolist() == [-1., 0., 1.]

    def test_signed_percentile_small_cross_section_is_nan():
        assert signed_percentile(pd.Series([1., 2.]), minimum_count=3).isna().all()

- [ ] **Step 2: 运行失败测试**

  Run: \`python -m pytest tests/test_sector_rotation2_normalizers.py -q\`  
  Expected: FAIL，提示模块不存在。

- [ ] **Step 3: 最小实现**

  实现冻结的 \`ModelConfig\`：最小截面 20、覆盖率 0.80、phase 进入/保持阈值 0.25/0.10、最低可用权重 0.60，权重为 trend 0.45、velocity 0.25、acceleration 0.15、participation 0.15。百分位公式为 \`2*(rank-1)/(n-1)-1\`；不足样本或常数列返回 NaN。哈希用排序 JSON 的 SHA-256。

- [ ] **Step 4: 补齐缺失权重与哈希测试**

    def test_available_weights_are_renormalized():
        frame = pd.DataFrame({"a": [1.], "b": [float("nan")]})
        assert weighted_available_mean(frame, {"a": .45, "b": .55}, .40).iloc[0] == 1.

- [ ] **Step 5: 验证并提交**

  Run: \`python -m pytest tests/test_sector_rotation2_normalizers.py -q\`  
  Expected: PASS.  
  Commit: \`git commit -m "feat: add sector rotation2 scoring configuration"\`

## Task 2: 独立导数与相对强度计算

**Files:**
- Create: \`src/morning_conference/sector_rotation2/derivatives.py\`
- Test: \`tests/test_sector_rotation2_derivatives.py\`

**Interfaces:**
- Produces: \`ma_slope\`, \`macd_hist\`, \`relative_strength\`, \`rs_acceleration\`, \`multi_horizon_acceleration\`。

- [ ] **Step 1: 写失败测试**

    def test_relative_strength_is_sector_return_less_benchmark_return():
        sector = pd.Series([100., 110., 121.])
        bench = pd.Series([100., 105., 110.])
        assert relative_strength(sector, bench, 2).iloc[-1] == pytest.approx(.11)

    def test_rs_acceleration_uses_relative_strength():
        assert rs_acceleration(pd.Series([.01, .02, .05]), lag=2).iloc[-1] == pytest.approx(.04)

- [ ] **Step 2: 运行失败测试**

  Run: \`python -m pytest tests/test_sector_rotation2_derivatives.py -q\`  
  Expected: FAIL。

- [ ] **Step 3: 实现**

  文件头标注复制自旧 \`derivatives.py\`，但不导入旧包；保持 MACD 12/26/9。相对强度必须先对齐索引，计算 \`sector.pct_change(n)-benchmark.pct_change(n)\`；加速度为 RS 减其 5 日滞后；多周期加速度为 \`rs5 - .25*rs20\`。

- [ ] **Step 4: 增加边界测试**

  覆盖历史不足、日期不重叠、平坦价格和 \`macd_hist\` 与 \`macd_hist.diff()\` 的不同语义。

- [ ] **Step 5: 验证并提交**

  Run: \`python -m pytest tests/test_sector_rotation2_derivatives.py -q\`  
  Expected: PASS.  
  Commit: \`git commit -m "feat: add independent sector rotation derivatives"\`

## Task 3: 迁移与快照持久化

**Files:**
- Create: \`sql/20260804_create_sector_rotation_persistence_tables.sql\`
- Create: \`src/morning_conference/sector_rotation2/snapshot_store.py\`
- Test: \`tests/test_sector_rotation2_snapshot_store.py\`

**Interfaces:**
- Produces: \`create_run\`, \`mark_run_failed\`, \`persist_daily_snapshot\`, \`load_previous_snapshot\`, \`load_snapshot_range\`。

- [ ] **Step 1: 写迁移失败测试**

    def test_migration_has_required_tables_and_unique_key():
        sql = Path("sql/20260804_create_sector_rotation_persistence_tables.sql").read_text(encoding="utf-8")
        assert "sector_rotation_run_log" in sql
        assert "sector_rotation_sector_daily_snapshot" in sql
        assert "sector_rotation_sector_forward_return" in sql
        assert "sector_rotation_backtest_metric" in sql
        assert "uq_snapshot (as_of_date, sector_level, sector_name, model_version)" in sql

- [ ] **Step 2: 运行失败测试**

  Run: \`python -m pytest tests/test_sector_rotation2_snapshot_store.py -q\`  
  Expected: FAIL。

- [ ] **Step 3: 实现 DDL 和 store**

  建立已批准的 \`sector_rotation_run_log\`、\`sector_rotation_sector_daily_snapshot\`、\`sector_rotation_sector_forward_return\`、\`sector_rotation_backtest_metric\` 表，使用 InnoDB/utf8mb4、规格中唯一键和 DECIMAL(18,8)。快照只允许参数化 \`INSERT ... ON DUPLICATE KEY UPDATE\`。上游异常时回滚快照写入，并把 run 标记为 failed。

- [ ] **Step 4: 写 fake DB 事务测试**

  测试同一唯一键使用 upsert、\`load_previous_snapshot\` 的日期严格小于 as_of_date、execute_many 抛错时没有 commit 且运行状态为 failed。

- [ ] **Step 5: 验证并提交**

  Run: \`python -m pytest tests/test_sector_rotation2_snapshot_store.py -q\`  
  Expected: PASS.  
  Commit: \`git commit -m "feat: add sector rotation2 snapshot persistence"\`

## Task 4: 数据加载、基准和质量门槛

**Files:**
- Create: \`src/morning_conference/sector_rotation2/data_loader.py\`
- Test: \`tests/test_sector_rotation2_data_loader.py\`

**Interfaces:**
- Produces: \`load_sector_panel\`, \`load_sector_stock_amounts\`, \`validate_sector_frame\`, \`build_market_benchmark\`, \`load_market_aggregates\`。

- [ ] **Step 1: 写失败测试**

    def test_validation_rejects_duplicate_dates_and_negative_amount():
        frame = pd.DataFrame({"close": [1., 1.1], "amount": [10., -1.]},
            index=pd.to_datetime(["2026-01-02", "2026-01-02"]))
        result = validate_sector_frame(frame)
        assert {"duplicate_trade_date", "negative_amount"} <= set(result.reasons)

- [ ] **Step 2: 运行失败测试**

  Run: \`python -m pytest tests/test_sector_rotation2_data_loader.py -q\`  
  Expected: FAIL。

- [ ] **Step 3: 实现**

  复制旧 loader 的 SQL 意图，不复制 import。加载 sector OHLC、成交额、涨跌家数、涨跌停、股票数量。个股面板从日线表 join 当前 \`trade_stock_status\`，每行写 \`membership_asof_mode='current_mapping'\`。基准仅由当日覆盖率不少于 0.80 的板块构成；市场聚合包含成交额、涨跌停和 breadth 中位数。

- [ ] **Step 4: 增加质量测试**

  验证低覆盖板块不进入排名，close 小于等于零、非升序日期和非正对数输入均被标记；验证基准只使用 eligible 集合。

- [ ] **Step 5: 验证并提交**

  Run: \`python -m pytest tests/test_sector_rotation2_data_loader.py tests/test_sector_loader.py -q\`  
  Expected: PASS.  
  Commit: \`git commit -m "feat: add sector rotation2 source data loader"\`

## Task 5: 原始特征面板

**Files:**
- Create: \`src/morning_conference/sector_rotation2/sector_features.py\`
- Test: \`tests/test_sector_rotation2_features.py\`

**Interfaces:**
- Produces: \`build_daily_feature_panel(level, as_of_date, min_history_days=90)\` 和 \`calculate_sector_features(sector, frame, benchmark, stock_panel)\`。

- [ ] **Step 1: 写失败测试**

    def test_amount_share_and_impulse_are_hand_calculated():
        result = calculate_sector_features("A", sector_frame(), benchmark_frame(), stock_panel())
        assert result["amount_share"] == pytest.approx(.20)
        assert result["share_impulse"] == pytest.approx(2.)

- [ ] **Step 2: 运行失败测试**

  Run: \`python -m pytest tests/test_sector_rotation2_features.py -q\`  
  Expected: FAIL。

- [ ] **Step 3: 实现全部原始指标**

  逐项生成 ret_5/20、rs_5/20/60、distance_ma20/60、MA slope、rs20_accel、ma20_accel、MACD 及 delta、rvol_5_20/5_60、amount_share、share_impulse、median_stock_rvol、breadth_rvol、breadth_up/above_ma20/new_high_20、coverage_ratio。历史不足一律 NaN，禁止以 0 填充。

- [ ] **Step 4: 写广度和缺失测试**

    def test_breadth_rvol_is_fraction_above_one():
        assert calculate_breadth_rvol(pd.Series([1.2, .8])) == .5

  再验证分母零、缺个股面板和少于 61 个交易日。

- [ ] **Step 5: 验证并提交**

  Run: \`python -m pytest tests/test_sector_rotation2_features.py -q\`  
  Expected: PASS.  
  Commit: \`git commit -m "feat: add sector rotation2 feature panel"\`

## Task 6: 连续评分、市场状态与 phase

**Files:**
- Create: \`src/morning_conference/sector_rotation2/scoring.py\`
- Create: \`src/morning_conference/sector_rotation2/market_regime.py\`
- Test: \`tests/test_sector_rotation2_scoring.py\`

**Interfaces:**
- Produces: \`score_feature_panel\`, \`apply_phase_history\`, \`classify_market_regime\`。

- [ ] **Step 1: 写失败测试**

    def test_phase_requires_two_of_last_three_candidate_days():
        current = scored_row(velocity_score=.30, acceleration_score=.30)
        history = phase_history(["neutral", "accel_up"])
        assert apply_phase_history(current, history).loc["A", "phase_confirmed"] == "accel_up"

    def test_bottoming_needs_two_reversal_conditions():
        row = scored_row(velocity_score=-.4, acceleration_score=.4, rs_5=.01, distance_ma20=.01)
        assert apply_phase_history(row, phase_history([])).loc["A", "phase_confirmed"] == "reversal_confirmed"

- [ ] **Step 2: 运行失败测试**

  Run: \`python -m pytest tests/test_sector_rotation2_scoring.py -q\`  
  Expected: FAIL。

- [ ] **Step 3: 实现评分和排名**

  对当日 eligible 截面做百分位。trend_level 为 RS20/RS60/MA20 距离/MA60 距离；strength_score 仅等于其别名。velocity、acceleration、volume、participation 严格按 spec 权重计算。base_score 只按可用分数重归一；可用权重低于 .60 不排名。component rank 和 composite_rank 均按分数，不按 phase。

- [ ] **Step 4: 实现状态机**

  风险状态按 risk_off、high_volatility、risk_on、range 的优先顺序。phase 使用 .25 进入/.10 保持、最近三日两次确认、最短两天保持。bottoming 必须命中 rs5、MA20、breadth、share impulse、velocity 穿零、连续改善排名中的至少两个条件。confidence 使用 velocity、acceleration、participation 与 phase_age。

- [ ] **Step 5: 增加边界测试并验证**

  覆盖常数截面、参与度缺失、阈值反复跨越、rank_change_1d/5d、top10_days_20 和 risk_off 的优先级。  
  Run: \`python -m pytest tests/test_sector_rotation2_normalizers.py tests/test_sector_rotation2_scoring.py -q\`  
  Expected: PASS.  
  Commit: \`git commit -m "feat: add sector rotation2 continuous scoring"\`

## Task 7: 每日入口与晨会输出

**Files:**
- Create: \`src/morning_conference/sector_rotation2/report.py\`
- Create: \`src/morning_conference/sector_rotation2/run_daily.py\`
- Test: \`tests/test_sector_rotation2_run_daily.py\`

**Interfaces:**
- Produces: \`run_one_date(level, as_of_date, config, output_dir)\`。
- CLI: \`--level --as-of-date --model-version --output --backfill-start --backfill-end\`。

- [ ] **Step 1: 写失败测试**

    def test_run_writes_only_after_persistence(monkeypatch, tmp_path):
        monkeypatch.setattr(run_daily, "build_daily_feature_panel", lambda **_: one_feature_panel())
        monkeypatch.setattr(run_daily, "persist_daily_snapshot", lambda df, run: len(df))
        run_daily.run_one_date(2, "2026-01-05", DEFAULT_CONFIG, tmp_path)
        assert (tmp_path / "sector_rotation2_daily_2026-01-05.csv").exists()

- [ ] **Step 2: 运行失败测试**

  Run: \`python -m pytest tests/test_sector_rotation2_run_daily.py -q\`  
  Expected: FAIL。

- [ ] **Step 3: 实现编排**

  创建 running 审计，按“特征→regime→评分→历史 phase→事务快照→输出”执行。仅 commit 成功后写 daily、TopN、data-quality 三个文件。异常时 rollback、标记 failed、CLI 非零退出。回填日期必须升序，以前一天快照确认 phase。

- [ ] **Step 4: 写回填/失败测试并验证**

  断言回填顺序升序；断言写入失败不产生成功 CSV。  
  Run: \`python -m pytest tests/test_sector_rotation2_run_daily.py -q\`  
  Expected: PASS.  
  Commit: \`git commit -m "feat: add sector rotation2 daily pipeline"\`

## Task 8: 未来标签与研究评估

**Files:**
- Create: \`src/morning_conference/sector_rotation2/backtest.py\`
- Create: \`src/morning_conference/sector_rotation2/run_backtest.py\`
- Test: \`tests/test_sector_rotation2_backtest.py\`

**Interfaces:**
- Produces: \`build_forward_return_labels(level, start_date, end_date, horizons=(5,10))\` 和 \`evaluate_factor(snapshots, labels, factor, horizon)\`。

- [ ] **Step 1: 写失败测试**

    def test_label_uses_fifth_future_trade_date():
        dates = pd.bdate_range("2026-01-01", periods=6)
        labels = make_forward_labels(pd.Series([100,101,102,103,104,110], index=dates), 5)
        assert labels.iloc[0]["target_date"] == dates[5]
        assert labels.iloc[0]["sector_return"] == pytest.approx(.10)

- [ ] **Step 2: 运行失败测试**

  Run: \`python -m pytest tests/test_sector_rotation2_backtest.py -q\`  
  Expected: FAIL。

- [ ] **Step 3: 实现**

  标签以交易日推进，写 sector/benchmark/excess return。评估输出 Pearson IC、Spearman IC、ICIR、五分组、Top-Bottom、换手、胜率、最大回撤和 regime 分桶。拒绝乱序日期、重复快照或 target_date 不晚于 as_of_date 的标签。

- [ ] **Step 4: 实现滚动样本外与测试**

  252 交易日训练、63 日验证、21 日步长；只记录评估，不自动换权。测试合成序列中 IC、分组收益和最大回撤的手算值。

- [ ] **Step 5: 验证并提交**

  Run: \`python -m pytest tests/test_sector_rotation2_backtest.py -q\`  
  Expected: PASS.  
  Commit: \`git commit -m "feat: add sector rotation2 research evaluation"\`

## Task 9: 全量验证与基线报告

**Files:**
- Create: \`src/morning_conference/sector_rotation2/doc/v1-baseline-report-template.md\`
- Modify: \`src/morning_conference/sector_rotation2/doc/sector_rotation2_development_spec.md\`
- Test: all \`tests/test_sector_rotation2_*.py\`

- [ ] **Step 1: 写基线报告模板**

  标题必须含 config hash、数据截止日、历史范围、membership mode、板块数、低覆盖数、5/10 日 IC/ICIR、五分组、换手、回撤、regime 分桶、滚动 OOS 窗口和“当前成分映射”的限制。

- [ ] **Step 2: 运行全量自动化验证**

  Run: \`python -m pytest tests/test_sector_rotation2_*.py tests/test_sector_loader.py -q\`  
  Expected: PASS，且无因数据库/QMT 缺失跳过的核心测试。

- [ ] **Step 3: 受控回填与研究命令**

  在迁移已由目标环境明确执行后运行：  
  \`python -m morning_conference.sector_rotation2.run_daily --level 2 --backfill-start YYYY-MM-DD --backfill-end YYYY-MM-DD --model-version v1 --output outputs\`  
  \`python -m morning_conference.sector_rotation2.run_backtest --level 2 --start-date YYYY-MM-DD --end-date YYYY-MM-DD --model-version v1 --output outputs\`

  Expected: 快照按日期顺序、标签只覆盖已成熟日期、报告显式记录 current_mapping 限制。

- [ ] **Step 4: 人工核查十个日期并提交**

  覆盖上涨、下跌、震荡市场；确认 phase 不影响排名、低覆盖不参与排名、bottoming_candidate 不被表述为推荐。  
  Commit: \`git commit -m "docs: add sector rotation2 baseline handoff"\`

## Plan self-review

- 覆盖性：任务 1–8 覆盖规格的参数、公式、表、快照、运行、标签和研究；任务 9 形成上线前证据。
- 边界：可视化、历史市值集中度和自动调权不在本计划实施范围内。
- 一致性：trend_level_score 为正式评分，strength_score 只是同值兼容别名；phase 永不影响综合排名。
