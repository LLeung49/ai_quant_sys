# Sector Rotation2 v1 基线报告

## 运行与数据口径

- 模型版本：`v1`
- 配置哈希：`<config_hash>`
- 数据截止日：`<source_max_trade_date>`
- 快照/标签历史范围：`<start_date>` 至 `<end_date>`
- 行业层级与板块数：`<sector_level>` / `<sector_count>`
- 低覆盖或不可评分板块数：`<skipped_sector_count>`
- 成员映射口径：`current_mapping`。历史回测未使用严格历史行业成分，结论须披露该限制。

## 研究结果

按 5 日、10 日分别填写：Pearson IC、Rank IC、ICIR、五分组收益、Top-Bottom、Top 组胜率、最大回撤、Top 组换手率，以及 risk_on/risk_off/range/high_volatility 分桶统计。

## 滚动样本外评估

使用 252 个交易日训练、63 个交易日验证、21 个交易日步长；只记录评估结果，不以本报告自动修改 v1 权重。

## 上线前人工核查

核查至少十个交易日，覆盖上涨、下跌和震荡市场；确认 phase 不改变排名、低覆盖板块不参与排名、bottoming_candidate 仅作为观察信号。

## 受控执行顺序

1. 经审批后由目标环境执行 `sql/20260804_create_sector_rotation_persistence_tables.sql`。
2. 使用 `run_daily --backfill-start/--backfill-end` 按交易日升序回填快照。
3. 使用 `run_backtest` 写入成熟标签并导出研究结果。
4. 填写本报告并由人工复核后，才允许讨论新模型版本或调权。
