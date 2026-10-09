#!/usr/bin/env python3
"""Verify the descriptive statistics and paired t-test reported for Table 6."""
from pathlib import Path
import csv
import statistics
from scipy import stats

DATA = Path(__file__).resolve().parents[1] / "data" / "experimental" / "self_optimization_table6.csv"
fixed=[]; mod=[]
with DATA.open(newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        fixed.append(float(row["fixed_speed_operating_time_min"]))
        mod.append(float(row["modulated_speed_operating_time_min"]))
diff=[b-a for a,b in zip(fixed,mod)]
mean_fixed=statistics.mean(fixed)
mean_mod=statistics.mean(mod)
mean_diff=statistics.mean(diff)
sd_diff=statistics.stdev(diff)
t,p=stats.ttest_rel(mod,fixed)
sem=stats.sem(diff)
ci=stats.t.interval(0.95, len(diff)-1, loc=mean_diff, scale=sem)
relative=100.0*mean_diff/mean_fixed
print(f"n={len(diff)}")
print(f"fixed mean={mean_fixed:.3f} min")
print(f"modulated mean={mean_mod:.3f} min")
print(f"mean difference={mean_diff:.3f} min")
print(f"SD difference={sd_diff:.3f} min")
print(f"relative improvement={relative:.3f}%")
print(f"paired t({len(diff)-1})={t:.4f}, p={p:.8f}")
print(f"95% CI=({ci[0]:.3f}, {ci[1]:.3f}) min")
