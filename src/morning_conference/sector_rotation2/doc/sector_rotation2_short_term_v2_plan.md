# 板块轮动短期异动增强方案 v2

> 适用对象：`sector_rotation2` 短期（1~2 个交易日）异动研究增强。
>
> 定位：在不污染 `v1` 主评分、阶段、Lifecycle 与排名的前提下，提供独立的"当日/次日异动参考信号"，用于辅助板块轮动后续观察方向的研究筛选。不构成交易指令，不作为回测/调权依据。

## 1. 背景与目标

### 1.1 现有体系的盲区

当前 `v1` 模型（详见《板块轮动使用指南》第 4 节）核心特征窗口起步为 5 日：

- 收益与相对强度：`ret_5`、`ret_20`、`rs_5/20/60`、`distance_ma20/60`、`ma20_slope`；
- 趋势加速度：`rs20_accel`、`ma20_accel`（均为 5 日差分）、`macd_hist_delta`（唯一日级差分）；
- 量能与广度：`rvol_5_20`、`rvol_5_60`、`share_impulse`（20 日均值）、`breadth_up`、`breadth_above_ma20`、`breadth_new_high_20`、`breadth_rvol`；
- 阶段确认：`recent_raw.count(raw) >= 2`，显式 2 日迟滞。

因此在板块发生**1~2 日短期异动**时，`v1` 通常表现为：

- 综合排名、综合分当日变化有限；
- 阶段切换要等迟滞条件满足后才确认，**至少晚 1~2 日**；
- 现有的 `rank_change_1d` 与 `lifecycle_changed` 只能做"已显化"的相对位置确认，不能识别"刚刚启动"的脉冲。

在"AI 整体回调 + 其余板块方向不明"的横截面低区分度场景下，上述滞后更明显：候选阶段很难在 2 日窗口内重复出现，阶段持续时间拉长，排名抖动被误读为短期异动。

### 1.2 v2 的目标

在**不修改 `v1` 任何字段、口径与现有快照**的前提下，新增一个独立的短期异动参考层 `v2_short_term`，覆盖以下能力：

1. **日级原始特征**：1 日、2 日绝对收益与相对强度、当日量能脉冲、当日份额冲击。
2. **个股层面的短期广度**：5 日新高占比、5 日均线站上占比、当日强势股比例、涨停家数占比。
3. **短期复合评分**：以截面百分位标准化的日级评分，不参与 `v1` 主评分与排名。
4. **短期异动标签**：单日脉冲上涨 / 单日脉冲下跌 / 量能异动 / 涨停集群 / 极端涨跌 / 短期修复候选 / 短期恶化候选；标签不引入迟滞。
5. **独立快照与 API**：新模型版本 `v2_short_term`、独立 `config_hash`、独立快照表与查询接口；与 `v1` 数据互不污染。

### 1.3 v2 不做的事

- 不参与 `v1` 的 `composite_rank`、`composite_score`、`phase_confirmed`、`lifecycle_state`、`market_regime` 计算。
- 不为 `v1` 主评分提供权重依据；不与 `v1` 评分合并或叠加。
- 不在本文档范围内开展回测、IC 评估、样本外验证与权重调优；这些属于后续迭代方向。
- 不引入任何交易指令、个股/ETF 推荐或仓位建议。
- 不修改上游行情采集口径；所需字段均来自已存在的 `trade_sector_daily`、`trade_stock_daily_qfq`、`trade_stock_status`。

## 2. 设计原则

1. **完全解耦**：所有计算、存储、API 与前端展示均独立于 `v1`；`v2_short_term` 与 `v1` 共用同一份原始行情，但**不**读取、**不**写入 `v1` 快照。
2. **截面一致性**：所有评分沿用 `signed_percentile` 截面标准化，与 `v1` 在 `normalizers.py` 中的实现保持一致，但分数等级与权重独立配置。
3. **当日反应**：异动标签**不引入迟滞确认**（与 `v1` 的 2 日确认形成对照），但同时要求至少 2 项证据命中，避免单日噪声误报。
4. **数据可得性优先**：所有特征必须能由现有 `trade_sector_daily` 与 `trade_stock_daily_qfq` 表导出；板块层面没有 open/high/low 时，从个股聚合等价指标。
5. **可比可复现**：特征、评分、标签的参数（窗口、阈值、权重）集中放在 `ModelConfigShortTerm`，并写入 `config_hash`，确保同日同配置可复现。

