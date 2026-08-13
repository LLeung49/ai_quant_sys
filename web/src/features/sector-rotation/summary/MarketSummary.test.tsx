import { render, screen } from "@testing-library/react";
import { MarketSummary } from "./MarketSummary";

describe("MarketSummary", () => {
  it("renders only the market-regime card, without lifecycle observation controls", () => {
    render(<MarketSummary marketRegime="high_volatility" />);

    expect(screen.getByText("高波动")).toBeInTheDocument();
    expect(screen.getByText("市场环境")).toBeInTheDocument();
    // 市场环境卡片右上角的 HintIcon 按钮用于展示说明文案，并非 Lifecycle 控件。
    expect(screen.getByRole("button")).toBeInTheDocument();
    expect(screen.queryByText("趋势运行")).not.toBeInTheDocument();
    expect(screen.queryByText("修复/初启")).not.toBeInTheDocument();
    expect(screen.queryByText("风险提示")).not.toBeInTheDocument();
    expect(screen.queryByText("今日 Lifecycle 变化")).not.toBeInTheDocument();
  });

  it("collapses the regime hint into the HintIcon button instead of inline text", () => {
    const { container } = render(<MarketSummary marketRegime="risk_on" />);

    // 卡片内部不再展示独立的 <p> 说明文案。
    const card = container.querySelector(".summary-card--regime");
    expect(card).not.toBeNull();
    expect(card!.querySelector("p")).toBeNull();

    // 说明文案改由 HintIcon 按钮提供（aria-label 与文字一致）。
    const button = screen.getByRole("button", { name: /市场参与度较活跃/ });
    expect(button).toBeInTheDocument();
  });
});
