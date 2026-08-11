import { buildLifecycleBands, type LifecyclePoint } from "../lifecycle/derive";
import { getLifecycleMeta } from "../lifecycle/meta";

interface LifecycleBandsProps {
  sectorNames: string[];
  points: LifecyclePoint[];
  expectedDates: string[];
}

/** 以语义化列表展示最多五个行业的 Lifecycle 历史区间。 */
export function LifecycleBands({ sectorNames, points, expectedDates }: LifecycleBandsProps) {
  return <section className="lifecycle-bands" aria-label="Lifecycle 历史状态带">
    {sectorNames.slice(0, 5).map((sectorName) => <article key={sectorName}>
      <strong>{sectorName}</strong>
      <ol>{buildLifecycleBands(points.filter((point) => point.sector_name === sectorName), expectedDates).map((band) =>
        <li key={`${sectorName}-${band.startDate}`} data-state={band.state ?? "unknown"}>
          <span>{band.gap ? "数据缺口" : getLifecycleMeta(band.state).label}</span>
          <small>{band.startDate} 至 {band.endDate} · {band.tradingDays} 日</small>
        </li>,
      )}</ol>
    </article>)}
  </section>;
}
