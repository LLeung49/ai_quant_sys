/** 板块 K 线系统 MACD 适配器：锁定与 Python ``adjust=False`` 一致的计算口径。 */
import {
  getSupportedIndicators,
  registerIndicator,
  type IndicatorTemplate,
  type KLineData,
} from "klinecharts";
import { INDICATOR_PARAMS } from "./sectorKlineConfig";

/** 当内置 MACD 初始化方式与 Python 不一致时，系统注册的薄适配器名称。 */
export const SYSTEM_MACD_NAME = "SYSTEM_MACD";

/** 单个交易日的系统 MACD 计算结果；``macd`` 即 HIST，固定为 ``2 × (DIF - DEA)``。 */
export interface SystemMacdValue {
  dif: number;
  dea: number;
  macd: number;
}

/**
 * 校验 MACD 周期参数，避免错误配置被静默带入图表运行时。
 *
 * 输入：快线、慢线和信号线的 EMA 周期。
 * 输出：无；参数通过时函数正常返回。
 * 异常：任一周期不是正整数，或快线周期不小于慢线周期时抛出 ``RangeError``。
 */
function validateMacdParams(fast: number, slow: number, signal: number): void {
  if (![fast, slow, signal].every((value) => Number.isInteger(value) && value > 0) || fast >= slow) {
    throw new RangeError("MACD 参数必须是正整数，且快线周期必须小于慢线周期");
  }
}

/**
 * 按 pandas ``ewm(span=n, adjust=False)`` 的递推公式计算系统 MACD。
 *
 * 输入：按交易日升序的有限收盘价，以及可选的快线、慢线和信号线周期。
 * 输出：与输入同长度的 DIF、DEA、MACD(HIST) 序列；首根从收盘价本身初始化 EMA。
 * 异常：收盘价包含非有限数值，或周期组合不合法时抛出 ``RangeError``。
 */
export function calculateSystemMacd(
  closes: readonly number[],
  fast: number = INDICATOR_PARAMS.macd[0],
  slow: number = INDICATOR_PARAMS.macd[1],
  signal: number = INDICATOR_PARAMS.macd[2],
): SystemMacdValue[] {
  validateMacdParams(fast, slow, signal);
  if (!closes.every(Number.isFinite)) {
    throw new RangeError("MACD 收盘价必须全部为有限数值");
  }
  if (closes.length === 0) {
    return [];
  }

  const fastWeight = 2 / (fast + 1);
  const slowWeight = 2 / (slow + 1);
  const signalWeight = 2 / (signal + 1);
  let fastEma = closes[0]!;
  let slowEma = closes[0]!;
  let dea = 0;

  return closes.map((close, index) => {
    if (index > 0) {
      fastEma = close * fastWeight + fastEma * (1 - fastWeight);
      slowEma = close * slowWeight + slowEma * (1 - slowWeight);
    }
    const dif = fastEma - slowEma;
    // pandas 的 adjust=False 信号线从首个 DIF 开始递推，而不是先做 SMA 预热。
    dea = index === 0 ? dif : dif * signalWeight + dea * (1 - signalWeight);
    return { dif, dea, macd: 2 * (dif - dea) };
  });
}

/**
 * 将 KLineChart 的日线数据转换为系统 MACD 所需的收盘价序列。
 *
 * 输入：KLineChart 提供的升序 K 线数据，以及指标实例当前的计算参数。
 * 输出：可由图表直接绘制的 DIF、DEA 和 MACD(HIST) 结果。
 * 异常：收盘价或指标参数不合法时透传 ``calculateSystemMacd`` 的 ``RangeError``。
 */
function calculateSystemMacdForKlineChart(
  dataList: KLineData[],
  indicator: { calcParams: number[] },
): SystemMacdValue[] {
  const [fast, slow, signal] = indicator.calcParams;
  return calculateSystemMacd(dataList.map((bar) => bar.close), fast, slow, signal);
}

/** 仅补齐内置 MACD 与 Python EMA 初始化差异的 KLineChart 指标模板。 */
const SYSTEM_MACD_TEMPLATE: IndicatorTemplate<SystemMacdValue, number> = {
  name: SYSTEM_MACD_NAME,
  shortName: "MACD",
  calcParams: [...INDICATOR_PARAMS.macd],
  figures: [
    { key: "dif", title: "DIF: ", type: "line" },
    { key: "dea", title: "DEA: ", type: "line" },
    { key: "macd", title: "MACD: ", type: "bar", baseValue: 0 },
  ],
  calc: calculateSystemMacdForKlineChart,
};

/**
 * 幂等注册系统 MACD 薄适配器，供图表运行时在创建指标前调用。
 *
 * 输入：无。
 * 输出：无；首次调用注册 ``SYSTEM_MACD``，重复调用不改变全局注册表。
 * 异常：KLineChart 注册表不可用时由第三方库抛出原始异常。
 */
export function ensureSystemMacdRegistered(): void {
  if (!getSupportedIndicators().includes(SYSTEM_MACD_NAME)) {
    registerIndicator(SYSTEM_MACD_TEMPLATE);
  }
}
