# Oak Valley Estates - Electrical Fixture Takeoff

Source basis:
- `C:\Users\racin\Desktop\Oak-Valley-Estates\Design\Single Page\E100 - Main Electrical.pdf`
- `C:\Users\racin\Desktop\Oak-Valley-Estates\Design\Single Page\E101 - UpperLower Electrical.pdf`
- `C:\Users\racin\Desktop\Oak-Valley-Estates\Design\Single Page\E102 - Main Ceiling Electrical.pdf`
- `C:\Users\racin\Desktop\Oak-Valley-Estates\Design\Single Page\E103 - UpperLower Electrical.pdf`
- `C:\Users\racin\Desktop\Oak-Valley-Estates\Design\Single Page\E104 - Panels.pdf`
- `C:\Users\racin\Desktop\Oak-Valley-Estates\Design\Single Page\E105 - Panel Schedlue.pdf`
- Cross-check: `Rodriquez Construction final.pdf`

Status: plan-specific fixture/device schedule extraction. Lighting fixture rows marked "verify" are present in the schedule, but the PDF text layer merges some rows/levels.

## Electrical Equipment

| Manufacturer / Type | Model | Count | Source |
|---|---|---:|---|
| HVAC | Disconnect | 13 | E100 / Electrical Equipment Schedule |
| Leviton | 28" Media Center | 1 | E100 / Electrical Equipment Schedule |
| Leviton | Load Center with Smart Breakers | 2 | E100 / Electrical Equipment Schedule |
| Smoke Detector | - | 9 | E100 / Electrical Equipment Schedule |

## Main Level Devices

| Type | Model / note | Level | Count |
|---|---|---|---:|
| Axion | 8" Android PoE Touch Screen | Main | 10 |
| Communication | LeGrande 9 & 120 duplex | Main | 7 |
| Outlet | Floor | Main | 5 |
| Outlet | Range | Main | 3 |
| Outlet | Stack | Main | 1 |
| Outlet | Water Proof | Main | 9 |
| Outlet Duplex | Microwave | Main | 1 |
| Outlet Duplex | Wall | Main | 32 |
| Outlet GFCI | Countertop | Main | 14 |
| Outlet GFCI | Island | Main | 4 |
| RAC | LAN1 | Main | 14 |

Main level device subtotal, excluding panels/smoke/HVAC equipment: 100 devices.

## Basement / Upper / Level 12 Devices

| Type | Model / note | Level | Count |
|---|---|---|---:|
| Axion | 8" Android PoE Touch Screen | Basement | 3 |
| Communication | LeGrande 9 & 120 duplex | Basement | 1 |
| Outlet | Ceiling | Basement | 3 |
| Outlet Duplex | Wall | Basement | 10 |
| Outlet GFCI | Countertop | Basement | 3 |
| Axion | 8" Android PoE Touch Screen | Level 12 | 4 |
| Communication | LeGrande 9 & 120 duplex | Level 12 | 1 |
| Outlet | Dryer | Level 12 | 1 |
| Outlet | Hybrid Water Heater 240 | Level 12 | 1 |
| Outlet | Water Proof | Level 12 | 4 |
| Outlet Duplex | Wall | Level 12 | 11 |
| Outlet GFCI | Countertop | Level 12 | 1 |
| Outlet GFCI | Island | Level 12 | 2 |
| RAC | LAN1 | Level 12 | 5 |

Basement / upper / Level 12 device subtotal: 50 devices.

## Lighting Fixtures

### Main Ceiling

| Manufacturer | Model | Wattage | Level | Count |
|---|---|---:|---|---:|
| Focal Point | 3.5" Wash | 7W | Main | 14 |
| XAL | Motion Flush | 12W | Main | 13 |

Main lighting subtotal: 27 fixtures.

### Upper / Lower Ceiling

| Manufacturer | Model | Mark | Wattage | Level | Count | Status |
|---|---|---|---:|---|---:|---|
| Focal Point | 3.5" Wash | `<varies>` | 7W | mixed | 103 | Verify as total schedule count |
| XAL | Motion Flush | XAL M | 12W | mixed | 9 | Verify |
| Focal Point | 3.5" Wash | FP3.5 | 7W | Basement | 2 | Clean |
| XAL | Motion Flush | XAL M | 12W | Basement | 1 | Clean |
| FLy Achilles | Modern Minimalist LED Long Strip Indoor Pendant Lights | - | 16W | Level 10 | 2 | Clean |
| Lightology | A Tubes | LAT | 12W | Level 10 | 1 | Clean |
| Focal Point | 3.5" Wash | FP7W | 7W | Level 12 | 26 | Clean |
| XAL | Laundry | `<varies>` | 7W | Level 12 | 4 | Clean |
| Lightology | A Tubes | `<varies>` | 12W | Level 22 | 3 | Clean |

