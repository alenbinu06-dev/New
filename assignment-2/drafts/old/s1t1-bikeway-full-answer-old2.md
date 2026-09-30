# S1.T1: Bikeway Data Inspection

## (a) Box plot

[Insert Figure 1 here - the output of Box 6]

Figure 1: Box plots of daily cyclist and pedestrian counts on the Bicentennial Bikeway (Brisbane) and the North Brisbane Bikeway (Windsor), 1 January 2014 to 31 December 2018. Each panel has its own y-axis scale. Circles are days more than 1.5 x IQR above the box.


## (b) Line graph

[Insert Figure 2 here - the output of Box 7]

Figure 2: Daily cyclist and pedestrian counts on the Bicentennial Bikeway (Brisbane) and the North Brisbane Bikeway (Windsor), 1 January 2014 to 31 December 2018. Gaps in a line are missing days; flat lines at zero are periods where a counter recorded nothing.


## (c) Problematic data and how it will be handled
All date ranges are inclusive. "Remove" or "leave as missing" means the affected values in the named columns are treated as missing in the cleaned dataset and left out of calculations; whole rows are not deleted and values are not replaced with zero. The raw CSV is kept unchanged. Code evidence is in Boxes 8-15 of the appendix.

### Missing data
| Column, problem and value | Date or date range | How it will be handled | Justification |
|---|---|---|---|
| Bicentennial pedestrians and cyclists: missing (NaN), 23 days | 9-31 Mar 2016 | Leave as missing; do not impute. | Bicentennial data is missing on 95 of 1,826 days (5.2%), just above the 5% level where deletion is usually safe. Every gap is a long block with no values inside it to interpolate from, and a seasonal mean would fill 23 days with one repeated number and hide the weekday/weekend pattern. |
| Bicentennial pedestrians and cyclists: 32 days of zeros, then 62 days missing | 26 Mar-27 Jun 2017 | Treat as one 94-day outage; leave both columns missing. | Both counters drop to 0 on the same day and then stop reporting (Box 9). The bikeway was not unused for a month, so the zeros belong to the same outage. 94 days is far too long to reconstruct. |
| Bicentennial pedestrians and cyclists: missing, 10 days | 27 Jul-5 Aug 2017 | Leave as missing. | A July-August seasonal mean was considered, but it would give all 10 days the same value and flatten daily variation. The block is under 1% of the record, so removing it costs little. |
| North Brisbane pedestrians and cyclists: missing, 169 days | 1 Jan-18 Jun 2014 | Leave as missing; North Brisbane analysis starts on 29 Jun 2014. | Both columns are blank from the first date and then start with 10 days of zeros (Box 9), indicating the counter was not yet operating. North Brisbane is missing on 170 of 1,826 days (9.3%), almost all in this period. There is nothing to impute from. |
| North Brisbane pedestrians: 22 days of zeros, then 1 day missing; cyclists: 2 days of zeros, then 1 day missing | Pedestrians 11 Jun-3 Jul 2018; cyclists 1-3 Jul 2018 | Pedestrians: leave 11 Jun-3 Jul as missing. Cyclists: keep 11-30 Jun; leave 1-3 Jul as missing. | The pedestrian channel read 0 for 22 days while cyclists at the same site kept recording normal counts (e.g. 283, 286 and 275 on 11-13 Jun), so only the pedestrian channel had failed at first. Both channels read 0 on 1-2 Jul and report nothing on 3 Jul (Box 9). Interpolating 3 Jul would rely on faulty zeros. |

### Outliers
Upper 1.5 x IQR bounds from describe() (Box 5): Bicentennial pedestrians 1,867, Bicentennial cyclists 3,814.5, North Brisbane pedestrians 244.5, North Brisbane cyclists 346 users per day. All lower bounds are negative, so there are no low outliers.

