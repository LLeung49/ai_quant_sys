# 基于收益暴露的 SW2 → ETF 映射设计

## 背景与目标

ETF 全持仓在 MiniQMT 中难以稳定、完整取得；AKShare 的定期披露大多只是前十大持仓，不能承担全市场 ETF 的完整持仓穿透。本设计以本地、可重放的日线收益建立正式的 SW2 → ETF Top3 映射；持仓数据降为可选验证证据，不再阻塞正式映射。

目标是在每个交易日为每个申万二级行业（SW2）输出最多三只境内股票型/指数型 ETF，并明确记录统计口径、置信度与风险状态。

## 数据边界

- SW2 基准：`trade_sector_daily`，限定 `sector_level=2`，使用 `close_idx`。
- ETF 收益：`trade_stock_daily`，使用 `close_price`。
- ETF 候选池：复用现有 ETF 代码识别、债券 ETF 排除逻辑，并按本地证券名称排除货币、商品、跨境等非权益产品。
- 仅使用本地已落库日线，不调用 AKShare/MiniQMT；因此日度和历史回填可重放。
- 日频收盘收益，滚动 60 个交易日；ETF 与 SW2 至少拥有 50 个共同交易日才可回归。

## 收益暴露计算

对每个共同样本充分的 `SW2 × ETF` 组合，使用简单日收益率计算：

```text
corr         = Corr(etf_return, sw2_return)
beta         = Cov(etf_return, sw2_return) / Var(sw2_return)
r_squared    = corr²
residual_vol = StdDev(etf_return - alpha - beta × sw2_return) × sqrt(252)

sector_fit_score =
  max(beta, 0) × max(corr, 0) × r_squared × 1 / (1 + residual_vol)
```

该误差是 ETF 相对 SW2 收益的拟合误差，不是、也不得标注为 ETF 相对法定跟踪基准的跟踪误差。

每个 SW2 按 `sector_fit_score DESC`、`r_squared DESC`、`etf_code ASC` 排序，持久化 Top3。

## 置信度与候选状态

- `qualified`：`beta > 0`、`corr > 0`、`r_squared >= 0.25`，并且共同样本数 `>= 50`。
- `low_confidence`：仍持久化其 SW2 Top3，但 ETF 候选强制为 `blocked`，并含风险标记 `low_return_exposure_confidence`。
- 样本不足、价格缺失或非权益 ETF：持久化可审计质量失败，不参与 Top3。
- 缺失持仓数据不会使收益映射失败。

## 持久化与迁移

在既有 `trade_sector_etf_map` 中新增收益映射的审计字段；使用独立的：

```text
mapping_type = return_exposure_derived
mapping_method = sw2_return_regression_v1
lookback_trading_days, window_start_date, window_end_date, sample_count
corr, beta, r_squared, residual_vol, sector_fit_score
confidence_status
price_source = local_trade_daily
price_as_of_date, universe_source
```

原 `exposure_derived` 与 `holdings_validation` 映射保留，只作审计和未来验证；不再是 ETF candidate runner 的输入。相同日期重跑以现有原子事件替换/有效区间重建机制处理，不产生重叠或重复。

ETF candidate runner 仅读取 `return_exposure_derived`。`qualified` 映射可继续通过执行证据与 MACD 门槛；`low_confidence` 映射始终 `blocked`。

## 新运行入口

新增独立 `refresh_return_mapping` 命令，在本地 `trade_sector_daily` 与 `trade_stock_daily` 都更新后运行。它加载本地价格、筛选 ETF 候选池、计算回归、原子持久化并汇总：行业数、候选 ETF 数、qualified、low_confidence、质量失败数。

原 `refresh_daily` 保留为持仓验证入口，不再承担正式映射职责。

## 验收标准

1. 本地数据充分时，131 个 SW2 各有最多三条 `return_exposure_derived` 映射。
2. 每条映射可查询窗口、样本数、Beta、相关性、R²、残差波动、分数、来源和公式版本。
3. 低置信度映射生成的候选必定为 `blocked`，不可能 READY。
4. 收益映射刷新不调用外部 ETF 持仓接口，不产生交易动作。
5. 同日重跑不产生映射重叠、重复候选或不可变快照冲突。