## 3. 数据来源与字段边界

### 3.1 可直接复用字段

来自 `trade_sector_daily`（板块日行情）：

| 字段 | 用途 |
| --- | --- |
| `close_idx` | 板块收盘指数；用于 1/2 日收益与短期均线 |
| `total_amount` | 板块成交额；用于日级量能脉冲 |
| `rise_count` / `fall_count` / `flat_count` | 当日上涨/下跌/平盘家数；用于计算 `breadth_up` 与短期广度 |
| `limit_up` / `limit_down` | 涨停 / 跌停家数；用于极端异动标签 |
| `stock_count` / `kline_stock_count` | 覆盖率；保留 `coverage_ratio` 口径 |

来自 `trade_stock_daily_qfq`（个股日行情，需按 `trade_stock_status` 当前映射聚合）：

| 字段 | 用途 |
| --- | --- |
| `close_price` | 个股收盘价；用于 1/2 日强势股比例、5 日新高占比 |
| `amount` | 个股成交额；用于个股 RVOL 与放量比例 |
| `high_price` / `low_price` | 个股最高 / 最低价；用于计算振幅与 5 日新高占比 |
| `turnover_rate` | 个股换手率；可作为可选补充字段 |

### 3.2 数据不可得时的退路

| 期望字段 | 不可得时 | 退路 |
| --- | --- | --- |
| 板块 open/high/low | `trade_sector_daily` 不含 OHLC | 从个股 OHLC 等权聚合；但需在文档与报告中显式披露"由个股聚合" |
| 历史行业成分变更 | `trade_stock_status` 仅当前映射 | 使用 `current_mapping`；同 `v1`，需在文档显式披露 |
| 板块层面涨跌停占比 | 板块已有 limit_up/limit_down，但缺总家数 | 用 `rise_count + fall_count + flat_count` 作分母 |

## 4. 短期原始特征定义

所有时间窗口均为交易日；所有特征在 `sector_name` 维度上计算后写入 `sector_rotation_short_term_daily_snapshot`（详见第 6 节）。

### 4.1 收益与相对强度

| 字段 | 公式 | 含义 |
| --- | --- | --- |
| `ret_1` | `P_t / P_{t-1} - 1` | 单日绝对收益 |
| `ret_2` | `P_t / P_{t-2} - 1` | 两日累计绝对收益 |
| `ret_3` | `P_t / P_{t-3} - 1` | 三日累计绝对收益（用于平滑 1 日噪声） |
| `rs_1` | `板块 ret_1 - 市场基准 ret_1` | 单日相对强度 |
| `rs_2` | `板块 ret_2 - 市场基准 ret_2` | 两日累计相对强度 |
| `rs5_accel_1d` | `rs_5 - rs_5.shift(1)` | 5 日相对强度的 1 日变化（与 `v1` 的 `rs20_accel` 对照） |

### 4.2 量能与份额脉冲

| 字段 | 公式 | 含义 |
| --- | --- | --- |
| `rvol_1_20` | `amount_t / mean(amount_{t-19:t})` | 当日成交额相对 20 日均额的倍数 |
| `rvol_1_60` | `amount_t / mean(amount_{t-59:t})` | 当日成交额相对 60 日均额的倍数 |
| `amount_share_today` | `amount_t / sum(amount_t of eligible sectors)` | 当日板块在市场成交中的份额 |
| `share_impulse_1d` | `amount_share_today / amount_share_{t-1}` | 当日份额相对昨日的脉冲（>1 表示放量集中） |

### 4.3 个股层面短期广度

通过当前映射从 `trade_stock_daily_qfq` 聚合：

| 字段 | 公式 | 含义 |
| --- | --- | --- |
| `breadth_up` | 沿用 `v1` 既有定义 | 当日上涨家数占比 |
| `breadth_above_ma5` | `close_t > MA5(close)` 的个股占比 | 站上短期均线家数占比（比 `breadth_above_ma20` 更敏感） |
| `breadth_new_high_5` | `close_t == max(high_{t-4:t})` 的个股占比 | 5 日新高家数占比 |
| `breadth_strong_1d` | `ret_1 > 5%` 的个股占比 | 单日强势股比例 |
| `breadth_weak_1d` | `ret_1 < -5%` 的个股占比 | 单日弱势股比例 |
| `breadth_rvol_1d` | `amount_t / MA20(amount) > 1.5` 的个股占比 | 当日强势放量家数占比 |
| `limit_up_ratio` | `limit_up / (rise + fall + flat)` | 涨停家数占比 |
| `limit_down_ratio` | `limit_down / (rise + fall + flat)` | 跌停家数占比 |

