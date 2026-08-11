/** 市场摘要卡片的显示与研究措辞测试。 */
import { fireEvent, render, screen } from "@testing-library/react";
import { vi } from "vitest";
import { MarketSummary } from "./MarketSummary";

describe("MarketSummary", () => {
  it("展示高波动环境和完整快照的 Lifecycle 观察数量", () => {
    render(<MarketSummary marketRegime="high_volatility" counts={{ trending: 8, repairOrEmerging: 3, risk: 14, changed: 2, insufficient: 1 }} activeLifecycle="all" changedOnly={false} onLifecycleFilterChange={vi.fn()} onChangedOnlyChange={vi.fn()} />);

    expect(screen.getByText("高波动")).toBeInTheDocument();
    expect(screen.getByRole("button", { name: /趋势运行 8/ })).toBeInTheDocument();
    expect(screen.getByRole("button", { name: /修复\/初启 3/ })).toBeInTheDocument();
    expect(screen.getByRole("button", { name: /拥挤\/背离\/退出 14/ })).toBeInTheDocument();
    expect(screen.getByRole("button", { name: /今日变化 2/ })).toBeInTheDocument();
    expect(screen.getByText("高波动环境下，强势信号存在更高不确定性。")).toBeInTheDocument();
  });

  it("基于完整截面计数并点击风险卡设置状态组", () => {
    const onLifecycleFilterChange = vi.fn();
    render(<MarketSummary marketRegime="range" counts={{ trending: 2, repairOrEmerging: 3, risk: 4, changed: 1, insufficient: 0 }} activeLifecycle="all" changedOnly={false} onLifecycleFilterChange={onLifecycleFilterChange} onChangedOnlyChange={vi.fn()} />);

    fireEvent.click(screen.getByRole("button", { name: /拥挤\/背离\/退出 4/ }));
    expect(onLifecycleFilterChange).toHaveBeenCalledWith("risk");
  });

  it("旧快照禁用四张 Lifecycle 交互卡", () => {
    render(<MarketSummary marketRegime="range" counts={{ trending: 0, repairOrEmerging: 0, risk: 0, changed: 0, insufficient: 3 }} activeLifecycle="all" changedOnly={false} lifecycleDisabled onLifecycleFilterChange={vi.fn()} onChangedOnlyChange={vi.fn()} />);

    expect(screen.getAllByRole("button")).toHaveLength(4);
    screen.getAllByRole("button").forEach((card) => expect(card).toBeDisabled());
  });
});
