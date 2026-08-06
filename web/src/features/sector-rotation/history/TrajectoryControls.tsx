/** 最多五个行业的轨迹对比选择状态。 */
import { X } from "lucide-react";
import { MAX_TRAJECTORY_SECTORS, TRAJECTORY_COLORS } from "./constants";

interface TrajectoryControlsProps {
  /** 当前进入轨迹对比的行业，调用方保证不超过五个。 */
  sectorNames: string[];
  /** 输入：待移除行业；输出：通知页面更新历史查询。 */
  onRemove: (sectorName: string) => void;
}

/**
 * 展示轨迹对比行业及移除入口。
 *
 * 输入：一至五个行业名称和移除回调。
 * 输出：带稳定颜色序号的可键盘操作行业标签。
 */
export function TrajectoryControls({ sectorNames, onRemove }: TrajectoryControlsProps) {
  return <div className="trajectory-controls" aria-label="轨迹对比行业">
    {sectorNames.map((sectorName, index) => <button key={sectorName} type="button" aria-label={`移除 ${sectorName}`} onClick={() => onRemove(sectorName)}><i style={{ background: TRAJECTORY_COLORS[index] }} />{sectorName}<X aria-hidden="true" size={11} /></button>)}
    <span>{sectorNames.length >= MAX_TRAJECTORY_SECTORS
      ? `已选择 ${sectorNames.length}/${MAX_TRAJECTORY_SECTORS} 个行业`
      : `已选择 ${sectorNames.length}/${MAX_TRAJECTORY_SECTORS} 个行业，可点击气泡或排行榜继续加入`}</span>
  </div>;
}
