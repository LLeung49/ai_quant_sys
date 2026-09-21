# QFQ 作为唯一前复权行情源：审计、换手率回填与下游迁移

## 目标与范围

`trade_stock_daily_qfq` 是系统唯一的前复权行情事实表。它由 QMT
ContextInfo Bridge 的 `front` 日线维护，并补齐 QMT 历史换手率。所有业务
下游改读此表；`trade_stock_daily` 停止写入和停止业务读取，仅保留为历史备份。

本变更包含：

1. 新增 raw/QFQ 内部完整性审计记录，区分真实故障和 QMT 原生复权差异；
2. 提供一次性、可恢复的 QFQ 换手率全量回填；
3. 删除新版 QMT 运行链路中旧表采集、旧表 K 线加载及旧/新表修复入口；
4. 将所有业务消费者切换到 QFQ，保留 raw 表只给需要交易事实的消费者。

不包含：删除物理旧表、改写原始数据供应商、以 AkShare 或当前流通股本推算换手率。

## 前复权数据契约

QMT `ContextInfo.get_market_data_ex(..., dividend_type='front')` 返回的 OHLC、
volume、amount 是 QFQ 的权威输入。QMT 的 `get_turnover_rate` 返回小数比例；
落库前乘以 100 并四舍五入四位，使 `0.001100...` 写为 `0.1101`（百分比）。

`turnover_rate` 仅在 QMT 对对应代码和日期有返回时写入。无值、非有限数值、QMT
调用失败或 AkShare 行情回退均保留 `NULL`，绝不使用当前流通股本倒推历史。

## 内部完整性审计

### 新表：`trade_qfq_integrity_audit`

该表与 `trade_price_reconcile_log` 分离。后者只比较旧
`trade_stock_daily` 和独立 QFQ，不能混入 raw/QFQ 同源验证。

| 字段 | 类型/约束 | 说明 |
|---|---|---|
| `id` | BIGINT 自增主键 | 审计记录标识 |
| `stock_code`, `trade_date` | 非空 | 异常定位；一条记录代表一个代码交易日 |
| `check_code` | VARCHAR(64) | `qfq_ohlc_non_affine`、`qfq_missing`、`raw_missing`、`invalid_ohlc` 等 |
| `severity` | ENUM(`warning`,`error`) | 影响程度 |
| `status` | ENUM | `qmt_verified_exception`、`repair_pending`、`repaired`、`failed`、`resolved` |
| `raw_ohlc_json`, `qfq_ohlc_json` | JSON | 发现时数据库或 QMT 的 OHLC 取证快照 |
| `source_fingerprint` | CHAR(64) | QMT raw/QFQ 响应的规范化 SHA-256 指纹 |
| `validator_version` | VARCHAR(32) | 规则版本，便于调整规则后追溯 |
| `first_detected_at`, `last_verified_at`, `resolved_at` | DATETIME | 异常生命周期 |
| `last_error`, `note` | VARCHAR/TEXT 可空 | 失败原因、人工说明 |

唯一键 `(stock_code, trade_date, check_code)`；每轮审计 UPSERT 同一异常，更新最新
快照、指纹和 `last_verified_at`，不制造重复日志。另建 `(status, severity,
last_verified_at)` 索引用于日常告警与待处理查询。

### 状态机与处理规则

1. 先进行本地硬校验：日期覆盖、可解析且有限的数值、OHLC 边界关系
   `low <= min(open, close) <= max(open, close) <= high`、非负 volume/amount。
   任何失败均为 `error/repair_pending`。
2. 若 raw/QFQ 出现缺日或本地历史与当前 QMT 同日期响应不一致，为
   `error/repair_pending`，执行既有全量重建；成功后记 `repaired`，仍失败记
   `failed` 并使任务非零退出。
3. `qfq_ohlc_non_affine` 不再直接视为数据错误。对该日期从 QMT 同时读取 raw 与
   front 响应：
   - QMT 响应与库内存储一致，且结构硬校验通过：记
     `warning/qmt_verified_exception`，不重建、不使任务失败；
   - QMT 响应不同：该差异可能是供应商历史修订，仍走 `repair_pending` 和全量重建；
   - QMT 验证失败：记 `error/failed`，保留原有数据，任务失败以便告警。
4. 以前的软异常在后续审计不再出现时，更新为 `resolved` 并设置
   `resolved_at`，不删除取证历史。

这保留全量 audit，同时避免 `300316.SZ` 等 QMT 原生结果在每日任务中无限重建。

## 全量换手率回填

新增临时 CLI 脚本至 `src/data_ingestion_qmt`，只处理
`trade_stock_daily_qfq.turnover_rate IS NULL`：

- 按代码和缺失窗口分组，固定小批次请求 QMT 历史换手率；
- 仅执行 `UPDATE ... SET turnover_rate=%s WHERE stock_code=%s AND
  trade_date=%s AND turnover_rate IS NULL`，因此可安全重跑；
- 提供 `--dry-run`、`--limit-codes`、`--start-date`、`--end-date`、
  `--batch-size`；输出请求、匹配、写入、缺失与失败统计；
- 不引入 AkShare 回退，也不修改 OHLC、volume、amount 或复权血缘；
- 脚本可中断；重启会继续扫描剩余 NULL 行，不需要单独的进度表。

日常 `8-原始行情与复权数据采集_qmt_bridge.py` 保持对新写入 QFQ/BFQ 行的换手率
合并；回填只补存量 QFQ NULL。

## 运行入口与下游迁移

### 废弃的 QMT 旧表路径

- `data_ingestion_qmt/1-行情数据采集_qmt_bridge.py`；
- `morning_conference_qmt/sector_rotation/stock_kline_loader_qmt_bridge.py`；
- `data_ingestion_qmt/9-前复权对账与定向重刷.py`；
- QMT sector rotation 初始化和每日入口中所有对应导入、参数、提示和文档。

`8-原始行情与复权数据采集_qmt_bridge.py` 是唯一日行情维护入口。板块指数
构建器已读 QFQ，无需 stock kline loader。

### 业务读取迁移

下列业务读取一律使用 `trade_stock_daily_qfq`：

- `pattern_detection` 的 K 线加载、形态雷达和 MACD 扫描；
- `morning_conference` 和 `morning_conference_qmt` 的 MACD、ETF 收益、估值、
  股票池与日期判断；
- `data_ingestion_qmt` 新闻、研报的股票代码池（`SELECT DISTINCT stock_code`）；
- 其他非 raw 语义的行情消费者。

`asset_allocation/etf_adaptive/market_data.py` 已经正确地区分 raw 交易事实表与
QFQ 价格表，不改其 raw 查询。旧表只可在未执行的历史归档工具中出现；任何可执行
脚本若仍写入或读取旧表，必须删除该路径或改为明确的废弃错误，避免误运行。

## 验收标准

1. 新表 DDL 可重复执行，状态 UPSERT 幂等；`300316.SZ` 被记录为
   `qmt_verified_exception`，不触发重建或日任务失败。
2. 缺日、非法 OHLC、QMT 当前结果与库不一致仍触发 `error` 与重建/告警。
3. 换手率回填 dry-run 不写库；实际运行仅填 NULL，QMT 值单位与新行写入一致。
4. `rg` 检查所有业务 Python 文件，不再有可运行的 `trade_stock_daily` 业务读写；
   允许值仅为 raw/QFQ/BFQ、旧表归档说明和不可执行 legacy 文本。
5. QMT 模块镜像、审计、回填和已受影响的下游测试全部通过。

