/** v2_short_term 标签元信息与解析工具的单元测试。 */
import { describe, expect, it } from "vitest";
import {
  INTENSITY_META,
  SHORT_TERM_LABEL_META,
  getIntensityMeta,
  getShortTermLabelMeta,
  orderLabelsByPriority,
  parseLabelsCsv,
} from "./labels";

describe("getShortTermLabelMeta", () => {
  it("返回已知标签的元信息", () => {
    const meta = getShortTermLabelMeta("pulse_up");
    expect(meta?.label).toBe("单日脉冲上涨");
    expect(meta?.color).toMatch(/^#/);
  });

  it("对未知标签返回 null", () => {
    expect(getShortTermLabelMeta("nonexistent")).toBeNull();
    expect(getShortTermLabelMeta(null)).toBeNull();
    expect(getShortTermLabelMeta(undefined)).toBeNull();
  });
});

describe("getIntensityMeta", () => {
  it("返回已知强度的元信息", () => {
    expect(getIntensityMeta("intense").label).toBe("强异动");
    expect(getIntensityMeta("moderate").label).toBe("中等异动");
    expect(getIntensityMeta("mild").label).toBe("轻度异动");
  });

  it("对未知值回退到 none", () => {
    expect(getIntensityMeta("unknown").label).toBe(INTENSITY_META.none.label);
    expect(getIntensityMeta(null).label).toBe("无异动");
  });
});

describe("parseLabelsCsv", () => {
  it("解析并去重", () => {
    expect(parseLabelsCsv("pulse_up,volume_spike,pulse_up")).toEqual(["pulse_up", "volume_spike"]);
  });
  it("空值与空串返回 []", () => {
    expect(parseLabelsCsv("")).toEqual([]);
    expect(parseLabelsCsv(null)).toEqual([]);
    expect(parseLabelsCsv(undefined)).toEqual([]);
  });
});

describe("orderLabelsByPriority", () => {
  it("按预设优先级排序", () => {
    const ordered = orderLabelsByPriority(["volume_spike", "pulse_up", "short_rebound_candidate"]);
    expect(ordered).toEqual(["pulse_up", "volume_spike", "short_rebound_candidate"]);
  });
});

describe("SHORT_TERM_LABEL_META 完整性", () => {
  it("所有 meta 项都包含 color + softColor + description", () => {
    for (const meta of Object.values(SHORT_TERM_LABEL_META)) {
      expect(meta.color).toBeTruthy();
      expect(meta.softColor).toBeTruthy();
      expect(meta.description.length).toBeGreaterThan(8);
    }
  });
});
