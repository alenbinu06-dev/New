# 10. Review findings — construction program, revision B

Defect register for `source/Enoggera_Construction_Program_A3_revB.pdf`, checked against the
briefing data in files 01–05. Supersedes file 09 for every item marked resolved below.

Re-run with `python3 scripts/audit_program_rev_b.py`.

The sheet now declares its relationship notation, so the audit applies it literally:
a bare ID is finish-to-start (`ES = pred finish + 1`), `FS−n` is n months of overlap,
`FS+n` is n months of lag, and `SS+n` means the successor starts n months after the
predecessor starts.

## A. Resolved since revision A

| Was | Now |
|---|---|
| Printed dates reproduced under no scheduling convention | **All 69 start dates reproduce exactly** from the declared notation, and the computed completion is month 25, matching the sheet |
| 51 of 63 float values irreproducible | **All 69 float values reproduce** from a backward pass |
| 9 activities started before a stated predecessor finished | **0** — the overlaps are now declared as `FS−1` and `SS+n` |
| 3 links in the stated critical path did not exist | **0** — every link in the stated chain is in the logic column |
| 7 open-ended activities | **1** (A9, and it is correctly flagged level of effort) |
| Month-number row offset one column left of the bars | **Fixed** — month 1 now sits over Apr 2027 and the year markers over Jan 2028 and Jan 2029 |
| D10 valves, E10 crane, F10 backfill, H1 first fill all unlinked | **All linked**: D10 → H1, E10 → E11, F10 → H7, H1 → H4 |
| Bridge opened month 13, after station concrete started month 12 | **Bridge opens month 11**, before E5 at month 12 |
| No care of water at the dam, no temporary works design, no nominated subcontractor appointment, no salvaged steel haulage, no final channel re-dredge, no E&M load confirmation, 400 dia tube not procured | **All added**: D0, A12, A10, B6, E14, A11, and A4 now includes the tube |
| RCC stated at 30,000–34,000 m³ | **~18,000 m³**, which sits inside the 12,000–20,000 m³ band the briefing geometry supports |
| Two A3 sheets | **One sheet** |
| `Fin` and `CP` columns, and "Self-perform" on 52 rows | **All removed**; delivery is now blank for self-performed work |

Bar geometry was also checked against the table: A1, B6, D0, E3, D7 and H7 all occupy exactly the
columns their Start and Dur imply, and the wet-season shading is correctly on months 8–12 and
20–24.

## B. Outstanding — technical

| # | Finding |
|---|---|
| B1 | **E3, dewatering and excavation to RL 67.0, is 100% inside the wet season and on the critical path with zero float.** Months 8–9 = Nov–Dec 2027, an 8 m deep excavation below reservoir level on two 200 dia pumps. This was raised against revision A and is unchanged. It is the single largest weather risk in the program and it has no float to absorb it. |
| B2 | **RCC placement still starts in the wet season.** D7 runs months 11–16 = Feb–Jul 2028, so 2 of 6 months are wet. Better than the previous 4 of 8, but the start is still in the wet and the sheet's own shading flags RCC as weather-sensitive. |
| B3 | **The concrete-demand footnote is wrong.** It says "Peak concrete demand (months 12–14, three fronts) exceeds one 5 m³ batch plant ... additional agitator capacity is hired for that period." Months 12–14 have only **two** fronts (dam and station). The genuine three-front months are **8** (bridge, dam, pipeline), **11** (bridge, dam, pipeline) and **16** (dam, station, switch yard). The mitigation is aimed at the wrong months. |
| B4 | **B3 quarry and borrow area has no cultural heritage clearance predecessor.** A8 covers "dam, pipeline & dredge areas", not the quarry. B3 breaks new ground at month 2 with only A2 as a predecessor. This undercuts the sheet's own claim that cultural heritage clearance gates the first ground disturbance. Either widen A8's scope in its title or add it as a predecessor of B3. |
| B5 | **G1 switch yard uses `B2 FS+13`.** A 13-month lag is not logic — nothing physically ties switch yard civils to the pump station access track thirteen months earlier. It should be driven by something real, such as area availability after E7 or working back from G2. This is the one place where "every date is derived from this logic" is true in form but not in substance. |
| B6 | **B6 hauls the Gladstone UB in months 2–3 = May–Jun 2027, but the briefing lists the steel beams as "Available July".** The briefing does not state the year, so this needs confirming, but as drawn the haulage precedes availability. |
| B7 | **D0 care of water is only 2 months (months 3–4) while dam works run to month 19.** Care of water is a level-of-effort item that must persist through the whole dam construction, like A9, and there is no activity to decommission the diversion before first fill at month 22. |
| B8 | **A9 cultural heritage monitoring is marked LOE but still carries 3 months of float, and ends at month 22** while H6 site restoration — a ground-disturbing activity — runs months 23–25. A level-of-effort bar should not carry float, and monitoring should extend to the end of ground disturbance. |
| B9 | **F2 names "paving breakers" as the trench excavation method for weathered granite.** Breakers are air-operated hand tools; the company owns two D8 dozers with rippers and a CAT 320, and weathered granite is rippable. Since the briefing judges "the appropriateness of the methods chosen to cope with the physical conditions", ripping should lead and breakers should be reserved for hard spots. |
| B10 | **D6 RCC trial mix and test pad is at month 5 but placement does not start until month 11.** A six-month gap between trial mix and first placement is long enough that the mix would need revalidating. D6 carries 7 months of float, so it can simply be moved later. |
| B11 | **The ~635 m penstock length is a new figure with no stated basis.** The briefing gives no pipeline length and the drawings are explicitly not to scale, so it should be labelled as a measured route length or an assumption. |
| B12 | **H6 demobilisation is driven by H3 via SS+1**, so it starts at month 23 while generation-mode commissioning and performance testing are still running, and it is the activity that sets practical completion. Defensible as staged demobilisation, but the bar should say "staged" or take its logic from H5. |
| B13 | **The plant-on-site question is acknowledged but not shown.** A5 is labelled "staged to lead times", which is the right idea, but the sheet still shows all plant mobilised by month 4 and gives no indication of when the 150 t crane actually arrives (E11 needs it at month 17) or when major items leave. The briefing asks specifically for the time major plant will be on site. |
| B14 | **The "refilling pipeline" is still not named.** Site plan item 7 is "Penstock and refilling pipeline" and item 4 is the separate emergency discharge; section F covers only the penstock and the emergency discharge. |

