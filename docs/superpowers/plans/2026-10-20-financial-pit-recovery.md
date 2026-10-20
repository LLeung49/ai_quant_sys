# 财务 PIT 迁移与历史回补实施计划

**目标：** 用仍可用的 QMT 桥接归档 2015 年起缓存，并建立关闭桥接后可重放的文件导入；把合格 QMT 历史、AKShare 缺口/日常增量及 EPS/ROE 等指标统一纳入可审计的 PIT，回补股本与 Repair Alpha 后验收。

**设计：** [财务 PIT 迁移、历史回补与验收设计](../specs/2026-10-20-financial-pit-recovery-design.md)。当前市场/非财务日常链路独立。现有 worktree 包含未提交的迁移变更，执行任务时只暂存各任务自己的文件，不重置其他变更。

**桥接限制：** 当前 `/api/data/raw_financial_data` 映射输出只有按报表期组织的数值；没有公告/修订时间，Capital 只有 `total_capital`。本周桥接归档可补数值，历史 PIT 日期须由已有来源证据或独立披露源核对。下载时间只证明下载后可见。

**环境：** Python 3.13、pytest、PyMySQL/MySQL、AKShare、PowerShell。QMT 桥接是临时只读来源；文件归档和 AKShare 是可持续入口。

## 全局约束

- 正式财务表在隔离批次验收前不得被 QMT 桥接、原生文件解析器或 AKShare 直接覆盖。旧 QMT 脚本只作参考，不执行其宽表/PIT 双写。
- 不删除现有 QMT 或 AKShare 行，不批量重标 `data_source`，不把无效/缺失数值改为零。历史值和原始文件留有哈希与批次证据。
- 指标值必须携带实际可用日及来源/公式；只有财报核心字段匹配，不能推断宽表 EPS/ROE 在旧公告日已可用。
- 严格历史回测只使用在研究日之前有证据可得的版本。一个报告期在一次计算中只选一个版本，优先通过校验的 QMT，缺失时 AKShare。
- QMT 桥接关闭和 QMT 原生文件格式未确认不影响已归档 JSONL 文件的重放；原生文件解析必须依据实际样本实现与测试。
- 财务链路失败不得阻断已验收的行情/非财务每日任务，但不能发布部分财务结果或伪成功 Repair Alpha。

## 任务 1：冻结基线和报告期覆盖审计

**文件：** 新增 `src/data_ingestion/financial_recovery/audit.py`、`tests/data_ingestion/test_financial_recovery_audit.py`、`reports/financial-audit/baseline-20261020.json`。

**接口：** `audit_financial_baseline(query, *, as_of_date: date) -> dict` 输出每表按来源/报告期/股票覆盖、核心空值、公告日异常、宽表/PIT 五字段匹配与未匹配键、股本覆盖、重复版本。只读。

- [ ] 先写查询结果 fixture 测试：未匹配的 PIT 版本不得被判为可回填，合法零利润不得判为坏值；运行 `python -m pytest tests/data_ingestion/test_financial_recovery_audit.py -q`，确认因接口缺失而失败。
- [ ] 实现只读审计和 JSON 报告；执行同一测试至通过。再实际导出基线，核对 166,904/507 宽表、166,973+1/507 PIT、空股本和 193 个未匹配版本这些已知数值，差异记录原因。

## 任务 2：扩展 PIT 字段及版本/指标可用日期契约

**文件：** 新增 `sql/20261020_extend_financial_pit_metrics.sql`；修改 `src/morning_conference/sector_rotation2/research/financial/schema.py`、`providers/base.py`、`providers/database.py`；测试 `tests/research/test_financial_provider.py` 和新增 `tests/data_ingestion/test_financial_pit_schema.py`。

**接口：** PIT 新增 `original_announcement_date`、`metric_available_at`、`metric_lineage_json`，以及 `eps/roe/roa/gross_margin/net_margin/debt_ratio/current_ratio` 与可得的营业成本、负债合计、流动资产、流动负债。字段为可空；旧行默认未验证指标，不反向填充旧公告日。以迁移 SQL 的 `INFORMATION_SCHEMA` 检查保证重复执行幂等。

- [ ] 测试先覆盖字段读取、空字段兼容、比例单位/金额精度、重复迁移不报错；运行目标测试确认 RED。
- [ ] 增加 DDL、读取模型与必要索引；在测试库先执行迁移和 `SHOW COLUMNS`，再对生产库执行一次。执行前记录 DDL、表行数与可用空间，执行后再核对行数不变和原哈希/来源不变。

