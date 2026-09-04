#!/usr/bin/env python3
"""Audit the Enoggera preliminary construction program.

Re-runs the program's own activity table (durations + declared predecessors)
through a strict finish-to-start CPM and compares against the printed
Start / Fin / Float / critical-path values.
"""

# id: (name, preds, start, dur, fin, float, cp_marked)
A = {
 "A1": ("Contract award, mobilisation & insurances", [], 1, 1, 1, 0, True),
 "A2": ("Site establishment - compound, offices, services", ["A1"], 1, 2, 2, 23, False),
 "A3": ("Survey, set-out & geotechnical confirmation", ["A1"], 1, 2, 2, 23, False),
 "A4": ("Long-lead procurement - batch plant, 150t crane, lifting gear", ["A1"], 1, 3, 3, 3, False),
 "A5": ("Plant mobilisation (staged to lead times)", ["A4"], 2, 3, 4, 3, False),
 "A6": ("Cultural heritage due diligence & TO engagement", ["A1"], 1, 1, 1, 0, True),
 "A7": ("CH survey & clearance - access corridors", ["A6"], 1, 1, 1, 0, True),
 "A8": ("CH survey & clearance - dam, pipeline & dredge", ["A6"], 2, 2, 3, 0, True),
 "A9": ("CH monitoring & stop-work protocol (ongoing)", ["A8"], 3, 20, 22, 3, False),
 "B1": ("Access road to dam site", ["A1", "A7"], 1, 3, 3, 3, False),
 "B2": ("Access track & laydown - pump station area", ["A1", "A7"], 1, 2, 2, 0, True),
 "B3": ("Quarry / borrow area, crushing & screening", ["A1"], 2, 3, 4, 3, False),
 "B4": ("Concrete batch plant erection & commissioning", ["B3", "A4"], 3, 2, 4, 3, False),
 "B5": ("Temporary marine access - barges & workboats", ["B2"], 3, 1, 3, 22, False),
 "C1": ("Bridge design & client approval (D&C)", ["A1"], 1, 4, 4, 3, False),
 "C2": ("Pier piling - 400 dia steel tube piles", ["C1", "A5", "E1"], 6, 2, 7, 2, False),
 "C3": ("Pier caps & substructure", ["C2"], 10, 2, 11, 5, False),
 "C4": ("Deck erection - salvaged 610x230 UB beams", ["C3"], 11, 2, 12, 5, False),
 "C5": ("Deck concrete, barriers & surfacing", ["C4"], 12, 2, 13, 5, False),
 "C6": ("Bridge services & cable ducts", ["C5"], 13, 1, 13, 5, False),
 "D1": ("Foundation stripping & excavation to sound rock", ["B1", "A8"], 4, 3, 6, 3, False),
 "D2": ("Foundation prep, cleanup & dental concrete", ["D1"], 6, 2, 7, 3, False),
 "D3": ("Concrete cut-off wall (1.0 m)", ["D2"], 7, 2, 8, 3, False),
 "D4": ("Grout curtain (subcontract)", ["D3"], 8, 3, 10, 3, False),
 "D5": ("Emergency discharge pipe 2.0 m dia at RL 88", ["D3"], 8, 2, 9, 3, False),
 "D6": ("RCC trial mix & test pad", ["B4"], 8, 1, 8, 3, False),
 "D7": ("RCC placement RL 88 -> RL 102", ["D4", "D5", "D6"], 9, 8, 16, 3, False),
 "D8": ("Penstock through-dam section 1.5 m dia at RL 92", ["D7"], 12, 2, 13, 4, False),
 "D9": ("Spillway section & crest slab", ["D7"], 17, 2, 18, 3, False),
 "D10": ("Valve actuating mechanism & gates", ["D9"], 18, 2, 19, 6, False),
 "D11": ("Upstream facing & dam finishing works", ["D9"], 18, 2, 19, 3, False),
 "E1": ("Dredging of intake channel to RL 68.5", ["B2", "A8"], 3, 3, 5, 0, True),
 "E2": ("Sheet pile cofferdam - salvaged BHP piling", ["E1"], 5, 3, 7, 0, True),
 "E3": ("Dewatering & excavation to RL 67.0", ["E2"], 8, 2, 9, 0, True),
 "E4": ("Steel tube pile driving 400 dia - station founds", ["E3", "C2"], 10, 2, 11, 0, True),
 "E5": ("Blinding & base slab RL 67.0", ["E4"], 12, 2, 13, 0, True),
 "E6": ("Substructure walls RL 67.0 -> RL 75.0", ["E5"], 13, 2, 14, 0, True),
 "E7": ("Superstructure RL 75.0 -> RL 83.0 incl. roof", ["E6"], 15, 2, 16, 0, True),
 "E8": ("Screens & inlet works", ["E7"], 16, 2, 17, 2, False),
 "E9": ("Building trades fit-out (subcontract)", ["E7"], 17, 2, 18, 0, True),
 "E10": ("Maintenance crane installation", ["E7"], 17, 1, 17, 8, False),
 "E11": ("Mechanical installation - turbine, pump, generator", ["E7", "C6"], 17, 4, 20, 0, True),
 "E12": ("Electrical installation & control room", ["E11", "E9"], 18, 3, 20, 0, True),
 "E13": ("Cofferdam removal & reinstatement", ["E8"], 21, 2, 22, 2, False),
 "F1": ("Route survey, clearing & access track", ["B1"], 11, 2, 12, 3, False),
 "F2": ("Trench excavation - weathered granite", ["F1", "A8"], 12, 4, 15, 3, False),
 "F3": ("Pipe delivery & site welding yard setup", ["F1"], 13, 2, 14, 3, False),
 "F4": ("Penstock 1.5 m dia - laying & welded jointing", ["F2", "F3"], 14, 5, 18, 3, False),
 "F5": ("Emergency discharge line - laying & jointing", ["F4"], 15, 4, 18, 3, False),
 "F6": ("Thrust & anchor blocks at bends", ["F4"], 15, 4, 18, 3, False),
 "F7": ("Tie-in to dam outlet RL 92", ["F4", "D8"], 18, 1, 18, 3, False),
 "F8": ("Tie-in to pump station RL 70", ["F4", "E6"], 18, 2, 19, 3, False),
 "F9": ("Hydrostatic pressure testing", ["F7", "F8", "F5", "F6"], 19, 2, 20, 3, False),
 "F10": ("Backfill & reinstatement", ["F9"], 20, 3, 22, 6, False),
 "G1": ("Switch yard civils & earthing", ["B2"], 17, 3, 19, 4, False),
 "G2": ("Transmission line connection to suburban network", ["G1", "E12"], 21, 3, 23, 1, False),
 "H1": ("Initial impoundment (first fill) & dam monitoring", ["D11", "F9", "H2"], 22, 2, 23, 1, False),
 "H2": ("Mechanical & electrical pre-commissioning", ["E11", "E12", "F9"], 21, 2, 22, 0, True),
 "H3": ("Wet commissioning - pump mode", ["H2"], 22, 2, 23, 0, True),
 "H4": ("Wet commissioning - generation mode", ["H3"], 23, 2, 24, 0, True),
 "H5": ("Performance & compliance testing", ["H4"], 24, 1, 24, 0, True),
 "H6": ("Demobilisation & site restoration", ["H4"], 23, 3, 25, 0, True),
 "H7": ("Practical completion & handover", ["H5", "H6", "H1", "E13", "G2"], 25, 1, 25, 0, True),
}

