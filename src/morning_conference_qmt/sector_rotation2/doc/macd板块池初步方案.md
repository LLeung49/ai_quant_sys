# MACD 板块池 — 板块轮动 v2 个人关注模块初步方案

> 文档定位:把 `src\pattern_detection\10-MACD全市场扫描选股.py` 的选股规则复用到 `sector_rotation2` 的 `run_daily`,并在板块轮动前端页面的"市场环境"组件下新增"个人关注"模块,把命中的股票 + 所属板块 + 二阶段可算指标一并展示。

---

## 1. 背景与目标

- 上游已有 `pattern_detection/10-MACD全市场扫描选股.py`,实现了 MACD 零轴上金叉 + 放量的全市场扫描,并把命中明细写到 `outputs/MACD动能趋势股票池_YYYY-MM-DD.csv`。但和 `sector_rotation2` 没有任何交集,也没有进入运行流程。
- `sector_rotation2` 当前只产出板块维度评分,没有"个股 × 板块"交叉输出,无法支撑用户做"板块下钻到个股"的决策。
- 用户需求文档 `pattern_detection/docs/user_demand/macd全市场扫描选股策略.txt` 给出五段策略(门槛/初筛/时机/风控/买入),本次先把**门槛**与**可算的初筛指标**纳入,时机/风控/买入后续单独迭代。

目标:

1. 把 MACD 第一步门槛筛选的纯函数抽取为可被 `run_daily` 调用的模块。
2. 把 `run_daily` 扩展成"板块打分 + MACD 个人关注扫描"双产物。
3. 通过新 API + 前端 "市场环境 → 个人关注" 模块,把当日命中个股、所属板块聚合、可算的二阶段指标呈现出来。
4. 数据缺失的指标(主力资金净流入 / 缠论第一买点)显式标记为 null,前端给出"待补字段"提示,不阻塞上线。

---

## 2. 数据可用性核查

通过查询 `information_schema.COLUMNS` 确认字段已存在:

| 指标 | 数据源 | 状态 |
| --- | --- | --- |
| ① ADX / RSI / KAMA / MA60 / Hurst | `trade_stock_daily` (OHLCV) | ✅ 可算 |
| ② 所属申万 2 级板块近 5 日涨幅 | `trade_stock_status.sector_2` × `trade_sector_daily` | ✅ 可算 |
| ③ 主力资金净流入 | **无对应表** | ❌ **需新增字段** |
| ④ 缠论可视化 / 第一买点 | 需要识别图,量化处理复杂 | ⚠️ 暂标记"人工判断" |

结论:除"主力资金净流入"外,其余指标全部可以从现有数据算出,无需新增字段。③ 在数据模型层保留列,持久化时写 NULL,前端写"待补数据源"提示;④ 列先不建,前端展示"待人工判断"。

---

## 3. 复用与扩展策略

把 `10-MACD全市场扫描选股.py` 的核心算法抽取为**纯函数模块** `src/morning_conference/sector_rotation2/macd_pool.py`:

- 复用 `data_ingestion.db_config.execute_query` 走只读 SQL,与 `data_loader.py` 同源,不引入新依赖。
- 保留 `talib.ADX / RSI / KAMA / SMA` 等调用,但每个函数只接 `numpy.ndarray`,方便单测与 mock。
- 拆出两个公开函数:
  - `step1_filter_macd_momentum_trend(df, **kwargs) -> (bool, dict)` — 与上游保持字节级一致的门槛筛选语义。
  - `step2_filter_trap_avoidance(df, **kwargs) -> dict` — 新增,封装 section 二的可算指标。
- 输出统一 dataclass `MacdPoolHit`(见 §5 schema)。

`run_daily` 调用方只需要:

```python
hits = run_personal_watchlist_scan(
    level=level,
    as_of_date=as_of_date,
    end_date=source_max_trade_date,
    enable_step2=True,
)
persist_personal_watchlist(hits, as_of_date, level, model_version, run_id)
```

---

## 4. 集成位置

**新表 `sector_rotation_personal_watchlist`** — 唯一键 `(as_of_date, sector_level, model_version, stock_code)`。

`run_daily.run_one_date` 流程扩展:

