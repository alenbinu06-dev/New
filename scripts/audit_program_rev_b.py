#!/usr/bin/env python3
"""Audit rev B of the Enoggera preliminary construction program.

Relationship notation as defined on the sheet:
  bare ID  = FS   -> ES_succ = pred_Fin + 1
  FS-n     = FS with n months overlap -> ES_succ = pred_Fin + 1 - n
  FS+n     = FS with n months lag     -> ES_succ = pred_Fin + 1 + n
  SS+n                                -> ES_succ = pred_Start + n
"""

# id: (name, [(pred, type, lag)], start, dur, float, critical_marked)
FS, SS = "FS", "SS"
A = {
 "A1": ("Contract award, mobilisation & insurances", [], 1, 1, 0, True),
 "A2": ("Site establishment", [("A1", FS, -1)], 1, 2, 7, False),
 "A3": ("Survey, set-out & geotechnical confirmation", [("A1", FS, -1)], 1, 2, 3, False),
 "A4": ("Long-lead procurement incl. 400 dia tube", [("A1", FS, -1)], 1, 3, 1, False),
 "A5": ("Plant mobilisation", [("A4", SS, 1)], 2, 3, 1, False),
 "A6": ("Cultural heritage due diligence & TO engagement", [("A1", FS, -1)], 1, 1, 0, True),
 "A7": ("CH survey & clearance - access corridors", [("A6", FS, -1)], 1, 1, 0, True),
 "A8": ("CH survey & clearance - dam, pipeline, dredge", [("A6", FS, 0)], 2, 2, 0, True),
 "A9": ("CH monitoring & stop-work protocol (LOE)", [("A8", FS, -1)], 3, 20, 3, False),
 "A10": ("Nominated subcontractor appointment & mobilisation", [("A1", FS, -1)], 1, 2, 0, True),
 "A11": ("Confirm E&M assembly & delivery loads", [("A10", FS, -1)], 2, 1, 2, False),
 "A12": ("Temporary works conceptual design", [("A1", FS, 0)], 2, 2, 2, False),
 "B1": ("Access road to dam site", [("A7", FS, -1)], 1, 3, 2, False),
 "B2": ("Access track & laydown - pump station", [("A7", FS, -1)], 1, 2, 0, True),
 "B3": ("Quarry / borrow area, crushing & screening", [("A2", FS, -1)], 2, 3, 7, False),
 "B4": ("Concrete batch plant erection & commissioning", [("B3", SS, 1), ("A4", FS, -1)], 3, 2, 7, False),
 "B5": ("Temporary marine access - barges & workboats", [("B2", FS, 0)], 3, 1, 1, False),
 "B6": ("Haulage of salvaged steel - Emerald, Gladstone", [("A5", SS, 0)], 2, 2, 1, False),
 "C1": ("Bridge design & client approval (D&C)", [("A11", FS, -1)], 2, 4, 2, False),
 "C2": ("Pier piling - 400 dia steel tube piles",
        [("C1", FS, 0), ("A5", FS, 0), ("B5", FS, 0), ("E1", FS, 0)], 6, 2, 2, False),
 "C3": ("Pier caps & substructure", [("C2", FS, 0)], 8, 2, 5, False),
 "C4": ("Deck erection - salvaged 610x230 UB", [("C3", FS, -1), ("B6", FS, 0)], 9, 2, 5, False),
 "C5": ("Deck concrete, barriers & surfacing", [("C4", FS, -1)], 10, 2, 5, False),
 "C6": ("Bridge services & cable ducts", [("C5", FS, -1)], 11, 1, 5, False),
 "D0": ("Care of water & stream diversion - dam site", [("B1", FS, -1), ("A12", FS, -1)], 3, 2, 2, False),
 "D1": ("Foundation stripping & excavation to sound rock",
        [("B1", FS, 0), ("A8", FS, 0), ("A3", FS, 0), ("D0", FS, -1)], 4, 3, 2, False),
 "D2": ("Foundation prep, cleanup & dental concrete", [("D1", FS, -1)], 6, 2, 2, False),
 "D3": ("Concrete cut-off wall (1.0 m)", [("D2", FS, -1)], 7, 2, 2, False),
 "D4": ("Grout curtain", [("D3", FS, -1)], 8, 3, 2, False),
 "D5": ("Emergency discharge pipe 2.0 m dia at RL 88", [("D3", FS, -1)], 8, 2, 3, False),
 "D6": ("RCC trial mix & test pad", [("B4", FS, 0)], 5, 1, 7, False),
 "D7": ("RCC placement RL 88 -> RL 102 (~18,000 m3, 47 lifts)",
        [("D4", FS, 0), ("D5", FS, 0), ("D6", FS, 0)], 11, 6, 2, False),
 "D8": ("Penstock through-dam section at RL 92", [("D7", SS, 3)], 14, 2, 2, False),
 "D9": ("Spillway section & crest slab", [("D7", FS, 0)], 17, 2, 2, False),
 "D10": ("Valve actuating mechanism & gates", [("D9", FS, -1)], 18, 2, 2, False),
 "D11": ("Upstream facing & dam finishing works", [("D9", FS, -1)], 18, 2, 2, False),
 "E1": ("Dredging of intake channel to RL 68.5",
        [("B2", FS, 0), ("A8", FS, -1), ("A10", FS, 0)], 3, 3, 0, True),
 "E2": ("Sheet pile cofferdam - salvaged BHP piling",
        [("E1", FS, -1), ("B5", FS, 0), ("B6", FS, 0), ("A12", FS, -1)], 5, 3, 0, True),
 "E3": ("Dewatering & excavation to RL 67.0", [("E2", FS, 0)], 8, 2, 0, True),
 "E4": ("Steel tube pile driving - station foundations", [("E3", FS, 0), ("C2", FS, 0)], 10, 2, 0, True),
 "E5": ("Blinding & base slab RL 67.0", [("E4", FS, 0)], 12, 2, 0, True),
 "E6": ("Substructure walls RL 67.0 -> RL 75.0", [("E5", FS, -1)], 13, 2, 0, True),
 "E7": ("Superstructure RL 75.0 -> RL 83.0 incl. roof", [("E6", FS, 0)], 15, 2, 0, True),
 "E8": ("Screens & inlet works", [("E7", FS, -1)], 16, 2, 4, False),
 "E9": ("Building trades fit-out", [("E7", FS, 0)], 17, 2, 0, True),
 "E10": ("Maintenance crane installation", [("E7", SS, 1)], 16, 1, 1, False),
 "E11": ("Mechanical installation - turbine, pump, generator",
         [("E7", FS, 0), ("C6", FS, 0), ("E10", FS, -1)], 17, 4, 0, True),
 "E12": ("Electrical installation & control room", [("E11", SS, 1), ("E9", FS, -1)], 18, 3, 0, True),
 "E13": ("Cofferdam removal & reinstatement", [("E8", FS, 0), ("E11", SS, 2)], 19, 2, 3, False),
 "E14": ("Final trim & re-dredge of intake channel", [("E13", FS, 0)], 21, 1, 3, False),
 "F1": ("Route survey, clearing & access track", [("B1", FS, 0), ("A8", FS, 0)], 4, 2, 7, False),
 "F2": ("Trench excavation - weathered granite", [("F1", FS, -1)], 5, 4, 7, False),
 "F3": ("Pipe delivery & site welding yard setup", [("F1", FS, 0)], 6, 2, 7, False),
 "F4": ("Penstock 1.5 m dia - laying & welded jointing (~635 m)",
        [("F2", SS, 2), ("F3", FS, -1)], 7, 5, 7, False),
 "F5": ("Emergency discharge line - laying & jointing", [("F4", SS, 1)], 8, 4, 7, False),
 "F6": ("Thrust & anchor blocks at bends", [("F4", SS, 1)], 8, 4, 7, False),
 "F7": ("Tie-in to dam outlet RL 92", [("F4", FS, -1), ("D8", FS, 0)], 16, 1, 2, False),
 "F8": ("Tie-in to pump station RL 70", [("F4", FS, -1), ("E6", FS, 0)], 15, 2, 3, False),
 "F9": ("Hydrostatic pressure testing",
        [("F7", FS, 0), ("F8", FS, -1), ("F5", FS, 0), ("F6", FS, 0)], 17, 2, 2, False),
 "F10": ("Backfill & reinstatement", [("F9", SS, 1)], 18, 3, 4, False),
 "G1": ("Switch yard civils & earthing", [("B2", FS, 13)], 16, 3, 4, False),
 "G2": ("Transmission line connection", [("G1", FS, -1), ("E12", FS, 0)], 21, 3, 1, False),
 "H1": ("Initial impoundment (first fill) & dam monitoring",
        [("D11", FS, 0), ("D10", FS, 0), ("F9", FS, 0), ("H2", FS, -1)], 22, 2, 0, True),
 "H2": ("Mechanical & electrical pre-commissioning",
        [("E11", FS, 0), ("E12", FS, 0), ("F9", FS, 0)], 21, 2, 0, True),
 "H3": ("Wet commissioning - pump mode", [("H2", FS, -1)], 22, 2, 0, True),
 "H4": ("Wet commissioning - generation mode", [("H3", FS, -1), ("H1", FS, -1)], 23, 2, 0, True),
 "H5": ("Performance & compliance testing", [("H4", FS, -1)], 24, 1, 0, True),
 "H6": ("Demobilisation & site restoration", [("H3", SS, 1)], 23, 3, 0, True),
 "H7": ("Practical completion & handover",
        [("H5", FS, 0), ("H6", FS, -1), ("F10", FS, 0), ("E14", FS, 0), ("G2", FS, 0)], 25, 1, 0, True),
}

