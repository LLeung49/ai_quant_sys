/** shortTermStrip 纯函数模块的单元测试。 */

import { describe, expect, it } from "vitest";
import {
  STRIP_WINDOW_DAYS,
  buildShortTermStripRow,
  describeStripCell,
  normalizeStripIntensity,
  type StripCell,
} from "./shortTermStrip";
import type { ShortTermHistoryResponse } from "../short_term/api";

function makePoint(overrides: Record<string, unknown> = {}) {
  return {
    sector_name: "半导体",
    score_eligible: true,
    short_term_intensity: null,
    short_term_labels: null,
    short_term_composite: null,
    ret_1: null,
    rs_1: null,
    rvol_1_20: null,
    as_of_date: "2026-08-11",
    ...overrides,
  };
}

const baseHistory: ShortTermHistoryResponse = {
  sector_level: 2,
  model_version: "v2_short_term",
  meta: {
    run_status: "succeeded",
    field_version: "v2_short_term",
    source_max_trade_date: "2026-08-11",
    eligible_sector_count: 30,
    skipped_sector_count: 0,
    pulse_up_count: 0,
    volume_spike_count: 0,
    limit_cluster_count: 0,
    limit_panic_count: 0,
  },
  points: [],
};

describe("STRIP_WINDOW_DAYS", () => {
  it("默认 5 个交易日", () => {
    expect(STRIP_WINDOW_DAYS).toBe(5);
  });
});

describe("normalizeStripIntensity", () => {
  it("识别三档已知值", () => {
    expect(normalizeStripIntensity("intense")).toBe("intense");
    expect(normalizeStripIntensity("moderate")).toBe("moderate");
    expect(normalizeStripIntensity("mild")).toBe("mild");
  });
  it("none / 空 / 未知值都归一为 null", () => {
    expect(normalizeStripIntensity("none")).toBeNull();
    expect(normalizeStripIntensity("")).toBeNull();
    expect(normalizeStripIntensity(null)).toBeNull();
    expect(normalizeStripIntensity(undefined)).toBeNull();
    expect(normalizeStripIntensity("ultra_intense")).toBeNull();
    expect(normalizeStripIntensity(42)).toBeNull();
  });
});

