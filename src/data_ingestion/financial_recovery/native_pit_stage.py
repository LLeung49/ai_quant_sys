"""Checksummed, streaming offline staging of QMT native PIT versions."""

from __future__ import annotations

import gzip
import hashlib
import heapq
from itertools import groupby
import json
from pathlib import Path
from typing import Any, Iterator

from .native_pit_composer import compose_native_pit_versions


_KINDS = {"7001", "7002", "7003", "7008"}


def _archive_path(manifest: Path, raw: str) -> Path:
    path = Path(raw)
    if path.is_absolute():
        return path
    # Existing archive manifests store repository-relative paths.
    for parent in (Path.cwd(), manifest.parent, manifest.parent.parent.parent):
        candidate = parent / path
        if candidate.exists():
            return candidate
    raise FileNotFoundError(raw)


def _validated_rows(path: Path, expected_count: int) -> Iterator[dict[str, Any]]:
    count = 0
    prior_code = ""
    with gzip.open(path, "rt", encoding="utf-8") as source:
        for line in source:
            row = json.loads(line)
            code = row["stock_code"]
            if code < prior_code:
                raise ValueError(f"archive stock order changed: {path}")
            prior_code = code
            count += 1
            yield row
    if count != expected_count:
        raise ValueError(f"archive record count mismatch: {path}: {count}/{expected_count}")


def stage_native_pit(manifest: Path, output_dir: Path) -> dict[str, Any]:
    """Write candidates and conflicts to files only; never touch the database."""
    manifest = Path(manifest)
    groups = [row for row in json.loads(manifest.read_text(encoding="utf-8"))["groups"]
              if str(row["kind"]) in _KINDS]
    if not groups:
        raise ValueError("no supported statement archives")
    keyed: dict[tuple[str, str], dict[str, Any]] = {}
    for group in groups:
        key = (group["market"], str(group["kind"]))
        if key in keyed:
            raise ValueError(f"duplicate archive group: {key}")
        keyed[key] = group
        path = _archive_path(manifest, group["archive"])
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != group["archive_sha256"]:
            raise ValueError(f"archive checksum mismatch: {path}")
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    count = {"input_records": 0, "candidate_rows": 0, "conflict_rows": 0,
             "stock_count": 0, "period_count": 0}
    with gzip.open(output_dir / "candidates.jsonl.gz", "wt", encoding="utf-8") as candidates, \
         gzip.open(output_dir / "conflicts.jsonl.gz", "wt", encoding="utf-8") as conflicts:
        for market in sorted({market for market, _ in keyed}):
            streams = [_validated_rows(_archive_path(manifest, group["archive"]), group["records"])
                       for (group_market, _), group in sorted(keyed.items())
                       if group_market == market]
            merged = heapq.merge(*streams, key=lambda row: row["stock_code"])
            for _, stock_group in groupby(merged, key=lambda row: row["stock_code"]):
                stock_rows = list(stock_group)
                count["input_records"] += len(stock_rows)
                count["stock_count"] += 1
                count["period_count"] += len({row["report_date"] for row in stock_rows})
                result = compose_native_pit_versions(stock_rows)
                for row in result["candidates"]:
                    candidates.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
                    count["candidate_rows"] += 1
                for row in result["conflicts"]:
                    conflicts.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
                    count["conflict_rows"] += 1
    summary = {**count, "status": "staged_only", "manifest": str(manifest)}
    (output_dir / "stage-summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    return summary


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("output_dir", type=Path)
    args = parser.parse_args()
    print(json.dumps(stage_native_pit(args.manifest, args.output_dir), indent=2))
