/** 基于预加载历史快照的全市场逐日象限回放视图。 */
import { useEffect, useMemo, useReducer } from "react";
import { QuadrantChart, type QuadrantSector } from "../chart/QuadrantChart";
import { ReplayControls } from "./ReplayControls";
import { initialReplayState, replayReducer } from "./replayState";

export interface ReplayPoint extends QuadrantSector { as_of_date: string; }
interface MarketReplayProps { points: ReplayPoint[]; }

/**
 * 将预加载的全市场快照按交易日播放。
 *
 * 输入：同一模型版本、同一行业层级的历史点。
 * 输出：当前日期的象限帧与播放时间轴；播放过程中不发送新的 HTTP 请求。
 */
export function MarketReplay({ points }: MarketReplayProps) {
  const dates = useMemo(() => [...new Set(points.map((point) => point.as_of_date))].sort(), [points]);
  const [state, dispatch] = useReducer(replayReducer, dates, initialReplayState);
  useEffect(() => { if (!state.playing) return undefined; const timer = window.setInterval(() => dispatch({ type: "NEXT" }), 900 / state.speed); return () => window.clearInterval(timer); }, [state.playing, state.speed]);
  const currentDate = state.dates[state.index];
  const frame = points.filter((point) => point.as_of_date === currentDate);
  return <section className="market-replay" aria-label="全市场轮动回放"><ReplayControls dates={state.dates} index={state.index} playing={state.playing} speed={state.speed} dispatch={dispatch} /><QuadrantChart sectors={frame} /></section>;
}