STATED_CP = "A1 A6 A7 B2 E1 E2 E3 E4 E5 E6 E7 E11 H2 H3 H6 H7".split()
MONTHS = ["Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Jan", "Feb", "Mar"]
WET = set(range(8, 13)) | set(range(20, 25))          # Nov-Mar in both years


def ml(n):
    return f"{MONTHS[(n - 1) % 12]} {2027 + (n - 1 + 3) // 12}"


def hdr(t):
    print("\n" + "=" * 100 + f"\n{t}\n" + "=" * 100)


fin = {k: v[2] + v[3] - 1 for k, v in A.items()}
succ = {k: [] for k in A}
for k, v in A.items():
    for p, _t, _l in v[1]:
        succ[p].append(k)

order, seen = [], set()


def visit(k):
    if k in seen:
        return
    for p, _t, _l in A[k][1]:
        visit(p)
    seen.add(k)
    order.append(k)


for k in A:
    visit(k)

# ------------------------------------------------------------------- forward
hdr("CHECK 1 - forward pass: does the sheet's own notation reproduce every Start?")
ES, EF = {}, {}
bad = []
for k in order:
    preds = A[k][1]
    if not preds:
        ES[k] = 1
    else:
        cands = []
        for p, t, lag in preds:
            cands.append(EF[p] + 1 + lag if t == FS else ES[p] + lag)
        ES[k] = max(cands)
    EF[k] = ES[k] + A[k][3] - 1
    if ES[k] != A[k][2]:
        bad.append((k, A[k][2], ES[k]))
