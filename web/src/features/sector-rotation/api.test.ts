/** 板块轮动 API 客户端对服务端契约的测试。 */
import { describe, expect, it, vi } from "vitest";
import { fetchAvailableDates, fetchCalendarAvailability, fetchReplay, fetchSectorHistory, fetchSnapshot, SectorRotationApiError, sectorPointSchema } from "./api";

describe("板块轮动 API 客户端", () => {
  const meta = { run_status: "succeeded", field_version: "v1", source_max_trade_date: "2026-08-04", eligible_sector_count: 113, skipped_sector_count: 0, market_regime: "high_volatility", regime_multiplier: 0.85 };

  it("保留合法 Lifecycle 字段并兼容旧快照", async () => {
    const current = sectorPointSchema.parse({
      sector_name: "半导体",
      score_eligible: 1,
      lifecycle_state: "trending",
      lifecycle_reason: "rank_and_participation",
      lifecycle_changed: 1,
      lifecycle_age: 3,
    });
    expect(current).toMatchObject({ score_eligible: true, lifecycle_state: "trending", lifecycle_changed: true, lifecycle_age: 3 });
    expect(sectorPointSchema.parse({ sector_name: "银行", score_eligible: true }).lifecycle_state).toBeUndefined();
  });

  it("解析最新日期列表并发送层级和版本参数", async () => {
    const fetchMock = vi.fn().mockResolvedValue(new Response(JSON.stringify({ sector_level: 2, model_version: "v1", dates: ["2026-08-04"], meta: { ...meta, source_max_trade_date: null, eligible_sector_count: null, skipped_sector_count: null, market_regime: null, regime_multiplier: null } })));
    vi.stubGlobal("fetch", fetchMock);

    await expect(fetchAvailableDates(2, "v1")).resolves.toEqual(["2026-08-04"]);
    expect(fetchMock.mock.calls[0][0]).toContain("level=2");
    expect(fetchMock.mock.calls[0][0]).toContain("model_version=v1");
  });

  it("解析月度交易日与快照可用性，并发送显示月的边界", async () => {
    const fetchMock = vi.fn().mockResolvedValue(new Response(JSON.stringify({
      sector_level: 2,
      model_version: "v1",
      trade_dates: ["2026-08-10", "2026-08-11"],
      snapshot_dates: ["2026-08-10"],
      latest_snapshot_date: "2026-08-10",
    })));
    vi.stubGlobal("fetch", fetchMock);

    await expect(fetchCalendarAvailability(2, "v1", "2026-08-01", "2026-08-31")).resolves.toEqual({
      sector_level: 2,
      model_version: "v1",
      trade_dates: ["2026-08-10", "2026-08-11"],
      snapshot_dates: ["2026-08-10"],
      latest_snapshot_date: "2026-08-10",
    });
    expect(fetchMock.mock.calls[0][0]).toContain("start_date=2026-08-01");
    expect(fetchMock.mock.calls[0][0]).toContain("end_date=2026-08-31");
  });

  it("保留快照运行元信息供页面展示数据新鲜度", async () => {
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue(new Response(JSON.stringify({ as_of_date: "2026-08-04", sector_level: 2, model_version: "v1", meta, sectors: [] }))));

    await expect(fetchSnapshot("2026-08-04", 2, "v1")).resolves.toMatchObject({ meta });
  });

  it("将统一错误信封转换为可分支的客户端异常", async () => {
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue(new Response(JSON.stringify({ error: { code: "SNAPSHOT_NOT_FOUND", message: "未找到已成功运行的板块快照", details: null, request_id: "trace-1" } }), { status: 404 })));

    await expect(fetchSnapshot("2026-08-04", 2, "v1")).rejects.toMatchObject({
      name: "SectorRotationApiError",
      code: "SNAPSHOT_NOT_FOUND",
      requestId: "trace-1",
    } satisfies Partial<SectorRotationApiError>);
  });

  it("将最多五个行业编码为重复的轨迹查询参数", async () => {
    const fetchMock = vi.fn().mockResolvedValue(new Response(JSON.stringify({ sector_level: 2, model_version: "v1", meta, points: [] })));
    vi.stubGlobal("fetch", fetchMock);
    await expect(fetchSectorHistory(["半导体", "通信设备", "软件开发", "证券", "贵金属"], "2026-07-01", "2026-08-04", 2, "v1")).resolves.toEqual([]);
    expect(fetchMock.mock.calls[0][0]).toContain("sector_name=%E5%8D%8A%E5%AF%BC%E4%BD%93");
    expect(new URL(String(fetchMock.mock.calls[0][0])).searchParams.getAll("sector_name")).toHaveLength(5);
  });

  it("在发送请求前拒绝第六个轨迹行业", async () => {
    const fetchMock = vi.fn();
    vi.stubGlobal("fetch", fetchMock);

    await expect(fetchSectorHistory(["A", "B", "C", "D", "E", "F"], "2026-07-01", "2026-08-04", 2, "v1")).rejects.toThrow("最多选择 5 个行业");
    expect(fetchMock).not.toHaveBeenCalled();
  });

  it("读取指定日期范围的全市场回放点", async () => {
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue(new Response(JSON.stringify({ sector_level: 2, model_version: "v1", meta, points: [] }))));
    await expect(fetchReplay("2026-07-01", "2026-08-04", 2, "v1")).resolves.toEqual([]);
  });
});
