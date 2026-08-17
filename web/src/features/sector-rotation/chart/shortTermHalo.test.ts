/** shortTermHalo 纯函数模块的单元测试。 */

import { describe, expect, it } from "vitest";
import {
  SHORT_TERM_CHIP_TEXT,
  SHORT_TERM_GLYPH_BORDER,
  SHORT_TERM_GLYPH_BORDER_WIDTH,
  SHORT_TERM_GLYPH_INTENSITY_SCALE,
  SHORT_TERM_GLYPH_PATHS,
  SHORT_TERM_HALO_STYLE,
  SHORT_TERM_LABEL_DIRECTION_COLOR,
  buildShortTermHaloIndex,
  buildShortTermHaloInfo,
  getShortTermChipText,
  getShortTermDirectionColor,
  getShortTermGlyphBaseSize,
  getShortTermGlyphColor,
  getShortTermGlyphColorByIntensity,
  getShortTermGlyphOffset,
  getShortTermGlyphPath,
  getShortTermGlyphShadowBlur,
  getShortTermGlyphSize,
  getShortTermHaloStyle,
  getShortTermIntensityLabel,
  normalizeShortTermIntensity,
  pickPrimaryShortTermLabel,
} from "./shortTermHalo";

describe("pickPrimaryShortTermLabel", () => {
  it("按照 chip 优先级顺序选择首个命中标签", () => {
    expect(pickPrimaryShortTermLabel(["volume_spike", "pulse_up", "limit_cluster"])).toBe("pulse_up");
    expect(pickPrimaryShortTermLabel(["limit_cluster", "short_rebound_candidate"])).toBe("limit_cluster");
    expect(pickPrimaryShortTermLabel(["short_breakdown_candidate", "short_rebound_candidate"])).toBe(
      "short_rebound_candidate",
    );
  });

  it("空数组与全无匹配时返回 null", () => {
    expect(pickPrimaryShortTermLabel([])).toBeNull();
    expect(pickPrimaryShortTermLabel(["unknown_label"])).toBeNull();
  });
});

describe("normalizeShortTermIntensity", () => {
  it("仅识别 SHORT_TERM_HALO_STYLE 已知的三个强度档位", () => {
    expect(normalizeShortTermIntensity("intense")).toBe("intense");
    expect(normalizeShortTermIntensity("moderate")).toBe("moderate");
    expect(normalizeShortTermIntensity("mild")).toBe("mild");
  });

  it("将未知值与空值规范化为 null", () => {
    expect(normalizeShortTermIntensity("none")).toBeNull();
    expect(normalizeShortTermIntensity("")).toBeNull();
    expect(normalizeShortTermIntensity("ultra_intense")).toBeNull();
    expect(normalizeShortTermIntensity(null)).toBeNull();
    expect(normalizeShortTermIntensity(undefined)).toBeNull();
  });
});

describe("buildShortTermHaloInfo", () => {
  it("score_eligible 为 false / 0 时不展示光晕", () => {
    expect(buildShortTermHaloInfo({ score_eligible: false, short_term_intensity: "intense", short_term_labels: "pulse_up" })).toEqual({
      intensity: null,
      primaryLabel: null,
      allLabels: [],
      isAnomaly: false,
    });
    expect(buildShortTermHaloInfo({ score_eligible: 0 })).toEqual({
      intensity: null,
      primaryLabel: null,
      allLabels: [],
      isAnomaly: false,
    });
  });

  it("score_eligible 缺失时,根据强度档位或标签决定 isAnomaly", () => {
    expect(buildShortTermHaloInfo({ short_term_intensity: "intense" })).toMatchObject({ intensity: "intense", primaryLabel: null, allLabels: [], isAnomaly: true });
    expect(
      buildShortTermHaloInfo({ short_term_labels: "short_rebound_candidate" }),
    ).toMatchObject({ intensity: null, primaryLabel: "short_rebound_candidate", isAnomaly: true });
    expect(
      buildShortTermHaloInfo({ short_term_labels: "" }),
    ).toMatchObject({ intensity: null, primaryLabel: null, isAnomaly: false });
  });

  it("主标签选择遵守 chip 优先级顺序", () => {
    const info = buildShortTermHaloInfo({
      score_eligible: true,
      short_term_intensity: "moderate",
      short_term_labels: "volume_spike,short_rebound_candidate,pulse_up",
    });
    expect(info.allLabels).toEqual(["volume_spike", "short_rebound_candidate", "pulse_up"]);
    expect(info.primaryLabel).toBe("pulse_up");
    expect(info.intensity).toBe("moderate");
    expect(info.isAnomaly).toBe(true);
  });

  it("CSV 中重复出现不影响去重保序", () => {
    const info = buildShortTermHaloInfo({
      score_eligible: true,
      short_term_intensity: "mild",
      short_term_labels: "pulse_up,volume_spike,pulse_up",
    });
    expect(info.allLabels).toEqual(["pulse_up", "volume_spike"]);
  });
});

