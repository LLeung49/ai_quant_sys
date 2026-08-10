/** 板块 K 线三窗格的 KLineChart 10 运行时适配、指标配置与资源生命周期。 */
import type { IndicatorCreate, KLineData, Options } from "klinecharts";
import { calculateSystemMacd, SYSTEM_MACD_NAME, ensureSystemMacdRegistered, type SystemMacdValue } from "./indicatorParity";
import { INDICATOR_PARAMS, KLINE_COLORS } from "./sectorKlineConfig";
import type { SectorKlineResponse } from "./sectorKlineApi";

/** KLineChart 内置主图 candle pane 的稳定标识。 */
const CANDLE_PANE_ID = "candle_pane";

/** 图表渲染形态：抽屉缩略图禁用操控，弹窗大图允许操控。 */
export type SectorKlineChartMode = "compact" | "expanded";

/** 创建板块 K 线运行时所需的不可变输入。 */
export interface CreateSectorKlineRuntimeOptions {
  /** 已获得正宽高的图表容器。 */
  container: HTMLElement;
  /** 已通过 Zod 契约校验且交易日升序的日 K 线。 */
  bars: SectorKlineResponse["bars"];
  /** 缩略图或放大图的交互模式。 */
  mode: SectorKlineChartMode;
  /** 希望可见的最近交易日根数。 */
  visibleCount: number;
}

/** 对外暴露的最小图表生命周期控制器。 */
export interface SectorKlineRuntime {
  /** 重新读取容器尺寸后调整图表，并恢复当前观察窗口。 */
  resize(): void;
  /** 修改期望展示的交易日根数，不触发新的 HTTP 请求。 */
  setVisibleCount(count: number): void;
  /** 释放第三方图表实例；重复调用安全。 */
  dispose(): void;
}

/**
 * 生成 KLineChart 深色主题和 A 股红涨绿跌样式。
 *
 * 输入：图表展示模式。
 * 输出：可传给 KLineChart 10 ``init`` 的局部样式配置。
 * 异常：无；调用方仅可使用 ``compact`` 或 ``expanded`` 两种模式。
 */
export function buildKlineStyles(mode: SectorKlineChartMode): NonNullable<Options["styles"]> {
  const textColor = mode === "compact" ? "#7890ad" : "#9cafc8";
  return {
    grid: {
      show: true,
      horizontal: { show: true, style: "solid", size: 1, color: "rgba(133, 161, 194, .14)", dashedValue: [2, 6] },
      vertical: { show: true, style: "solid", size: 1, color: "rgba(133, 161, 194, .12)", dashedValue: [2, 6] },
    },
    candle: {
      bar: {
        upColor: KLINE_COLORS.up,
        downColor: KLINE_COLORS.down,
        noChangeColor: "#8595ae",
        upBorderColor: KLINE_COLORS.up,
        downBorderColor: KLINE_COLORS.down,
        noChangeBorderColor: "#8595ae",
        upWickColor: KLINE_COLORS.up,
        downWickColor: KLINE_COLORS.down,
        noChangeWickColor: "#8595ae",
      },
      priceMark: { show: false },
      tooltip: { showRule: "always", showType: "standard" },
    },
    indicator: {
      ohlc: {
        upColor: KLINE_COLORS.up,
        downColor: KLINE_COLORS.down,
        noChangeColor: "#8595ae",
      },
      bars: [{
        upColor: KLINE_COLORS.up,
        downColor: KLINE_COLORS.down,
        noChangeColor: "#8595ae",
      }],
      lines: [
        { color: KLINE_COLORS.ma5, size: 1 },
        { color: KLINE_COLORS.ma10, size: 1 },
        { color: KLINE_COLORS.ma20, size: 1 },
        { color: KLINE_COLORS.ma60, size: 1 },
      ],
      lastValueMark: { show: false },
      tooltip: { showRule: "always", showType: "standard" },
    },
    xAxis: { tickText: { color: textColor } },
    yAxis: { tickText: { color: textColor } },
  };
}