### 4.4 个股振幅与一致性（可选）

| 字段 | 公式 | 含义 |
| --- | --- | --- |
| `intraday_range` | `(high - low) / close` 的板块等权均值 | 个股日内振幅板块均值 |
| `ret_dispersion` | 个股 `ret_1` 横截面标准差 | 个股表现一致性；高分散 + 高涨幅表"分化上涨" |

### 4.5 连续性轻量指标

| 字段 | 公式 | 含义 |
| --- | --- | --- |
| `streak_pos_ret` | 连续 `ret_1 > 0` 的天数（最多统计 5 日） | 短期连续上涨天数 |
| `streak_high_breadth` | 连续 `breadth_up > 0.5` 的天数（最多 5 日） | 短期连续广度健康 |
| `streak_top_limit_up` | 连续 `limit_up >= 1` 的天数（最多 5 日） | 短期连续出现涨停 |

> `streak_*` 上限为 5 是为了避免与 `v1` 的 5 日以上趋势信号语义重叠。

### 4.6 短期均线（用于广度对齐）

| 字段 | 公式 | 含义 |
| --- | --- | --- |
| `ma5` | 收盘 5 日均线 | 用于 `breadth_above_ma5` 与个股筛选 |
| `ma5_slope` | `ma5 - ma5.shift(1)` | 短期均线日级斜率 |

## 5. 短期评分与异动标签

### 5.1 短期评分族

对以下原始特征沿用 `v1` 的 `signed_percentile` 截面标准化方法，每项得到 `[-1, 1]` 的截面得分。**短期评分族不进入 `v1` 主评分与 `composite_rank`**。

| 评分 | 输入特征 | 含义 |
| --- | --- | --- |
| `pulse_score` | `rs_1`、`rs_2` | 短期相对强度脉冲 |
| `volume_spike_score` | `rvol_1_20`、`share_impulse_1d`（取对数后标准化） | 当日量能脉冲 |
| `breadth_spike_score` | `breadth_above_ma5`、`breadth_new_high_5`、`breadth_strong_1d`、`breadth_rvol_1d` | 短期广度脉冲 |
| `limit_score` | `limit_up_ratio`、`limit_down_ratio`（跌停取反向） | 涨跌停集群信号 |
| `momentum_shift_score` | `rs5_accel_1d`、`ma5_slope` | 短期趋势切换 |
| `short_term_composite` | 上述评分按 `ModelConfigShortTerm.short_term_weights` 加权合成 | 短期综合参考 |

`short_term_composite_rank` 仅在 `score_eligible=true` 的板块内做截面排名，**与 `composite_rank` 独立**。

### 5.2 短期异动标签（无迟滞）

标签规则采用**双证据最少命中**策略，避免单日噪声误报；阈值集中在 `ModelConfigShortTerm.short_term_thresholds`，运行期可调但不暴露给前端。

| 标签 | 触发条件 | 语义 |
| --- | --- | --- |
| `pulse_up` | `rs_1 ≥ pulse_up_rs_min` 且 `breadth_up ≥ pulse_up_breadth_min` | 单日强势脉冲上涨 |
| `pulse_down` | `rs_1 ≤ -pulse_up_rs_min` 且 `breadth_up ≤ 1 - pulse_up_breadth_min` | 单日强势脉冲下跌 |
| `volume_spike` | `rvol_1_20 ≥ volume_spike_min` 或 `share_impulse_1d ≥ share_impulse_min` | 当日显著放量 |
| `limit_cluster` | `limit_up ≥ limit_cluster_up_min` 且 `limit_down ≤ limit_cluster_down_max` | 涨停集群（情绪高涨） |
| `limit_panic` | `limit_down ≥ limit_panic_down_min` 且 `limit_up ≤ limit_panic_up_max` | 跌停集群（情绪恐慌） |
| `extreme_up` | `ret_1 ≥ extreme_move_up_min` | 单日极端上涨 |
| `extreme_down` | `ret_1 ≤ -extreme_move_up_min` | 单日极端下跌 |
| `short_rebound_candidate` | `rs_1 ≥ rebound_rs_min` 且 `rs_5 < 0` | 短期反弹候选（前 5 日弱势中突然转强） |
| `short_breakdown_candidate` | `rs_1 ≤ -rebound_rs_min` 且 `rs_5 > 0` | 短期走弱候选（前 5 日强势中突然转弱） |
| `inconclusive` | 未命中任何上述标签 | 当日无明显短期异动 |

