# MACD 标的池使用指南

> 适用对象：`sector_rotation2` 新增的 MACD 标的池模块（默认模型版本 `v1`，默认层级 `level=2`）。
>
> 定位：这是一个按交易日运行的 **MACD 动能与趋势门槛筛选**工具，扫描 ETF、申万一级和申万二级板块；其结果独立于板块轮动 `v1` 主评分、阶段、Lifecycle 和排名，用于形成后续研究观察池，不构成交易指令或收益承诺。

## 1. 已完成能力与使用边界

当前模块已形成“日度扫描 → 全量指标留存 → 命中池落库 → API 查询 → 前端展示”的闭环：

1. 从 ETF 日行情与申万一级/二级板块日行情读取近端历史数据，计算 MACD、量比和趋势辅助指标。
2. 将全部扫描对象（包括未触发对象）写入 `sector_rotation_macd_entity_daily`，并以 `is_triggered` 标记当日是否满足入池规则。
3. 将当日命中对象写入 `sector_rotation_macd_pool`；该表是前端 MACD 标的池页和命中列表的唯一来源。
4. 对 ETF 自动同步可解析的名称到 `trade_stock_status`；债券、货币类 ETF 按规则排除。
5. 提供独立 API：命中池、可用日期和 ER/ADX 近端轨迹。
6. 前端提供独立的“MACD 标的池”工作区：趋势质量气泡图、ETF/申万一级/申万二级三类榜单，以及选中标的的近 5 日趋势质量轨迹。

本期边界如下：

- 仅扫描 `etf`、`sector_l1`、`sector_l2`；**不扫描个股**。
- 不参与 `composite_score`、`phase_*`、`lifecycle_*`，也不改变板块轮动主页面的排名或回测。
- 不与短期异动模块叠加计算；两个模块共用上游行情，但字段、阈值、存储和展示均独立。
- 不执行自动下单，不将金叉、趋势质量或榜单位置解释为确定性的涨跌预测。

## 2. 日度运行方式

后端入口为 `src/morning_conference/sector_rotation2/run_macd_daily.py`。

```bash
# 使用 trade_stock_daily 中的最近交易日，默认 level=2、model_version=v1
python -m morning_conference.sector_rotation2.run_macd_daily

# 指定交易日
python -m morning_conference.sector_rotation2.run_macd_daily --as-of-date 2026-08-13

# 指定板块层级或模型版本
python -m morning_conference.sector_rotation2.run_macd_daily \
  --as-of-date 2026-08-13 \
  --level 1 \
  --model-version v1
```

运行顺序：

1. 确认目标日期在 `trade_stock_daily` 中存在；非交易日会直接报错。
2. 幂等创建 `sector_rotation_macd_pool` 与 `sector_rotation_macd_entity_daily` 两张表。
3. 调用 `run_macd_daily_metrics(as_of_date)` 扫描 ETF、申万一级、申万二级的全部对象。
4. 同步 ETF 名称；仅命中对象进入 `sector_rotation_macd_pool`，全部对象写入 `sector_rotation_macd_entity_daily`。
5. 返回扫描数、命中持久化数、全量指标持久化数、ETF 名称同步数和按实体类型统计的命中数。

示例返回：

```python
{
  "as_of_date": "2026-08-13",
  "scanned_count": 1663,
  "persisted_count": 39,
  "metrics_persisted_count": 1663,
  "etf_names_synced": 12,
  "counts": {"etf": 28, "sector_l1": 0, "sector_l2": 11}
}
```

其中 `persisted_count` 是当日命中池的行数，`metrics_persisted_count` 是全量扫描对象的指标行数；它们不是同一个概念。

## 3. 当前入池规则

核心实现位于 `macd_pool.step1_filter_macd_momentum_trend`。MACD 采用：

- 快线 EMA：12 日；
- 慢线 EMA：26 日；
- DEA：DIF 的 9 日 EMA；
- 量比均线：20 日均量；
- 扫描窗口：从目标日向前取约 220 个自然日的数据，实际指标最多使用尾部 120 个交易日。

### 3.1 按实体类型的参数

| 实体类型 | 金叉回看 | 零轴要求 | 量比阈值 |
| --- | ---: | --- | ---: |
| `etf` | 最近 7 个交易日（含当日） | 要求最新日及金叉日 DIF、DEA 均大于 0 | 1.5 |
| `sector_l1` | 最近 7 个交易日（含当日） | 不要求零轴上方 | 0.8 |
| `sector_l2` | 最近 7 个交易日（含当日） | 不要求零轴上方 | 0.8 |

对象进入当日标的池必须同时满足：

