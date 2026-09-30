# S1.T2: Weather Data Inspection - answer text for the report

## (a) Box plots

[Insert Figure 3 here - the output of Box 9]

Figure 3: Box plots of daily rainfall, daily maximum temperature and daily solar exposure, Brisbane, 1 January 2014 to 31 December 2018. Each factor has its own panel and units. Circles are days beyond 1.5 x IQR from the box.

## (b) Line graphs

[Insert Figures 4, 5 and 6 here - the outputs of Boxes 11, 12 and 13]

Figure 4: Daily rainfall, Brisbane, 2014-2018.
Figure 5: Daily maximum temperature, Brisbane, 2014-2018.
Figure 6: Daily solar exposure, Brisbane, 2014-2018.
Gaps in a line are missing days.

## (d) Problematic data and how it will be handled

All date ranges are inclusive. "Interpolate" means filling the gap with a straight line between the readings on either side (Week 7). "Remove" means the value is left as missing and excluded from calculations; it is not replaced with zero. The raw CSV is kept unchanged. Code evidence is in Boxes 15-21 of the appendix.

### Missing data
| Column, problem and value | Date or date range | How it will be handled | Justification |
|---|---|---|---|
| Daily rainfall: missing, 2 days | 30-31 Mar 2017 | Remove; do not impute. | These are the days ex-Tropical Cyclone Debbie hit Brisbane, and the Bureau of Meteorology reports that the city gauge had equipment failures on the 30th (Bureau of Meteorology, 2017). Solar exposure fell to 0.8 MJ/m2 on the 30th (Box 16). The readings either side are 0.0 and 0.2 mm, so interpolation or a mean would record a cyclone as a dry day. |
| Daily rainfall: missing, 3 days (longest rainfall gap) | 19-21 Feb 2018 | Remove; do not impute. | Rain does not change smoothly from day to day, so a line between 0.0 mm (18 Feb) and 0.2 mm (22 Feb) means nothing. Solar exposure was already falling (27.6 to 9.6 MJ/m2) ahead of the 62.8 mm and 135.8 mm storm on 23-24 Feb (Box 16). Rainfall is missing on 39 of 1,826 days (2.1%), under the 5% level where deletion is acceptable. |
| Daily rainfall: missing, 1 day | 14 Feb 2014 | Remove. | The days either side are dry, but solar exposure dipped to 18.7 MJ/m2 that day (Box 16), so rain cannot be ruled out and filling it with 0 would be a guess. Losing one day is negligible. |
| Daily maximum temperature: missing, 1 day | 4 May 2014 | Interpolate between 3 May (21.1 C) and 5 May (22.5 C). | Maximum temperature changes gradually from day to day, so the Week 7 interpolation method for short gaps gives a realistic value. Only 24 of 1,826 days (1.3%) are missing, all in gaps of 1-2 days with readings on both sides (Box 15). |
| Daily maximum temperature: missing, 2 days | 25-26 Feb 2018 | Interpolate between 24 Feb (29.1 C) and 27 Feb (28.5 C). | Short gap with close readings on both sides (Box 16), so interpolation adds very little error and keeps these days for later analysis. |
| Daily maximum temperature: missing, 2 days | 29-30 Oct 2018 | Interpolate between 28 Oct (30.3 C) and 31 Oct (27.0 C). | Same reasoning: a two-day gap in a slowly changing series with valid readings either side (Box 16). |
| Daily solar exposure: missing, 1 day (the only one) | 26 Nov 2017 | Interpolate between 25 Nov (24.2 MJ/m2) and 27 Nov (26.4 MJ/m2). | Dry days either side (0 mm) and a steady maximum temperature of 28.7-29.5 C (Box 16), so a clear-day value in between is realistic. |

