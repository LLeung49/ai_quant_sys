/** 预加载市场回放帧的纯函数测试。 */
import { buildReplayFrames } from "./frameState";

describe("buildReplayFrames", () => {
  it("按日期升序分帧，且最新帧与同日快照保持同一行业集合", () => {
    const points = [
      { as_of_date: "2026-08-05", sector_name: "教育" },
      { as_of_date: "2026-08-04", sector_name: "教育" },
      { as_of_date: "2026-08-05", sector_name: "软件开发" },
    ];
    const frames = buildReplayFrames(points);
    expect(frames.dates).toEqual(["2026-08-04", "2026-08-05"]);
    expect(frames.byDate["2026-08-05"].map((point) => point.sector_name)).toEqual(["教育", "软件开发"]);
  });
});
