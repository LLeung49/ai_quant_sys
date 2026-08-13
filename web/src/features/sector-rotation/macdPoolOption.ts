export type MacdPoint = {
  name: string; code: string; er: number; adx: number; volume: number; momentum: number;
  rsi?: number | null; hurst?: number | null; hist?: number | null; entityType?: string; gcAge?: number | null;
};
export type MacdTrajectory = {
  stock_code: string;
  points: Array<{ as_of_date: string; er: number | null; adx: number | null }>;
};

export function buildMacdPoolOption(points: MacdPoint[], trajectory?: MacdTrajectory | null, selectedCode?: string | null) {
  const data = points.map((point) => ({
    name: point.name,
    value: [point.er, point.adx, point.volume],
    point,
    symbol: point.entityType === "etf" ? "circle" : point.entityType === "sector_l1" ? "diamond" : "triangle",
    itemStyle: {
      color: point.momentum >= 0 ? "#f04f5f" : "#26a69a",
      borderColor: selectedCode === point.code ? "#ffffff" : "#dce8f8",
      borderWidth: selectedCode === point.code ? 3 : 1.2,
      opacity: selectedCode === point.code ? 1 : selectedCode ? 0.45 : Math.max(0.42, 1 - Math.min(point.gcAge ?? 10, 10) * 0.055),
      shadowBlur: 8,
      shadowColor: "rgba(0,0,0,.25)",
    },
  }));
  const path = trajectory?.points
    .filter((point) => point.er != null && point.adx != null)
    .map((point, index, validPoints) => ({
      value: [point.er as number, point.adx as number],
      asOfDate: point.as_of_date,
      label: index === 0 ? "起点" : index === validPoints.length - 1 ? "当前" : "",
    })) ?? [];
  const series: object[] = [{
    type: "scatter" as const,
    data,
    symbolSize: (value: number[]) => Math.max(12, Math.min(48, 20 + value[2] * 16)),
    label: { show: true, position: "top", color: "#dce8f8", fontSize: 10, formatter: "{b}" },
    labelLayout: { hideOverlap: true, moveOverlap: "shiftY" as const },
    emphasis: { focus: "self", scale: 1.2 },
    markArea: { silent: true, data: [
      [{ xAxis: 0.6, yAxis: 25, itemStyle: { color: "rgba(55,214,176,.08)" } }, { xAxis: 1, yAxis: 80 }],
      [{ xAxis: 0.6, yAxis: 0, itemStyle: { color: "rgba(240,182,90,.05)" } }, { xAxis: 1, yAxis: 25 }],
      [{ xAxis: 0, yAxis: 0, itemStyle: { color: "rgba(255,114,133,.04)" } }, { xAxis: 0.6, yAxis: 25 }],
      [{ xAxis: 0, yAxis: 25, itemStyle: { color: "rgba(145,133,255,.04)" } }, { xAxis: 0.6, yAxis: 80 }],
    ] },
  }];
  if (path.length > 1) {
    series.push({
      type: "line", data: path, symbol: "circle", symbolSize: 7, z: 5,
      lineStyle: { color: "#ffd166", width: 2, type: "solid" },
      itemStyle: { color: "#ffd166", borderColor: "#fff", borderWidth: 1 },
      endLabel: { show: true, formatter: "当前", color: "#ffd166", fontSize: 10 },
      label: { show: true, formatter: (params: { data: { label: string } }) => params.data.label, color: "#ffd166", fontSize: 10, fontWeight: 700 },
    });
  }
  return {
    animationDuration: 420, animationEasing: "cubicOut" as const,
    grid: { left: 64, right: 54, top: 42, bottom: 58 },
    tooltip: {
      trigger: "item", renderMode: "html" as const, confine: true, backgroundColor: "rgba(9,18,32,.96)", borderColor: "#30445f", padding: 14, textStyle: { color: "#dce8f8", fontSize: 12 },
      formatter: (params: { data: { point?: MacdPoint; asOfDate?: string; value?: number[] } }) => {
        const p = params.data?.point;
        if (!p) return params.data?.asOfDate ? `${params.data.asOfDate}<br/>KAMA ER：${params.data.value?.[0].toFixed(2)}<br/>ADX：${params.data.value?.[1].toFixed(1)}` : "ER × ADX 轨迹";
        return `<strong>${p.name}</strong><br/>代码：${p.code}<br/>KAMA ER：${p.er.toFixed(2)}<br/>ADX：${p.adx.toFixed(1)}<br/>量比：${p.volume.toFixed(2)}<br/>距金叉：${p.gcAge == null ? "未知" : `T-${p.gcAge}`}<br/>MACD柱：${p.hist == null ? "待补" : p.hist.toFixed(4)}<br/>RSI：${p.rsi == null ? "待补" : p.rsi.toFixed(1)}<br/>Hurst：${p.hurst == null ? "待补" : p.hurst.toFixed(2)}`;
      },
    },
    xAxis: { type: "value", min: 0, max: 1, name: "趋势效率 KAMA ER →", nameLocation: "middle", nameGap: 34, axisLine: { lineStyle: { color: "#62728a" } }, axisLabel: { color: "#7f8da3" }, splitLine: { lineStyle: { color: "rgba(92,112,140,.16)" } } },
    yAxis: { type: "value", min: 0, name: "趋势强度 ADX ↑", nameLocation: "middle", nameGap: 44, axisLine: { lineStyle: { color: "#62728a" } }, axisLabel: { color: "#7f8da3" }, splitLine: { lineStyle: { color: "rgba(92,112,140,.16)" } } },
    series,
  };
}
