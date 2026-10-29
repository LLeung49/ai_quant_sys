/** 板块 K 线三窗格运行时的第三方适配与资源生命周期测试。 */
import { beforeEach, describe, expect, it, vi } from "vitest";
import type { SectorKlineResponse } from "./sectorKlineApi";

const klineMocks = vi.hoisted(() => ({
  init: vi.fn(),
  dispose: vi.fn(),
  getSupportedIndicators: vi.fn(() => ["SYSTEM_MACD"]),
  registerIndicator: vi.fn(),
  registerOverlay: vi.fn(),
}));

vi.mock("klinecharts", () => ({
  init: klineMocks.init,
  dispose: klineMocks.dispose,
  getSupportedIndicators: klineMocks.getSupportedIndicators,
  registerIndicator: klineMocks.registerIndicator,
  registerOverlay: klineMocks.registerOverlay,
}));

import {
  buildBollOverride,
  buildKlineStyles,
  buildSystemMacdOverride,
  createSectorKlineRuntime,
} from "./klinechartRuntime";
import { SYSTEM_MACD_NAME } from "./indicatorParity";

const fixtureBars: SectorKlineResponse["bars"] = [
  { trade_date: "2026-08-03", timestamp: 1785686400000, open: 10, high: 11, low: 9, close: 10.5, volume: 1000, amount: 2000 },
  { trade_date: "2026-08-04", timestamp: 1785772800000, open: 10.5, high: 12, low: 10, close: 11.5, volume: 1100, amount: 2200 },
];

function createFakeChart() {
  return {
    setDataLoader: vi.fn(), setSymbol: vi.fn(), setPeriod: vi.fn(),
    createIndicator: vi.fn((indicator: { name: string }) => indicator.name === "VOL" ? "volume_pane" : indicator.name === SYSTEM_MACD_NAME ? "macd_pane" : null),
    overrideIndicator: vi.fn(), overrideYAxis: vi.fn(), setZoomEnabled: vi.fn(), setScrollEnabled: vi.fn(),
    setPaneOptions: vi.fn(),
    getSize: vi.fn(() => ({ width: 960, height: 400, left: 0, right: 960, top: 0, bottom: 400 })),
    setBarSpace: vi.fn(), scrollToRealTime: vi.fn(), resize: vi.fn(),
    createOverlay: vi.fn(),
  };
}