> **不引入迟滞**：上述标签只看当日截面值；不做 2 日确认。原因：1~2 日异动本身要求"快"，迟滞会把脉冲信号抹平。

### 5.3 短期异动等级（可选）

为方便前端展示，可对命中的板块再做一个轻量"强度"标签：

| 等级 | 条件 |
| --- | --- |
| `intense` | `pulse_score ≥ 0.75` 且 `volume_spike_score ≥ 0.5`，或命中 `limit_cluster`/`limit_panic` |
| `moderate` | 仅命中 1 条主标签 |
| `mild` | 仅命中次级标签（如 `volume_spike`、`short_rebound_candidate`） |

等级本身不影响其他字段，只用于前端高亮。

## 6. 与 v1 的解耦边界

| 维度 | v1 | v2_short_term |
| --- | --- | --- |
| `model_version` | `v1` | `v2_short_term` |
| `config_hash` | `v1` 配置哈希 | `v2_short_term` 独立配置哈希 |
| 快照表 | `sector_rotation_sector_daily_snapshot` | 新建 `sector_rotation_short_term_daily_snapshot` |
| 运行审计 | `sector_rotation_run_log` 复用 | 同一表追加新行；`model_version` 区分 |
| 主评分 | `base_score`、`composite_score`、`composite_rank` | **不写入** `composite_rank`；提供 `short_term_composite_rank` |
| 阶段 | `phase_raw`/`phase_confirmed`/`phase_age` | **不读取不写入**；保留各自的阶段逻辑 |
| Lifecycle | `lifecycle_state` 等 | **不读取不写入**；保留各自版本 |
| 市场状态 | `market_regime`、`regime_multiplier` | 不参与；可单独定义短期市场环境（仅用于显示） |
| 评分归一化 | `signed_percentile` | 复用 `signed_percentile` 实现，权重独立 |
| 评分阈值 | `phase_enter_threshold`、`phase_hold_threshold` | 标签阈值集中在 `short_term_thresholds`，独立 |
| 数据契约 | 同 `v1` API | 新增 `GET /api/v1/sector-rotation/short-term-snapshot` |

> **强约束**：v2 任何字段都不得反向回填到 `v1` 快照或读取 `v1` 阶段的中间结果（如 `phase_age`、`velocity_score`）。

## 7. 数据契约与存储

### 7.1 新增快照表（建议命名）

```sql
CREATE TABLE IF NOT EXISTS sector_rotation_short_term_daily_snapshot (
    as_of_date DATE NOT NULL,
    sector_level TINYINT NOT NULL,
    sector_name VARCHAR(128) NOT NULL,
    model_version VARCHAR(32) NOT NULL,           -- 固定为 v2_short_term
    run_id CHAR(36) NOT NULL,
    coverage_ratio DECIMAL(18,8) NULL,
    -- 收益与相对强度
    ret_1 DECIMAL(18,8) NULL, ret_2 DECIMAL(18,8) NULL, ret_3 DECIMAL(18,8) NULL,
    rs_1 DECIMAL(18,8) NULL, rs_2 DECIMAL(18,8) NULL,
    rs5_accel_1d DECIMAL(18,8) NULL, ma5_slope DECIMAL(18,8) NULL,
    -- 量能与份额脉冲
    rvol_1_20 DECIMAL(18,8) NULL, rvol_1_60 DECIMAL(18,8) NULL,
    amount_share_today DECIMAL(18,8) NULL, share_impulse_1d DECIMAL(18,8) NULL,
    -- 个股广度
    breadth_up DECIMAL(18,8) NULL,
    breadth_above_ma5 DECIMAL(18,8) NULL, breadth_new_high_5 DECIMAL(18,8) NULL,
    breadth_strong_1d DECIMAL(18,8) NULL, breadth_weak_1d DECIMAL(18,8) NULL,
    breadth_rvol_1d DECIMAL(18,8) NULL,
    limit_up_ratio DECIMAL(18,8) NULL, limit_down_ratio DECIMAL(18,8) NULL,
    intraday_range DECIMAL(18,8) NULL, ret_dispersion DECIMAL(18,8) NULL,
    -- 连续性
    streak_pos_ret INT NULL, streak_high_breadth INT NULL, streak_top_limit_up INT NULL,
    -- 短期评分
    score_eligible TINYINT(1) NOT NULL DEFAULT 0,
    pulse_score DECIMAL(18,8) NULL, volume_spike_score DECIMAL(18,8) NULL,
    breadth_spike_score DECIMAL(18,8) NULL, limit_score DECIMAL(18,8) NULL,
    momentum_shift_score DECIMAL(18,8) NULL,
    short_term_composite DECIMAL(18,8) NULL, short_term_composite_rank INT NULL,
    -- 异动标签（可多值；用枚举字符串或位掩码存；本方案推荐字符串数组）
    short_term_labels VARCHAR(255) NULL,
    short_term_intensity ENUM('intense','moderate','mild','none') NOT NULL DEFAULT 'none',
    -- 质量
    eligible_member_count INT NULL, valid_member_count INT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (as_of_date, sector_level, sector_name, model_version),
    KEY idx_short_run_id (run_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='sector_rotation2 短期异动参考快照（v2_short_term）';
```

