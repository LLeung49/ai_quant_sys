# sector_rotation2 开发规格（指标与历史验证优先）

## 1. 目标与范围

### 1.1 目标

在不改动 `sector_rotation` 的前提下，新建一个可独立运行的 `sector_rotation2`：每日为申万行业产出连续、多维、可解释的板块轮动特征，保存可追溯历史快照，并生成可直接用于 IC、分组收益和样本外验证的研究数据集。

首个可交付版本的终点为：给定任意有效交易日，均可重算并落库该日全部有效板块的特征、评分、状态和未来收益标签；每日运行可产出供晨会消费的 CSV/文本摘要。可视化只保证数据字段、查询接口和输出结构，不实现图表。

### 1.2 明确不在本期实现

- 四象限、热力图、雷达图和交互式前端。
- 自动下单、仓位管理或把评分直接解释为买卖指令。
- 用全样本拟合得到“最优”参数后直接上线。
- 修改 `sector_rotation` 中任意 Python 文件或其既有输出格式。

### 1.3 关键设计决策

1. `sector_rotation2` 是独立包。需要沿用旧逻辑时，复制到新包，不允许 `import sector_rotation...`；复制文件的模块头必须写明来源文件、复制日期和优化差异。
2. `trade_sector_daily`、`trade_stock_daily_qfq`、`trade_stock_status` 是只读上游数据；新版派生数据获批准新建专用持久化表，且只写入 `sector_rotation_` 前缀的表。
3. 主评分只使用连续标准化分数，`phase` 仅作解释标签，不再使用旧版固定 `PHASE_BONUS`。
4. 初版权重固定且版本化；调权必须由滚动训练/样本外评估结果批准，不能依据单段历史收益人工调参。
5. 每次运行都必须带 `as_of_date`、`model_version`、`data_version`，支持同日重跑幂等覆盖。

## 2. 当前实现基线与迁移边界

旧模块已形成“板块等权指数 → 三个强度指标 → 导数/离散 phase → `score + phase_bonus`”的单日管线。可用的上游字段包括：

- `trade_sector_daily`：`close_idx`、`total_amount`、`rise_count`、`fall_count`、`flat_count`、`limit_up`、`limit_down`、`stock_count`、`kline_stock_count`。
- `trade_stock_daily_qfq`：股票日线及 `amount`，用于个股 RVOL 的中位数和量能广度。
- `trade_stock_status`：当前申万一级/二级成员映射。

下列复制关系必须在新文件头部注释中逐项记录：

| 新文件 | 复制/参考来源 | 新版差异 |
| --- | --- | --- |
| `data_loader.py` | `sector_loader.py` | 批量面板加载、日期完整性校验、读取广度字段；不依赖旧包。 |
| `derivatives.py` | `derivatives.py` | 保留 ROC、MA 斜率、MACD 的基础计算，新增 RS5/RS20、标准化辅助函数。 |
| `sector_features.py` | `industry_strength.py`、`inflection_detector.py` | 用每日特征面板替代三指标静态评分和硬投票。 |
| `snapshot_store.py` | 无 | 新增快照、运行审计和幂等 upsert。 |
| `backtest.py` | 无 | 新增未来超额收益标签、IC、分组收益和样本外评估。 |

不得复制旧的 `PHASE_BONUS`。不得通过修改 `sys.path` 后导入旧模块；新包内部使用相对导入或以 `python -m` 运行。

## 3. 目标目录与职责