## 任务 3：统一归档格式、暂存和发布边界

**文件：** 新增 `src/data_ingestion/financial_recovery/archive.py`、`normalizer.py`、`store.py`、`sql/20261020_financial_recovery_batches.sql`；测试 `tests/data_ingestion/test_financial_recovery_archive.py`、`test_financial_recovery_store.py`。

**接口：** `FinancialArchiveV1` 包含 `batch_id`、源类型、股票、源表名、源原始字段、报告期、公告/更新原值、捕获时间、原始哈希；`stage_archive(path, batch_id) -> BatchAudit` 只写暂存；`publish_batch(batch_id) -> PublishResult` 仅发布通过校验的完整股票/报告期包。

- [ ] 先测重复导入幂等、同键不同哈希产生新版本、失败包不触及正式 PIT、事务回滚、空响应记为未知而非无财报；确认 RED。
- [ ] 实现带 manifest/checksum 的 JSONL 归档与暂存表。所有正式写入只能通过发布器；测试 GREEN 后用两个股票的样本验证归档重放得到相同哈希。

## 任务 4：QMT 桥接只读归档与离线文件导入

**文件：** 新增 `src/data_ingestion/financial_recovery/qmt_bridge_reader.py`、`file_importer.py`、`run_archive.py` 和相应测试。旧 `src/data_ingestion_qmt/2-财务数据采集_qmt_bridge.py` 不再作为执行入口。

**接口：** 桥接读取适配器将 Balance/Income/CashFlow/PershareIndex/Capital 原始记录转为 `FinancialArchiveV1`；命令支持 `--start 2015-01-01 --end <日期> --codes-file --batch-size --resume --output-dir`。`run_archive --input-manifest` 可在无桥接、无 `xtquant` 的环境重放同一归档。

- [ ] 桥接适配器测试要求不得调用生产 DB 写函数；`m_timetag` 不得映射为公告日，缺失的公告/修订字段写 `null`，`total_capital` 不能被误写为流通股本；字段缺失、超时、分页/截断、空股票、重试和断点续跑都形成明确失败清单。确认 RED 后实现。
- [ ] 用少量已缓存股票做端到端归档，核对源行数/日期/指标/文件哈希；然后按可测吞吐分批完成本周 QMT 缓存归档，批次日志保留。不得估算完成数量为成功数量。
- [ ] 用户下载的 QMT 原生文件到位后先取真实样本，识别格式、版本与日期字段，写解析 fixture 测试，再把解析器接至同一归档契约；无法证明时间字段时仅按实际捕获日使用，不伪造历史 `EXACT`。JSONL 归档重放可先独立验收。

## 任务 5：财报/指标/股本校验与定向回补

**文件：** 新增 `src/data_ingestion/financial_recovery/validate.py`、`reconcile.py`、`backfill.py`；修改 `akshare_financial_provider.py`、`akshare_financial_collection.py` 使新入口先进入暂存；新增 `tests/data_ingestion/test_financial_recovery_validate.py`、`test_financial_recovery_reconcile.py`。

**接口：** `validate_version(record, as_of_date) -> ValidationResult` 区分核心合格、指标历史可用、股本合格；`reconcile_periods(qmt, akshare, wide) -> RecoveryDecision` 逐股票/报告期选择 QMT、AKShare 或隔离，列出差异与字段缺口。

- [ ] 先测负利润合法、全核心空、非法日期、公告早于报告期、未来修订、股本负值、单位冲突、QMT 缺失时 AKShare 补位、字段冲突隔离；确认 RED 后实现。
- [ ] 宽表指标只在来源和五字段精确匹配时暂存；匹配的 166,781+507 行仍须有指标版次与可用日证据才可标为严格历史可用。193 个未匹配 QMT 行生成逐键核查表。
- [ ] 用 QMT 缓存优先回补历史数值；对同版本历史公告/修订日逐样本追溯原证据，没有证据则将指标可用日设为本次捕获日。股本若缺变动/公告日或流通股数，优先由可核对披露日期的来源补；失败/缺口清单再跑 AKShare 定向采集。任何一方失败均保留原值并产生可复跑清单。

## 任务 6：修改历史读取规则并核查指标口径

**文件：** 修改 `src/morning_conference/sector_rotation2/research/financial/pit.py`、`ttm.py`、`capital.py`、`providers/database.py`、`quality.py`；测试 `tests/research/test_financial_provider.py`、`test_financial_pit.py`、`test_financial_ttm.py`、`test_repair_pipeline_integration.py`。

