/** 历史轨迹缺口说明测试。 */
import { findHistoryGaps } from "./historyGaps";

describe("findHistoryGaps", () => {
  it("识别行业缺失日期和坐标为空日期", () => {
    const gaps = findHistoryGaps(["2026-08-01", "2026-08-04", "2026-08-05"], ["教育"], [
      { as_of_date: "2026-08-01", sector_name: "教育", velocity_score: 0.1, acceleration_score: 0.2 },
      { as_of_date: "2026-08-05", sector_name: "教育", velocity_score: null, acceleration_score: 0.4 },
    ]);
    expect(gaps).toEqual([{ sector_name: "教育", dates: ["2026-08-04", "2026-08-05"] }]);
  });
});
