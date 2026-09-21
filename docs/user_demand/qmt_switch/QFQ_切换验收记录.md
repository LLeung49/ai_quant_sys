# QFQ 数据源切换验收记录

验收日期：2026-09-22

## 已部署的数据库变更

- 已执行 `sql/2026-09-21-qfq-integrity-audit.sql`；`trade_qfq_integrity_audit`
  可被数据库查询到。
- 该表与旧的 `trade_price_reconcile_log` 分离，用于记录 raw/QFQ 同源校验。

## 换手率回填

回填程序：`src/data_ingestion_qmt/10-QFQ换手率全量回填_qmt.py`。

| 阶段 | 结果 |
|---|---|
| 20 代码 dry-run | `requested=56822`、`matched=8371`、`written=0`、`missing=48451`、`failed=5` |
| 全量运行 | 于 2026-09-21 启动，后台进程已退出；其标准输出未被宿主保留，不能补报运行期的批次数或失败数 |
| 运行后表统计 | 总行数 `14,415,635`；非 NULL `137,992`；NULL `14,277,643` |
| 审计状态 | `trade_qfq_integrity_audit` 当前无记录 |

`turnover_rate` 只会在 QMT 返回对应代码和日期时写入；剩余 NULL 不以当前流通股本或 AkShare 推算。回填 SQL 附带 `AND turnover_rate IS NULL`，可安全重跑，只会尝试余下 NULL 行。

## 运行入口和消费者

- 唯一日行情维护入口：`8-原始行情与复权数据采集_qmt_bridge.py`；它维护 raw、QFQ、BFQ 三张独立事实表。
- QMT 旧日线采集、旧 K 线加载和旧/新对账重刷入口均已退役。
- pattern_detection、morning_conference、data_ingestion 的业务前复权读取均已切换至 `trade_stock_daily_qfq`。
- `asset_allocation/etf_adaptive/market_data.py` 保留 raw 交易事实读取，同时使用 QFQ 进行复权价格分析。

## 已知限制

- 项目全量 pytest 仍会受历史 `reports/pytest-temp/*` 和 `tmp_data/*` 的权限错误影响；本次使用受影响模块的定向测试验收。
- 后台全量回填的细分 QMT 失败/未匹配日志未持久化；后续安全重跑时应将控制台汇总另存为运行证据。