### Outliers
1.5 x IQR bounds from describe() (Box 7): rainfall above 1.5 mm; maximum temperature below 15.3 C or above 38.5 C; solar exposure below -0.45 or above 37.55 MJ/m2. Rainfall is very skewed: 1,161 of the 1,787 recorded days have no rain, so Q1 and the median are both 0 and every day above 1.5 mm (338 days) is flagged (Box 18). The IQR rule does not suit rainfall, so these days are checked against the line graph and the other readings instead of being removed as a group. There are no low temperature outliers and no solar outliers by the IQR rule.

| Column, problem and value | Date | How it will be handled | Justification |
|---|---|---|---|
| Daily rainfall: outlier, 182.6 mm | 2 May 2015 | Keep. | A real storm: the Bureau of Meteorology's Brisbane May 2015 summary records 56.2 mm on the 1st and 183 mm on the 2nd, matching this data (Box 19; Bureau of Meteorology, 2015). BOM daily rainfall covers the 24 hours to 9 am, so most of it fell on 1 May, which is why solar exposure on the 2nd looks normal. Heavy-rain days are what the bikeway analysis needs to capture. |
| Daily rainfall: outlier, 135.8 mm | 24 Feb 2018 | Keep. | Second day of a storm (62.8 mm the day before, with solar exposure down to 4.2 MJ/m2) (Box 16). All three readings agree. |
| Daily rainfall: outlier, 110.6 mm | 20 Jun 2016 | Keep. | The surrounding days are cloudy (solar 4.6-13.2 MJ/m2) and cool (maximums 19.0-23.2 C) (Box 19), which fits a winter storm rather than a gauge fault. |
| Daily maximum temperature: outlier, 38.9 C | 16 Nov 2014 | Keep. | Above 38.5 C, but the Bureau of Meteorology's spring 2014 summary reports record spring heat across Brisbane on 15-16 Nov 2014 (Bureau of Meteorology, 2014). The day was dry (0 mm) and sunny (24.3 MJ/m2) (Box 19). |
| Daily maximum temperature: outlier, 38.7 C | 4 Jan 2014 | Keep. | Dry and sunny (30.5 MJ/m2) in a run of hot days (34.5 C the day before) (Box 19). A genuine summer heat day. |
| Daily solar exposure: lowest value, 0.5 MJ/m2 (visible on the line graph, not an IQR outlier) | 16 Dec 2018 | Keep, flagged. | The lowest reading in five years, but rain fell on the day (9.0 mm) and the next (32.6 mm) and the maximum temperature dropped from 31.0 to 25.9 C (Box 19), so all three readings agree it was a very dark, stormy day. The second-lowest, 0.8 MJ/m2 on 30 Mar 2017, is the day of ex-Tropical Cyclone Debbie. |

### Errors
| Column, problem and value | Date or date range | How it will be handled | Justification |
|---|---|---|---|
| Daily rainfall: no errors found | - | No action. | No negative values (Box 21). After the rainfall gaps shown in Box 16, the next readings (15 Feb 2014, 1 Apr 2017, 22 Feb 2018 and 28 Feb 2018) are only 0.0-0.2 mm, so no multi-day total was added into a single day. The very large values match BOM records (see Outliers). |
| Daily maximum temperature: no errors found | - | No action. | No negative values, and every reading lies between 16.1 and 38.9 C (Box 7), which is realistic for Brisbane. |
| Daily solar exposure: no errors found | - | No action. | No negative values, readings lie between 0.5 and 31.5 MJ/m2 (Box 7), and no June or July day has summer-level exposure above 20 MJ/m2 (Box 21). The two very low days are backed up by rain and lower temperatures (see Outliers). |

These decisions follow the checks recommended in the practical: compare each reading with the other weather factors, look at the line graphs and surrounding days, and search the date for known events.

## References
Bureau of Meteorology. (2014). Brisbane in spring 2014. http://www.bom.gov.au/climate/current/season/qld/archive/201411.brisbane.shtml
Bureau of Meteorology. (2015). Brisbane in May 2015. https://www.bom.gov.au/climate/current/month/qld/archive/201505.brisbane.shtml
Bureau of Meteorology. (2017). Brisbane in March 2017. https://www.bom.gov.au/climate/current/month/qld/archive/201703.brisbane.shtml
