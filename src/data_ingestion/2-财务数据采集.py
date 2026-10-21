# -*- coding: utf-8 -*-
"""Operator entry point for AKShare financial statement collection."""

from __future__ import annotations

from pathlib import Path
import sys

if __package__:
    from .akshare_financial_collection import main
else:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from data_ingestion.akshare_financial_collection import main


if __name__ == "__main__":
    raise SystemExit(main())
