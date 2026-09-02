import { ShieldCheck } from "lucide-react";

export function ResearchStatusBadge({ status = "shadow", execution = "manual_only" }: { status?: string; execution?: string }) {
  return <span className="research-status-badge" title="研究影子输出，不代表已验证交易信号"><ShieldCheck size={13} aria-hidden="true" />{status.toUpperCase()} · {execution === "manual_only" ? "MANUAL ONLY" : execution.toUpperCase()}</span>;
}
