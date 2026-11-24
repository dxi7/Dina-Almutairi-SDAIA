# Interpretability report | Tamweel Lite

**Status:** Ready for review; this is not an approval or a grade
**Explanation source:** LIVE | **Model and calibration:** LIVE | **Capacity:** CAPACITY_REVIEW_REQUIRED

## Model and roles
Class-weighted LightGBM, 80 trees. Target: a synthetic default within 90 days. Roles are separated by time and by customer: fit 2516 rows, calibration 584 (40 positives), policy 589, evaluation 1733. Gap periods and overlapping customers are excluded. The evaluation data was seen earlier in the course, so it is not an untouched final test.

## Global and local explanation
Permutation importance measures the Average Precision lost on the evaluation rows when a feature is shuffled. SHAP explains the raw model in log-odds: base value + sum of SHAP = raw margin, and a sigmoid of that sum gives the raw score. The values are not probability points and do not explain the calibrated probability.

Most important feature by mean |SHAP|: **bureau_score** (0.9042 log-odds). Largest held-out AP drop: **bureau_score** (0.1270).

Synthetic request TR-009585: raw score 0.90308, calibrated probability 0.47952. It was chosen as the highest raw score inside the SHAP sample, without using its real outcome.
- bureau_score = 497: Fictional bureau score at application (SHAP +2.2693 log-odds; imputed: False)
- dti = 1.2806: Obligations plus proposed principal-only instalment divided by income (SHAP +1.1981 log-odds; imputed: False)
- loan_amount_sar = 93437.3: Requested principal (SHAP +0.2007 log-odds; imputed: False)

## Calibration
On 1733 rows (139 positives): Brier 0.113027 -> 0.067112; ECE 0.146871 -> 0.022486. AP 0.258677 -> 0.258677 and ROC-AUC 0.770804 -> 0.770804 are unchanged because the mapping is monotone. These are results for this sample, not a promise for the future.

## Stability
200 valid customer-cluster bootstrap replicates, 95% percentile intervals, model and calibrator fixed. They exclude refitting, recalibration and future drift, and do not describe one person's probability. The AP spread between the two evaluation quarters is descriptive only. The bureau_score +/-1 check ran; see day4_local_stability.csv.

## Threshold and review zone
Raw threshold 0.5881953696965011 was chosen on the policy role (loss 10 x FN + FP, 12% capacity) and carried to 0.17331013263107387 on the calibrated scale; it was not adjusted using the evaluation role. The diagnostic band [0.15331, 0.19331] is +/-0.02 and is not a confidence interval; a request is counted once.
- 2024Q3: limit 100, risk flags 97, flags + near threshold 109
- 2024Q4: limit 107, risk flags 109, flags + near threshold 122

If the review set exceeds capacity, document that a new policy must be designed on development data and tested with new evidence. Do not raise the limit or trim cases after seeing the result. SHAP and reason codes describe the model, not causes or fairness. Loss is in teaching units, not money or grade points. This exercise is not for real lending.
