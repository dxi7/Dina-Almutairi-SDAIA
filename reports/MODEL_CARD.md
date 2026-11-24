# Model card | Tamweel Lite

## Status
READY_FOR_REVIEW. The quality of the reasoning still needs human review; this is not an automatic grade.

## Purpose and use
This is a fictional training exercise on synthetic data. The flags simulate sending a request to review. It must not be used for real financing, to approve or reject an applicant, or as evidence about real people or regions.

Tamweel Lite data is synthetic; the target is a default event within 90 days of the application. The model uses the 22 features available at application time, with no identifiers, dates or target in the inputs. Training use only: no real financing decisions.

## Data and validation
Fit-and-selection pool: 6576 applications. Calibration period: 836 applications with 78 positives, with its customers held out. Labels must be 90 days mature, and the nested forward OOF keeps customers separate at both levels. Comparison folds are 2023Q1, 2023Q3 and 2024Q1. Rows whose outcomes would not yet have matured are left out, and the most recent training data is not used automatically.

The evidence is nested forward OOF: folds 2023Q1, 2023Q3 and 2024Q1, training far enough in the past for 90-day outcomes to mature, validation customers removed from training, and ensemble weights and the stacker learned on inner OOF only. The limits are that three periods overlap in their training history, so the fold SD (0.030) is descriptive and not a confidence interval, that the AP gaps between candidates are small, and that the same training data was used earlier in the course, so this is not an untouched final test.

## Model selection
KEEP SINGLE / Logistic. Reference fold SD of AP: 0.029808. Full numbers are in `artifacts/ensemble_comparison.csv` and `day5_fold_scores.csv`.

I kept a single model, Logistic Regression. It had the best mean Average Precision across the three forward folds (0.392, fold SD 0.030), ahead of XGBoost (0.353) and LightGBM (0.346). No ensemble beat it: equal averaging scored 0.372 (-0.020), weighted averaging 0.389 (-0.002) and stacking 0.383 (-0.009), so none came close to the required gain of more than 0.030. Brier (0.0633 vs 0.0633) and ECE (0.0188 vs 0.0177) were also no better in a way that would justify the extra complexity. Gate result: KEEP SINGLE.

## Calibration
A sigmoid was learned on the reserved calibration sample. The plot and metrics are fit diagnostics on the rows that taught the calibrator, not independent evidence. No improvement is claimed for the unlabeled challenge set.

The sigmoid was learned on a reserved period (July to September 2024, 836 rows, 78 positives) kept out of the fit pool, but its diagnostics are scored on those same rows, so they are fit diagnostics, not independent evidence. On them the sigmoid left ranking unchanged (AP 0.288, ROC-AUC 0.789) and did not improve calibration (Brier 0.0765 to 0.0781, ECE 0.0211 to 0.0349), which suggests the unweighted logistic scores were already reasonably calibrated. With only 78 positives the estimate is noisy, and no challenge labels exist to test it.

## Policy, capacity and regions
Loss 10 FN + FP. Raw OOF threshold 0.16892161427109176, transported threshold 0.12225843144286948. Batch capacity 300; threshold candidates 330; final flags 300. Equal-score blocks are never split. 1 = a simulated review flag, 0 = flag not raised.

Capacity was applied once to the whole 2,500-request batch: 330 requests were above the transported threshold (0.1223), the 300-request cap kept 300 and removed 30 (boundary score 0.1299), and no equal-score block was split. The regional OOF flag rate among negatives ranges from 6.3% (eastern) to 10.3% (western), a gap of 3.98 percentage points, with 486 to 507 negatives per region. This is a descriptive diagnostic with no confidence interval and is not a fairness certificate; challenge FPR cannot be computed without labels.

## Explanation scope
Day 4 explanations belong to the Day 4 model and are not attributed automatically to this version. A change of model, features or calibration requires rechecking them.

The Day 4 explanations belong to the class-weighted LightGBM of Day 4. The final model is an unweighted Logistic Regression with a sigmoid calibrator, so those SHAP values and reason codes do not transfer to it. For the final model I would need to recheck its own coefficients or SHAP values, the calibration, and the review zone against the 12% capacity before explaining any individual decision.

## Monitoring and limitations
Track feature and score distributions against the training data for drift; the share of requests flagged per period against the 12% capacity; calibration (Brier, ECE and reliability) on each newly labelled period, recalibrating or retraining when it drifts; and the regional flag rate and recall. Because the transported threshold can change flag volume after refitting, capacity must be checked on every new batch before use.

OOF evidence is used for selection, and three periods are not a significance test. The threshold's capacity effect can change when moved to a refitted model. There are no challenge labels, so no performance or fairness claim is made for it. The data does not represent real people or regions.

## Reproducibility
seed=211; trees=80; free CPU. Package versions are in `artifacts/environment.json` and source hashes in `artifacts/day5_run.json`. The model is in `artifacts/final_model`; `inference.predict` returns an ID and a probability, and the policy is applied after the whole batch is collected. `replay_final` reproduces the saved predictions and `rebuild_final` retrains from data. Do not retrain the model after the calibrator is frozen.

## Submission ownership
Complete the earlier days' evidence and the presentation, save the executed notebook, then record your repository SHA and tag in the private submission channel. The course support revision f486fc50dd9ac8403016facc58cf6a62beb4abf4 is not your submission SHA.
