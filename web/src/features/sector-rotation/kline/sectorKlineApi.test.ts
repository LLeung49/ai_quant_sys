/** 板块 K 线 HTTP 契约和运行时数据校验测试。 */
import { describe, expect, it, vi } from "vitest";
import { fetchSectorKline } from "./sectorKlineApi";

const validResponse = {
  sector_name: "半导体",
  sector_level: 2,
  requested_end_date: "2026-08-06",
  actual_end_date: "2026-08-06",
  price_basis: "equal_weight_composite_index",
  bars: [{
    trade_date: "2026-08-05",
    timestamp: 1785859200000,
    open: 10,
    high: 12,
    low: 9,
    close: 11,
    volume: 100,
    amount: 1_000,
  }, {
    trade_date: "2026-08-06",
    timestamp: 1785945600000,
    open: 11,
    high: 13,
    low: 10,
    close: 12,
    volume: 110,
    amount: 1_100,
  }],
  meta: {
    field_version: "v1",
    source: "trade_sector_daily",
    bar_count: 2,
    skipped_bar_count: 0,
    warmup_target: 100,
  },
};

/** 输入：任意 API 响应体；输出：模拟的成功 fetch 调用。 */
function mockSuccess(body: unknown) {
  vi.stubGlobal("fetch", vi.fn().mockResolvedValue(new Response(JSON.stringify(body))));
}

describe("fetchSectorKline", () => {
  it("拒绝字符串数值和不合法 OHLC，避免图表引擎接收脏数据", async () => {
    mockSuccess({
      ...validResponse,
      bars: [{ ...validResponse.bars[0], close: "10.5", high: 9 }],
    });

    await expect(fetchSectorKline("半导体", 2, "2026-08-06")).rejects.toThrow();
  });

  it("拒绝非升序、重复或晚于请求截止日的交易日", async () => {
    mockSuccess({
      ...validResponse,
      bars: [
        validResponse.bars[1],
        { ...validResponse.bars[1], trade_date: "2026-08-07", timestamp: 1786032000000 },
      ],
    });

    await expect(fetchSectorKline("半导体", 2, "2026-08-06")).rejects.toThrow();
  });

  it("编码行业、层级和截止日，并向 fetch 透传取消信号", async () => {
    const controller = new AbortController();
    const fetchMock = vi.fn().mockResolvedValue(new Response(JSON.stringify(validResponse)));
    vi.stubGlobal("fetch", fetchMock);

    await expect(fetchSectorKline("半导体 设备", 2, "2026-08-06", controller.signal)).resolves.toMatchObject({
      sector_name: "半导体",
    });

    const [url, init] = fetchMock.mock.calls[0] as [string, RequestInit];
    const query = new URL(url).searchParams;
    expect(query.get("sector_name")).toBe("半导体 设备");
    expect(query.get("level")).toBe("2");
    expect(query.get("end_date")).toBe("2026-08-06");
    expect(init.signal).toBe(controller.signal);
  });
});