Clean upper/lower lighting subtotal, excluding the mixed/total rows: 39 fixtures.

If the `Focal Point 3.5" Wash <varies> = 103` row is a true grand total, use 103 for that fixture family and do not add the FP3.5/FP7W detail rows on top of it.

## Combined Clean Counts

| Category | Count |
|---|---:|
| Electrical equipment | 25 |
| Main level devices | 100 |
| Basement / upper / Level 12 devices | 50 |
| Main lighting fixtures | 27 |
| Clean upper/lower lighting fixtures, excluding mixed total rows | 39 |

Clean counted total excluding mixed/verify lighting rows: 241 items.

## LED Strip / Channel / Low-Voltage Panel Takeoff

Source: E104 Panels.

### Smart / Control Hardware

| Item | Count | Status | Notes |
|---|---:|---|---|
| Leviton Load Center with Smart Breakers | 2 | Clean | From E100 equipment schedule |
| Leviton 28" Media Center | 1 | Clean | From E100 equipment schedule |
| Homey Pro 2023 | 1 | Clean | Shown on E104 control diagram |
| POE Switch | 1 | Clean | Shown on E104 control diagram |
| Custom Rotary Switch | 1 | Clean | Shown on E104 control diagram |
| Fused 24V Distro | 8 | Clean | Two per panel shown on E104 |

### Shelly Modules

| Item | Count | Status | Notes |
|---|---:|---|---|
| Shelly Dual Cover | 8 | Clean | Visual count from E104: Panel 1 = 3, Panel 2 = 2, Panel 3 = 3 |
| Shelly PM4 | 1 | Clean | E104 control diagram |
| Shelly RGBW Plus | 1 | Clean | E104 control diagram |
| Shelly / PM module references | 10 | Cross-check | Text extraction count includes Dual Cover, PM4, RGBW labels |

### Shelly Pro / PM Modules

| Item | Count | Status | Notes |
|---|---:|---|---|
| PM-1 Pro | 11 | Verify | Text extraction count for `PM-1`; includes `PM-1 Pro` and `PM-1-Pro` labels |
| PM-2 Pro | 3 | Clean | E104 text/visual count |
| PM-3 Pro | 1 | Clean | E104 text/visual count |
| PM-4 Pro | 4 | Clean | E104 text/visual count |

### MeanWell 24V Drivers / Transformers

| Driver | Count | Status |
|---|---:|---|
| MeanWell HDR-150-24 | 4 | Clean |
| MeanWell HDR-240-24 | 11 | Clean |
| MeanWell HDR-320-24 | 10 | Clean |
| MeanWell HDR-360-24 | 1 | Clean |
| MeanWell HDR-480-24 | 10 | Clean |
| MeanWell 120/24V transformer callout | 1 | Diagram callout |

MeanWell driver total by model rows: 36. Text extraction sees 37 `MeanWell` labels because one is a generic transformer callout.

### LED Strip / Channel Zones

E104 shows 70 low-voltage strip/channel output zones. For ordering channel, use one matching channel/diffuser run per zone unless field layout combines runs.

| Panel | Top strip/channel zones | Bottom strip/channel zones | Total zones |
|---|---:|---:|---:|
| Panel 1 | 10 | 11 | 21 |
| Panel 2 | 8 | 9 | 17 |
| Panel 3 | 9 | 9 | 18 |
| Panel 4 | 7 | 7 | 14 |
| Total | 34 | 36 | 70 |

Zone families visible on E104:

- EXT zones
- LVC zones
- LVM zones
- LV zones
- LVS zones
- FL/F zones
- P3/P4 zones

The sheet gives amperage by zone and driver/panel assignment. It does not give a reliable linear-foot total in the text extraction. Exact LED strip footage and aluminum channel footage should be traced from E102/E103 ceiling plans by run if ordering by length.

## Verify Before Ordering

- Upper/lower lighting table: confirm whether `Focal Point 3.5" Wash <varies> = 103` is a fixture-family grand total or a separate row.
- LED strip schedules/panels are shown, but the schedule text extraction does not provide a clean linear-foot count.
- Panel/driver hardware from E104 should be reviewed separately if ordering low-voltage LED drivers/controllers.
- Appliance/specialty equipment rows are listed for circuiting but do not always show counts; do not treat them as purchased electrical fixtures without owner/vendor confirmation.
