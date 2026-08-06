/** 行业轮动轨迹配置的连续性测试。 */
import { buildTrajectoryOption } from "./trajectoryOption";

describe("buildTrajectoryOption", () => {
  it("按日期连接坐标，并对缺失坐标保留断点", () => {
    const option = buildTrajectoryOption([{
      sector_name: "半导体", points: [
        { as_of_date: "2026-08-01", velocity_score: 0.1, acceleration_score: 0.2 },
        { as_of_date: "2026-08-04", velocity_score: null, acceleration_score: null },
        { as_of_date: "2026-08-05", velocity_score: 0.3, acceleration_score: 0.4 },
      ],
    }]);
    expect(option.series[0].data).toEqual([
      { value: [0.1, 0.2], as_of_date: "2026-08-01", isLatest: false },
      null,
      { value: [0.3, 0.4], as_of_date: "2026-08-05", isLatest: true },
    ]);
    const tooltip = (option.tooltip as { formatter: (params: { seriesName: string; data: { value: number[]; as_of_date: string } }) => string }).formatter({ seriesName: "半导体", data: { value: [0.3, 0.4], as_of_date: "2026-08-05" } });
    expect(tooltip).toContain("半导体");
    expect(tooltip).toContain("2026-08-05");
    expect(tooltip).toContain("趋势速度");
  });

  it("最多绘制五条轨迹并为五个行业使用不同的稳定颜色", () => {
    const trajectories = ["A", "B", "C", "D", "E", "F"].map((sectorName, index) => ({
      sector_name: sectorName,
      points: [{ as_of_date: "2026-08-06", velocity_score: index / 10, acceleration_score: index / 10 }],
    }));

    const option = buildTrajectoryOption(trajectories);
    expect(option.series).toHaveLength(5);
    expect(new Set(option.series.map((series) => series.lineStyle.color))).toEqual(new Set(["#37d6b0", "#67a9ff", "#f0b65a", "#ff7189", "#a98bff"]));
  });
});