```text
src/morning_conference/sector_rotation2/
├── __init__.py
├── config.py                    # 参数、字段列表、模型版本和初始权重
├── data_loader.py               # 上游查询、批量面板、数据质量检查
├── derivatives.py               # 纯 Pandas/Numpy 时间序列计算
├── normalizers.py               # 截面 percentile / robust-z，纯函数
├── sector_features.py           # 单板块日特征和全截面特征面板
├── scoring.py                   # 五类连续分数、phase/confidence、综合评分
├── market_regime.py             # 市场状态标签及 regime multiplier
├── snapshot_store.py             # DDL、运行审计、快照写入与查询
├── backtest.py                  # 标签、IC、分组收益、滚动样本外评估
├── report.py                    # CSV、晨会文本摘要，不含图表
├── run_daily.py                 # 每日/指定日重算入口
├── run_backtest.py              # 研究评估入口
└── doc/
    └── sector_rotation2_development_spec.md
tests/
├── test_sector_rotation2_data_loader.py
├── test_sector_rotation2_derivatives.py
├── test_sector_rotation2_features.py
├── test_sector_rotation2_scoring.py
├── test_sector_rotation2_snapshot_store.py
├── test_sector_rotation2_backtest.py
└── test_sector_rotation2_run_daily.py
```

所有计算函数接收 DataFrame/Series 并返回值，不在函数内部打印、写库或访问环境变量；I/O 仅位于 `data_loader.py`、`snapshot_store.py` 和两个入口脚本。

## 4. 数据契约与完整性规则

### 4.1 板块日面板

`load_sector_panel(level, start_date, end_date, min_history_days)` 返回：

```python
dict[str, pd.DataFrame]  # key=sector_name，index=DatetimeIndex（升序且唯一）
```

每个 DataFrame 至少含：

```text
open, high, low, close, amount, change_pct,
stock_count, kline_stock_count, rise_count, fall_count, flat_count,
limit_up, limit_down
```

规则：

- `close <= 0`、`amount < 0`、重复交易日、日期不升序均视为数据质量错误，记录到运行审计并跳过该板块。
- `kline_stock_count / stock_count < 0.80` 时该日 `coverage_ratio` 仍输出，但该板块不参与当日截面排名；阈值放在配置中。
- 需要 61 个有效交易日的指标必须至少有 61 行共同日期；不足者的值为 `NaN`，不得以 0 填充。
- 市场基准使用同一 `level` 的有效板块等权价格指数和成交额求和，且必须只由当日可参与排名的板块组成，避免样本碎片化。

### 4.2 个股量能面板

`load_sector_stock_amounts(sector_name, level, dates)` 返回当前成员在日期区间内的 `stock_code, trade_date, amount, close` 面板。初版使用 `trade_stock_status` 的当前行业映射，并在每条快照中写入 `membership_asof_mode='current_mapping'`。

这是已知口径限制：若未来需要严格历史成分，必须先引入成分变更历史表，再将该字段切换为 `historical_mapping`；在此之前，回测报告必须显示该限制。

## 5. 指标定义与初版参数

### 5.1 原始价格与相对强度

对板块 (s)、交易日 (t)、市场基准 (m)：

```text
ret_5  = close_t / close_{t-5} - 1
ret_20 = close_t / close_{t-20} - 1
rs_5   = ret_5(s)  - ret_5(m)
rs_20  = ret_20(s) - ret_20(m)
rs_60  = ret_60(s) - ret_60(m)
distance_ma20 = close_t / MA20_t - 1
distance_ma60 = close_t / MA60_t - 1
ma20_slope = 20 日均线在最近 10 日的最小二乘斜率，按 252 日年化并除以 MA 均值
rs20_accel = rs_20(t) - rs_20(t-5)
ma20_accel = ma20_slope(t) - ma20_slope(t-5)
macd_hist_delta = MACD_HIST(t) - MACD_HIST(t-1)
multi_horizon_accel = rs_5 - 0.25 * rs_20
```

MACD 参数固定为 12/26/9。所有时间窗口和权重定义于 `config.py`，并写入 `model_version` 的配置哈希。

### 5.2 量能与资金关注

```text
rvol_5_20 = mean(amount[t-4:t]) / mean(amount[t-19:t])
rvol_5_60 = mean(amount[t-4:t]) / mean(amount[t-59:t])
amount_share = sector_amount_t / sum(valid_sector_amount_t)
share_impulse = amount_share_t / mean(amount_share[t-19:t])
median_stock_rvol = median_i(amount_i,t / mean(amount_i[t-19:t]))
breadth_rvol = count_i(stock_rvol_i > 1) / count_i(valid_stock_rvol_i)
```

