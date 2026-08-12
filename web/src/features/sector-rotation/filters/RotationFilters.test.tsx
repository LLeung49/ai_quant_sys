/** 板块轮动筛选器的用户交互测试。 */
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { fireEvent, render, screen, within } from "@testing-library/react";
import { type ReactNode } from "react";
import { RotationFilters } from "./RotationFilters";

describe("RotationFilters", () => {
  function renderFilters(ui: ReactNode) {
    const client = new QueryClient({ defaultOptions: { queries: { retry: false } } });
    return render(<QueryClientProvider client={client}>{ui}</QueryClientProvider>);
  }

  beforeEach(() => {
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue(new Response(JSON.stringify({
      sector_level: 2,
      model_version: "v1",
      trade_dates: ["2026-08-10", "2026-08-11"],
      snapshot_dates: ["2026-08-10"],
      latest_snapshot_date: "2026-08-10",
    }))));
  });

  it("默认显示二级行业，并将用户选择回传给页面状态", () => {
    const onLevelChange = vi.fn();
    renderFilters(<RotationFilters dates={["2026-08-04", "2026-08-03"]} selectedDate="2026-08-04" level={2} modelVersion="v1" onDateChange={vi.fn()} onLevelChange={onLevelChange} />);

    expect(screen.getByLabelText("行业层级")).toHaveValue("2");
    fireEvent.change(screen.getByLabelText("行业层级"), { target: { value: "1" } });
    expect(onLevelChange).toHaveBeenCalledWith(1);
  });

  it("旧快照禁用 Lifecycle 控件并解释原因", () => {
    renderFilters(<RotationFilters dates={["2026-08-04"]} selectedDate="2026-08-04" level={2} modelVersion="v1" onDateChange={vi.fn()} onLevelChange={vi.fn()} lifecycleDisabled lifecycleFilter="all" changedOnly={false} onLifecycleChange={vi.fn()} onChangedOnlyChange={vi.fn()} />);

    expect(screen.getByLabelText("生命周期状态")).toBeDisabled();
    expect(screen.getByLabelText("仅看今日变化")).toBeDisabled();
    expect(screen.getByText("该日期无 Lifecycle 数据")).toBeInTheDocument();
  });

  it("将 Lifecycle 筛选交互回传给页面状态", () => {
    const onLifecycleChange = vi.fn();
    const onChangedOnlyChange = vi.fn();
    renderFilters(<RotationFilters dates={["2026-08-04"]} selectedDate="2026-08-04" level={2} modelVersion="v1" onDateChange={vi.fn()} onLevelChange={vi.fn()} lifecycleFilter="all" changedOnly={false} onLifecycleChange={onLifecycleChange} onChangedOnlyChange={onChangedOnlyChange} />);

    fireEvent.change(screen.getByLabelText("生命周期状态"), { target: { value: "risk" } });
    fireEvent.click(screen.getByLabelText("仅看今日变化"));

    expect(onLifecycleChange).toHaveBeenCalledWith("risk");
    expect(onChangedOnlyChange).toHaveBeenCalledWith(true);
  });

  it("将仅看今日变化渲染为独立的紧凑勾选控件", () => {
    renderFilters(<RotationFilters dates={["2026-08-10"]} selectedDate="2026-08-10" level={2} modelVersion="v1" onDateChange={vi.fn()} onLevelChange={vi.fn()} lifecycleFilter="all" changedOnly={false} onLifecycleChange={vi.fn()} onChangedOnlyChange={vi.fn()} />);

    const checkbox = screen.getByLabelText("仅看今日变化");
    expect(checkbox).toHaveAttribute("type", "checkbox");
    expect(checkbox.closest(".filter-field")).toHaveClass("filter-field--checkbox");
  });
  it("returns a pending trading-date selection to the page", async () => {
    const onDateChange = vi.fn();
    const view = renderFilters(<RotationFilters dates={["2026-08-10"]} selectedDate="2026-08-10" level={2} modelVersion="v1" onDateChange={onDateChange} onLevelChange={vi.fn()} />);

    const pendingDay = await within(view.container).findByRole("button", { name: /2026-08-11.*尚未生成快照/ });
    fireEvent.click(pendingDay);
    expect(onDateChange).toHaveBeenCalledWith("2026-08-11");
  });
});