print(f"  activities: {len(A)}")
print(f"  printed Start != computed Start on {len(bad)} rows  {bad}")
print(f"  computed completion: month {max(EF.values())} ({ml(max(EF.values()))})   printed: month 25 ({ml(25)})")
print("  => the sheet's claim that every date is reproducible from the logic HOLDS."
      if not bad else "  => claim fails")

# ------------------------------------------------------------------ backward
hdr("CHECK 2 - backward pass: does the printed Float column reproduce?")
T = max(EF.values())
LS, LF, TF = {}, {}, {}
for k in reversed(order):
    if not succ[k]:
        LF[k] = T
    else:
        lim = []
        for s in succ[k]:
            for p, t, lag in A[s][1]:
                if p != k:
                    continue
                lim.append(LS[s] - 1 - lag if t == FS else LS[s] - lag + A[k][3] - 1)
        LF[k] = min(lim)
    LS[k] = LF[k] - A[k][3] + 1
    TF[k] = LF[k] - EF[k]
mis = [(k, A[k][4], TF[k]) for k in A if A[k][4] != TF[k]]
print(f"  rows where printed float != recomputed float: {len(mis)} of {len(A)}")
for k, pr, ca in sorted(mis, key=lambda t: -abs(t[1] - t[2])):
    print(f"    {k:<4} printed {pr:<3} recomputed {ca:<3}  {A[k][0][:58]}")