describe("buildShortTermHaloIndex", () => {
  it("按 sector_name 索引出所有光晕信息,且空列表返回空 map", () => {
    const map = buildShortTermHaloIndex([
      { sector_name: "半导体", short_term_intensity: "intense", short_term_labels: "pulse_up" },
      { sector_name: "银行", short_term_intensity: "mild", short_term_labels: "limit_cluster" },
    ] as Array<{ sector_name: string; short_term_intensity: string; short_term_labels: string }>);
    expect(map.size).toBe(2);
    expect(map.get("半导体")?.primaryLabel).toBe("pulse_up");
    expect(map.get("银行")?.primaryLabel).toBe("limit_cluster");
    expect(buildShortTermHaloIndex([])).toEqual(new Map());
  });
});

describe("getShortTermChipText / SHORT_TERM_CHIP_TEXT", () => {
  it("所有 chip 文本字段均不为空字符串", () => {
    for (const text of Object.values(SHORT_TERM_CHIP_TEXT)) {
      expect(text.length).toBeGreaterThan(0);
      expect(text.length).toBeLessThanOrEqual(4);
    }
  });

  it("命中已知标签时返回短码,未知标签回退到 id 原文", () => {
    expect(getShortTermChipText("pulse_up")).toBe("脉冲↑");
    expect(getShortTermChipText("limit_cluster")).toBe("涨停");
    expect(getShortTermChipText("unknown_label")).toBe("unknown_label");
    expect(getShortTermChipText(null)).toBeNull();
    expect(getShortTermChipText(undefined)).toBeNull();
  });
});

describe("SHORT_TERM_HALO_STYLE / getShortTermHaloStyle", () => {
  it("P2.2 后 SHORT_TERM_HALO_STYLE 只包含 color 字段", () => {
    expect(Object.keys(SHORT_TERM_HALO_STYLE.intense)).toEqual(["color"]);
    expect(Object.keys(SHORT_TERM_HALO_STYLE.moderate)).toEqual(["color"]);
    expect(Object.keys(SHORT_TERM_HALO_STYLE.mild)).toEqual(["color"]);
  });

  it("三档强度色为 6 位 hex,与 INTENSITY_META 对齐", () => {
    expect(SHORT_TERM_HALO_STYLE.intense.color).toBe("#ef5350");
    expect(SHORT_TERM_HALO_STYLE.moderate.color).toBe("#f0b65a");
    expect(SHORT_TERM_HALO_STYLE.mild.color).toBe("#67c3a2");
  });

  it("getShortTermHaloStyle 仅在已知三档返回样式,null 与 unknown 一律 null", () => {
    expect(getShortTermHaloStyle("intense")?.color).toBe(SHORT_TERM_HALO_STYLE.intense.color);
    expect(getShortTermHaloStyle(null)).toBeNull();
    expect(getShortTermHaloStyle(undefined)).toBeNull();
  });
});

