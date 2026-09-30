# Week 8 Study Notes – Correlation and Regression

These notes summarise the Week 8 transcripts in [`transcripts/`](transcripts/) and the slides in [`slides/`](slides/). Transcript numbers in brackets, such as (09), point to the matching file.

**Datasets:**
- **Washington bike share daily data** ([`../week-7/data/day.csv`](../week-7/data/day.csv)): 731 days, 2011–2012. Used in the MATLAB and Python tracks.
- **Concrete compressive strength data** (from Canvas): used in the Excel track.

**How the numbers were checked:** all bike share figures quoted below were recomputed from `day.csv` with pandas and statsmodels, and they match the lecturers' results.

**Assignment link:** this week covers **Assignment 2, Section 2 (correlation) and Section 3 (multiple linear regression)**.

---

## 1. Correlation concepts (01, 02, 03, slides)

### What correlation is
- Correlation measures how two variables move together.
  - **Direction:** positive (they rise together, for example rainfall and raincoat sales) or negative (one rises as the other falls).
  - **Strength:** on a scale from −1 to +1.
- **Pearson correlation coefficient r:**
  - +1 is a perfect positive linear relationship, −1 a perfect negative one, and about 0 means no *linear* relationship.
  - |r| close to 1 means a strong association; |r| close to 0 means a weak one.
  - The slides show example plots at r = 0.8, 0.3, −0.9, −0.2 and 0.0. As |r| falls, the points spread further from a line.
- **Formula:**

  r = cov(x, y) / (s_x × s_y) = Σ(xᵢ − x̄)(yᵢ − ȳ) / √[Σ(xᵢ − x̄)² × Σ(yᵢ − ȳ)²]

- **Why the formula gives the direction (14):** when x and y are both above their means, or both below, each product (xᵢ − x̄)(yᵢ − ȳ) is positive. When one is above and the other below, the product is negative. Summing the products gives the overall direction, and dividing by the standard deviations normalises the result into −1 to +1.
- **Covariance (03):** the average of (x − mean of x) × (y − mean of y), which describes how the two variables vary together. Use `cov` in MATLAB and `np.cov` in Python.
- **Distributions (03):**
  - A **joint distribution** describes x and y together.
  - A **marginal (unconditional) distribution** describes x ignoring y, or y ignoring x.
  - A **conditional distribution** describes y within a slice of x (for example x between 4 and 4.25), or x within a slice of y.
  - Real data is a sampled ("discretised") version of the ideal distribution.

### Assumptions for Pearson r (07, 14, slides)
1. Both variables are **continuous**, measured on an interval or ratio scale (for example temperature, height, test scores).
2. The relationship is **linear**. Check with a scatter plot first.
3. There are **no extreme outliers**. A single outlier shifts the means and can change r a lot. Check with box plots.
4. The variables are roughly **normally distributed**. Check that the histogram is bell-shaped, or that the box plot's median is centred with whiskers of similar length.

### Non-linear relationships
- Pearson r only captures *linear* relationships. It will still return a number for a non-linear relationship, but the number doesn't describe that relationship.
  - **Quadratic example:** building energy use vs outdoor temperature. Energy use is high when it's cold (heating), low when it's mild, and high again when it's hot (cooling).
  - **y = x² example:** a perfect relationship, yet r ≈ 0 because the positive and negative products cancel out.
  - Exponential and polynomial relationships are common in engineering, for example the age of a structural component vs its failure likelihood.
- **Always plot the data first.**

