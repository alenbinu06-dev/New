# Week 7 Study Notes – Data Analysis: Wrangling, Statistics and Visualisation

These notes summarise the Week 7 transcripts in [`transcripts/`](transcripts/), the lecture slides in [`slides/`](slides/) and the practical dataset in [`data/`](data/). Transcript numbers in brackets, such as (05), point to the matching file. Code snippets are cleaned-up versions of what the presenters typed; check them against the provided live scripts or notebooks.

---

## 1. Introduction to data analysis in engineering (01)

### Why engineers need data analysis
- **Civil engineering case (Sarah):** site sensors (temperature, humidity, material stress, worker productivity) fed a predictive model that forecast storm delays and found over-used materials, leading to cost savings.
- **Mechanical engineering case (Alex):** machine temperature, pressure and vibration data revealed that small temperature variations during critical production phases caused defects. Vibration patterns also enabled **predictive maintenance**.
- About 2.5 quintillion bytes of data were generated per day in 2021, roughly a billion two-hour HD movies.
- Data analysis means inspecting, transforming and modelling data to uncover useful information, draw conclusions and support decisions.

### Types of data
- **Quantitative** (numerical): discrete (countable) or continuous.
- **Qualitative** (categorical, non-numerical): for example gender or colour.
- **Structured** (organised and searchable, like a movie database) vs **unstructured** (text, multimedia).
- **Spatial** (tied to a location, like satellite or drone images) vs **temporal** (sequences over time, like daily stock prices or hourly weather).
- **Metadata**: data about data, such as the authors and submission dates of a paper.
- The data type determines which analysis methods are valid.

### The six-stage data analysis pipeline
1. **Define the research question and objectives**: the problem, scope, key metrics and outcomes (links to Week 3).
2. **Data collection**: experiments, sensors, surveys or historical data. The data must be accurate, complete and representative.
3. **Data cleaning and preprocessing**: handle missing data, remove outliers or erroneous points, normalise or scale (essential for machine learning), and convert data to a usable format (for example images to numbers).
4. **Exploratory data analysis (EDA)**: histograms, scatter plots and box plots to see distributions, relationships, trends and anomalies, plus descriptive statistics (mean, median, standard deviation).
5. **Data modelling and analysis**: choose a method suited to the data and question (for example correlation, regression or machine learning), then build, train and validate the model. Simulation or optimisation can also be used.
6. **Interpretation and communication**: interpret the results against the research question, assess validity and reliability, and report clearly to stakeholders.

### Data collection methods
- **Experimental:** laboratory experiments (controlled) or field experiments (real environments).
- **Sensor and instrumentation data:** specialised sensors and IoT devices.
- **Surveys and questionnaires:** describe characteristics of large populations.
- **Simulation:** computer or mathematical simulation (for example finite element analysis) when real collection is too risky.
- **Historical data:** other studies, public data (weather, infrastructure), internal records, ERP systems.

### Data quality: four things to ensure
- **Accuracy:** values represent the true values.
- **Consistency:** the same methods and tools are used throughout.
- **Calibration:** instruments and sensors are calibrated regularly.
- **Documentation:** keep detailed records of methods, conditions and anomalies. Students most often skip this.

### Data storage
- Choose storage to suit the data (relational database, cloud storage, data warehouse), considering its **volume, variety and velocity**.
- **Security:** access levels, encryption, access controls, secure backups.
- **Integrity:** checksums, versioning and validation.
- **Organisation:** logical structures (tables, indexes, file systems) and consistent file naming.
- **Scalability:** plan for growing volume and complexity.
- **Policies:** document retention schedules, backup procedures and access control, and make sure all users know them.

---

## 2. Data wrangling, summary statistics and visualisation (02)

### Data wrangling
- Data wrangling is the process of cleaning, transforming and preparing raw data for analysis. It includes handling missing data, transforming data and integrating multiple sources.
- It takes a large share of analysis time because real-world data is messy. Plan data collection carefully to reduce errors.
- **There is no one-size-fits-all strategy.** Decide case by case, test different cleaning approaches and check their effect on data quality and on the goal of the analysis.
  - Duplicates can usually be removed.
  - Missing data can sometimes be removed (the slides suggest removing is usually acceptable if under 5% of the data is affected), imputed with the mean, median or mode, set to a default value, or predicted with a model such as regression.
  - Sanity checks from the slides: does the data make sense? Does it follow the rules of its field? What have published papers in your field done, and why?
  - Outliers may distort results, but sometimes they are exactly what you are studying (for example irregular heart rhythms for a medical device), so don't filter them blindly.

