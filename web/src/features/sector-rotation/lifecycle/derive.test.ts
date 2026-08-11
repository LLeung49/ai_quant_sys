import { describe, expect, it } from "vitest";
import {
  buildLifecycleBands,
  findPreviousLifecycle,
  hasLifecycleCoverage,
  matchesLifecycleFilter,
  summarizeLifecycle,
} from "./derive";

describe("lifecycle derived state", () => {
  it("intersects state group and today's changed flag", () => {
    expect(matchesLifecycleFilter({ lifecycle_state: "crowded", lifecycle_changed: true }, "risk", true)).toBe(true);
    expect(matchesLifecycleFilter({ lifecycle_state: "exit", lifecycle_changed: false }, "risk", true)).toBe(false);
    expect(matchesLifecycleFilter({ lifecycle_state: "repair", lifecycle_changed: true }, "risk", true)).toBe(false);
  });

  it("allows all states without changed-only filtering", () => {
    expect(matchesLifecycleFilter({ lifecycle_state: null, lifecycle_changed: false }, "all", false)).toBe(true);
    expect(matchesLifecycleFilter({ lifecycle_state: "emerging", lifecycle_changed: false }, "repair_or_emerging", false)).toBe(true);
  });

  it("reports whether at least one known lifecycle state is present", () => {
    expect(hasLifecycleCoverage([{ lifecycle_state: null }, { lifecycle_state: "trending" }])).toBe(true);
    expect(hasLifecycleCoverage([{ lifecycle_state: undefined }, { lifecycle_state: "legacy" }])).toBe(false);
  });

  it("counts known states and puts missing or unknown states in insufficient", () => {
    expect(summarizeLifecycle([
      { lifecycle_state: "trending" },
      { lifecycle_state: "repair" },
      { lifecycle_state: "emerging" },
      { lifecycle_state: "crowded" },
      { lifecycle_state: "divergence" },
      { lifecycle_state: "exit" },
      { lifecycle_state: null },
      { lifecycle_state: "legacy" },
    ])).toEqual({ trending: 1, repairOrEmerging: 2, risk: 3, changed: 0, insufficient: 2 });
    expect(summarizeLifecycle([{ lifecycle_state: "trending", lifecycle_changed: true }, { lifecycle_state: "neutral", lifecycle_changed: true }]).changed).toBe(2);
  });

  it("finds only the latest valid prior point for the sector", () => {
    const points = [
      { as_of_date: "2026-08-08", sector_name: "半导体", lifecycle_state: "repair" },
      { as_of_date: "2026-08-10", sector_name: "半导体", lifecycle_state: "trending" },
      { as_of_date: "2026-08-11", sector_name: "半导体", lifecycle_state: "crowded" },
    ];
    expect(findPreviousLifecycle(points, "半导体", "2026-08-10")?.lifecycle_state).toBe("repair");
  });

  it("builds a gap band for each missing expected date", () => {
    const bands = buildLifecycleBands(
      [
        { as_of_date: "2026-08-08", sector_name: "半导体", lifecycle_state: "trending" },
        { as_of_date: "2026-08-11", sector_name: "半导体", lifecycle_state: "trending" },
      ],
      ["2026-08-08", "2026-08-10", "2026-08-11"],
    );
    expect(bands).toHaveLength(3);
    expect(bands.map((band) => band.gap)).toEqual([false, true, false]);
    expect(bands.map((band) => band.tradingDays)).toEqual([1, 0, 1]);
  });
});
