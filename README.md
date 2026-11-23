Tamweel | SDAIA

## Daily answers

### Day 1
**Initial Candidate:** LightGBM.

**Strongest Evidence:** LightGBM achieved a ROC-AUC of 0.814 and Average Precision of 0.325, while training faster than XGBoost. The performance differences between models were not statistically significant, making LightGBM a practical initial choice.

**Limitation & Next Step:** The evaluation used a single random split and did not account for customer overlap or time. Day 2 will use customer-grouped, time-ordered validation for a more reliable assessment.

### Day 2
**Leakage Risk:** The fields `days_past_due_60` and `collection_calls` contain post-application information, causing data leakage. Including them inflated AP to 0.9988, while removing them reduced it to 0.311.

**Validation Design:** Removed leakage fields and duplicates, used three time-ordered folds with 90-day label maturity, and ensured no customer overlap. Imputation and tuning were restricted to training data.

**Limitations:** The validation folds are relatively small, and tuning did not improve performance (AP 0.313 vs. 0.315). Results are not yet a final independent test.