describe("getShortTermIntensityLabel", () => {
  it("返回 getIntensityMeta 的中文化 label,未提供强度时为无异动", () => {
    expect(getShortTermIntensityLabel("intense")).toBe("强异动");
    expect(getShortTermIntensityLabel("moderate")).toBe("中等异动");
    expect(getShortTermIntensityLabel("mild")).toBe("轻度异动");
    expect(getShortTermIntensityLabel(null)).toBe("无异动");
    expect(getShortTermIntensityLabel(undefined)).toBe("无异动");
  });
});

describe("SHORT_TERM_GLYPH_PATHS 完整性", () => {
  it("P2.2 后仍覆盖 13 条路径:pulse_up / pulse_down 各 3 档 + 7 个固定标签", () => {
    const keys = Object.keys(SHORT_TERM_GLYPH_PATHS);
    expect(keys.length).toBe(13);
    for (const label of [
      "pulse_up_intense",
      "pulse_up_moderate",
      "pulse_up_mild",
      "pulse_down_intense",
      "pulse_down_moderate",
      "pulse_down_mild",
      "extreme_up",
      "extreme_down",
      "volume_spike",
      "limit_cluster",
      "limit_panic",
      "short_rebound_candidate",
      "short_breakdown_candidate",
    ]) {
      expect(keys).toContain(label);
    }
  });

  it("rebound / breakdown 由两个 sub-path 组成(三角 + 同侧方块),M 数量为 2", () => {
    const rebound = SHORT_TERM_GLYPH_PATHS.short_rebound_candidate;
    expect((rebound.match(/M/g) || []).length).toBe(2);
    const breakdown = SHORT_TERM_GLYPH_PATHS.short_breakdown_candidate;
    expect((breakdown.match(/M/g) || []).length).toBe(2);
  });

  it("每条路径都是合法 SVG path(M / L / H / V / Z 字符,且不空)", () => {
    for (const [label, path] of Object.entries(SHORT_TERM_GLYPH_PATHS)) {
      expect(path.length, label).toBeGreaterThan(0);
      expect(/^[MLHVZ0-9.,\s-]+$/i.test(path), label).toBe(true);
    }
  });
});

describe("getShortTermGlyphPath", () => {
  it("pulse_up / pulse_down 在三档 intensity 下分别选择尖锐 / 中等 / 扁三角", () => {
    const intenseUp = getShortTermGlyphPath("pulse_up", "intense");
    const mildUp = getShortTermGlyphPath("pulse_up", "mild");
    expect(intenseUp).toBe(SHORT_TERM_GLYPH_PATHS.pulse_up_intense);
    expect(mildUp).toBe(SHORT_TERM_GLYPH_PATHS.pulse_up_mild);
    const upHeight = (path: string): number => {
      const m = path.match(/^M(\d+),(\d+)/);
      const baseM = path.match(/L(\d+),(\d+) L(\d+),(\d+) Z$/);
      if (!m || !baseM) return 0;
      const apexY = Number(m[2]);
      const baseY = Number(baseM[4]);
      const baseLeftX = Number(baseM[1]);
      const baseRightX = Number(baseM[3]);
      return (baseY - apexY) / Math.max(1, Math.abs(baseRightX - baseLeftX));
    };
    expect(upHeight(intenseUp)).toBeGreaterThan(upHeight(mildUp));
  });

  it("非 pulse 标签固定路径,不随 intensity 变化", () => {
    expect(getShortTermGlyphPath("extreme_up", "intense")).toBe(SHORT_TERM_GLYPH_PATHS.extreme_up);
    expect(getShortTermGlyphPath("extreme_up", "mild")).toBe(SHORT_TERM_GLYPH_PATHS.extreme_up);
    expect(getShortTermGlyphPath("limit_cluster", "intense")).toBe(SHORT_TERM_GLYPH_PATHS.limit_cluster);
    expect(getShortTermGlyphPath("short_rebound_candidate", "intense")).toBe(SHORT_TERM_GLYPH_PATHS.short_rebound_candidate);
  });

  it("未知 label 回退到 pulse_up_mild,保证 Layer C 始终有形状可绘制", () => {
    expect(getShortTermGlyphPath("bogus_label", "intense")).toBe(SHORT_TERM_GLYPH_PATHS.pulse_up_mild);
    expect(getShortTermGlyphPath("", "moderate")).toBe(SHORT_TERM_GLYPH_PATHS.pulse_up_mild);
  });
});

