# Machine Learning — Interview Notes

Status: **L1–L3 done. RESUME at L4 (classification metrics).** Plain-text math only.
Full topic list: `SYLLABUS.md` (CampusX 100 Days). Answer in 3 beats.

## L1 — Types of ML + Bias-Variance
- **Supervised:** labeled data → learn input→output (regression, classification).
- **Unsupervised:** no labels → find structure (clustering, dimensionality reduction).
- **Reinforcement:** agent takes actions in an environment, gets rewards, learns a policy by trial and error.
- **Bias** = model too simple → underfit → bad on BOTH train and test.
- **Variance** = model too complex → overfit → great on train, bad on test.
- Goal = sweet spot minimizing total error. (Note: "bias" here is NOT the `b` intercept in y=mx+b.)

## L2 — Regression metrics
- **MAE** = (1/n) Σ|y − ŷ|. Avg error magnitude, robust to outliers, same units.
- **MSE** = (1/n) Σ(y − ŷ)². Squares errors → penalizes large ones, smooth → used as training loss.
- **RMSE** = √MSE. Same units as target, readable; still outlier-sensitive.
- **R²** = 1 − SS_res/SS_tot. How much better than predicting the mean (1 = perfect, 0 = no better than mean, <0 = worse).
- Use MAE when outliers shouldn't dominate; MSE/RMSE when big errors must be punished.

## L3 — Regularization
- Adds a weight penalty to the loss → shrinks weights → smoother function → lower variance/overfitting.
- **Ridge (L2):** MSE + λΣw². Shrinks weights toward 0, keeps all features. Gradient 2λw fades near 0 (never exactly 0).
- **Lasso (L1):** MSE + λΣ|w|. Constant ±λ gradient drives weights exactly to 0 → feature selection / sparsity.
- **ElasticNet:** both penalties combined.
- High λ → penalty dominates the loss → underfit. Low λ → barely regularizes. Tune λ via cross-validation.

## L4 — Classification metrics (RESUME / review)
- **Confusion matrix:** TP, FP (Type I, false alarm), FN (Type II, miss), TN.
- **Accuracy** = (TP+TN)/all — misleading on imbalanced data.
- **Precision** = TP/(TP+FP) — of predicted positives, how many were right. (Care when false positives are costly.)
- **Recall (sensitivity)** = TP/(TP+FN) — of actual positives, how many you caught. (Care when misses are costly, e.g. disease.)
- **F1** = 2·P·R/(P+R) — harmonic mean, balances P and R.
- **ROC-AUC:** TPR vs FPR across thresholds; AUC = ranking quality, threshold-independent.

## Still to cover (per SYLLABUS.md)
Feature scaling (standardize/normalize), encoding, decision trees (entropy/gini/info-gain), bagging/random forest, boosting (AdaBoost/GradientBoosting/XGBoost), gradient descent (batch/SGD/mini-batch), logistic regression + sigmoid + BCE, SVM + kernel trick, naive bayes, KNN, K-means/DBSCAN/hierarchical clustering, PCA, imbalanced data (SMOTE), cross-validation, hyperparameter tuning.

## Quick recall (high-yield)
- **Why scale features?** Distance/gradient-based models (KNN, SVM, linear+GD, PCA) are scale-sensitive; trees are not.
- **Bagging vs boosting:** bagging = parallel, independent models on bootstrap samples → reduces variance (Random Forest). Boosting = sequential, each model fixes prior errors → reduces bias (AdaBoost/XGBoost).
- **Decision tree split:** pick the feature/threshold that maximizes information gain (entropy drop) or Gini decrease.
- **Cross-validation:** k-fold → train on k−1, validate on 1, rotate → robust estimate, used to tune hyperparameters.
- **Imbalanced data:** resample (SMOTE oversample / undersample), class weights, use precision/recall/F1/AUC not accuracy.
