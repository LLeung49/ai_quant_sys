/** 象限气泡图数据编码的纯函数测试。 */
import { buildQuadrantOption } from "./quadrantOption";

describe("buildQuadrantOption", () => {
  it("Lifecycle 不改变气泡的 Phase 颜色，并在 tooltip 展示状态、持续时间与原因", () => {
    const baseSector = { sector_name: "半导体", velocity_score: .4, acceleration_score: .2, volume_score: .3, participation_score: .5, phase_confirmed: "accel_up", phase_confidence: .8, composite_rank: 1 };
    const trending = buildQuadrantOption([{ ...baseSector, lifecycle_state: "trending" }]);
    const exit = buildQuadrantOption([{ ...baseSector, lifecycle_state: "exit", lifecycle_age: 6, lifecycle_changed: true, lifecycle_reason: "phase_accel_down" }]);
    const data = exit.series[0].data[0] as unknown as { sector: Parameters<typeof buildQuadrantOption>[0][number] };
    const formatter = (exit.tooltip as unknown as { formatter: (params: { data: typeof data }) => string }).formatter;

    expect(trending.series[0].data[0].itemStyle.color).toBe(exit.series[0].data[0].itemStyle.color);
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

  it("使用固定分数坐标轴，并忽略缺失坐标的行业", () => {
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

  it("在悬浮框中醒目标识行业入选关注标签的原因", () => {
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

  it("将悬浮框限制在图表上下左右边界内，避免被相邻组件裁剪", () => {
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
});
