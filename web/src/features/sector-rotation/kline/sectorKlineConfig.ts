/** 板块 K 线组件共享的观察窗口、指标参数与 A 股配色常量。 */

/** 行情弹窗可切换的交易日观察窗口，顺序同时用于控件展示。 */
export const KLINE_WINDOWS = [60, 120, 250] as const;

/** 单个可选交易日窗口的联合类型，防止 UI 传入未设计的任意天数。 */
export type KlineWindow = (typeof KLINE_WINDOWS)[number];

/** 抽屉缩略图和弹窗首次打开时默认展示的交易日数量。 */
export const DEFAULT_KLINE_WINDOW: KlineWindow = 120;

/**
 * KLineChart 内置指标与系统 MACD 适配器共享的固定计算参数。
 *
 * 输入：无。
 * 输出：MA、BOLL、VOL 和 MACD 的只读周期参数。
 * 异常：无；调用方不得修改本常量，应直接传递或复制其中数组。
 */
export const INDICATOR_PARAMS = {
  ma: [5, 10, 20, 60],
  boll: [20, 2],
  vol: [5, 10],
  macd: [12, 26, 9],
} as const;

/**
 * 量化工作台深色主题下的 A 股红涨绿跌及指标线配色。
 *
 * 输入：无。
 * 输出：图表运行时与样式层可复用的十六进制颜色。
 * 异常：无；颜色语义固定，避免各 pane 出现不一致的涨跌方向。
 */
export const KLINE_COLORS = {
  up: "#ff7285",
  down: "#37d6b0",
  ma5: "#f0b65a",
  ma10: "#67a9ff",
  ma20: "#9a8cff",
  ma60: "#ff8fc7",
  boll: "#35cbd6",
  dif: "#f0b65a",
  dea: "#67a9ff",
} as const;
