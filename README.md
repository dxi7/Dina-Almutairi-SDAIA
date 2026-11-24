# Tamweel | SDAIA

Credit-risk modelling project. The task is to predict whether a synthetic loan applicant defaults within 90 days of applying (`default_within_90d`), using only information that exists at application time.

All records are synthetic. Nothing in this repository is real customer data, and none of the results are deployment evidence.

## Repository structure

```text
.
├── README.md                              Project overview and daily answers
├── notebooks/
│   ├── 01_baseline_boosting.ipynb         Day 1: model comparison
│   ├── 02_validation_tuning.ipynb         Day 2: honest validation and tuning
│   ├── 03_cost_sensitive_decision.ipynb  Day 3: threshold, cost and capacity
│   ├── 04_explain_calibrate.ipynb        Day 4: explanation and calibration
│   └── 05_final_model.ipynb              Day 5: final model and delivery
└── artifacts/                             Generated evidence files by day
```

## Day 1 - Baseline vs. boosting

Three models (Logistic Regression, XGBoost, LightGBM) are trained on the same development rows. The tree counts of the two boosters are chosen on an inner stopping split, and all three models are scored once on 2,000 untouched comparison rows.

| Model | ROC-AUC | Average Precision | Train time | Trees |
|---|---:|---:|---:|---:|
| Logistic Regression | 0.821 | 0.326 | 0.04 s | - |
| XGBoost | 0.812 | 0.334 | 0.38 s | 61 |
| LightGBM | 0.814 | 0.325 | 0.24 s | 41 |

The positive rate is 7.9%. A paired bootstrap (1,000 draws) shows that the differences between the models are within noise.

**Boundary:** the Day 1 split is random and stratified. It is a teaching baseline only: the same customer can appear on both sides of the split (1,226 customers do) and time is ignored.

## Day 2 - Honest validation and tuning

* The audit removes two post-outcome fields (`days_past_due_60`, `collection_calls`) and checks for duplicate events (none found).
* Three forward folds train only on mature labels (application date + 90 days < validation start) and remove each fold's validation customers from its training rows.
* A bounded Optuna search (at most 8 trials, 120 s) runs on a separate older cohort and is frozen before any outer result is read.

| Protocol | ROC-AUC (mean of 3 folds) | AP (mean of 3 folds) | Rows scored |
|---|---:|---:|---:|
| Leaky random control (unsafe) | 0.9999 | 0.9988 | 10,000 |
| Clean random control (unsafe) | 0.801 | 0.311 | 10,000 |
| Honest, fixed 80 trees | 0.798 | 0.315 | 5,039 |
| Honest, reserved search | 0.786 | 0.313 | 5,039 |

Every fold has 0 shared customers. Out-of-fold predictions cover 5,039 requests (50.39% of the data); the remaining 4,961 warm-up rows have no prediction.

**Boundary:** the forward folds describe one scenario (later requests from unseen customers). They are not an independent final test and say nothing about fairness, calibration or operational value.

## Daily answers

### Day 1
**Initial Candidate:** LightGBM.

**Strongest Evidence:** LightGBM achieved a ROC-AUC of 0.814 and Average Precision of 0.325, while training faster than XGBoost. The performance differences between models were not statistically significant, making LightGBM a practical initial choice.

**Limitation & Next Step:** The evaluation used a single random split and did not account for customer overlap or time. Day 2 will use customer-grouped, time-ordered validation for a more reliable assessment.

### Day 2
**Leakage risk:** the fields `days_past_due_60` and `collection_calls` are recorded only after the application, so they leak the outcome. Keeping them inflated AP to 0.9988; the clean random control without them gave 0.311.

**How the validation design prevented it:** I dropped the two leaked fields and checked for duplicate events (none found). I used three time-ordered folds where training labels must be mature (application date + 90 days < validation start), and removed each fold's validation customers from its training rows (0 shared customers). Imputation was learned inside training only, and tuning was done on a separate older cohort before reading any outer result.

**Limitations:** the folds are small and related (5,039 out-of-fold rows, 50.39% coverage), and tuning did not improve performance (AP 0.313 vs 0.315 for the fixed model). These results are not a final independent test.
