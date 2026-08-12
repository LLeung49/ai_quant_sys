/** 今日关注行业排行榜的展示与选择测试。 */
import { fireEvent, render, screen } from "@testing-library/react";
import { SectorRanking } from "./SectorRanking";

describe("SectorRanking", () => {
  it("以独立片段展示结构化 Lifecycle 短标签，且仍按 composite_rank 排序", () => {
    render(<SectorRanking sectors={[
      { sector_name: "稳定行业", score_eligible: true, composite_rank: 2, composite_score: .7, phase_confirmed: "decel_up", rank_change_1d: -3, lifecycle_state: "crowded", lifecycle_age: 8, lifecycle_changed: false },
      { sector_name: "第一行业", score_eligible: true, composite_rank: 1, composite_score: .8, phase_confirmed: "accel_up", rank_change_1d: 2, lifecycle_state: "divergence", lifecycle_age: 1, lifecycle_changed: true },
    ]} onSelect={vi.fn()} />);

    const rows = screen.getAllByRole("button", { name: /查看 .* 详情/ });
    expect(rows[0]).toHaveTextContent("第一行业");
    expect(rows[0].querySelector(".lifecycle-pill")).toHaveTextContent("背离｜第 1 日｜今日切换");
    expect(rows[1].querySelector(".lifecycle-pill")).toHaveTextContent("拥挤｜第 8 日");
    expect(rows[1].querySelector(".lifecycle-pill")).not.toHaveTextContent("今日切换");
  });

  it("Lifecycle 缺失时显示数据不足，排名变化同时保留方向和数值", () => {
    render(<SectorRanking sectors={[
      { sector_name: "上升行业", score_eligible: true, composite_rank: 1, composite_score: .8, phase_confirmed: "accel_up", rank_change_1d: 2 },
      { sector_name: "下降行业", score_eligible: true, composite_rank: 2, composite_score: .7, phase_confirmed: "decel_up", rank_change_1d: -3, lifecycle_state: "crowded", lifecycle_age: 8, lifecycle_changed: false },
    ]} onSelect={vi.fn()} />);

    const rows = screen.getAllByRole("button", { name: /查看 .* 详情/ });
    expect(rows[0].querySelector(".lifecycle-pill")).toHaveTextContent("数据不足");
    expect(rows[0].querySelector(".rank-up")).toHaveTextContent("2");
    expect(rows[0].querySelector(".rank-up svg")).toBeInTheDocument();
    expect(rows[1].querySelector(".rank-down")).toHaveTextContent("3");
    expect(rows[1].querySelector(".rank-down svg")).toBeInTheDocument();
  });

  it("只展示可评分行业，并回传用户选中的行业名称", () => {
    const onSelect = vi.fn();
    render(<SectorRanking sectors={[
      { sector_name: "半导体", score_eligible: true, composite_rank: 1, composite_score: 0.42, phase_confirmed: "accel_up", rank_change_1d: 2 },
      { sector_name: "数据不足", score_eligible: false, composite_rank: null, composite_score: null, phase_confirmed: "neutral", rank_change_1d: null },
    ]} onSelect={onSelect} />);

    fireEvent.click(screen.getByRole("button", { name: /半导体/ }));
    expect(onSelect).toHaveBeenCalledWith("半导体");
    expect(screen.queryByRole("button", { name: /查看 数据不足 详情/ })).not.toBeInTheDocument();
  });
});
