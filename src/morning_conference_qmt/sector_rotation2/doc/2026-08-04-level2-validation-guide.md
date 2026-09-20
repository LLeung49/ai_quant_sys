# Sector Rotation2 单日验证与断点 Review 指南

> 验证对象：`2026-08-04`、申万二级行业（`--level 2`）、模型版本 `v1`。
> 
> 目标：按“数据源 → 特征 → 市场状态 → 评分/phase → 落库 → 输出 → 标签与研究”的顺序，既验证业务口径，也理解代码的输入、处理和输出。首次仅运行单日；确认无误后再进入历史回填。

## 0. 验证原则与边界

- 本次运行会向四张已批准的 `sector_rotation_` 前缀表写入数据；不会改写 `trade_sector_daily`、`trade_stock_daily_qfq` 或 `trade_stock_status`。
- `2026-08-04` 的当日评分只用截至当日的数据；`phase_confirmed`、排名变化和 Top10 持续天数只读取 `2026-08-04` 以前的快照。首次运行没有历史快照时，这些历史字段为空或从初始状态开始，属于正常现象。
- 请先使用独立输出目录，避免与日常晨会输出混在一起，例如 `outputs\sector_rotation2_validation_20260804`。
- 任一步骤出现异常时，先保留终端完整错误和对应 SQL 查询结果，不要立即大范围回填或修改参数。

## 1. 运行前检查

### 1.1 确认代码版本与 Python 导入位置

在仓库根目录 `D:\aiQuant\ai_quant_sys` 执行：

```powershell
git log -1 --oneline
$env:PYTHONPATH = 'src'
python -c "import morning_conference.sector_rotation2 as m; print(m.__file__)"
```

验证标准：

- 最新提交应至少包含 DDL 注释提交 `e2a6c6b`。
- 输出路径应位于当前仓库的 `src\morning_conference\sector_rotation2`，不能指向旧版 `sector_rotation` 或其他 worktree。

### 1.2 确认四张派生表及核心字段

在 MySQL 执行：

```sql
SHOW TABLES LIKE 'sector_rotation_%';
SHOW CREATE TABLE sector_rotation_sector_daily_snapshot;
```

验证标准：

- 存在 `sector_rotation_run_log`、`sector_rotation_sector_daily_snapshot`、`sector_rotation_sector_forward_return`、`sector_rotation_backtest_metric`。
- 快照表至少包含 `rs_20`、`velocity_score`、`base_score`、`phase_confirmed`、`market_regime`、`rank_change_1d` 等字段。
- 表和字段应能看到中文 `COMMENT`；字符集为 `utf8mb4`。

### 1.3 检查上游 2026-08-04 数据完整性

```sql
SELECT sector_level, COUNT(*) AS row_count, COUNT(DISTINCT sector_name) AS sector_count,
       MIN(trade_date) AS min_date, MAX(trade_date) AS max_date
FROM trade_sector_daily
WHERE sector_level = 2 AND trade_date <= '2026-08-04'
GROUP BY sector_level;

SELECT trade_date, COUNT(*) AS row_count, SUM(total_amount) AS total_amount
FROM trade_sector_daily
WHERE sector_level = 2 AND trade_date = '2026-08-04'
GROUP BY trade_date;

SELECT COUNT(*) AS stock_daily_count
FROM trade_stock_daily_qfq
WHERE trade_date = '2026-08-04';
```

验证标准：

- 二级行业的最大交易日为 `2026-08-04`，且当日有多个板块。
- 每个拟参与板块应至少有 90 个有效交易日；不足者应在后续质量输出中体现，而不是静默进入排名。
- 个股日线数据不应为空，否则个股 RVOL/广度相关指标会缺失。

## 2. 推荐断点与调用链

使用 PyCharm 或 VS Code 以仓库根目录为工作目录，环境变量设置为 `PYTHONPATH=src`。建议按以下顺序设置断点：

