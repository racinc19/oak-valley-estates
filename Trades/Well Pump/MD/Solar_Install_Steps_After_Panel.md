# Solar installation steps — after the panel is mounted (Starlink / job site)

Use this after the solar panel (e.g. SOLPERK 50W) is already on the pole and the pole is in place.

---

## What you need (besides the panel)

- [ ] Charge controller (from SOLPERK kit or equivalent 12V waterproof unit)
- [ ] 12V battery, 50–100 Ah (deep-cycle or LiFePO4)
- [ ] Battery box or weatherproof enclosure (optional but recommended)
- [ ] Wire: panel → controller (use kit cables if long enough; otherwise 10–12 AWG)
- [ ] Wire: controller → battery (short, 10–12 AWG)
- [ ] Fuses: one in positive line panel → controller, one battery → load (e.g. 15–20 A)
- [ ] Starlink power: either (A) Starlink 12V cable, or (B) small 150–300 W inverter + Starlink AC adapter
- [ ] Basic tools: screwdriver, wire strippers, crimp connectors or terminal blocks, multimeter

---

## Step 1 — Mount the charge controller

1. Choose a spot **out of direct weather** (under an eave, in a small enclosure at the base of the pole, or in a trailer/shed).
2. Mount the controller on a flat surface (wood, plastic, metal) with screws or double-sided tape so it doesn’t move.
3. Keep it **close to the battery** so the wires from controller to battery are short (1–3 ft).
4. Ensure the controller is **dry and ventilated** (no standing water, not in a sealed box with no air).

---

## Step 2 — Place and connect the battery

1. Put the 12V battery in a **stable, level** spot (same enclosure or box as the controller if possible).
2. If using a battery box, put the battery inside and close the lid; leave vents clear.
3. **Do not connect the solar panel yet.** First connect only **battery → controller**:
   - Controller **Battery (+)** terminal → battery **positive (+)**.
   - Controller **Battery (–)** terminal → battery **negative (–)**.
4. Use correct polarity. Double-check with a multimeter (battery should read ~12–13 V).
5. If the controller has a display, it should turn on and show battery voltage. If it has a fuse on the battery side, ensure it’s installed.

---

## Step 3 — Wire the solar panel to the controller

1. Run the **panel positive (+)** and **panel negative (–)** wires from the pole down to the controller. Use the kit cables or 10–12 AWG, and keep connections dry (waterproof connectors or junction box if outside).
2. **Before connecting**, ensure the panel is **not in full sun** (early morning or shade), or cover the panel. This avoids a voltage spike when you plug in.
3. Connect:
   - Panel **positive (+)** → controller **Solar (+)** (or “PV+”).
   - Panel **negative (–)** → controller **Solar (–)** (or “PV–”).
4. Put a **fuse** (e.g. 15 A) in the **positive** line between panel and controller, close to the controller.
5. Once wired, expose the panel to sun. The controller should show charging (LED or display). Check manual for “charging” vs “full” indicators.

---

## Step 4 — Add a fuse between battery and load

1. For anything you power from the battery (inverter or Starlink 12V cable), put a **fuse** in the **positive** wire from the battery to the load.
2. Size the fuse for the load (e.g. Starlink ~5–8 A on 12V → use 10–15 A fuse). Inverter may need 20–30 A depending on size.
3. Keep the fuse **close to the battery** so the whole wire from battery to load is protected.

---

## Step 5A — Power Starlink with 12V cable (no inverter)

1. Get Starlink’s **12V power cable** (if available for your dish model).
2. Run the cable from the **battery** (through the fuse in the positive line) to the Starlink router/dish.
3. Connect **positive** to battery + (via fuse), **negative** to battery –.
4. Plug the 12V cable into the Starlink router as per Starlink instructions.
5. Turn on Starlink and confirm it boots. Check the Starlink app for connection.

---

## Step 5B — Power Starlink with an inverter (if no 12V cable)

1. Place the **inverter** near the battery, in a dry spot.
2. Connect inverter to battery:
   - Inverter **red (+)** → battery **positive (+)** (through the load fuse from Step 4).
   - Inverter **black (–)** → battery **negative (–)**.
3. Use short, thick wires (e.g. 10 AWG) for inverter connections to avoid voltage drop.
4. Plug Starlink’s **AC power supply** into the inverter’s AC outlet.
5. Turn the inverter **on**, then plug the Starlink cable into the power supply. Starlink should power up; verify in the app.

---

## Step 6 — Final checks

1. **Polarity:** All connections positive-to-positive, negative-to-negative. No shorts.
2. **Fuses:** One in panel → controller (positive), one in battery → load (positive).
3. **Controller:** Shows battery voltage and, in sun, charging state.
4. **Starlink:** Powers on and connects in the app.
5. **Weatherproofing:** All outdoor connections in waterproof boxes or heat-shrink; no exposed copper.
6. **Cable runs:** Panel and Starlink cables secured to the pole (straps or clips) so they don’t swing or abrade.

---

## Optional — Add a battery monitor

- A simple **voltage display** or **battery monitor** (e.g. shunt-based) on the battery helps you see when it’s low so you can reduce use or add more solar later.

---

## Summary order of connections

1. Mount controller; place battery.
2. Connect **battery → controller** (no panel yet).
3. Connect **panel → controller** (panel shaded when connecting); add panel fuse.
4. Add **battery → load** fuse; connect **battery → inverter or Starlink 12V**.
5. Power Starlink (12V cable or inverter); verify in app.
6. Expose panel to sun; confirm controller shows charging.

---

*For Rodriguez job site — Starlink on pole with SOLPERK 50W (or similar) panel. Cameras are separate (AOSU solar, no connection to this system).*
