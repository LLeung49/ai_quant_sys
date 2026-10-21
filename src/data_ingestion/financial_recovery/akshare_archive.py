"""Immutable local snapshots of AKShare finance and capital responses."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from datetime import date, datetime
from decimal import Decimal
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
from typing import Any
from uuid import uuid4

import pandas as pd


def _jsonable(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(key): _jsonable(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_jsonable(item) for item in value]
    if value is None or pd.isna(value):
        return None
    if isinstance(value, (datetime, date)):
        return value.isoformat()
    if isinstance(value, Decimal):
        return str(value)
    if isinstance(value, float) and not math.isfinite(value):
        return None
    if hasattr(value, "item"):
        return _jsonable(value.item())
    return value


def archive_snapshot(rows: Sequence[dict[str, Any]], *, stock_code: str,
                     as_of_date: date, kind: str, root: Path) -> Path:
    """Keep first observed payload for each content hash; never overwrite it."""
    if kind not in {"financial", "capital"}:
        raise ValueError("unsupported AKShare archive kind")
    body = {"provider": "akshare", "kind": kind, "stock_code": stock_code,
            "as_of_date": as_of_date.isoformat(),
            "rows": _jsonable(list(rows))}
    canonical = json.dumps(body, sort_keys=True, ensure_ascii=False,
                           allow_nan=False, separators=(",", ":"))
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    path = Path(root) / as_of_date.isoformat() / kind / f"{stock_code}-{digest}.json.gz"
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        return path
    document = {**body, "captured_at": datetime.now().astimezone().isoformat(),
                "content_sha256": digest}
    temporary = path.with_name(path.name + "." + uuid4().hex + ".tmp")
    try:
        with gzip.open(temporary, "wt", encoding="utf-8") as output:
            json.dump(document, output, ensure_ascii=False, allow_nan=False, sort_keys=True)
        try:
            os.link(temporary, path)
        except FileExistsError:
            pass
    finally:
        temporary.unlink(missing_ok=True)
    return path


def read_snapshot(path: Path) -> dict[str, Any]:
    """Verify an archived response and restore top-level date fields for replay."""
    path = Path(path)
    with gzip.open(path, "rt", encoding="utf-8") as source:
        document = json.load(source)
    body = {key: document[key] for key in
            ("provider", "kind", "stock_code", "as_of_date", "rows")}
    canonical = json.dumps(body, sort_keys=True, ensure_ascii=False,
                           allow_nan=False, separators=(",", ":"))
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    if digest != document.get("content_sha256") or digest not in path.name:
        raise ValueError(f"AKShare archive checksum mismatch: {path}")
    for row in document["rows"]:
        if row.get("stock_code") != document["stock_code"]:
            raise ValueError("AKShare archive stock mismatch")
        for key in ("report_date", "announcement_date", "original_announcement_date",
                    "metric_available_at", "source_updated_at"):
            if row.get(key):
                row[key] = date.fromisoformat(str(row[key])[:10])
    return document