**接口：** `resolve_latest_visible(rows, *, as_of_date, allow_estimated_pit=False)` 在同报告期只选一个当日可见且合格的版本：先版本可用日、同版本 QMT 优先、稳定哈希打平。指标读取独立检查 `metric_available_at`。`build_ttm` 对四个报告期各取一个版本。

- [ ] 先测同报告期 QMT/AKShare 并存、公告前不可见、后续修订不回溯、QMT 无效时 AKShare 取代、EPS/ROE 指标迟到、四季不重复、股本变更日与公告日分离；确认 RED 后实现。
- [ ] 解决当前 `EXACT` 与 `pit_exact` 存量状态的兼容映射，但不得把没有公告证据的行自动升级。对源报告 EPS/ROE 与基于原始字段/TTM 计算的口径加明确标记；复算前后 Repair Alpha 结果差异留痕。

## 任务 7：分批发布、回补财务衍生数据和 Web 验收

**文件：** 新增 `src/data_ingestion/financial_recovery/acceptance.py`、`reports/financial-audit/<批次>/` 报告、`scripts/monitor_financial_recovery.ps1`；按需要修改 `run_repair_daily.py` 调用入口。

- [ ] 小样本发布后运行数据库校验：异常日期、全核心空、重复被选版本、未来泄漏、股本非正/异常市值均为 0；记录 QMT/AKShare 选中数量、各字段覆盖和未解决清单。
- [ ] 逐批发布全量合格版本，每批记录前后行数、哈希、失败键和可回退批次。报告按年度、季度、股票上市时代、数据源分别展示覆盖；不得只给一个总行数。
- [ ] 对受影响交易日重算 Repair Alpha/估值 `backfill`，比较候选数、缺失股本标记、质量/估值字段；API TestClient 与 Web 工作台验证 `stock_repair` 及 summary 日期和数量。旧趋势股 `persistence` 规则问题仍作为独立遗留事项。

## 任务 8：AKShare 财务日常增量及宽表退役门槛

**文件：** 修改 `src/data_ingestion/run_daily_pipeline.py`、`akshare_financial_collection.py`、`scripts/run_daily_once.ps1` 或新增独立财务日常入口；测试 `tests/research/test_repair_pipeline_integration.py`、`tests/data_ingestion/test_akshare_financial_collection.py`。

- [ ] 先测实际披露选择失败、部分股票采集失败、股本失败、财务质量门失败时财务阶段返回非零且不发布不完整结果；确认 RED 后实现。
- [ ] 以 AKShare 运行一天真实增量并完成 PIT/Repair Alpha/API 验收；独立入口只在质量门通过后纳入每日任务。QMT 桥接配置和 `xtquant` 在日常环境不存在时仍可运行。
- [ ] 查明所有内部和外部宽表消费者。EPS/ROE 等 PIT 字段、历史读取、日常增量和回补均通过后，停止对 `trade_stock_financial` 双写；宽表保持只读归档并附回退说明，后续清理须再核对消费者。

## 每阶段的完成证据

- 完整测试命令：`$env:PYTHONPATH='src'; python -m pytest tests/data_ingestion tests/research -q`；再运行仓库全量 `python -m pytest -q`，记录失败名称，不把局部测试通过称为全量通过。
- 数据库验收：`financial_recovery.acceptance` 输出发布批次、来源/报告期/字段覆盖、非法/隔离数量、同日版本选择样本、QMT 优先/AKShare 补位样本、股本与估值样本；脚本结果非零则不标记完成。
- 运行验收：关闭 QMT 桥接后用归档文件重放成功，AKShare 日常增量成功，Repair Alpha/API/Web 当日与历史回补均可查看。所有真实缺口列明股票、报告期、字段、原因和下一步。

## 重点复核

1. 旧宽表的 166,781 行数值匹配并不能证明 EPS/ROE 当时可见；确保 `metric_available_at` 不提前。
2. 193 个不匹配 QMT PIT 不能被按报告期强制补入旧宽表值。
3. `EXACT` 与 `pit_exact` 大小写兼容不能绕过公告日证据。
4. QMT/AKShare 对同一报告期的值、修订和比率口径不同；TTM 只能选择一个历史可见版本。
5. 股本为空时不得伪造市值；AKShare 股本接口空响应、QMT 字段单位不明要留为缺口。
