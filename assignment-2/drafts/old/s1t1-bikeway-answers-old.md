# S1.T1 Bikeway Data Inspection - answer text

## (a) Box plot
Figure 1: Box plots of daily cyclist and pedestrian counts on the Bicentennial Bikeway (Brisbane) and North Brisbane Bikeway (Windsor), 2014-2018 (code: Box 6). Each panel has its own y-axis scale. Circles are days beyond 1.5 x IQR above the box.

## (b) Line graph
Figure 2: Daily cyclist and pedestrian counts, 2014-2018 (code: Box 7). Gaps in a line are missing days; flat lines at zero are periods where a counter recorded nothing.

## (c) Problematic data and handling
All date ranges are inclusive. "Remove" means the values are treated as missing in the cleaned dataset and left out of calculations; they are not replaced with zero. The raw CSV is kept unchanged. Code evidence is in Boxes 8-15 of the appendix.

### Missing data
| Column, problem and value | Date or date range | How it will be handled | Justification |
|---|---|---|---|
| Bicentennial pedestrians and cyclists: missing (NaN), 23 days | 9-31 Mar 2016 | Remove these days; do not impute. | Bicentennial data is missing on 95 of 1,826 days (5.2%), just above the 5% level where deletion is usually safe. Every gap is a long block with no values inside it to interpolate from, and a seasonal mean would fill 23 days with one repeated number and hide the weekday/weekend pattern. |
| Bicentennial pedestrians and cyclists: 32 days of zeros, then 62 days missing | 26 Mar-27 Jun 2017 | Treat as one 94-day outage and remove. | Both counters drop to 0 on the same day and then stop reporting (Box 9). The bikeway was not unused for a month, so the zeros belong to the same outage. 94 days is far too long to reconstruct. |
| Bicentennial pedestrians and cyclists: missing, 10 days | 27 Jul-5 Aug 2017 | Remove. | A July-August seasonal mean was considered, but it would give all 10 days the same value and flatten daily variation. The block is under 1% of the record, so removing it costs little. |
| North Brisbane pedestrians and cyclists: missing, 169 days | 1 Jan-18 Jun 2014 | Remove; North Brisbane analysis starts on 29 Jun 2014. | Both columns are blank from the first date and then start with 10 days of zeros (Box 9), so the counter was not yet operating. North Brisbane is missing on 170 of 1,826 days (9.3%), almost all in this period. There is nothing to impute from. |
| North Brisbane pedestrians and cyclists: 22 days of zeros, then 1 day missing | 11 Jun-3 Jul 2018 | Treat as one 23-day outage and remove. | Both counters read 0 together and then report nothing on 3 Jul (Box 9). Interpolating 3 Jul would rely on 2 Jul, which is itself a faulty zero. |

### Outliers
Upper 1.5 x IQR bounds from describe() (Box 5): Bicentennial pedestrians 1,867, Bicentennial cyclists 3,814.5, North Brisbane pedestrians 244.5, North Brisbane cyclists 346 users per day. All lower bounds are negative, so there are no low outliers.

| Column, problem and value | Date | How it will be handled | Justification |
|---|---|---|---|
| Bicentennial cyclists: outlier, 2,786 | Sun 3 Aug 2014 | Keep. | About 4.8 times the days either side (552-655), while pedestrians dropped to 928 that day (Box 15), which fits a cycling event rather than a counter fault. It sits inside the IQR bound, so it only shows on the line graph. Real peak demand matters for BCC upgrade planning. |
| Bicentennial pedestrians: outlier, 6,827 | Sat 21 Mar 2015 | Keep, flagged. | Above 1,867 but not a multiple of 128, so not part of the January fault. 18-19 Mar were also high (3,722 and 3,312) and the cyclist counter read 0 all week (Box 15), so pedestrian and cyclist traffic cannot be separated. Kept as total path demand, with that limitation noted. |
| Bicentennial pedestrians: outlier, 3,328 | Sun 7 Aug 2016 | Keep. | The only 2016 value above 1,867 (Box 13). Cyclists fell to 720 the same day, so the counter was working. The date was UQ St Lucia Open Day (University of Queensland, 2016), a genuine one-off event, and peak demand is relevant to upgrade planning. |
| North Brisbane pedestrians: outlier, 546 | Sat 17 Oct 2015 | Remove. | The days either side are 28-85 and cyclists did not rise (92) (Box 15). A single pedestrian-only jump with no support from the other counter points to a recording error. |
| North Brisbane pedestrians: outlier, 670 | Sun 10 Jan 2016 | Remove. | The pedestrian counter read 0 on 5-9 and 12 Jan and 5-6 on 11 and 13 Jan while cyclists were normal (Box 15), so it was failing on and off. 670 in the middle of this is not credible. |
| North Brisbane cyclists: outlier, 365 | Tue 23 Oct 2018 | Keep. | Only slightly above 346, and the surrounding weekdays are similar (304, 285, 330) (Box 15). 2018 is the busiest year on this bikeway, so this is normal high use. |

