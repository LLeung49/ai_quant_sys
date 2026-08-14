# 板块短期异动可视化优化建议(2026-08-14)

> 上下文:短期异动(`v2_short_term`)已具备 24 项原始特征、5 类短期评分、9 种异动标签、4 档强度、历史轨迹 API,但前端仅以"2×2 KPI + 上下热力图 + 字段抽屉"呈现,大量维度被浪费。本文件汇总用户提出的 5 个改造方向、优先级与可选的数据层增强,作为后续设计与实施的输入。

## 背景与问题诊断

短期层的数据资产远超当前热力图的承载力。当前浪费的视角:

| 已有数据 | 当前用途 | 浪费的视角 |
| --- | --- | --- |
| `pulse_score` / `volume_spike_score` / `breadth_spike_score` / `limit_score` / `momentum_shift_score` | 仅在详情抽屉以数字列出 | 缺少类 v1 象限图,无法一眼定位"脉冲上涨 + 量能"的板块 |
| `rs_5`、`rs5_accel_1d`、`ma5_slope` | 未参与任何可视化 | 缺少数 5 日动量变化的方向感(从弱势反弹 / 从强势走弱) |
| `streak_pos_ret` / `streak_high_breadth` / `streak_top_limit_up` | 仅在详情抽屉显示 | 缺少短期连续性时间轴,看不出"连续 3 天放量"这种积累过程 |
| `breadth_above_ma5` / `breadth_new_high_5` / `breadth_strong_1d` | 仅在详情抽屉显示 | 缺少板块内部广度热图,无法看出"指数涨但只有 20% 个股跟"的内部分化 |
| `short_term_composite` + v1 的 `composite_score` | 完全隔离 | 缺少两套评分的并列视图,看不出"v1 中期向上 + 当日脉冲异动"这类叠加信号 |
| 9 种标签的多值命中 | 详情抽屉以 Chip 罗列 | 缺少当日所有异动榜总览,以及"明日观察候选"的智能聚合 |

## 五个改造方向

### 方向 ① 明日观察候选面板(Next-Day Watch Panel)—— 已交付(2026-08-14)

**目的**:把当日命中板块按"信号组合"聚合成 4 类次日观察候选。

**触发规则**(纯前端组合,0 后端改动):

| 卡片 | 触发条件 | 含义 |
| --- | --- | --- |
| 强势跟进 | `pulse_up + volume_spike` | 当日强势 + 量能确认,次日继续观察 |
| 恐慌观察 | `pulse_down + volume_spike` 或 `limit_panic` | 当日恐慌 + 放量,等待情绪修复 |
| V形反弹 | `short_rebound_candidate` | 前 5 日弱势中突然转强 |
| 破位警惕 | `short_breakdown_candidate` | 前 5 日强势中突然走弱 |

**输出**:
- 每张卡片显示命中板块数 + 列表(最多展示 5 个,展开可看全部);
- 命中板块按 `short_term_composite` 降序 → `short_term_composite_rank` 升序 → 行业名稳定排序;`null` / `NaN` 排在末尾;
- 点击板块名直接联动到详情抽屉;
- 当某类卡片命中数为 0 时仍展示,文案写"今日无此类信号";
- **基于完整 `snapshot.sectors`,不受页面标签筛选影响**;
- 切换日期 / 层级时,展开状态通过 `useEffect` 自动收起。

**交付物**:
- 纯函数与测试:`web/src/features/sector-rotation/short_term/nextDayWatch.ts`、`nextDayWatch.test.ts` (4 项断言:四类规则、允许多重归类、稳定排序、标签 CSV 顺序无关);
- 面板组件与测试:`web/src/features/sector-rotation/short_term/NextDayWatchPanel.tsx`、`NextDayWatchPanel.test.tsx` (8 项断言:渲染、排序、展开 / 收起、点击、空态、快照切换重置、初始空快照);
- 元数据:`labels.ts` 新增 `NEXT_DAY_WATCH_GROUP_META` 与 `getNextDayWatchGroupMeta`,暴露中文标题、研究说明、配色基调、图标名;
- 集成:`ShortTermAnomalyModule.tsx` 在 KPI 之后、热力图前接入面板,接收完整 `sectors` 与 `handleSelect`;
- 集成测试:`ShortTermAnomalyModule.test.tsx` 新增 4 项断言:KPI / 候选面板位置、标签筛选不影响候选面板、点击候选按钮触发详情抽屉与外部 `onSectorSelect`;
- 样式:`web/src/styles/globals.css` 末尾追加 `.next-day-watch*` 作用域,桌面 4 列 / 中宽 2 列 / ≤760px 单列,聚焦样式明确;
- 文档:`板块异动使用指南.md` §10.6 同步记录规则、边界与测试覆盖。

