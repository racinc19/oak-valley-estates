"""Generate RFP - Excavator Well Water System.pdf with Scope 3 (Solar Electrical Vault)."""
import os
from fpdf import FPDF

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..")
PDF_PATH = os.path.join(OUTPUT_DIR, "RFP - Excavator Well Water System.pdf")


def pdf():
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=12)
    pdf.set_margins(18, 14, 18)
    pdf.add_page()
    pdf.set_font("Helvetica", "", 9)

    lines = [
        "RAC DEVELOPMENT",
        "REQUEST FOR PROPOSAL",
        "EXCAVATOR / CIVIL - Well Water System - Site Work",
        "Rodriguez Residence - Oak Valley Estates | Kanarraville, UT 84742",
        "Owner / Developer RAC Development | Craig Engel | (435) 229-7360 | racinc19@gmail.com",
        "Date Issued March 9, 2026",
        "Response Due ___________________________",
        "",
        "System Overview",
        "Figure 1 - Solar Well Water System | Rodriguez Residence | Oak Valley Estates",
        "",
        "Project Overview",
        "RAC Development is soliciting bids for civil and excavation work associated with the solar-powered",
        "well water and storage system at the Rodriguez residence, Kanarraville, UT.",
        "",
        "NOTE: Trench (288 ft, 36\" deep) is already excavated and complete. Do not include trench work in bid.",
        "",
        "--------------------------------------------------------------------------------",
        "Scope 1 - Wellhead Vault (36\" Sump Bucket)",
        "",
        "The wellhead vault is a 36\" diameter sump bucket - NOT a precast concrete vault. Contractor shall",
        "procure and install the sump bucket per specifications below.",
        "",
        "Specification:",
        "Type           36\" diameter structural foam sump bucket",
        "Reference      Zoeller 31-0110 or approved equivalent",
        "Dimensions     24\" dia x 36\" depth minimum (or 36\" dia version per site requirement)",
        "Material       Structural foam / HDPE - suitable for burial",
        "Access         Watertight lid/hatch at grade - tamper-resistant hardware",
        "Inlets/Outlets Contractor to confirm knockout locations suit site plumbing layout",
        "",
        "Figure 2 - Reference: 36\" Sump Bucket / Zoeller Basin (Contractor may propose approved equivalent)",
        "",
        "Wellhead Vault Work Includes:",
        "- Excavate and prepare vault location",
        "- Procure 36\" sump bucket (Zoeller 31-0110 or approved equivalent)",
        "- Set sump bucket level on prepared gravel base",
        "- Install watertight access lid/hatch flush to finished grade with tamper-resistant hardware",
        "- Backfill and compact to finished grade",
        "",
        "--------------------------------------------------------------------------------",
        "Scope 2 - 1,000 Gallon Buried Storage Tank",
        "",
        "Specification:",
        "Type          1,000 gallon vertical water storage tank - buried",
        "Reference     Norwesco 1000 Gal Black Vertical or approved equivalent",
        "Material      Black HDPE / polyethylene - UV and soil resistant",
        "Access        Riser to grade with watertight access hatch",
        "Connections   Supply and return line tie-in by Contractor",
        "",
        "Figure 3 - Reference: Norwesco 1,000 Gal Black Vertical Tank (Contractor may propose approved equivalent)",
        "",
        "Storage Tank Work Includes:",
        "- Excavate for buried 1,000 gal tank near wellhead",
        "- Procure tank (Norwesco or approved equivalent)",
        "- Set tank level on prepared gravel base",
        "- Install access riser and watertight access hatch at finished grade",
        "- Tie in supply and return lines",
        "- Backfill and compact around tank",
        "",
        "--------------------------------------------------------------------------------",
        "Scope 3 - Solar Electrical Vault (Fiberglass FRP Storage Vault)",
        "",
        "The solar electrical vault is an underground fiberglass (FRP) enclosure that will house solar electrical",
        "equipment (Victron MPPT charge controller, 24V battery bank, Victron MultiPlus-II inverter). Electrical",
        "install is a separate trade; this scope is excavation and vault structure only.",
        "",
        "Specification:",
        "Type          Underground fiberglass (FRP) storage vault",
        "Reference     Hubbell Power Systems / Quazite model B1A366048B or approved equivalent",
        "Dimensions    36\" W x 60\" L x 48\" D interior (depth 48\")",
        "Material      FRP - Tier 8 / ANSI-type rated underground electrical enclosure, solid bottom",
        "Access        Frame and cover at grade; hatch for personnel access, weatherproof, foot-traffic capable",
        "Conduit       Provide or coordinate stub-ups/entry points for DC cable (from array) and AC cable (to VFD)",
        "Drainage      Contractor shall state how drainage is handled (e.g. sump, weep)",
        "Ventilation   Required. Passive ventilation (e.g. high and low vents, louvered frame, or vented cover)",
        "              so heat from batteries and inverter can escape; vault must not be fully sealed.",
        "",
        "Reference: Well Pump\\HTML\\4_Well_Solar_Visual.html - vault layout and equipment.",
        "",
        "Solar Electrical Vault Work Includes:",
        "- Excavate for vault at designated location (per site plan / coordination with GC)",
        "- Furnish and install FRP vault (B1A366048B or equivalent 36\" x 60\" x 48\")",
        "- Set vault level; install frame and cover at grade",
        "- Provide drainage and passive ventilation per above",
        "- Backfill and compact to finished grade; leave site clean",
        "- Coordinate conduit entry points with electrical scope (trench by others)",
        "",
        "Excluded from Scope 3: Trench for conduit (panel to vault, vault to VFD) is in initial project scope",
        "unless Contractor includes and prices separately. No electrical equipment or wiring - electrical is separate RFP.",
        "",
        "--------------------------------------------------------------------------------",
        "Scope Exclusions",
        "",
        "- Trench work - complete, do not include (unless Scope 3 trench explicitly added and priced separately)",
        "- No electrical work of any kind",
        "- No plumbing connections at the house",
        "- Supply line stub-out at house foundation only - plumber connects",
        "",
        "--------------------------------------------------------------------------------",
        "Bid Requirements",
        "",
        "- Lump sum price broken out by: (1) Wellhead Vault, (2) Storage Tank, (3) Solar Electrical Vault",
        "- Estimated duration and crew size",
        "- List of similar completed projects",
        "- Proof of insurance and license",
        "- Payment terms",
        "",
        "For Scope 3, also provide: vault make/model or equivalent, drainage and ventilation approach.",
        "",
        "--------------------------------------------------------------------------------",
        "Proposal Submission",
        "",
        "Submit all questions and bids in writing to Craig Engel by the Response Due date above.",
        "",
        "Company Name    _________________________________________",
        "Signature       _________________________________________",
        "Date            _________________________________________",
        "License #       _________________________________________",
        "",
        "Lump Sum - Wellhead Vault ($)        _________________________",
        "Lump Sum - Storage Tank ($)          _________________________",
        "Lump Sum - Solar Electrical Vault ($) _________________________",
        "Total Bid Amount ($)                 _________________________",
    ]

    w = pdf.w - pdf.l_margin - pdf.r_margin
    for line in lines:
        s = line.encode("latin-1", "replace").decode("latin-1") if line else " "
        pdf.multi_cell(w, 5, s)

    pdf.output(PDF_PATH)
    return PDF_PATH


if __name__ == "__main__":
    path = pdf()
    print("Created:", path)
