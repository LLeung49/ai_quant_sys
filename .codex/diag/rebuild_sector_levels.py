"""Operator wrapper: rebuild sector aggregates after an audited fact-table repair."""

from morning_conference.sector_rotation.sector_index_builder import rebuild_all_sectors


for level in (1, 2):
    print(f"[sector-rebuild] level={level} start", flush=True)
    rows = rebuild_all_sectors(level=level, full=True)
    print(f"[sector-rebuild] level={level} complete rows={rows}", flush=True)
