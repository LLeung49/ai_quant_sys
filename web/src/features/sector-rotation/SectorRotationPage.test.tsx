/** 板块轮动主视图组装与加载状态测试。 */
import { render, screen } from "@testing-library/react";
import { vi } from "vitest";

vi.mock("./useRotationData", () => ({ useRotationData: () => ({ latestDate: undefined, dates: { data: undefined, isLoading: true, isError: false }, snapshot: { data: undefined, isLoading: false, isError: false } }) }));
vi.mock("./useReplayData", () => ({ useReplayData: () => ({ data: undefined, isLoading: false, isError: false }) }));
vi.mock("./useHistoryData", () => ({ useHistoryData: () => ({ data: undefined, isLoading: false, isError: false }) }));
import { SectorRotationPage } from "./SectorRotationPage";

describe("SectorRotationPage", () => {
  it("在读取可用日期时显示可理解的加载状态", () => {
    render(<SectorRotationPage />);
    expect(screen.getByText("正在加载最新板块快照…")).toBeInTheDocument();
  });
});
