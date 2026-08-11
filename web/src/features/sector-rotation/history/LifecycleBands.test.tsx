import { render, screen } from "@testing-library/react";
import { LifecycleBands } from "./LifecycleBands";

describe("LifecycleBands", () => {
  it("合并连续状态区间并保留缺口", () => {
    const pointsWithGap = [
      { as_of_date: "2026-08-08", sector_name: "半导体", lifecycle_state: "trending" },
      { as_of_date: "2026-08-11", sector_name: "半导体", lifecycle_state: "trending" },
    ];

    render(<LifecycleBands sectorNames={["半导体"]} points={pointsWithGap} expectedDates={["2026-08-08", "2026-08-10", "2026-08-11"]} />);

    expect(screen.getAllByText("趋势运行")).toHaveLength(2);
    expect(screen.getByText("数据缺口")).toBeInTheDocument();
  });

  it("把相邻同状态合并为一段", () => {
    render(<LifecycleBands sectorNames={["半导体"]} points={[
      { as_of_date: "2026-08-08", sector_name: "半导体", lifecycle_state: "trending" },
      { as_of_date: "2026-08-10", sector_name: "半导体", lifecycle_state: "trending" },
    ]} expectedDates={["2026-08-08", "2026-08-10"]} />);

    expect(screen.getAllByText("趋势运行")).toHaveLength(1);
    expect(screen.getByText(/2026-08-08 至 2026-08-10/)).toBeInTheDocument();
  });
});
