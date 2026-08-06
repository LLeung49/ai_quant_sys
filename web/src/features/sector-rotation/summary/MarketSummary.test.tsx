/** 市场摘要卡片的显示与研究措辞测试。 */
import { render, screen } from "@testing-library/react";
import { MarketSummary } from "./MarketSummary";

describe("MarketSummary", () => {
  it("展示高波动环境和基于快照的行业观察数量", () => {
    render(<MarketSummary marketRegime="high_volatility" eligibleCount={113} acceleratingCount={8} riskCount={14} />);

    expect(screen.getByText("高波动")).toBeInTheDocument();
    expect(screen.getByText("113 个行业具备完整评分证据")).toBeInTheDocument();
    expect(screen.getByText("8 个行业处于加速走强阶段")).toBeInTheDocument();
    expect(screen.getByText("高波动环境下，强势信号存在更高不确定性。")).toBeInTheDocument();
  });
});
