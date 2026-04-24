# Oak Valley Estates - Plan-Specific Framing Lumber Takeoff V2

This supersedes `framing_lumber_takeoff_prelim.md`.

Source basis:
- `C:\Users\racin\Desktop\Oak-Valley-Estates\Design\Single Page\Rodriquez Construction final.pdf`
- Wall material takeoff in full construction set, text lines 4446-4519.
- Floor/roof material takeoff in full construction set, text lines 1960-1974 and floor schedules around lines 2523, 2641-2642.
- Rammed earth schedule in `A905 - Rammed Earth.pdf`.
- Structural notes/table from `Main Structural.pdf`.

## Direct Material Callouts Found

| Scope | Plan callout / material | Net plan quantity | Source note |
|---|---:|---:|---|
| 2x4 wall framing | `2x4 Wood Stud`, model `10` | 371'-5 7/8" wall length / 3,715 SF wall area | Wall Material Takeoff |
| 2x6 wall framing | `2x6 Wood Stud`, model `10` | 600'-7 7/8" wall length / 6,277 SF wall area | Wall Material Takeoff |
| 2x6 wall framing | `2x6 Wood Stud`, model `12` | 39'-7 1/2" wall length / 385 SF wall area | Wall Material Takeoff |
| 2x4 column/parapet framing | `2x4 Column 14` | 112'-11 1/4" length / 305 SF area | Wall Material Takeoff |
| Exterior structural sheathing | `OX Si 10`, `OX SI 1"` | 504'-9" length / 5,315 SF area | Wall Material Takeoff |
| OX parapet sheathing | `OX SI Parapet` | 11'-3 3/4" length / 43 SF area | Wall Material Takeoff |
| Roof deck / roof assembly | `3/4" T&G Advantech` | 9,097 SF | Owner correction to roof deck basis |
| Roof plywood layer | `Plywood 5/8 CDX` | 9,097 SF | Roof Material Takeoff |
| Floor sheathing | `Advaantec 1.125` | 2,320 SF total | Floor schedules: main 1,060 SF + upper 1,260 SF |
| Rammed earth | `Clay works White Custom Rammed Earth White` | 249'-10 1/2" / 3,073 SF | Wall Material Takeoff |
| Scheduled 11 LSL rammed-earth walls | `11 LSL` | 126'-8 1/2" in A905 schedule | A905 schedule |

## Framing Lumber Order Calculation

Stud counts below are calculated from the plan wall lengths at 16" o.c. plus an allowance for ends, corners, intersections, openings, jacks, cripples, and waste. Structural table confirms 16" o.c. for the listed 8", 9", 10", 14", and 26" wall types, and 12" o.c. for 12" and 20" wall types. The Revit material schedule does not break every wall run by mark, so these are order quantities from the actual scheduled lengths.

| Material | Net wall length basis | Base calc | Recommended order qty | Notes |
|---|---:|---:|---:|---|
| 2x4x10 studs | 371'-5 7/8" | 279 studs @ 16" o.c. | 325 ea | Includes approx. 15% for corners/openings/blocking waste |
| 2x6x10 studs | 600'-7 7/8" | 451 studs @ 16" o.c. | 525 ea | Includes approx. 15% for corners/openings/blocking waste |
| 2x6x12 studs | 39'-7 1/2" | 30 studs @ 16" o.c. | 36 ea | Based on separate 12-ft 2x6 wall schedule row |
| 2x4x14 studs / column stock | 112'-11 1/4" | 85 studs @ 16" o.c. | 100 ea | From `2x4 Column 14` schedule row |
| 2x4x16 plate stock | 371'-5 7/8" wall length x 3 plates | 1,114 LF | 78 ea | 16-ft pieces, includes waste |
| 2x6x16 plate stock | 640'-3 3/8" 2x6 wall length x 3 plates | 1,921 LF | 132 ea | Includes 10-ft and 12-ft 2x6 wall runs |
| 2x4x16 backing/blocking | Plan-specific allowance | - | 90 ea | For cabinet, drywall, MEP, misc blocking |
| 2x6x16 backing/blocking | Plan-specific allowance | - | 70 ea | For exterior wall blocking/backing |
| 11 LSL rammed-earth wall package | 126'-8 1/2" length / 1,811 SF area | See schedule below | Include | Owner confirmed this belongs in scope |

## Sheathing / Sheet Goods

