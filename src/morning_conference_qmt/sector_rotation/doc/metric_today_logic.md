# 板块轮动 · 当日指标监控 · 计算逻辑说明

> 本文档对应 `src/morning_conference/sector_rotation/` 模块（21-CASE-B）：
> 从已落库的板块 K 线 → 派生一/二阶导 → 强度打分 → 四象限分类 → 综合排名。
> 主要入口脚本：`3-run_metric_today.py`。

---

## 1. 架构总览

模块自下而上分四层，每层有清晰输入输出，方便微调与可视化替换：

```
┌────────────────────────────────────────────────────────────────┐
│ Layer 1: 数据底座  (sector_index_builder.py + sector_loader.py) │
│   trade_stock_daily_qfq / trade_stock_status / trade_sector_daily│
│   → load_all_sectors()  →  {sector_name: OHLCV DataFrame}        │
└────────────────────────────────────────────────────────────────┘
                              ↓
┌────────────────────────────────────────────────────────────────┐
│ Layer 2: 导数层    (derivatives.py)                              │
│   给定一条 close 序列 → 一阶导 (ROC_20, MA20_SLOPE)             │
│                       → 二阶导 (MACD_HIST, MA20_ACCEL, ROC_ACCEL)│
└────────────────────────────────────────────────────────────────┘
                  ↓                              ↓
┌────────────────────────────┐  ┌─────────────────────────────────┐
│ Layer 3a: 强度打分         │  │ Layer 3b: 拐点检测              │
│ industry_strength.py       │  │ inflection_detector.py          │
│ → 3 个静态指标             │  │ → 一阶/二阶投票 → phase 5 分类  │
│ → Z-score 等权 → score    │  │   (accel_up/decel_up/           │
│ → rank                    │  │    accel_down/decel_down/       │
│                            │  │    neutral)                     │
└────────────────────────────┘  └─────────────────────────────────┘
                  ↓                              ↓
┌────────────────────────────────────────────────────────────────┐
│ Layer 4: 综合视图  (3-run_metric_today.py)                       │
│   composite_score = strength_score + PHASE_BONUS[phase]        │
│   落盘 4 个文件: combined/strength/phase CSV + TopN txt          │
└────────────────────────────────────────────────────────────────┘
```

---

## 2. 数据依赖

| 来源 | 用途 | 落库脚本 |
|---|---|---|
| `trade_stock_daily_qfq` | 股票日 K（前复权），CASE-A 增量下载 | `2-run_data_daily.py` |
| `trade_stock_status` | 申万一/二级成分股映射 | `1-run_init.py` (`industry_meta`) |
| `trade_sector_daily` | 板块等权合成 OHLCV + 涨跌统计 | `sector_index_builder.rebuild_all_sectors` |
| `build_market_benchmark` | 用全部板块等权代理「全市场基准」（基准归一化到 1000） | `sector_loader.build_market_benchmark` |

**关键过滤**：`load_all_sectors(..., min_days=60)` 会剔除历史 < 60 交易日的板块（数据不足无法算 ROC_20 / MA20_SLOPE）。

---

## 3. 全部计算指标罗列

### 3.1 强度类（Level 横截面，3 个）

输入：单板块 close / amount + 市场基准 close。

| 指标 | 公式 | 含义 | 阈值 |
|---|---|---|---|
| **MOM_21** | `close[-1] / close[-22] - 1` | 21 日累计收益（≈ 1 个月动量） | 无 |
| **RS_60** | `(close[-1]/close[-61] - 1) - (bench[-1]/bench[-61] - 1)` | 60 日板块超额收益（跑赢基准多少） | 无 |
| **VOL_RATIO** | `amount[-5:].mean() / amount[-60:].mean()` | 近 5 日量能 / 近 60 日均量（>1 即放量） | 分母为 0 时返回 NaN |

> 数据最少需要 **70** 个交易日才能完整算 3 个指标（代码 `industry_strength.py:58-64`）。

### 3.2 速度类（一阶导，2 个）

输入：单板块 close 序列。

| 指标 | 公式 | 含义 |
|---|---|---|
| **ROC_20** | `pct_change(20) = (close_t / close_{t-20}) - 1` | 20 日变化率，一阶导离散近似 |
| **MA20_SLOPE** | 对 `MA(close, 20)` 在 10 日窗口做最小二乘回归，年化为 **%/年**（×252/MA） | MA20 斜率的年化百分比 |

> **MA20_SLOPE 年化公式**：  
> `slope = cov(x,y) / var(x)`，`annual_pct = slope * 252 / |y_mean| * 100`

### 3.3 加速度类（二阶导，3 个）

| 指标 | 公式 | 含义 |
|---|---|---|
| **MACD_HIST** | `(DIF - DEA) * 2`，其中 `DIF=EMA12-EMA26`，`DEA=EMA(DIF,9)` | 速度差的二阶导代理（通达信 ×2 约定） |
| **MA20_ACCEL** | `MA20_SLOPE - MA20_SLOPE.shift(5)` | 斜率变化，**真正的二阶导**（5 日差） |
| **ROC_ACCEL** | `ROC_20 - ROC_20.shift(5)` | ROC 的 5 日变化 |

