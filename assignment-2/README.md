# Assignment 2 – Data Analysis (EGH404)

The datasets and working drafts for Assignment 2, which analyses Brisbane bikeway counts and weather from 2014 to 2018. For the unit's guidance on each section, see the Assignment 2 tips in [`../week-9/notes.md`](../week-9/notes.md#assignment-2-tips-practical-slides-and-07). Regression background is in [`../week-8/notes.md`](../week-8/notes.md).

- [`data/`](data/) – the four supplied CSV files (raw and cleaned).
- [`drafts/`](drafts/) – the current answer drafts, saved verbatim. Earlier versions are in [`drafts/old/`](drafts/old/).
- [`checks/verify_drafts.py`](checks/verify_drafts.py) – recomputes 47 figures quoted in the drafts from the CSV files and reports any mismatch.
- [`assessment-2-template.pdf`](assessment-2-template.pdf) – the official answer template. Answers go directly into it; keep the template wording.

## The task (from the template)

**Scenario:** Brisbane City Council (BCC) is planning bikeway upgrades. You assess cyclist and pedestrian usage of the Bicentennial Bikeway (Brisbane) and the North Brisbane Bikeway (Windsor) from 2014 to 2018, and how usage relates to rainfall, solar exposure and maximum temperature.

**General rules:**
- Use MATLAB, Python or Excel.
- Put evidence (code, or Excel formula and Data Analysis screenshots) in an appendix at the end. The code won't normally be run, but it may be used to judge your process.
- Every figure needs a title, axis labels, a legend where applicable, and units.

| Part | Data | What to produce | Points |
|------|------|-----------------|--------|
| S1.T1 (a) | Raw bikeway file | One visualisation containing box plots for the 4 series | 1 |
| S1.T1 (b) | Raw bikeway file | One line graph with 4 lines | 1 |
| S1.T1 (c) | Raw bikeway file | Table: column, problem type and value; date or range; handling; justification. Up to 3 examples per problem type per bikeway | 4 |
| S1.T2 (a) | Raw weather file | Separate box plots for rainfall, maximum temperature and solar exposure | 1 |
| S1.T2 (b) | Raw weather file | Separate line graphs for the 3 factors | 1 |
| S1.T2 (d) | Raw weather file | The same table as S1.T1 (c). The template has no part (c), and its wording says "for each bikeway", which in practice means each weather factor | 4 |
| S2.T1 | Cleaned files | r for (a) Bicentennial cyclists vs pedestrians, (b) North Brisbane cyclists vs pedestrians, (c) Bicentennial cyclists vs North Brisbane cyclists, (d) Bicentennial pedestrians vs North Brisbane cyclists | 2 |
| S2.T2 | Cleaned files | Scatter plot: North Brisbane cyclists (x) against Bicentennial pedestrians (y) | 2 |
| S2.T3 | Cleaned files | Interpretation of that pair in 400 words, using r, the plot and patterns over time | 4 |
| S3.T1, pedestrians | Cleaned files, train/test split | Multiple regression of Bicentennial **pedestrians** on the weather factors. Remove variables until all are significant. (a) Summary table with p-values, R², adjusted R², and RMSE on train and test. (b) A scatter plot for each independent variable against the dependent variable, with the fitted line. (c) Discussion of simplification and its effect | 3 |
| S3.T1, cyclists | Cleaned files, train/test split | The same for Bicentennial **cyclists** | 3 |
| S3.T2 | Both models | Interpretation in 400 words. (a) Predicted vs actual plot on the test set, and predictive power. (b) Suitability, using coefficients, R², adjusted R², RMSE and p-values. (c) Reasons for any gap between training and test performance, supported by plots | 5 |
| S4 (choose **one** of TA or TB) | Your Assignment 1 topic | **TA:** a public tabular dataset with at least 100 rows, at least 5 columns (3 or more quantitative), a source link and a licence or terms of use, broadly related to your topic. **TB:** a synthetic dataset with 3–5 variables (up to 4 independent, 1 dependent) and at least 200 rows, plus a table giving min, max, units, distribution and assumed relationships. Both need a justification of about 150–250 words and a description table. The same dataset is used in the Assessment 3 pitch | 4 |
| S5.T1 | The Section 4 dataset | (a) Scatter plots and a correlation matrix for related variables. (b) The nature of each relationship (linear, inverse, nonlinear or none), with evidence. (c) A comparison with the literature | 5 |
| **Total** | | | **40** |

**Section 3 split (confirmed by the template):**
- Training is 1 Jan 2014 – 31 Dec 2017, inclusive, and testing is everything after.
- The cleaned file starts on 19 Jun 2014, which gives **1,145 training days** (19 Jun 2014 – 31 Dec 2017) and **316 test days** (2018).

**Two template quirks to handle explicitly in your answers:**
- **S2.T3** refers to "the correlation coefficient calculated in 2.1(a)", but the pair it asks about (North Brisbane cyclists vs Bicentennial pedestrians) is row **(d)**. The S2 draft already handles this by stating which row it uses and also discussing row (a).
- **S1.T2 (d)** copies the bikeway wording ("for each bikeway"). Reading it as "for each weather factor", as the draft does, is sensible.

