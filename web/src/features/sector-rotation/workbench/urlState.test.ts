/** 统一工作台 URL 状态契约测试。 */
import { parseWorkbenchUrl, serializeWorkbenchUrl } from "./urlState";

describe("workbench URL state", () => {
  it("解析有效参数并对非法枚举安全回退", () => {
    expect(parseWorkbenchUrl("?date=2026-08-04&level=1&mode=replay&phase=accel_up&q=教育&sector=教育&window=60&labels=all")).toEqual({
      date: "2026-08-04", level: 1, mode: "replay", phase: "accel_up", query: "教育", sector: "教育", historyWindow: 60, labelDensity: "all", lifecycle: "all", changedOnly: false,
    });
    expect(parseWorkbenchUrl("?level=9&mode=bad&window=7&labels=nope")).toMatchObject({ level: 2, mode: "snapshot", historyWindow: 20, labelDensity: "focus" });
  });

  it("恢复 Lifecycle 状态组与今日变化", () => {
    expect(parseWorkbenchUrl("?lifecycle=risk&changed=1")).toMatchObject({ lifecycle: "risk", changedOnly: true });
    expect(parseWorkbenchUrl("?lifecycle=invalid&changed=0")).toMatchObject({ lifecycle: "all", changedOnly: false });
  });

  it("序列化研究现场并省略空行业选择", () => {
    const query = serializeWorkbenchUrl({ date: "2026-08-04", level: 2, mode: "snapshot", phase: "all", query: "", sector: null, historyWindow: 20, labelDensity: "focus", lifecycle: "risk", changedOnly: true });
    expect(query).toContain("date=2026-08-04");
    expect(query).toContain("lifecycle=risk");
    expect(query).toContain("changed=1");
    expect(query).not.toContain("sector=");
  });

  it("序列化非今日变化时不写 changed 参数", () => {
    const query = serializeWorkbenchUrl({ date: undefined, level: 2, mode: "snapshot", phase: "all", query: "", sector: null, historyWindow: 20, labelDensity: "focus", lifecycle: "all", changedOnly: false });
    expect(query).toContain("lifecycle=all");
    expect(query).not.toContain("changed=");
  });

  it("兼容旧调用并为缺失的 Lifecycle 筛选写入默认值", () => {
    const query = serializeWorkbenchUrl({ date: undefined, level: 2, mode: "snapshot", phase: "all", query: "", sector: null, historyWindow: 20, labelDensity: "focus" });
    expect(query).toContain("lifecycle=all");
    expect(query).not.toContain("changed=");
  });
});