> HIST、ACCEL 的正负组合直接对应 4 个拐点象限（详见 §5）。

### 3.4 排名合成指标（4 个）

| 指标 | 公式 | 备注 |
|---|---|---|
| **MOM_21_z** | `(MOM_21 - μ_MOM21) / σ_MOM21`（横截面） | μ/σ 在**当日所有有效板块**上算 |
| **RS_60_z** | 同上 | |
| **VOL_RATIO_z** | 同上 | sd=0 时退化为 0 |
| **score**（强度分） | `(MOM_21_z + RS_60_z + VOL_RATIO_z) / 3` | 等权合成 |
| **rank** | `score.rank(ascending=False, method='min')` | 1 = 最强 |

---

## 4. 综合评分与最终排名

```
composite_score = score + PHASE_BONUS[phase]
```

### 4.1 PHASE_BONUS 加分表

| phase | 中文 | 加分 | 推荐度 |
|---|---|---|---|
| `accel_up` | 主升 / 强势确认 | **+3.0** | ★★★ 强烈推荐 |
| `decel_down` | 见底 / 底背离前兆 | **+2.0** | ★★ 左侧抄底 |
| `decel_up` | 高位钝化 / 顶背离前兆 | **+0.5** | ☆ 中性偏空 |
| `accel_down` | 杀跌 / 戴维斯双杀 | **-2.0** | ✗ 规避 |
| `neutral` | 震荡 / 信号不明 | **0.0** | - |

> **设计意图**：强度分只看「绝对水平」，加上 phase 加分后能在横截面里区分"现在正在加速上行"和"高位横盘"。注意加分是 **绝对值**（3、2、0.5、-2），与强度 z-score 同量纲（z 通常在 -2 ~ +3 之间），所以权重影响显著。

### 4.2 composite_rank

按 `composite_score` 降序排，1 = 最推荐。

---

## 5. 四象限判定逻辑（phase）

### 5.1 投票机制

```
速度组 (一阶导) vote = sign(ROC_20)*2 + sign(MA20_SLOPE)*1
   → velocity_dir ∈ {-1, 0, +1}
   → ROC_20 阈值 0.5%（过滤平盘噪音）

加速度组 (二阶导) vote = sign(MA20_ACCEL)*1 + sign(MACD_HIST 变化)*1
   → accel_dir ∈ {-1, 0, +1}
   → 阈值 0
```

### 5.2 象限映射

| velocity_dir | accel_dir | phase | 操作建议 |
|---|---|---|---|
| +1 | +1 | **accel_up** | 追涨 / 持有 |
| +1 | -1 | **decel_up** | 减仓 / 观望（顶背离前兆） |
| -1 | -1 | **accel_down** | 清仓 / 不接刀 |
| -1 | +1 | **decel_down** | 小仓试探 / 等右侧（底背离前兆） |
| 0 | * | **neutral** | 观望 |

### 5.3 阶段边界

- 样本不足（deriv 长度 < 30）→ 返回 `neutral` 且带 `_skip=True`（被 `scan_all_sectors_phase` 过滤）
- 速度分=0 → phase=`neutral`（即使加速度有信号，也归 neutral）

---

## 6. 完整 Pipeline 串讲

入口脚本 `3-run_metric_today.py`：

```
1. rank_industries(level=2, end_date=None, lookback_days=90)
   → load_all_sectors() 拉所有板块 OHLCV
   → build_market_benchmark() 合成全市场基准（板块等权 × 1000）
   → 对每板块算 MOM_21 / RS_60 / VOL_RATIO
   → 横截面 Z-score → score → rank
   → 返回 DataFrame: [MOM_21, RS_60, VOL_RATIO, *_z, score, rank, member_count]

2. scan_all_sectors_phase(level=2, end_date=None)
   → load_all_sectors() 同上
   → 对每板块 calc_all_derivatives() → ROC_20 / MA20_SLOPE / MACD_HIST / MA20_ACCEL / ...
   → detect_one_sector_phase() 投票判定 phase
   → 按 (phase 优先级, ROC_20 desc) 排序
   → 返回 DataFrame: [phase, phase_desc, vote_*, ROC_20, MA20_SLOPE, MACD_HIST, MA20_ACCEL, ...]

3. build_combined_view() 把两者 left join
   → phase 缺失 → 'neutral'
   → composite_score = score + PHASE_BONUS[phase]
   → composite_rank 按 composite_score 降序

4. save_today_view() 落盘到 outputs/ 目录
```

---

## 7. 输出文件清单

`outputs/` 目录下（默认相对 `3-run_metric_today.py`）：

