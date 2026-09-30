# Assignment 2 – Data Analysis (EGH404)

The datasets and working drafts for Assignment 2, which analyses Brisbane bikeway counts and weather from 2014 to 2018. For the unit's guidance on each section, see the Assignment 2 tips in [`../week-9/notes.md`](../week-9/notes.md#assignment-2-tips-practical-slides-and-07). Regression background is in [`../week-8/notes.md`](../week-8/notes.md).

- [`data/`](data/) – the four supplied CSV files (raw and cleaned).
- [`drafts/`](drafts/) – the current answer drafts, saved verbatim. Earlier versions are in [`drafts/old/`](drafts/old/).
- [`checks/verify_drafts.py`](checks/verify_drafts.py) – recomputes 47 figures quoted in the drafts from the CSV files and reports any mismatch.

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
- **Section 3 train/test split:** the data runs from 2014 to 2018. The Week 9 recording's "January 1, 2024 to December 31, 2017" is therefore almost certainly **1 January 2014 – 31 December 2017 (train)** and **2018 (test)**. Because the cleaned file starts on 19 Jun 2014, training effectively covers 19 Jun 2014 – 31 Dec 2017. Confirm the dates on the assignment page.
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
2. **Check the S1.T2 part letters.** The draft goes from (b) to (d). Either part (c) is missing, or the labelling should be checked against the template.
3. **S1.T2 Errors row for rainfall:** it says the readings after each gap are "only 0.0–0.2 mm". The 1–2 Mar 2018 gap, which the Missing-data row mentions, is followed by **0.8 mm on 3 Mar**. Either add that date or change the wording to "0.0–0.8 mm". The point still stands.
4. **S1.T1 "220 flagged days" paragraph:** 18 of the 220 fall inside the 2 Dec 2014 – 6 Feb 2015 pedestrian fault (the multiples of 128 plus 5,452 on 6 Feb), and one more is 21 Mar 2015. Those days are handled individually, so it would be more precise to say they are excluded from the "older level" explanation. "Most" is still true: about 200 of the 220 are ordinary pre-June 2015 days.
5. **Check against the Week 9 tips.** The drafts already meet all of these:
   - At most three examples per problem type per bikeway: Bicentennial has 3 missing-data rows, 3 outliers and 3 errors; North Brisbane has 2, 3 and 3.
   - Specific dates and a justification for every row.
   - Outliers not removed automatically.
   - Plot code sets titles, axis labels and a legend.
   - The S2 interpretation is under 400 words and covers clusters, explanations and what r implies.