describe("buildShortTermStripRow", () => {
  it("history 为 null 时返回空数组", () => {
    expect(buildShortTermStripRow(null, "半导体", "2026-08-11")).toEqual([]);
  });

  it("sectorName 为空时返回空数组", () => {
    expect(buildShortTermStripRow(baseHistory, "", "2026-08-11")).toEqual([]);
  });

  it("sectorName 不在 points 中时返回空数组", () => {
    const history: ShortTermHistoryResponse = {
      ...baseHistory,
      points: [makePoint({ sector_name: "银行", as_of_date: "2026-08-11" })],
    };
    expect(buildShortTermStripRow(history, "半导体", "2026-08-11")).toEqual([]);
  });

  it("按 as_of_date desc 取前 days 条;asOfDate 早于历史最近日仍按 desc 取 days", () => {
    const history: ShortTermHistoryResponse = {
      ...baseHistory,
      points: [
        makePoint({ as_of_date: "2026-08-07" }),
        makePoint({ as_of_date: "2026-08-11" }),
        makePoint({ as_of_date: "2026-08-10" }),
        makePoint({ as_of_date: "2026-08-09" }),
        makePoint({ as_of_date: "2026-08-08" }),
        makePoint({ as_of_date: "2026-08-06" }),
      ],
    };
    const rows = buildShortTermStripRow(history, "半导体", "2026-08-05", 5);
    expect(rows.map((r) => r.as_of_date)).toEqual([
      "2026-08-11",
      "2026-08-10",
      "2026-08-09",
      "2026-08-08",
      "2026-08-07",
    ]);
  });

  it("实际历史 < days 时返回实际天数", () => {
    const history: ShortTermHistoryResponse = {
      ...baseHistory,
      points: [
        makePoint({ as_of_date: "2026-08-11" }),
        makePoint({ as_of_date: "2026-08-10" }),
      ],
    };
    const rows = buildShortTermStripRow(history, "半导体", "2026-08-11", 5);
    expect(rows).toHaveLength(2);
    expect(rows.map((r) => r.as_of_date)).toEqual(["2026-08-11", "2026-08-10"]);
  });

  it("primaryLabel 按 SHORT_TERM_LABEL_PRIORITY 顺序,首条命中即返回", () => {
    const history: ShortTermHistoryResponse = {
      ...baseHistory,
      points: [
        makePoint({ as_of_date: "2026-08-11", short_term_labels: "volume_spike,pulse_up,limit_cluster" }),
      ],
    };
    const rows = buildShortTermStripRow(history, "半导体", "2026-08-11");
    expect(rows[0]?.primaryLabel).toBe("pulse_up");
    expect(rows[0]?.labels).toEqual(["volume_spike", "pulse_up", "limit_cluster"]);
  });

  it("intensity 归一化:none / 未知值 / 空 全部为 null", () => {
    const history: ShortTermHistoryResponse = {
      ...baseHistory,
      points: [
        makePoint({ as_of_date: "2026-08-11", short_term_intensity: "intense" }),
        makePoint({ as_of_date: "2026-08-10", short_term_intensity: "moderate" }),
        makePoint({ as_of_date: "2026-08-09", short_term_intensity: "mild" }),
        makePoint({ as_of_date: "2026-08-08", short_term_intensity: "none" }),
        makePoint({ as_of_date: "2026-08-07", short_term_intensity: "unknown_value" }),
        makePoint({ as_of_date: "2026-08-06", short_term_intensity: "" }),
      ],
    };
    // 默认窗口 5 个交易日,只取最近 5 个
    const rows = buildShortTermStripRow(history, "半导体", "2026-08-11");
    expect(rows.map((r) => r.intensity)).toEqual([
      "intense",
      "moderate",
      "mild",
      null,
      null,
    ]);
  });

  it("intensity 归一化:窗口放大到 7 时返回 7 行", () => {
    const history: ShortTermHistoryResponse = {
      ...baseHistory,
      points: [
        makePoint({ as_of_date: "2026-08-11", short_term_intensity: "intense" }),
        makePoint({ as_of_date: "2026-08-10", short_term_intensity: "moderate" }),
        makePoint({ as_of_date: "2026-08-09", short_term_intensity: "mild" }),
        makePoint({ as_of_date: "2026-08-08", short_term_intensity: "none" }),
        makePoint({ as_of_date: "2026-08-07", short_term_intensity: "unknown_value" }),
        makePoint({ as_of_date: "2026-08-06", short_term_intensity: "" }),
      ],
    };
    const rows = buildShortTermStripRow(history, "半导体", "2026-08-11", 7);
    expect(rows.map((r) => r.intensity)).toEqual([
      "intense",
      "moderate",
      "mild",
      null,
      null,
      null,
    ]);
  });

  it("labels 是去重保序数组,空字符串或 null 返回 []", () => {
    const history: ShortTermHistoryResponse = {
      ...baseHistory,
      points: [
        makePoint({ as_of_date: "2026-08-11", short_term_labels: "pulse_up,volume_spike,pulse_up" }),
        makePoint({ as_of_date: "2026-08-10", short_term_labels: "" }),
        makePoint({ as_of_date: "2026-08-09", short_term_labels: null }),
      ],
    };
    const rows = buildShortTermStripRow(history, "半导体", "2026-08-11");
    expect(rows[0]?.labels).toEqual(["pulse_up", "volume_spike"]);
    expect(rows[1]?.labels).toEqual([]);
    expect(rows[2]?.labels).toEqual([]);
  });

  it("ret_1 / rs_1 / rvol_1_20 透传 strip cell", () => {
    const history: ShortTermHistoryResponse = {
      ...baseHistory,
      points: [
        makePoint({ as_of_date: "2026-08-11", ret_1: 0.012, rs_1: 0.005, rvol_1_20: 1.85 }),
      ],
    };
    const rows = buildShortTermStripRow(history, "半导体", "2026-08-11");
    expect(rows[0]?.ret_1).toBeCloseTo(0.012);
    expect(rows[0]?.rs_1).toBeCloseTo(0.005);
    expect(rows[0]?.rvol_1_20).toBeCloseTo(1.85);
  });

  it("composite 透传", () => {
    const history: ShortTermHistoryResponse = {
      ...baseHistory,
      points: [
        makePoint({ as_of_date: "2026-08-11", short_term_composite: 0.85 }),
      ],
    };
    const rows = buildShortTermStripRow(history, "半导体", "2026-08-11");
    expect(rows[0]?.composite).toBe(0.85);
  });

  it("其它 sector 的 point 不污染目标 sector 的 strip", () => {
    const history: ShortTermHistoryResponse = {
      ...baseHistory,
      points: [
        makePoint({ sector_name: "银行", as_of_date: "2026-08-11", short_term_intensity: "intense" }),
        makePoint({ sector_name: "半导体", as_of_date: "2026-08-11", short_term_intensity: "mild" }),
      ],
    };
    const rows = buildShortTermStripRow(history, "半导体", "2026-08-11");
    expect(rows).toHaveLength(1);
    expect(rows[0]?.intensity).toBe("mild");
  });
});

describe("describeStripCell", () => {
  it("返回 ret_1 / rs_1 / rvol_1_20 与 labels 拷贝", () => {
    const cell: StripCell = {
      as_of_date: "2026-08-11",
      primaryLabel: "pulse_up",
      intensity: "intense",
      composite: 0.85,
      labels: ["pulse_up", "volume_spike"],
      ret_1: 0.012,
      rs_1: 0.005,
      rvol_1_20: 1.85,
    };
    const desc = describeStripCell(cell);
    expect(desc.ret_1).toBe(0.012);
    expect(desc.rs_1).toBe(0.005);
    expect(desc.rvol_1_20).toBe(1.85);
    expect(desc.labels).toEqual(["pulse_up", "volume_spike"]);
  });

  it("labels 是新数组引用,修改返回值不影响原 cell", () => {
    const cell: StripCell = {
      as_of_date: "2026-08-11",
      primaryLabel: "pulse_up",
      intensity: "intense",
      composite: 0.85,
      labels: ["pulse_up"],
      ret_1: null,
      rs_1: null,
      rvol_1_20: null,
    };
    const desc = describeStripCell(cell);
    desc.labels.push("new_label");
    expect(cell.labels).toEqual(["pulse_up"]);
  });
});