STATED_CP = ("A1 A6 A7 B2 A8 E1 E2 E3 E4 E5 E6 E7 E9 E11 E12 H2 H3 H4 H5 H6 H7").split()

MONTHS = ["Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
          "Jan", "Feb", "Mar"]


def month_label(n):
    idx = (n - 1) % 12
    year = 2027 + (n - 1 + 3) // 12
    return f"{MONTHS[idx]} {year}"


def hdr(t):
    print()
    print("=" * 104)
    print(t)
    print("=" * 104)


succ = {k: [] for k in A}
for k, (_, preds, *_rest) in A.items():
    for p in preds:
        succ[p].append(k)

# ---------------------------------------------------------------- 1. arithmetic
hdr("CHECK 1 — Fin = Start + Dur - 1")
bad = [k for k, (_, _, s, d, f, *_r) in A.items() if s + d - 1 != f]
print(f"Activities: {len(A)}   rows failing the arithmetic: {len(bad)}  {bad}")
print("=> The bar arithmetic itself is internally consistent on every row.")

# ------------------------------------------------- 2. finish-to-start integrity
hdr("CHECK 2 — does each activity start after its stated predecessors finish?")
hard, soft, ok = [], [], []
for k, (_, preds, s, d, f, fl, cp) in A.items():
    if not preds:
        continue
    pf = max(A[p][4] for p in preds)
    drv = [p for p in preds if A[p][4] == pf]
    if s < pf:
        hard.append((k, s, pf, drv))
    elif s == pf:
        soft.append((k, s, pf, drv))
    else:
        ok.append(k)
print(f"  starts strictly BEFORE a predecessor finishes (impossible)   : {len(hard)}")
print(f"  starts in the SAME month a predecessor finishes (overlap)    : {len(soft)}")
print(f"  starts the month AFTER the last predecessor finishes (clean) : {len(ok)}")
print()
print("  HARD violations — the activity begins while a predecessor is still running:")
for k, s, pf, drv in hard:
    print(f"    {k:<4} starts M{s:<2} but {'/'.join(drv)} does not finish until M{pf}"
          f"   ({pf - s} month overlap)   {A[k][0]}")
print()
print("  The remaining rows are split between two different conventions, which is why")
print("  the network cannot be reproduced: same-month starts =", len(soft),
      "vs next-month starts =", len(ok))