describe("getShortTermGlyphBaseSize", () => {
  it("volume_spike 使用更窄的垂直尺寸,呼应成交量立柱视觉语言", () => {
    expect(getShortTermGlyphBaseSize("volume_spike")).toEqual([6, 13]);
  });

  it("limit_cluster / limit_panic 等 W/M 形状使用等比例尺寸", () => {
    expect(getShortTermGlyphBaseSize("limit_cluster")).toEqual([14, 12]);
    expect(getShortTermGlyphBaseSize("limit_panic")).toEqual([14, 12]);
  });

  it("extreme_up / extreme_down 相对 pulse_up 更窄更长", () => {
    const pulseDims = getShortTermGlyphBaseSize("pulse_up");
    const extremeDims = getShortTermGlyphBaseSize("extreme_up");
    expect(pulseDims[0]).toBeGreaterThan(extremeDims[0]);
    expect(pulseDims[1]).toBeLessThan(extremeDims[1]);
  });
});

describe("getShortTermGlyphSize", () => {
  it("pulse_up / pulse_down 直接返回基础尺寸,intensity 由 path 尖锐度承载", () => {
    expect(getShortTermGlyphSize("pulse_up", "intense")).toEqual([12, 13]);
    expect(getShortTermGlyphSize("pulse_up", "mild")).toEqual([12, 13]);
    expect(getShortTermGlyphSize("pulse_down", "moderate")).toEqual([12, 13]);
  });

  it("非 pulse 标签按 intensity 缩放面积,intense > moderate > mild", () => {
    const intense = getShortTermGlyphSize("limit_cluster", "intense");
    const moderate = getShortTermGlyphSize("limit_cluster", "moderate");
    const mild = getShortTermGlyphSize("limit_cluster", "mild");
    expect(intense[0] * intense[1]).toBeGreaterThan(moderate[0] * moderate[1]);
    expect(moderate[0] * moderate[1]).toBeGreaterThan(mild[0] * mild[1]);
  });

  it("缩放系数 INTENSITY_SCALE 单调下降,intense=1.10,mild=0.80", () => {
    expect(SHORT_TERM_GLYPH_INTENSITY_SCALE.intense).toBeGreaterThan(SHORT_TERM_GLYPH_INTENSITY_SCALE.moderate);
    expect(SHORT_TERM_GLYPH_INTENSITY_SCALE.moderate).toBeGreaterThan(SHORT_TERM_GLYPH_INTENSITY_SCALE.mild);
    expect(SHORT_TERM_GLYPH_INTENSITY_SCALE.intense).toBeCloseTo(1.10, 5);
    expect(SHORT_TERM_GLYPH_INTENSITY_SCALE.mild).toBeCloseTo(0.80, 5);
  });

  it("unknown label 返回 mild 缩放后的 pulse 家族尺寸,不抛出", () => {
    expect(getShortTermGlyphSize("unknown_label", "mild")).toEqual([10, 10]);
  });

  it("最小尺寸护栏 6px,即使 mild 缩放后也不会太小", () => {
    const [w, h] = getShortTermGlyphSize("volume_spike", "mild");
    expect(w).toBeGreaterThanOrEqual(6);
    expect(h).toBeGreaterThanOrEqual(6);
  });
});

describe("getShortTermGlyphShadowBlur", () => {
  it("三档强度的 shadowBlur 单调递减,intense=8 / moderate=6 / mild=4", () => {
    expect(getShortTermGlyphShadowBlur("intense")).toBe(8);
    expect(getShortTermGlyphShadowBlur("moderate")).toBe(6);
    expect(getShortTermGlyphShadowBlur("mild")).toBe(4);
    expect(getShortTermGlyphShadowBlur("intense")).toBeGreaterThan(getShortTermGlyphShadowBlur("moderate"));
    expect(getShortTermGlyphShadowBlur("moderate")).toBeGreaterThan(getShortTermGlyphShadowBlur("mild"));
  });
});