## Sections 4–5: options for the Assignment 1 topic

The topic is CO2 curing of recycled concrete aggregate, and whether a co-treatment agent adds anything beyond controlled carbonation. See [`../assignment-1/README.md`](../assignment-1/README.md).

A web search (30 Sep 2026) found no public dataset that varies CO2 curing and agent dose together, which is the gap Assignment 1 identifies. The candidates below come from the search results and **haven't been downloaded or checked yet**. Before choosing one, confirm its columns, row count and licence.

| Candidate | What it is | Fit to the template |
|---|---|---|
| [IIT Bhubaneswar RCA dataset (Mendeley, DOI 10.17632/5wkxzmzwnz.2)](https://data.mendeley.com/datasets/5wkxzmzwnz/2) | 188 lab mixes of recycled-aggregate concrete; water/binder 0.25–0.75; fly ash, GGBS and metakaolin additions; cube compressive strength | ≥100 rows; CC BY 4.0. It is RAC, not CO2-treated, so it serves as a broad proxy (mix and aggregate quality vs strength) |
| [RAC data-driven database (Mendeley, DOI 10.17632/wc898ff5pj.1)](https://data.mendeley.com/datasets/wc898ff5pj/1) | Includes 956 RAC mix-proportion entries with compressive strength, compiled from the literature | ≥100 rows; licence not shown in the search result |
| [Carbonated recycled fines (RefoDat)](https://refodat.de/receive/refodat_mods_00000077) | Wet carbonation of recycled fines, with CSV concrete test data | Directly on topic, but likely far fewer than 100 rows |
| Gebremariam et al. (2026), *Scientific Reports* | 108 samples of carbonated RCA concrete: w/c, water absorption, CO2 stored, replacement % | Very close to the topic, but the data is only "available from the corresponding author", so it fails the public-access requirement |

- **Pathway A (a real dataset):** the practical's preferred route. Use a RAC dataset as a proxy and argue that water absorption and mix quality are exactly what CO2 curing targets.
- **Pathway B (synthetic data):** the variables could match the research question exactly. For example:
  - independent variables: CO2 concentration, curing pressure or time, agent dose, RCA replacement %;
  - dependent variable: 28-day compressive strength;
  - ranges taken from the Assignment 1 literature table.

  The practical warns that synthetic data won't show real between-variable relationships unless you specify them.

## Data

| File | Rows | Dates | Columns | Use in |
|------|------|-------|---------|--------|
| [`data/brisbane_bikeway_counters.csv`](data/brisbane_bikeway_counters.csv) | 1,826 | 1 Jan 2014 – 31 Dec 2018, every day | `Date`, Bicentennial Bikeway pedestrians and cyclists, North Brisbane Bikeway pedestrians and cyclists (daily counts; blanks are missing) | Section 1 (raw) |
| [`data/brisbane_weather.csv`](data/brisbane_weather.csv) | 1,826 | 1 Jan 2014 – 31 Dec 2018, every day | `Date`, `daily_rainfall` (mm), `solar_exposure` (MJ/m²), `maximum_temperature` (°C) | Section 1 (raw) |
| [`data/brisbane_bikeway_counters_cleaned.csv`](data/brisbane_bikeway_counters_cleaned.csv) | 1,461 | 19 Jun 2014 – 31 Dec 2018, 196 days removed | Same as the raw bikeway file, with no blanks | Sections 2 and 3 |
| [`data/brisbane_weather_cleaned.csv`](data/brisbane_weather_cleaned.csv) | 1,461 | The same 1,461 dates as the cleaned bikeway file | Same as the raw weather file, with no blanks | Sections 2 and 3 |

Notes on the data:
- The Week 9 practical says to use the **raw** files for Section 1 and the **supplied cleaned** files for Sections 2 and 3. Don't use your own cleaned versions for Sections 2 and 3.
- **The cleaned files drop whole days, so dates don't match row positions.** Row 0 is 19 Jun 2014, and later dates shift wherever days were removed. Row ranges written for the raw file (for example `iloc[0:365]` for 2014) are wrong on the cleaned file. The S2 draft already uses positions that suit the cleaned file.
- **Some faults are still in the cleaned bikeway file.** It keeps 72 days of zero Bicentennial pedestrians (Dec 2014 – Jan 2015 and Mar – Apr 2017) and 40 days of zero North Brisbane cyclists (Jun 2014, Feb – Mar 2017, Jul 2018). Section 1 identifies all of these as counter faults, and the S2 interpretation discusses them.
- **Section 3 train/test split:** training is 1 January 2014 – 31 December 2017 and testing is 2018, as confirmed by the template. Because the cleaned file starts on 19 Jun 2014, training effectively covers 19 Jun 2014 – 31 Dec 2017.
- **File names:** the draft code loads `brisbane_bikeway_counters (1).csv`, the original download name. The copies here are renamed without " (1)", so change the file name in `pd.read_csv` if you run the code from this folder.

## Drafts

| File | Covers | Status |
|------|--------|--------|
| [`drafts/s1t1-bikeway-data-inspection.md`](drafts/s1t1-bikeway-data-inspection.md) | S1.T1 (a) box plot, (b) line graph, (c) problematic-data tables, plus appendix code (Boxes 1–15) | Complete |
| [`drafts/s1t2-weather-data-inspection.md`](drafts/s1t2-weather-data-inspection.md) | S1.T2 (a) box plots, (b) line graphs, (d) problematic-data tables, plus references | Text complete; **no appendix code** in this file |
| [`drafts/s2-correlation-revisions.md`](drafts/s2-correlation-revisions.md) | Replacement S2 Boxes 6–8, the Figure 7 caption and the S2.T3 interpretation (392 words) | A revision, not the full section: Boxes 1–5, Box 9 and the S2.T1 table are not included |
| [`drafts/old/`](drafts/old/) | Earlier versions of S1.T1 (two) and S1.T2 (one) | Superseded |

The earlier drafts differ from the current ones mainly in wording. For example, the current S1.T1 says "leave as missing" where the old one said "remove these days". The current version also adds:
- the 19–28 Jun 2014 North Brisbane zeros;
- the 30 Jun 2018 partial day (34 cyclists);
- a paragraph explaining that the 58 IQR-flagged North Brisbane pedestrian days belong to the 2017 and 2018 fault periods.

Sections 3 (regression), 4 (preliminary data) and 5 (correlation on preliminary data) have no drafts here yet.

## Check of the drafts against the data

I ran [`checks/verify_drafts.py`](checks/verify_drafts.py) and reviewed the drafts line by line. **All 47 automated checks pass**, and so do the other figures I checked by hand. Every `df.iloc[a:b]` row range in the S1.T1 and S2 appendix code covers exactly the dates its label claims.

**Section 1, bikeways (S1.T1):**
- Missing-day counts are correct: 95 Bicentennial and 170 North Brisbane.
- The IQR bounds are correct: 1,867, 3,814.5, 244.5 and 346.
- Every outlier value is correct, and so is every weekday.
- The multiples-of-128 fault is confirmed: all 17 days from 20 Jan to 5 Feb 2015 are exact multiples.
- The before/after means (1,711/654 and 593/1,582) and the fault-period medians and counts are correct.

**Section 1, weather (S1.T2):**
- Missing-day counts are correct: 39 rainfall, 24 maximum temperature, 1 solar exposure.
- The claim that 15 of 22 temperature gaps are followed by a rainfall gap the next day is correct.
- The IQR bounds and flag counts are correct: 1,161 dry days and 338 days above 1.5 mm.
- Every quoted neighbouring reading is correct.

**Section 2 (S2):**
- The overall and subgroup correlation coefficients are correct: r = −0.028, 0.469 and 0.216.
- The yearly r values (0.109–0.382), the means (1,440 → 648 and 91 → 144), row (a)'s r = −0.355 (Bicentennial pedestrians vs cyclists), and the 72 and 40 zero days are all correct.

**Suggested fixes** (small; nothing changes a conclusion):

1. **Add the S1.T2 appendix code.** The weather text cites Boxes 7, 9, 11–13 and 15–21, but the file contains no code. The practical requires supporting evidence in the appendix.
2. **S1.T2 Errors row for rainfall:** it says the readings after each gap are "only 0.0–0.2 mm". The 1–2 Mar 2018 gap, which the Missing-data row mentions, is followed by **0.8 mm on 3 Mar**. Either add that date or change the wording to "0.0–0.8 mm". The point still stands.
3. **S1.T1 "220 flagged days" paragraph:** 18 of the 220 fall inside the 2 Dec 2014 – 6 Feb 2015 pedestrian fault (the multiples of 128 plus 5,452 on 6 Feb), and one more is 21 Mar 2015. Those days are handled individually, so it would be more precise to say they are excluded from the "older level" explanation. "Most" is still true: about 200 of the 220 are ordinary pre-June 2015 days.
4. **S1.T1 (a) layout:** the template asks for "a SINGLE visualisation" containing the four box plots. The draft uses one figure with a 2×2 grid, each panel on its own scale. That is defensible, because Bicentennial counts are about ten times North Brisbane's. If you want to follow the wording literally, put all four boxes on one axis as well, but they would be hard to read.
5. **Check against the Week 9 tips.** The drafts already meet all of these:
   - At most three examples per problem type per bikeway: Bicentennial has 3 missing-data rows, 3 outliers and 3 errors; North Brisbane has 2, 3 and 3.
   - Specific dates and a justification for every row.
   - Outliers not removed automatically.
   - Plot code sets titles, axis labels and a legend.
   - The S2 interpretation is under 400 words and covers clusters, explanations and what r implies.
