/** 象限图数据编码的纯函数测试。 */
import { describe, expect, it } from "vitest";
import { buildQuadrantOption } from "./quadrantOption";
import {
  buildShortTermHaloIndex,
  SHORT_TERM_GLYPH_PATHS,
  SHORT_TERM_HALO_STYLE,
  type ShortTermHaloInfo,
} from "./shortTermHalo";

describe("buildQuadrantOption", () => {
  it("Lifecycle 不改变气泡的 Phase 颜色,并在 tooltip 展示状态、持续时间与原因", () => {
    const baseSector = { sector_name: "半导体", velocity_score: .4, acceleration_score: .2, volume_score: .3, participation_score: .5, phase_confirmed: "accel_up", phase_confidence: .8, composite_rank: 1 };
    const trending = buildQuadrantOption([{ ...baseSector, lifecycle_state: "trending" }]);
    const exit = buildQuadrantOption([{ ...baseSector, lifecycle_state: "exit", lifecycle_age: 6, lifecycle_changed: true, lifecycle_reason: "phase_accel_down" }]);
    const data = exit.series[0].data[0] as unknown as { sector: Parameters<typeof buildQuadrantOption>[0][number] };
    const formatter = (exit.tooltip as unknown as { formatter: (params: { data: typeof data }) => string }).formatter;

    const trendingScatter = trending.series.find((series) => series.type === "scatter");
    const exitScatter = exit.series.find((series) => series.type === "scatter");
    expect(trendingScatter).toBeDefined();
    expect(exitScatter).toBeDefined();
    if (!trendingScatter || !exitScatter) throw new Error("散点系列缺失");

    expect((trendingScatter.data[0] as { itemStyle: { color: string } }).itemStyle.color).toBe((exitScatter.data[0] as { itemStyle: { color: string } }).itemStyle.color);
    expect(formatter({ data })).toContain("加速转弱");
    expect(formatter({ data })).toContain("6 日");
    expect(formatter({ data })).toContain("今日变化");
    expect(formatter({ data })).toContain("确认阶段为加速走弱");
  });

  it("tooltip 对未知 Lifecycle 状态与原因保持可见", () => {
    const option = buildQuadrantOption([{
      sector_name: "未知行业", velocity_score: .4, acceleration_score: .2, volume_score: .3, participation_score: .5,
      phase_confirmed: "accel_up", phase_confidence: .8, composite_rank: 1, lifecycle_state: "future_state", lifecycle_reason: "future_reason",
    }]);
    const data = option.series[0].data[0] as unknown as { sector: Parameters<typeof buildQuadrantOption>[0][number] };
    const formatter = (option.tooltip as unknown as { formatter: (params: { data: typeof data }) => string }).formatter;

    expect(formatter({ data })).toContain("未知状态");
    expect(formatter({ data })).toContain("原因字段暂未识别");
  });

  it("使用固定分数坐标轴,并排除掉缺失坐标的行业", () => {
    const option = buildQuadrantOption([
      { sector_name: "半导体", velocity_score: 0.4, acceleration_score: 0.2, volume_score: 0.3, participation_score: 0.5, phase_confirmed: "accel_up", phase_confidence: 0.8, composite_rank: 1 },
      { sector_name: "数据不足", velocity_score: null, acceleration_score: 0.2, volume_score: null, participation_score: null, phase_confirmed: "neutral", phase_confidence: null, composite_rank: null },
    ]);

    expect(option.xAxis.min).toBe(-1);
    expect(option.xAxis.max).toBe(1);
    expect(option.yAxis.min).toBe(-1);
    expect(option.series[0].data).toHaveLength(1);
    expect((option.series[0].data[0] as { name: string }).name).toBe("半导体");
  });

  it("在筛选框中跟踪行业的入选原因", () => {
    const option = buildQuadrantOption([{
      sector_name: "教育", velocity_score: 0.6, acceleration_score: 0.82, volume_score: 0.3,
      participation_score: 0.5, phase_confirmed: "accel_down", phase_confidence: 0.8,
      composite_rank: 2, composite_score: 0.73, rank_change_1d: 9, rank_change_5d: 23,
      phase_changed: 1,
    }], "教育", "focus");
    const data = option.series[0].data[0] as unknown as { sector: Parameters<typeof buildQuadrantOption>[0][number]; attentionReasons: string[] };
    const formatter = (option.tooltip as unknown as { formatter: (params: { data: typeof data }) => string }).formatter;
    const tooltip = formatter({ data });

    expect(tooltip).toContain("关注原因");
    expect(tooltip).toContain("正在跟踪");
    expect(tooltip).toContain("综合排名前10");
    expect(tooltip).toContain("阶段刚切换");
    expect(tooltip).toContain("1日排名上升9位");
    expect(tooltip).toContain("5日排名上升23位");
    expect(tooltip).toContain("加速度处于极值区");
    expect(tooltip).toContain("加速走弱");
  });

  it("将悬浮框限制在图表上下左右边界内,避免被相邻组件裁剪", () => {
    const option = buildQuadrantOption([{
      sector_name: "边界行业", velocity_score: 0.98, acceleration_score: 0.98, volume_score: 0.5,
      participation_score: 0.5, phase_confirmed: "accel_up", phase_confidence: 0.8,
      composite_rank: 1,
    }]);

    expect(option.tooltip).toMatchObject({
      confine: true,
      renderMode: "html",
    });
  });

  describe("Layer C 短期异动形状编码 (P2.2)", () => {
    function findBaseScatter(option: ReturnType<typeof buildQuadrantOption>) {
      const scatters = option.series.filter((series) => series.type === "scatter");
      for (const s of scatters) {
        const arr = (s as { data?: unknown }).data;
        if (!Array.isArray(arr) || arr.length === 0) continue;
        const sampleName = (arr[0] as { name: string }).name;
        if (!sampleName.endsWith("-halo") && !sampleName.endsWith("-chip")) return s;
      }
      return undefined;
    }
    function findGlyphSeries(option: ReturnType<typeof buildQuadrantOption>) {
      return option.series.find((series) => (series as { name?: string }).name === "短期异动形状");
    }

    it("未提供 shortTermHaloByName 时不渲染任何 chip 系列(无 Layer B)", () => {
      const option = buildQuadrantOption([{
        sector_name: "半导体", velocity_score: 0.4, acceleration_score: 0.2, volume_score: 0.3, participation_score: 0.5,
        phase_confirmed: "accel_up", phase_confidence: 0.8, composite_rank: 1,
      }]);
      const chipSeries = option.series.filter((series) => (series as { name?: string }).name === "短期异动形状");
      expect(chipSeries).toHaveLength(0);
      // Layer B 不再存在
      const haloSeries = option.series.filter((series) => (series as { name?: string }).name === "短期异动光晕");
      expect(haloSeries).toHaveLength(0);
    });

    it("主气泡在 halo 存在时也保留 v1 的参与度描边(不被短期覆盖)", () => {
      const haloIndex = buildShortTermHaloIndex([
        { sector_name: "半导体", short_term_intensity: "intense", short_term_labels: "pulse_up" },
      ]);
      const option = buildQuadrantOption(
        [{
          sector_name: "半导体", velocity_score: 0.4, acceleration_score: 0.2, volume_score: 0.3,
          participation_score: 0.5, phase_confirmed: "accel_up", phase_confidence: 0.8, composite_rank: 1,
        }],
        undefined,
        "focus",
        [],
        haloIndex,
      );
      const scatter = findBaseScatter(option);
      if (!scatter) throw new Error("散点系列缺失");
      const bubble = (scatter.data as Array<{ name: string; itemStyle: { borderColor: string; borderWidth: number; shadowColor: string; shadowBlur: number } }>)[0];
      // 参与度 0.5 > 0,应使用 #d7e7ff / 1.5px 而非 halo 颜色
      expect(bubble.itemStyle.borderColor).toBe("#d7e7ff");
      expect(bubble.itemStyle.borderWidth).toBe(1.5);
      // shadow 也应保留 phase 综合分规则而非 halo
      expect(bubble.itemStyle.shadowColor).toBe("rgba(0, 0, 0, 0.2)");
      expect(bubble.itemStyle.shadowBlur).toBe(8);
    });

    it("未命中的板块保持原描边规则", () => {
      const haloIndex = buildShortTermHaloIndex([
        { sector_name: "半导体", short_term_intensity: "intense", short_term_labels: "pulse_up" },
      ]);
      const option = buildQuadrantOption(
        [
          {
            sector_name: "银行", velocity_score: 0.1, acceleration_score: -0.1, volume_score: 0.2,
            participation_score: 0.5, phase_confirmed: "decel_up", phase_confidence: 0.6, composite_rank: 5,
          },
        ],
        undefined,
        "focus",
        [],
        haloIndex,
      );
      const scatter = findBaseScatter(option);
      if (!scatter) throw new Error("散点系列缺失");
      const bubble = (scatter.data as Array<{ name: string; itemStyle: { borderColor: string } }>)[0];
      expect(bubble.itemStyle.borderColor).toBe("#d7e7ff");
    });

    it("选中板块仍保留白色描边优先级(不与短期形状冲突)", () => {
      const haloIndex = buildShortTermHaloIndex([
        { sector_name: "半导体", short_term_intensity: "moderate", short_term_labels: "limit_cluster" },
      ]);
      const option = buildQuadrantOption(
        [{
          sector_name: "半导体", velocity_score: 0.6, acceleration_score: 0.6, volume_score: 0.3,
          participation_score: 0.5, phase_confirmed: "accel_up", phase_confidence: 0.8, composite_rank: 1,
        }],
        "半导体",
        "focus",
        [],
        haloIndex,
      );
      const scatter = findBaseScatter(option);
      if (!scatter) throw new Error("散点系列缺失");
      const bubble = (scatter.data as Array<{ itemStyle: { borderColor: string; borderWidth: number; shadowColor: string } }>)[0];
      expect(bubble.itemStyle.borderColor).toBe("#ffffff");
      expect(bubble.itemStyle.borderWidth).toBe(3);
    });

    it("生成 Layer C 形状并按主标签选择 SVG path,无 Layer B 圆环", () => {
      const haloIndex = buildShortTermHaloIndex([
        { sector_name: "半导体", short_term_intensity: "intense", short_term_labels: "pulse_up,volume_spike" },
      ]);
      const option = buildQuadrantOption(
        [{
          sector_name: "半导体", velocity_score: 0.6, acceleration_score: 0.4, volume_score: 0.3,
          participation_score: 0.5, phase_confirmed: "accel_up", phase_confidence: 0.8, composite_rank: 1,
        }],
        undefined,
        "focus",
        [],
        haloIndex,
      );
      const glyphSeries = findGlyphSeries(option);
      expect(glyphSeries).toBeDefined();
      if (!glyphSeries) throw new Error("glyph 系列缺失");
      const glyphData = glyphSeries.data as unknown as Array<{
        value: [number, number, number, string];
        symbol: string;
        symbolSize: [number, number];
        itemStyle: { color: string };
        label: { show: boolean };
      }>;
      expect(glyphData[0].value[3]).toBe("pulse_up");
      expect(glyphData[0].symbol.startsWith("path://")).toBe(true);
      expect(glyphData[0].symbol).toContain(SHORT_TERM_GLYPH_PATHS.pulse_up_intense);
      expect(glyphData[0].symbolSize).toEqual([12, 13]);
      expect(glyphData[0].itemStyle.color).toBe(SHORT_TERM_HALO_STYLE.intense.color);
      expect(glyphData[0].label.show).toBe(false);
    });

    it("非 pulse 标签的形状 size 按 intensity 缩放,intense > moderate > mild", () => {
      const haloIndex = buildShortTermHaloIndex([
        { sector_name: "半导体", short_term_intensity: "intense", short_term_labels: "limit_cluster" },
        { sector_name: "银行", short_term_intensity: "mild", short_term_labels: "limit_panic" },
      ]);
      const option = buildQuadrantOption(
        [
          { sector_name: "半导体", velocity_score: 0.6, acceleration_score: 0.4, volume_score: 0.3, participation_score: 0.5, phase_confirmed: "accel_up", phase_confidence: 0.8, composite_rank: 1 },
          { sector_name: "银行", velocity_score: 0.1, acceleration_score: -0.3, volume_score: 0.2, participation_score: 0.5, phase_confirmed: "decel_up", phase_confidence: 0.7, composite_rank: 5 },
        ],
        undefined,
        "focus",
        [],
        haloIndex,
      );
      const glyphSeries = findGlyphSeries(option);
      const data = (glyphSeries as { data: Array<{ name: string; symbolSize: [number, number] }> }).data;
      const intense = data.find((d) => d.name.startsWith("半导体"))!;
      const mild = data.find((d) => d.name.startsWith("银行"))!;
      // intense 面积应该严格大于 mild
      expect(intense.symbolSize[0] * intense.symbolSize[1]).toBeGreaterThan(mild.symbolSize[0] * mild.symbolSize[1]);
    });

    it("pulse_up / pulse_down 直接走基础尺寸,size 不随 intensity 变化", () => {
      const haloIndex = buildShortTermHaloIndex([
        { sector_name: "半导体", short_term_intensity: "intense", short_term_labels: "pulse_up" },
        { sector_name: "银行", short_term_intensity: "mild", short_term_labels: "pulse_down" },
      ]);
      const option = buildQuadrantOption(
        [
          { sector_name: "半导体", velocity_score: 0.6, acceleration_score: 0.4, volume_score: 0.3, participation_score: 0.5, phase_confirmed: "accel_up", phase_confidence: 0.8, composite_rank: 1 },
          { sector_name: "银行", velocity_score: -0.2, acceleration_score: -0.3, volume_score: 0.2, participation_score: 0.5, phase_confirmed: "accel_down", phase_confidence: 0.7, composite_rank: 5 },
        ],
        undefined,
        "focus",
        [],
        haloIndex,
      );
      const glyphSeries = findGlyphSeries(option);
      const data = (glyphSeries as { data: Array<{ name: string; symbol: string; symbolSize: [number, number] }> }).data;
      const semicon = data.find((d) => d.name.startsWith("半导体"))!;
      const bank = data.find((d) => d.name.startsWith("银行"))!;
      expect(semicon.symbolSize).toEqual([12, 13]);
      expect(bank.symbolSize).toEqual([12, 13]);
      // shape path 反映 intensity 差异(intense vs mild)
      expect(semicon.symbol).toContain(SHORT_TERM_GLYPH_PATHS.pulse_up_intense);
      expect(bank.symbol).toContain(SHORT_TERM_GLYPH_PATHS.pulse_down_mild);
    });

    it("rebound / breakdown 由 sub-path 组成(三角 + 同侧方块)", () => {
      const haloIndex = buildShortTermHaloIndex([
        { sector_name: "软件", short_term_intensity: "moderate", short_term_labels: "short_rebound_candidate" },
        { sector_name: "建材", short_term_intensity: "moderate", short_term_labels: "short_breakdown_candidate" },
      ]);
      const option = buildQuadrantOption(
        [
          { sector_name: "软件", velocity_score: 0.1, acceleration_score: 0.4, volume_score: 0.3, participation_score: 0.5, phase_confirmed: "bottoming_candidate", phase_confidence: 0.7, composite_rank: 7 },
          { sector_name: "建材", velocity_score: -0.1, acceleration_score: -0.4, volume_score: 0.3, participation_score: 0.5, phase_confirmed: "accel_down", phase_confidence: 0.7, composite_rank: 8 },
        ],
        undefined,
        "focus",
        [],
        haloIndex,
      );
      const glyphSeries = findGlyphSeries(option);
      const data = (glyphSeries as { data: Array<{ name: string; symbol: string }> }).data;
      const software = data.find((d) => d.name.startsWith("软件"))!;
      const building = data.find((d) => d.name.startsWith("建材"))!;
      expect(software.symbol).toContain(SHORT_TERM_GLYPH_PATHS.short_rebound_candidate);
      expect(building.symbol).toContain(SHORT_TERM_GLYPH_PATHS.short_breakdown_candidate);
      // 每个 path 都含有两个 M(代表两个 sub-path)
      expect((software.symbol.match(/M/g) || []).length).toBe(2);
      expect((building.symbol.match(/M/g) || []).length).toBe(2);
    });

    it("Layer C 形状的 shadowBlur 按 intensity 缩放(intense=8 / mild=4)", () => {
      const haloIndex = buildShortTermHaloIndex([
        { sector_name: "半导体", short_term_intensity: "intense", short_term_labels: "limit_cluster" },
        { sector_name: "银行", short_term_intensity: "mild", short_term_labels: "volume_spike" },
      ]);
      const option = buildQuadrantOption(
        [
          { sector_name: "半导体", velocity_score: 0.6, acceleration_score: 0.4, volume_score: 0.3, participation_score: 0.5, phase_confirmed: "accel_up", phase_confidence: 0.8, composite_rank: 1 },
          { sector_name: "银行", velocity_score: 0.1, acceleration_score: -0.1, volume_score: 0.2, participation_score: 0.5, phase_confirmed: "decel_up", phase_confidence: 0.6, composite_rank: 5 },
        ],
        undefined,
        "focus",
        [],
        haloIndex,
      );
      const glyphSeries = findGlyphSeries(option);
      const data = (glyphSeries as { data: Array<{ name: string; itemStyle: { shadowBlur: number } }> }).data;
      const intense = data.find((d) => d.name.startsWith("半导体"))!;
      const mild = data.find((d) => d.name.startsWith("银行"))!;
      expect(intense.itemStyle.shadowBlur).toBe(8);
      expect(mild.itemStyle.shadowBlur).toBe(4);
      expect(intense.itemStyle.shadowBlur).toBeGreaterThan(mild.itemStyle.shadowBlur);
    });

    it("tooltip 末尾追加短期命中标签与强度", () => {
      const halo: ShortTermHaloInfo = { intensity: "intense", primaryLabel: "pulse_up", allLabels: ["pulse_up", "volume_spike"], isAnomaly: true };
      const option = buildQuadrantOption(
        [{
          sector_name: "半导体", velocity_score: 0.6, acceleration_score: 0.4, volume_score: 0.3,
          participation_score: 0.5, phase_confirmed: "accel_up", phase_confidence: 0.8, composite_rank: 1,
        }],
        undefined,
        "focus",
        [],
        new Map([["半导体", halo]]),
      );
      const scatter = findBaseScatter(option);
      if (!scatter) throw new Error("散点系列缺失");
      const bubble = scatter.data[0] as unknown as { sector: Parameters<typeof buildQuadrantOption>[0][number]; halo?: ShortTermHaloInfo | null };
      const formatter = option.tooltip && (option.tooltip as unknown as { formatter?: (params: { data: typeof bubble }) => string }).formatter;
      expect(formatter).toBeDefined();
      if (!formatter) throw new Error("tooltip formatter 缺失");
      const tooltip = formatter({ data: bubble });
      expect(tooltip).toContain("短期命中");
      expect(tooltip).toContain("脉冲↑");
      expect(tooltip).toContain("量异");
      expect(tooltip).toContain("intense");
    });

    it("未命中短期标签时不追加短期命中信息条", () => {
      const option = buildQuadrantOption(
        [{
          sector_name: "半导体", velocity_score: 0.6, acceleration_score: 0.4, volume_score: 0.3,
          participation_score: 0.5, phase_confirmed: "accel_up", phase_confidence: 0.8, composite_rank: 1,
        }],
      );
      const scatter = findBaseScatter(option);
      if (!scatter) throw new Error("散点系列缺失");
      const bubble = scatter.data[0] as unknown as { sector: Parameters<typeof buildQuadrantOption>[0][number] };
      const formatter = option.tooltip && (option.tooltip as unknown as { formatter?: (params: { data: typeof bubble }) => string }).formatter;
      if (!formatter) throw new Error("tooltip formatter 缺失");
      const tooltip = formatter({ data: bubble });
      expect(tooltip).not.toContain("chart-tooltip-halo");
    });
  });
});