| 顺序  | 文件 / 方法                                          | 要观察的变量                                     | 业务验证点                                                     |
| --- | ------------------------------------------------ | ------------------------------------------ | --------------------------------------------------------- |
| 1   | `run_daily.py / run_one_date`                    | `level`、`as_of_date`、`run_id`              | 本次确实是 level=2、日期为 2026-08-04，且运行 ID 唯一。                   |
| 2   | `data_loader.py / load_sector_panel`             | 每个板块的行数、`close`、`amount`                   | 只读取上游数据；日期升序，无重复日期、负成交额或非正收盘价。                            |
| 3   | `data_loader.py / build_market_benchmark`        | `normalized`、输出 `close/amount`             | 每个板块先除以自身首日收盘价，再等权平均为市场价格基准；成交额为各板块求和。                    |
| 4   | `sector_features.py / build_daily_feature_panel` | 单板块 feature 行                              | 核对 RS、均线距离、RVOL、份额冲量与广度是否符合人工计算。                          |
| 5   | `market_regime.py / classify_market_regime`      | `ma20`、`ma60`、广度、限涨跌、结果                    | 按 `risk_off → high_volatility → risk_on → range` 的优先顺序判断。 |
| 6   | `scoring.py / score_feature_panel`               | 四类 `*_score`、`base_score`、`composite_rank` | 分数为横截面标准化；排名按 `base_score`，不能由 phase 改变。                  |
| 7   | `scoring.py / apply_phase_history`               | `phase_raw`、`phase_confirmed`、`phase_age`  | 新状态遵循进入/保持迟滞和三日两次确认；首次运行通常无历史确认。                          |
| 8   | `snapshot_store.py / persist_daily_snapshot`     | `rows`、SQL、受影响行数                           | 所有值参数化写入；唯一键重跑时 upsert，不重复插入。                             |
| 9   | `report.py / write_daily_reports`                | `final`、输出文件路径                             | 仅在快照成功提交后生成文件。                                            |

## 3. 执行单日计算

### 3.1 执行命令

```powershell
Set-Location D:\aiQuant\ai_quant_sys
$env:PYTHONPATH = 'src'
python -m morning_conference.sector_rotation2.run_daily `
  --level 2 `
  --as-of-date 2026-08-04 `
  --model-version v1 `
  --output outputs\sector_rotation2_validation_20260804
```

`python -m morning_conference.sector_rotation2.run_daily  --level 2  --as-of-date 2026-08-05  --model-version v1  --output outputs\sector_rotation2_validation_20260805`

验证标准：

- 进程以退出码 `0` 结束。
- 未出现对旧包 `morning_conference.sector_rotation` 的导入。
- 运行失败时，`sector_rotation_run_log` 中应有 `failed` 状态和错误摘要；不应生成成功口径的 CSV/TopN 文件。

### 3.2 检查运行审计

```sql
SELECT run_id, as_of_date, sector_level, model_version, status,
       eligible_sector_count, skipped_sector_count, error_summary,
       started_at, finished_at
FROM sector_rotation_run_log
WHERE as_of_date = '2026-08-04' AND sector_level = 2
ORDER BY started_at DESC;
```

验证标准：

- 最新记录为 `succeeded`。
- `eligible_sector_count + skipped_sector_count` 等于本次处理板块数。
- `config_hash` 固定，可用于后续重现该次结果。

## 4. 验证特征、评分与状态快照

### 4.1 总体分布检查

```sql
SELECT COUNT(*) AS total_count,
       SUM(score_eligible = 1) AS eligible_count,
       SUM(score_eligible = 0) AS ineligible_count,
       MIN(base_score) AS min_base_score,
       MAX(base_score) AS max_base_score,
       MIN(composite_rank) AS min_rank,
       MAX(composite_rank) AS max_rank
FROM sector_rotation_sector_daily_snapshot
WHERE as_of_date = '2026-08-04' AND sector_level = 2 AND model_version = 'v1';
```

验证标准：

- `composite_rank` 仅对 `score_eligible=1` 的行非空。
- 有效板块的名次从 1 开始，与有效数量一致；并列时当前实现使用最小名次，需留意是否存在间断名次。
- `base_score`、各 `*_score` 应在合理的横截面范围内，极端值需回到原始特征核对，不应直接调权。

