import joblib
import numpy as np
import os

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "../ml/model.pkl"
)

model = joblib.load(MODEL_PATH)


def predict_fraud(transaction):

    features = np.array([[
        transaction.amount,
        transaction.transaction_type,
        transaction.account_age_days,
        transaction.location_risk
    ]])

    score = model.predict_proba(features)[0][1]

    return {
        "fraud_probability": float(score),
        "status": "BLOCKED" if score > 0.8 else "APPROVED"
    }