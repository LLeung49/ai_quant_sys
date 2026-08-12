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

  it("falls back to neutral observation when phase is unknown despite an emerging lifecycle", () => {
    expect(getCombinationConclusion("future_phase", "emerging")).toEqual({
      title: "方向未明 · 初步启动",
      guidance: "当前证据不足，建议继续观察后续连续变化。",
      tone: "neutral",
    });
  });

  it("falls back to neutral observation when phase matches an inherited property", () => {
    expect(getCombinationConclusion("toString", "emerging")).toEqual({
      title: "方向未明 · 初步启动",
      guidance: "当前证据不足，建议继续观察后续连续变化。",
      tone: "neutral",
    });
  });

  it("falls back to neutral observation when lifecycle is unknown", () => {
    expect(getCombinationConclusion("accel_up", "future_lifecycle")).toEqual({
      title: "加速走强 · 未知状态",
      guidance: "当前证据不足，建议继续观察后续连续变化。",
      tone: "neutral",
    });
  });

  it.each([
    ["bottoming_candidate", "repair", "positive", "连续性验证"],
    ["accel_up", "repair", "watch", "修复信号"],
    ["reversal_confirmed", "emerging", "positive", "共同确认"],
    ["accel_down", "trending", "watch", "分歧"],
    ["accel_up", "trending", "positive", "相对顺畅"],
    ["accel_up", "crowded", "watch", "拥挤"],
    ["accel_up", "divergence", "risk", "背离"],
    ["accel_up", "exit", "risk", "转弱"],
    ["neutral", "neutral", "neutral", "证据不足"],
  ])("keeps %s/%s lifecycle mapping at %s with %s guidance", (phase, lifecycle, tone, guidanceKeyword) => {
    const conclusion = getCombinationConclusion(phase, lifecycle);

    expect(conclusion.tone).toBe(tone);
    expect(conclusion.guidance).toContain(guidanceKeyword);
  });
});