1. **近期金叉**：在最近 7 个交易日中，存在某日 `DIF[i-1] <= DEA[i-1]` 且 `DIF[i] > DEA[i]`。
2. **ETF 零轴过滤**：ETF 除金叉外，还要求最新日和金叉日都满足 `DIF > 0`、`DEA > 0`；一级、二级板块不应用该限制，因此板块可能在零轴下方金叉后入池。
3. **放量过滤**：比较“目标日量比”和“金叉日量比”，只要两者中的较大值达到阈值即可：

   ```text
   max(当日成交量 / 当日20日均量, 金叉日成交量 / 金叉日20日均量) >= 阈值
   ```

4. **历史长度**：至少要有 35 个交易日（`slowperiod + signalperiod`），否则不触发。

`gc_offset=0` / `gc_label="T-0"` 表示当日新出现金叉；`T-1` 至 `T-6` 表示金叉发生在此前相应交易日。它只是“距金叉的交易日数”，不是持有期限或买卖建议。

### 3.2 ETF 排除规则

扫描 ETF 时先执行 `is_excluded_bond_etf`：

- 代码去掉交易所后缀后以 `511` 开头的 ETF 直接排除；
- 名称包含“债、国债、信用债、短融、货币、现金管理、同业存单”任一关键词时排除。

该规则用于剔除债券和货币类 ETF，避免其低波动、异常成交口径进入动能筛选。

## 4. 趋势辅助指标与阅读方式

命中与未命中的全量对象都会尽量计算二阶段辅助指标；该计算不改变是否入池。

| 字段 | 含义 | 阅读提示 |
| --- | --- | --- |
| `dif` / `dea` / `macd_hist` | 目标日 MACD 指标 | `macd_hist = DIF - DEA`；正值表示当日 DIF 在 DEA 上方，但不替代入池条件判断 |
| `vol_ratio` | 目标日量比 | 目标日成交量相对 20 日均量 |
| `vol_ratio_gc` | 金叉日量比 | 判断放量门槛时会与 `vol_ratio` 取较大值 |
| `gc_dif` / `gc_dea` | 金叉日 DIF / DEA | 用于复核当时是否满足金叉和 ETF 零轴条件 |
| `adx_14` | 14 日 ADX 趋势强度 | 样本不足时为 `null`；数值较高通常表示趋势性更强，但不区分涨跌方向 |
| `rsi_14` | 14 日 RSI | 只作强弱辅助，不是超买超卖交易规则 |
| `kama_efficiency` | 最近 11 日价格效率系数 | 接近 1 表示净位移相对路径更直接；接近 0 表示震荡、反复更明显 |
| `hurst_60` | 最近最多 60 日的简化 Hurst 指标 | 样本不足 20 日时为 `null`，仅作结构性辅助观察 |
| `above_ma60` | 最新收盘价是否高于 MA60 | 1=高于，0=不高于，样本不足为 `null` |

建议按以下顺序阅读：

1. 先确认 `gc_label`：优先识别是否为 `T-0` 新金叉，还是已发生数日的近期金叉。
2. 看 `vol_ratio` 和 `vol_ratio_gc`：确认是金叉日放量，还是后续继续放量。
3. 看 DIF、DEA、柱值：确认当前是否仍维持在金叉结构中；进入池并不保证之后不会死叉。
4. 用 ER（`kama_efficiency`）和 ADX 判断趋势质量，再结合 RSI、MA60 和量比做人工复核。

前端将 ER 与 ADX 组合成“趋势质量”图：横轴为 KAMA ER，纵轴为 ADX。ER 高且 ADX 高表示“强且高效”；ER 低、ADX 高可能意味着趋势强度存在但路径混乱；这是一种研究分区，不是收益分类。

## 5. 数据表、更新语义与数据质量

### 5.1 两张结果表

| 表 | 内容 | 主要用途 |
| --- | --- | --- |
| `sector_rotation_macd_pool` | 仅保存 `is_triggered=1` 的命中对象 | 前端池列表、当日命中复盘 |
| `sector_rotation_macd_entity_daily` | 保存所有被扫描对象，含 `is_triggered=0` | 轨迹查询、未命中原因复核、后续研究 |

两张表的唯一键均包含 `as_of_date`、`sector_level`、`model_version`、`entity_type` 与 `stock_code`。ETF 的 `stock_code` 是交易所代码（如 `510300.SH`），板块的 `stock_code` 与 `stock_name` 都是板块名称。

写入使用 `INSERT ... ON DUPLICATE KEY UPDATE`。因此：

