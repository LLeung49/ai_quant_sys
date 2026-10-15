# 运行时数据源迁移清单（2026-10-15）

本清单用于区分长期生产入口、一次性恢复入口、已禁用的历史代码和仍待迁移的依赖。历史行中的 `data_source` 值是审计证据，不做批量改名。

## 已迁移的长期入口

| 能力 | 当前入口 | 状态 |
| --- | --- | --- |
| 原始、前复权、后复权行情 | `src/data_ingestion/8-原始行情与复权数据采集.py` | 仅允许 AKShare；写入前拒绝零价、非有限值和不完整批次；失败返回非零状态 |
| 行情持久化 | `src/data_ingestion/price_projection_store.py` | 缺省血缘为 `akshare`；三张正式行情表使用固定白名单 |
| 申万行业分类 | `src/morning_conference/sector_rotation/industry_meta.py` | AKShare 二级行业目录与成分；完整拉取和校验后统一写库 |
| ETF 持仓日常刷新 | `src/morning_conference/sector_rotation2/research/etf_core/refresh_daily.py` | `auto` 和显式运行只选择 AKShare |
| 旧板块个股 K 线兼容读取 | `src/morning_conference/sector_rotation/stock_kline_loader.py` | 只读 `trade_stock_daily_qfq`；旧下载和写入入口已拒绝执行 |

## 一次性恢复专用

以下代码只服务批次 `market-full-qmt-20261014`，只能写 `_rebuild` staging 表：

- `src/data_ingestion/qmt_bootstrap_provider.py`
- `src/data_ingestion/run_market_rebuild.py`
- `src/data_ingestion_qmt/qmt_data_gateway.py` 及 QMT HTTP Bridge 服务

在整层重建、审计、原子切换、回滚观察期和下游回补完成前保留。完成后与 `src/data_ingestion_qmt/`、`src/morning_conference_qmt/` 和 `qmt-module-mirror` 工作树一并退役。

## 已禁用的历史参考代码

| 文件 | 约束 |
| --- | --- |
| `src/data_ingestion/1-行情数据采集.py` | 仅作历史参考；`main()` 在旧表写入前立即失败；正式行情入口是脚本 8 |
| `src/data_ingestion/9-前复权对账与定向重刷.py` | 旧 `trade_stock_daily` 修复入口已在 `main()` 拒绝执行 |
| `src/morning_conference/sector_rotation/stock_kline_loader.py` | 保留只读兼容接口；任何同步调用立即失败 |

## 尚待迁移或退役

| 能力 | 文件 | 剩余工作 |
| --- | --- | --- |
| 财务采集与 PIT | `src/data_ingestion/2-财务数据采集.py`、`run_daily_pipeline.py`、`research/financial/` | 用户正在补齐 QMT 财务缓存；完成后先审计现有数据，再实现 AKShare 采集、公告日校验和异常隔离。流水线阶段失败已能返回非零状态 |
| 公司行为 | `src/data_ingestion/price_corporate_actions.py` | 当前标准化和快照仍以 QMT 字段为准；需用 AKShare 股票/基金权益事件接口替换，并保留历史来源 |
| 公司行为消费者 | `src/asset_allocation/etf_adaptive/market_data.py`、`research/validation_provider.py` | 当前只筛选 `data_source='xtquant'`；生产切换前改为已验收的 AKShare 当前来源，历史回放不得把不同来源事件重复应用 |
| ETF 旧 provider | `src/morning_conference/sector_rotation2/research/etf_core/providers.py` | 日常入口已不选择 miniQMT；回滚观察期结束后删除 miniQMT provider、合并选择逻辑和对应测试 |

## 删除门槛

QMT/miniQMT 文件和工作树只有在以下条件全部满足后才能删除：

1. 6,958 个原始预期代码已完成或有可审计的排除证据；三张 staging 表通过零价、重复、非有限值、日期范围、行数和投影一致性审计。
2. AKShare 分层抽样完成；差异按已放宽的恢复口径记录，不能掩盖零价或结构性缺失。
3. 原子切换完成且正式表读检通过，旧表以 rollback 名称保留。
4. 财务、行业、ETF、板块和研究快照完成依赖顺序回补；Web/API 数据烟测通过。
5. 回滚观察期结束，且架构测试确认支持的运行入口在没有 QMT 配置和 `xtquant` 的环境中可启动。
