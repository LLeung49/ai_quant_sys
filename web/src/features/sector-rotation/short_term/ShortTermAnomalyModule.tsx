/** 板块轮动工作台内嵌入的"短期异动模块":2x2 KPI 加异动榜与候选面板。*/
import { useCallback, useMemo, useState } from "react";
import { useQuery } from "@tanstack/react-query";
import { CalendarRange, Filter } from "lucide-react";
import { fetchShortTermAvailableDates, SHORT_TERM_LABEL_WHITELIST, type ShortTermLabel, type ShortTermSector } from "./api";
import { ShortTermKpi } from "./ShortTermKpi";
import { ShortTermLeaders } from "./ShortTermLeaders";
import { NextDayWatchPanel } from "./NextDayWatchPanel";
import { HintIcon } from "../HintIcon";
import { parseLabelsCsv } from "./labels";
import { useShortTermHaloSectors } from "./useShortTermHaloSectors";
import { SectorDetailDrawer } from "../detail/SectorDetailDrawer";
import { useRotationData } from "../useRotationData";
import type { SectorPoint } from "../api";

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

/** 板块至少命中一个标签或强度档位非 none 时才算有异动。*/
function hasAnomaly(sector: ShortTermSector): boolean {
  if (sector.short_term_intensity && sector.short_term_intensity !== "none") return true;
  return parseLabelsCsv(sector.short_term_labels).length > 0;
}

/**
 * v1 sector 转换为 SectorDetailDrawer 所需的最小 DetailSector 形状。
 *
 * 输入:完整的 SectorPoint(可能含 null 字段)。
 * 输出:Drawer 关心的可空字段集合,保证生命周期与得分字段类型一致。
 *
 * 注:SectorDetailDrawer 中的字段大多标记为可空,这里透传即可;phase 字段缺失时
 * 由 Drawer 内部 fallback 到 "neutral"。
 */
function toDetailSector(sector: SectorPoint) {
  const num = (v: unknown): number | null => (typeof v === "number" && !Number.isNaN(v) ? v : null);
  const numOpt = (v: unknown): number | null | undefined => {
    if (v == null) return v as null | undefined;
    return typeof v === "number" && !Number.isNaN(v) ? v : null;
  };
  const str = (v: unknown): string | null => (typeof v === "string" ? v : null);  return {
    sector_name: sector.sector_name,
    phase_confirmed: str(sector.phase_confirmed),
    phase_age: numOpt(sector.phase_age),
    phase_confidence: num(sector.phase_confidence),
    composite_rank: num(sector.composite_rank),
    rank_change_1d: num(sector.rank_change_1d),
    coverage_ratio: numOpt(sector.coverage_ratio),
    trend_level_score: num(sector.trend_level_score),
    velocity_score: num(sector.velocity_score),
    acceleration_score: num(sector.acceleration_score),
    participation_score: num(sector.participation_score),
    volume_score: num(sector.volume_score),
    lifecycle_state: sector.lifecycle_state ?? null,
    lifecycle_reason: sector.lifecycle_reason ?? null,
    lifecycle_changed: sector.lifecycle_changed == null ? null : Boolean(sector.lifecycle_changed),
    lifecycle_age: numOpt(sector.lifecycle_age),
  };
}

export interface ShortTermAnomalyModuleProps {
  /** 与板块轮动页面共享的当日行业层级。*/
  level: 1 | 2;
  /** 与板块轮动页面共享的当前成功快照日期。未提供时会自动回退到最近可用日期。*/
  asOfDate: string;
  /** 作为层级提供的最近成功日期列表,未提供则不展示。*/
  availableDates?: string[];
  /** 输入:点击名称;输出:通知父页面同步选中状态以打开详情抽屉。*/
  onSectorSelect?: (sectorName: string) => void;
}

/**
 * 渲染"短期异动模块":2x2 KPI 加异动榜的统一面板。
 *
 * 输入:与板块轮动页面共享的行业层级与当前日期,可选参数由父页面控制。
 * 输出:与主面板调性一致的"市场环境"同一层级的短期异动面板,包含标题、KPI 与异动榜。
 *
 * 数据请求统一通过 useShortTermHaloSectors / useRotationData hooks,与 SectorRotationPage 共用 queryKey
 * 以实现 TanStack Query 自动 dedupe,避免在两个组件里都调用底层 fetch。
 */
export function ShortTermAnomalyModule({ level, asOfDate, availableDates, onSectorSelect }: ShortTermAnomalyModuleProps) {
  const [labelFilter, setLabelFilter] = useState<ShortTermLabel | "all">("all");
  const [selectedSectorName, setSelectedSectorName] = useState<string | null>(null);

  const availableDatesQuery = useQuery({
    queryKey: ["short-term-available-dates", level],
    queryFn: () => fetchShortTermAvailableDates(level),
    staleTime: 5 * 60 * 1000,
    enabled: !availableDates,
  });

  const effectiveAvailableDates = availableDates ?? availableDatesQuery.data?.dates;

  const haloQuery = useShortTermHaloSectors(level, asOfDate);
  const sectors = haloQuery.sectors;
  const meta = haloQuery.snapshot?.meta ?? null;
  const isLatestDate = asOfDate != null && effectiveAvailableDates?.[0] === asOfDate;

  // 拉取 v1 快照,只为详情抽屉提供 lifecycle / phase / 评分族字段;与 SectorRotationPage 共用 queryKey。
  const v1Rotation = useRotationData(level, "v1", asOfDate);
  const v1Sectors = useMemo<SectorPoint[]>(
    () => (v1Rotation.snapshot.data?.sectors ?? []) as SectorPoint[],
    [v1Rotation.snapshot.data],
  );

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

  const selectedV1Sector = useMemo(() => {
    if (!selectedSectorName) return null;
    return v1Sectors.find((sector) => sector.sector_name === selectedSectorName) ?? null;
  }, [v1Sectors, selectedSectorName]);

  const handleSelect = useCallback((name: string) => {
    setSelectedSectorName(name);
    onSectorSelect?.(name);
  }, [onSectorSelect]);

  const lastSuccessDate = effectiveAvailableDates?.[0];
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
            text="同一快照日期下的极短期异动示例，右侧可点击详情。"
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
        {sourceCutoff && <span><strong>上交所行情截止</strong> {sourceCutoff}</span>}
        {summaryText && <span className="short-term-anomaly__summary">{summaryText}</span>}
      </div>

      <div className="short-term-anomaly__kpi short-term-anomaly__kpi--top">
        <ShortTermKpi meta={meta ?? undefined} layout="grid" onSectorSelect={handleSelect} />
      </div>
      <NextDayWatchPanel sectors={sectors} onSelect={handleSelect} />
      <div className="short-term-anomaly__heatmaps">
        <ShortTermLeaders direction="up" sectors={filteredSectors} selectedSectorName={selectedSectorName} onSelect={handleSelect} />
        <ShortTermLeaders direction="down" sectors={filteredSectors} selectedSectorName={selectedSectorName} onSelect={handleSelect} />
      </div>

      {selectedV1Sector && (
        <SectorDetailDrawer
          sector={toDetailSector(selectedV1Sector)}
          shortTerm={selectedSector}
          level={level}
          asOfDate={asOfDate}
          isLatestDate={isLatestDate}
          onClose={() => setSelectedSectorName(null)}
        />
      )}
    </section>
  );
}