#!/usr/bin/env python3
"""Scenario tests for the Enoggera program under the fixed April-2027 anchor.

Answers three questions raised against revision B:
  1. Is the calendar anchor a free variable?
  2. How should the Gladstone "Available July" constraint on B6 be applied?
  3. Where does RCC placement land if D7's own float is spent?
"""

import contextlib
import copy
import io
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
with contextlib.redirect_stdout(io.StringIO()):
    from audit_program_rev_b import A as BASE, FS, SS, MONTHS, WET


def ml(n):
    return f"{MONTHS[(n - 1) % 12]} {2027 + (n - 1 + 3) // 12}"


def wet(s, f):
    ms = list(range(s, f + 1))
    return sum(1 for m in ms if m in WET), len(ms)


def solve(acts, nets=None):
    """Forward and backward pass. nets maps an activity id to a not-earlier-than month."""
    nets = nets or {}
    succ = {k: [] for k in acts}
    for k, v in acts.items():
        for p, _t, _l in v[1]:
            succ[p].append(k)
    order, seen = [], set()

    def visit(k):
        if k in seen:
            return
        for p, _t, _l in acts[k][1]:
            visit(p)
        seen.add(k)
        order.append(k)

    for k in acts:
        visit(k)
    ES, EF = {}, {}
    for k in order:
        cands = [nets.get(k, 1)]
        for p, t, lag in acts[k][1]:
            cands.append(EF[p] + 1 + lag if t == FS else ES[p] + lag)
        ES[k] = max(cands)
        EF[k] = ES[k] + acts[k][3] - 1
    T = max(EF.values())
    LS, LF, TF = {}, {}, {}
    for k in reversed(order):
        if not succ[k]:
            LF[k] = T
        else:
            lim = []
            for s in succ[k]:
                for p, t, lag in acts[s][1]:
                    if p == k:
                        lim.append(LS[s] - 1 - lag if t == FS
                                   else LS[s] - lag + acts[k][3] - 1)
            LF[k] = min(lim)
        LS[k] = LF[k] - acts[k][3] + 1
        TF[k] = LF[k] - EF[k]
    return ES, EF, TF, T


def split_b6(acts):
    """Split B6 into its two sources: Emerald piling feeds E2, Gladstone UB feeds C4."""
    v = copy.deepcopy(acts)
    v["B6a"] = ("Haul sheet piling & corners - Emerald (Stacked)", [("A5", SS, 0)], 2, 2, 1, False)
    v["B6b"] = ("Haul 610x230 UB - Gladstone (Available July)", [("A5", SS, 0)], 4, 2, 1, False)
    del v["B6"]
    for k in list(v):
        v[k] = (v[k][0],
                [(("B6a" if k == "E2" else "B6b") if p == "B6" else p, t, l)
                 for p, t, l in v[k][1]],
                *v[k][2:])
    return v


def line(tag, acts, nets=None, watch=("E3", "D7")):
    ES, EF, TF, T = solve(acts, nets)
    print(f"\n  {tag}")
    print(f"     completion M{T} ({ml(T)})   terminal float vs contract M26 = {26 - T}")
    for k in watch:
        if k not in acts:
            continue
        w, n = wet(ES[k], EF[k])
        print(f"     {k:<5} M{ES[k]}-{EF[k]} = {ml(ES[k])}-{ml(EF[k])}   wet {w}/{n}   "
              f"float {TF[k]}{'   <-- fully dry' if w == 0 else ''}")
    return ES, EF, TF, T


def head(t):
    print("\n" + "=" * 98 + f"\n{t}\n" + "=" * 98)


head("Q1  IS THE CALENDAR ANCHOR A FREE VARIABLE?")
print('  Briefing, "Additional Information - Timing":')
print('    "The project is to be awarded at the end of March, 2027 and is due for')
print('     completion by 31st May, 2029."')
print()
print("  => Month 1 = Apr 2027 is REQUIRED, not chosen. The available window is")
print("     Apr 2027 - May 2029 = 26 months, and the program uses 25 with 1 month")
print("     terminal float.")
print("  => A Dec-2026 anchor would place months 1-4 before the contract exists and")
print("     would finish at month 25 = Dec 2028, claiming terminal float that is not real.")
print("  => The anchor cannot be used to move E3 out of the wet season.")

