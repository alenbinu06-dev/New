# Week 7 – Data Analysis: Wrangling, Statistics and Visualisation (EGH404)

Lecture and tutorial video transcripts for the Week 7 content, plus consolidated study notes.

- [`notes.md`](notes.md) – study notes summarising every transcript, grouped by topic and platform.
- [`transcripts/`](transcripts/) – the raw auto-generated transcripts (unedited, so expect speech-to-text errors such as "philtre" for "filter" or "Nan" for "NaN").
- [`slides/`](slides/) – lecture slides and the practical sheet.
- [`data/`](data/) – the dataset used in the visualisation practicals.

## Slides, practical sheet and data

| File | What it is |
|------|------------|
| [`slides/summary-stats-data-wrangling-statistics-visualisation.pdf`](slides/summary-stats-data-wrangling-statistics-visualisation.pdf) | "Data Analysis: Data Wrangling, Statistics & Visualisation" lecture slides, which go with transcript 02 |
| [`slides/introduction-to-jupyter-notebook.pdf`](slides/introduction-to-jupyter-notebook.pdf) | "Introduction to Jupyter Notebook" slides (Dr Tharindu Fernando), which go with transcript 14 |
| [`slides/practical-3-matlab-refresher.pdf`](slides/practical-3-matlab-refresher.pdf) | Practical 3 MATLAB refresher: how to install MATLAB or use MATLAB Online, and run the lecture examples |
| [`data/day.csv`](data/day.csv) | Washington bike share daily data for 2011–2012 (731 rows × 16 columns), used in transcripts 09 and 15 |

The unit lets you follow the practical work in **MATLAB, Excel or Python**; you only need one of the three tool tracks below, but the two general lectures apply to everyone.

## Transcripts

### General lectures

| # | File | Topic |
|---|------|-------|
| 01 | [`01-intro-to-data-analysis-in-engineering.txt`](transcripts/01-intro-to-data-analysis-in-engineering.txt) | Why engineers need data analysis, data types, the six-stage analysis pipeline, data collection and storage |
| 02 | [`02-data-wrangling-statistics-and-visualisation.txt`](transcripts/02-data-wrangling-statistics-and-visualisation.txt) | Data wrangling, outliers and missing data, summary statistics, histograms, skewness |

### MATLAB track (Brisbane bike counter data, then Washington bike share data)

| # | File | Topic |
|---|------|-------|
| 03 | [`03-matlab-live-script-setup.txt`](transcripts/03-matlab-live-script-setup.txt) | Setting the working directory (`cd`) in the provided live script |
| 04 | [`04-matlab-data-wrangling-part-1-loading-data.txt`](transcripts/04-matlab-data-wrangling-part-1-loading-data.txt) | Loading a CSV with `readtable`, indexing tables, file-path errors, plotting |
| 05 | [`05-matlab-data-wrangling-part-2-missing-data.txt`](transcripts/05-matlab-data-wrangling-part-2-missing-data.txt) | `NaN` values, `isnan` / `isfinite`, removing rows with missing data |
| 06 | [`06-matlab-data-wrangling-part-3-filtering-by-date.txt`](transcripts/06-matlab-data-wrangling-part-3-filtering-by-date.txt) | Filtering on `datetime` (month, `weekday`, weekday vs weekend) |
| 07 | [`07-matlab-data-wrangling-part-4-splitting-and-merging.txt`](transcripts/07-matlab-data-wrangling-part-4-splitting-and-merging.txt) | Selecting columns/rows, horizontal and vertical concatenation, `size` |
| 08 | [`08-matlab-import-tool-no-code-loading.txt`](transcripts/08-matlab-import-tool-no-code-loading.txt) | Using the MATLAB Import Tool app to load data and drop missing rows without code |
| 09 | [`09-matlab-visualising-distributions.txt`](transcripts/09-matlab-visualising-distributions.txt) | `histogram` vs `hist`, `boxplot`, outliers, subplots for comparing groups |

### Excel track (concrete compressive strength data)

| # | File | Topic |
|---|------|-------|
| 10 | [`10-excel-importing-and-missing-values.txt`](transcripts/10-excel-importing-and-missing-values.txt) | Importing CSVs, finding/counting blanks, omission vs imputation |
| 11 | [`11-excel-filtering-data.txt`](transcripts/11-excel-filtering-data.txt) | Tables, AutoFilter, number/custom filters, Advanced Filter, `FILTER` |
| 12 | [`12-excel-appending-and-merging-tables.txt`](transcripts/12-excel-appending-and-merging-tables.txt) | Power Query: appending tables and merging on a common ID |
| 13 | [`13-excel-data-visualisation.txt`](transcripts/13-excel-data-visualisation.txt) | Histograms, column charts, box and whisker plots |

### Python track (Brisbane bike counter data, then Washington bike share data)

| # | File | Topic |
|---|------|-------|
| 14 | [`14-python-jupyter-notebooks-intro.txt`](transcripts/14-python-jupyter-notebooks-intro.txt) | Using the QUT Jupyter environment, notebook cells, Markdown, exporting |
| 15 | [`15-python-preprocessing-merging-and-visualisation.txt`](transcripts/15-python-preprocessing-merging-and-visualisation.txt) | Full pandas practical: loading, missing values, dates, `concat`, correlation, `describe`, histograms, box plots |
| 16 | [`16-python-preprocessing-and-merging-shorter-take.txt`](transcripts/16-python-preprocessing-and-merging-shorter-take.txt) | Shorter recording of the same practical (loading, missing values, dates, merging only) |

## Source file mapping

The uploaded transcripts were renamed by topic. Two uploads were byte-identical duplicates and are stored once.

| Stored as | Original upload(s) |
|-----------|--------------------|
| 01 | transcript 1, unnumbered `transcript` upload (identical) |
| 02 | transcript 13 |
| 03 | transcript 7 |
| 04 | transcript 2 |
| 05 | transcript 3 |
| 06 | transcript 4 |
| 07 | transcript 5 |
| 08 | transcript 6 |
| 09 | transcript 14 |
| 10 | transcript 9 |
| 11 | transcript 10, transcript 11 (identical) |
| 12 | transcript 12 |
| 13 | transcript 16 |
| 14 | transcript 17 |
| 15 | transcript 15 |
| 16 | transcript 8 |
