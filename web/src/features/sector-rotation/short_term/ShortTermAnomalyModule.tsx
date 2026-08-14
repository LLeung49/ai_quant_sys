/** 板块轮动工作台内嵌入的“短期异动模块”： 2×2 KPI 加异动榜。 */
import { useCallback, useMemo, useState } from "react";
import { useQuery } from "@tanstack/react-query";
import { CalendarRange, Filter } from "lucide-react";
import { fetchShortTermAvailableDates, fetchShortTermSnapshot, SHORT_TERM_LABEL_WHITELIST, type ShortTermLabel, type ShortTermSector } from "./api";
import { ShortTermKpi } from "./ShortTermKpi";
import { ShortTermLeaders } from "./ShortTermLeaders";
import { ShortTermDetailDrawer } from "./ShortTermDetailDrawer";
import { NextDayWatchPanel } from "./NextDayWatchPanel";
import { HintIcon } from "../HintIcon";
import { parseLabelsCsv } from "./labels";

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
  return parseLabelsCsv(sector.short_term_labels).length > 0;
}

export interface ShortTermAnomalyModuleProps {
  /** 与板块轮动页面共享的申万行业层级。 */
  level: 1 | 2;
  /** 与板块轮动页面共享的当前成功快照日期。未提供时则会自动退回最近可用日期。 */
  asOfDate: string;
  /** 作为层级提供的最近成功日期列表，未提供则不展示。 */
  availableDates?: string[];
  /** 输入：点击名称；输出：通知父页面同步选中状态以打开详情抽屉。 */
  onSectorSelect?: (sectorName: string) => void;
}

/**
 * 渲染“短期异动模块”： 2×2 KPI 加异动榜的统一面板。
 *
 * 输入：与板块轮动页面共享的行业层级与当前日期，可选参数由父页控制。
 * 输出：与主面板风格一致的“市场环境”同一层级的短期异动面板，包含标题、 KPI 与异动榜以及板块详情抽屉。
 */
export function ShortTermAnomalyModule({ level, asOfDate, availableDates, onSectorSelect }: ShortTermAnomalyModuleProps) {
  const [labelFilter, setLabelFilter] = useState<ShortTermLabel | "all">("all");
  const [selectedSectorName, setSelectedSectorName] = useState<string | null>(null);

  const availableDatesQuery = useQuery({
    queryKey: ["short-term-available-dates", level],
    queryFn: () => fetchShortTermAvailableDates(level, DEFAULT_MODEL),
    staleTime: 5 * 60 * 1000,
    enabled: !availableDates,
  });

  const effectiveAvailableDates = availableDates ?? availableDatesQuery.data?.dates;

  const snapshotQuery = useQuery({
    queryKey: ["short-term-snapshot", level, asOfDate],
    queryFn: () => fetchShortTermSnapshot(asOfDate, level, DEFAULT_MODEL),
    enabled: Boolean(asOfDate),
  });

  const sectors = snapshotQuery.data?.sectors ?? [];
  const meta = snapshotQuery.data?.meta;

  const summaryText = useMemo(() => {
    if (!meta) return "";
    const eligible = meta.eligible_sector_count ?? null;
    const skipped = meta.skipped_sector_count ?? null;
    if (eligible == null) return "";
    if (skipped == null) return `评分行业 ${eligible}`;
    return `评分行业 ${eligible} / 总计 ${eligible + skipped}`;
  }, [meta]);

  const filteredSectors = useMemo<ShortTermSector[]>(() => {
    const base = sectors.filter((sector) => Boolean(sector.score_eligible) && hasAnomaly(sector));
    if (labelFilter === "all") return base;
    return base.filter((sector) => parseLabelsCsv(sector.short_term_labels).includes(labelFilter));
  }, [sectors, labelFilter]);

  const selectedSector = useMemo<ShortTermSector | null>(() => {
    if (!selectedSectorName) return null;
    return sectors.find((sector) => sector.sector_name === selectedSectorName) ?? null;
  }, [sectors, selectedSectorName]);

  const handleSelect = useCallback((name: string) => {
    setSelectedSectorName(name);
    onSectorSelect?.(name);
  }, [onSectorSelect]);

  const lastSuccessDate = effectiveAvailableDates?.[0];
  const fieldVersion = meta?.field_version;
  const sourceCutoff = meta?.source_max_trade_date;

  return (
    <section className="short-term-anomaly" aria-label="短期异动模块">
      <header className="short-term-anomaly__header">
        <div>
          <h2><CalendarRange aria-hidden="true" size={16} />短期异动</h2>
        </div>
        <div className="short-term-anomaly__controls">
          <HintIcon
            tone="cool"
            placement="left"
            text="同一快照日期下的极短期异动示例，右侧供可点击详查。"
          />
          <label className="short-term-anomaly__filter">
            <Filter aria-hidden="true" size={12} />
            <span>标签</span>
            <select aria-label="短期异动标签" value={labelFilter} onChange={(event) => {
              const next = event.target.value;
              setLabelFilter(next === "all" || isLabel(next) ? next : "all");
            }}>
              {LABEL_FILTER_OPTIONS.map((option) => (
                <option key={option.value} value={option.value}>{option.label}</option>
              ))}
            </select>
          </label>
        </div>
      </header>

      <div className="short-term-anomaly__meta">
        {lastSuccessDate && <span><strong>最近成功日期</strong> {lastSuccessDate}</span>}
        {sourceCutoff && <span><strong>上游行情截至</strong> {sourceCutoff}</span>}
        {summaryText && <span className="short-term-anomaly__summary">{summaryText}</span>}
      </div>

      <div className="short-term-anomaly__kpi short-term-anomaly__kpi--top">
        <ShortTermKpi meta={meta} layout="grid" />
      </div>
      <NextDayWatchPanel sectors={sectors} onSelect={handleSelect} />
      <div className="short-term-anomaly__heatmaps">
        <ShortTermLeaders direction="up" sectors={filteredSectors} selectedSectorName={selectedSectorName} onSelect={handleSelect} />
        <ShortTermLeaders direction="down" sectors={filteredSectors} selectedSectorName={selectedSectorName} onSelect={handleSelect} />
      </div>

      <ShortTermDetailDrawer sector={selectedSector} onClose={() => setSelectedSectorName(null)} />
    </section>
  );
}
