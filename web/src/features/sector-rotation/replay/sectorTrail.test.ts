/** 回放主图单行业尾迹构建测试。 */
import { buildSectorTrail } from "./sectorTrail";

describe("buildSectorTrail", () => {
  it("截至当前帧按日期生成最近历史，并为缺失坐标保留断点", () => {
    const points = [
      { as_of_date: "2026-08-01", sector_name: "教育", velocity_score: 0.1, acceleration_score: 0.2 },
      { as_of_date: "2026-08-02", sector_name: "软件", velocity_score: 0.3, acceleration_score: 0.2 },
      { as_of_date: "2026-08-03", sector_name: "教育", velocity_score: null, acceleration_score: 0.4 },
      { as_of_date: "2026-08-04", sector_name: "教育", velocity_score: 0.5, acceleration_score: 0.6 },
    ];
    expect(buildSectorTrail(points, "教育", "2026-08-04", 10)).toEqual([
      { as_of_date: "2026-08-01", velocity_score: 0.1, acceleration_score: 0.2 },
      null,
      null,
      { as_of_date: "2026-08-04", velocity_score: 0.5, acceleration_score: 0.6 },
    ]);
  });
});
