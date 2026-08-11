import { describe, expect, it } from "vitest";
import { getLifecycleMeta } from "./meta";

describe("lifecycle metadata", () => {
  it("未知 Lifecycle 不会被映射为 neutral", () => {
    expect(getLifecycleMeta("future_state")).toMatchObject({ state: "unknown", label: "未知状态" });
  });
});