| Column, problem and value | Date | How it will be handled | Justification |
|---|---|---|---|
| Bicentennial cyclists: outlier, 2,786 | Sun 3 Aug 2014 | Keep. | About 4.8 times the days either side (552-655), while pedestrians dropped to 928 that day (Box 15), which fits a cycling event rather than a counter fault. It sits inside the IQR bound, so it only shows on the line graph. Real peak demand matters for BCC upgrade planning. |
| Bicentennial pedestrians: outlier, 6,827 | Sat 21 Mar 2015 | Keep, flagged. | Above 1,867 but not a multiple of 128, so not part of the January fault. 18-19 Mar were also high (3,722 and 3,312) and the cyclist counter read 0 all week (Box 15), so pedestrian and cyclist traffic cannot be separated. Kept as a potentially genuine high pedestrian observation, but flagged because the cyclist counter was not operating and total path usage cannot be determined. |
| Bicentennial pedestrians: outlier, 3,328 | Sun 7 Aug 2016 | Keep. | The only 2016 value above 1,867 (Box 13). Cyclists fell to 720 the same day, so this is not a counter-wide failure. The spike coincides with UQ St Lucia Open Day (University of Queensland, 2016), so it is plausibly a genuine event-related increase rather than a sensor error, and peak demand is relevant to upgrade planning. |
| North Brisbane pedestrians: outlier, 546 | Sat 17 Oct 2015 | Remove. | The days either side are 28-85 and cyclists did not rise (92) (Box 15). A single pedestrian-only jump with no support from the other counter points to a recording error. |
| North Brisbane pedestrians: outlier, 670 | Sun 10 Jan 2016 | Remove. | The pedestrian counter read 0 on 5-9 and 12 Jan and 5-6 on 11 and 13 Jan while cyclists were normal (Box 15), which is consistent with an intermittent fault. 670 in the middle of this is not credible. |
| North Brisbane cyclists: outlier, 365 | Tue 23 Oct 2018 | Keep. | Only slightly above 346, and the surrounding weekdays are similar (304, 285, 330) (Box 15). 2018 is the busiest year on this bikeway, so this is normal high use. |

The IQR rule flags 220 Bicentennial pedestrian days, but 147 are in 2014, 72 in 2015 and only 1 in 2016 (Box 13), so most of them reflect an older level rather than individual outliers and they are not removed as a group. From 1 Jan to 29 Sep 2014 pedestrians averaged 1,711 a day and cyclists 654; from 1 Jun to 31 Dec 2015 pedestrians averaged 593 and cyclists 1,582 (Box 14). The combined totals are similar (about 2,370 and 2,170), and the change happens over 31 May-1 Jun 2015: the counter recorded 1,312 pedestrians and 0 cyclists on 30 May, 806 and 422 on 31 May, and 513 and 1,709 on 1 Jun (Box 11). This pattern is consistent with a change in how the counter classified users rather than a real change in behaviour. These days are kept, the break is noted, and it will be considered when interpreting the Section 2 correlations.

### Errors
| Column, problem and value | Date or date range | How it will be handled | Justification |
|---|---|---|---|
| Bicentennial pedestrians: counter fault (zeros, then values that are all exact multiples of 128) | 2 Dec 2014-5 Feb 2015 | Remove all pedestrian values in this period. | 46 of the 49 days from 2 Dec to 19 Jan are 0 (the exceptions are 90, 2,047 and 256). From 20 Jan to 5 Feb every value is an exact multiple of 128 (e.g. 8,960 = 70 x 128, 12,288 = 96 x 128, 8,064 = 63 x 128), up to six times normal, while cyclists on the same path did not rise and North Brisbane cyclists stayed normal (Box 11). Genuine counts are very unlikely to all be multiples of 128, so this is treated as a recording fault rather than crowds. |
| Bicentennial cyclists: undercount (median 24 per day) | 30 Sep-28 Dec 2014 | Remove the cyclist values. | Counts fall within two days (586 on 29 Sep, 145 on 30 Sep, 56 on 1 Oct) to a median of 24, never above 109 after 30 Sep, while pedestrians stay normal (Box 11). Checking for zeros misses this, but the line graph shows it. From 29 Dec to 14 Mar 2015 the counts are kept but flagged as uncertain: they are no longer stuck near zero and vary from day to day about as much as in early 2014 (standard deviation 192 against 177), but they stay about 40% lower (median 379 against 656) (Boxes 11 and 14), so they may still undercount. |
| Bicentennial cyclists: 77 days of zeros | 15 Mar-30 May 2015 | Remove the cyclist values. | Pedestrians kept recording normally (for example 1,222-2,157 around the start and 1,312-2,023 around the end, Box 11) while cyclists read 0 for 77 days in a row, indicating the cyclist channel was not recording. Cyclists reappear at 1,709 on 1 Jun. |
| North Brisbane pedestrians and cyclists: 10 days of zeros | 19-28 Jun 2014 | Remove, together with the 169 missing days before them. | These are the first 10 days after the counter starts reporting and both read 0 together (Box 9), indicating it was not yet counting properly. |
| North Brisbane pedestrians: on-and-off counter fault | 29 Dec 2014-11 Jul 2015 | Remove the pedestrian values. | 161 of these 195 days are 0 and the median is 0 (maximum 133), compared with a median of 61 a day before the fault (29 Jun-28 Dec 2014) and 63 after it (12 Jul-31 Dec 2015), while cyclists at the same site stayed normal (median 120) (Box 12). |
| North Brisbane cyclists read 0 while pedestrians jump | 6 Feb-8 Mar 2017 | Remove both North Brisbane columns. | Cyclists read 0 from 7 Feb to 7 Mar (84 and 71 on the part-days either side), and over the same period pedestrians jumped to a median of 271, compared with 46-112 in the days either side (Box 12). The pattern is consistent with cyclists being recorded in the pedestrian channel, so both columns are unreliable for this period. |

