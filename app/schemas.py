from datetime import date
from pydantic import BaseModel, Field

# --- INVOICE SCHEMAS ---
class InvoiceCreate(BaseModel):
    customer_id: str
    amount: float = Field(..., gt=0, description="Amount must be greater than 0")
    due_date: date

class InvoiceResponse(InvoiceCreate):
    id: int

    class Config:
        from_attributes = True


# --- PAYMENT SCHEMAS ---
class PaymentCreate(BaseModel):
    customer_id: str
    amount: float = Field(..., gt=0, description="Amount must be greater than 0")
    payment_date: date

class PaymentResponse(PaymentCreate):
    id: int

    class Config:
        from_attributes = True


# --- STATEMENT SCHEMAS ---
class StatementLineItem(BaseModel):
    date: date
    type: str  # "INVOICE", "PAYMENT" or "LATE_FEE"
    description: str
    amount: float
    running_balance: float

class StatementResponse(BaseModel):
    customer_id: str
    as_of_date: date
    total_balance_due: float
    statement: list[StatementLineItem]