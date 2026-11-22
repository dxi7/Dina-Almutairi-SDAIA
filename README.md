Tamweel | SDAIA

## Daily answers | الإجابات اليومية

### Day 1 | اليوم الأول

**Initial candidate: Logistic Regression.**

**Strongest evidence:** On the 2,000 untouched comparison rows, Logistic Regression had the best ROC-AUC (0.821, against 0.812 for XGBoost and 0.814 for LightGBM) and a practically tied Average Precision (0.326 vs 0.334 and 0.325, with a 7.9% prevalence baseline). It also trained in 0.04 s versus 0.38 s (XGBoost) and 0.24 s (LightGBM). A paired bootstrap shows no clear statistical difference between the models (every 95% confidence interval for the difference versus Logistic Regression includes 0). Therefore, the boosters have not yet demonstrated a meaningful performance gain that justifies their extra complexity.

**Limitation:** This is one random split; 1,226 customers appear on both the development and comparison sides, and time is ignored, so the scores may be optimistic and the ranking may change under more robust validation.

**Next test (Day 2):** Customer-grouped, time-ordered validation that respects target maturity.
