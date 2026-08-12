import { describe, expect, it } from "vitest";
import { getCombinationConclusion } from "./combinationConclusion";

describe("getCombinationConclusion", () => {
  it("combines confirmed repair with early activation", () => {
    expect(getCombinationConclusion("reversal_confirmed", "emerging")).toEqual({
      title: "修复确认 · 初步启动",
      guidance: "可进入重点跟踪，等待排名与市场环境共同确认。",
      tone: "positive",
    });
  });

  it("warns against chasing a cooling strong sector with divergence", () => {
    const conclusion = getCombinationConclusion("decel_up", "divergence");

    expect(conclusion.tone).toBe("risk");
    expect(conclusion.guidance).toContain("避免追涨");
  });

  it("covers every supported phase and lifecycle without trading instructions", () => {
    const phases = ["accel_up", "decel_up", "bottoming_candidate", "reversal_confirmed", "accel_down", "neutral"];
    const lifecycles = ["repair", "emerging", "trending", "crowded", "divergence", "exit", "neutral"];
    const forbidden = /买入|卖出|加仓|减仓/;

    for (const phase of phases) {
      for (const lifecycle of lifecycles) {
        const conclusion = getCombinationConclusion(phase, lifecycle);
        expect(conclusion.title).toBeTruthy();
        expect(conclusion.guidance).toBeTruthy();
        expect(["positive", "watch", "risk", "neutral"]).toContain(conclusion.tone);
        expect(`${conclusion.title}${conclusion.guidance}`).not.toMatch(forbidden);
      }
    }
  });

  it("falls back safely when phase or lifecycle is missing", () => {
    expect(getCombinationConclusion(null, undefined)).toEqual({
      title: "方向未明 · 未知状态",
      guidance: "当前证据不足，建议继续观察后续连续变化。",
      tone: "neutral",
    });
  });
});
