"""Archive Repair Alpha forward labels and evaluations before historical replacement."""

from __future__ import annotations

import gzip
import hashlib
import json
from functools import lru_cache
from pathlib import Path

import pymysql.cursors

from data_ingestion.db_config import get_connection


DEFAULT_ROOT = Path("reports/financial-audit/repair-dependencies-20261020")


@lru_cache(maxsize=4)
def archived_bounds(root: Path = DEFAULT_ROOT) -> dict:
    verify_archive(root)
    bounds = {}
    for name in QUERIES:
        maximum_id = 0
        maximum_updated = ""
        with gzip.open(root / f"{name}.jsonl.gz", "rt", encoding="utf-8") as handle:
            for line in handle:
                row = json.loads(line)
                maximum_id = max(maximum_id, int(row["id"]))
                maximum_updated = max(maximum_updated, str(row.get("updated_at") or ""))
        bounds[name] = {"max_id": maximum_id, "max_updated": maximum_updated}
    return bounds

QUERIES = {
    "forward_labels": """
        SELECT f.* FROM sector_rotation_research_forward_label f
        JOIN research_candidate_snapshot s ON s.id=f.source_snapshot_id
        WHERE s.strategy_type='stock_repair'
    """,
    "evaluations": """
        SELECT * FROM sector_rotation_research_evaluation
        WHERE signal_family='stock_repair'
    """,
    "evaluation_metrics": """
        SELECT m.* FROM sector_rotation_research_evaluation_metric m
        JOIN sector_rotation_research_evaluation e ON e.id=m.evaluation_id
        WHERE e.signal_family='stock_repair'
    """,
}


def verify_archive(root: Path = DEFAULT_ROOT) -> dict:
    manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
    for name, details in manifest.items():
        path = root / f"{name}.jsonl.gz"
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != details["sha256"]:
            raise ValueError(f"dependency archive failed verification: {name}")
    return manifest


def archive(root: Path = DEFAULT_ROOT) -> dict:
    if (root / "manifest.json").exists():
        return verify_archive(root)
    root.mkdir(parents=True, exist_ok=True)
    manifest = {}
    for name, query in QUERIES.items():
        path = root / f"{name}.jsonl.gz"
        if path.exists():
            raise FileExistsError(f"incomplete dependency archive: {path}")
        connection = get_connection()
        cursor = connection.cursor(pymysql.cursors.SSDictCursor)
        count = 0
        try:
            cursor.execute(query)
            with gzip.open(path, "wt", encoding="utf-8", compresslevel=1) as handle:
                for row in cursor:
                    handle.write(json.dumps(row, ensure_ascii=False, default=str) + "\n")
                    count += 1
        finally:
            cursor.close()
            connection.close()
        manifest[name] = {
            "rows": count,
            "bytes": path.stat().st_size,
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        }
        print(f"archived {name}: {count}", flush=True)
    (root / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8",
    )
    return verify_archive(root)


if __name__ == "__main__":
    print(json.dumps(archive(), indent=2))
