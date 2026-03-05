from pydantic import BaseModel

class Transaction(BaseModel):
    amount: float
    transaction_type: int
    account_age_days: int
    location_risk: int