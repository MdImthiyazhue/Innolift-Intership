"""
ShopIQ Churn Prediction — Phase 2 Model
Day 46 - Task 01: Verify the model works standalone before integrating with Flask.

This regenerates the trained model artifact (model.pkl) used by ml/model.py.
Run once: python train_model.py
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import pickle
import os

RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)

# ---------------------------------------------------------------------------
# Synthetic customer dataset shaped like the ShopIQ churn dataset:
# tenure_months, monthly_charges, total_purchases, support_tickets -> churn (0/1)
# ---------------------------------------------------------------------------
n = 1000
tenure_months = np.random.randint(1, 72, n)
monthly_charges = np.round(np.random.uniform(15, 120, n), 2)
total_purchases = np.random.randint(0, 50, n)
support_tickets = np.random.randint(0, 10, n)

# Churn probability rises with high charges + low tenure + many support tickets
churn_score = (
    -0.04 * tenure_months
    + 0.02 * monthly_charges
    + 0.35 * support_tickets
    - 0.05 * total_purchases
    + np.random.normal(0, 1.5, n)
)
churn = (churn_score > np.percentile(churn_score, 70)).astype(int)

df = pd.DataFrame({
    "tenure_months": tenure_months,
    "monthly_charges": monthly_charges,
    "total_purchases": total_purchases,
    "support_tickets": support_tickets,
    "churn": churn,
})

FEATURES = ["tenure_months", "monthly_charges", "total_purchases", "support_tickets"]
X = df[FEATURES]
y = df["churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=RANDOM_STATE, stratify=y
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = RandomForestClassifier(n_estimators=100, max_depth=6, random_state=RANDOM_STATE)
model.fit(X_train_scaled, y_train)

# ---- Task 01: verify the model works standalone before touching Flask ----
preds = model.predict(X_test_scaled)
acc = accuracy_score(y_test, preds)
print(f"Standalone verification — test accuracy: {acc:.3f}")

sample = pd.DataFrame([{
    "tenure_months": 3,
    "monthly_charges": 95.0,
    "total_purchases": 2,
    "support_tickets": 6,
}])
sample_scaled = scaler.transform(sample[FEATURES])
sample_pred = model.predict(sample_scaled)[0]
sample_proba = model.predict_proba(sample_scaled)[0][1]
print(f"Sample input: {sample.to_dict('records')[0]}")
print(f"Sample prediction: {'Churn' if sample_pred == 1 else 'No Churn'} (probability: {sample_proba:.3f})")

# ---------------------------------------------------------------------------
# Save the model + scaler + feature order together as one artifact
# ---------------------------------------------------------------------------
os.makedirs(os.path.dirname(__file__), exist_ok=True)
artifact = {"model": model, "scaler": scaler, "features": FEATURES}

with open(os.path.join(os.path.dirname(__file__), "model.pkl"), "wb") as f:
    pickle.dump(artifact, f)

print("Model saved to ml/model.pkl")