`short_term_labels` 推荐存为逗号分隔字符串，例如 `pulse_up,volume_spike`；解析与序列化由 Python 端负责。如未来标签数量增加或需做位运算，再迁移到位掩码表。

### 7.2 运行审计

`sector_rotation_run_log` 不变；新增一行 `model_version='v2_short_term'` 的运行记录；`config_hash` 来自 `ModelConfigShortTerm.config_hash`。

### 7.3 与 `v1` 快照的关系

- 同一 `as_of_date`、`sector_level`、`sector_name` 在两个快照表里各有自己的行；不互相覆盖。
- 前端可通过 `(as_of_date, sector_level, sector_name)` 在 API 层 join；如需服务端 join，新增 `/api/v1/sector-rotation/combined-snapshot`，但本期不强制要求。

## 8. 模块结构建议

新增独立模块 `src/morning_conference/sector_rotation2/short_term/`，避免与 `v1` 模块互相污染：

```
short_term/
├── __init__.py
├── config.py            # ModelConfigShortTerm（含阈值与权重）
├── features.py          # 短期原始特征计算
├── scoring.py           # 短期评分合成
├── labels.py            # 异动标签规则
├── snapshot_store.py    # 短期快照的读写
├── run_daily.py         # 每日运行编排
└── api/
    ├── repository.py
    ├── router.py
    └── schemas.py
```

`config.py` 提供与 `v1` 同等的 `config_hash(config)` 函数，确保同日同配置可复现。

## 9. API 接口设计

### 9.1 快照查询

```
GET /api/v1/sector-rotation/short-term-snapshot
    ?as_of_date=YYYY-MM-DD
    &level=1|2
    &model_version=v2_short_term
```

响应字段（与 `v1` 一致部分沿用既有命名，新增字段全部带 `short_term_` 前缀以避免冲突）：

```json
{
  "meta": {
    "as_of_date": "2026-08-12",
    "sector_level": 2,
    "model_version": "v2_short_term",
    "eligible_sector_count": 113,
    "pulse_up_count": 6,
    "volume_spike_count": 12,
    "limit_cluster_count": 2,
    "limit_panic_count": 1
  },
  "sectors": [
    {
      "sector_name": "示例行业",
      "score_eligible": true,
      "ret_1": 0.023, "ret_2": 0.041,
      "rs_1": 0.018, "rs_2": 0.030,
      "rvol_1_20": 1.85, "share_impulse_1d": 1.42,
      "breadth_up": 0.71, "breadth_above_ma5": 0.62,
      "breadth_new_high_5": 0.18, "breadth_strong_1d": 0.24,
      "breadth_rvol_1d": 0.33,
      "limit_up_ratio": 0.05, "limit_down_ratio": 0.0,
      "streak_pos_ret": 2,
      "pulse_score": 0.62, "volume_spike_score": 0.71,
      "breadth_spike_score": 0.55, "limit_score": 0.40,
      "momentum_shift_score": 0.48,
      "short_term_composite": 0.58,
      "short_term_composite_rank": 4,
      "short_term_labels": ["pulse_up","volume_spike"],
      "short_term_intensity": "intense"
    }
  ]
}
```