`amount_share` 必须使用同一层级、同一交易日、完成覆盖检查后的有效板块总成交额。`rvol_*`、`share_impulse`、`median_stock_rvol` 先取自然对数再参与截面标准化；非正数不取对数，记为缺失。

### 5.3 广度与覆盖率

```text
breadth_up = rise_count / (rise_count + fall_count + flat_count)
breadth_above_ma20 = count_i(close_i,t > MA20_i,t) / count_i(valid_i)
breadth_new_high_20 = count_i(close_i,t >= rolling_max(close_i, 20)) / count_i(valid_i)
coverage_ratio = kline_stock_count / stock_count
```

分母为 0 时记为缺失。初版将 `breadth_up` 从 `trade_sector_daily` 读取，另外两项由个股面板计算；若个股面板缺失，保留板块主特征和 `breadth_up`，但 `participation_score` 置为缺失并从综合分加权分母中移除。

### 5.4 截面标准化与五类连续分数

每天、同一 `level`、通过覆盖检查的板块构成截面。对每个原始指标使用百分位映射：

```text
pctl(x) = (rank(x, method='average') - 1) / (valid_count - 1)
signed_pctl(x) = 2 * pctl(x) - 1
```

若有效样本数小于 20，或某指标截面无变化，则该项为缺失，不伪造区分度。反向指标先取负号再计算百分位。

```text
trend_level_score = mean(signed_pctl(rs_20), signed_pctl(rs_60),
                         signed_pctl(distance_ma20), signed_pctl(distance_ma60))
strength_score = trend_level_score  # 仅为晨会语义兼容保留的别名
velocity_score = 0.40*signed_pctl(rs_5)
               + 0.35*signed_pctl(rs_20)
               + 0.25*signed_pctl(ma20_slope)
acceleration_score = 0.40*signed_pctl(rs20_accel)
                   + 0.35*signed_pctl(ma20_accel)
                   + 0.25*signed_pctl(macd_hist_delta)
volume_score = 0.50*signed_pctl(log(rvol_5_20))
             + 0.50*signed_pctl(log(share_impulse))
participation_score = mean(signed_pctl(breadth_up),
                           signed_pctl(breadth_above_ma20),
                           signed_pctl(breadth_new_high_20),
                           signed_pctl(breadth_rvol))
```

`multi_horizon_accel` 作为诊断字段输出但不进入 v1 加速度分，待阶段 4 的增量 IC 评估后再决定是否替换 `macd_hist_delta`。

各组内采用“可用项等权重归一化”：只有当一组至少有 2 项可用时才输出该组分数；`volume_score` 两项均缺失时为缺失。所有分数范围为 `[-1, 1]`。

### 5.5 综合评分、phase 与置信度

初版固定权重：

```text
base_score = weighted_mean(
    trend_level_score: 0.45,
    velocity_score: 0.25,
    acceleration_score: 0.15,
    participation_score: 0.15,
)
composite_score = base_score * regime_multiplier
```

`weighted_mean` 仅在可用组间重新归一化；若可用权重和低于 0.60，`score_eligible=False`，保留原始特征但不产生 `composite_rank`。

`phase_raw` 由连续分数和迟滞阈值给出。进入状态采用 `±0.25`，保持已有方向采用 `±0.10`；这两个阈值均应用于 `velocity_score` 和 `acceleration_score`，防止边界往复切换：

| velocity_score | acceleration_score | phase_raw |
| --- | --- | --- |
| >= +threshold | >= +threshold | `accel_up` |
| >= +threshold | <= -threshold | `decel_up` |
| <= -threshold | <= -threshold | `accel_down` |
| <= -threshold | >= +threshold | `bottoming_candidate` |
| 其他 | `neutral` |

