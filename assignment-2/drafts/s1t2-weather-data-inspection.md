# S1.T2: Weather Data Inspection

## (a) Box plots

[Insert Figure 3 here - the output of Box 9]

Figure 3: Box plots of daily rainfall, daily maximum temperature and daily solar exposure, Brisbane, 1 January 2014 to 31 December 2018. Each factor has its own panel and units. Circles are days more than 1.5 x IQR beyond the box.


## (b) Line graphs

[Insert Figures 4, 5 and 6 here - the outputs of Boxes 11, 12 and 13]

Figure 4: Daily rainfall (mm), Brisbane, 1 January 2014 to 31 December 2018.
Figure 5: Daily maximum temperature (°C), Brisbane, 1 January 2014 to 31 December 2018.
Figure 6: Daily solar exposure (MJ/m²), Brisbane, 1 January 2014 to 31 December 2018.
Gaps in a line are missing days. Single-day gaps are too small to see at this scale, so Box 15 lists every missing day.


## (d) Problematic data and how it will be handled
All date ranges are inclusive. "Leave as missing" means the value is treated as missing in the cleaned dataset and left out of calculations; whole rows are not deleted and values are not replaced with zero. "Interpolate" means estimating a missing value from the readings on the days either side, as described in Week 7. The raw CSV is kept unchanged. BOM daily rainfall is the total for the 24 hours to 9 am on the date, and daily maximum temperature is for the 24 hours from 9 am (Bureau of Meteorology, n.d.). Code evidence is in Boxes 15-21 of the appendix.

### Missing data
Rainfall is missing on 39 of 1,826 days (2.1%), maximum temperature on 24 days (1.3%) and solar exposure on 1 day (Box 15). 15 of the 22 maximum-temperature gaps are followed by a rainfall gap the next day (e.g. 3-4 Feb 2015, 5-6 Jan 2016 and 21-22 May 2018). Given the reading times above, this is what one missed 9 am reading would produce, so most gaps look like short weather-station outages rather than faulty values.

| Column, problem and value | Date or date range | How it will be handled | Justification |
|---|---|---|---|
| Daily rainfall: missing, 2 days | 30-31 Mar 2017 | Leave as missing; do not impute. | These are the days ex-Tropical Cyclone Debbie reached Brisbane. The Bureau of Meteorology reports equipment outages at the Brisbane City gauge on the 30th and says the true March total is not known (Bureau of Meteorology, 2017). Solar exposure fell to 0.8 MJ/m² on the 30th (Box 16). The readings either side are 0.0 mm (29 Mar) and 0.2 mm (1 Apr), so interpolation would record a cyclone as a dry day. |
| Daily rainfall: missing, 3 days (the longest rainfall gap) | 19-21 Feb 2018 | Leave as missing; do not impute. | Part of the worst stretch of missing data in the record: rainfall is also missing on 26-27 Feb and 1-2 Mar, and maximum temperature on 18 Feb, 25-26 Feb and 1 Mar, during an unsettled fortnight with 17.0, 62.8 and 135.8 mm days (Box 16). Rain does not change smoothly from day to day, so a straight line between 0.0 mm (18 Feb) and 0.2 mm (22 Feb) would be a guess. With only 2.1% of rainfall days missing, leaving these out loses little data. |
| Daily rainfall: missing, 1 day | 6 Jan 2016 | Leave as missing. | Maximum temperature is also missing on 5 Jan, the missed-reading pattern described above. This reading covers 5 Jan, which was very dark (3.4 MJ/m²) after readings of 8.8 mm and 23.2 mm (Box 16), so rain probably fell and a 0 would be wrong, but the amount cannot be estimated from the days either side. |
| Daily maximum temperature: missing, 1 day | 4 May 2014 | Interpolate between 3 May (21.1 °C) and 5 May (22.5 °C). | Maximum temperature changes gradually, and solar exposure on 4 May (16.3 MJ/m²) was almost the same as on 5 May (16.2), so conditions were steady (Box 16). All 24 missing temperature days are in gaps of 1-2 days with readings on both sides (Box 15), which suits interpolation. |
| Daily maximum temperature: missing, 2 days | 25-26 Feb 2018 | Interpolate between 24 Feb (29.1 °C) and 27 Feb (28.5 °C). | The readings either side differ by only 0.6 °C, and both missing days were fairly sunny (21.9 and 23.8 MJ/m²) (Box 16), so a straight line adds very little error and keeps these days for later analysis. |
| Daily maximum temperature: missing, 2 days | 29-30 Oct 2018 | Leave as missing; do not interpolate. | Unlike the other gaps, conditions changed inside this one: solar exposure fell to 6.5 MJ/m² on the 29th, with 3.6 mm of rain in the 24 hours to 9 am on the 30th (Box 16). The 29th was probably cooler than a straight line from 30.3 °C to 27.0 °C would give, and two days is a negligible loss. |
| Daily solar exposure: missing, 1 day (the only one) | 26 Nov 2017 | Interpolate between 25 Nov (24.2 MJ/m²) and 27 Nov (26.4 MJ/m²). | No rain was recorded on 26 or 27 Nov and the maximum temperature was steady at 28.7-29.5 °C (Box 16), so a clear-day value in between is realistic. |

