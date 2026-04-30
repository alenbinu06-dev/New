# AGENTS.md

## Cursor Cloud specific instructions

### Overview

This repository contains a Python-based PDF generation script using the `reportlab` library. The main branch is a placeholder; the actual application code lives on feature branches.

### Running the application

```bash
python3 event5_vo4.py
```

This generates `Event5_VO4_Submission.pdf` in the workspace root.

### Dependencies

- Python 3.12+
- `reportlab` (installed via pip)

### Notes

- There is no test suite, linter configuration, or build system in this repository.
- The script is standalone — no services, databases, or external APIs are required.
- Output PDF files are generated in the working directory and should not be committed.
