/** v2_short_term 短期异动页面：KPI + 异动榜。气泡图因解读价值有限已下线。 */
import { useMemo, useState } from "react";
import { useQuery } from "@tanstack/react-query";
import { CalendarRange } from "lucide-react";
import { fetchShortTermAvailableDates, fetchShortTermSnapshot, type ShortTermSector } from "./api";
import { SHORT_TERM_LABEL_WHITELIST, type ShortTermLabel } from "./api";
import { ShortTermKpi } from "./ShortTermKpi";
import { ShortTermLeaders } from "./ShortTermLeaders";
import { ShortTermDetailDrawer } from "./ShortTermDetailDrawer";

const DEFAULT_LEVEL: 1 | 2 = 2;
const DEFAULT_MODEL = "v2_short_term";

const LABEL_FILTER_OPTIONS: Array<{ value: ShortTermLabel | "all"; label: string }> = [
  { value: "all", label: "全部标签" },
  { value: "pulse_up", label: "单日脉冲上涨" },
  { value: "pulse_down", label: "单日脉冲下跌" },
  { value: "extreme_up", label: "单日极端上涨" },
  { value: "extreme_down", label: "单日极端下跌" },
  { value: "volume_spike", label: "量能异动" },
  { value: "limit_cluster", label: "涨停集群" },
  { value: "limit_panic", label: "跌停集群" },
  { value: "short_rebound_candidate", label: "短期反弹候选" },
  { value: "short_breakdown_candidate", label: "短期走弱候选" },
];

function isLabel(value: string): value is ShortTermLabel {
  return (SHORT_TERM_LABEL_WHITELIST as readonly string[]).includes(value);
}

/** 板块至少命中一个标签或强度档位非 none 时才算有异动。 */
function hasAnomaly(sector: ShortTermSector): boolean {
  if (sector.short_term_intensity && sector.short_term_intensity !== "none") return true;
  const labels = (sector.short_term_labels ?? "").split(",").map((part) => part.trim()).filter(Boolean);
  return labels.length > 0;
}

/**
 * 短期异动独立页面：顶部 KPI、异动榜，板块详情抽屉。
 *
 * 输入：无；状态由 URL 与用户交互驱动。
 * 输出：完整的异动观察页面，可在 ``App.tsx`` 中作为单独标签页渲染。
 */
export function ShortTermPage() {
  const [level, setLevel] = useState<1 | 2>(DEFAULT_LEVEL);
  const [selectedDate, setSelectedDate] = useState<string | undefined>(undefined);
  const [selectedSectorName, setSelectedSectorName] = useState<string | null>(null);
  const [labelFilter, setLabelFilter] = useState<ShortTermLabel | "all">("all");

  const availableDatesQuery = useQuery({
    queryKey: ["short-term-available-dates", level],
    queryFn: () => fetchShortTermAvailableDates(level, DEFAULT_MODEL),
    staleTime: 5 * 60 * 1000,
  });

  const fallbackDate = useMemo(() => {
    const dates = availableDatesQuery.data?.dates ?? [];
    return dates[0];
  }, [availableDatesQuery.data]);

  const effectiveDate = selectedDate ?? fallbackDate;

  const snapshotQuery = useQuery({
    queryKey: ["short-term-snapshot", level, effectiveDate],
    queryFn: () => fetchShortTermSnapshot(effectiveDate, level, DEFAULT_MODEL),
    enabled: Boolean(effectiveDate),
  });

  const sectors = snapshotQuery.data?.sectors ?? [];
  const isScoreEligible = (sector: ShortTermSector) => Boolean(sector.score_eligible);
  const filteredSectors = useMemo<ShortTermSector[]>(() => {
    const base = sectors.filter((sector) => isScoreEligible(sector) && hasAnomaly(sector));
    if (labelFilter === "all") return base;
    return base.filter((sector) => (sector.short_term_labels ?? "").split(",").includes(labelFilter));
  }, [sectors, labelFilter]);

  const selectedSector = useMemo<ShortTermSector | null>(() => {
    if (!selectedSectorName) return null;
    return sectors.find((sector) => sector.sector_name === selectedSectorName) ?? null;
  }, [sectors, selectedSectorName]);

  const meta = snapshotQuery.data?.meta;
  const summaryText = useMemo(() => {
    if (!meta) return "";
    const eligible = meta.eligible_sector_count ?? null;
    const skipped = meta.skipped_sector_count ?? null;
    if (eligible == null) return "";
    if (skipped == null) return `评分行业 ${eligible}`;
    return `评分行业 ${eligible} / 总计 ${eligible + skipped}`;
  }, [meta]);

  return (
    <div className="short-term-page">
      <header className="short-term-toolbar">
        <div className="short-term-toolbar__group">
          <label className="short-term-toolbar__date">
            <CalendarRange aria-hidden="true" size={14} />
            <input
              type="date"
              value={effectiveDate ?? ""}
              onChange={(event) => setSelectedDate(event.target.value || undefined)}
              aria-label="选择交易日"
            />
          </label>
          <div className="segmented-control" role="group" aria-label="行业层级">
            {([1, 2] as const).map((optionLevel) => (
              <button
                key={optionLevel}
                type="button"
                className={level === optionLevel ? "is-active" : ""}
                aria-pressed={level === optionLevel}
                onClick={() => setLevel(optionLevel)}
              >
                {optionLevel === 1 ? "申万一级" : "申万二级"}
              </button>
            ))}
          </div>
          <label className="short-term-toolbar__filter">
            <span>标签</span>
            <select value={labelFilter} onChange={(event) => {
              const next = event.target.value;
              setLabelFilter(next === "all" || isLabel(next) ? next : "all");
            }}>
              {LABEL_FILTER_OPTIONS.map((option) => (
                <option key={option.value} value={option.value}>{option.label}</option>
              ))}
            </select>
          </label>
        </div>
        <div className="short-term-toolbar__meta">
          {availableDatesQuery.data?.dates && availableDatesQuery.data.dates.length > 0 && (
            <span><strong>最近成功日期</strong> {availableDatesQuery.data.dates[0]}</span>
          )}
          {meta?.source_max_trade_date && (
            <span><strong>上游行情截至</strong> {meta.source_max_trade_date}</span>
          )}
          {meta?.field_version && (
            <span className="short-term-toolbar__version">{meta.field_version}</span>
          )}
        </div>
      </header>

      {availableDatesQuery.isLoading && <div className="empty-panel" role="status">正在加载可用日期…</div>}
      {!availableDatesQuery.isLoading && !effectiveDate && (
        <div className="empty-panel" role="status">
          当前模型版本（{DEFAULT_MODEL}）暂无可用快照。请确认后端是否已成功运行。
        </div>
      )}
      {effectiveDate && snapshotQuery.isLoading && <div className="empty-panel" role="status">短期异动快照加载中…</div>}
      {snapshotQuery.isError && (
        <div className="empty-panel" role="status">
          短期异动数据加载失败：{snapshotQuery.error instanceof Error ? snapshotQuery.error.message : "未知错误"}
        </div>
      )}
      {snapshotQuery.data && (
        <>
          <ShortTermKpi meta={meta} />
          {summaryText && <p className="short-term-summary-note" role="note">{summaryText}</p>}
          <ShortTermLeaders
            sectors={filteredSectors}
            selectedSectorName={selectedSectorName}
            onSelect={(name) => setSelectedSectorName(name)}
          />
        </>
      )}

      <ShortTermDetailDrawer sector={selectedSector} onClose={() => setSelectedSectorName(null)} />
    </div>
  );
}