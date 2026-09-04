# Repository guide

## What is in here

This repository holds the reference knowledge base for the **EGB387 Engineering Economy & Planning
project assignment (2026) — Enoggera Reservoir Hydro Project**.

- `docs/egb387/` — structured extraction of every fact from the five supplied assessment documents.
  Start at `docs/egb387/00-index.md`.
- `docs/egb387/source/` — the original PDFs, kept so every extracted fact can be verified.

## Academic integrity constraint — applies to all work in this repository

The project briefing states: **"The use of artificial intelligence (GenAI) tools are prohibited for
the assessment."**

Accordingly:

- `docs/egb387/` is a **reorganised transcription of the supplied source documents only**. It
  deliberately contains **no drafted assessment content** — no scope statement, construction
  methodology, construction program, stakeholder analysis, or reflection text.
- Do not add drafted report content to this repository.
- The assessment itself must be written by the students. Part 1 requires **sign off and date by all
  group members**; Part 2 requires a **signed statement certifying it is the individual work of that
  member**.

## Working with the PDFs

`poppler-utils` is not installed. Use PyMuPDF instead:

```bash
pip3 install pymupdf
python3 -c "
import pymupdf
d = pymupdf.open('docs/egb387/source/EGB387_Project_briefing_090726.pdf')
d[7].get_pixmap(dpi=140).save('/tmp/page8.png')
"
```

**Always render the drawing pages (briefing pages 7–11) as images rather than relying on the PDF
text layer.** The text layer reorders the dimension callouts and produces wrong readings — for
example it makes the dam's 13 m base width look like a section height, and attaches RL 68.5 to the
generator instead of the dredged channel.
