/** 板块详情抽屉的研究文案与关闭交互测试。 */
import { fireEvent, render, screen } from "@testing-library/react";
import { vi } from "vitest";
import { SectorDetailDrawer } from "./SectorDetailDrawer";

vi.mock("../kline/SectorKlineCard", () => ({
  SectorKlineCard: ({ sectorName, level, asOfDate, onExpand }: { sectorName: string; level: number; asOfDate: string; onExpand: (data: unknown) => void }) => <button data-testid="sector-kline-card" type="button" onClick={() => onExpand({})}>{sectorName}|{level}|{asOfDate}</button>,
}));
vi.mock("../kline/SectorKlineModal", () => ({
  SectorKlineModal: () => <div role="dialog" aria-label="半导体放大行情图" />,
}));

describe("SectorDetailDrawer", () => {
  it("展示 Lifecycle 研究解释，并允许关闭详情", () => {
    const onClose = vi.fn();
    render(<SectorDetailDrawer sector={{ sector_name: "半导体", phase_confirmed: "accel_up", phase_age: 4, phase_confidence: 0.72, composite_rank: 1, rank_change_1d: 2, coverage_ratio: 0.96, trend_level_score: 0.4, velocity_score: 0.5, acceleration_score: 0.3, participation_score: 0.4, volume_score: 0.2 }} level={2} asOfDate="2026-08-04" isLatestDate={false} onClose={onClose} />);

    expect(screen.getByText("未知状态")).toBeInTheDocument();
    expect(screen.getByTestId("sector-kline-card")).toHaveTextContent("半导体|2|2026-08-04");
    fireEvent.click(screen.getByRole("button", { name: "关闭详情" }));
    expect(onClose).toHaveBeenCalledOnce();
  });

  it("第一次 Escape 只关闭行情弹窗，第二次才关闭详情抽屉", () => {
    const onClose = vi.fn();
    render(<SectorDetailDrawer sector={{ sector_name: "半导体", phase_confirmed: "accel_up", phase_age: 4, phase_confidence: 0.72, composite_rank: 1, rank_change_1d: 2, coverage_ratio: 0.96, trend_level_score: 0.4, velocity_score: 0.5, acceleration_score: 0.3, participation_score: 0.4, volume_score: 0.2 }} level={2} asOfDate="2026-08-04" isLatestDate={false} onClose={onClose} />);

    fireEvent.click(screen.getByTestId("sector-kline-card"));
    expect(screen.getByRole("dialog", { name: "半导体放大行情图" })).toBeInTheDocument();
    fireEvent.keyDown(window, { key: "Escape" });
    expect(screen.queryByRole("dialog")).not.toBeInTheDocument();
    expect(onClose).not.toHaveBeenCalled();
    fireEvent.keyDown(window, { key: "Escape" });
    expect(onClose).toHaveBeenCalledOnce();
  });

  it("工作台日期变化时自动关闭旧的行情弹窗", () => {
    const onClose = vi.fn();
    const sector = { sector_name: "半导体", phase_confirmed: "accel_up", phase_age: 4, phase_confidence: 0.72, composite_rank: 1, rank_change_1d: 2, coverage_ratio: 0.96, trend_level_score: 0.4, velocity_score: 0.5, acceleration_score: 0.3, participation_score: 0.4, volume_score: 0.2 };
    const { rerender } = render(<SectorDetailDrawer sector={sector} level={2} asOfDate="2026-08-04" isLatestDate={false} onClose={onClose} />);

    fireEvent.click(screen.getByTestId("sector-kline-card"));
    expect(screen.getByRole("dialog")).toBeInTheDocument();
    rerender(<SectorDetailDrawer sector={sector} level={2} asOfDate="2026-08-05" isLatestDate={false} onClose={onClose} />);
    expect(screen.queryByRole("dialog")).not.toBeInTheDocument();
  });

  it("展示当前 Lifecycle、转移与固定声明", () => {
    render(<SectorDetailDrawer sector={{ sector_name: "半导体", phase_confirmed: "accel_up", phase_age: 4, phase_confidence: 0.72, composite_rank: 1, rank_change_1d: 2, coverage_ratio: 0.96, trend_level_score: 0.4, velocity_score: 0.5, acceleration_score: 0.3, participation_score: 0.4, volume_score: 0.2, lifecycle_state: "trending", lifecycle_reason: "phase_accel_up", lifecycle_age: 3, lifecycle_changed: true }} previousLifecycleState="repair" level={2} asOfDate="2026-08-10" isLatestDate={false} onClose={vi.fn()} />);

    expect(screen.getByText("趋势运行")).toBeInTheDocument();
    expect(screen.getByText(/修复观察.*趋势运行/)).toBeInTheDocument();
    expect(screen.getByText("Lifecycle 为市场状态观察标签，不构成交易建议。")).toBeInTheDocument();
  });

  it("在 K 线卡之前展示当前层级和截至日的板块行情信息卡", () => {
    render(<SectorDetailDrawer sector={{ sector_name: "半导体", phase_confirmed: "accel_up", phase_age: 4, phase_confidence: 0.72, composite_rank: 1, rank_change_1d: 2, coverage_ratio: 0.96, trend_level_score: 0.4, velocity_score: 0.5, acceleration_score: 0.3, participation_score: 0.4, volume_score: 0.2, lifecycle_state: "trending" }} previousLifecycleState="repair" level={2} asOfDate="2026-08-10" isLatestDate={false} onClose={vi.fn()} />);

    const context = screen.getByLabelText("板块行情信息");
    const klineCard = screen.getByTestId("sector-kline-card");
    expect(context).toHaveTextContent("板块行情");
    expect(context).toHaveTextContent("价格口径：申万二级行业等权合成指数日线收盘价");
    expect(context).toHaveTextContent("截至日期：2026-08-10");
    expect(context.compareDocumentPosition(klineCard) & Node.DOCUMENT_POSITION_FOLLOWING).toBeTruthy();
    expect(screen.getByText(/修复观察.*趋势运行/)).toBeInTheDocument();
  });

  it("在前一状态缺失时明示不可用", () => {
    render(<SectorDetailDrawer sector={{ sector_name: "半导体", phase_confirmed: "accel_up", phase_age: 4, phase_confidence: 0.72, composite_rank: 1, rank_change_1d: 2, coverage_ratio: 0.96, trend_level_score: 0.4, velocity_score: 0.5, acceleration_score: 0.3, participation_score: 0.4, volume_score: 0.2, lifecycle_state: "trending" }} level={2} asOfDate="2026-08-10" isLatestDate={false} onClose={vi.fn()} />);

    expect(screen.getByText("前一状态暂不可用")).toBeInTheDocument();
  });

  it("将 Lifecycle 持续天数与今日变化的缺失值显示为数据不足", () => {
    const baseSector = { sector_name: "半导体", phase_confirmed: "accel_up", phase_age: 4, phase_confidence: 0.72, composite_rank: 1, rank_change_1d: 2, coverage_ratio: 0.96, trend_level_score: 0.4, velocity_score: 0.5, acceleration_score: 0.3, participation_score: 0.4, volume_score: 0.2, lifecycle_state: "trending" };
    const { rerender } = render(<SectorDetailDrawer sector={{ ...baseSector, lifecycle_age: 3, lifecycle_changed: true }} level={2} asOfDate="2026-08-10" isLatestDate={false} onClose={vi.fn()} />);

    expect(screen.getByText("持续天数").parentElement).toHaveTextContent("3 日");
    expect(screen.getByText("今日变化").parentElement).toHaveTextContent("是");

    rerender(<SectorDetailDrawer sector={{ ...baseSector, lifecycle_age: null, lifecycle_changed: false }} level={2} asOfDate="2026-08-10" isLatestDate={false} onClose={vi.fn()} />);
    expect(screen.getByText("持续天数").parentElement).toHaveTextContent("数据不足");
    expect(screen.getByText("今日变化").parentElement).toHaveTextContent("否");

    rerender(<SectorDetailDrawer sector={{ ...baseSector, lifecycle_changed: undefined }} level={2} asOfDate="2026-08-10" isLatestDate={false} onClose={vi.fn()} />);
    expect(screen.getByText("持续天数").parentElement).toHaveTextContent("数据不足");
    expect(screen.getByText("今日变化").parentElement).toHaveTextContent("数据不足");

    rerender(<SectorDetailDrawer sector={{ ...baseSector, lifecycle_changed: null }} level={2} asOfDate="2026-08-10" isLatestDate={false} onClose={vi.fn()} />);
    expect(screen.getByText("今日变化").parentElement).toHaveTextContent("数据不足");
  });
});