### Examples from the slides
- **Temperature vs heaters sold** (12 months): `=CORREL(Table1[Temperature], Table1[Heaters Sold])` gives **r = −0.984**, a strong negative correlation. (The transcript's "−9.8" is a transcription error.)
- **Concrete correlation matrix** (Kaggle cement manufacturing dataset), correlation of each ingredient with strength:

| Ingredient | cement | slag | ash | water |
|---|---|---|---|---|
| r with strength | 0.498 | 0.135 | −0.106 | −0.29 |

  Cement contributes moderately and positively to strength, while ash and water are negatively correlated with it.

### Correlation does not imply causation
- **Ice cream sales vs sunburns (r ≈ 0.8):** neither causes the other. The sun is the root cause of both.
- **Spurious correlations (02):**
  - US science spending vs suicides by hanging.
  - Pool drownings vs the number of Nicolas Cage films.
- **Confounding variables (14):**
  - Coffee consumption vs income: age drives both.
  - Social media use vs fitness: younger people use more social media and tend to be fitter.
- To establish causation, design experiments after you find a correlation.
  - **Concrete example (07):** cement acts as a binding agent, which is why more cement is associated with higher strength.
  - **Superplasticiser example (07):** superplasticiser keeps the mix workable with less water. Less water means fewer pores and a more compact structure, so the mix is stronger.
  - From correlation alone you can only say "strength increase is *associated with* more cement", not "cement increases strength".
- **Don't correlate proportions (02).**

### Anscombe's quartet (02)
- Four x–y datasets with the same means, standard deviations and correlation (r ≈ 0.81) but completely different shapes:
  1. A noisy linear trend.
  2. A clear curve, so the relationship is non-linear.
  3. A perfect line distorted by one outlier.
  4. No real relationship, with one extreme point creating r.
- Always combine r with visualisation.

### Subgroups (14)
- If the data contains distinct clusters (for example weekday vs weekend electricity use, or active vs inactive people), r describes the *separation between the groups*, not the relationship within them.
- Split the data and compute r for each group separately.

### Why correlation matters for modelling (06)
- It helps with **feature selection**: keep the variables that correlate with the target, and drop redundant ones.
- Too many variables lead to overfitting and the curse of dimensionality. For example, 30 sensors where 5 would do.
- A **correlation matrix**, optionally drawn as a heat map, shows every pair of variables at once.

### Why this matters for the assignment (14)
- **Synthetic data:** data generated by a generative AI model from per-variable constraints lacks the realistic relationships between variables that real data has. That's why the assignment asks for a realistic dataset related to your topic.
- **Interpreting r in the assignment:** interpret and justify each r you report. Discuss clusters, outliers and possible confounders.

---

## 2. Correlation in practice

### MATLAB (04, 05)
```matlab
dailyData = readtable('day.csv');
figure; subplot(2,2,1); scatter(dailyData.temp, dailyData.cnt); title('count vs temp')
% ... repeat for atemp, hum, windspeed in subplots 2 to 4
C = corrcoef(dailyData.temp, dailyData.cnt)   % 2x2 matrix: diagonal = 1, off-diagonal = r
title(num2str(C(1,2)))                          % put r in the plot title
noDaysOff = dailyData(dailyData.workingday == 1, :);   % 500 x 16
corrcoef([d.casual d.temp d.atemp d.hum d.windspeed])  % 5x5 matrix of every pair
```
- **Reading the output:**
  - `corrcoef` returns a symmetric matrix. Only the off-diagonal value matters for a single pair.
  - Passing many columns gives every pair at once. This is useful for comparing many sensors, but pairs like temp vs atemp (both derived from temperature) are meaningless.
- **Common errors:** unbalanced parentheses, and mistyping `gcf` as `cfg`. Check copy-and-paste edits carefully.

Correlation of daily users with weather, recomputed from `day.csv`:

| Users | temp | atemp | hum | windspeed |
|---|---|---|---|---|
| All days, total (`cnt`) | 0.63 | 0.63 | −0.10 | −0.24 |
| All days, registered | 0.54 | 0.54 | −0.09 | −0.22 |
| All days, casual | 0.54 | 0.54 | −0.08 | −0.17 |
| Working days, registered | 0.55 | 0.55 | −0.14 | −0.21 |
| Working days, casual | **0.72** | 0.71 | −0.15 | −0.18 |

- **Lesson 1: the same r can hide different shapes.** Registered and casual users both have r = 0.54 with temperature, but their scatter plots look very different. Registered users follow a linear trend with noise; casual users follow a curved, more exponential-looking shape.
- **Lesson 2: filtering reveals structure.** Restricting to **working days** shows that casual users (likely tourists) are much more weather-sensitive (r = 0.72), with a linear relationship. Registered users barely change.
- Correlation is a starting point: filter, visualise and rerun the analysis to understand what's going on.

### Python (06)
```python
daily = pd.read_csv('day.csv', header=0)
daily['dteday'] = pd.to_datetime(daily['dteday'], format='%Y-%m-%d')   # shape (731, 16)
fig, ax = plt.subplots(2, 2); ax[0, 0].scatter(daily.cnt, daily.temp)   # etc.
np.corrcoef(daily.temp, daily.cnt)[0, 1]
```
- **Reading scatter plots:**
  - An upward trend means positive correlation; a downward trend means negative.
  - The tighter the points sit around the imagined trend line, the stronger the correlation.
  - In this data, temperature and apparent temperature show strong positive trends; humidity and wind speed show weak negative ones.
- r = +1 and r = −1 are *both* strong correlations. The sign gives only the direction.
- **`cnt` = `casual` + `registered`**. For example, the first day has 331 + 654 = 985. (The transcript says "645", a transcription error.)

### Excel (07): concrete data, 7-day samples only
- **Water–cement ratio:**
  1. Add a new column `=water/cement`.
  2. Draw a scatter plot against 7-day strength (Insert → Scatter; add axis titles via Chart Design → Add Chart Element).
  3. Try **Trendline → More Options** with Linear, Exponential and **Power** fits. Power fits best, so the relationship is not linear and you shouldn't report Pearson r for it.
- **Cement vs strength:** looks linear, so compute r.
  - **Data → Data Analysis → Correlation** (enable the **Analysis ToolPak** under Add-ins if it's missing). Tick "Labels in first row" and choose an output cell.
  - The result is **r = 0.759**, a strong positive correlation.
- **Full correlation matrix:** run the same tool on all ingredients plus strength.
  - The diagonal is always 1. Focus on the **last row** (each input vs strength). Cement and superplasticiser are strongly positive; water is negative.
  - Use **Home → Conditional Formatting → Color Scales** (green–yellow–red) to visualise it. The colours are relative to the values in the matrix, so read them with care.
  - Use Format Cells → Wrap Text so the headers are readable.

---

## 3. Regression concepts (08, 14, slides)

### What regression is
- Regression models the relationship between a **dependent variable** (what you predict) and one or more **independent variables** (predictors), so you can predict unseen cases.
- **Engineering examples:**
  - concrete strength vs curing time;
  - implant working life vs surface coating;
  - packet transmission time vs network load;
  - battery capacity vs temperature;
  - fatigue life vs stress amplitude.
- **Correlation vs regression:** correlation asks *is there a relationship?* Regression *quantifies and predicts* it.

### Simple linear regression
- "Simple" means one independent variable. "Linear" means linear *in the parameters*.
- The model is Y = β₀ + β₁X + ε, which is the same as y = mx + c.
  - β₀ (c) is the intercept.
  - β₁ (m) is the slope, or coefficient.
  - ε is the error term.
- "Fitting a line to a bivariate dataset can be a deceptively complex problem" (Warton et al., 2006).
- **Multiple linear regression:** y = β₀ + β₁x₁ + β₂x₂ + … With two predictors the model fits a plane; with more, a hyperplane.

### Fitting methods (the regression slides)
- **Ordinary least squares (OLS), y onto x:** minimises the squared *vertical* distances. Used to predict y from x. This is the default.
  - Errors are squared so that positive and negative errors don't cancel out.
- **OLS, x onto y:** minimises the squared *horizontal* distances. Used to predict x from y.
- **Orthogonal regression:** minimises the *perpendicular* distances. Used when both x and y have measurement error. It relates to principal component analysis (PCA).
- **The three methods give different "best-fit" lines for the same data.** Robust fitting options can also down-weight outliers.

### Reading regression output (14, slides)

| Statistic | Meaning |
|---|---|
| **Coefficient** | Expected change in y for a one-unit change in that predictor. The sign gives the direction, the size gives the magnitude, and it carries the predictor's units. For example, an age coefficient of 1314 means income rises by about $1314 per extra year. |
| **Standard error** | Uncertainty in the coefficient estimate; smaller is more precise. Coefficients have different scales, so compare the coefficient-to-standard-error ratio. Rule of thumb: if the coefficient is less than about 2 × its standard error, the estimate is too uncertain to trust. |
| **t-stat and p-value** | The null hypothesis is that the predictor has no effect. **p < 0.05** means the predictor is statistically significant at the 95% level. p > 0.05 means there is insufficient evidence that it adds explanatory power. |
| **F-statistic** | Whether the model *as a whole* explains more variance than just predicting the mean. Most useful with many predictors. |
| **R²** (coefficient of determination) | Proportion of the variance in y explained by the model; closer to 1 is better. For example, R² = 0.18 means 18% of the variation is explained and 82% is not. In simple regression, R² = r². |
| **Adjusted R²** | R² penalised for the number of predictors. Plain R² always rises when you add variables, even noise, so **use adjusted R² for multiple regression**. |
| **Residuals** | Actual minus predicted values. Plot them against fitted values: an even band (homoscedasticity) is good. A **fan shape** (heteroscedasticity) or curve means the model is misspecified, for example missing a non-linear term. |
| **RMSE** | √(mean of squared errors). Report it on the **test set**. |

- **Assumptions of linear regression:** linearity, independence and homoscedasticity.
- **Multicollinearity:** correlated predictors (for example temp and atemp, or age and fitness) inflate standard errors and p-values. Removing one of them can make others significant.

### Model building workflow (14, and Assignment 2)
1. Split into **training** and **test** sets. Never change the test set between models.
   - Assignment 2 specifies the split. The transcript says "first January 24 to December 31 inclusive" for training and the remaining data for testing. Check the exact dates in the assignment brief.
2. Fit the model with **all** candidate predictors.
3. Remove the **least significant** predictor (highest p-value above 0.05), **refit**, and repeat. The p-values change after each removal, so remove one at a time.
4. Stop when every predictor has p < 0.05 and adjusted R² is highest.
5. Evaluate on the test set with RMSE, actual-vs-predicted plots and residual plots.
6. In the report, justify each simplification and its impact on performance. Put intermediate models and plots in an appendix.

- **Prefer the simplest model that performs as well.** Simpler models generalise better.
- **Categorical predictors** (holiday, weekday, workingday, weathersit) must be marked as categorical. They become dummy (indicator) variables with one coefficient per level. Keep a categorical variable if any of its levels is significant.
- **Rank deficiency and the curse of dimensionality:** too many parameters for the data gives "design matrix is rank deficient" warnings and unstable predictions.

---

## 4. Regression in practice: bike share data

**Train/test split used in both MATLAB and Python:** the test set is July to December 2012 (184 days). The training set is everything before (547 days).

Model results, recomputed from `day.csv` with OLS (they match the lecture output):

| Model | Predictors | Train R² | Adj. R² | Test MSE | Test RMSE |
|---|---|---|---|---|---|
| 1. Basic | temp | 0.420 | 0.419 | 4.73 M | 2175 |
| 2. Weather | temp, atemp, hum, windspeed | 0.506 | 0.503 | 4.63 M | 2152 |
| 3. Everything | Model 2 + categorical holiday, weekday, workingday, weathersit | 0.528 | 0.517 | 4.43 M | 2105 |
| 4. Refined, all training data | categorical weathersit, atemp, hum, windspeed | 0.521 | 0.517 | 4.33 M | 2082 |
| 5. Refined, **2012 training data only** | same as Model 4 | **0.739** | **0.732** | **1.91 M** | **1383** |

- **Model 1:** the equation is cnt ≈ 1055 + 6109 × temp. The training RMSE is about 1300, but the model underestimates the test period by about 1000 or more per day.
- **Model 2:** `temp` becomes insignificant (p = 0.057) because it is almost the same as `atemp`. This is multicollinearity.
- **Model 3:** holiday, weekday, workingday and temp all have p > 0.05. Adding them all barely improves the fit and triggers the rank-deficiency warning.
- **Model 5:** usage jumped from 2011 to 2012, so the 2011 data describes a different distribution from the test period. Training only on 2012 more than halves the test error.
  - **Lesson:** training data should represent the conditions you'll predict, and more data isn't always better.
  - **Lesson:** visualise the data before modelling.
- **Unseen events:** the sharp dip in late October 2012 is Hurricane Sandy. No model predicts an event it has never seen.
- **Correlation doesn't always carry over to regression:** workingday was very revealing in the correlation analysis, but it is not significant as a regression predictor.

### MATLAB `fitlm` (09, 10)
```matlab
testFlag = dailyData.dteday.Year == 2012 & dailyData.dteday.Month > 6;
training = dailyData(~testFlag, :);  testing = dailyData(testFlag, :);   % 547 / 184 rows
model = fitlm(training.temp, training.cnt)      % shows estimates, SE, tStat, pValue, RMSE, R-squared
plot(model)                                      % data, fit and confidence bounds (call figure first!)
pred = predict(model, testing.temp);
plot(testing.dteday, [testing.cnt pred]); legend('actual', 'predicted')
m2 = fitlm([training.temp training.atemp training.hum training.windspeed], training.cnt);
mAll = fitlm([... 8 columns ...], training.cnt, 'CategoricalVars', [5 6 7 8]);
mRobust = fitlm(X, y, 'RobustOpts', 'on');       % down-weights outliers (no gain here: the data is clean)
mQuad = fitlm(X, y, 'quadratic');                % adds squared and interaction terms: better fit, many more terms
rmse = sqrt(mean((testing.cnt - pred).^2));
```
- **Categorical indices:** `'CategoricalVars'` indices refer to column positions in X. Update them when you remove columns, or MATLAB errors.
- **`predict` input:** it needs the same number and order of columns the model was trained on. The error "X must have 8 columns" means they don't match.
- **Wilkinson formula notation:** `fitlm(tbl, 'cnt ~ temp + hum')` also works with table column names.
- **Refined model results:** training RMSE about 1000, test RMSE just under 2000. Test error is always the honest measure.

### MATLAB Regression Learner app (11)
- **Opening it:** Apps → **Regression Learner** → New Session → From File (or From Workspace) → `day.csv`.
- **Setup:**
  - Choose the **response** (`cnt`) and untick non-predictors: `instant`, `casual`, `registered`, and optionally season, year and month.
  - Set variables to **categorical in the import step**. You can't change this later.
- **Validation options:**
  - **Cross-validation:** train several times, holding out a different chunk each time, then compare average performance. Use it when data is limited.
  - **Holdout validation:** hold out one fixed portion.
  - **None.**
- **Training:** train a Linear model, or "All Quick-To-Train" to compare several; Stepwise Linear did slightly better here.
  - Plots: response, predicted vs actual, residuals.
  - Other model types (trees, SVMs, ensembles, Gaussian processes, which also give prediction uncertainty) are beyond this unit, which uses linear models only.
  - Feature Selection and PCA options are also available.
- **Export:**
  - **Export Model** gives a struct `trainedModel`, with `trainedModel.predictFcn(newData)` and `.LinearModel`.
  - **Generate Function** produces the training code; it calls `stepwiselm` for stepwise models.
- The app is slow, and the transcript assumes MATLAB 2017b or later.

### Python `statsmodels` (12)
```python
import statsmodels.api as sm, statsmodels.formula.api as smf
from sklearn.metrics import mean_squared_error
test_flag = (daily.dteday.dt.year == 2012) & (daily.dteday.dt.month > 6)
train, test = daily[~test_flag], daily[test_flag]
X = sm.add_constant(train[['temp']])             # OLS has no intercept unless you add a constant
model = sm.OLS(train.cnt, X).fit(); print(model.summary())
pred = model.predict(sm.add_constant(test[['temp']]))
mean_squared_error(test.cnt, pred)
m3 = smf.ols('cnt ~ C(holiday) + C(weekday) + C(workingday) + C(weathersit) + temp + atemp + hum + windspeed',
             data=train).fit()                   # C() marks categorical variables
```
- **Data splits:** training, validation and test sets.
  - The validation set is for hyperparameter tuning. Plain linear regression has no hyperparameters, so here you only need training and test sets.
- **Evaluate fairly:** results on the training set are optimistic; always judge the model on the test set.
- **Compare visually:** use subplots to put actual-vs-predicted plots for several models side by side.

---

## 5. Regression in Excel: concrete data (13)

- **Split the data:** the 1018 cleaned observations are split into roughly 25% test (the first 254 rows) and 75% training (764 rows). Both files are on Canvas.
- **Visualise first:** scatter plot each ingredient against strength. Cement shows a moderate-to-strong positive trend.
- **Run the regression:** Data → Data Analysis → **Regression**.
  1. Set the Input Y Range (strength) and Input X Range, and tick **Labels**.
  2. Choose the output: a new worksheet, and tick **Residuals**. Residual plots and line fit plots are optional.
  3. The X range must be **contiguous columns**. To drop predictors, copy the data and delete those columns first.
- **Reading the summary output:**
  - **Regression Statistics:** Multiple R (= |r|), R², adjusted R², standard error (in MPa) and observations.
  - **ANOVA table:** not covered in the unit.
  - **Coefficients table:** coefficients, standard errors, t-stats, p-values and 95% confidence intervals.
  - **Residual output:** predicted values and residuals.

| Model | Predictors | Multiple R | R² | Adj. R² | Std error |
|---|---|---|---|---|---|
| 1 | cement only | 0.43 | 0.186 | – | 13.7 MPa |
| 2 | all 8 (7 ingredients + age) | 0.78 | 0.609 | 0.605 | 9.54 MPa |
| 3 | Model 2 without coarse and fine aggregate (p > 0.05) | ≈ same | ≈ same | ≈ same | ≈ same |

- **Model 1 equation:** strength ≈ 15.89 + 0.0635 × cement. For cement = 212 kg/m³ this predicts ≈ 29.37 MPa. The model follows the general trend but misses the peaks.
- **Model 2:** its intercept is −1.23. Actual-vs-predicted line charts show it captures most peaks.
- **Model 3:** it performs as well as Model 2 with fewer inputs, so it is preferred.
- **Testing on the held-out 254 rows:**
  1. Copy the Model 3 coefficients into the test sheet.
  2. Write the prediction formula (intercept + Σ coefficient × input).
  3. **Lock the coefficient and intercept cells with `$`** before filling the formula down. Forgetting to lock the intercept gave badly wrong predictions in the demo.
  - The result is very good agreement between predicted and actual strength.

---

## 6. Live Week 8 practical (14, practical slides)

- **Research process recap:** identify the problem → review the literature → formulate questions → design the methodology → collect data → **analyse data** (this week) → draw conclusions → report.
- **Activity 1: `correlation_explorer.html`** (on the practical's Canvas page):

| Scenario | r | Lesson |
|---|---|---|
| Age vs income, 300 adults | ≈ 0.92 | Textbook linear case: strong positive correlation |
| Age vs internet use | weak, negative | Non-linear peak in middle age, which r misses |
| Age vs fitness, adding an outlier | moderate negative, changes with the outlier | Outliers shift r; clean the data first |
| Exercise vs heart rate, two clusters | negative | r reflects the group separation, not the within-group relationship |
| Coffee vs income; social media vs fitness | positive | Confounder (age), not causation |

- **Activity 2: `regression_explorer.html`:**
  - **Interpreting output:** the age coefficient (≈1314 $/year); standard errors compared as coefficient/SE ratios (about 45 for age vs about 8 for coffee); a p-value showing internet usage adds nothing beyond age.
  - **Fit statistics:** R² of 0.87 vs 0.17; a fan-shaped residual plot (heteroscedasticity); a large F-statistic.
  - **Backward elimination:** start with 5–6 predictors and remove the least significant one at a time.
  - **Final exercise:** find the model with the highest adjusted R² where every predictor has p < 0.05, and spot the one predictor with no real relationship to sale price.
- **Interactive Quiz Agent:** on the Canvas page "8.3 Practical: Correlation and Regression".
- **Homework:** Assignment 2, Section 2 (correlation) and Section 3 (multiple linear regression). The next class covers generating synthetic data and the remaining assignment sections.

---

## Key takeaways

1. **Plot before you compute.** Pearson r assumes a linear relationship, continuous variables, no extreme outliers and roughly normal data. Anscombe's quartet shows identical r values for completely different data.
2. **Correlation ≠ causation.** Look for confounders and subgroups, and use experiments to establish cause.
3. **The same r can hide different relationships**, and filtering (for example to working days) can reveal them.
4. **Regression quantifies and predicts.** Read the coefficients (direction, magnitude, units), standard errors, p-values (< 0.05), R² and adjusted R², the F-statistic and residuals.
5. **Keep models simple:** remove insignificant or redundant (collinear) predictors one at a time and refit. Mark categorical variables as categorical.
6. **Judge models on a fixed test set** with RMSE and actual-vs-predicted plots. Training data should represent the conditions you'll predict.
