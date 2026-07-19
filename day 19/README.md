# ShopIQ — Customer Churn Prediction

**Individual Machine Learning Project — Module 2, Day 19**
Full Stack AI Developer Internship @ Innolift Ventures
Parent Project: *ShopIQ — Customer Churn & Sentiment Insights Dashboard*

---

## 📌 Problem Statement

E-commerce and subscription businesses lose recurring revenue whenever a customer stops using
their service ("churns"). If a business can flag *which* customers are likely to churn ahead of
time, it can step in with targeted retention offers, support outreach, or discounts before that
customer actually leaves.

This project builds a **binary classification model** that predicts whether a customer will
churn (`Yes`) or stay (`No`), based on their account details, billing history, and the services
they've subscribed to. The trained model will later be integrated into the ShopIQ Flask backend
and surfaced on the React dashboard as a per-customer churn-risk indicator.

## 📊 Dataset Information

| Detail | Value |
|---|---|
| Dataset Name | Telco Customer Churn (IBM Sample Dataset) |
| Dataset Source | [Kaggle — blastchar/telco-customer-churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) |
| Rows | 7,043 |
| Columns | 21 (19 features + `customerID` + target) |
| Target Variable | `Churn` (Yes / No) |
| Missing Values | 11 blank `TotalCharges` entries (all new customers, `tenure = 0`) |

**Feature groups:**
- **Demographics:** gender, SeniorCitizen, Partner, Dependents
- **Account info:** tenure, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges
- **Services subscribed:** PhoneService, MultipleLines, InternetService, OnlineSecurity,
  OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies

## 🎯 Project Objectives

- Understand and document the churn dataset thoroughly (structure, types, missing values, class balance).
- Explore relationships between customer attributes (tenure, contract type, charges, add-on services) and churn.
- Design a preprocessing and modeling plan suited to a moderately imbalanced tabular classification problem.
- Build a model that prioritizes **recall on churned customers**, so at-risk customers aren't missed,
  while keeping false alarms manageable.
- Produce a reusable pipeline that can plug directly into the ShopIQ backend for real-time churn scoring.

## 🛠️ Technologies Used

- **Language:** Python
- **Data handling:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Modeling:** Scikit-learn (Logistic Regression, Random Forest), with Gradient Boosting as a stretch comparison
- **Environment:** Jupyter / Google Colab
- **Version Control:** Git & GitHub

## 🗺️ Planned Workflow

1. **Data Preprocessing** — clean `TotalCharges`, impute missing values, encode categorical
   features (One-Hot), scale numerical features, stratified train/test split.
2. **Feature Engineering** — `AvgMonthlySpend`, tenure buckets, `TotalServicesSubscribed`,
   `IsMonthToMonth` flag.
3. **Modeling** — train Logistic Regression (baseline/interpretable), Random Forest, and
   Gradient Boosting, using `class_weight='balanced'` to address class imbalance.
4. **Evaluation** — compare models on Recall, Precision, F1-score, ROC-AUC, and Confusion Matrix.
5. **Deployment prep** — save the winning pipeline as `.pkl` for backend integration (Day 20 onward).

## 📁 Repository Structure

```
ShopIQ-Churn-Prediction/
├── Dataset/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
├── Notebook/
│   └── ShopIQ_Churn_Project_Day19.ipynb
├── Model/
│   └── (churn_pipeline.pkl — added after training, Day 20)
├── Documentation/
│   └── (supporting docs, screenshots, reports)
└── README.md
```

## ✅ Day 19 Status

Dataset understanding, exploratory data analysis, and full implementation plan are complete
(see `Notebook/ShopIQ_Churn_Project_Day19.ipynb`). Model training and evaluation begin Day 20.

---
*Mohamed Imthiyaz | B.Tech AI & Data Science, BSACIST Chennai | Innolift Ventures Internship*