### 9.2 历史查询（参考用）

```
GET /api/v1/sector-rotation/short-term-history
    ?sector_names=...
    &start_date=YYYY-MM-DD
    &end_date=YYYY-MM-DD
    &level=1|2
    &model_version=v2_short_term
```

返回所选板块在区间内每日的 `ret_1`、`rs_1`、`rvol_1_20`、`pulse_score`、`short_term_labels` 等；不返回 `phase_*` 与 `lifecycle_*`（属于 `v1`）。

### 9.3 异动排行榜（用于"今日短期异动看板"）

```
GET /api/v1/sector-rotation/short-term-leaders
    ?as_of_date=YYYY-MM-DD
    &level=1|2
    &labels=pulse_up,volume_spike,limit_cluster,extreme_up
    &min_intensity=moderate
```

可选 `labels` 与 `min_intensity` 过滤；默认返回当日命中任何主标签的板块。

## 10. 前端可视化建议

### 10.1 新增"短期异动"页面（与主视图并列）

| 区块 | 数据 | 用户价值 |
| --- | --- | --- |
| 顶部 KPI | `pulse_up_count`、`volume_spike_count`、`limit_cluster_count`、`limit_panic_count` | 一眼看到当日短期异动密度 |
| 异动标签筛选 | `pulse_up`、`pulse_down`、`volume_spike`、`limit_cluster`、`limit_panic`、`extreme_up/down`、`short_rebound/breakdown_candidate` | 用户按需筛选关心的异动类型 |
| 异动榜单 | 按 `short_term_intensity` 与 `short_term_composite` 排序；展示触发标签、涨幅、相对强度、量能倍数 | 直接定位当日异动板块 |
| 强度气泡 | X 轴 `pulse_score`，Y 轴 `volume_spike_score`，大小 `breadth_spike_score`，颜色 `short_term_intensity` | 把 v1 的象限思想移植到短期维度 |
| 板块详情抽屉 | 当日全部原始特征、命中标签、`streak_*` 与 `v1` 主评分并列展示（**两套字段并列，不互相替换**） | 让用户能并排比较"短期异动 vs 中期趋势" |

### 10.2 在 v1 主视图增加"短期提示"侧栏

- 在 `SectorRanking` 旁边增加 `ShortTermHintPanel`：只展示当日 `short_term_intensity ∈ {intense, moderate}` 的板块，每行 1 个最关键的 `short_term_labels`；
- **点击跳转**到短期异动页面并预选该板块；**不得**修改主视图的 `composite_rank` 排序逻辑。

### 10.3 不复制 v1 视觉编码

- v1 的 `phase_confirmed` 颜色（青绿/琥珀/珊瑚/蓝紫/灰）只用于 `v1` 主视图；v2 用独立的"强度"配色（建议：intense=橙红、moderate=琥珀、mild=蓝绿、none=灰），并始终在 tooltip 写明"短期参考信号，不构成投资建议"。

## 11. 质量规则与边界

| 场景 | 处理 |
| --- | --- |
| 板块 `coverage_ratio < 0.80` | `score_eligible=false`；标签一律置 `inconclusive` |
| 个股有效样本 < 5 | `breadth_*` 全部置空，标签不命中 |
| 板块 `close_idx` 缺失或非正 | 该板块跳过；运行日志记录 `skip_reason=nonpositive_close` |
| `trade_stock_daily_qfq` 当日缺失 | 用最近有效交易日补齐（只补 1 日），并在日志中标注 `patched_member_count` |
| `amount_t` 缺失 | `rvol_*`、`share_impulse_1d`、`amount_share_today` 全部置空 |
| 1 日涨跌停家数同时为 0 | `limit_score = NaN`；避免人为把所有板块都打成中性 |
| 同一板块多标签命中 | `short_term_labels` 用逗号串接，排序按 §5.3 优先级 |
| 当日数据未回填 | API 返回 `SHORT_TERM_SNAPSHOT_NOT_FOUND`，前端展示"今日异动数据尚未生成" |
| 运行失败 | 沿用 `v1` 的 `sector_rotation_run_log.status=failed` 记录，不生成短期快照 |

## 12. 已知限制

