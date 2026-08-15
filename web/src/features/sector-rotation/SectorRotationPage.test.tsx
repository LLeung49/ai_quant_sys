/** 板块轮动主视图装配与加载状态测试。 */
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { render, screen } from "@testing-library/react";
import { vi } from "vitest";

vi.mock("./useRotationData", () => ({
  useRotationData: () => ({
    latestDate: undefined,
    dates: { data: undefined, isLoading: true, isError: false },
    snapshot: { data: undefined, isLoading: false, isError: false },
  }),
}));
vi.mock("./useReplayData", () => ({ useReplayData: () => ({ data: undefined, isLoading: false, isError: false }) }));
vi.mock("./useHistoryData", () => ({ useHistoryData: () => ({ data: undefined, isLoading: false, isError: false }) }));
vi.mock("./short_term/useShortTermHaloSectors", () => ({
  useShortTermHaloSectors: () => ({ sectors: [], isLoading: true, isError: false, snapshot: null, queryRef: {} }),
}));
import { SectorRotationPage } from "./SectorRotationPage";

function renderWithQueryClient(ui: React.ReactElement) {
  const queryClient = new QueryClient({ defaultOptions: { queries: { retry: false } } });
  return render(<QueryClientProvider client={queryClient}>{ui}</QueryClientProvider>);
}

describe("SectorRotationPage", () => {
  it("在读取可用日期时显示可理解的加载状态", () => {
    renderWithQueryClient(<SectorRotationPage />);
    expect(screen.getByText("正在加载最新板块快照…")).toBeInTheDocument();
  });
});