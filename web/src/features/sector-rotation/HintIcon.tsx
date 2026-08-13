/** v2_short_term + 板块轮动共用的悬停/点击提示图标。 */
import { useId, useState } from "react";
import { CircleAlert } from "lucide-react";

interface HintIconProps {
  /** 鼠标悬停或点击后展示的说明文字。 */
  text: string;
  /** 无障碍标签；缺省回退到 text。 */
  ariaLabel?: string;
  /** 显式指定 tooltip 出现位置，默认在图标左侧。 */
  placement?: "left" | "right" | "top" | "bottom";
  /** 视觉风格：v2_short_term 橙调 / sector-rotation 蓝调。 */
  tone?: "warm" | "cool";
}

/**
 * 圆圈 + 感叹号图标，悬停或点击展示说明文字。
 *
 * 输入：要展示的说明文字、可选的位置与色调。
 * 输出：自包含的图标 + 暗色 tooltip；点击会切换锁定状态，鼠标离开自动关闭。
 */
export function HintIcon({ text, ariaLabel, placement = "left", tone = "warm" }: HintIconProps) {
  const [hover, setHover] = useState(false);
  const [pinned, setPinned] = useState(false);
  const open = hover || pinned;
  const tooltipId = useId();

  return (
    <span
      className={`hint-icon-wrapper hint-icon-wrapper--${tone} hint-icon-wrapper--${placement} ${open ? "is-open" : ""}`}
      onMouseEnter={() => setHover(true)}
      onMouseLeave={() => setHover(false)}
    >
      <button
        type="button"
        className="hint-icon"
        aria-label={ariaLabel ?? text}
        aria-expanded={open}
        aria-describedby={open ? tooltipId : undefined}
        onClick={() => setPinned((prev) => !prev)}
      >
        <CircleAlert aria-hidden="true" size={12} />
      </button>
      <span id={tooltipId} className="hint-icon__tooltip" role="tooltip">
        {text}
      </span>
    </span>
  );
}