`phase_confirmed` 使用“最近 3 日至少出现 2 次”的确认规则，且候选非中性状态至少保持 2 日才允许切换；否则保持上一确认状态，首次无历史时为 `neutral`。`phase_age` 是确认状态连续持续的交易日数。

`bottoming_candidate` 永远不产生推荐加分；只有同时满足以下至少两个条件，才输出 `reversal_confirmed`：`rs_5 > 0`、`distance_ma20 > 0`、`breadth_up > 0.50`、`share_impulse > 1`、`velocity_score` 穿越 0、`composite_rank` 连续两日改善。其余 `bottoming_candidate` 保持为观察状态。

`phase_confidence = min(1, 0.35*abs(velocity_score) + 0.35*abs(acceleration_score) + 0.20*max(participation_score, 0) + 0.10*persistence_score)`，其中 `persistence_score=min(phase_age/3, 1)`。任一速度或加速度轴缺失时为缺失；参与度缺失时该项从分母移除并重新归一化。`phase` 不可调整 `composite_score`。

### 5.6 市场状态

初版市场状态基于市场基准：

| 条件（按顺序匹配） | market_regime | regime_multiplier |
| --- | --- | --- |
| 基准收盘 < MA60、breadth_up 中位数 < 0.45，且全市场限跌数大于限涨数 | `risk_off` | 0.70 |
| 20 日收益绝对值 >= 8% 或 20 日收益率标准差位于过去 252 日 80 分位以上 | `high_volatility` | 0.85 |
| 收盘 > MA20 > MA60、breadth_up 中位数 >= 0.55，且全市场成交额高于自身 20 日均值 | `risk_on` | 1.00 |
| 其他 | `range` | 0.90 |

`regime_multiplier` 是风险暴露缩放参数，不改变同日行业排序；若所有板块共享同一 multiplier，`composite_rank` 应按 `base_score` 排序并同时输出两列，避免不必要重排。

## 6. 持久化模型

迁移脚本置于 `sql/`，命名为 `YYYYMMDD_create_sector_rotation_persistence_tables.sql`；须显式使用 `utf8mb4`、`InnoDB`。不能在运行入口里隐式建表。

### 6.1 `sector_rotation_run_log`

记录每次运行，主键 `run_id CHAR(36)`：

```text
run_id, as_of_date, sector_level, model_version, config_hash,
source_max_trade_date, status, started_at, finished_at,
eligible_sector_count, skipped_sector_count, error_summary, created_at
```

`status ∈ {running, succeeded, failed}`。失败运行不写入正式日快照，必须保留错误摘要。

### 6.2 `sector_rotation_sector_daily_snapshot`

唯一键 `(as_of_date, sector_level, sector_name, model_version)`。字段分五组：

- 标识与审计：`as_of_date, sector_level, sector_name, model_version, run_id, membership_asof_mode, coverage_ratio, score_eligible`。
- 原始指标：本规格 5.1–5.3 中所有 `ret_*`、`rs_*`、均线距离、导数、RVOL、份额、广度字段。
- 分数：五个 `*_score`、`base_score, composite_score, strength_rank, velocity_rank, acceleration_rank, participation_rank, composite_rank`。
- 状态：`phase_raw, phase_confirmed, phase_age, phase_confidence, phase_changed, market_regime, regime_multiplier`。
- 变动：`rank_change_1d, rank_change_5d, top10_days_20`，首次无法计算时为 `NULL`。

数值使用 `DECIMAL(18,8)`；排名使用 `INT`；枚举状态使用 `VARCHAR(32)`。快照 upsert 时仅允许同一唯一键的同版本重算覆盖；重跑必须产生新 `run_id` 并更新 `run_id/updated_at`。

### 6.3 `sector_rotation_sector_forward_return`

唯一键 `(as_of_date, sector_level, sector_name, horizon)`：

```text
as_of_date, sector_level, sector_name, horizon, target_date,
sector_return, benchmark_return, excess_return, label_ready_at, created_at
```

`horizon ∈ {5, 10}`。仅当未来第 N 个交易日存在时写入；不得将自然日误作交易日。