| 文件 | 内容 | 用途 |
|---|---|---|
| `sector_combined_today.csv` | 全字段合并表（强度 + phase + composite） | 数据下游、Excel 透视 |
| `sector_strength_today.csv` | 仅强度列（score / rank / MOM_21 / RS_60 / VOL_RATIO / *_z / member_count） | 横截面监控 |
| `sector_phase_today.csv` | 仅 phase 列（phase / phase_desc / ROC_20 / MA20_SLOPE / MACD_HIST / MA20_ACCEL / vote_*） | 拐点监控 |
| `sector_today_topN.txt` | 人类可读摘要：Top N + 主升/见底列表 + 末 5 警示 | 晨会报告 |

---

## 8. 可调参数清单（后续优化抓手）

| 参数 | 当前值 | 文件:行 | 影响 |
|---|---|---|---|
| `--days` 增量窗口 | 60 | `2-run_data_daily.py:52` | 重算板块 K 线的尾部长度 |
| `lookback_days` | 90 | `industry_strength.rank_industries` | 强度打分最少需要的天数 |
| `min_days` | 60 | `sector_loader.load_all_sectors` | 数据过滤阈值 |
| `roc_threshold` | 0.005（0.5%） | `detect_one_sector_phase` | 速度组 ROC 阈值，影响 phase 灵敏度 |
| `accel_threshold` | 0.0 | `detect_one_sector_phase` | 加速度组阈值 |
| `PHASE_BONUS` | {accel_up:3, decel_down:2, decel_up:0.5, accel_down:-2, neutral:0} | `3-run_metric_today:32` | 综合分权重 |
| `top_n` | 10 | `3-run_metric_today` CLI | 报告输出 TopN 大小 |
| 等权 vs 流通市值加权 | 当前**等权** | `sector_index_builder.aggregate_sector_one_day` | 龙头股影响力 |
| MA / ROC 窗口 | MA20/SLOPE10/ROC20/ACCEL_LAG5 | `derivatives.py` | 一/二阶导的灵敏度 |
| MACD 参数 | 12/26/9 | `derivatives.macd_hist` | 经典默认 |
| Z-score vs 百分位 vs 排名分 | 当前**Z-score** | `industry_strength:142` | 横截面可比性 |

---

## 9. 当前实现的局限性（可优化的点）

1. **量能/价格未做"加速"判断**：`VOL_RATIO` 只看近 5 日 vs 近 60 日的静态比，没有「量能是否在加速放大」的二阶指标。
2. **缺少板块间相关性矩阵**：rotational 信号常受"全市场风险偏好"影响，但当前 benchmark 是简单等权，没有风格中性化。
3. **Z-score 对极端值敏感**：单板块因成分股重组或极端行情产生的 outlier 会拉高 σ，建议后续加 winsorize 或换 rank 分。
4. **PHASE_BONUS 是硬编码**：加分量级决定了"phase 派 vs 强度派"的胜负，但当前没有任何自适应机制（比如根据历史回测调整）。
5. **没有持续性度量**：连续 N 天在 Top 10 / 连续 N 天 phase=accel_up 这种"动量延续"信号没纳入。
6. **样本不足时静默退化为 neutral**：新板块或回溯日期过早时容易出空信号，没有标记"因数据不足跳过"。
7. **市场基准只用了"全部板块等权"**：没考虑市值加权、没考虑剔除当日停牌板块，理论上大票主导的指数会偏离。

---

## 10. 后续可视化能力建设建议

按以下顺序增量加：

1. **强度热力图**：横轴=交易日，纵轴=板块，色块=`composite_score`，滚动 N 天窗口。
2. **四象限散点图**：x=`ROC_20`（速度），y=`MA20_ACCEL`（加速度），点=板块，颜色=phase；右上=accel_up，左下=accel_down。
3. **Phase 时序切换图**：每个板块一条线，颜色随 phase 变化（accel_up 绿、accel_down 红、neutral 灰），时间滑块。
4. **TopN 漂移图**：连续 N 天 Top10 板块集合的并集热力（看"持续热门"vs"昙花一现"）。
5. **综合评分雷达**：选定 K 个候选板块，把 MOM/RS/VOL/MACD/SLOPE/ACCEL 6 维标准化后画雷达对比。

---

## 11. 相关文件索引

| 文件 | 角色 |
|---|---|
| `1-run_init.py` | 一次性初始化（申万分类） |
| `2-run_data_daily.py` | 每日 K 线下载 + 板块指数增量重算 |
| `3-run_metric_today.py` | **本说明文档的主入口**，产出当日综合视图 |
| `derivatives.py` | 一/二阶导基础指标 |
| `industry_strength.py` | 强度打分（MOM/RS/VOL → score → rank） |
| `inflection_detector.py` | 速度+加速度投票 → phase |
| `sector_loader.py` | 板块 K 线加载 + 市场基准合成 |
| `sector_index_builder.py` | 等权板块 OHLC 合成（落 trade_sector_daily） |
| `industry_meta.py` | 申万分类同步与查询 |
| `stock_kline_loader.py` | 股票 K 线下载 |

---

> **维护说明**：本模块与 CASE-A 的 `trade_sector_daily` 表强耦合。任何字段重命名、窗口调整、阈值变更，请同步更新本文档的 §3、§5、§8 三张表。