| 限制 | 事实与影响 |
| --- | --- |
| 板块无 OHLC | 缺口/振幅类信号只能从个股聚合；与板块指数层面观察可能存在细微差异，需在报告中披露 |
| 不引入迟滞 | 标签对单日噪声更敏感；阈值需保守，必要时配合 `intensity=mild` 过滤 |
| 个股映射使用 `current_mapping` | 与 `v1` 同口径，存在历史回填偏差（详见指南第 11 节）；本方案不进行成分历史修正 |
| 不与 `v1` 主评分叠加 | 短期信号仅作"研究方向参考"，不能用于权重优化、组合构建或自动下单 |
| 不评估有效性 | 本文档不涉及 IC、Rank IC、分组收益、换手等指标；后续如需评估，必须用独立的样本外窗口（建议起步 1/2/3 日 horizon） |
| 与 Lifecycle 不联动 | `v2_short_term` 不会自动覆盖 `lifecycle_state`；如要联动，需另立规格 |
| 参数版本化但未跨阶段验证 | 所有阈值集中在 `ModelConfigShortTerm`，首次落地必须明确写出"v2_short_term 不进行 OOS 验证，仅做参数记录"的限制 |

## 13. 后续迭代方向（不在本期范围）

1. **引入板块日 K 线 OHLC 字段**：从上游扩展 `trade_sector_daily` 或新增 `trade_sector_kline_daily`，允许缺口/振幅类信号从板块层面直采。
2. **板块分时数据接入**：若后续引入日内分时，可计算"午盘异动""尾盘异动"等更精细的短期信号。
3. **与 v1 联动观察工具**：在两套字段都齐全的前提下，提供"v1 阶段 + v2 短期异动"的并列视图，**仅作研究展示，不参与评分**。
4. **样本外验证**：当积累 6~12 个月短期快照后，可独立评估 `pulse_score`、`volume_spike_score` 等与 1/2 日前瞻收益的 IC 与分组表现。
5. **事件标注**：接入新闻、研报、政策事件流，作为"短期异动"的旁证；本期不接入。
6. **个性化过滤**：未来允许用户订阅"仅看 `pulse_up + volume_spike`"等组合；但本期只暴露预设筛选。
7. **数据血统披露**：所有异动榜单需显示数据截至时间、模型版本、配置哈希与"非投资建议"提示。

## 14. 字段速查

| 字段 | 解释 |
| --- | --- |
| `ret_1` / `ret_2` / `ret_3` | 1/2/3 日绝对收益 |
| `rs_1` / `rs_2` | 1/2 日相对强度（vs 市场基准） |
| `rs5_accel_1d` | 5 日相对强度的 1 日变化 |
| `rvol_1_20` / `rvol_1_60` | 当日成交 / 20 或 60 日均额 |
| `amount_share_today` | 当日成交额在有效板块总和中的份额 |
| `share_impulse_1d` | 当日份额 / 昨日份额 |
| `breadth_up` | 当日上涨家数占比 |
| `breadth_above_ma5` | 站上 5 日均线家数占比 |
| `breadth_new_high_5` | 5 日新高家数占比 |
| `breadth_strong_1d` / `breadth_weak_1d` | 单日涨幅 >5% / <-5% 个股占比 |
| `breadth_rvol_1d` | 个股 RVOL > 1.5 的占比 |
| `limit_up_ratio` / `limit_down_ratio` | 涨跌停家数占有效家数比例 |
| `intraday_range` | 个股日内振幅的板块等权均值 |
| `ret_dispersion` | 个股 ret_1 的横截面标准差 |
| `streak_pos_ret` / `streak_high_breadth` / `streak_top_limit_up` | 短期连续性（最多 5 日） |
| `ma5_slope` | 5 日均线日级斜率 |
| `pulse_score` | rs_1/rs_2 截面评分 |
| `volume_spike_score` | rvol_1_20/share_impulse_1d 截面评分 |
| `breadth_spike_score` | 短期广度四指标截面评分 |
| `limit_score` | 涨跌停占比截面评分 |
| `momentum_shift_score` | rs5_accel_1d/ma5_slope 截面评分 |
| `short_term_composite` | 短期评分按权重合成 |
| `short_term_composite_rank` | 短期综合的截面名次 |
| `short_term_labels` | 命中标签集合（逗号分隔） |
| `short_term_intensity` | `intense` / `moderate` / `mild` / `none` |