### Outliers
1.5 x IQR bounds from the quartiles in describe() (Box 7): rainfall above 1.5 mm; maximum temperature below 15.3 °C or above 38.5 °C; solar exposure below -0.45 or above 37.55 MJ/m². Rainfall is heavily skewed: 1,161 of the 1,787 recorded days have no rain, so Q1 and the median are both 0 and all 338 days above 1.5 mm are flagged (Box 18). The IQR rule does not suit rainfall, so the largest falls (four days above 100 mm) were checked against the other readings and BOM records instead of being removed as a group. Maximum temperature has two outliers, both high. Solar exposure has none by the IQR rule, so the two lowest values on the line graph were checked instead.

| Column, problem and value | Date | How it will be handled | Justification |
|---|---|---|---|
| Daily rainfall: outlier, 182.6 mm | 2 May 2015 | Keep. | The Bureau of Meteorology's Brisbane May 2015 summary records 56.2 mm on the 1st and 183 mm on the 2nd, matching this data (Bureau of Meteorology, 2015). This reading covers 9 am on 1 May to 9 am on 2 May, and solar exposure on 1 May was only 3.7 MJ/m² (Box 19), so all three readings are consistent with a real storm. Heavy-rain days are what the bikeway analysis needs to capture. |
| Daily rainfall: outlier, 135.8 mm | 24 Feb 2018 | Keep. | BOM reports severe thunderstorms over Brisbane in the last week of February 2018 and lists 62.8 mm and 136 mm for the 23rd and 24th (Bureau of Meteorology, 2018a), matching this data. Solar exposure on the 23rd was only 4.2 MJ/m² (Box 16). |
| Daily rainfall: outlier, 110.6 mm | 20 Jun 2016 | Keep. | BOM states that Brisbane received 110.6 mm to 9 am on 20 June 2016 (Bureau of Meteorology, 2016), exactly matching this value. Solar exposure on the 19th was 4.6 MJ/m², the lowest that week (Box 19). |
| Daily maximum temperature: outlier, 38.9 °C | 16 Nov 2014 | Keep. | Above the 38.5 °C bound, but BOM reports very hot conditions across the Brisbane metropolitan area on 15-16 Nov 2014, with spring temperature records set at Amberley and Archerfield (Bureau of Meteorology, 2014). The day was dry (0.0 mm) and sunny (24.3 MJ/m²) (Box 19). |
| Daily maximum temperature: outlier, 38.7 °C | 4 Jan 2014 | Keep. | Dry (0.0 mm) and sunny (30.5 MJ/m²), between hot days of 34.5 °C and 33.6 °C (Box 19), which is consistent with a genuine summer heat day. |
| Daily solar exposure: lowest value, 0.5 MJ/m² (inside the IQR bounds; seen on the line graph) | 16 Dec 2018 | Keep. | The lowest reading in five years, but BOM reports that the remnants of ex-Tropical Cyclone Owen brought rain to Brisbane on 15-17 Dec 2018, with 9.0 mm and 32.6 mm on the 16th and 17th (Bureau of Meteorology, 2018b), matching this data. The maximum temperature also fell from 31.0 to 25.9 °C (Box 19). |
| Daily solar exposure: second-lowest value, 0.8 MJ/m² (inside the IQR bounds) | 30 Mar 2017 | Keep. | The day ex-Tropical Cyclone Debbie reached Brisbane (Bureau of Meteorology, 2017). The maximum temperature also dropped from 29.5 to 25.8 °C (Box 16). |

### Errors
| Column, problem and value | Date or date range | How it will be handled | Justification |
|---|---|---|---|
| Daily rainfall: no errors found | - | No action. | No negative values (Box 21). After the rainfall gaps shown in Box 16, the next readings (7 Jan 2016, 1 Apr 2017, 22 Feb 2018, 28 Feb 2018 and 1 Nov 2018) are only 0.0-0.2 mm, so no multi-day total appears to have been added to a single day. The largest values match BOM records (see Outliers). |
| Daily maximum temperature: no errors found | - | No action. | No negative values (Box 21), and every reading lies between 16.1 and 38.9 °C (Box 7), which is realistic for Brisbane. The highest value is supported by BOM (see Outliers). |
| Daily solar exposure: no errors found | - | No action. | No negative values (Box 21), and every reading lies between 0.5 and 31.5 MJ/m² (Box 7), which is realistic for Brisbane. The two lowest days are backed up by rain, lower temperatures and BOM records (see Outliers). |

These decisions follow the checks recommended in the practical: compare each reading with the other weather factors, look at the line graphs and surrounding days, and search the date for known events.

## References
Bureau of Meteorology. (n.d.). Notes to accompany daily weather observations. https://www.bom.gov.au/climate/dwo/IDCJDW0000.shtml
Bureau of Meteorology. (2014). Brisbane in spring 2014. https://www.bom.gov.au/climate/current/season/qld/archive/201411.brisbane.shtml
Bureau of Meteorology. (2015). Brisbane in May 2015. https://www.bom.gov.au/climate/current/month/qld/archive/201505.brisbane.shtml
Bureau of Meteorology. (2016). Brisbane in June 2016. https://www.bom.gov.au/climate/current/month/qld/archive/201606.brisbane.shtml
Bureau of Meteorology. (2017). Brisbane in March 2017. https://www.bom.gov.au/climate/current/month/qld/archive/201703.brisbane.shtml
Bureau of Meteorology. (2018a). Brisbane in February 2018. https://www.bom.gov.au/climate/current/month/qld/archive/201802.brisbane.shtml
Bureau of Meteorology. (2018b). Brisbane in December 2018. https://www.bom.gov.au/climate/current/month/qld/archive/201812.brisbane.shtml
