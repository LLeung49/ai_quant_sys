# 板块详情 K 线三联图设计规格

> 状态：已完成产品与技术方案评审，等待用户最终复核后进入实施计划。
> 日期：2026-08-07
> 适用模块：`morning_conference.sector_rotation2` 只读 API 与 `web` 板块轮动工作台。

## 1. 背景

当前板块详情抽屉能够解释阶段、排名、评分分解和数据质量，但缺少直接的量价走势证据。用户需要在抽屉内快速查看板块传统 K 线、均线、布林带、成交量和 MACD，并能放大到专业行情窗口进行更细致的历史观察。

本功能展示的是 `trade_sector_daily` 已生成的板块等权合成指数，不是成分股价格的临时聚合，也不是可交易证券价格。所有技术指标仅用于研究观察，不产生买入、卖出或收益承诺。

## 2. 目标与非目标

### 2.1 目标

- 在现有板块详情抽屉中增加全宽行情缩略三联图。
- 同时展示 K 线与 MA/BOLL、成交量与量均线、MACD。
- 提供明确的“放大查看”入口，在大尺寸悬浮窗口中复用同一套行情数据和指标。
- 确保单日观察和动态回放都严格以工作台显示日期为行情截止日，禁止未来数据泄漏。
- 支持 60、120、250 个交易日窗口，默认 120 日。
- 优先使用成熟专业三方工具，避免自行实现金融图表引擎和已有技术指标。
- 延续现有统一 API 契约、错误码、日志、数值序列化、测试和中文注释规范。

### 2.2 非目标

- 不新增 MySQL 表，不执行 DDL。
- 不在 API 请求时重新聚合板块成分股。
- 不提供分时、分钟线、实时 WebSocket、画线工具、交易下单或预警。
- 不把技术指标结果持久化到快照表。
- 不生成“买入”“卖出”等交易信号。
- 不改造现有象限图和行业历史轨迹图；它们继续使用 ECharts。

## 3. 已确认的产品决策

| 决策项 | 结论 |
|---|---|
| 抽屉布局 | 采用单画布纵向三联图：K 线、成交量、MACD 同时可见 |
| 放大布局 | 采用全宽专业三联图，不增加右侧解释栏 |
| 截止日期 | 始终等于工作台当前显示日期；不得读取其后行情 |
| 可见窗口 | 60/120/250 日，默认 120 日，缩略图与弹窗同步 |
| MA | MA5、MA10、MA20、MA60 |
| BOLL | BOLL20，标准差倍数 2 |
| MACD | 12/26/9，柱值遵循 `2 × (DIF - DEA)` |
| 成交量 | 成交量柱 + VOL MA5、VOL MA10 |
| 数据源 | 现有 `trade_sector_daily` |
| 涨跌颜色 | A 股习惯：红涨绿跌 |
| 图表引擎 | 精确锁定 KLineChart Core；不使用 KLineChart Pro |

## 4. 三方工具调研与技术选型

### 4.1 采用 KLineChart Core

实施时安装并精确锁定 `klinecharts@10.0.0`，通过 `package-lock.json` 固定版本，不使用 CDN 或浮动版本。

采用原因：

- 专门面向金融行情，原生提供蜡烛、多窗格、缩放、滚动、Tooltip 和移动端交互。
- 内置 MA、BOLL、VOL、MACD，可覆盖本需求，避免自行实现指标与多窗格联动。
- TypeScript 开发、零运行时依赖、约 40KB gzip，适合按需加载。
- Apache License 2.0，适合未来 TOC 商业产品。
- 官方数据结构需要 `timestamp/open/high/low/close/volume/turnover`，可由现有表直接映射。

官方资料：