/**
 * 创建 MA 覆盖配置，使 MA20 与 BOLL 中轨在 Tooltip 中使用同一业务语义。
 *
 * 输入：无。
 * 输出：MA 指标覆盖对象，固定 5/10/20/60 周期的标题和颜色。
 * 异常：无；由 KLineChart 在覆盖不存在的内置指标时返回 false。
 */
function buildMaOverride(): IndicatorCreate {
  const colors = [KLINE_COLORS.ma5, KLINE_COLORS.ma10, KLINE_COLORS.ma20, KLINE_COLORS.ma60];
  const titles = ["MA5: ", "MA10: ", "MA20 / BOLL MID: ", "MA60: "];
  return {
    name: "MA",
    calcParams: [...INDICATOR_PARAMS.ma],
    figures: colors.map((color, index) => ({
      key: `ma${index + 1}`,
      title: titles[index],
      type: "line",
      styles: () => ({ color }),
    })),
  };
}

/**
 * 创建 BOLL 覆盖配置：上下轨使用青色虚线，中轨透明以避免与 MA20 重复绘制。
 *
 * 输入：无。
 * 输出：BOLL 指标覆盖对象；中轨仍保留数值计算，仅隐藏其视觉图形。
 * 异常：无；由 KLineChart 处理指标不存在的情况。
 */
export function buildBollOverride(): IndicatorCreate {
  return {
    name: "BOLL",
    calcParams: [...INDICATOR_PARAMS.boll],
    figures: [
      { key: "up", title: "BOLL UP: ", type: "line", styles: () => ({ color: KLINE_COLORS.boll, style: "dashed" }) },
      { key: "mid", title: "BOLL MID (MA20): ", type: "line", styles: () => ({ color: "transparent" }) },
      { key: "dn", title: "BOLL DN: ", type: "line", styles: () => ({ color: KLINE_COLORS.boll, style: "dashed" }) },
    ],
  };
}

/**
 * 创建系统 MACD 覆盖配置，明确 DIF/DEA 的业务配色而不依赖通用线条数组位置。
 *
 * 输入：无。
 * 输出：SYSTEM_MACD 指标覆盖对象；柱体涨跌色继续由 ``indicator.bars`` 统一控制。
 * 异常：无；由 KLineChart 处理指标不存在的情况。
 */
export function buildSystemMacdOverride(): IndicatorCreate {
  return {
    name: SYSTEM_MACD_NAME,
    calcParams: [...INDICATOR_PARAMS.macd],
    figures: [
      { key: "dif", title: "DIF: ", type: "line", styles: () => ({ color: KLINE_COLORS.dif }) },
      { key: "dea", title: "DEA: ", type: "line", styles: () => ({ color: KLINE_COLORS.dea }) },
      { key: "macd", title: "MACD: ", type: "bar", baseValue: 0, styles: ({ data }) => ({ color: ((data.current as SystemMacdValue | null)?.macd ?? 0) >= 0 ? KLINE_COLORS.up : KLINE_COLORS.down }) },
    ],
  };
}

/**
 * 将后端契约日 K 线映射成 KLineChart 10 所需字段。
 *
 * 输入：已通过前端契约校验的日 K 线列表。
 * 输出：升序的 KLineChart 本地数据，其中 ``amount`` 映射为 ``turnover``。
 * 异常：无；数值合法性已由 Zod 在请求边界完成校验。
 */
function toKlineData(bars: SectorKlineResponse["bars"]): KLineData[] {
  return bars.map((bar) => ({
    timestamp: bar.timestamp,
    open: bar.open,
    high: bar.high,
    low: bar.low,
    close: bar.close,
    volume: bar.volume,
    turnover: bar.amount,
  }));
}

/**
 * 将任意输入收敛为图表可计算的可见根数。
 *
 * 输入：调用方传入的期望根数。
 * 输出：至少为 1 的有限整数，避免除零或无穷柱间距。
 * 异常：无；非法输入降级为 1，图表仍可维持可用状态。
 */
function normalizeVisibleCount(count: number): number {
  return Number.isFinite(count) ? Math.max(1, Math.round(count)) : 1;
}

