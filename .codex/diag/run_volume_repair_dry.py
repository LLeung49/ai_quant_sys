"""Explicit no-mutation runner for the volume-repair dry-run."""

from data_ingestion.repair_market_volume_units import main


raise SystemExit(main([]))