## C. Outstanding — presentation

| # | Finding |
|---|---|
| C1 | **The critical path sentence names 16 activities but 23 rows carry a triangle.** The legend says the triangle means zero float and on the critical path. The seven not named — A8, A10, E9, E12, H1, H4, H5 — sit on parallel zero-float chains that converge at E1 and again at H7. The sentence should say "critical paths" and name the parallel branches. |
| C2 | **A3 is authorised** — resolved. The group guide says "Submitted in A4 sized documents", but the unit coordinator stated in the Week 2 tutorial: "page 1 to page 11, page 12 is the gantt chart and A3 size." The sheet should carry a one-line note citing that so a marker does not read it as a format breach. |

## E. Resolving E3 — the anchor, the B6 constraint and the RCC window

Run `python3 scripts/scenario_anchor_b6_rcc.py`.

### E.1 The calendar anchor is fixed by the brief

> "The project is to be awarded at the end of March, 2027 and is due for completion by
> 31st May, 2029."

Month 1 = Apr 2027 is **required, not chosen**. The window is Apr 2027 – May 2029 = 26 months and
the program uses 25 with 1 month terminal float. A Dec-2026 anchor would place months 1–4 before the
contract exists and would finish at month 25 = Dec 2028, claiming terminal float that is not real.
**The anchor cannot be used to move E3 out of the wet season.**

### E.2 B6 must be split by source, not date-constrained as one activity

The briefing register treats the two sources differently: the Gladstone UB is "Available July",
while the Emerald sheet piling and corners are "Stacked", i.e. unconstrained. B6 currently bundles
both and feeds both E2 (which needs the Emerald piling) and C4 (which needs the Gladstone UB).

| Treatment | E3 | Completion |
|---|---|---|
| As drawn | M8–9, 2/2 wet | M25 |
| Naive: B6 not earlier than M4 | **M9–10, 2/2 wet — one month deeper** | **M26, all terminal float gone** |
| **Split: B6a Emerald → E2, B6b Gladstone NET M4 → C4** | M8–9 unchanged | M25 unchanged |

Applying the constraint to the bundled activity makes both problems worse. The split removes the
conflict at no schedule cost; B6b lands M4–5 with 8 months of float against C4 at M9.

### E.3 E3 can be improved but not made dry

The chain is A6 (M1) → A8 (M2–3) → E1 (M3–5) → E2 (M5–7) → E3 (M8–9). A8 finishing at M3 is the
floor. The only slack is the E1/E2 relationship, currently `E1 FS−1`.

Changing it to `E1 SS+1` — cofferdam installation starting one month after dredging starts — puts
**E3 at M7–8 = Oct–Nov 2027, one wet month instead of two**, and improves completion to M24.
`SS+0` buys nothing further because B5 and B6a already floor E2 at M4. This is a coordination
decision, not a scheduling trick: it runs the nominated dredging subcontractor alongside
self-performed sheet piling in adjacent water, which is squarely the Principal Contractor's brief.

### E.4 RCC can be bought dry with its own float

| Package | Completion | Terminal float | Zero-float activities | Min dam float | E3 wet | D7 wet |
|---|---|---|---|---|---|---|
| Revision B as drawn | M25 | 1 | 23 of 69 | 2 | 2/2 | 2/6 |
| B6 split + E2 SS+1 | M24 | 2 | 27 of 70 | 1 | 1/2 | 2/6 |
| … + D7 delayed 1 | M24 | 2 | **34 of 70** | 0 | 1/2 | 1/6 |
| … + D7 delayed 2 | M25 | 1 | **14 of 70** | 0 | 1/2 (float 1) | **0/6** |

The intermediate option is the worst: it makes nearly half the program critical for one month of
weather gain. Delaying D7 by two months puts RCC entirely in Apr–Sep 2028, gives E3 a month of
float, and leaves the leanest critical network, at the cost of returning to 1 month terminal float
and making the dam chain critical.

Either way the sheet's line "the dam is NOT critical" needs rewriting, because the dam chain loses
its float in every package that improves the weather exposure.

## D. Strengths worth keeping

- The declared logic notation with `FS−n` and `SS+n`, and the claim that every date is reproducible
  from it, is now **true**. That is unusual at this level and is exactly what the rubric means by
  "logically and accurately addressed with well argued reasons".
- Cultural heritage is on the critical path with its own numbered activities, which is the clearest
  available cross-link between the program (15 marks) and the stakeholder criterion (30 marks).
- The additions since revision A — care of water, temporary works design, nominated subcontractor
  appointment, E&M load confirmation feeding the bridge D&C, salvaged steel haulage, final channel
  re-dredge — each close a specific gap in the briefing rather than padding the bar count.
- All ten milestones tie to the correct activity dates.
- The subcontracting split still matches the briefing exactly.