| Material | Net plan area | Net 4x8 sheets | Recommended order qty | Notes |
|---|---:|---:|---:|---|
| 1" OX SI exterior wall sheathing | 5,315 SF + 43 SF parapet = 5,358 SF | 168 sheets | 185 sheets | Uses the `OX SI 1"` / `OX Si 10` plan callout |
| 3/4" T&G Advantech roof deck | 9,097 SF | 285 sheets | 315 sheets | Owner-corrected roof deck basis |
| 5/8 CDX plywood roof layer | 9,097 SF | 285 sheets | 315 sheets | Roof Material Takeoff lists separate 5/8 CDX layer |
| Advantech 1.125 floor sheathing | 2,320 SF | 73 sheets | 82 sheets | Main + upper floor schedules |
## Headers / Opening Framing

Structural framing note: bearing wall door/window headers are double 2x10 unless specified otherwise. Openings 6 ft wide and under use one trimmer and one king each end unless noted otherwise. Openings over 6 ft wide use trimmers as indicated plus one king each end.

Plan-derived default header order, excluding steel/LVL-specific openings:

| Material | Recommended order qty | Basis |
|---|---:|---|
| 2x10x6 headers | 70 ea | Small scheduled door/window openings, doubled |
| 2x10x10 headers | 36 ea | 6 ft to 6'-3" openings, doubled; includes 2-piece verification allowance for Urban Iron 106 |

Important: many major openings are called out with LVL/HSS/W-steel on the structural framing plans. Those are not included as standard 2x10 lumber and should be ordered from the structural beam/steel schedule.

### Header Schedule Detail

| Level | Mark | Count | Rough width | Default header stock | Pieces | Status |
|---|---:|---:|---:|---|---:|---|
| Main | 100 | 9 | 3'-2" | double 2x10x6 | 18 | Include |
| Main | 101 | 3 | 3'-2" | double 2x10x6 | 6 | Include |
| Main | 101-E | 1 | 3'-2" | double 2x10x6 | 2 | Include |
| Main | 102 | 1 | 2'-8" | double 2x10x6 | 2 | Include |
| Main | 103 pocket | 5 | 6'-3" | double 2x10x10 | 10 | Include |
| Main | 104 | 1 | 3'-2" | double 2x10x6 | 2 | Include |
| Main | 105 double closet | 1 | 6'-3" | double 2x10x10 | 2 | Include |
| Main | 106 Urban Iron | 1 | 6'-3" | double 2x10x10 | 2 | Verify structural/steel |
| Main | 107 garage | 4 | varies / 9x20 model | structural/LVL/steel | - | Excluded from lumber header count |
| Main | 108 | 1 | 3'-2" | double 2x10x6 | 2 | Include |
| Main | 109 | 1 | 3'-2" | double 2x10x6 | 2 | Include |
| Main | 110 | 1 | 3'-2" | double 2x10x6 | 2 | Include |
| Main | 111 | 1 | 3'-2" | double 2x10x6 | 2 | Include |
| Main | W1 | 8 | 6'-0" | double 2x10x10 | 16 | Include |
| Main | W2 | 1 | 6'-0" | double 2x10x10 | 2 | Include |
| Basement | 302 | 3 | 2'-8" | double 2x10x6 | 6 | Include |
| Basement | 307 Vault | 1 | not listed | double 2x10x6 | 2 | Verify |
| Level 12 | 200 | 1 | 3'-2" | double 2x10x6 | 2 | Include |
| Level 12 | 202 | 3 | 2'-8" | double 2x10x6 | 6 | Include |
| Level 12 | 203 pocket | 3 | model 3x8 | double 2x10x6 | 6 | Verify rough width |
| Level 12 | 204 opening | 2 | 2'-6" | double 2x10x6 | 4 | Include |
| Level 12 | 303 | 1 | 3'-2" | double 2x10x6 | 2 | Include |
| Level 12 | 304 | 1 | 3'-2" | double 2x10x6 | 2 | Include |
| Level 10 | W3 | 1 | 6'-0" | double 2x10x10 | 2 | Include |
| Level 12 | W4 | 1 | 6'-0" | double 2x10x10 | 2 | Include |
| Level 12 | W13 | 1 | 3'-0 1/2" | double 2x10x6 | 2 | Include |

## 11-Inch / LSL / Rammed Earth Conditions

Yes, the project has 11-inch wall conditions:

| Mark | Material/model | Height | Level/base | Length | Area |
|---|---|---:|---|---:|---:|
| RE INT 113 | 11 LSL Rammed | 3'-11 7/8" | 12 | 7'-5 3/8" | 29 SF |
| RE EXT1112 | 11 LSL Rammed | 10'-1 1/8" | Main | 8'-6" | 78 SF |
| RE INT 1114 | 11 LSL Rammed | 14'-11 1/8" | 12 | 32'-4" | 457 SF |
| RE INT 11 Rake | 11 LSL Rammed | 16'-4 3/4" | Main | 36'-6" | 325 SF |
| RE EXT/INT 1126 | 11 LSL Rammed | 27'-3" | Main | 41'-11 1/8" | 922 SF |

Total scheduled 11 LSL rammed-earth length in A905: 126'-8 1/2". Total scheduled 11 LSL area: 1,811 SF.

## Exclusions / Must Verify

- Roof trusses: by truss package.
- Floor trusses/open web beams: by truss/vendor package.
- Structural steel W-shapes/HSS: by structural steel package.
- LVL/PSL beams: structural plan has multiple specific callouts; these need a separate beam schedule takeoff.
- Fasteners/connectors/holdowns: structural connector schedule required.