These decisions follow the checks recommended in the practical: compare with the other counter, look at the line graph and surrounding days, and search the date for events or closures.


## References

The University of Queensland. (2016). *UQ Open Day St Lucia: Sunday 7 August* [Event program]. https://www.readkong.com/page/uq-open-day-st-lucia-sunday-7-august-8523890


## Appendix: S1.T1 Python code

Run each box as its own Jupyter cell, in order.


**Box 1 - Import the libraries**

```python
# Box 1 - Import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```


**Box 2 - Load the raw bikeway data and check its structure**

```python
# Box 2 - Load the raw bikeway data and check its structure
df = pd.read_csv('brisbane_bikeway_counters (1).csv', header=0)
print(df.info())

df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')

print("Shape : ", df.shape)
print("Rows : ", df.shape[0])
print("Columns : ", df.shape[1])
```


**Box 3 - First five rows**

```python
# Box 3 - First five rows
df.head()
```


**Box 4 - Last five rows**

```python
# Box 4 - Last five rows
df.tail()
```


**Box 5 - Reload with Date as the index and get summary statistics (quartiles for the IQR rule)**

```python
# Box 5 - Reload with Date as the index and get summary statistics (quartiles for the IQR rule)
df = pd.read_csv('brisbane_bikeway_counters (1).csv', header=0, index_col='Date')
df.index = pd.to_datetime(df.index)

df.describe()
```


**Box 6 - Part (a): Box plots of daily bikeway usage**

```python
# Box 6 - Part (a): Box plots of daily bikeway usage
fig, axs = plt.subplots(2, 2, figsize=(12, 11))

axs[0, 0].boxplot([df['Bicentennial Bikeway Cyclists'][np.isfinite(df['Bicentennial Bikeway Cyclists'])]])
axs[0, 0].set_title('Bicentennial Bikeway (Brisbane) - Cyclists')
axs[0, 0].set_xlabel('Bicentennial Bikeway cyclists')
axs[0, 0].set_ylabel('Number of users per day')

axs[0, 1].boxplot([df['Bicentennial Bikeway Pedestrians'][np.isfinite(df['Bicentennial Bikeway Pedestrians'])]])
axs[0, 1].set_title('Bicentennial Bikeway (Brisbane) - Pedestrians')
axs[0, 1].set_xlabel('Bicentennial Bikeway pedestrians')
axs[0, 1].set_ylabel('Number of users per day')

axs[1, 0].boxplot([df['North Brisbane Bikeway Cyclists'][np.isfinite(df['North Brisbane Bikeway Cyclists'])]])
axs[1, 0].set_title('North Brisbane Bikeway (Windsor) - Cyclists')
axs[1, 0].set_xlabel('North Brisbane Bikeway cyclists')
axs[1, 0].set_ylabel('Number of users per day')

axs[1, 1].boxplot([df['North Brisbane Bikeway Pedestrians'][np.isfinite(df['North Brisbane Bikeway Pedestrians'])]])
axs[1, 1].set_title('North Brisbane Bikeway (Windsor) - Pedestrians')
axs[1, 1].set_xlabel('North Brisbane Bikeway pedestrians')
axs[1, 1].set_ylabel('Number of users per day')

plt.show()
```


**Box 7 - Part (b): Line graph of daily bikeway usage**

```python
# Box 7 - Part (b): Line graph of daily bikeway usage
df[['Bicentennial Bikeway Cyclists', 'Bicentennial Bikeway Pedestrians', 'North Brisbane Bikeway Cyclists', 'North Brisbane Bikeway Pedestrians']].plot(kind='line', title='Daily cyclist and pedestrian counts, 2014-2018')
plt.xlabel('Date')
plt.ylabel('Number of users per day')
plt.legend()
plt.show()
```