### 6.4 `sector_rotation_backtest_metric`

唯一键 `(evaluation_date, sector_level, model_version, horizon, metric_name, window_name)`，保存 `ic, rank_ic, top_group_excess_return, bottom_group_excess_return, long_short_return, turnover, sample_count` 等研究结果。评估结果必须可追溯到快照版本。

## 7. 对外接口与每日执行流

### 7.1 Python 接口

```python
def build_daily_feature_panel(
    level: int, as_of_date: str, min_history_days: int = 90
) -> pd.DataFrame: ...

def score_feature_panel(panel: pd.DataFrame, config: ModelConfig) -> pd.DataFrame: ...

def apply_phase_history(
    scored: pd.DataFrame, previous: pd.DataFrame | None
) -> pd.DataFrame: ...

def classify_market_regime(
    benchmark: pd.DataFrame, breadth_history: pd.Series, as_of_date: pd.Timestamp
) -> MarketRegime: ...

def persist_daily_snapshot(
    df: pd.DataFrame, run: RunMetadata
) -> int: ...

def build_forward_return_labels(
    level: int, start_date: str, end_date: str, horizons: tuple[int, ...] = (5, 10)
) -> int: ...
```

### 7.2 `run_daily.py`

```bash
python -m morning_conference.sector_rotation2.run_daily \
  --level 2 --as-of-date 2026-08-03 --model-version v1 --output outputs
```

执行顺序：

1. 校验上游最大交易日不早于 `as_of_date`，创建 `running` 审计记录。
2. 读取 90 个以上交易日的板块与个股数据，建立市场基准并完成质量过滤。
3. 计算原始指标、截面分数、市场状态、phase 确认和排名变动。
4. 在单个数据库事务中 upsert 快照并将运行置为 `succeeded`。
5. 输出 `sector_rotation2_daily_{date}.csv`、`sector_rotation2_topN_{date}.txt`、`sector_rotation2_data_quality_{date}.csv`。
6. 任何异常均回滚快照事务、标记运行失败并以非零退出码退出。

默认只计算指定交易日；`--backfill-start/--backfill-end` 用于按交易日顺序回填，回填时 `phase_confirmed` 必须使用前一日快照。

### 7.3 晨会输出最低字段

主 CSV 的每个板块至少包括：

```text
sector_name, composite_rank, composite_score, base_score,
trend_level_score, strength_score, velocity_score, acceleration_score, volume_score,
participation_score, phase_confirmed, phase_confidence, market_regime,
rank_change_1d, rank_change_5d, top10_days_20, coverage_ratio
```

文本摘要包括 Top 10、当日新进 Top 10、排名上升最多的 5 个板块、`accel_up`/`decel_down` 列表、数据覆盖告警和市场状态。措辞是“观察/候选/风险提示”，不得使用确定性交易承诺。

## 8. 回测与研究规范

### 8.1 标签和防前视偏差

- T 日快照只能使用 T 日收盘前已经落库的数据；未来收益从 T 收盘至 T+N 收盘计算。
- 每日截面排名与分组仅使用当日有效板块；不得用未来存在与否筛选 T 日样本。
- `phase_confirmed` 只读取 T-1 及以前快照。
- 行业成员采用当前映射这一限制必须出现在每份回测报告开头。

### 8.2 必做评估

对 `trend_level_score`、`velocity_score`、`acceleration_score`、`volume_score`、`participation_score`、`base_score` 和 `composite_score`，分别计算 5/10 日：

1. Pearson IC、Spearman Rank IC、均值、标准差、ICIR 和有效样本数；并单列 `multi_horizon_accel` 对 v1 加速度分的增量 IC。
2. 每日五分组的未来超额收益、Top - Bottom 多空差、胜率和最大回撤。
3. Top 10 的单日换手率、连续在榜天数、1 日/5 日排名变动。
4. `risk_on/risk_off/range/high_volatility` 四类状态下的独立统计。
5. 以 252 个交易日训练、63 个交易日验证、按 21 日步长向前滚动的样本外结果。

