"""Read-only import and input inspection for the sector builder."""

import morning_conference.sector_rotation.sector_index_builder as builder


print("[builder_file]", builder.__file__)
print("[members_function_module]", builder.get_sector_member_codes.__module__)
members = builder.get_sector_member_codes("交通运输", level=1)
dates = builder.get_all_trade_dates()
print("[members]", len(members))
print("[dates]", len(dates), dates[0], dates[-1])
panel = builder.fetch_member_kline_panel(members, dates[:2])
print("[panel_rows]", len(panel))
