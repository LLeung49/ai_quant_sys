/** 板块 K 线指标参数与 Python MACD 口径的一致性门禁测试。 */
import { describe, expect, it, vi } from "vitest";
import {
  dispose,
  getSupportedIndicators,
  init,
  type KLineData,
} from "klinecharts";
import {
  calculateSystemMacd,
  ensureSystemMacdRegistered,
  SYSTEM_MACD_NAME,
} from "./indicatorParity";
import {
  INDICATOR_PARAMS,
  KLINE_COLORS,
  KLINE_WINDOWS,
} from "./sectorKlineConfig";

/** 由 pandas ``ewm(span=n, adjust=False)`` 预先计算并固化的末三项口径。 */
const PYTHON_MACD_TAIL = {
  dif: [1.2699075437491558, 1.1991115788507614, 1.1778428134306438],
  dea: [1.2792604654824336, 1.263230688156099, 1.2461531132110082],
  hist: [-0.01870584346655546, -0.12823821861067541, -0.1366205995607288],
} as const;

/** 输入：固定的非线性收盘价序列；输出：用于口径比较的收盘价数组。 */
function createCloses(): number[] {
  return Array.from({ length: 80 }, (_, index) => 100 + index * 0.18 + ((index % 7) - 3) * 0.42);
}

/** 输入：数值序列与期望值；输出：断言所有同位置数值的绝对误差不超过 ``1e-10``。 */
function expectCloseTo(actual: readonly number[], expected: readonly number[]): void {
  expect(actual).toHaveLength(expected.length);
  actual.forEach((value, index) => {
    expect(Math.abs(value - expected[index]!)).toBeLessThan(1e-10);
  });
}

describe("板块 K 线指标口径", () => {
  it("以 Python adjust=False 的 12/26/9 和 HIST×2 计算系统 MACD", () => {
    const result = calculateSystemMacd(createCloses());
    const tail = result.slice(-3);

    expectCloseTo(tail.map((item) => item.dif), PYTHON_MACD_TAIL.dif);
    expectCloseTo(tail.map((item) => item.dea), PYTHON_MACD_TAIL.dea);
    expectCloseTo(tail.map((item) => item.macd), PYTHON_MACD_TAIL.hist);
    expect(SYSTEM_MACD_NAME).toBe("SYSTEM_MACD");
  });

  it("确认 KLineChart 10 内置 MACD 存在，但系统采用已验证的薄适配器", () => {
    expect(getSupportedIndicators()).toContain("MACD");
    expect(SYSTEM_MACD_NAME).toBe("SYSTEM_MACD");
  });

  it("幂等注册系统 MACD，并拒绝无效收盘价和周期参数", () => {
    ensureSystemMacdRegistered();
    ensureSystemMacdRegistered();

    expect(getSupportedIndicators().filter((name) => name === SYSTEM_MACD_NAME)).toHaveLength(1);
    expect(() => calculateSystemMacd([100, Number.NaN])).toThrow(RangeError);
    expect(() => calculateSystemMacd([100, 101], 26, 12, 9)).toThrow(RangeError);
  });

  it("通过真实 KLineChart API 验证系统 MACD 精确对齐 Python，内置 MACD 三项均有初始化差异", async () => {
    // JSDOM 不提供 Canvas 2D；此处只补齐 KLineChart 初始化和取指标所需的无副作用绘图接口。
    const canvasContext = new Proxy({
      measureText: () => ({ width: 0 }),
      getImageData: () => ({ data: [] }),
    }, {
      get(target, property) {
        return Reflect.get(target, property) ?? (() => undefined);
      },
    }) as unknown as CanvasRenderingContext2D;
    const getContextSpy = vi.spyOn(HTMLCanvasElement.prototype, "getContext").mockReturnValue(canvasContext);
    vi.stubGlobal("ResizeObserver", class {
      observe(): void {}
      disconnect(): void {}
      unobserve(): void {}
    });
    const host = document.createElement("div");
    Object.defineProperties(host, {
      clientWidth: { value: 720 },
      clientHeight: { value: 480 },
    });
    document.body.append(host);
    let chart: ReturnType<typeof init> = null;
    try {
      chart = init(host);

      expect(chart).not.toBeNull();
      ensureSystemMacdRegistered();
      chart?.createIndicator("MACD");
      chart?.createIndicator(SYSTEM_MACD_NAME);
      const builtin = chart?.getIndicators({ name: "MACD" })[0];
      const adapter = chart?.getIndicators({ name: SYSTEM_MACD_NAME })[0];
      const bars: KLineData[] = createCloses().map((close, index) => ({
        timestamp: index + 1,
        open: close,
        high: close,
        low: close,
        close,
      }));

      expect(builtin).toBeDefined();
      expect(adapter).toBeDefined();
      if (!builtin || !adapter) {
        throw new Error("KLineChart 未能创建内置或系统 MACD 指标");
      }
      const builtinResult = await builtin.calc(bars, builtin);
      const adapterResult = await adapter.calc(bars, adapter);
      const builtinTail = builtinResult.slice(-3) as Array<Record<string, number>>;
      const adapterTail = adapterResult.slice(-3) as Array<Record<string, number>>;

      expect(builtinTail).toHaveLength(3);
      expect(adapterTail).toHaveLength(3);
      expectCloseTo(adapterTail.map((item) => item.dif), PYTHON_MACD_TAIL.dif);
      expectCloseTo(adapterTail.map((item) => item.dea), PYTHON_MACD_TAIL.dea);
      expectCloseTo(adapterTail.map((item) => item.macd), PYTHON_MACD_TAIL.hist);
      // 内置 MACD 从各周期 SMA 预热，系统 MACD 则从首个 DIF 以 adjust=False 递推，三列都必须保留差异证据。
      expect(builtinTail.map((item) => item.dif)).not.toEqual(PYTHON_MACD_TAIL.dif);
      expect(builtinTail.map((item) => item.dea)).not.toEqual(PYTHON_MACD_TAIL.dea);
      expect(builtinTail.map((item) => item.macd)).not.toEqual(PYTHON_MACD_TAIL.hist);
    } finally {
      if (chart) {
        dispose(chart);
      }
      host.remove();
      getContextSpy.mockRestore();
      vi.unstubAllGlobals();
    }
  });

  it("集中锁定 MA、BOLL、VOL、MACD 参数、窗口与 A 股配色", () => {
    expect(INDICATOR_PARAMS).toEqual({
      ma: [5, 10, 20, 60],
      boll: [20, 2],
      vol: [5, 10],
      macd: [12, 26, 9],
    });
    expect(KLINE_WINDOWS).toEqual([60, 120, 250]);
    expect(KLINE_COLORS).toMatchObject({
      up: "#ff7285",
      down: "#37d6b0",
      dif: "#f0b65a",
      dea: "#67a9ff",
    });
  });
});
