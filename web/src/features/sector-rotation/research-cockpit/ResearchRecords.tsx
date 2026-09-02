import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { fetchDecisions, fetchWatchlist, removeFromWatchlist, updateWatchlist } from "./api";

export function ResearchRecords() {
  const client = useQueryClient();
  const refresh = () => void client.invalidateQueries({ queryKey: ["research-watchlist"] });
  const update = useMutation({ mutationFn: ({ snapshotId, status }: { snapshotId: number; status: "watch" | "paused" | "done" }) => updateWatchlist(snapshotId, status), onSuccess: refresh });
  const remove = useMutation({ mutationFn: removeFromWatchlist, onSuccess: refresh });
  const watch = useQuery({ queryKey: ["research-watchlist"], queryFn: fetchWatchlist });
  const decisions = useQuery({ queryKey: ["research-decisions"], queryFn: fetchDecisions });
  const watched = (watch.data as { items?: Array<{ snapshot_id: number; entity_code: string; strategy_type: string; watch_status: "watch" | "paused" | "done" }> } | undefined)?.items ?? [];
  const logged = (decisions.data as { decisions?: Array<{ entity_code: string; decision: string; note?: string }> } | undefined)?.decisions ?? [];
  return <section className="research-cockpit-panel"><header><div><p className="eyebrow">HUMAN RESEARCH LOG</p><h2>观察清单与人工决定</h2></div></header><div className="research-records-grid"><div><strong>观察清单</strong>{watched.length === 0 ? <p className="research-muted">暂无记录</p> : watched.slice(0, 8).map((item) => <p className="research-record" key={`${item.entity_code}-${item.strategy_type}`}><span>{item.entity_code}</span><small>{item.watch_status}</small><span className="research-row-actions"><button type="button" disabled={update.isPending} onClick={() => update.mutate({ snapshotId: item.snapshot_id, status: item.watch_status === "watch" ? "paused" : "watch" })}>{item.watch_status === "watch" ? "暂停" : "恢复"}</button><button type="button" disabled={remove.isPending} onClick={() => remove.mutate(item.snapshot_id)}>移除</button></span></p>)}</div><div><strong>最近决定</strong>{logged.length === 0 ? <p className="research-muted">暂无记录</p> : logged.slice(0, 8).map((item, index) => <p className="research-record" key={`${item.entity_code}-${index}`}><span>{item.entity_code}</span><small>{item.decision}</small></p>)}</div></div></section>;
}
