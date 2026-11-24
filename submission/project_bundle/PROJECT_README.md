# Tamweel Lite | final project

## Executive summary
We chose a single Logistic Regression because it had the best mean Average Precision (0.392) across three forward folds, and no ensemble beat it by more than the 0.030 fold SD. Probabilities were calibrated with a sigmoid and the 12% capacity was applied once to the challenge batch (300 flags of 2,500 requests). The data are synthetic and the results are for training only.

## الملخص التنفيذي
اخترنا نموذج Logistic Regression منفرداً لأنه حقق أعلى متوسط Average Precision (0.392) عبر الطيات الأمامية الثلاث، ولم يتجاوزه أي تجميع بالقدر المطلوب (أكثر من 0.030). عُيّرت الاحتمالات بتحويل sigmoid، وطُبقت سعة 12% مرة واحدة على دفعة التحدي (300 إشارة من 2,500 طلب). البيانات اصطناعية والنتائج للتدريب فقط.

Decision: KEEP SINGLE / Logistic. Full-batch flags: 300/2500.

Read `reports/MODEL_CARD.md` and the policy in `artifacts/final_policy.json`. This bundle is for training; it is not a final evaluation result or proof of submission. Merge your earlier daily evidence and save the executed notebook and the presentation.