describe("createSectorKlineRuntime", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    klineMocks.getSupportedIndicators.mockReturnValue([SYSTEM_MACD_NAME]);
  });

  it("创建 MA/BOLL、VOL、系统 MACD 三窗格并以本地数据加载", async () => {
    const chart = createFakeChart();
    klineMocks.init.mockReturnValue(chart);

    const runtime = await createSectorKlineRuntime({ container: document.createElement("div"), bars: fixtureBars, mode: "compact", visibleCount: 120 });

    expect(chart.setDataLoader).toHaveBeenCalledOnce();
    expect(chart.setSymbol).toHaveBeenCalledWith(expect.objectContaining({ ticker: "SECTOR_INDEX", pricePrecision: 4, volumePrecision: 0 }));
    expect(chart.setPeriod).toHaveBeenCalledWith({ span: 1, type: "day" });
    expect(chart.createIndicator).toHaveBeenCalledWith(expect.objectContaining({ name: "MA", calcParams: [5, 10, 20, 60], paneId: "candle_pane" }), true);
    expect(chart.createIndicator).toHaveBeenCalledWith(expect.objectContaining({ name: "BOLL", calcParams: [20, 2], paneId: "candle_pane" }), true);
    expect(chart.createIndicator).toHaveBeenCalledWith(expect.objectContaining({ name: "VOL", calcParams: [5, 10] }));
    expect(chart.createIndicator).toHaveBeenCalledWith(expect.objectContaining({ name: SYSTEM_MACD_NAME, calcParams: [12, 26, 9] }));
    expect(chart.setPaneOptions).toHaveBeenCalledWith(expect.objectContaining({ id: "volume_pane", height: 72 }));
    expect(chart.setPaneOptions).toHaveBeenCalledWith(expect.objectContaining({ id: "macd_pane", height: 120 }));
    expect(chart.overrideYAxis).toHaveBeenCalledWith({ paneId: "candle_pane", gap: { top: 72, bottom: 12 } });
    expect(chart.overrideIndicator).toHaveBeenCalledWith(expect.objectContaining({ name: SYSTEM_MACD_NAME, minValue: expect.any(Number), maxValue: expect.any(Number) }));
    expect(chart.setZoomEnabled).toHaveBeenCalledWith(false);
    expect(chart.setScrollEnabled).toHaveBeenCalledWith(false);

    const loader = chart.setDataLoader.mock.calls[0]?.[0];
    const callback = vi.fn();
    loader.getBars({ type: "init", callback });
    expect(callback).toHaveBeenCalledWith([
      expect.objectContaining({ timestamp: fixtureBars[0]?.timestamp, turnover: fixtureBars[0]?.amount }),
      expect.objectContaining({ timestamp: fixtureBars[1]?.timestamp, turnover: fixtureBars[1]?.amount }),
    ], false);
    loader.getBars({ type: "backward", callback });
    expect(callback).toHaveBeenLastCalledWith([], false);

    runtime.dispose();
    runtime.dispose();
    expect(klineMocks.dispose).toHaveBeenCalledOnce();
  });

  it("在主图叠加全部波段，以顶部半透明悬浮信息展示紧凑排行", async () => {
    const chart = createFakeChart();
    klineMocks.init.mockReturnValue(chart);
    const wave = { base_date: "2026-08-03", start_date: "2026-08-03", end_date: "2026-08-04",
      start_timestamp: fixtureBars[0]!.timestamp, end_timestamp: fixtureBars[1]!.timestamp,
      start_low: 9, end_high: 12, trading_days: 2, sector_change_pct: 12,
      is_confirmed: true, leaders: [
        { rank: 1, stock_code: "000001.SZ", stock_name: "甲", change_pct: 60 },
        { rank: 2, stock_code: "000002.SZ", stock_name: "乙", change_pct: 50 },
        { rank: 3, stock_code: "000003.SZ", stock_name: "丙", change_pct: 40 },
      ] };
    const runtime = await createSectorKlineRuntime({
      container: document.createElement("div"), bars: fixtureBars, mode: "expanded", visibleCount: 60,
      waves: Array.from({ length: 4 }, () => wave),
    });
    expect(klineMocks.registerOverlay).toHaveBeenCalledWith(expect.objectContaining({ name: "sectorRisingWave" }));
    expect(chart.createOverlay).toHaveBeenCalledWith(expect.objectContaining({
      name: "sectorRisingWave", paneId: "candle_pane",
      points: [{ timestamp: fixtureBars[0]!.timestamp, value: 9 }, { timestamp: fixtureBars[1]!.timestamp, value: 12 }],
      extendData: expect.objectContaining({ sector_change_pct: 12, leaders: expect.any(Array) }),
    }));
    const template = klineMocks.registerOverlay.mock.calls.at(-1)?.[0] as { createPointFigures: (params: unknown) => Array<{ type: string; attrs: { text?: string } }> };
    const overlay = chart.createOverlay.mock.calls[0]?.[0];
    expect(chart.createOverlay).toHaveBeenCalledTimes(4);
    const figures = template.createPointFigures({ coordinates: [{ x: 10, y: 250 }, { x: 80, y: 150 }], bounding: { width: 960, height: 400 }, overlay });
    expect(figures.filter((figure) => figure.type === "text").map((figure) => figure.attrs.text)).toEqual([
      "上涨波段 +12.00%", "甲", "+60.00%", "乙", "+50.00%", "丙", "+40.00%",
    ]);
    expect(figures.some((figure) => figure.type === "line")).toBe(true);
    const rects = figures.filter((figure) => figure.type === "rect") as unknown as Array<{ attrs: { y: number; height: number }; styles: { style?: string; borderColor?: string; color: string } }>;
    expect(rects).toHaveLength(2);
    const [region, label] = rects;
    expect(region.attrs).toMatchObject({ y: 178, height: 222 });
    expect(label.attrs.y + label.attrs.height).toBeLessThan(region.attrs.y);
    expect(label.attrs.y).toBe(112);
    expect(label.attrs.height).toBeLessThanOrEqual(62);
    expect(region.styles).toMatchObject({ style: "fill" });
    expect(label.styles).toMatchObject({ style: "fill" });
    expect(label.styles.color).toMatch(/^rgba\(/);
    expect(label.styles.borderColor).toBeUndefined();
    expect(chart.overrideYAxis).toHaveBeenCalledWith({ paneId: "candle_pane", gap: { top: 202, bottom: 12 } });
    expect(chart.setPaneOptions).toHaveBeenCalledWith({ id: "volume_pane", height: 110, minHeight: 48 });
    expect(chart.setPaneOptions).toHaveBeenCalledWith({ id: "macd_pane", height: 164, minHeight: 80 });
    const narrowFigures = template.createPointFigures({ coordinates: [{ x: 10, y: 250 }, { x: 80, y: 150 }], bounding: { width: 480, height: 400 }, overlay });
    const narrowLabel = narrowFigures.filter((figure) => figure.type === "rect")[1] as unknown as { attrs: { y: number; height: number } };
    expect(narrowLabel.attrs.y).toBeGreaterThan(label.attrs.y);
    expect(narrowLabel.attrs.y).toBe(144);
    expect(narrowLabel.attrs.y + narrowLabel.attrs.height).toBeLessThan(210);
    chart.getSize.mockReturnValue({ width: 480, height: 400, left: 0, right: 480, top: 0, bottom: 400 });
    runtime.resize();
    expect(chart.overrideYAxis).toHaveBeenLastCalledWith({ paneId: "candle_pane", gap: { top: 234, bottom: 12 } });
    const name = figures.find((figure) => figure.attrs.text === "甲") as { styles?: { color?: string } };
    const gain = figures.find((figure) => figure.attrs.text === "+60.00%") as unknown as { attrs: { x: number }; styles?: { color?: string } };
    expect(name.styles?.color).not.toBe(gain.styles?.color);
    const nameX = (name as { attrs: { x: number } }).attrs.x;
    expect(gain.attrs.x - nameX).toBeLessThan(24);
    expect(template.createPointFigures({ coordinates: [{ x: -200, y: 100 }, { x: -120, y: 40 }], bounding: { width: 960, height: 400 }, overlay })).toEqual([]);
  });

  it("缩略模式即使收到波段数据也不创建标注", async () => {
    const chart = createFakeChart();
    klineMocks.init.mockReturnValue(chart);
    await createSectorKlineRuntime({ container: document.createElement("div"), bars: fixtureBars, mode: "compact", visibleCount: 120,
      waves: [{ base_date: "2026-08-03", start_date: "2026-08-03", end_date: "2026-08-04", start_timestamp: fixtureBars[0]!.timestamp,
        end_timestamp: fixtureBars[1]!.timestamp, start_low: 9, end_high: 12, trading_days: 2, sector_change_pct: 12, is_confirmed: true, leaders: [] }] });
    expect(chart.createOverlay).not.toHaveBeenCalled();
  });

  it("放大模式允许缩放滚动，并在尺寸变化后按窗口数重新计算柱间距", async () => {
    const chart = createFakeChart();
    klineMocks.init.mockReturnValue(chart);
    const runtime = await createSectorKlineRuntime({ container: document.createElement("div"), bars: fixtureBars, mode: "expanded", visibleCount: 60 });

    expect(chart.setZoomEnabled).toHaveBeenCalledWith(true);
    expect(chart.setScrollEnabled).toHaveBeenCalledWith(true);
    expect(chart.setBarSpace).toHaveBeenLastCalledWith(16);
    runtime.setVisibleCount(250);
    expect(chart.setBarSpace).toHaveBeenLastCalledWith(3.84);
    runtime.resize();
    expect(chart.resize).toHaveBeenCalledOnce();
    expect(chart.scrollToRealTime).toHaveBeenCalledWith(0);
  });

  it("将 BOLL 中轨隐藏并固定 A 股涨跌与指标配色", () => {
    const bollOverride = buildBollOverride();
    const midFigure = bollOverride.figures?.find((figure) => figure.key === "mid");
    expect(bollOverride.name).toBe("BOLL");
    expect(midFigure?.styles?.({} as never)).toMatchObject({ color: "transparent" });
    const styles = buildKlineStyles("compact");
    // KLineChart 类型允许 styles 为预注册样式名称字符串；本工厂承诺返回对象，先显式缩窄再读取字段。
    if (typeof styles === "string") {
      throw new Error("板块 K 线样式必须返回局部配置对象，而非预注册样式名称");
    }
    expect(styles.candle?.bar).toMatchObject({ upColor: "#ff7285", downColor: "#37d6b0" });
    expect(styles.grid?.horizontal).toMatchObject({ color: "rgba(133, 161, 194, .14)" });
    expect(styles.grid?.vertical).toMatchObject({ color: "rgba(133, 161, 194, .12)" });
    expect(styles.candle?.priceMark?.show).toBe(false);
    expect(styles.candle?.tooltip).toMatchObject({ showRule: "always", showType: "standard" });
    expect(styles.indicator?.lastValueMark?.show).toBe(false);
    expect(styles.indicator?.tooltip).toMatchObject({ showRule: "always", showType: "standard" });
    expect(styles.indicator?.lines).toEqual(expect.arrayContaining([
      expect.objectContaining({ color: "#f0b65a" }),
      expect.objectContaining({ color: "#67a9ff" }),
      expect.objectContaining({ color: "#9a8cff" }),
      expect.objectContaining({ color: "#ff8fc7" }),
    ]));
    expect(styles.indicator?.bars).toEqual([expect.objectContaining({
      upColor: "#ff7285", downColor: "#37d6b0", noChangeColor: "#8595ae",
    })]);
    const systemMacd = buildSystemMacdOverride();
    expect(systemMacd.figures?.find((figure) => figure.key === "dif")?.styles?.({} as never)).toMatchObject({ color: "#f0b65a" });
    expect(systemMacd.figures?.find((figure) => figure.key === "dea")?.styles?.({} as never)).toMatchObject({ color: "#67a9ff" });
  });

  it("图表创建成功后配置指标失败会释放实例并继续抛出原始异常", async () => {
    const chart = createFakeChart();
    const configurationError = new Error("指标创建失败");
    chart.createIndicator.mockImplementation(() => { throw configurationError; });
    klineMocks.init.mockReturnValue(chart);

    await expect(createSectorKlineRuntime({ container: document.createElement("div"), bars: fixtureBars, mode: "compact", visibleCount: 120 }))
      .rejects.toBe(configurationError);
    expect(klineMocks.dispose).toHaveBeenCalledWith(chart);
  });
});