# ------------------------------------------------------------- critical path
hdr("CHECK 3 - critical path")
broken = [(a, b) for a, b in zip(STATED_CP, STATED_CP[1:])
          if a not in [p for p, _t, _l in A[b][1]]]
print(f"  links in the stated chain that do not exist in the logic: {len(broken)} {broken}")
marked = {k for k in A if A[k][5]}
calc = {k for k in A if TF[k] == 0}
print(f"  rows marked with a triangle : {len(marked)}")
print(f"  rows in the stated CP string: {len(set(STATED_CP))}")
print(f"  recomputed zero-float rows  : {len(calc)}")
print(f"  marked but not in the string: {sorted(marked - set(STATED_CP))}")
print(f"  marked but not zero float   : {sorted(marked - calc)}")
print(f"  zero float but not marked   : {sorted(calc - marked)}")

# ------------------------------------------------------------------ open ends
hdr("CHECK 4 - open-ended activities")
d = [k for k in A if not succ[k] and k != "H7"]
print(f"  {len(d)}: " + ", ".join(f"{k} ({A[k][0]}, float {A[k][4]})" for k in d))

# ----------------------------------------------------------------- wet season
hdr("CHECK 5 - weather-sensitive work in the wet season (Nov-Mar shaded)")
for k in ("D1", "D7", "E2", "E3", "F2", "B3"):
    s, f = A[k][2], fin[k]
    months = list(range(s, f + 1))
    w = [m for m in months if m in WET]
    print(f"    {k:<4} M{s}-{f} = {ml(s)} to {ml(f)}   wet-season months: {len(w)}/{len(months)}"
          f"{'   <-- CRITICAL PATH' if A[k][5] else ''}")

# -------------------------------------------------------------- concrete peak
hdr("CHECK 6 - the footnote claims peak concrete demand is 'months 12-14, three fronts'")
conc = {"D2": ("dam", 6, 7), "D3": ("dam", 7, 8), "D6": ("dam", 5, 5), "D7": ("dam", 11, 16),
        "D8": ("dam", 14, 15), "D9": ("dam", 17, 18), "D11": ("dam", 18, 19),
        "C3": ("bridge", 8, 9), "C5": ("bridge", 10, 11),
        "E5": ("station", 12, 13), "E6": ("station", 13, 14), "E7": ("station", 15, 16),
        "F6": ("pipeline", 8, 11), "G1": ("switchyard", 16, 18)}
print("   month | activities | distinct fronts")
for m in range(5, 20):
    act = [k for k, (_f, s, f) in conc.items() if s <= m <= f]
    fr = {conc[k][0] for k in act}
    flag = "  <-- 3 fronts" if len(fr) >= 3 else ""
    print(f"     {m:>3}  |     {len(act)}      |   {len(fr)}  {sorted(fr)}{flag}")