**Box 8 - Part (c): Missing values in each column**

```python
# Box 8 - Part (c): Missing values in each column
print('Bicentennial Bikeway Pedestrians - missing days')
print(df[np.isnan(df['Bicentennial Bikeway Pedestrians'])])
print(df[np.isnan(df['Bicentennial Bikeway Pedestrians'])].shape)

print('Bicentennial Bikeway Cyclists - missing days')
print(df[np.isnan(df['Bicentennial Bikeway Cyclists'])])
print(df[np.isnan(df['Bicentennial Bikeway Cyclists'])].shape)

print('North Brisbane Bikeway Pedestrians - missing days')
print(df[np.isnan(df['North Brisbane Bikeway Pedestrians'])])
print(df[np.isnan(df['North Brisbane Bikeway Pedestrians'])].shape)

print('North Brisbane Bikeway Cyclists - missing days')
print(df[np.isnan(df['North Brisbane Bikeway Cyclists'])])
print(df[np.isnan(df['North Brisbane Bikeway Cyclists'])].shape)
```


**Box 9 - Part (c): Start and end of each missing period**

```python
# Box 9 - Part (c): Start and end of each missing period
print('Bicentennial: missing 9-31 Mar 2016')
print(df.iloc[797:822, :])

print('Bicentennial: zeros from 26 Mar 2017, then missing from 27 Apr 2017')
print(df.iloc[1178:1214, :])

print('Bicentennial: missing period ends 27 Jun 2017')
print(df.iloc[1270:1276, :])

print('Bicentennial: missing 27 Jul-5 Aug 2017')
print(df.iloc[1302:1314, :])

print('North Brisbane: missing until 18 Jun 2014, then zeros 19-28 Jun 2014')
print(df.iloc[165:182, :])

print('North Brisbane: pedestrians zero 11 Jun-2 Jul 2018; cyclists zero 1-2 Jul; both missing 3 Jul')
print(df.iloc[1620:1646, :])
```


**Box 10 - Part (c): Zero counts in each column**

```python
# Box 10 - Part (c): Zero counts in each column
print('Bicentennial Bikeway Pedestrians - zero days')
print(df[df['Bicentennial Bikeway Pedestrians'] == 0])
print(df[df['Bicentennial Bikeway Pedestrians'] == 0].shape)

print('Bicentennial Bikeway Cyclists - zero days')
print(df[df['Bicentennial Bikeway Cyclists'] == 0])
print(df[df['Bicentennial Bikeway Cyclists'] == 0].shape)

print('North Brisbane Bikeway Pedestrians - zero days')
print(df[df['North Brisbane Bikeway Pedestrians'] == 0])
print(df[df['North Brisbane Bikeway Pedestrians'] == 0].shape)

print('North Brisbane Bikeway Cyclists - zero days')
print(df[df['North Brisbane Bikeway Cyclists'] == 0])
print(df[df['North Brisbane Bikeway Cyclists'] == 0].shape)
```


**Box 11 - Part (c): Bicentennial Bikeway fault periods**

```python
# Box 11 - Part (c): Bicentennial Bikeway fault periods
print('Bicentennial pedestrians: zeros start 2 Dec 2014')
print(df.iloc[332:338, :])

print('Bicentennial pedestrians: odd values on 22-23 Dec 2014')
print(df.iloc[353:359, :])

print('Bicentennial pedestrians: zeros end 19 Jan 2015, multiples of 128 from 20 Jan to 5 Feb 2015')
print(df.iloc[378:402, :])

print('Bicentennial cyclists: undercount starts 30 Sep 2014')
print(df.iloc[268:277, :])

print('Bicentennial cyclists: near-zero counts end 28 Dec 2014, then stay below normal')
print(df.iloc[357:366, :])

bc_fault = df.iloc[272:362, :]
print('Bicentennial cyclists, 30 Sep-28 Dec 2014')
print(bc_fault[['Bicentennial Bikeway Cyclists']].describe())

bc_partial = df.iloc[362:438, :]
print('Bicentennial cyclists, 29 Dec 2014-14 Mar 2015 (partial recovery)')
print(bc_partial[['Bicentennial Bikeway Cyclists']].describe())

print('Bicentennial cyclists: zeros start 15 Mar 2015')
print(df.iloc[435:441, :])

print('Bicentennial cyclists: zeros end 30 May 2015')
print(df.iloc[512:518, :])
```


**Box 12 - Part (c): North Brisbane Bikeway fault periods**

