# Week 8 – Correlation and Regression (EGH404)

Lecture and tutorial transcripts, slides and study notes for the Week 8 content. This week supports **Assignment 2, Sections 2 (correlation) and 3 (multiple linear regression)**.

- [`notes.md`](notes.md) – study notes summarising every transcript and slide deck, grouped by topic and platform.
- [`transcripts/`](transcripts/) – the raw auto-generated transcripts (unedited, so expect speech-to-text errors such as "fiddle M" for `fitlm` or "PSN" for "Pearson").
- [`slides/`](slides/) – lecture and practical slides.
- `slides/*-ocr.txt` – OCR text of the slide images (code screenshots, rubric tables and figures), because most slides are images with no extractable text.

The practicals use the Washington bike share data (`day.csv`), stored in [`../week-7/data/day.csv`](../week-7/data/day.csv), and the concrete compressive strength data from Canvas.

## Slides

| File | What it is |
|------|------------|
| [`slides/introduction-to-correlation.pdf`](slides/introduction-to-correlation.pdf) | "Introduction to Correlation" (Dr Tharindu Fernando), which goes with transcript 01 |
| [`slides/regression-simple-linear-regression.pdf`](slides/regression-simple-linear-regression.pdf) | "Regression": simple linear regression, OLS and orthogonal regression, which goes with transcript 08 |
| [`slides/week-8-practical-correlation-and-regression.pdf`](slides/week-8-practical-correlation-and-regression.pdf) | Week 8 practical slides: Pearson r, regression output, in-class activities, wrap-up, which go with transcript 14 |

## Transcripts

### Concepts (all tools)

| # | File | Topic |
|---|------|-------|
| 01 | [`01-correlation-introduction.txt`](transcripts/01-correlation-introduction.txt) | Direction and strength, Pearson r, non-linear relationships, correlation matrix, correlation vs causation |
| 02 | [`02-correlation-pitfalls-causation-and-anscombes-quartet.txt`](transcripts/02-correlation-pitfalls-causation-and-anscombes-quartet.txt) | Spurious correlations, don't correlate proportions, Anscombe's quartet |
| 03 | [`03-distributions-and-covariance.txt`](transcripts/03-distributions-and-covariance.txt) | Joint, marginal and conditional distributions; covariance |
| 08 | [`08-regression-introduction-simple-linear-and-ols.txt`](transcripts/08-regression-introduction-simple-linear-and-ols.txt) | Simple linear regression, ordinary least squares, orthogonal regression |
| 14 | [`14-week-8-live-practical-correlation-and-regression.txt`](transcripts/14-week-8-live-practical-correlation-and-regression.txt) ([`.srt`](transcripts/14-week-8-live-practical-correlation-and-regression.srt)) | Live Week 8 practical: correlation and regression explorer activities, reading regression output, Assignment 2 guidance |

### MATLAB track (Washington bike share data)

| # | File | Topic |
|---|------|-------|
| 04 | [`04-matlab-correlation-part-1-scatter-plots-and-corrcoef.txt`](transcripts/04-matlab-correlation-part-1-scatter-plots-and-corrcoef.txt) | Scatter plots of counts vs weather, `corrcoef`, registered vs casual users |
| 05 | [`05-matlab-correlation-part-2-working-days-and-correlation-matrix.txt`](transcripts/05-matlab-correlation-part-2-working-days-and-correlation-matrix.txt) | Filtering to working days, multi-variable `corrcoef` matrix |
| 09 | [`09-matlab-regression-part-1-fitlm.txt`](transcripts/09-matlab-regression-part-1-fitlm.txt) | Train/test split, `fitlm`, reading p-values, RMSE and R² |
| 10 | [`10-matlab-regression-part-2-refining-models.txt`](transcripts/10-matlab-regression-part-2-refining-models.txt) | Categorical variables, rank deficiency, removing predictors, robust and quadratic fits, test RMSE |
| 11 | [`11-matlab-regression-learner-app.txt`](transcripts/11-matlab-regression-learner-app.txt) | Regression Learner app, cross-validation vs holdout, exporting models and generating code |

### Python track (Washington bike share data)

| # | File | Topic |
|---|------|-------|
| 06 | [`06-python-correlation-practical.txt`](transcripts/06-python-correlation-practical.txt) | Scatter plots, `np.corrcoef`, correlation for feature selection |
| 12 | [`12-python-linear-regression-practical.txt`](transcripts/12-python-linear-regression-practical.txt) | `statsmodels` OLS, R² and adjusted R², p-values, categorical variables with `C()`, training on 2012 only |

### Excel track (concrete compressive strength data)

| # | File | Topic |
|---|------|-------|
| 07 | [`07-excel-correlation.txt`](transcripts/07-excel-correlation.txt) | Correlation assumptions, trend lines, Analysis ToolPak correlation matrix, conditional formatting |
| 13 | [`13-excel-regression.txt`](transcripts/13-excel-regression.txt) | Analysis ToolPak regression, reading the summary output, simplifying the model, testing on held-out data |

## Source file mapping

The uploaded files were renamed by topic. Transcripts 7 and 8 were byte-identical duplicates and are stored once. The live practical came as subtitles; the original `.srt` is kept alongside a plain-text version with the timestamps removed.

| Stored as | Original upload |
|-----------|-----------------|
| 01 | transcript 1 |
| 02 | transcript 2 |
| 03 | unnumbered transcript |
| 04 | transcript 3 |
| 05 | transcript 4 |
| 06 | transcript 5 |
| 07 | transcript 6 |
| 08 | transcripts 7 and 8 (identical) |
| 09 | transcript 9 |
| 10 | transcript 10 |
| 11 | transcript 11 |
| 12 | transcript 12 |
| 13 | transcript 13 |
| 14 | `EGH404_26Sem2_Week_8_Practical.srt` |