# ------------------------------------------------------------- 3. open ends
hdr("CHECK 3 — open-ended activities (no successor, so they drive nothing)")
dangle = [k for k in A if not succ[k] and k != "H7"]
for k in dangle:
    print(f"    {k:<4} M{A[k][2]}-{A[k][4]}  float {A[k][5]:<2}  {A[k][0]}")
print(f"  => {len(dangle)} activities float free of the network.")

# ------------------------------------------------- 4. stated critical path links
hdr("CHECK 4 — does the stated critical path exist in the logic table?")
print("  Stated: " + " -> ".join(STATED_CP))
print()
broken = []
for a, b in zip(STATED_CP, STATED_CP[1:]):
    if a not in A[b][1]:
        broken.append((a, b))
        print(f"    BROKEN LINK  {a} -> {b} : {b}'s stated predecessors are {A[b][1]}"
              f"  ({a} is not one of them)")
if not broken:
    print("    all links present")
print()
marked = {k for k in A if A[k][6]}
print(f"  Activities flagged with a CP dot : {len(marked)}")
print(f"  Activities named in the CP string: {len(set(STATED_CP))}")
print(f"  Flagged but not in the string    : {sorted(marked - set(STATED_CP))}")

# ------------------------------------------- 5. strict CPM using the same logic
hdr("CHECK 5 — re-run the SAME durations and logic under strict finish-to-start")
ES, EF = {}, {}
order, seen = [], set()


def visit(k, stack=()):
    if k in seen:
        return
    if k in stack:
        raise SystemExit(f"cycle at {k}")
    for p in A[k][1]:
        visit(p, stack + (k,))
    seen.add(k)
    order.append(k)


for k in A:
    visit(k)
for k in order:
    preds = A[k][1]
    ES[k] = 1 if not preds else max(EF[p] for p in preds) + 1
    EF[k] = ES[k] + A[k][3] - 1

finish = max(EF.values())
LS, LF, TF = {}, {}, {}
for k in reversed(order):
    LF[k] = finish if not succ[k] else min(LS[s] for s in succ[k]) - 1
    LS[k] = LF[k] - A[k][3] + 1
    TF[k] = LF[k] - EF[k]

print(f"  Program as printed  : practical completion month 25  ({month_label(25)})")
print(f"  Same logic, strict  : practical completion month {finish}  ({month_label(finish)})")
print(f"  Slip               : {finish - 25} months")
print(f"  Contract completion : month 26 ({month_label(26)}) = 31 May 2029")
over = finish - 26
print(f"  => strict CPM finishes {over} months AFTER the contractual completion date"
      if over > 0 else "  => still inside the contract date")
print()
true_cp = sorted([k for k in A if TF[k] == 0], key=lambda k: (ES[k], k))
print("  True zero-float chain under strict logic:")
print("    " + " -> ".join(true_cp))
print()
print(f"  Stated critical activities : {len(marked)}")
print(f"  Strict critical activities : {len(true_cp)}")
print(f"  Marked critical but is NOT : {sorted(marked - set(true_cp))}")
print(f"  Critical but NOT marked    : {sorted(set(true_cp) - marked)}")

# -------------------------------------------------------------- 6. float column
hdr("CHECK 6 — can the printed Float column be reproduced?")
mismatch = [(k, A[k][5], TF[k]) for k in A if A[k][5] != TF[k]]
print(f"  Rows where printed float != recomputed float: {len(mismatch)} of {len(A)}")
for k, printed, calc in sorted(mismatch, key=lambda t: -abs(t[1] - t[2]))[:12]:
    print(f"    {k:<4} printed {printed:<3} recomputed {calc:<3}  {A[k][0][:56]}")

# ------------------------------------------------------- 7. RCC volume sanity
hdr("CHECK 7 — RCC volume stated on the bar vs the briefing geometry")
crest_w, base_w, crest_len = 4.0, 13.0, 250.0
for top, base, lbl in ((102, 86, "RL 102 to founding RL 86 (16 m)"),
                       (102, 88, "RL 102 to RL 88 as the bar states (14 m)")):
    Hmax = top - base
    batter = (base_w - crest_w) / Hmax

    def area(h):
        return crest_w * h + batter * h * h / 2

    n = 20000
    for shape, hf in (("V-shaped valley", lambda t: Hmax * (1 - abs(t))),
                      ("parabolic valley", lambda t: Hmax * (1 - t * t))):
        vol = sum(area(hf(-1 + 2 * i / n)) for i in range(n + 1)) * crest_len / (n + 1)
        print(f"    {lbl:<38} {shape:<17} ~{vol:6,.0f} m3")
print()
print("    Stated on the bar: ~30,000-34,000 m3")
print("    Lifts: RL 88 -> RL 102 = 14 m at 300 mm/lift = 46.7 lifts -> '~47 lifts' checks out.")
print("    But 47 lifts x 250 m x mean section cannot reach 30,000 m3 with a 4 m crest,")
print("    13 m base and a 250 m crest length. The volume and the lift count disagree.")
