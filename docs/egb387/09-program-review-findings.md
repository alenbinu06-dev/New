# 9. Review findings — preliminary construction program (Gantt), rev. A3_2

Defect register for `source/Enoggera_Construction_Program_A3_v2.pdf`, checked against the briefing
data captured in files 01–05 of this knowledge base.

Re-run the checks with `python3 scripts/audit_program.py`.

These are review notes on the group's own drawing. They are a defect list, not report content.

## A. Errors that break the program as a CPM network

| # | Finding | Evidence |
|---|---|---|
| A1 | **The printed dates cannot be reproduced from the printed logic.** Feeding the chart's own durations and predecessor column through a CPM gives month 23 if a successor may start in the same month its predecessor finishes, and month 39 if it must start the month after. The chart says 25. Neither convention reproduces it, so the bars were placed by hand rather than calculated. | `audit_program.py` check 5 |
| A2 | **Nine activities start before a stated predecessor has finished.** A5 (1 month), B4 (1), D7 (1), D8 (4), E12 (2), F4 (1), F5 (3), F6 (3), H6 (1). These are impossible under any finish-to-start reading. E12 is the worst because it sits on the declared critical path. | check 2 |
| A3 | **The finish-to-start convention is applied inconsistently** — 32 successors start in the same month the predecessor finishes, 21 start the month after. Float and the critical path cannot be derived from a network that uses two conventions at once. | check 2 |
| A4 | **The stated critical path contains three links that do not exist in the logic column.** `B2 → A8` (A8's only predecessor is A6), `E9 → E11` (E11's predecessors are E7 and C6), `H5 → H6` (H6's predecessor is H4). | check 4 |
| A5 | **The Float column cannot be reproduced on 51 of 63 rows.** | check 6 |
| A6 | **Seven activities have no successor**, so they drive nothing and their float is meaningless: A2 site establishment, A3 survey/set-out/geotech, A9 cultural heritage monitoring, B5 temporary marine access, D10 valves and gates, E10 maintenance crane, F10 backfill and reinstatement. | check 3 |

## B. Missing logic links (physically required, not shown)

| # | Missing link | Why it is required |
|---|---|---|
| B1 | **D10 (valve actuating mechanism & gates) → H1 (first fill)** | The reservoir cannot be impounded before the outlet valves and gates are operable. D10 currently drives nothing. |
| B2 | **H1 (first fill) → H4 (wet commissioning, generation mode)** | There is no water in the upper storage to generate from until first fill is done. H1 and H3 (pump-mode commissioning) also overlap conceptually, because the scheme fills by pumping. |
| B3 | **E10 (maintenance crane) → E11 (mechanical installation)** | The station's maintenance crane is the lifting facility for landing the turbine, pump and generator. Both currently start in month 17 in parallel with no link. |
| B4 | **A3 (survey, set-out & geotechnical confirmation) → D1 (foundation excavation)** | Excavating to sound rock without the geotechnical confirmation closed out. |
| B5 | **B5 (temporary marine access — barges & workboats) → C2 and E2** | Bridge pier piling and the sheet pile cofferdam are both in-water work needing the barges and workboats. |
| B6 | **F10 (backfill & reinstatement) → H7 (practical completion)** | Handover cannot precede reinstatement of the pipeline route. |

## C. Sequencing and buildability

| # | Finding |
|---|---|
| C1 | **RCC placement (D7) runs months 9–16 = Dec 2027 – Jul 2028, starting at the peak of the wet season.** The chart's own footnote says the shaded Nov–Mar columns mean reduced productivity on earthworks and RCC placement, so the program contradicts its own note. Foundation excavation (D1, months 4–6 = Jul–Sep 2027) is correctly placed in the dry; the RCC should follow the same logic. |
| C2 | **E3 dewatering & excavation to RL 67.0 runs months 8–9 = Nov–Dec 2027**, i.e. an 8 m deep excavation below reservoir level, on two 200 dia pumps, in the wet season. |
| C3 | **The access bridge does not open until month 13, but station concrete starts at month 12** (E5 base slab). The drawings show the vehicle bridge as the only vehicular access to the station. Either concrete is barged and pumped — which is not shown — or the bridge is needed earlier. |
| C4 | **C3 pier caps start month 10 although C2 pier piling finishes month 7**, an unexplained 2-month gap. Closing it would open the bridge around month 10–11 and resolve C3 above. |
| C5 | **No final trim or re-dredge of the intake channel after cofferdam removal.** E1 dredges to RL 68.5 in months 3–5; the cofferdam is not removed until months 21–22, some 16 months later, in the same water. |
| C6 | **No care of water or stream diversion at the dam site.** The dam impounds a new ponded area in a gully, so it has a catchment. D1–D7 span two wet seasons with no diversion, cofferdam or care-of-water activity. |
| C7 | **D8 (penstock through-dam section at RL 92) is shown as a successor of D7 (RCC placement RL 88 → RL 102) but starts 4 months before D7 ends.** The intent is right — RL 92 is reached partway up — but it should be a start-to-start relationship with a lag, or D7 should be split at RL 92. |

## D. Resources and the plant registers

| # | Finding |
|---|---|
| D1 | **One hired 5 m³ batch plant and two 5 m³ agitator trucks serve up to five concurrent pours on three separated fronts.** Month 13 has D7 RCC at the dam, D8 penstock block, C5 bridge deck concrete, E5 station base slab and E6 station walls all live. No resource levelling is shown. |
| D2 | **The 150 t tracked crane is mobilised by month 4 but not needed until E11 in month 17** — about 13 months of idle hire. The briefing explicitly asks for an assessment of the time major plant is on site, so this is directly marked. |
| D3 | **Only 100 m of the 400 dia × 10 mm salvaged steel tube exists**, yet it is called on twice: C2 bridge pier piling and E4 station foundation piles. There is no procurement activity for additional tube. |
| D4 | **No activity for hauling the salvaged materials from Central Queensland.** A4 covers only the batch plant, 150 t crane and lifting gear. The 1900 m / 145 t of sheet piling and the sheetpile corners are at **Emerald**, and the 330 m / 42 t of 610 × 230 UB is at **Gladstone**. E2 needs the piling by month 5 and C4 needs the beams by month 11. |
| D5 | **The 610 × 230 UB is noted "Available July" with no year stated in the briefing.** C4 deck erection is months 11–12 = Feb–Mar 2028. If July means July 2028 the bridge cannot be built when shown. This needs confirming rather than assuming. |
| D6 | **No activity for engaging and mobilising the three Client-nominated subcontractors.** Dredging (E1) is a nominated subcontractor sitting on the declared critical path from month 3, with no lead-in shown, and the briefing makes coordination of the three nominated companies the Principal Contractor's responsibility. |

## E. Scope gaps against the briefing

| # | Finding |
|---|---|
| E1 | **No activity confirming the electrical and mechanical contractors' site-assembly and delivery loads before bridge design.** The briefing states the bridge is bid as Design and Construct precisely because the loading depends on the degree of site assembly envisaged by those contractors. C1 bridge design runs months 1–4 with A1 as its only predecessor. |
| E2 | **No temporary works design activity** other than the bridge. The briefing requires conceptual design of the temporary works — cofferdam, falsework, barge bridging — and this is one of the four individual reflective report topics. |
| E3 | **The "refilling pipeline" is not named.** Site plan item 7 is "Penstock and refilling pipeline" and item 4 is the separate emergency discharge pipe, but section F covers only the penstock and the emergency discharge. If the penstock is reversible and serves both duties, say so. |
| E4 | **Cultural heritage durations look optimistic and start too late.** A6 due diligence and Traditional Owner engagement is 1 month, and clearance of the dam, pipeline and dredge areas is 2 months. A cultural heritage management plan under the Queensland *Aboriginal Cultural Heritage Act 2003* takes longer, and engagement should begin during the tender period rather than at month 1 after award. Putting cultural heritage on the critical path is otherwise a genuine strength of this program. |

## F. Presentation

| # | Finding |
|---|---|
| F1 | **The "Month no." row is printed one column to the left of the bars.** Verified from the PDF vector geometry: the Apr-2027 column is centred at x ≈ 701.4 and the A1 bar is drawn there correctly, but the digit "2" is centred at x ≈ 701.7 over it, while "1" and the "27" year marker fall at x ≈ 676–683, inside the Float column and off the timeline. Consequently every month number reads one column late, May 2029 has no number, and the year markers land on Dec 2027 and Dec 2028 instead of Jan 2028 and Jan 2029. |
| F2 | **D7 states ~30,000–34,000 m³ of RCC, which the geometry does not support.** With a 250 m crest, 4 m crest width, 13 m base width and RL 102 to RL 86, the volume is about 14,000 m³ for a V-shaped valley and about 20,000 m³ for a parabolic one; taking the bar's own RL 88 to RL 102 body gives about 12,000–18,000 m³. The "~47 lifts" figure is right (14 m at 300 mm), but it cannot coexist with 30,000 m³. |

## G. What is correct — keep it

- Every row satisfies `Fin = Start + Dur − 1`; the bar arithmetic is clean on all 63 rows.
- Month 1 = Apr 2027, practical completion month 25 = Apr 2029, contract completion month 26 =
  31 May 2029 with 1 month terminal float. This matches the briefing exactly.
- The wet season is correctly shaded Nov–Mar in both years (months 8–12 and 20–24).
- The subcontracting split matches the briefing exactly: only the grout curtain (D4) and the
  building trades fit-out (E9) are subcontracted, and the three Client-nominated companies are used
  for mechanical, electrical and dredging.
- All eight key milestones tie to the correct activity finish dates.
- The program is consistent with the personnel availability dates: every key staff member listed in
  the briefing is free before April 2027.
- The footnote correctly connects the 10 h day, six-day week and 6 pm noise curfew to the fact that
  RCC cannot be placed continuously, and draws the right conclusion about lift-joint treatment.
- Cultural heritage is on the critical path with its own numbered activities rather than being a
  footnote. Given that stakeholders and Aboriginal groups carry 30 of the 100 group marks, this is
  the strongest structural decision in the program.
