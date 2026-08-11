import { LIFECYCLE_STATES, type LifecycleFilter, type LifecycleSectorFields, type LifecycleState } from "./meta";

export interface LifecyclePoint extends LifecycleSectorFields {
  as_of_date: string;
  sector_name: string;
}

export interface LifecycleSummaryCounts {
  trending: number;
  repairOrEmerging: number;
  risk: number;
  changed: number;
  insufficient: number;
}

export interface LifecycleBand {
  state: string | null;
  startDate: string;
  endDate: string;
  tradingDays: number;
  gap: boolean;
}

const FILTER_STATES: Record<Exclude<LifecycleFilter, "all">, readonly LifecycleState[]> = {
  repair: ["repair"],
  emerging: ["emerging"],
  trending: ["trending"],
  crowded: ["crowded"],
  divergence: ["divergence"],
  exit: ["exit"],
  neutral: ["neutral"],
  repair_or_emerging: ["repair", "emerging"],
  risk: ["crowded", "divergence", "exit"],
};

const isLifecycleState = (value: string | null | undefined): value is LifecycleState =>
  value !== null && value !== undefined && (LIFECYCLE_STATES as readonly string[]).includes(value);

export function hasLifecycleCoverage(sectors: LifecycleSectorFields[]): boolean {
  return sectors.some((sector) => isLifecycleState(sector.lifecycle_state));
}

export function matchesLifecycleFilter(
  sector: LifecycleSectorFields,
  filter: LifecycleFilter,
  changedOnly: boolean,
): boolean {
  if (changedOnly && sector.lifecycle_changed !== true) return false;
  if (filter === "all") return true;
  return FILTER_STATES[filter].includes(sector.lifecycle_state as LifecycleState);
}

export function summarizeLifecycle(sectors: LifecycleSectorFields[]): LifecycleSummaryCounts {
  const summary: LifecycleSummaryCounts = {
    trending: 0,
    repairOrEmerging: 0,
    risk: 0,
    changed: 0,
    insufficient: 0,
  };
  for (const sector of sectors) {
    if (sector.lifecycle_changed === true) summary.changed += 1;
    switch (sector.lifecycle_state) {
      case "trending":
        summary.trending += 1;
        break;
      case "repair":
      case "emerging":
        summary.repairOrEmerging += 1;
        break;
      case "crowded":
      case "divergence":
      case "exit":
        summary.risk += 1;
        break;
      default:
        summary.insufficient += 1;
    }
  }
  return summary;
}

export function findPreviousLifecycle(
  points: LifecyclePoint[],
  sectorName: string,
  asOfDate: string,
): LifecyclePoint | undefined {
  return points
    .filter((point) => point.sector_name === sectorName && point.as_of_date < asOfDate && isLifecycleState(point.lifecycle_state))
    .sort((left, right) => right.as_of_date.localeCompare(left.as_of_date))[0];
}

export function buildLifecycleBands(points: LifecyclePoint[], expectedDates: string[]): LifecycleBand[] {
  const byDate = new Map(points.map((point) => [point.as_of_date, point]));
  const bands: LifecycleBand[] = [];
  for (const date of expectedDates) {
    const point = byDate.get(date);
    const state = point?.lifecycle_state ?? null;
    const gap = !point;
    const previous = bands[bands.length - 1];
    if (!gap && previous && !previous.gap && previous.state === state) {
      previous.endDate = date;
      previous.tradingDays += 1;
      continue;
    }
    bands.push({ state, startDate: date, endDate: date, tradingDays: gap ? 0 : 1, gap });
  }
  return bands;
}