### Detecting outliers
- **Histograms:** points far from the main distribution stand out.
- **Box plots (box and whisker):** show the five-number summary: minimum, Q1, median, Q3 and maximum.
  - **Interquartile range (IQR) = Q3 − Q1**, the spread of the middle 50% of the data. It is robust to extreme values.
- **Z-scores:** the number of standard deviations a point lies from the mean.
  - A z-score near 0 means the point is close to the mean. z > 1 means more than one standard deviation above; z < −1 means more than one below.
  - Small samples can mislead: with 10 or fewer observations, no z-score can exceed ±3.

### Detecting missing data
- For small datasets, plot or inspect the data manually.
- For large datasets, use code or formulas, for example a heat map of missing values.

### Summary (descriptive) statistics
- **Distribution shape:** histograms and box plots.
- **Central tendency:** mean, median and mode.
- **Dispersion:** range, IQR, variance and standard deviation.
- **Symmetry:** skewness.

### Histograms
- Show the frequency of values within equal-width **bins** (class intervals). Bins are on the x-axis and frequency on the y-axis.
- Bin tips:
  - Use equal bin sizes.
  - Include all data, including outliers.
  - Use roughly 5 to 20 bins; larger datasets usually need more.
  - The final choice is a judgement call.
- Histograms reveal central tendency, spread (wide means high variability), symmetry or skew, and whether the data is **bimodal or multimodal**. They are also useful for comparing distributions.
- **Normal distribution (bell curve):** mean, median and mode are equal, and most data clusters around the centre.

