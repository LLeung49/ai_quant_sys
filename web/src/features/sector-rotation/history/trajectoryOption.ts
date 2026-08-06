/** 板块轮动历史轨迹的 ECharts 配置生成器。 */
import { MAX_TRAJECTORY_SECTORS, TRAJECTORY_COLORS } from "./constants";

interface TrajectoryPoint { as_of_date: string; velocity_score: number | null; acceleration_score: number | null; }
interface SectorTrajectory { sector_name: string; points: TrajectoryPoint[]; }

/**
 * 构建最多五行业的固定象限轨迹配置。
 *
 * 输入：按日期升序的历史坐标；任一坐标缺失时保留 ``null`` 断点。
 * 输出：不插值、不预测的 ECharts 折线散点轨迹配置。
 */
export function buildTrajectoryOption(trajectories: SectorTrajectory[]) {
  return {
    animationDuration: 380,
    grid: { left: 64, right: 30, top: 36, bottom: 54 },
    tooltip: {
      trigger: "item",
      backgroundColor: "rgba(9, 18, 32, .96)",
      borderColor: "#30445f",
      textStyle: { color: "#dce8f8" },
      formatter: (params: { seriesName: string; data?: { value: number[]; as_of_date: string } }) => {
        if (!params.data) return "数据缺口：该交易日未形成有效坐标";
        return `<div class="chart-tooltip-title">${params.seriesName}<span>${params.data.as_of_date}</span></div><div class="chart-tooltip-grid"><span>趋势速度</span><b>${params.data.value[0].toFixed(2)}</b><span>趋势加速度</span><b>${params.data.value[1].toFixed(2)}</b></div><div class="chart-tooltip-note">折线按成功交易日连接，缺失点不插值</div>`;
      },
    },
    xAxis: { type: "value", min: -1, max: 1, interval: .5, name: "趋势速度（相对得分）", nameLocation: "middle", nameGap: 36, axisLabel: { color: "#7f8da3" }, axisLine: { lineStyle: { color: "#62728a" } }, splitLine: { lineStyle: { color: "rgba(92,112,140,.16)" } } },
    yAxis: { type: "value", min: -1, max: 1, interval: .5, name: "趋势加速度（相对得分）", nameLocation: "middle", nameGap: 44, axisLabel: { color: "#7f8da3" }, axisLine: { lineStyle: { color: "#62728a" } }, splitLine: { lineStyle: { color: "rgba(92,112,140,.16)" } } },
    series: trajectories.slice(0, MAX_TRAJECTORY_SECTORS).map((trajectory, index) => {
      const latestValidIndex = trajectory.points.reduce(
        (latest, point, pointIndex) => point.velocity_score !== null && point.acceleration_score !== null ? pointIndex : latest,
        -1,
      );
      return {
        type: "line", name: trajectory.sector_name, connectNulls: false,
        data: trajectory.points.map((point, pointIndex) => point.velocity_score === null || point.acceleration_score === null ? null : ({ value: [point.velocity_score, point.acceleration_score], as_of_date: point.as_of_date, isLatest: pointIndex === latestValidIndex })),
        lineStyle: { width: 2, color: TRAJECTORY_COLORS[index], opacity: .72 },
        itemStyle: { color: TRAJECTORY_COLORS[index], borderColor: "#dce8f8", borderWidth: 1 },
        symbolSize: (_value: number[], params: { data?: { isLatest?: boolean } }) => params.data?.isLatest ? 13 : 7,
        emphasis: { focus: "series" },
      };
    }),
  };
}
