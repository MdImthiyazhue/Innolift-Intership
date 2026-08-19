"""
ml/model.py — ShopIQ Churn Prediction module.

Keeps ML logic (loading, preprocessing, inference) completely separate from
the Flask route logic in app.py. app.py only calls predict_churn(); it never
touches the model, scaler, or feature order directly.
"""

import os
import pickle

_MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")

_artifact = None  # populated once by load_model()


class InvalidPredictionInput(Exception):
    """Raised when the input dict is missing fields or has bad values."""
    pass


def load_model():
    """
    Loads the model artifact from disk into memory.
    Called ONCE when the Flask app starts (see app.py), not per-request.
    """
    global _artifact
    with open(_MODEL_PATH, "rb") as f:
        _artifact = pickle.load(f)
    return _artifact


def is_loaded():
    return _artifact is not None


def _validate_and_extract(data):
    if not isinstance(data, dict):
        raise InvalidPredictionInput("Request body must be a JSON object.")

    features = _artifact["features"]
    values = []

    for field in features:
        if field not in data:
            raise InvalidPredictionInput(f"Missing required field: '{field}'.")

        raw = data[field]

        if raw is None or (isinstance(raw, str) and raw.strip() == ""):
            raise InvalidPredictionInput(f"Field '{field}' cannot be empty.")

        try:
            num = float(raw)
        except (TypeError, ValueError):
            raise InvalidPredictionInput(
                f"Field '{field}' must be a number, got: {raw!r}."
            )

        if num < 0:
            raise InvalidPredictionInput(f"Field '{field}' cannot be negative.")

        values.append(num)

    return values


def predict_churn(data):
    """
    Runs inference on a single input dict, e.g.:
    {"tenure_months": 3, "monthly_charges": 95.0, "total_purchases": 2, "support_tickets": 6}

    Returns a dict: {"prediction": "Churn" | "No Churn", "churn_probability": float}
    Raises InvalidPredictionInput if the input is malformed.
    """
    if _artifact is None:
        raise RuntimeError("Model is not loaded. Call load_model() at app startup.")

    values = _validate_and_extract(data)

    model = _artifact["model"]
    scaler = _artifact["scaler"]

    scaled = scaler.transform([values])
    pred = model.predict(scaled)[0]
    proba = model.predict_proba(scaled)[0][1]

    return {
        "prediction": "Churn" if pred == 1 else "No Churn",
        "churn_probability": round(float(proba), 3),
    }
