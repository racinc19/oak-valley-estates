#!/usr/bin/env python3
"""Push selection_data_to_paste_in_supabase.json to Supabase."""
import json
import urllib.request

url = "https://mcvkkohtvywwvtndpuvw.supabase.co/rest/v1/selections?id=eq.main"
key = "sb_publishable_WN9vSmDmDJTTXE5uMP0lzQ_yl_ak5tL"

with open("selection_data_to_paste_in_supabase.json", "r", encoding="utf-8") as f:
    data = json.load(f)

body = json.dumps({
    "data": data,
    "updated_at": "2026-03-20T00:00:00.000Z"
}, separators=(",", ":"))

req = urllib.request.Request(url, data=body.encode("utf-8"), method="PATCH")
req.add_header("apikey", key)
req.add_header("Authorization", "Bearer " + key)
req.add_header("Content-Type", "application/json")
req.add_header("Prefer", "return=representation")

try:
    with urllib.request.urlopen(req, timeout=30) as r:
        resp = json.loads(r.read().decode())
        print("Response:", json.dumps(resp)[:500])
        if resp:
            d = resp[0].get("data") if isinstance(resp[0], dict) else None
            has_lefton = "Lefton" in json.dumps(d) if d else False
            print("Push OK. Contains Lefton:", has_lefton)
        else:
            print("Push returned empty (0 rows updated)")
except urllib.error.HTTPError as e:
    print("HTTP", e.code, e.reason)
    print(e.read().decode())
except Exception as e:
    print("Error:", e)
