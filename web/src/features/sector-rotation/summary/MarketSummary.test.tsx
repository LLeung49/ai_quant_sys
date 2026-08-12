import { render, screen } from "@testing-library/react";
import { MarketSummary } from "./MarketSummary";

describe("MarketSummary", () => {
  it("renders only the market-regime card, without lifecycle observation controls", () => {
    render(<MarketSummary marketRegime="high_volatility" />);

    expect(screen.getByText("高波动")).toBeInTheDocument();
    expect(screen.getByText("市场环境")).toBeInTheDocument();
    expect(screen.queryByRole("button")).not.toBeInTheDocument();
    expect(screen.queryByText("趋势运行")).not.toBeInTheDocument();
    expect(screen.queryByText("修复/初启")).not.toBeInTheDocument();
    expect(screen.queryByText("风险提示")).not.toBeInTheDocument();
    expect(screen.queryByText("今日 Lifecycle 变化")).not.toBeInTheDocument();
  });
});
