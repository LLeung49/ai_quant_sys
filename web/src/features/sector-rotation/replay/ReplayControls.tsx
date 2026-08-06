/** 全市场回放的播放、步进和时间轴控件。 */
import type { ReplayAction, ReplaySpeed } from "./replayState";

interface ReplayControlsProps { dates: string[]; index: number; playing: boolean; speed?: ReplaySpeed; dispatch: (action: ReplayAction) => void; }

/**
 * 渲染受控的逐日回放操作区。
 *
 * 输入：日期数组、当前指针、播放状态和 reducer 分发函数。
 * 输出：可键盘操作的播放、步进和时间轴控件。
 */
export function ReplayControls({ dates, index, playing, speed = 1, dispatch }: ReplayControlsProps) {
  const last = Math.max(0, dates.length - 1);
  return <section className="replay-controls" aria-label="全市场回放控制">
    <button type="button" aria-label="上一帧" onClick={() => dispatch({ type: "PREVIOUS" })}>‹</button>
    <button type="button" aria-label={playing ? "暂停回放" : "播放回放"} onClick={() => dispatch({ type: playing ? "PAUSE" : "PLAY" })}>{playing ? "暂停" : "播放"}</button>
    <button type="button" aria-label="下一帧" onClick={() => dispatch({ type: "NEXT" })}>›</button>
    <input aria-label="回放日期时间轴" type="range" min={0} max={last} value={index} onChange={(event) => dispatch({ type: "SEEK", index: Number(event.target.value) })} />
    <output>{dates[index] ?? "暂无日期"}</output>
    <label className="replay-speed"><span>速度</span><select aria-label="回放速度" value={speed} onChange={(event) => dispatch({ type: "SET_SPEED", speed: Number(event.target.value) as ReplaySpeed })}><option value={0.5}>0.5×</option><option value={1}>1×</option><option value={2}>2×</option></select></label>
  </section>;
}
