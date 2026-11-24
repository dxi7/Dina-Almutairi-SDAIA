# Decision card | Tamweel Lite

**Status:** Ready for review; this is not an approval or a grade
**Source:** LIVE | **Strategy:** weighted | **Rows:** 5,039 out-of-fold requests

**Task.** `default_within_90d = 1` is a synthetic default within 90 days of the application. Each fold validates on later requests, removes their customers from training and uses only matured labels.

| Evidence | Value |
|---|---:|
| Capacity-constrained threshold (full precision) | 0.6583471436014694 |
| Unconstrained minimum-loss threshold | 0.44863935722081005 |
| Recall | 40.89% |
| Precision | 29.85% |
| Pooled out-of-fold AP | 0.3100 |
| Flags | 526 of 5,039 |
| FN / FP | 227 / 369 |
| Teaching loss | 2639 units |
| Loss at 0.5 | 2403 units; within capacity: False |
| Change versus 0.5 | +236 units (positive = more loss) |
| False-positive-rate gap between regions | 0.648 percentage points |

**Rule.** Score >= 0.6583471436014694 means "send to review" inside this exercise. It is not an approval or a rejection. Keep the full precision: rounding the threshold can change the queue size.

**Policy.** FN = 10 and FP = 1 teaching units; capacity 12% per period, rounded down. These are not riyals, tool fees or grade deductions.

**Capacity evidence.** period 1: 137/195, period 2: 183/200, period 3: 206/207.

**Limits.** Out-of-fold predictions cover 50.39% of the training data (4,961 warm-up rows have no prediction). The threshold and its loss are estimated on the same out-of-fold outcomes, so this is a development result, not a final test. The challenge file was not used. Regional comparisons are descriptive and are not a fairness certificate; class weights do not make scores calibrated.

Evidence files: `artifacts/threshold_metrics.json`, `day3_period_capacity.csv`, `day3_region_audit.csv`, `day3_cost_sensitivity.csv`, `cost_curve.png`. Sensitivity rows are +/-20% scenarios for the miss cost, not confidence intervals.