- 同一交易日、同一层级、同一模型版本重复运行时，指标字段和 `run_id` 会被新一次运行结果覆盖；
- `entity_daily` 保留未命中对象，便于确认“指标存在但 `is_triggered=0`”；
- `pool` 只写命中对象，不会因为后一次扫描未命中而自动删除同日历史命中行。若需处理历史脏数据或旧口径数据，必须先确认具体 `run_id`、来源脚本和清理范围。

### 5.2 数据质量规则

- 目标日必须是 `trade_stock_daily` 中的交易日。
- 价格或成交量缺失会导致部分 MACD 或趋势辅助字段为 `null`，前端按“数据不足”处理。
- ADX 需更长暖机窗口；MA60、Hurst 等字段样本不足时不会被伪造为 0。
- `sector_2_5d_return`、`main_capital_net_inflow_20d`、`chan_first_buy` 当前仅为预留字段，尚未由本任务计算，前端和 API 中应按 `null` 阅读。
- `run_id` 是本次扫描唯一标识；排查同一日期的异常记录时，应优先使用 `run_id` 与指标值交叉核查，而不能仅按页面当前展示判断历史口径。

## 6. API 使用说明

API 位于 `src/morning_conference/sector_rotation2/api/macd_router.py`，在 `api/app.py` 的 `create_app()` 中注册，统一前缀为 `/api/v1/sector-rotation`。

### 6.1 查询命中池

```http
GET /api/v1/sector-rotation/macd-pool
```

参数：

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `as_of_date` | 不传时取池表中的最新日期 | 格式 `YYYY-MM-DD` |
| `level` | `2` | 仅支持 `1` 或 `2` |
| `model_version` | `v1` | 模型版本 |

响应会同时返回：

- `groups`：按 `etf`、`sector_l1`、`sector_l2` 分组的命中列表；
- `stocks`：同一批命中对象的平铺列表；
- `meta.hit_count`：当日命中总数；
- `meta.run_status`：固定为 `"succeeded"`（与首页 `ResponseMeta` 共用字段契约）；
- `meta.field_version`：固定为 `"v1"`（API 字段语义版本，不等同于 `model_version`）。

`meta` 中额外的 `run_status` / `field_version` 是公共响应契约的一部分，便于前端做版本判断与异常降级；不应仅依据是否返回来推断是否成功。

若指定日期无命中池数据，返回 `404 / MACD_POOL_NOT_FOUND`；日期格式不合法返回 `422 / INVALID_PARAMETER`。

### 6.2 查询可用日期

```http
GET /api/v1/sector-rotation/macd-pool-dates?level=2&model_version=v1
```

返回池表已有数据的日期，按降序排列：

```json
{ "dates": ["2026-08-13", "2026-08-12"] }
```

这是前端交易日历的可选日期来源；它表示该日池表存在数据，不代表所有交易日都运行完成。

### 6.3 查询 ER/ADX 轨迹

```http
GET /api/v1/sector-rotation/macd-pool-trajectory
```

必要参数：

| 参数 | 说明 |
| --- | --- |
| `as_of_date` | 截止交易日，格式 `YYYY-MM-DD` |
| `entity_type` | `etf`、`sector_l1` 或 `sector_l2` |
| `stock_code` | ETF 传交易所代码，板块传板块名称 |

可选参数：`level=2`、`model_version=v1`、`days=5`（范围 2~5）。

该端点直接查询 `sector_rotation_macd_entity_daily`，返回所选对象截至目标日的最近若干个 ER、ADX 点。因此它可以展示命中对象在近几日的趋势质量变化，而不仅是当日池表中的单点数据。

返回的实际点数受 `entity_daily` 覆盖度约束：如果目标日之前存在未运行的交易日、或者该对象当日未入池（`is_triggered=0`）但 `entity_daily` 已落库，仍会返回；返回点数可能少于 `days`，前端需要按"非空数组"而非"长度等于 `days`"来判断是否缺失数据。

## 7. 前端使用说明

前端入口在 `web/src/app/App.tsx`，顶部工作区切换为“板块轮动”和“MACD 标的池”；MACD 页面实现位于 `web/src/features/sector-rotation/MacdPoolPage.tsx`。

### 7.1 操作流程

1. 切换到“MACD 标的池”标签。
2. 在交易日历中选择日期。页面首次加载时会默认使用 `macd-pool-dates` 的最近日期。
3. 先看趋势质量气泡图：
   - 圆形=ETF，菱形=申万一级，三角形=申万二级；
   - 红色表示当日涨跌幅非负，绿色表示当日涨跌幅为负；
   - 气泡面积表示量比；
   - `T-0` 新金叉对象有额外高亮；距金叉越久，透明度越低。