1. 步骤 1/7 ~ 7/7 — 保持原样(板块打分、生命周期、市场状态、快照落库)。
2. **新增步骤 8/7:个人关注扫描**
   - 数据源:复用 `load_sector_panel` 拉到的 `source_max_trade_date` 作为扫描基准日。
   - 加载范围:近 120 个交易日的 `trade_stock_daily`,复用 `10-MACD` 的批量 SQL(单次 `SELECT ... GROUP BY`)。
   - 计算:先跑 step1 门槛,命中后跑 step2 指标;全部转成 DataFrame。
   - 落库:upsert 到新表,**失败仅记录日志,不阻塞本次 run 的"成功"判定**。
   - 输出:不写 `outputs/MACD动能趋势股票池_*.csv`(避免和上游脚本重复输出),改由 API 端按需返回。

---

## 5. 新表 schema

```sql
CREATE TABLE IF NOT EXISTS sector_rotation_personal_watchlist (
    id BIGINT NOT NULL AUTO_INCREMENT,
    as_of_date DATE NOT NULL,
    sector_level TINYINT NOT NULL,
    model_version VARCHAR(32) NOT NULL,
    run_id CHAR(36) NOT NULL,
    stock_code VARCHAR(20) NOT NULL,
    stock_name VARCHAR(50),
    sector_1 VARCHAR(30),
    sector_2 VARCHAR(50),
    -- MACD 第一步门槛输出
    close DECIMAL(10,2),
    change_pct DECIMAL(8,2),
    dif DECIMAL(12,4),
    dea DECIMAL(12,4),
    macd_hist DECIMAL(12,4),
    vol_ratio DECIMAL(8,2),
    vol_ratio_gc DECIMAL(8,2),
    gc_offset TINYINT,
    gc_label VARCHAR(20),
    gc_dif DECIMAL(12,4),
    gc_dea DECIMAL(12,4),
    -- section 二 可算指标
    adx_14 DECIMAL(8,2),
    rsi_14 DECIMAL(8,2),
    hurst_60 DECIMAL(8,4),
    kama_efficiency DECIMAL(8,4),
    above_ma60 TINYINT(1),
    sector_2_5d_return DECIMAL(8,2),
    -- 待补字段
    main_capital_net_inflow_20d DECIMAL(20,2) NULL COMMENT ''主力资金 20 日净流入, 待补数据源',
    chan_first_buy TINYINT(1) NULL COMMENT '缠论第一买点, 需人工/视觉识别',
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uk_pw_date_level_code (as_of_date, sector_level, model_version, stock_code),
    KEY idx_pw_sector (sector_level, sector_1, sector_2),
    KEY idx_pw_run (run_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT 'MACD 板块池: 个股 + 板块映射 + 二阶段可算指标';
```

字段语义说明(全部 nullable,因为每条记录不一定所有指标都齐全):

- `adx_14` / `rsi_14` / `kama_efficiency`:最近一日的 ADX(14)/RSI(14)/KAMA 效率系数。
- `hurst_60`:用最近 60 个交易日收盘价做的简化 Hurst 指数(`np.log(R/S)/np.log(N)`)。
- `above_ma60`:最新一日 close > MA60 的 0/1。
- `sector_2_5d_return`:所属申万 2 级板块的近 5 日涨跌幅(来自 `trade_sector_daily`)。
- `main_capital_net_inflow_20d`:20 日主力资金净流入,**本次保持列存在但恒写 NULL**;等接入数据源后填实。
- `chan_first_buy`:缠论第一买点,**本次不计算**,保持 NULL。

---

## 6. 新 API

```
GET /api/v1/sector-rotation/personal-watchlist
    ?as_of_date=YYYY-MM-DD
    &level=1|2
    &model_version=v1
```

响应结构(对齐现有 `ResponseMeta` 风格):

```jsonc
{
  "as_of_date": "2026-08-12",
  "sector_level": 2,
  "model_version": "v1",
  "meta": {
    "run_status": "succeeded",
    "field_version": "v1",
    "source_max_trade_date": "2026-08-12",
    "strategy_name": "MACD 动能+趋势门槛 (零轴上金叉 + MA20×1.5 放量)",
    "scanned_count": 5247,
    "hit_count": 38,
    "scan_elapsed_seconds": 4.21
  },
  "sectors": [
    { "sector_1": "电子", "sector_2": "半导体", "hit_count": 6, "stock_codes": ["..."] }
  ],
  "stocks": [
    {
      "stock_code": "688256.SH",
      "stock_name": "寒武纪",
      "sector_1": "电子",
      "sector_2": "半导体",
      "close": 720.50,
      "change_pct": 6.12,
      "dif": 12.3456, "dea": 10.1234, "macd_hist": 2.2222,
      "vol_ratio": 2.34, "vol_ratio_gc": 1.89,
      "gc_label": "T-0 (最新日)",
      "adx_14": 32.5, "rsi_14": 67.4,
      "hurst_60": 0.71, "kama_efficiency": 0.86,
      "above_ma60": 1, "sector_2_5d_return": 3.45,
      "main_capital_net_inflow_20d": null,
      "chan_first_buy": null
    }
  ]
}
```

