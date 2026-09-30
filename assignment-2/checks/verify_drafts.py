"""Recompute the key figures quoted in the Assignment 2 drafts and assert that they match.

Run from anywhere:  python assignment-2/checks/verify_drafts.py
Requires pandas and numpy.
"""
from pathlib import Path

import numpy as np
import pandas as pd

DATA = Path(__file__).resolve().parent.parent / "data"

raw = pd.read_csv(DATA / "brisbane_bikeway_counters.csv", index_col="Date", parse_dates=True)
clean = pd.read_csv(DATA / "brisbane_bikeway_counters_cleaned.csv", index_col="Date", parse_dates=True)
wx = pd.read_csv(DATA / "brisbane_weather.csv", index_col="Date", parse_dates=True)
BP, BC, NP, NC = raw.columns
R, S, T = wx["daily_rainfall"], wx["solar_exposure"], wx["maximum_temperature"]

checks = []


def check(label, got, expected, tol=0.0):
    got = got.item() if hasattr(got, "item") else got
    ok = abs(got - expected) <= tol if isinstance(expected, (int, float)) else got == expected
    checks.append(ok)
    print(f"{'OK  ' if ok else 'FAIL'} {label}: got {got!r}, draft says {expected!r}")


def upper(s):
    q1, q3 = s.quantile(0.25), s.quantile(0.75)
    return q3 + 1.5 * (q3 - q1)


print("== S1.T1 bikeways (raw file)")
check("rows", len(raw), 1826)
check("Bicentennial days missing", int((raw[BP].isna() | raw[BC].isna()).sum()), 95)
check("North Brisbane days missing", int((raw[NP].isna() | raw[NC].isna()).sum()), 170)
check("Bicentennial 26 Mar-26 Apr 2017 all zero", bool((raw.loc["2017-03-26":"2017-04-26", [BP, BC]] == 0).all(axis=None)), True)
check("IQR upper BP", upper(raw[BP]), 1867)
check("IQR upper BC", upper(raw[BC]), 3814.5)
check("IQR upper NP", upper(raw[NP]), 244.5)
check("IQR upper NC", upper(raw[NC]), 346)
check("BC 3 Aug 2014", raw.loc["2014-08-03", BC], 2786)
check("BP 21 Mar 2015", raw.loc["2015-03-21", BP], 6827)
check("BP 7 Aug 2016", raw.loc["2016-08-07", BP], 3328)
check("NP 17 Oct 2015", raw.loc["2015-10-17", NP], 546)
check("NP 10 Jan 2016", raw.loc["2016-01-10", NP], 670)
check("NC 23 Oct 2018", raw.loc["2018-10-23", NC], 365)
check("BP days > 1867", int((raw[BP] > 1867).sum()), 220)
check("NP days > 244.5", int((raw[NP] > 244.5).sum()), 58)
check("BP mean 1 Jan-29 Sep 2014", round(raw.loc["2014-01-01":"2014-09-29", BP].mean()), 1711)
check("BC mean 1 Jun-31 Dec 2015", round(raw.loc["2015-06-01":"2015-12-31", BC].mean()), 1582)
dec_jan = raw.loc["2014-12-02":"2015-01-19", BP]
check("BP zero days 2 Dec 2014-19 Jan 2015 (of 49)", int((dec_jan == 0).sum()), 46)
check("BP 20 Jan-5 Feb 2015 all multiples of 128", bool((raw.loc["2015-01-20":"2015-02-05", BP] % 128 == 0).all()), True)
check("BC median 30 Sep-28 Dec 2014", raw.loc["2014-09-30":"2014-12-28", BC].median(), 23.5)
check("BC zero run 15 Mar-30 May 2015 (77 days)", bool((raw.loc["2015-03-15":"2015-05-30", BC] == 0).all()), True)
nb_fault = raw.loc["2014-12-29":"2015-07-11", NP]
check("NP zero days 29 Dec 2014-11 Jul 2015 (of 195)", int((nb_fault == 0).sum()), 161)
check("NP median 6 Feb-8 Mar 2017", raw.loc["2017-02-06":"2017-03-08", NP].median(), 271)
check("NC median 9 Nov-31 Dec 2018", raw.loc["2018-11-09":"2018-12-31", NC].median(), 32)

print("\n== S1.T2 weather (raw file)")
check("rainfall days missing", int(R.isna().sum()), 39)
check("max temperature days missing", int(T.isna().sum()), 24)
check("solar days missing", int(S.isna().sum()), 1)
check("rain days recorded as 0", int((R == 0).sum()), 1161)
check("rain days > 1.5 mm", int((R > 1.5).sum()), 338)
check("IQR upper max temperature", round(upper(T), 2), 38.5)
check("rain 2 May 2015", R["2015-05-02"], 182.6)
check("rain 24 Feb 2018", R["2018-02-24"], 135.8)
check("rain 20 Jun 2016", R["2016-06-20"], 110.6)
check("max temperature 16 Nov 2014", T["2014-11-16"], 38.9)
check("max temperature 4 Jan 2014", T["2014-01-04"], 38.7)
check("solar 16 Dec 2018", S["2018-12-16"], 0.5)
check("solar 30 Mar 2017", S["2017-03-30"], 0.8)

print("\n== S2 correlation (supplied cleaned file)")


def r(d, x=NC, y=BP):
    return round(float(np.corrcoef(d[x], d[y])[0, 1]), 3)


check("cleaned rows", len(clean), 1461)
check("r, NC vs BP, all days", r(clean), -0.028)
check("r, before 1 Jun 2015", r(clean.loc[:"2015-05-31"]), 0.469)
check("r, from 1 Jun 2015", r(clean.loc["2015-06-01":]), 0.216)
check("r, 2017", r(clean.loc["2017"]), 0.109)
check("r, 2015", r(clean.loc["2015"]), 0.382)
check("r, row (a) BP vs BC", r(clean, BP, BC), -0.355)
check("zero BP days in cleaned file", int((clean[BP] == 0).sum()), 72)
check("zero NC days in cleaned file", int((clean[NC] == 0).sum()), 40)

print(f"\n{sum(checks)}/{len(checks)} checks passed")
raise SystemExit(0 if all(checks) else 1)