### 4.2 抽样核对 Top 10 与末尾板块

```sql
SELECT sector_name, coverage_ratio, rs_5, rs_20, rs_60,
       distance_ma20, distance_ma60, rvol_5_20, share_impulse,
       breadth_up, trend_level_score, velocity_score, acceleration_score,
       participation_score, base_score, composite_score, composite_rank,
       phase_raw, phase_confirmed, phase_confidence, market_regime
FROM sector_rotation_sector_daily_snapshot
WHERE as_of_date = '2026-08-04' AND sector_level = 2 AND model_version = 'v1'
ORDER BY composite_rank ASC
LIMIT 10;
```

再将排序改为 `ORDER BY composite_rank DESC`，抽样核对末尾有效板块；并额外查询 `score_eligible=0` 的板块。

验证问题：

1. Top 板块是否同时具备较高的趋势位置、速度或参与度，而非仅由单一异常成交额主导？
2. `base_score` 是否是可用四类主评分按权重重归一的结果？`volume_score` 是诊断维度，不进入 v1 的 `base_score`。
3. `phase` 是否只作解释标签，未改变 `composite_rank`？相同 `base_score` 排序下应保持一致。
4. `coverage_ratio < 0.80` 或证据不足的板块是否未参与排名？

### 4.3 人工复算一只板块的关键口径

选取 Top 10 中一只板块，记为 `<sector_name>`：

```sql
SELECT trade_date, close_idx, total_amount, rise_count, fall_count, flat_count,
       limit_up, limit_down, stock_count, kline_stock_count
FROM trade_sector_daily
WHERE sector_level = 2 AND sector_name = '<sector_name>'
  AND trade_date <= '2026-08-04'
ORDER BY trade_date DESC
LIMIT 90;
```

重点复算：

- `RS20 = 板块 20 日收益 - 市场基准 20 日收益`；市场基准是全部有效板块归一后等权价格序列。
- `distance_ma20 = close / MA20 - 1`；MA20 只使用截至当日的 20 个交易日。
- `rvol_5_20 = 近 5 日成交额均值 / 近 20 日成交额均值`。
- `breadth_up = rise_count / (rise_count + fall_count + flat_count)`。

复算允许有显示精度误差，但不能存在未来日期或自然日替代交易日。

## 5. 验证输出文件

```powershell
Get-ChildItem outputs\sector_rotation2_validation_20260804
Import-Csv outputs\sector_rotation2_validation_20260804\sector_rotation2_daily_2026-08-04.csv | Select-Object -First 5
Get-Content outputs\sector_rotation2_validation_20260804\sector_rotation2_topN_2026-08-04.txt
Import-Csv outputs\sector_rotation2_validation_20260804\sector_rotation2_data_quality_2026-08-04.csv | Select-Object -First 10
```

验证标准：

- 仅在数据库快照成功后存在三个文件。
- daily CSV 的排名与快照表一致；TopN 文本与 CSV 前 N 名一致。
- 数据质量 CSV 明确列出 `coverage_ratio`、可评分标记和缺失特征数量，便于解释被跳过的板块。

## 6. 首次单日验证后的下一步

首次单日验证通过后，不要立即全量回填。建议先选连续 5 至 10 个交易日回填：

```powershell
python -m morning_conference.sector_rotation2.run_daily `
  --level 2 `
  --backfill-start <起始交易日> `
  --backfill-end 2026-08-04 `
  --model-version v1 `
  --output outputs\sector_rotation2_validation_backfill
```

重点验证 `phase_confirmed`、`phase_age`、`rank_change_1d`、`rank_change_5d` 与 `top10_days_20` 是否只依赖此前快照。确认后才可扩大回填区间，并运行 `run_backtest` 生成成熟的 5/10 日收益标签和研究结果。

## 7. 问题记录模板

每发现一个问题，建议记录：运行 `run_id`、板块名、交易日、字段名、当前值、人工复算值、预期口径、对应断点/SQL、是否可复现。不要仅依据单个收益表现调整 v1 权重或 phase 阈值。
