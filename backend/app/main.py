from fastapi import FastAPI
from .schemas import Transaction
from .fraud_model import predict_fraud

app = FastAPI(title="Fraud Detection API")

@app.get("/")
def root():
    return {"message": "Fraud Detection API running"}

@app.post("/predict")
def predict(transaction: Transaction):
    return predict_fraud(transaction)