The IQR rule flags 220 Bicentennial pedestrian days, but 147 are in 2014, 72 in 2015 and only 1 in 2016 (Box 13), so most of them reflect an older level rather than individual outliers and they are not removed as a group. From 1 Jan to 29 Sep 2014 pedestrians averaged 1,711 a day and cyclists 654; from 1 Jun to 31 Dec 2015 pedestrians averaged 593 and cyclists 1,582 (Box 14). The combined totals are similar (about 2,370 and 2,170), and the change happens overnight: on 30 May 2015 the counter recorded 1,312 pedestrians and 0 cyclists, and on 1 Jun it recorded 513 pedestrians and 1,709 cyclists (Box 11). This points to the counter changing how it classified users, not a real change in behaviour. These days are kept, the break is noted, and it will be considered when interpreting the Section 2 correlations.

### Errors
| Column, problem and value | Date or date range | How it will be handled | Justification |
|---|---|---|---|
| Bicentennial pedestrians: counter fault (zeros, then values that are all exact multiples of 128) | 2 Dec 2014-5 Feb 2015 | Remove all pedestrian values in this period. | 46 of the 49 days from 2 Dec to 19 Jan are 0 (the exceptions are 90, 2,047 and 256). From 20 Jan to 5 Feb every value is an exact multiple of 128 (e.g. 8,960 = 70 x 128, 12,288 = 96 x 128, 8,064 = 63 x 128), up to six times normal, while cyclists on the same path did not rise and North Brisbane cyclists stayed normal (Box 11). Real counts would not all be multiples of 128, so this is a recording fault, not crowds. |
| Bicentennial cyclists: undercount (median 24 per day) | 30 Sep-28 Dec 2014 | Remove the cyclist values. | Counts fall overnight from about 600-750 to a median of 24 (never above 109 after 30 Sep) while pedestrians stay normal (Box 11). Checking for zeros misses this, but the line graph shows it. From 29 Dec to 14 Mar 2015 counts only partly recover (median 379); those values are kept but noted. |
| Bicentennial cyclists: 77 days of zeros | 15 Mar-30 May 2015 | Remove the cyclist values. | Pedestrians kept recording normally (for example 1,222-2,157 around the start and 1,312-2,023 around the end, Box 11) while cyclists read 0 for 77 days in a row, so the counter was not counting cyclists. Cyclists reappear at 1,709 on 1 Jun. |
| North Brisbane pedestrians and cyclists: 10 days of zeros | 19-28 Jun 2014 | Remove, together with the 169 missing days before them. | These are the first 10 days after the counter starts reporting and both read 0 together (Box 9), so it was not yet counting properly. |
| North Brisbane pedestrians: on-and-off counter fault | 29 Dec 2014-11 Jul 2015 | Remove the pedestrian values. | 161 of these 195 days are 0 and the median is 0 (maximum 133), compared with about 55-65 a day before and after (Box 14), while cyclists at the same site stayed normal (median 120) (Box 12). |
| North Brisbane cyclists read 0 while pedestrians jump | 6 Feb-8 Mar 2017 | Remove both North Brisbane columns. | Cyclists read 0 from 7 Feb to 7 Mar (84 and 71 on the part-days either side), and over the same period pedestrians jumped to a median of 271, compared with 46-112 in the days either side (Box 12). The counter was logging cyclists as pedestrians, so both columns are wrong for this period. |

Shorter zero runs at North Brisbane (for example pedestrians in Jan-Feb 2016) are handled the same way: zeros during a counter fault are removed, not treated as no users. These decisions follow the checks recommended in the practical: compare with the other counter, look at the line graph and surrounding days, and search the date for events or closures.