describe("getShortTermGlyphColor / getShortTermDirectionColor", () => {
  it("pulse_up / pulse_down 等涨/跌主标签走对应方向色,intensity 仅调整 alpha", () => {
    const pulseUpIntense = getShortTermGlyphColor("pulse_up", "intense");
    const pulseUpMild = getShortTermGlyphColor("pulse_up", "mild");
    // 同主标签的颜色 base rgb 一致,只在 alpha 上有别
    expect(pulseUpIntense).toMatch(/^rgba\(239, 83, 80, 1\)$/);
    expect(pulseUpMild).toMatch(/^rgba\(239, 83, 80, 0\.66\)$/);
    // pulse_down 与 pulse_up 必须不同色调
    expect(getShortTermGlyphColor("pulse_down", "intense")).toMatch(/^rgba\(38, 166, 154,/);
  });

  it("中间量能 / 反弹 / 破位三类标签走各自专属方向色", () => {
    expect(getShortTermGlyphColor("volume_spike", "intense")).toMatch(/^rgba\(240, 182, 90,/);
    expect(getShortTermGlyphColor("short_rebound_candidate", "intense")).toMatch(/^rgba\(103, 169, 255,/);
    expect(getShortTermGlyphColor("short_breakdown_candidate", "intense")).toMatch(/^rgba\(145, 133, 255,/);
  });

  it("未知主标签走中性灰而非误用其它方向色", () => {
    expect(getShortTermDirectionColor("not_a_label")).toBe("#8795ab");
    expect(getShortTermGlyphColor("not_a_label", "moderate")).toMatch(/^rgba\(135, 149, 171, 0\.86\)$/);
  });

  it("getShortTermGlyphColorByIntensity 走中性色 + intensity alpha,用于 strip 空 cell 等无主标签场景", () => {
    expect(getShortTermGlyphColorByIntensity("intense")).toMatch(/^rgba\(135, 149, 171, 1\)$/);
    expect(getShortTermGlyphColorByIntensity("mild")).toMatch(/^rgba\(135, 149, 171, 0\.66\)$/);
  });
});

describe("getShortTermGlyphOffset", () => {
  it("dx 跟随 bubbleRadius + 2 像素", () => {
    expect(getShortTermGlyphOffset("pulse_up", 12)).toEqual([14, -9.8]);
  });

  it("bubbleRadius 越大,形状越远离气泡中心(保持视觉间距稳定)", () => {
    const small = getShortTermGlyphOffset("pulse_up", 12);
    const big = getShortTermGlyphOffset("pulse_up", 30);
    expect(small[0]).toBeLessThan(big[0]);
    expect(small[1]).toBeGreaterThan(big[1]);
  });

  it("统一返回稳定的右上方向偏移,所有主标签使用同一策略", () => {
    const a = getShortTermGlyphOffset("pulse_up", 12);
    const b = getShortTermGlyphOffset("limit_cluster", 12);
    const c = getShortTermGlyphOffset("volume_spike", 12);
    expect(a[0]).toBe(b[0]);
    expect(a[1]).toBe(b[1]);
    expect(a[0]).toBe(c[0]);
  });
});

describe("SHORT_TERM_GLYPH_BORDER / BORDER_WIDTH 一致性", () => {
  it("描边色固定为深色半透明,与 phase 色面形成可读衬底", () => {
    expect(SHORT_TERM_GLYPH_BORDER).toMatch(/^rgba/);
  });
  it("描边宽度 1.2 像素,小于 halo 描边且大于 0", () => {
    expect(SHORT_TERM_GLYPH_BORDER_WIDTH).toBeGreaterThan(0.6);
    expect(SHORT_TERM_GLYPH_BORDER_WIDTH).toBeLessThan(3);
  });
});