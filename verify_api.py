# -*- coding: utf-8 -*-
import json
import urllib.request
import urllib.parse

BASE = "http://127.0.0.1:8000"
sectors = ["光伏设备", "白酒", "半导体", "煤炭开采", "股份制银行"]

for s in sectors:
    query = [
        ("start_date", "2026-08-10"),
        ("end_date", "2026-08-14"),
        ("level", "2"),
        ("model_version", "v2_short_term"),
        ("sector_names", s),
    ]
    url = f"{BASE}/api/v1/sector-rotation/short-term/history?{urllib.parse.urlencode(query)}"
    try:
        req = urllib.request.urlopen(url, timeout=3)
        data = json.loads(req.read().decode("utf-8"))
        points = data.get("points", [])
        summary = []
        for p in points:
            d = p.get("as_of_date", "??")
            lbl = p.get("short_term_labels") or ""
            summary.append(f"{d[-5:]}={lbl or '-'}")
        print(f"{s}: {len(points)} pts ({', '.join(summary)})")
    except urllib.error.HTTPError as e:
        print(f"{s}: HTTP {e.code}")
    except Exception as e:
        print(f"{s}: ERROR {e}")