4. 再看下方三类榜单。榜单内部按 `ADX × KAMA ER` 降序，只是展示优先级，不是策略评分或买入排序。
5. 点击某个对象，图上会高亮，并拉取最近 5 日 ER/ADX 轨迹。页面会给出“趋势强化、趋势走弱、效率先行 / Emerging、强度上升但变乱、结构迁移”之一的辅助文案。

### 7.2 空态与异常

- 当日 API 没有池表记录时，页面显示“该日期暂无 MACD 板块池数据”。
- 某一种实体类型无命中时，对应榜单显示“暂无命中”，不影响其它类别展示。
- ER 或 ADX 不足两个有效点时，轨迹状态显示“轨迹数据不足”。

## 8. 测试覆盖

当前测试包括：

| 层级 | 文件 | 已覆盖内容 |
| --- | --- | --- |
| 计算与存储 | `tests/test_sector_rotation2_macd_pool.py` | 短序列拒绝、二阶段暖机、平价序列效率系数、债券 ETF 排除、未触发对象仍保存指标、非交易日拒绝、ETF 名称同步 |
| API | `tests/test_sector_rotation2_macd_api.py` | 非法日期 422、空池 404、按实体类型分组的成功响应、轨迹端点读取全量 `entity_daily` 表 |
| 前端 | `web/src/features/sector-rotation/MacdPoolPage.test.tsx` | 三类分组渲染、请求失败空态、选中后趋势状态渲染 |

建议在改动 MACD 参数、表字段、API 响应或前端图形映射后，至少执行上述测试集与前端页面测试。

## 9. 核心限制与风险

| 限制 | 影响 |
| --- | --- |
| 板块不要求零轴上方 | 申万板块可以在零轴下方金叉后入池；“进入标的池”不等于趋势已确认向上 |
| 近期金叉允许 `T-0` 至 `T-6` | 标的可能在金叉后已经走出若干天，不能把池内全部标的理解成当日新信号 |
| 量比按当日与金叉日取最大值 | 后续缩量不必然使标的离开池；需要同时阅读两类量比字段 |
| 当前仅做筛选，不做有效性评估 | 模块未提供 IC、分组收益、换手、交易成本或样本外验证，不能据此判断策略收益能力 |
| 未接入资金流和缠论信号 | 预留字段当前为 `null`，不得推断为资金净流入或第一买点已确认 |
| 日度重跑会覆盖当日指标 | 回溯时需看 `run_id` 和数据来源；不同脚本或历史版本写入的数据不能混用 |
| ETF 通过前缀与名称关键字过滤 | 新品种命名异常时可能误包含或误排除，需定期检查关键词与代码规则 |

## 10. 后续迭代方向

1. 增加个股 `entity_type=stock` 的独立扫描口径，并明确与 ETF/板块参数的差异。
2. 接入并计算 `sector_2_5d_return`、主力资金净流入和缠论第一买点等预留字段。
3. 建立 MACD 命中后的 5/10/20 日样本外收益、分层和成本研究；参数调整必须使用新模型版本。
4. 对同日多次运行保留更完整的运行审计或历史版本，降低覆盖写入对排障和复盘的影响。
5. 提供“板块轮动阶段/Lifecycle 与 MACD 命中”并列研究视图，但保持其不参与主评分和自动化交易。
6. 增加可导出的 CSV/JSONL 结果，供离线复盘、模型研究和异常数据审计使用。

## 11. 常用字段速查

| 字段 | 解释 |
| --- | --- |
| `entity_type` | `etf`、`sector_l1`、`sector_l2` |
| `stock_code` / `stock_name` | ETF 为代码/名称；板块两者通常均为板块名称 |
| `close` / `change_pct` | 目标日收盘值和相对上一交易日涨跌幅 |
| `dif` / `dea` / `macd_hist` | 目标日 MACD 指标 |
| `vol_ratio` / `vol_ratio_gc` | 目标日量比 / 金叉日量比 |
| `gc_offset` / `gc_label` | 金叉距今天数 / 展示标签，例如 `0` / `T-0` |
| `gc_dif` / `gc_dea` | 金叉发生日的 DIF、DEA |
| `adx_14` / `rsi_14` / `hurst_60` / `kama_efficiency` / `above_ma60` | 趋势和结构辅助指标 |
| `is_triggered` | 仅在 `sector_rotation_macd_entity_daily` 中保存；1=入池，0=未入池 |
| `run_id` | 单次扫描 UUID；用于追踪和排查同日重复运行 |
| `sector_2_5d_return` / `main_capital_net_inflow_20d` / `chan_first_buy` | 当前预留字段，尚未填充，按 `null` 处理 |