错误码:

- `WATCHLIST_NOT_FOUND`:当日无成功扫描数据 → 404。
- `INVALID_PARAMETER`:日期或层级非法 → 422。

---

## 7. 前端

`web/src/features/sector-rotation/summary/MarketSummary.tsx` 是当前"市场环境"卡片。在它下方新增同级组件 `PersonalWatchlistPanel.tsx`,被 `SectorRotationPage.tsx` 渲染在 `MarketSummary` 与象限图之间。

视觉:

- 顶部策略元信息条:`策略名 / 扫描家数 / 命中家数 / 耗时 / 扫描基准日`,沿用现有 `.summary-card` 风格。
- 命中板块聚合:横向 chip 列表,按命中家数降序,最多展示前 10 个,鼠标悬停显示该板块下命中的股票代码。
- 命中个股表格:列 `代码 / 名称 / 所属板块 / 涨跌幅 / 量比 / 金叉时点 / ADX / RSI / Hurst / KAMA / 股价>MA60 / 板块5日涨幅`。
- 待补字段列(主力资金净流入 / 缠论第一买点):空单元格显示浅色 `待补数据源` / `人工判断` 标签,不阻塞其它列阅读。
- 数据为空:`命中数 = 0` 时给出"今日无符合门槛的标的"的空态文案,不报错。

URL 状态:沿用 `workbench/urlState.ts` 的既有模式,`selectedDate` 直接驱动;`level` 与现有页面同步。

---

## 8. 测试计划

后端:

- `tests/test_sector_rotation2_macd_pool.py`:覆盖 `step1_filter_macd_momentum_trend` 与 `step2_filter_trap_avoidance` 的纯函数分支(金叉/未金叉、零轴上方/下方、量比达标/未达标、ADX/RSI/Hurst 边界、缺失数据降级)。
- `tests/test_sector_rotation2_personal_watchlist_store.py`:覆盖 `persist_personal_watchlist` 的 upsert 与 run 失败不影响板块落库。
- `tests/test_sector_rotation2_api_personal_watchlist.py`:覆盖 404 / 422 / 200 三种路径;校验 `meta` 字段语义与现有 `ResponseMeta` 对齐。

前端:

- `web/src/features/sector-rotation/summary/PersonalWatchlistPanel.test.tsx`:渲染命中列表、空态、待补字段三种 case。
- 在 `SectorRotationPage.integration.test.tsx` 增加"市场环境组件下出现个人关注模块"的回归断言。

---

## 9. 已知遗留与后续迭代

| 项 | 状态 | 下一步 |
| --- | --- | --- |
| 主力资金净流入(20 日) | 列已占位,写 NULL | 等接入数据源(tushare / akshare / 自建采集);接好之后改 step2 填实 |
| 缠论第一买点 | 未建模 | 短期由用户在前端人工判断;长期可接独立识别服务 |
| section 三(时机) / section 四(风控) / section 五(买入) | 本次未覆盖 | 后续按需迭代;`personal_watchlist` 表预留 `score_section3/4/5` 占位列 |
| 与板块打分结果的交叉视图 | 本次仅做并列展示 | 后续可加 "命中个股所在板块的 composite_rank",做交叉验证 |

---

## 10. 设计决策(请确认)

> 以下是开工前向用户提出的三个问题,默认按 A/A/A 推进。

1. **扫描结果保存方式**:A. 持久化到新表(推荐) / B. API 端按需算 / C. 前端实时算
2. **二阶段指标覆盖范围**:A. 能算的全算,缺的标 null(推荐) / B. 本次只做第一步 / C. 等数据齐再做
3. **建表 SQL 执行方**:A. 自动建表(推荐) / B. 我给 SQL 你手动建