### Skewness
- **Positive (right) skew:** the right tail is longer, so the mean is pulled above the median.
- **Negative (left) skew:** the left tail is longer, so the mean is pulled below the median.
- In skewed data, the **median is the more robust measure of central tendency**. The mode sits near the peak but can still be influenced by the skew.
- **Example (material strength testing):** 30 strength tests, mostly between 23 and 29, with one extreme value of 800. The values sum to 1551, so the **mean is 1551 / 30 ≈ 51.17**, while the **median is 26**. The skewed mean makes the material look about twice as strong as it really is, which matters for the safety and reliability of a building design. (The transcript's figure of "701.36" is a transcription error; the slide gives 51.17.)
- Mitigation:
  - Find and fix sources of skew during data collection.
  - Apply transformations.
  - Use robust statistics such as the median.
  - Run sensitivity analysis.
  - Always tell stakeholders that skew is present and how it may affect the results.
- Other visualisations include the **Q–Q (quantile–quantile) plot** against a normal distribution.
- The slides list the goals of data wrangling as handling missing values, removing duplicates, integrating or merging data, filtering, grouping, reshaping and transforming. They also cite a Forbes survey: data preparation is about 80% of a data scientist's work, and about 60% of that time goes on cleaning and organising data.
- Descriptive statistics also include **kurtosis** (how heavy the tails are) alongside skewness.
- Beyond histograms and box plots, try density plots and violin plots (see data-to-viz.com).
- **Rule of thumb:** visualise first, then decide what to do with outliers and missing values. Summary statistics alone can hide important features.

---

## 3. MATLAB track

The first datasets are the Brisbane City Council bike and pedestrian counter data (`bike-ped-auto-counts-2016.csv`, 366 daily rows × 91 columns) and Bureau of Meteorology weather data for 2016. Transcript 09 switches to the Washington bike share data.

### Live script setup (03)
- Live scripts run in your MATLAB home directory by default. Change the first line, `cd('...')`, to the folder where you unzipped the script and data, or you will get "file not found" errors.
- The script deliberately includes some errors (such as failed loads) for illustration. You can skip past them.

### Part 1: Loading data (04)
```matlab
data = readtable('bike-ped-auto-counts-2016.csv');   % Tab key autocompletes file names
data(1:20, 1:20)                                     % first 20 rows and columns (returns a table)
data.BicentennialBikeway(1:20)                       % dot + Tab lists columns
plot(data.BicentennialBikeway); hold on; plot(data.SomeOtherColumn)
```
- The warning "Variable names were modified to make them valid MATLAB identifiers" is harmless. It appears here because the time column has no header, so it becomes `Var2`.
- `readtable` produces a **table** and infers the column types (datetime, string, numeric).
- The error "Unable to open file" usually means you are in the wrong directory. Use a relative path or the **full absolute path**.
- Use `help readtable` or the documentation for options. There are many ways to do the same thing in MATLAB.

### Part 2: Missing data (05)
- Empty cells are read in as `NaN` (Not a Number). Any arithmetic involving `NaN` returns `NaN`, so `mean` and `sum` fail.
- `nanmean` ignores NaNs, but NaN-aware variants are inconsistent across functions, so it is simpler to remove them.
- `isnan(x)` returns true where a value is NaN. `isfinite(x)` is effectively the opposite.
- Single column: `x_nonans = x(~isnan(x));` gives 343 of 366 values.
- Removing NaNs per column leaves columns of uneven length. It is better to **remove every row that contains a NaN in any column**:
```matlab
tableArray = table2array(bikePathTable(:, 3:end));   % drop Date and Time; arrays must be all numeric
findNans   = sum(tableArray, 2);                      % sum across each ROW (dimension 2) -> NaN if any NaN
bikePathTableNoNans = bikePathTable(isfinite(findNans), :);   % 279 x 91, keeps Date
```
- `sum` does not work directly on tables, which is why the data is converted with `table2array` first.
- Watch the (rows, columns) ordering. The Workspace panel sizes are a quick sanity check.
- Keep the table version rather than the array so you retain the dates for later analysis.

### Part 3: Filtering by date and time (06)
```matlab
isMay     = bikePathTableNoNans.Date.Month == 5;
mayData   = bikePathTableNoNans(isMay, :);
dayOfWeek = weekday(bikePathTableNoNans.Date);       % 1 = Sunday ... 7 = Saturday
weekend   = dayOfWeek == 1 | dayOfWeek == 7;
weekdays  = ~weekend;                                % 198 weekday rows, 81 weekend rows
mean(bikePathTableNoNans.BicentennialBikeway(weekdays))
mean(bikePathTableNoNans.BicentennialBikeway(weekend))   % about 1000 fewer on weekends
```
- `==` tests equality, `=` assigns, `|` is OR and `~` is NOT.
- You can filter the same way on any variable: seasons, school holidays, public holidays, special events or weather.

### Part 4: Splitting and merging tables (07)
- **Splitting:**
  - `T(:, 6)` selects one column.
  - `T(:, 6:8)` or `T(:, [6 8])` selects several columns.
  - `T(10:100, :)` selects a range of rows.
  - `T(:, {'BishopStreet...'})` selects columns by name. Names come from the CSV header row.
- **Horizontal merge (adding columns):**
```matlab
weather1 = readtable('...rainfall...csv');      % BOM gives one variable per file
weather2 = readtable('...maxtemp...csv');
merged = [weather1(:, 'Rainfall...') weather2(:, 'MaximumTemperature...') bikePathTable];   % 366 x 93
```
  - All tables must have the **same number of rows**. Using the 279-row no-NaN table with the 366-row weather tables gives an error, so merge first and remove NaNs afterwards.
- **Vertical stacking (adding rows):** `[T; T]` gives 732 × 91. This is useful for combining several years of data.
  - Tables must have the **same variables (columns)**. 93 vs 91 columns gives an error.
  - You can only concatenate tables with tables. Convert arrays with `array2table` first.
- `size(T)`, `size(T, 1)` (rows) and `size(T, 2)` (columns). Asking for a dimension that doesn't exist returns 1 rather than an error.

### Loading data without code: the Import Tool (08)
- Double-click the CSV, or use the **Apps** tab, to open the Import Tool.
- Choose **Delimited** and **Output Type: Table**. You can rename columns (for example `Var2` to `Time`) and change column types (numeric, text, categorical).
- Under missing data rules, change "Replace unimportable cells with NaN" to **Exclude rows**. The result is the same 279 × 91 table as the code approach.
- **Generate Script** or **Generate Function** turns the import into reusable code.
- The Import Tool is slower than code but needs no programming.

### Visualising distributions (09)
- **Dataset:** Washington bike share, daily data for 2011 and 2012. Columns include:
  - instant, date, season, year, month, holiday, weekday (**0 to 6**, unlike MATLAB's 1 to 7), working day and weather situation (1 clear through 4 heavy rain or snow).
  - temperature and apparent temperature, humidity and wind speed. These are all scaled into the 0–1 range. The presenter says they are min–max normalised, but in `data/day.csv` `temp` only spans 0.06 to 0.86, so they are scaled down rather than normalised to exactly 0 and 1.
  - casual, registered and total user counts.
- **`histogram`:** easy to overlay datasets of different lengths, but gets crowded with many series and automatic bin widths can differ. Set consistent bin edges.
- **`hist`:** draws side-by-side bars, but requires series of equal length because they are concatenated.
- Histograms don't show the mean or median directly, so pair them with a table of summary statistics.
- **`boxplot`:**
  - The red line is the median and the blue box is the middle 50% (IQR).
  - Whiskers show the rest of the data, and red crosses mark outliers. By default MATLAB flags points beyond 1.5 × IQR from the box.
  - Side-by-side box plots make comparison easy: registered users greatly outnumber casual users, but casual users have more outliers.
  - Box plots don't show relationships between variables. Use scatter plots for that.
- Box plots of different-length series can't be concatenated, and `hold on` just draws them on top of each other. The workaround is to use **`subplot`s with the same `ylim`** (for example 0 to 7000).
  - This shows usage rising from 2011 to 2012 across all groups, and a much larger registered-vs-casual gap on weekdays than on weekends.
- Always label axes and add titles in reports. Box plot comparisons stay valid with unequal sample sizes or sporadic missing data, as long as big chunks (such as a whole peak season) are not missing.

---

## 4. Excel track

**Dataset:** concrete compressive strength, from Canvas as a CSV. It has 9 attributes: cement, blast furnace slag, fly ash, water, superplasticiser, coarse aggregate and fine aggregate (all in kg/m³), age in days, and compressive strength in MPa. There are 1030 observations.

### Importing and handling missing values (10)
- **Import option 1:** File → Open, change the file type filter to *All files* or *Text files*, open the CSV, then **Save As → Excel Workbook**.
- **Import option 2:** Data → **From Text/CSV** → Load, which loads the data as a table.
- **Locate blanks:** select the data (Shift + End), then Conditional Formatting → New Rule → "Format only cells that contain" → **Blanks**, and choose a highlight colour.
- **Count functions:**
  - `COUNT` counts cells containing numbers.
  - `COUNTA` counts non-empty cells, including text.
  - `ISBLANK` returns TRUE or FALSE for one cell.
  - `COUNTBLANK` counts the blank cells in a range.
- `COUNTBLANK` per row, summed, gives **17 missing values**. Doing the same per column shows which attributes are missing data. The missing percentage is small (about 2%); increase the decimal places to see it.
- **Strategy 1: Omission (deletion).** Remove every observation with at least one missing value. This is the most common approach.
  - Drawbacks: it reduces the sample size and statistical power, and can introduce bias.
  - In Excel: filter the per-row blank-count column for values ≥ 1, then delete those rows. This leaves **1018 observations**.
- **Strategy 2: Imputation.** Replace blanks with an estimate such as the mean, median or mode.
  - Be careful: this is not suitable for every dataset, or when many values are missing.
  - In Excel:
    1. Compute `AVERAGE` for each column.
    2. Paste the averages **as values** to avoid a circular reference.
    3. Select a column and press **Ctrl + G → Special → Blanks**.
    4. Type `=` followed by the (absolute) average cell, then press **Ctrl + Enter**.
- Omission was used for the rest of the Excel videos.

### Filtering data (11)
- Convert the data to a table with **Ctrl + T** (tick "My table has headers"), or use Insert → Table.
- **Column drop-down:** sort, filter by value (for example age = 7), or use **Number Filters** (greater than, top 10, above average, and so on).
- **Custom AutoFilter:** combine two conditions with AND/OR, for example age ≥ 7 AND age ≤ 14.
- **Clear filters:** Data → Clear.
- **Advanced Filter** (Data → Advanced):
  1. Create a criteria range: a header matching the column name, with the values underneath (for example 7).
  2. Set the list range to the table.
  3. Choose to filter in place or copy to another location. Adding more rows to the criteria range adds OR conditions (for example ages 1, 3 and 7).
- **`FILTER` function:** for example `=FILTER(table, table[Age]=7)`.

### Appending and merging tables with Power Query (12)
- **Appending (stacking rows):** example using a 7-day table and a 14-day table.
  1. Name each table (Table Design → Table Name).
  2. Data → Get Data → From Other Sources → **Blank Query**.
  3. In the formula bar enter `= Excel.CurrentWorkbook()`, then **expand** the Content column.
  4. **Close & Load To** a table in a new worksheet. The result is 189 rows: all day-7 rows followed by all day-14 rows.
- **Merging (joining columns on a key):** example using a mix-design table and a strength/age table that share an **ID** column.
  1. Trim each table to only the rows with data. Extra blank rows slow queries down and cause errors.
  2. For each table: Data → **From Table/Range** → Close & Load To → **Only Create Connection**.
  3. Data → Get Data → **Combine Queries → Merge**. Select both tables and click the common ID column in each.
  4. **Expand the second table's column.** Forgetting this step gives only the first table's data.
  5. Close & Load To a new worksheet.

### Data visualisation (13)
- **Histogram** (Insert → Charts → All Charts → Histogram) for compressive strength: roughly normal but slightly skewed. Always add a chart title and axis titles for reports.
- A **clustered column** chart shows individual observations but doesn't reveal the distribution.
- **Box and whisker chart:**
  - Shows the minimum, Q1, median, Q3, maximum and IQR. Whiskers extend from the box, and outliers are plotted as dots.
  - If the median is below the centre of the box, the data is positively skewed. If it is above the centre, the data is negatively skewed.
- **Comparing groups:** box plots of strength at 7, 28 and 90 days on one chart (add a legend).
  - Strength increases over time.
  - At 7 days the data is positively skewed; by 90 days it is roughly normal.
  - 28 days has more outliers.

---

## 5. Python track

### Jupyter notebooks (14)
- **Setup:** go to <https://jupyter.eres.qut.edu.au/> and choose **EGH404 Notebook** under Server Options (not EGB103 or General Notebook), then Start. JupyterLab opens with a file browser on the left and a Launcher for new Python 3 notebooks, consoles, terminals and text or Markdown files. Log out and back in if the environment isn't listed. Files you create there persist.
- **Why notebooks:** they combine code, results, charts and Markdown explanations, and results can be reproduced and edited in place.
- **Cells:**
  - Shift + Enter runs a cell and moves to the next one.
  - The numbers on the left show **execution order**, not position. If something behaves unexpectedly, check the order. **Run → Run All Cells** executes top to bottom.
- **Markdown cells:** `#` for a title, `##` for a heading, plus text and numbered lists.
- **Export:** File → Save and Export Notebook As (PDF, HTML and others), or Download.
- **New to Python?** Work through the first two chapters of the GitHub course [jvdkwast/Python3_Jupyter_Notebook](https://github.com/jvdkwast/Python3_Jupyter_Notebook). This is enough for the modules from Week 8. Download the `.ipynb` and upload it to JupyterHub.

### Preprocessing with pandas (15, 16)
Transcript 16 is a shorter recording covering the loading, missing-data, date and merging sections of the same practical.

```python
import pandas as pd, numpy as np, matplotlib.pyplot as plt

df = pd.read_csv('bike-ped-auto-counts-2016.csv', header=0)   # header=None if there is no header row
df.info()               # dtypes and non-null counts: 366 vs 343/350 non-null reveals missing values
df.head(); df.tail()    # first and last 5 rows: sanity-check the load
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')   # object -> datetime64
df.shape, df.shape[0], df.shape[1]                           # (rows, cols)
```
- Prefer **pandas** over the `csv` module because pandas makes data manipulation much easier.
- There are two ways to access a column: `df.Date` or `df['Date']`. The dot form only works when the name has no spaces or special characters.
- **Spot gaps visually:**
  - `df['Bicentennial Bikeway'].plot()` shows gaps around rows 60 to 100.
  - Plotting a second column shows it has gaps too, at slightly different places, and a very different scale (about 4000 vs 400 to 500 per day).
- **Integer indexing:** `df.iloc[60:80, 0:10]` (rows, columns) shows NaN from row 68, most likely a sensor malfunction.
- **Boolean masks:** for example `samples = np.array(range(10)); samples[samples < 5]`.
- `np.isfinite(col)` is False for NaN and ±inf. `np.isnan(col)` / `col.isna()` detect only NaN.
- Filtering one column this way gives 343 finite values out of 366.
- `.values` / `df.to_numpy()` return plain NumPy arrays without metadata (the index and column names).
- To keep only the numeric data: `df.iloc[:, 2:].to_numpy()`.
- **Removing missing values:**
  - `df.dropna(axis=0)` drops rows with any NaN.
  - `axis=1` drops columns instead.
  - Make sure enough samples remain for modelling.
  - For time series, **interpolating** from neighbouring days is an alternative.
- **Dates** (`clean` is the NaN-free data frame):
```python
wd = clean.Date.dt.weekday                      # pandas: 0 = Monday ... 6 = Sunday
weekend = (wd == 5) | (wd == 6)                 # | is OR
weekdays = clean.loc[~weekend]                  # ~ is NOT
march_weekdays = weekdays.loc[weekdays.Date.dt.month == 3]   # only 2 rows: most of March was missing
```
- **`.iloc` vs `.loc`:** `iloc` uses integer positions. `loc` uses labels, for example `df.loc[:, ['Bicentennial Bikeway', 'Bishop Street ...']]`.

### Merging data sets with pandas (15, 16)
- The example combines Bureau of Meteorology rainfall and maximum temperature files with the bike counts. All cover 1 January to 31 December 2016 (366 rows).
- **Merge first, then remove NaNs.** Missing days differ between sources, so dropping them first would misalign the rows.
- `pd.merge` needs a common key column. These files have none, so use **`pd.concat`**:
```python
merged = pd.concat([w1['Rainfall amount (millimetres)'],
                    w2['Maximum temperature (Degree C)'],
                    bike], axis=1)              # side by side: 366 x 93 (was 91)
stacked = pd.concat([w1, w2, bike], axis=0)     # stacked: 1098 rows, filled with NaN / NaT
```
- Vertical stacking of unrelated tables fills the gaps with NaN (and NaT, "not a time"), so it is rarely what you want here.
- When adding columns, make sure the rows actually correspond (same date in every row).

### Correlation, summary statistics and distributions (15)
- **Dataset:** Washington bike share daily data, loaded with `pd.read_csv('day.csv', header=0, index_col='dteday')`, then `df.index = pd.to_datetime(df.index)`.
  - After setting `index_col`, access the dates through `df.index`, not the column name.
  - In this dataset, `weekday` uses 0 = Sunday and 6 = Saturday, which differs from pandas `dt.weekday`.
- **Four subsets:** 2011 weekday, 2011 weekend, 2012 weekday and 2012 weekend. They are built from `~((weekday == 0) | (weekday == 6)) & (yr == 0)` and similar. 2011 has 365 days and 2012 has 366 (leap year). The subsets have 260, 105, 261 and 105 rows.
- **Pearson correlation** (ranges from −1 to +1; 0 means uncorrelated). Correlation is covered properly in Weeks 9 and 10.
  - 2011 weekday registered vs casual: about **0.65**, a moderate positive correlation. The scatter plot shows an upward trend with spread.
  - 2011 weekend registered vs casual: about **0.81**, a stronger correlation with a tighter trend.
  - 2011 vs 2012 weekend registered: about **0.62**.
  - Both variables need the same number of samples.
- **Date lookups:** `df[(df.index.month == 3) & (df.index.day == 5)]` returns one row per year. 29 February returns only a 2012 row.
- **`df[['registered', 'casual']].describe()`** gives count, mean, std, min, 25% (Q1), 50% (median) and 75% (Q3), and max. Use `.mean()` and similar for individual statistics.

| Group | Registered mean | Casual mean |
|---|---|---|
| 2011 weekday | about 2900 | 492 |
| 2011 weekend | about 2263 | 1134 |
| 2012 weekday | about 4900 | 756 |
| 2012 weekend | about 3712 | 1668 |

- **Histograms** (`plt.hist(..., bins=range(0, 5000, 50), label=...)` plus `plt.legend()`):
  - Weekday casual users are mostly under 1000 per day; registered users are mostly 3000 to 4000 or more.
  - Weekends need wider bins (100) because there are fewer samples.
  - Weekends have more casual users and fewer registered users.
- **Histograms vs box plots:**
  - Histograms show shape, modality, spread and skew.
  - Box plots show the median, Q1, Q3, IQR and **potential outliers**.
- **Box plot details:**
  - The upper whisker bound is **Q3 + 1.5 × IQR** and the lower bound is **Q1 − 1.5 × IQR**. Points beyond the bounds are potential outliers.
  - Using `plt.boxplot` in four subplots shows that 2012 usage is higher than 2011 and registered users are always higher than casual users.
- The variables have very different ranges and scales, which is a signal to **standardise** data before regression or machine learning (Week 10).

---

## 6. Other Week 7 materials

### Practical 3: MATLAB refresher ([`slides/practical-3-matlab-refresher.pdf`](slides/practical-3-matlab-refresher.pdf))
A one-page setup sheet with three steps:
1. Install MATLAB through the QUT IT Helpdesk (Software and Downloads). The sheet names MATLAB 2017b, which is an old version, so use whatever the helpdesk currently offers.
2. Or sign up for [MATLAB Online](https://au.mathworks.com/products/matlab-online.html).
3. Download, review and run the examples from the online lectures. The sheet's Blackboard link is out of date; the examples are now on Canvas.

### Lecture slides
- [`slides/summary-stats-data-wrangling-statistics-visualisation.pdf`](slides/summary-stats-data-wrangling-statistics-visualisation.pdf): the 16 slides for transcript 02. Their extra details are merged into section 2 of these notes. They include the histogram of student heights (114 to 129 cm, peaking at 121 to 122 cm, from the ABS) and the steps for IQR outlier limits:
  1. Find Q1 and Q3.
  2. Compute IQR = Q3 − Q1.
  3. Treat anything outside Q1 − 1.5 × IQR to Q3 + 1.5 × IQR as an outlier.
- [`slides/introduction-to-jupyter-notebook.pdf`](slides/introduction-to-jupyter-notebook.pdf): the 9 slides for transcript 14. They are screenshots of the same walkthrough, with the details merged into section 5.

### Practical dataset: [`data/day.csv`](data/day.csv)
This is the Washington bike share daily dataset used in transcripts 09 and 15. Load it with `readtable('day.csv')` in MATLAB or `pd.read_csv('day.csv', index_col='dteday')` in pandas.
- 731 rows (1 January 2011 to 31 December 2012) and 16 columns: `instant, dteday, season, yr, mnth, holiday, weekday, workingday, weathersit, temp, atemp, hum, windspeed, casual, registered, cnt`.
- `yr` is 0 for 2011 and 1 for 2012. `weekday` uses 0 = Sunday to 6 = Saturday. `cnt` = `casual` + `registered`.
- No missing values, so it needs no NaN cleaning (unlike the Brisbane data).
- Total daily rentals (`cnt`) range from 22 to 8714, with a mean of about 4504 and a median of 4548.
- Recomputing the practical's figures from this file confirms the transcript numbers:

| Subset | Days | Registered mean | Casual mean | Pearson r (registered vs casual) |
|---|---|---|---|---|
| 2011 weekday | 260 | 2916 | 493 | 0.65 |
| 2011 weekend | 105 | 2263 | 1135 | 0.81 |
| 2012 weekday | 261 | 4931 | 757 | 0.60 |
| 2012 weekend | 105 | 3712 | 1669 | 0.81 |

---

## Key takeaways across all tools

1. Always **look at the data first**: check the header row, column types, size and head/tail before analysing.
2. **Missing values** (`NaN` or blanks) break arithmetic. Find them, measure how many there are, then choose between **omission** and **imputation** (or interpolation for time series) based on context.
3. When combining sources, **merge first, then clean**, and make sure rows line up (same dates or IDs). Horizontal merges need equal row counts; vertical stacks need matching columns.
4. Convert dates to proper **date/time types** so you can filter by month, weekday, weekend or season. Weekday numbering conventions differ between tools and datasets (MATLAB: 1 = Sunday; pandas: 0 = Monday; bike share data: 0 = Sunday).
5. Use **histograms** for distribution shape and **box plots** for medians, spread and outliers. Pair plots with tables of summary statistics, and always label axes and titles.
6. In skewed data, the **median** is more robust than the mean. Decide on outliers deliberately, because they may be errors or they may be the signal you are looking for.