head("Q2  THE GLADSTONE CONSTRAINT ON B6")
print("  Briefing salvaged materials register:")
print("    steel beams 610x230 UB, 330 m, Gladstone .......... 'Available July'")
print("    steel sheet piling BHP 50 lb, 1900 m, Emerald ..... 'Stacked'  (no constraint)")
print("    sheetpile corners, 4 off, Emerald ................. 'Stacked'  (no constraint)")
print()
print("  B6 currently bundles both sources into one activity that feeds both E2")
print("  (which needs the Emerald piling) and C4 (which needs the Gladstone UB).")
base = copy.deepcopy(BASE)
line("as drawn", base)
line("naive fix: B6 not earlier than M4 (= July 2027)", base, {"B6": 4})
print("     ^ pushes E2, drives E3 one month DEEPER into the wet season,")
print("       and consumes the whole terminal float.")
sp = split_b6(base)
line("split by source: B6a Emerald -> E2, B6b Gladstone NET M4 -> C4", sp, {"B6b": 4},
     watch=("E3", "D7", "B6a", "B6b", "C4"))
print("     ^ conflict removed at no schedule cost.")

head("Q3  HOW FAR CAN E3 BE PULLED FORWARD WITHOUT COMPRESSING HERITAGE CLEARANCE?")
print("  Chain to E3:  A6 (M1) -> A8 (M2-3) -> E1 (M3-5) -> E2 (M5-7) -> E3 (M8-9)")
print("  A8 finishing M3 is the floor: E1 cannot start before M3.")
print("  The only slack is the E1/E2 relationship, currently E1 FS-1.")
for lag in (1, 0):
    v = copy.deepcopy(sp)
    v["E2"] = (v["E2"][0], [("E1", SS, lag)] + [(p, t, l) for p, t, l in v["E2"][1] if p != "E1"],
               *v["E2"][2:])
    line(f"E2 = E1 SS+{lag}", v, {"B6b": 4}, watch=("E1", "E2", "E3", "D7"))
print("\n  SS+0 buys nothing over SS+1: B5 and B6a already floor E2 at M4.")
print("  Best available is E3 at M7-8 = Oct-Nov 2027, i.e. 1 wet month instead of 2,")
print("  and the completion date improves to M24, giving 2 months of terminal float.")

head("Q4  RCC - WHERE DOES D7 LAND IF ITS FLOAT IS SPENT? (on top of the Q3 package)")
best = copy.deepcopy(sp)
best["E2"] = (best["E2"][0],
              [("E1", SS, 1)] + [(p, t, l) for p, t, l in best["E2"][1] if p != "E1"],
              *best["E2"][2:])
ES0, _, _, _ = solve(best, {"B6b": 4})
for shift in (0, 1, 2, 3):
    ES, EF, TF, T = solve(best, {"B6b": 4, "D7": ES0["D7"] + shift})
    w, n = wet(ES["D7"], EF["D7"])
    dam = min(TF[k] for k in best if k.startswith("D") and k != "D6")
    verdict = "LATE" if T > 26 else "ok"
    print(f"  D7 +{shift}:  M{ES['D7']}-{EF['D7']} = {ml(ES['D7'])}-{ml(EF['D7'])}   "
          f"wet {w}/6   D7 float {TF['D7']}   min dam float {dam}   "
          f"completion M{T}   [{verdict}]{'   <-- fully dry' if w == 0 else ''}")
print("\n  +1 is free in completion terms and removes the February exposure.")
print("  +2 removes the March exposure as well but costs a month of terminal float")
print("     and makes the dam chain critical.")

head("EFFECT ON THE DRIVING CHAIN (package = B6 split + E2 SS+1 + D7 +1)")
ES, EF, TF, T = solve(best, {"B6b": 4, "D7": ES0["D7"] + 1})
crit = sorted([k for k in best if TF[k] == 0], key=lambda k: (ES[k], k))
was = {k for k in BASE if BASE[k][4] == 0}
print(f"  completion M{T} ({ml(T)}), terminal float {26 - T}")
print(f"  zero-float activities ({len(crit)}): " + " ".join(crit))
print(f"\n  gained float : {sorted(was - set(crit))}")
print(f"  newly critical: {sorted(set(crit) - was)}")
print("\n  => the program becomes dual-critical: the pump station chain through")
print("     commissioning AND the dam chain through first fill. The sheet's line")
print("     'the dam is NOT critical' will need rewriting.")