初版不根据评估结果自动调权。只有满足以下准入条件，才可提交新的 `model_version` 权重方案：至少两个独立样本外窗口中 `composite_score` 的 5 日 Rank IC 均值为正，Top 组相对 Bottom 组平均超额收益为正，且换手率不高于当前版本的 120%。

## 9. 实施计划与验收

### 阶段 0：独立骨架与数据库迁移

- 建立目标目录、`config.py`、包导入方式及 SQL 迁移。
- 复制并改造数据加载/导数纯函数，在文件头记录来源与差异。
- 为四张已批准的新表创建 DDL、索引与唯一键；测试迁移 SQL 含全部表和唯一约束。

验收：`python -m pytest tests/test_sector_rotation2_data_loader.py tests/test_sector_rotation2_derivatives.py -q` 通过；旧模块无文件变更。

### 阶段 1：可靠数据加载与原始特征

- 实现批量板块面板、市场基准、个股量能加载和日期/覆盖率校验。
- 实现 5.1–5.3 的全部原始特征，并为缺失数据保留原因字段。
- 用固定小型 DataFrame 编写单元测试，覆盖窗口边界、零成交额、缺日期、低覆盖和基准对齐。

验收：对手工构造样本，各公式精确匹配预期；同日有效板块集合在所有截面指标中一致。

### 阶段 2：连续评分、状态和排名历史

- 实现 percentile 标准化、可用项权重归一化、五类分数和各类排名。
- 实现市场状态、三日 phase 确认、置信度、排名变化和 Top10 持续天数。
- 为相同值、样本不足、单组部分缺失、phase 切换与重新进入 Top10 编写测试。

验收：不产生 `PHASE_BONUS` 或离散 phase 加分；每个 `score_eligible=True` 行的 `composite_rank` 从 1 连续编号且排序与 `base_score` 一致。

### 阶段 3：快照、幂等运行和晨会输出

- 实现运行审计、事务 upsert、同日同版本重跑、失败回滚及 CSV/文本输出。
- 实现单日、指定历史日和顺序回填 CLI；输出数据质量文件。
- 用 monkeypatch/fake DB 验证 SQL 参数、事务顺序、失败状态和非零退出。

验收：同一命令连续运行两次，快照唯一键行数不增加、特征结果一致、`run_id` 更新；失败时没有半成品快照。

### 阶段 4：未来标签与回测研究

- 按交易日生成 5/10 日未来板块和基准收益标签。
- 实现 IC、分组收益、换手率、最大回撤和 market regime 分桶统计。
- 实现滚动训练/验证切分并将结果写入 `sector_rotation_backtest_metric` 与 CSV。

验收：合成收益序列中标签、IC 和分组收益均与手算一致；回测代码检测并拒绝日期乱序或目标日早于标签期的输入。

### 阶段 5：历史回填与上线前基线报告

- 先回填可用历史区间的日快照，再生成已成熟日期的未来标签与基线报告。
- 人工核查至少 10 个交易日、覆盖上涨/下跌/震荡行情，确认字段、市场状态和 phase 解释合理。
- 固化 `v1` 的配置哈希、回填范围、数据限制和基线指标。

验收：产生可复现的研究报告，且报告明确样本起止、板块数量、缺失率、当前成员映射限制和样本外统计。

## 10. 测试、质量门槛与交付物

### 10.1 最低测试集

- 单元测试：所有公式、标准化、评分、phase、状态、标签和排序。
- 集成测试：伪造数据库返回，覆盖一日运行、回填顺序、幂等重跑和事务回滚。
- 回归测试：旧的 `tests/test_sector_loader.py` 必须继续通过。
- 数据质量测试：重复日期、负成交额、缺 `close`、低覆盖、样本不足、截面少于 20 个板块。

建议验收命令：

