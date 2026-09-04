#!/usr/bin/env python3
"""Verify that every key figure in docs/egb387/ traces back to the source PDFs.

Each check names a fact, the source PDF token(s) that must be present in that
PDF's text layer, and the knowledge-base file(s) that must quote the value.

Run: python3 scripts/verify_extraction.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "docs" / "egb387" / "source"
KB = ROOT / "docs" / "egb387"

BRIEFING = "EGB387_Project_briefing_090726.pdf"
GUIDE_GROUP = "EGB387_Project_-_Guide_to_group_component.pdf"
GUIDE_IND = "EGB387_Project-_Guide_to_individual_component.pdf"
CRA_GROUP = "EGB387_Project_CRA-_Group_component.pdf"
CRA_IND = "EGB387_Project_CRA-_Individual_component.pdf"

# (description, source pdf, tokens required in that pdf, kb file, tokens required in kb)
CHECKS: list[tuple[str, str, list[str], str, list[str]]] = [
    # --- Assessment particulars -------------------------------------------------
    ("Weighting is 25%", BRIEFING, ["25%"], "00-index.md", ["25% of the unit"]),
    ("Group 15% / individual 10%", BRIEFING, ["Group (15%)", "individually (10%)"],
     "06-deliverables-and-report-structure.md", ["Group 15%", "Individual 10%"]),
    ("Due 11 September 23:59", BRIEFING, ["11th September at 23.59"],
     "06-deliverables-and-report-structure.md", ["11 September 2026, 23:59"]),
    ("Word format via Canvas", BRIEFING, ["word format", "via Canvas"],
     "06-deliverables-and-report-structure.md", ["Word format", "via Canvas"]),
    ("Group of 4 or 5, by week 2", BRIEFING, ["group of 4 or 5", "week 2"],
     "06-deliverables-and-report-structure.md", ["4 or 5", "week 2"]),
    ("7 week work period", BRIEFING, ["period of 7 weeks"],
     "06-deliverables-and-report-structure.md", ["7 weeks"]),
    ("Group report max 12 pages", GUIDE_GROUP, ["maximum 12 pages"],
     "06-deliverables-and-report-structure.md", ["12 pages"]),
    ("Preamble about 300 words", GUIDE_GROUP, ["300 words"],
     "06-deliverables-and-report-structure.md", ["300 words"]),
    ("Individual report 2-3 pages", GUIDE_IND, ["2-3 pages"],
     "06-deliverables-and-report-structure.md", ["2–3 pages"]),
    ("Sketches mandatory or rejected", BRIEFING, ["deemed incomplete", "rejected"],
     "06-deliverables-and-report-structure.md", ["deemed incomplete", "rejected"]),
    ("GenAI prohibited", BRIEFING, ["GenAI) tools are prohibited"],
     "08-conflicts-gaps-and-checklist.md", ["GenAI) tools are prohibited"]),

    # --- Timing -----------------------------------------------------------------
    ("Award end of March 2027", BRIEFING, ["end of March, 2027"],
     "02-timing-and-working-constraints.md", ["End of March 2027"]),
    ("Completion 31 May 2029", BRIEFING, ["May, 2029"],
     "02-timing-and-working-constraints.md", ["31 May 2029"]),
    ("10 hours per day", BRIEFING, ["10 hours per day"],
     "02-timing-and-working-constraints.md", ["10 hours per day"]),
    ("No noise after 6pm", BRIEFING, ["6.00pm"],
     "02-timing-and-working-constraints.md", ["6:00 pm"]),
    ("Six day week", BRIEFING, ["six days per week"],
     "02-timing-and-working-constraints.md", ["six days per week"]),
    ("Environmental approvals secured", BRIEFING, ["environmental approvals have been secured"],
     "02-timing-and-working-constraints.md", ["secured"]),

    # --- Personnel --------------------------------------------------------------
    ("PM free November 2026", BRIEFING, ["November 2026"],
     "03-company-personnel-and-capacity.md", ["November 2026"]),
    ("Only 1 of 2 project engineers", BRIEFING, ["only 1 available October 2026"],
     "03-company-personnel-and-capacity.md", ["Only 1 available October 2026"]),
    ("Earthworks foreman end January 2027", BRIEFING, ["end January 2027"],
     "03-company-personnel-and-capacity.md", ["end January 2027"]),
    ("Concreting foreman end October 2026", BRIEFING, ["end October 2026"],
     "03-company-personnel-and-capacity.md", ["end October 2026"]),
    ("Company at Sumner Park", BRIEFING, ["Sumner Park"],
     "03-company-personnel-and-capacity.md", ["Sumner Park"]),
    ("Subcontract limited to building trades and curtain grouting", BRIEFING,
     ["curtain grouting"], "03-company-personnel-and-capacity.md", ["curtain grouting"]),

    # --- Plant and materials ----------------------------------------------------
    ("Two CAT D8 dozers with rippers", BRIEFING, ["Caterpillar D8"],
     "04-plant-and-materials-registers.md", ["Caterpillar D8"]),
    ("Mobile cranes 16t @ 20m", BRIEFING, ["Capacity 16t @ 20m"],
     "04-plant-and-materials-registers.md", ["16 t @ 20 m"]),
    ("Pile frame extends to 30m in 4m increments", BRIEFING, ["Extends to 30m in 4m increments"],
     "04-plant-and-materials-registers.md", ["extends to 30 m in 4 m increments"]),
    ("Two dumb barges 13m x 6m x 1.5", BRIEFING, ["13m x 6m x 1.5"],
     "04-plant-and-materials-registers.md", ["13 m × 6 m × 1.5"]),
    ("Three workboats 50hp", BRIEFING, ["50 hp outboard"],
     "04-plant-and-materials-registers.md", ["50 hp outboard"]),
    ("Salvaged UB 610x230 125kg/m 330m from Gladstone", BRIEFING,
     ["610 x 230 UB 125kg/m 330 M", "Gladstone"],
     "04-plant-and-materials-registers.md", ["610 × 230 UB", "330 m", "Gladstone"]),
    ("Sheet piling 1900m from Emerald", BRIEFING, ["1900 m random", "Emerald"],
     "04-plant-and-materials-registers.md", ["1900 m random lengths", "Emerald"]),
    ("Salvaged tube 400 dia x 10mm, 100m", BRIEFING, ["400 dia x 10mm wall, 100 M"],
     "04-plant-and-materials-registers.md", ["400 dia × 10 mm wall, 100 m"]),
    ("Pile helmet 30 day lead", BRIEFING, ["Suit 400dia steel tube piles"],
     "04-plant-and-materials-registers.md", ["30 days"]),
    ("Hired batch plant 5m3, 30 days, Gladstone", BRIEFING, ["5m3 complete with all ancillary"],
     "04-plant-and-materials-registers.md", ["5 m³, complete with all ancillary equipment"]),
    ("Hired 150t Hitachi tracked crane", BRIEFING, ["150t Hitachi"],
     "04-plant-and-materials-registers.md", ["150 t Hitachi"]),
    ("Lifting gear 40 day lead", BRIEFING, ["Misc purpose made slings"],
     "04-plant-and-materials-registers.md", ["40 days"]),

    # --- Technical data ---------------------------------------------------------
    ("Crest length 250 m", BRIEFING, ["250 crest length"],
     "05-technical-data-drawings.md", ["250 m"]),
    ("Top of dam RL 102", BRIEFING, ["RL 102 top dam"],
     "05-technical-data-drawings.md", ["RL 102"]),
    ("Top water level RL 100", BRIEFING, ["RL 100 top water level"],
     "05-technical-data-drawings.md", ["RL 100"]),
    ("Lowest operating water level RL 95", BRIEFING, ["RL 95 lowest operating water level"],
     "05-technical-data-drawings.md", ["RL 95"]),
    ("Inlet invert RL 70", BRIEFING, ["Inlet invert RL 70"],
     "05-technical-data-drawings.md", ["Inlet invert RL 70"]),
    ("Outlet invert RL 92", BRIEFING, ["Outlet invert RL 92"],
     "05-technical-data-drawings.md", ["Outlet invert RL 92"]),
    ("Max head 30 m", BRIEFING, ["Max. Head 30 m"],
     "05-technical-data-drawings.md", ["30 m"]),
    ("Founding level RL 86 follows contours", BRIEFING, ["RL 86 (follows contours)"],
     "05-technical-data-drawings.md", ["RL 86 (follows contours)"]),
    ("Penstock 1.5 m dia", BRIEFING, ["1.5 m dia"],
     "05-technical-data-drawings.md", ["1.5 m dia"]),
    ("Emergency discharge 2.0 m dia", BRIEFING, ["2.0m dia"],
     "05-technical-data-drawings.md", ["2.0 m dia"]),
    ("Cut off wall 1 M", BRIEFING, ["Conc. cut off wall"],
     "05-technical-data-drawings.md", ["1 m**, a central wall"]),
    ("Foundation typically 3 m", BRIEFING, ["Typically 3 m"],
     "05-technical-data-drawings.md", ['"Typically 3 m"']),
    ("Pump station average water level RL 75.0", BRIEFING, ["Average water level RL 75.0"],
     "05-technical-data-drawings.md", ["RL 75.0"]),
    ("Pump station invert RL 70.0", BRIEFING, ["Invert RL 70.0"],
     "05-technical-data-drawings.md", ["RL 70.0"]),
    ("Pump station base RL 67.0", BRIEFING, ["RL 67.0"],
     "05-technical-data-drawings.md", ["RL 67.0"]),
    ("Dredged channel RL 68.5", BRIEFING, ["RL 68.5"],
     "05-technical-data-drawings.md", ["RL 68.5"]),
    ("Pump station top RL 83.0", BRIEFING, ["RL 83.0"],
     "05-technical-data-drawings.md", ["RL 83.0"]),
    ("Steel tube piles at pump station", BRIEFING, ["Steel tube piles"],
     "05-technical-data-drawings.md", ["steel tube piles"]),
    ("Strata: weathered granite with clay seams", BRIEFING, ["WEATHERED GRANITE (some clay seams)"],
     "05-technical-data-drawings.md", ["Weathered granite (some clay seams)"]),
    ("Strata: unweathered granite with fracturing", BRIEFING,
     ["UNWEATHERED GRANITE (some fracturing)"],
     "05-technical-data-drawings.md", ["Unweathered granite (some fracturing)"]),

    # --- Marking criteria -------------------------------------------------------
    ("Zero mark rule", CRA_GROUP, ["the Mark will be ZERO"],
     "07-marking-criteria.md", ["the Mark will be ZERO"]),
    ("Group criterion 4 is stakeholders / aboriginal groups", CRA_GROUP,
     ["Stakeholders including", "aboriginal groups"],
     "07-marking-criteria.md", ["Stakeholders including Aboriginal groups"]),
    ("Group criterion 3 mentions formwork", CRA_GROUP, ["including formwork"],
     "07-marking-criteria.md", ["including formwork"]),
    ("Individual criteria are exploration/selection and mechanics/review", CRA_IND,
     ["Initial exploration", "Mechanics of selection"],
     "07-marking-criteria.md", ["Initial exploration & selection process",
                                "Mechanics of selection and review process"]),

    # --- Guides -----------------------------------------------------------------
    ("Group guide says select one method to present", GUIDE_GROUP, ["select one to present"],
     "08-conflicts-gaps-and-checklist.md", ["select one to present"]),
    ("Briefing says four areas of construction", BRIEFING, ["the four areas of construction"],
     "08-conflicts-gaps-and-checklist.md", ["the four areas of construction"]),
    ("Group guide requires sign off by all students", GUIDE_GROUP, ["Sign off and date"],
     "06-deliverables-and-report-structure.md", ["Sign off and date"]),
    ("Individual guide review process prompts", GUIDE_IND, ["Review process"],
     "06-deliverables-and-report-structure.md", ["Review process"]),
]

# Group CRA mark weightings, checked as a set against the rubric text.
CRA_MARKS = {"25": "scope statement / value proposition / methodology",
             "15": "preliminary construction program",
             "30": "construction methods AND stakeholders"}


def normalise(text: str) -> str:
    """Collapse whitespace and unify dash/quote variants so token matching is stable."""
    text = text.replace("\u2013", "-").replace("\u2014", "-").replace("\u00a0", " ")
    text = text.replace("\u2018", "'").replace("\u2019", "'")
    text = text.replace("\u201c", '"').replace("\u201d", '"')
    text = text.replace("\u00d7", "x").replace("\u00b3", "3")
    return re.sub(r"\s+", " ", text)


def load_pdf_text(name: str) -> str:
    with pymupdf.open(SOURCE / name) as doc:
        return normalise(" ".join(page.get_text() for page in doc))


def main() -> int:
    pdf_text = {name: load_pdf_text(name) for name in
                (BRIEFING, GUIDE_GROUP, GUIDE_IND, CRA_GROUP, CRA_IND)}
    kb_text = {p.name: normalise(p.read_text()) for p in KB.glob("*.md")}

    passed = failed = 0
    width = max(len(desc) for desc, *_ in CHECKS) + 2

    print("=" * 100)
    print("EGB387 knowledge base — source traceability verification")
    print("=" * 100)
    print(f"Source PDFs : {len(pdf_text)}")
    print(f"KB files    : {len(kb_text)}")
    print(f"Checks      : {len(CHECKS) + 1}")
    print("-" * 100)

    for desc, pdf, pdf_tokens, kb_file, kb_tokens in CHECKS:
        problems = []
        haystack = pdf_text[pdf]
        for token in pdf_tokens:
            if normalise(token) not in haystack:
                problems.append(f"not in {pdf}: {token!r}")
        if kb_file not in kb_text:
            problems.append(f"missing KB file {kb_file}")
        else:
            for token in kb_tokens:
                if normalise(token) not in kb_text[kb_file]:
                    problems.append(f"not in {kb_file}: {token!r}")

        if problems:
            failed += 1
            print(f"FAIL  {desc.ljust(width)}")
            for problem in problems:
                print(f"        -> {problem}")
        else:
            passed += 1
            print(f"pass  {desc.ljust(width)} [{pdf} -> {kb_file}]")

    # Mark weightings: confirm each value appears in both the rubric and the KB table.
    marks_ok = all(m in pdf_text[CRA_GROUP] and f"| **{m}** |" in kb_text["07-marking-criteria.md"]
                   for m in CRA_MARKS)
    total_ok = "| **100** |" in kb_text["07-marking-criteria.md"]
    if marks_ok and total_ok:
        passed += 1
        print(f"pass  {'Group CRA mark weightings 25/15/30/30 = 100'.ljust(width)} "
              f"[{CRA_GROUP} -> 07-marking-criteria.md]")
    else:
        failed += 1
        print("FAIL  Group CRA mark weightings 25/15/30/30 = 100")

    print("-" * 100)
    print(f"RESULT: {passed} passed, {failed} failed")
    print("=" * 100)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