```python
# Box 12 - Part (c): North Brisbane Bikeway fault periods
print('North Brisbane pedestrians: fault starts 29 Dec 2014')
print(df.iloc[358:377, :])

print('North Brisbane pedestrians: fault ends 11 Jul 2015')
print(df.iloc[550:560, :])

nb_ped_fault = df.iloc[362:557, :]
print('North Brisbane pedestrians, 29 Dec 2014-11 Jul 2015')
print(nb_ped_fault[['North Brisbane Bikeway Pedestrians']].describe())
print(nb_ped_fault[nb_ped_fault['North Brisbane Bikeway Pedestrians'] == 0].shape)
print('North Brisbane cyclists over the same period')
print(nb_ped_fault[['North Brisbane Bikeway Cyclists']].describe())

print('North Brisbane: pedestrians jump on 6 Feb 2017; cyclists are zero from 7 Feb')
print(df.iloc[1129:1136, :])

print('North Brisbane: cyclists zero until 7 Mar 2017; both normal again from 9 Mar')
print(df.iloc[1158:1165, :])

nb_ped_before = df.iloc[179:362, :]
print('North Brisbane pedestrians before the fault, 29 Jun-28 Dec 2014')
print(nb_ped_before[['North Brisbane Bikeway Pedestrians']].describe())

nb_ped_after = df.iloc[557:730, :]
print('North Brisbane pedestrians after the fault, 12 Jul-31 Dec 2015')
print(nb_ped_after[['North Brisbane Bikeway Pedestrians']].describe())

nb_2017 = df.iloc[1132:1163, :]
print('North Brisbane pedestrians, 6 Feb-8 Mar 2017')
print(nb_2017[['North Brisbane Bikeway Pedestrians']].describe())
```


**Box 13 - Part (c): Outliers using the 1.5 x IQR rule**

```python
# Box 13 - Part (c): Outliers using the 1.5 x IQR rule
# Upper bounds from the quartiles in Box 5 (Q3 + 1.5 x IQR):
# BP upper = 1102 + 1.5*(1102-592) = 1867
# BC upper = 1918.5 + 1.5*(1918.5-654.5) = 3814.5
# NP upper = 120 + 1.5*(120-37) = 244.5
# NC upper = 184 + 1.5*(184-76) = 346
# All lower bounds are negative and the lowest counts are 0, so there are no low outliers.

print('Bicentennial pedestrians above 1867')
print(df[df['Bicentennial Bikeway Pedestrians'] > 1867].shape)
year_2014 = df.iloc[0:365, :]
year_2015 = df.iloc[365:730, :]
year_2016 = df.iloc[730:1096, :]
print(year_2014[year_2014['Bicentennial Bikeway Pedestrians'] > 1867].shape)
print(year_2015[year_2015['Bicentennial Bikeway Pedestrians'] > 1867].shape)
print(year_2016[year_2016['Bicentennial Bikeway Pedestrians'] > 1867])

print('Bicentennial pedestrians above 3000')
print(df[df['Bicentennial Bikeway Pedestrians'] > 3000])

print('Bicentennial cyclists above 3814.5')
print(df[df['Bicentennial Bikeway Cyclists'] > 3814.5])

print('North Brisbane pedestrians above 244.5')
print(df[df['North Brisbane Bikeway Pedestrians'] > 244.5].shape)

print('North Brisbane pedestrians above 500')
print(df[df['North Brisbane Bikeway Pedestrians'] > 500])

print('North Brisbane cyclists above 346')
print(df[df['North Brisbane Bikeway Cyclists'] > 346])
```


**Box 14 - Part (c): Bicentennial Bikeway level change, 2014 vs 2015**

```python
# Box 14 - Part (c): Bicentennial Bikeway level change, 2014 vs 2015
print('Bicentennial Bikeway, 1 Jan-29 Sep 2014')
print(df.iloc[0:272, 0:2].describe())

print('Bicentennial Bikeway, 1 Jun-31 Dec 2015')
print(df.iloc[516:730, 0:2].describe())
```


**Box 15 - Part (c): Values around each outlier**

```python
# Box 15 - Part (c): Values around each outlier
print('3 Aug 2014')
print(df.iloc[211:218, :])

print('21 Mar 2015')
print(df.iloc[441:448, :])

print('7 Aug 2016')
print(df.iloc[946:953, :])

print('17 Oct 2015')
print(df.iloc[651:658, :])

print('10 Jan 2016')
print(df.iloc[734:743, :])

print('23 Oct 2018')
print(df.iloc[1753:1760, :])
```


