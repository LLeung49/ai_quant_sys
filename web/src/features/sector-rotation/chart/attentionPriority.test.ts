/** 气泡智能标注优先级与解释原因测试。 */
import { rankAttention } from "./attentionPriority";

const sector = (overrides: Record<string, unknown>) => ({
  sector_name: "测试行业", composite_rank: 50, acceleration_score: 0.1, phase_confirmed: "neutral", phase_changed: 0,
  rank_change_1d: 0, rank_change_5d: 0, ...overrides,
});

describe("rankAttention", () => {
  it("同时解释选中、阶段切换、排名大幅变化、加速度极值和风险阶段", () => {
    const [decision] = rankAttention([sector({ sector_name: "教育", phase_changed: 1, rank_change_1d: 14, acceleration_score: -0.82, phase_confirmed: "accel_down" })], "教育", "focus");
    expect(decision.visible).toBe(true);
    expect(decision.reasons).toEqual(expect.arrayContaining(["正在跟踪", "阶段刚切换", "1日排名上升14位", "加速度处于极值区", "加速走弱"]));
  });

  it("默认关注模式限制为三十个标签，并始终保留选中行业", () => {
    const sectors = Array.from({ length: 40 }, (_, index) => sector({ sector_name: `行业${index + 1}`, composite_rank: index + 1 }));
    const decisions = rankAttention(sectors, "行业40", "focus");
    expect(decisions.filter((item) => item.visible)).toHaveLength(30);
    expect(decisions.find((item) => item.sector.sector_name === "行业40")?.visible).toBe(true);
  });

  it("修复确认板块获得明确关注原因", () => {
    const [decision] = rankAttention([sector({ phase_confirmed: "reversal_confirmed" })], null, "compact");
    expect(decision.reasons).toContain("修复确认");
  });
});
