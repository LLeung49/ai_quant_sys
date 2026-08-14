/** nextDayWatch 纯函数分组与排序的单元测试。 */
import { describe, expect, it } from "vitest";
import type { ShortTermSector } from "./api";
import { buildNextDayWatchGroups } from "./nextDayWatch";

function sector(
  sector_name: string,
  short_term_labels: string,
  short_term_composite: number | null,
  short_term_composite_rank: number | null,
  score_eligible = true,
): ShortTermSector {
  return {
    sector_name,
    short_term_labels,
    short_term_composite,
    short_term_composite_rank,
    score_eligible,
  };
}

describe("buildNextDayWatchGroups", () => {
  it("按既有标签组合归入四类研究观察情景", () => {
    const groups = buildNextDayWatchGroups([
      sector("强势板块", "volume_spike,pulse_up", 0.62, 4),
      sector("恐慌板块", "pulse_down,volume_spike", -0.24, 12),
      sector("跌停板块", "limit_panic", -0.75, 3),
      sector("反弹板块", "short_rebound_candidate", 0.12, 22),
      sector("走弱板块", "short_breakdown_candidate", -0.17, 16),
      sector("无资格板块", "pulse_up,volume_spike", 0.95, 1, false),
    ]);

    expect(groups.map((group) => group.id)).toEqual([
      "strength_follow_through",
      "panic_reversal_watch",
      "short_rebound_watch",
      "short_breakdown_watch",
    ]);
    expect(groups[0].sectors.map((item) => item.sector_name)).toEqual(["强势板块"]);
    // 综合分高的恐慌板块 (-0.24) 应排在跌停板块 (-0.75) 之前。
    expect(groups[1].sectors.map((item) => item.sector_name)).toEqual(["恐慌板块", "跌停板块"]);
    expect(groups[2].sectors.map((item) => item.sector_name)).toEqual(["反弹板块"]);
    expect(groups[3].sectors.map((item) => item.sector_name)).toEqual(["走弱板块"]);
  });

  it("允许同一板块携带多重证据并出现于多个观察情景", () => {
    const groups = buildNextDayWatchGroups([
      sector("多重证据", "pulse_up,volume_spike,short_rebound_candidate", 0.8, 1),
    ]);

    expect(groups[0].sectors.map((item) => item.sector_name)).toEqual(["多重证据"]);
    expect(groups[2].sectors.map((item) => item.sector_name)).toEqual(["多重证据"]);
  });

  it("按综合分降序、排名升序、行业名稳定排序，并将缺失分数排在最后", () => {
    const groups = buildNextDayWatchGroups([
      sector("乙行业", "pulse_up,volume_spike", 0.5, 3),
      sector("甲行业", "pulse_up,volume_spike", 0.5, 2),
      sector("丙行业", "pulse_up,volume_spike", null, 1),
      sector("丁行业", "pulse_up,volume_spike", 0.7, 8),
    ]);

    expect(groups[0].sectors.map((item) => item.sector_name)).toEqual(["丁行业", "甲行业", "乙行业", "丙行业"]);
  });

  it("标签 CSV 顺序不同不影响分组判定", () => {
    const groups = buildNextDayWatchGroups([
      sector("A 行业", "pulse_up,volume_spike", 0.1, 5),
      sector("B 行业", "volume_spike, pulse_up ", 0.2, 4),
    ]);

    expect(groups[0].sectors.map((item) => item.sector_name)).toEqual(["B 行业", "A 行业"]);
  });
});
