#!/usr/bin/env python3
"""Apply user selections to selection_data_to_paste_in_supabase.json"""
import json
import re

with open("selection_data_to_paste_in_supabase.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def find_room(rid):
    for r in data:
        if r["id"] == rid:
            return r
    return None

def find_item(room, name_pattern):
    for i in room["items"]:
        if name_pattern.lower() in (i.get("name") or "").lower():
            return i
    return None

def update_item(room, name_pattern, **kwargs):
    it = find_item(room, name_pattern)
    if it:
        for k, v in kwargs.items():
            it[k] = v
        return True
    return False

def add_item(room, item):
    if "id" not in item:
        rid = room["id"]
        n = len(room["items"]) + 100
        item["id"] = f"{rid}_i{n}"
    item.setdefault("vendor", "TBD")
    item.setdefault("link", "")
    item.setdefault("notes", "")
    item.setdefault("status", "not_started")
    item.setdefault("model", "")
    item.setdefault("color", "")
    item.setdefault("leadTime", "")
    item.setdefault("photo", "")
    room["items"].append(item)

# KITCHEN
k = find_room("kitchen")
update_item(k, "Glacier Bay", name="Kraus Loften 33\" Drop-In Sink", vendor="Kraus",
    link="https://www.homedepot.com/p/KRAUS-Loften-33-in-Drop-In-Undermount-Single-Bowl-18-Gauge-Stainless-Steel-Kitchen-Workstation-Sink-with-Accessories-KWT320-33-18/315436104",
    notes="KWT320-33-18. Single bowl 18-gauge SS. Qty 2 - main sink + island.")
update_item(k, "Kohler Crue", name="Delta Stryke Touch Touchless Faucet (x2)", vendor="Delta",
    link="https://www.homedepot.com/p/Delta-Stryke-Touch-Touchless-Arctic-Stainless-17-25-in-H-Pull-Down-Sprayer-Kitchen-Faucet-with-360-Spout-Swivel-9176TL-AR-PR-DST/334993343",
    notes="9176TL-AR-PR-DST. Touch/touchless, 360 spout. Arctic Stainless. Qty 2 - main sink + island.")

# OFFICE BATH
ob = find_room("office_bath")
update_item(ob, "HOROW Undermount Sink", name="HOROW Flush Mount Black Sink", vendor="HOROW",
    link="https://horow.com/products/flush-mount-black-sink-with-overflow-and-seamless-model-hwtp-s6039d-b",
    model="HWTP-S6039D-B")
update_item(ob, "Arc Waterfall", name="Lefton Single-Hole Rotatable Faucet", vendor="Lefton",
    link="https://www.leftonhome.com/products/lefton-single-hole-rotatable-faucet-bf2204-with-pop-up-drain-stopper?variant=47000282661123",
    model="BF2204")
update_item(ob, "HOROW Smart Toilet", name="HOROW Smart Toilet T38P", vendor="HOROW",
    link="https://horow.com/products/smart-toilet-with-flush-tank-and-ada-compliance-for-12-inch-rough-in-model-t38p",
    model="T38P", notes="12\" rough-in, ADA compliant")
add_item(ob, {"name": "Grandjoy Triple Handle Shower", "vendor": "Grandjoy", "id": "office_bath_i65",
    "link": "https://www.grandjoyhome.com/products/multiple-press-12-in-triple-handle-7-spray-shower-faucet-2-5-gpm-with-anti-scald-in-valve-included",
    "notes": "7-spray, 2.5 GPM, anti-scald"})
add_item(ob, {"name": "Oatey Designline 24\" Linear Drain", "vendor": "Oatey", "id": "office_bath_i66",
    "link": "https://www.homedepot.com/p/Oatey-Designline-24-in-Stainless-Steel-Linear-Shower-Drain-with-Square-Pattern-Drain-Cover-in-Matte-Black-DL32240/309613602",
    "model": "DL32240", "notes": "Matte black, square pattern"})

# POWDER BATH
pb = find_room("powder")
update_item(pb, "HOROW Undermount Sink", name="HOROW Flush Mount Black Sink", vendor="HOROW",
    link="https://horow.com/products/flush-mount-black-sink-with-overflow-and-seamless-model-hwtp-s6039d-b",
    model="HWTP-S6039D-B")
update_item(pb, "Arc Waterfall", name="Lefton Single-Hole Rotatable Faucet", vendor="Lefton",
    link="https://www.leftonhome.com/products/lefton-single-hole-rotatable-faucet-bf2204-with-pop-up-drain-stopper?variant=47000282661123",
    model="BF2204")
update_item(pb, "HOROW Smart Toilet", name="HOROW Smart Toilet T38P", vendor="HOROW",
    link="https://horow.com/products/smart-toilet-with-flush-tank-and-ada-compliance-for-12-inch-rough-in-model-t38p",
    model="T38P")

# GARAGE
g = find_room("garage")
update_item(g, "Mop Sink", name="Karl Home 24x24 Mop Sink", vendor="Karl Home",
    link="https://www.homedepot.com/p/Karl-home-24-in-x-24-in-Stainless-Steel-Floor-Mount-Freestanding-Mop-Sink-Laundry-Utility-Sink-in-Silver-K1G47000888/334840213",
    model="K1G47000888", notes="24x24, floor mount, silver")
update_item(g, "Moen Align", name="EVERSTEIN Wall Mount Faucet", vendor="EVERSTEIN",
    link="https://www.homedepot.com/p/EVERSTEIN-Single-Handle-Wall-Mount-8-in-Kitchen-Faucet-Brushed-Nickeled-Faucet-for-Kitchen-with-Spray-Gun-SFS-1087-NK/332726688",
    model="SFS-1087-NK", notes="8\" wall mount, spray gun, brushed nickel")

# OUTDOOR / BBQ
obbq = find_room("outdoor_bbq")
update_item(obbq, "Hose Bibbs", name="Hose Bibbs w/ Vacuum Breaker (10 total)", vendor="Aquor",
    link="https://www.aquorwatersystems.com/collections/hydrants/products/premium-house-hydrant-v2-brushed-stainless-steel",
    notes="2x Hot/Cold Hydrant (main areas, BBQ, dog area): https://www.aquorwatersystems.com/collections/hydrants/products/hot-cold-hydrant. 8x Premium V2 (elsewhere): see link.")

# PRIMARY BATH
prb = find_room("primary_bath")
update_item(prb, "HOROW Undermount Sink", name="HOROW Flush Mount Black Sink (x2)", vendor="HOROW",
    link="https://horow.com/products/flush-mount-black-sink-with-overflow-and-seamless-model-hwtp-s6039d-b",
    model="HWTP-S6039D-B")
update_item(prb, "Arc Waterfall", name="Lefton Single-Hole Rotatable Faucet", vendor="Lefton",
    link="https://www.leftonhome.com/products/lefton-single-hole-rotatable-faucet-bf2204-with-pop-up-drain-stopper?variant=47000282661123",
    model="BF2204")
update_item(prb, "HOROW Smart Toilet T05", name="HOROW Smart Toilet T38P (x2)", vendor="HOROW",
    link="https://horow.com/products/smart-toilet-with-flush-tank-and-ada-compliance-for-12-inch-rough-in-model-t38p",
    model="T38P")
update_item(prb, "GRANDJOY Thermostatic", name="Grandjoy Multi-Function Shower (x2)", vendor="Grandjoy",
    link="https://www.grandjoyhome.com/products/multi-function-shower-system-with-360-swivel-head-and-body-jets",
    notes="360 swivel head + body jets. 2 showers in primary.")
update_item(prb, "Freestanding Tub", name="Woodbridge 71\" Whirlpool Tub", vendor="Woodbridge",
    link="https://www.homedepot.com/p/WOODBRIDGE-71-in-x-31-in-Acrylic-Whirlpool-and-Air-with-Inline-Heater-Combination-Bathtub-with-Reversible-Drain-in-White-HBT7240/326559523",
    model="HBT7240", notes="71x31, whirlpool + air, inline heater, white")
update_item(prb, "Tub Filler", name="Woodbridge Florence Tub Filler", vendor="Woodbridge",
    link="https://www.homedepot.com/p/WOODBRIDGE-Florence-Single-Handle-Freestanding-Tub-Faucet-with-Hand-Shower-in-Matte-Black-F1015/316251304",
    model="F1015", notes="CENTER OF TUB (not on end). Freestanding, matte black, hand shower")
update_item(prb, "Oatey 24", name="Oatey Designline 24\" Linear Drain (x2)", vendor="Oatey",
    link="https://www.homedepot.com/p/Oatey-Designline-24-in-Stainless-Steel-Linear-Shower-Drain-with-Square-Pattern-Drain-Cover-in-Matte-Black-DL32240/309613602",
    model="DL32240")

# UPPER LAUNDRY
ul = find_room("upper_laundry")
update_item(ul, "Laundry Sink", name="Sarlai 24x18 Laundry Sink", vendor="Sarlai",
    link="https://www.homedepot.com/p/Sarlai-24-in-W-x-18-in-D-Undermount-Gunmetal-Black-Laundry-Utility-Sink-Stainless-Steel-Laundry-Sink-with-Bottom-Grid-XYC2418A1/338117813",
    model="XYC2418A1", notes="24x18 undermount, gunmetal black")
add_item(ul, {"name": "Delta Stryke Laundry Faucet", "vendor": "Delta", "id": "upper_laundry_i124",
    "link": "https://www.homedepot.com/p/Delta-Stryke-Single-Handle-Pull-Down-Sprayer-Kitchen-Faucet-in-Matte-Black-9176-BL-DST/318509182",
    "model": "9176-BL-DST", "notes": "Matte black, pull-down sprayer"})

# BASEMENT BATH
bb = find_room("basement_bath")
update_item(bb, "HOROW Undermount Sink", name="HOROW Flush Mount Black Sink", vendor="HOROW",
    link="https://horow.com/products/flush-mount-black-sink-with-overflow-and-seamless-model-hwtp-s6039d-b",
    model="HWTP-S6039D-B")
add_item(bb, {"name": "Lefton Single-Hole Rotatable Faucet", "vendor": "Lefton", "id": "basement_bath_i146",
    "link": "https://www.leftonhome.com/products/lefton-single-hole-rotatable-faucet-bf2204-with-pop-up-drain-stopper?variant=47000282661123",
    "model": "BF2204"})
update_item(bb, "HOROW Smart Toilet", name="HOROW Smart Toilet T38P", vendor="HOROW",
    link="https://horow.com/products/smart-toilet-with-flush-tank-and-ada-compliance-for-12-inch-rough-in-model-t38p",
    model="T38P")

# ADU KITCHEN
ak = find_room("adu_kitchen")
update_item(ak, "Guest Kitchenette Sink", name="Kraus Loften 33\" Drop-In Sink", vendor="Kraus",
    link="https://www.homedepot.com/p/KRAUS-Loften-33-in-Drop-In-Undermount-Single-Bowl-18-Gauge-Stainless-Steel-Kitchen-Workstation-Sink-with-Accessories-KWT320-33-18/315436104",
    notes="KWT320-33-18. Incl. disposal + air switch + icemaker line")
add_item(ak, {"name": "Delta Stryke Touch Touchless Faucet", "vendor": "Delta", "id": "adu_kitchen_i177",
    "link": "https://www.homedepot.com/p/Delta-Stryke-Touch-Touchless-Arctic-Stainless-17-25-in-H-Pull-Down-Sprayer-Kitchen-Faucet-with-360-Spout-Swivel-9176TL-AR-PR-DST/334993343",
    "model": "9176TL-AR-PR-DST"})

# ADU BATH 1
ab1 = find_room("adu_bath1")
update_item(ab1, "HOROW Undermount Sink", name="HOROW Flush Mount Black Sink", vendor="HOROW",
    link="https://horow.com/products/flush-mount-black-sink-with-overflow-and-seamless-model-hwtp-s6039d-b",
    model="HWTP-S6039D-B")
update_item(ab1, "Arc Waterfall", name="Lefton Single-Hole Rotatable Faucet", vendor="Lefton",
    link="https://www.leftonhome.com/products/lefton-single-hole-rotatable-faucet-bf2204-with-pop-up-drain-stopper?variant=47000282661123",
    model="BF2204")
update_item(ab1, "HOROW Smart Toilet", name="HOROW Smart Toilet T38P", vendor="HOROW",
    link="https://horow.com/products/smart-toilet-with-flush-tank-and-ada-compliance-for-12-inch-rough-in-model-t38p",
    model="T38P")
add_item(ab1, {"name": "Grandjoy Multi-Function Shower", "vendor": "Grandjoy", "id": "adu_bath1_i187",
    "link": "https://www.grandjoyhome.com/products/multi-function-shower-system-with-360-swivel-head-and-body-jets",
    "notes": "360 swivel head + body jets"})
add_item(ab1, {"name": "Oatey Designline 24\" Linear Drain", "vendor": "Oatey", "id": "adu_bath1_i188",
    "link": "https://www.homedepot.com/p/Oatey-Designline-24-in-Stainless-Steel-Linear-Shower-Drain-with-Square-Pattern-Drain-Cover-in-Matte-Black-DL32240/309613602",
    "model": "DL32240"})

with open("selection_data_to_paste_in_supabase.json", "w", encoding="utf-8") as f:
    json.dump(data, f, separators=(",", ":"))

print("Updated selection_data_to_paste_in_supabase.json")