/**
 * 创建 KLineChart 10 三窗格运行时，并将数据限定为内存本地数据源。
 *
 * 输入：有效 DOM 容器、升序日 K 线、展示模式和可见根数。
 * 输出：支持尺寸变化、窗口切换和幂等释放的运行时控制器。
 * 异常：KLineChart 动态加载、初始化或指标注册失败时抛出原始异常；容器无法初始化时抛出 ``Error``。
 */
export async function createSectorKlineRuntime(options: CreateSectorKlineRuntimeOptions): Promise<SectorKlineRuntime> {
  const klinecharts = await import("klinecharts");
  await ensureSystemMacdRegistered();
  const chart = klinecharts.init(options.container, {
    locale: "zh-CN",
    timezone: "Asia/Shanghai",
    styles: buildKlineStyles(options.mode),
  });
  if (chart === null) {
    throw new Error("KLineChart 未能创建图表实例");
  }

  try {
    const data = toKlineData(options.bars);
    chart.setDataLoader({
      // 图表仅消费本次 Query 已校验的数据，禁止网络补数或实时订阅，以保证历史回放不泄漏未来 K 线。
      getBars: ({ type, callback }) => callback(type === "init" ? data : [], false),
    });
    chart.setSymbol({ ticker: "SECTOR_INDEX", pricePrecision: 4, volumePrecision: 0 });
    chart.setPeriod({ span: 1, type: "day" });
    chart.createIndicator({ name: "MA", calcParams: [...INDICATOR_PARAMS.ma], paneId: CANDLE_PANE_ID }, true);
    chart.createIndicator({ name: "BOLL", calcParams: [...INDICATOR_PARAMS.boll], paneId: CANDLE_PANE_ID }, true);
    const volumePaneId = chart.createIndicator({ name: "VOL", calcParams: [...INDICATOR_PARAMS.vol] });
    const macdPaneId = chart.createIndicator({ name: SYSTEM_MACD_NAME, calcParams: [...INDICATOR_PARAMS.macd] });
    chart.overrideYAxis({ paneId: CANDLE_PANE_ID, gap: { top: 72, bottom: 12 } });
    chart.overrideIndicator(buildMaOverride());
    chart.overrideIndicator(buildBollOverride());
    const macdValues = calculateSystemMacd(data.map((bar) => bar.close));
    const macdMaxAbs = Math.max(1, ...macdValues.flatMap((value) => [Math.abs(value.dif), Math.abs(value.dea), Math.abs(value.macd)]));
    chart.overrideIndicator({ ...buildSystemMacdOverride(), minValue: -macdMaxAbs, maxValue: macdMaxAbs });

    // 放大图给足副图高度以便读数；缩略图压缩副图，仍保留成交量和 MACD 的业务信息。
    if (volumePaneId) {
      chart.setPaneOptions({ id: volumePaneId, height: options.mode === "expanded" ? 128 : 72, minHeight: 48 });
    }
    if (macdPaneId) {
      chart.setPaneOptions({ id: macdPaneId, height: options.mode === "expanded" ? 152 : 88, minHeight: 56 });
    }
    const interactionEnabled = options.mode === "expanded";
    chart.setZoomEnabled(interactionEnabled);
    chart.setScrollEnabled(interactionEnabled);

    let disposed = false;
    let visibleCount = normalizeVisibleCount(options.visibleCount);
    const applyVisibleCount = () => {
      const size = chart.getSize(CANDLE_PANE_ID, "main");
      if (!size || size.width <= 0) return;
      chart.setBarSpace(Math.min(50, Math.max(1, size.width / visibleCount)));
      chart.scrollToRealTime(0);
    };
    applyVisibleCount();

    return {
      resize() {
        if (disposed) return;
        chart.resize();
        applyVisibleCount();
      },
      setVisibleCount(count) {
        if (disposed) return;
        visibleCount = normalizeVisibleCount(count);
        applyVisibleCount();
      },
      dispose() {
        if (disposed) return;
        disposed = true;
        klinecharts.dispose(chart);
      },
    };
  } catch (error) {
    // init 已创建 Canvas 后任一配置失败都必须立即释放，避免后续重试叠加事件监听和 DOM 资源。
    klinecharts.dispose(chart);
    throw error;
  }
}