```bash
python -m pytest tests/test_sector_rotation2_*.py tests/test_sector_loader.py -q
python -m morning_conference.sector_rotation2.run_daily --level 2 --as-of-date YYYY-MM-DD --model-version v1 --output outputs
python -m morning_conference.sector_rotation2.run_backtest --level 2 --start-date YYYY-MM-DD --end-date YYYY-MM-DD --model-version v1
```

### 10.2 最终交付物

1. 独立的 `sector_rotation2` 实现、SQL 迁移和完整自动化测试。
2. 可重跑的每日快照、数据质量 CSV、晨会摘要和历史特征 CSV。
3. 5/10 日标签及含 IC、分组收益、换手率、状态分桶和滚动样本外结果的基线报告。
4. 一份面向后续可视化的字段字典：横轴 `velocity_score`、纵轴 `acceleration_score`、气泡 `volume_score`、颜色 `phase_confirmed`、透明度 `phase_confidence`、边框 `participation_score`、轨迹为最近 5 个交易日坐标。

## 11. 上线后再决策项

以下事项必须以阶段 5 的样本外报告为输入，再形成独立变更规格：

- 将百分位标准化替换为 robust-z 的必要性。
- 五类分数的权重、`phase` 阈值和 regime 参数调整。
- 是否引入严格历史行业成分映射。
- 哪些字段进入可视化主视图，以及四象限图的交互设计。
- 等权收益与市值加权收益差：该指标依赖按历史日期可得的自由流通市值或可靠市值权重；当前上游表未提供，禁止以当前市值回填历史。取得该数据后再作为 `leadership_concentration_score` 的独立规格实现。

## 12. 与 `sector_rotation_optimization.md` 的覆盖核对

| 优化方案项 | 当前规格处理 | 说明 |
| --- | --- | --- |
| 四类状态：趋势位置、速度、加速度、参与度 | 已覆盖 | `trend_level_score`、`velocity_score`、`acceleration_score`、`participation_score` 均为独立连续分数。 |
| 使用 RS20、弱化 MOM/ROC 重复 | 已补充 | 趋势位置改为 RS20/RS60/MA 距离；绝对 `ret_20` 不再单独驱动评分。 |
| 加速度消除市场共同上涨 | 已补充 | v1 用 `rs20_accel` 取代绝对 `roc_accel`；保留多周期加速度作研究诊断。 |
| MACD 柱与其变化的语义统一 | 已覆盖 | 加速度评分只使用 `macd_hist_delta`，`macd_hist` 仅作原始诊断字段。 |
| RVOL、成交额份额及其冲量 | 已覆盖 | 同时输出 5/20、5/60 RVOL、`amount_share`、`share_impulse` 和 `volume_score`。 |
| 广度及典型个股放量 | 已覆盖 | 有上涨广度、MA20 广度、新高广度、`median_stock_rvol`、`breadth_rvol`。 |
| 少数龙头主导识别 | 有意延后 | 历史流通市值数据缺失；禁止使用错误的当前市值替代。 |
| 连续 phase、迟滞、持续性、置信度 | 已补充 | 进入/退出阈值、最近 3 日 2 次确认、最短保持期、`phase_age` 和含参与度/持续性的置信度均已明确。 |
| 筑底候选与反转确认分离 | 已补充 | `bottoming_candidate` 不加分；达到两个确认条件才标注 `reversal_confirmed`。 |
| 位置维度与 phase 联合解释 | 已覆盖 | `distance_ma20/60` 进入位置分，并可与 phase、参与度共同输出。 |
| 取消 `PHASE_BONUS`，以 IC/样本外决定权重 | 已覆盖 | phase 不进主评分；阶段 4/5 规定了 IC、分组、滚动样本外和版本准入条件。 |
| 市场状态层 | 已增强 | 加入趋势、广度、成交额和限涨跌聚合判断；小/大盘相对强弱因指数数据依赖列为后续。 |
| 历史快照、排名变化、5 日轨迹 | 已覆盖 | 日快照、排名字段、Top10 持续性及可视化轨迹数据均已定义。 |