- [KLineChart GitHub](https://github.com/klinecharts/KLineChart)
- [技术指标](https://klinecharts.com/en-US/guide/indicator.html)
- [数据接入](https://klinecharts.com/en-US/guide/data-integration)
- [环境与响应式要求](https://klinecharts.com/en-US/guide/environment)
- [npm 包](https://www.npmjs.com/package/klinecharts)

### 4.2 未采用方案

- **继续使用 ECharts**：项目已安装，但金融行情多窗格、完整指标、联动十字线和专业缩放仍需较多手工配置和测试。ECharts 保留给现有象限与轨迹图。
- **TradingView Lightweight Charts**：性能优秀，但本需求的多个指标仍需自行计算或维护插件，而且产品页面需要遵守 TradingView 署名与链接要求。
- **KLineChart Pro**：虽有开箱 UI，但官方 GitHub 最新发布仍是 2023 年的 `0.1.1`，与当前 Core 10.x 的维护节奏不一致。
- **Highcharts Stock**：指标完善，但未来 TOC 商业使用需要相应商业许可证。

### 4.3 MACD 口径验证门槛

实现第一步必须用固定收盘序列验证 KLineChart 内置 MACD 是否与现有 Python 口径一致：

```text
DIF = EMA(close, 12) - EMA(close, 26)
DEA = EMA(DIF, 9)
HIST = 2 × (DIF - DEA)
```

若完全一致，直接使用内置 MACD；若柱值缺少倍数 2 或 EMA 初始化口径不一致，只注册一个薄的 MACD 适配指标。MA、BOLL、VOL 仍使用内置实现，不扩展自研范围。

## 5. 数据源与口径

### 5.1 来源字段

从 `trade_sector_daily` 读取：

| API 字段 | 数据库字段 | 含义 |
|---|---|---|
| `trade_date` | `trade_date` | 板块交易日 |
| `open` | `open_idx` | 板块等权合成开盘指数 |
| `high` | `high_idx` | 板块等权合成最高指数 |
| `low` | `low_idx` | 板块等权合成最低指数 |
| `close` | `close_idx` | 板块等权合成收盘指数 |
| `volume` | `total_volume` | 有效成分股成交量合计 |
| `amount` | `total_amount` | 有效成分股成交额合计 |

查询维度为 `sector_name + sector_level`，条件必须包含 `trade_date <= requested_end_date`。

### 5.2 查询数量与指标预热

接口固定最多返回最近 350 根有效日 K 线，并按交易日升序排列：

- 最多 250 根用于可见窗口。
- 额外最多 100 根用于 MA60、BOLL 和 MACD 预热。
- 60/120/250 日切换只修改 KLineChart 可见范围，不重新访问 API。
- 若历史不足，展示已有数据并明确提示长周期指标仍在形成。

前端针对当前窗口计算：

```text
warmup_used = max(0, bar_count - visible_count)
warmup_sufficient = warmup_used >= 100
```

### 5.3 日线时间戳

API 同时返回 ISO 交易日和毫秒时间戳。`timestamp` 固定表示该交易日 `00:00:00 Asia/Shanghai` 对应的 Unix 毫秒值，图表时区也设置为 `Asia/Shanghai`。必须用测试覆盖日期不前移、不后移。

### 5.4 指标计算位置

API 只返回原始 OHLCV/成交额；MA、BOLL、VOL 均线和 MACD 由浏览器中的 KLineChart 对完整 350 根序列计算。指标不写入数据库，也不与 `sector_rotation_sector_daily_snapshot` 混合。

## 6. API 设计

### 6.1 接口

```http
GET /api/v1/sector-rotation/sector-kline
```

参数：

| 参数 | 类型 | 约束 |
|---|---|---|
| `sector_name` | string | 必填，去除首尾空白后非空，长度不超过 64 |
| `level` | integer | 必填，只允许 1 或 2 |
| `end_date` | ISO date | 必填，工作台当前显示日期 |

不传 `model_version`。板块行情是模型无关的基础行情，模型版本仅属于评分快照。

### 6.2 成功响应

```json
{
  "sector_name": "半导体",
  "sector_level": 2,
  "requested_end_date": "2026-08-06",
  "actual_end_date": "2026-08-06",
  "price_basis": "equal_weight_composite_index",
  "bars": [
    {
      "trade_date": "2026-08-06",
      "timestamp": 1785945600000,
      "open": 1270.12,
      "high": 1291.30,
      "low": 1262.48,
      "close": 1284.32,
      "volume": 185342000,
      "amount": 84260000000
    }
  ],
  "meta": {
    "field_version": "v1",
    "source": "trade_sector_daily",
    "bar_count": 350,
    "skipped_bar_count": 0,
    "warmup_target": 100
  }
}
```

当请求日是非交易日时，`actual_end_date` 为此前最近交易日。响应中绝不允许出现晚于 `requested_end_date` 的 K 线。

### 6.3 数据校验

每根 K 线必须满足：

```text
open/high/low/close 为有限正数
low <= open 且 low <= close
high >= open 且 high >= close
high >= low
volume >= 0
amount >= 0
trade_date 唯一且严格升序
trade_date <= requested_end_date
```

非法行从 `bars` 排除，并计入 `skipped_bar_count`。前端必须展示数据质量提示，不能静默掩盖。

### 6.4 错误码

| HTTP | `error.code` | 场景 |
|---:|---|---|
| 422 | `INVALID_PARAMETER` | 行业、层级或日期不合法 |
| 404 | `SECTOR_KLINE_NOT_FOUND` | 截止日期前无有效行情 |
| 503 | `DATABASE_UNAVAILABLE` | 数据库不可用 |
| 500 | `INTERNAL_ERROR` | 未预期错误 |

继续使用现有统一错误信封：

```json
{
  "error": {
    "code": "SECTOR_KLINE_NOT_FOUND",
    "message": "未找到该板块在指定日期前的有效行情",
    "details": null,
    "request_id": "..."
  }
}
```

## 7. 前端架构

### 7.1 组件结构

```text
SectorDetailDrawer
├─ 原有阶段结论与三项摘要
├─ SectorKlineCard
│  ├─ 行情标题、截止日期、数据质量、放大按钮
│  └─ LazySectorKlineChart(mode="compact")
├─ 原有评分拆解
├─ 原有排名与数据质量
└─ SectorKlineModal（通过 Portal 挂载到 document.body）
   ├─ 标题、关键行情快照、窗口与指标开关
   └─ LazySectorKlineChart(mode="expanded")
```

建议文件边界：

- `api.ts` 或独立 `sectorKlineApi.ts`：请求与 Zod 契约校验。
- `useSectorKline.ts`：TanStack Query 封装。
- `kline/SectorKlineCard.tsx`：抽屉行情区状态外壳。
- `kline/SectorKlineChart.tsx`：KLineChart 生命周期和指标创建。
- `kline/LazySectorKlineChart.tsx`：动态图表依赖入口。
- `kline/SectorKlineModal.tsx`：Portal、焦点约束、遮罩和关闭。
- `kline/sectorKlineTheme.ts`：颜色、字体、网格、Tooltip 样式。
- `kline/sectorKlineConfig.ts`：窗口和指标参数常量。

### 7.2 请求与缓存

- 只有抽屉已打开且行业、层级、截止日期完整时才请求。
- Query Key 包含 `sector_name/level/end_date`。
- 缩略图与放大弹窗共享同一份 Query 数据，不重复请求。
- 过去日期行情可长时间缓存；当前最新日期使用较短 `staleTime`。
- 快速切换行业、层级或日期时取消旧请求，旧响应不得覆盖新抽屉。

### 7.3 图表生命周期

- 通过动态 `import('klinecharts')` 延迟加载，首页首屏不引入行情图引擎。
- 容器真实可见且宽高大于零后才调用 `init()`。
- 使用 `ResizeObserver` 触发 `resize()`。
- 组件卸载或弹窗关闭时必须调用 `dispose()`。
- 弹窗实例只在弹窗打开时存在；关闭后立即释放。

## 8. 布局与视觉

### 8.1 抽屉顺序

```text
板块名称与关闭
阶段结论
阶段持续 / 综合排名 / 阶段置信度
板块行情缩略三联图
评分拆解
排名与数据质量
风险提示
```

### 8.2 缩略图

- 宽度占满抽屉内容区，总高度约 340px。
- K 线约 190px、成交量约 55px、MACD 约 75px、时间轴约 20px。
- 默认显示 120 日。
- 支持悬浮十字线，不允许缩放、拖动和区间选择。
- 只通过明确的“放大查看”按钮打开弹窗。

### 8.3 放大弹窗

- 桌面端约 `92vw × 88vh`，最大宽度 1440px。
- 窄屏使用接近 `100vw × 100dvh` 的全屏布局。
- K 线、成交量、MACD 高度比例约为 58%、15%、23%，其余为时间轴和间距。
- 顶部显示板块、实际截止日期、层级、收盘指数、涨跌幅、阶段和成交额。
- 支持 60/120/250 日切换、滚轮缩放、拖动平移和底部范围控制。
- 三个窗格共享日期十字线。

### 8.4 颜色与指标显示

- 上涨 K 线、上涨成交量柱和正 MACD 柱：红色。
- 下跌 K 线、下跌成交量柱和负 MACD 柱：绿色。
- MA5：金色；MA10：蓝色；MA20：紫色；MA60：粉色。
- BOLL 上下轨：青色虚线。
- DIF：金色；DEA：蓝色。

BOLL 中轨等于 MA20。为避免完全重叠，只绘制一次，在 Tooltip 中标为 `MA20 / BOLL MID`。

### 8.5 Tooltip

十字线定位交易日后展示：

- 日期、开盘、最高、最低、收盘。
- 涨跌幅、振幅。
- 成交量、成交额。
- MA5、MA10、MA20、MA60。
- BOLL 上轨、中轨、下轨。
- DIF、DEA、MACD 柱。

不展示交易建议。

## 9. 交互和可访问性

- 缩略图允许悬浮读取，但不响应缩放与拖动。
- 弹窗允许缩放、平移和范围调整。
- 抽屉与弹窗共享 60/120/250 日窗口状态。
- 弹窗通过右上角按钮、Esc 或点击遮罩关闭。
- 第一次 Esc 只关闭弹窗，第二次才关闭抽屉。
- 弹窗打开后锁定背景滚动并限制焦点；关闭后焦点返回“放大查看”按钮。
- 切换行业、层级或工作台日期时自动关闭弹窗，防止旧行情闪现。
- 按钮提供可读中文 `aria-label`，图表容器提供板块、截止日和图表组成的辅助说明。

## 10. 加载、空态与降级

- 加载中：行情卡片骨架屏，原有抽屉信息立即可读。
- 无数据：展示“该板块在指定日期前暂无有效行情”，隐藏放大按钮。
- 部分坏数据：继续绘图，并展示“有 N 个交易日行情异常已跳过”。
- 预热不足：展示“长周期指标仍在形成”。
- API 失败：只影响行情卡片，提供重试；不能导致整个抽屉白屏。
- KLineChart 初始化异常：局部错误边界捕获，记录错误并显示降级提示。
- 数据库不可用：保留现有 `request_id`，方便服务端日志定位。

## 11. 测试设计

### 11.1 后端

- 仓储使用参数化 SQL，行业名称不拼接进 SQL。
- 查询包含 `trade_date <= end_date`，最多返回 350 根。
- 结果按交易日升序、无重复。
- Decimal 转换为 JSON number。
- 非法 OHLCV 被跳过并准确计数。
- 覆盖请求日、实际交易截止日和 Asia/Shanghai 时间戳。
- 覆盖 200、404、422、503 与统一错误信封。
- 断言任何响应都没有晚于请求日的行情。

### 11.2 前端

- Zod 拒绝字符串数值、缺字段和不合法 OHLC。
- 抽屉关闭时不请求。
- Query Key 包含行业、层级和截止日期。
- 60/120/250 日切换不产生新请求。
- 动态 import、初始化、ResizeObserver、resize 和 dispose 生命周期。
- MA/BOLL/VOL/MACD 参数与颜色。
- compact 禁用缩放，expanded 启用缩放和平移。
- 弹窗 Portal、焦点约束、Esc 层级和焦点恢复。
- API 或图表失败不影响抽屉其他区域。
- 快速切换行业时不显示旧数据。
- 后续日期数据不会进入历史回放图表。

### 11.3 指标一致性

使用同一组固定 OHLCV 测试数据对比：

- MA5/10/20/60。
- BOLL20/2。
- VOL MA5/10。
- MACD DIF/DEA/HIST 与现有 Python `derivatives.py`。

## 12. 验收标准

1. 单日观察中，行情实际截止日与工作台日期一致。
2. 动态回放到历史日期后，任何未来 K 线均不可见。
3. 数据库抽样 OHLCV、成交额与 Tooltip 一致。
4. 抽屉内三联图完整、可读、宽度自适应且不会误拖动。
5. 放大窗口布局符合已确认的全宽方案。
6. 红涨绿跌、指标参数和颜色符合本规格。
7. 60/120/250 日切换、缩放、平移和联动十字线有效。
8. 无数据、坏数据、预热不足和数据库失败都有局部状态。
9. 桌面和窄屏布局均可使用，键盘焦点与 Esc 行为正确。
10. 控制台无零尺寸、重复初始化、未销毁实例或未处理 Promise 警告。
11. 前后端测试、TypeScript lint 和生产构建全部通过。
12. README 包含启动、接口、第三方库、许可证、使用与 Review 步骤。

## 13. 数据库影响

本功能为纯只读能力：

- 不新增表或字段。
- 不执行 DDL。
- 不修改 `trade_sector_daily`。
- 不修改 `sector_rotation_` 快照、运行审计或回测表。
