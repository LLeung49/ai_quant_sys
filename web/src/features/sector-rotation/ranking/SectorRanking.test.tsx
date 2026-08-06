/** 今日关注行业排行榜的展示与选择测试。 */
import { fireEvent, render, screen } from "@testing-library/react";
import { SectorRanking } from "./SectorRanking";

describe("SectorRanking", () => {
  it("只展示可评分行业，并回传用户选中的行业名称", () => {
    const onSelect = vi.fn();
    render(<SectorRanking sectors={[
      { sector_name: "半导体", score_eligible: true, composite_rank: 1, composite_score: 0.42, phase_confirmed: "accel_up", rank_change_1d: 2 },
      { sector_name: "数据不足", score_eligible: false, composite_rank: null, composite_score: null, phase_confirmed: "neutral", rank_change_1d: null },
    ]} onSelect={onSelect} />);

    fireEvent.click(screen.getByRole("button", { name: /半导体/ }));
    expect(onSelect).toHaveBeenCalledWith("半导体");
    expect(screen.queryByText("数据不足")).not.toBeInTheDocument();
  });
});
