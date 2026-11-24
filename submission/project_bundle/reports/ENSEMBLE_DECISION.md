# Ensemble decision

KEEP SINGLE: Logistic

I kept a single model, Logistic Regression. It had the best mean Average Precision across the three forward folds (0.392, fold SD 0.030), ahead of XGBoost (0.353) and LightGBM (0.346). No ensemble beat it: equal averaging scored 0.372 (-0.020), weighted averaging 0.389 (-0.002) and stacking 0.383 (-0.009), so none came close to the required gain of more than 0.030. Brier (0.0633 vs 0.0633) and ECE (0.0188 vs 0.0177) were also no better in a way that would justify the extra complexity. Gate result: KEEP SINGLE.

The evidence is nested forward OOF: folds 2023Q1, 2023Q3 and 2024Q1, training far enough in the past for 90-day outcomes to mature, validation customers removed from training, and ensemble weights and the stacker learned on inner OOF only. The limits are that three periods overlap in their training history, so the fold SD (0.030) is descriptive and not a confidence interval, that the AP gaps between candidates are small, and that the same training data was used earlier in the course, so this is not an untouched final test.

Evidence: `artifacts/ensemble_comparison.csv` and `day5_ensemble_gate.json`. The SD is descriptive, not a significance test.
