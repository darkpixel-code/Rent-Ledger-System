import uuid
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Payment Gateway Service")

class PaymentRequest(BaseModel):
    house_id: str
    amount: float
    payment_method: str
    card_number: Optional[str] = None
    upi_id: Optional[str] = None

@app.get("/")
def read_root():
    return {"status": "Payment Gateway Active"}

@app.post("/charge")
def process_charge(payment: PaymentRequest):
    if payment.amount <= 0:
        raise HTTPException(status_code=400, detail="Invalid payment amount")
# ---------------------------------------
# Fake Transaction ID
# ---------------------------------------    
    transaction_id = f"TXN-{uuid.uuid4().hex[:8].upper()}"
    return {
        "status": "SUCCESS",
        "transaction_id": transaction_id,
        "amount": payment.amount,
        "message": "Payment charged successfully"
    }