**约束遵守**:不修改后端、数据库、`v1` 或 `v2` 标签规则;面板仅在 `score_eligible=true` 板块中聚合;不输出交易指令、仓位或收益判断;`useEffect([sectors])` 收起避免上一日交互状态污染新快照。

### 方向 ② v1 主象限图叠加短期异动光晕

**目的**:不动 v1 象限图本身,给它加一层"短期异动光晕"作为信息加成。

- 主象限图保留原有坐标(velocity × acceleration);
- 每个气泡描边在命中短期标签时变成带颜色的脉冲环(`intense=橙红 / moderate=琥珀 / mild=蓝绿`),线宽映射 `short_term_intensity`;
- 每个气泡右上角挂一个标签 Chip(优先显示 `pulse_up` / `limit_cluster` / `pulse_down` 这类主标签);
- 顶部加一行小提示:"带橙红光晕 = 当日短期异动榜命中"。

**复用与改动**:
- `quadrantOption.ts` 增加 `shortTermIntensity` / `shortTermLabels` 字段映射;
- `SectorRotationPage` 把 `ShortTermAnomalyModule` 拉来的快照按 `sector_name` 索引合并;
- `LazyQuadrantChart` 不修改数据契约,只新增装饰层。

### 方向 ③ 短期连续性时间轴(strip chart)

**目的**:在异动榜下方插入一条"最近 5 个交易日"的 strip,区分单日异动与连续异动。

- 每个板块一行,每个交易日一格;
- 单元格颜色 = 当日命中标签的最高优先级(`SHORT_TERM_LABEL_PRIORITY`);
- 单元格深浅 = `|short_term_composite|`;
- 悬浮 tooltip:当日 `ret_1` / `rs_1` / `rvol_1_20` / 完整标签列表。

**复用**:复用现有 `fetchShortTermHistory` 接口,把时间窗口固定为最近 5~10 个交易日;不新建接口。

### 方向 ④ 短期层自己的象限图

**目的**:在 KPI 与热力图之间插入一张与 v1 平行的短期象限图。

- X 轴:`pulse_score`
- Y 轴:`volume_spike_score`
- 气泡大小:`breadth_spike_score`
- 颜色:`short_term_intensity`
- 描边:`limit_score`

**复用**:复用现有 `ShortTermLeaders` 的 ECharts 容器与 `globals.css` 的样式 token。

### 方向 ⑤ 详情抽屉升级:短期 vs v1 并列

**目的**:单板块级别的"短 + 中"信号交叉验证。

- 短期列:异动分、短期排名、强度、命中标签;
- 中期列(v1):综合分、排名、阶段、Lifecycle;
- 5 日连续性时间轴(短期连续);
- 收益曲线叠加(v1 vs v2,水平线条);
- 贡献个股 Top 5(涨停 / 跌停 / 强势放量,数据扩展项,本期可暂缓)。

**复用**:现有 `DetailSector` 类型已包含 v1 字段,合并数据即可。

## 推荐落地顺序

| 顺序 | 模块 | 价值 | 改动量 |
| --- | --- | --- | --- |
| ① | 明日观察候选面板 | 直接服务"次日投资" | 1 个组件,纯前端聚合 | **已交付**(2026-08-14) |
| ② | v1 象限图叠加短期光晕 | 最高 ROI 的信息加成 | 装饰层,不动数据 |
| ③ | 短期连续性时间轴 | 揭示连续异动 vs 单日脉冲 | 1 个组件 + 复用 history 接口 |
| ④ | 短期象限图 | 短期层自己的"主视图" | 1 个组件 |
| ⑤ | 详情抽屉双列对照 | 单板块深度 | 抽屉组件改造 |

① + ② 可在一次迭代里同时落地,实现"次日投资入口 + 主视图加成"两个核心诉求。

## 可选的数据层扩展(中长期,本期不做)

1. 贡献个股列表:从 `trade_stock_daily_qfq` 取当日涨停 / 跌停 / 强势放量个股 Top 5,喂到详情抽屉。
2. 当日分时数据:午盘异动 / 尾盘异动 / 集合竞价跳空。
3. 短期 vs 前瞻收益的回测:积累 6~12 个月快照后评估各标签对 T+1 / T+2 收益的 IC 和分组表现。
4. 异动原因旁证:接入新闻 / 研报 / 公告流,作为异动榜的"事件归因"。

## 当前文件

- 优化建议:本文件(`2026-08-14-short-term-anomaly-visualization-suggestions.md`)
- 第①项设计:`2026-08-14-p1-next-day-watch-panel-design.md`
- 第①项实施计划:`2026-08-14-p1-next-day-watch-panel-implementation-plan.md`
