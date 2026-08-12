import time
from datetime import date, timedelta
from typing import Optional

import httpx

from fastapi import FastAPI, Depends, Request, Form, Query, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session
from sqlalchemy import func
from sqlalchemy.exc import OperationalError

from app.database import engine, Base, get_db
from app import models
from app.seed import seed_database

app = FastAPI(title="Rent Ledger System")

templates = Jinja2Templates(directory="app/templates")
# -------------------------
# 1 electricity unit = ₹8
# -------------------------
ELECTRIC_RATE_PER_UNIT = 8.0

GATEWAY_URL = "http://payment_gateway:8002/charge"


# ============================================================
# DATABASE INITIALIZATION
# ============================================================

def init_db():
    retries = 5

    while retries > 0:
        try:
            Base.metadata.create_all(bind=engine)

            print(
                "✅ Database connected and tables created successfully!"
            )

            seed_database()

            break

        except OperationalError as e:
            retries -= 1

            print(
                f"⏳ Database not ready yet... "
                f"Retrying in 2 seconds ({retries} retries left)"
            )

            if retries == 0:
                print("❌ Could not connect to the database.")
                raise e

            time.sleep(2)


init_db()


# ============================================================
# ROOT - UI ONLY
# ============================================================
#
# "/" only serves index.html.
#
# ============================================================

@app.get("/", response_class=HTMLResponse)
def home(
    request: Request,
    db: Session = Depends(get_db)
):
    houses = db.query(models.House).all()

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "statement_data": None,
            "search_house": "",
            "search_owner": "",
            "search_date": "",
            "houses": houses
        }
    )


# ============================================================
# GET /tenants/{id}/statement?asOf=YYYY-MM-DD
# ============================================================

@app.get("/tenants/{id}/statement")
def get_tenant_statement(
    id: str,
    as_of: date = Query(..., alias="asOf"),
    db: Session = Depends(get_db)
):
    """
    Returns the tenant ledger statement as of the requested date.

    Example:

    GET /tenants/H101/statement?asOf=2026-08-11
    """
# --------------------------------------------------
# Check the house is registered or not in database
# ---------------------------------------------------

    house = (
        db.query(models.House)
        .filter(
            models.House.house_id == id
        )
        .first()
    )

    if not house:
        raise HTTPException(
            status_code=404,
            detail=(
                f"No registered house found for "
                f"'{id}'. Please check House ID."
            )
        )

    # --------------------------------------------------------
    # INVOICES
    # --------------------------------------------------------

    invoices = (
        db.query(models.Invoice)
        .filter(
            models.Invoice.house_id == id,
            models.Invoice.created_date <= as_of
        )
        .order_by(
            models.Invoice.month_sequence
        )
        .all()
    )

    # --------------------------------------------------------
    # PAYMENTS
    # --------------------------------------------------------

    payments = (
        db.query(models.Payment)
        .filter(
            models.Payment.house_id == id,
            models.Payment.payment_date <= as_of
        )
        .order_by(
            models.Payment.month_sequence
        )
        .all()
    )

    events = []

    # --------------------------------------------------------
    # INVOICE EVENTS + PENALTIES
    # --------------------------------------------------------

    for inv in invoices:

        events.append({
            "date": inv.created_date,
            "type": "INVOICE",
            "description": (
                f"Rent Invoice #{inv.month_sequence} "
                f"(Rent: ₹{inv.rent_amount} + "
                f"Elec: ₹{inv.electric_amount} + "
                f"Water: ₹{inv.water_bill} + "
                f"Maint: ₹{inv.society_maintenance})"
            ),
            "amount": inv.total_invoice_amount
        })

        penalty_date = (
            inv.created_date +
            timedelta(days=7)
        )

        if as_of >= penalty_date:
#--------------------------------------------------------------------
# check how much payment is done before penalty date for that month
#--------------------------------------------------------------------
            paid_before_penalty = sum(
                p.amount_paid
                for p in payments
                if (
                    p.payment_date < penalty_date
                    and getattr(
                        p,
                        "status",
                        "SUCCESS"
                    ) == "SUCCESS"
                )
            )
# ----------------------------------------------------------------------------------------
# If Invoice of that month is not fully paid then penalty = rentamount(f0r that month)/10
# It is not the 10% of total invoice
# ----------------------------------------------------------------------------------------
            if (
                paid_before_penalty
                < inv.total_invoice_amount
            ):

                penalty_amount = (
                    inv.rent_amount * 0.10
                )

                events.append({
                    "date": penalty_date,
                    "type": "PENALTY",
                    "description": (
                        f"10% Overdue Penalty "
                        f"for Invoice #{inv.month_sequence}"
                    ),
                    "amount": penalty_amount
                })

    # --------------------------------------------------------
    # PAYMENT EVENTS
    # --------------------------------------------------------

    for pay in payments:

        pay_status = getattr(
            pay,
            "status",
            "SUCCESS"
        )

        if pay_status == "SUCCESS":

            events.append({
                "date": pay.payment_date,
                "type": "PAYMENT",
                "description": (
                    f"Payment Received "
                    f"#{pay.month_sequence} "
                    f"via {pay.payment_method} "
                    f"(Txn: {pay.transaction_id})"
                ),
                "amount": -pay.amount_paid
            })

        else:

            reason = getattr(
                pay,
                "failure_reason",
                "Transaction Failed"
            )

            events.append({
                "date": pay.payment_date,
                "type": "PAYMENT_FAILED",
                "description": (
                    f"❌ FAILED Payment Attempt "
                    f"#{pay.month_sequence} "
                    f"via {pay.payment_method} "
                    f"(Reason: {reason})"
                ),
                "amount": 0.0
            })

    # --------------------------------------------------------
    # SORT EVENTS WITH DATE
    # Important for Running Ledger
    # --------------------------------------------------------

    events.sort(
        key=lambda x: x["date"]
    )

    running_balance = 0.0
    statement_items = []

    total_invoiced = 0.0
    total_paid = 0.0

    # --------------------------------------------------------
    # RUNNING BALANCE
    # We will process Sorted Event one-by-one
    # --------------------------------------------------------

    for event in events:

        if event["type"] in [
            "INVOICE",
            "PENALTY"
        ]:

            total_invoiced += event["amount"]

        elif event["type"] == "PAYMENT":
# ---------------------------------------------------------------------------------------------------------------------------
#  When the payment status is SUCCESS abs() removes the negative sign from UI because payments are stored as negative ledger 
#  events but total paid should be positive. But, in calculation amount is stored as a negative event.
# ---------------------------------------------------------------------------------------------------------------------------
            total_paid += abs(
                event["amount"]
            )
# -----------------------------------------------------------------------------
# Invoice and penalty increase the balance; payment decreases the balance
# -----------------------------------------------------------------------------
        running_balance += event["amount"]

        statement_items.append({
            "date": event["date"],
            "type": event["type"],
            "description": event["description"],
            "amount": abs(
                event["amount"]
            ),
            "running_balance": round(
                running_balance,
                2
            )
        })

    return {
        "house_id": house.house_id,
        "owner_name": house.owner_name,
        "customer_id": house.house_id,
        "as_of_date": as_of,
        "total_money_to_be_paid": round(
            total_invoiced,
            2
        ),
        "payment_received": round(
            total_paid,
            2
        ),
        "outstanding_balance": round(
            max(0.0, running_balance),
            2
        ),
        "statement": statement_items
    }


# ============================================================
# POST /register-house
# ============================================================

@app.post("/register-house")
def register_house(
    house_id: str = Form(...),
    owner_name: str = Form(...),
    monthly_rent: float = Form(...),
    db: Session = Depends(get_db)
):
    existing = (
        db.query(models.House)
        .filter(
            models.House.house_id == house_id
        )
        .first()
    )

    if existing:
        return HTMLResponse(
            f"<script>"
            f"alert('House {house_id} already exists!');"
            f"window.location.href='/';"
            f"</script>"
        )

    house = models.House(
        house_id=house_id,
        owner_name=owner_name,
        monthly_rent=monthly_rent
    )

    db.add(house)
    db.commit()

    return HTMLResponse(
        "<script>"
        "alert('House Registered Successfully!');"
        "window.location.href='/';"
        "</script>"
    )


# ============================================================
# POST /generate-invoice
# ============================================================

@app.post("/generate-invoice")
def generate_invoice(
    house_id: str = Form(...),
    electric_units: float = Form(...),
    water_bill: float = Form(...),
    is_quarterly_month: bool = Form(False),
    maintenance: Optional[float] = Form(0.0),
    created_date: str = Form(...),
    db: Session = Depends(get_db)
):
    house = (
        db.query(models.House)
        .filter(
            models.House.house_id == house_id
        )
        .first()
    )

    if not house:
        return HTMLResponse(
            f"<script>"
            f"alert('Error: Register house ID "
            f"{house_id} first!');"
            f"window.location.href='/';"
            f"</script>"
        )
# ------------------------------------------------------------------------------------
# We count existing invoices for that house to generate the next invoice sequence
# -------------------------------------------------------------------------------------
    count = (
        db.query(func.count(models.Invoice.id))
        .filter(
            models.Invoice.house_id == house_id
        )
        .scalar()
    )

    next_seq = count + 1

    elec_amount = (
        electric_units *
        ELECTRIC_RATE_PER_UNIT
    )

    maint_amount = (
        (maintenance or 0.0)
        if is_quarterly_month
        else 0.0
    )

    total_amt = (
        house.monthly_rent
        + elec_amount
        + water_bill
        + maint_amount
    )
# ----------------------------------------------------------------------------------------
# We convert the incoming ISO date string into a Python date object before storing it
# ----------------------------------------------------------------------------------------
    c_date = date.fromisoformat(
        created_date
    )

    invoice = models.Invoice(
        house_id=house_id,
        month_sequence=next_seq,
        rent_amount=house.monthly_rent,
        electric_units=electric_units,
        electric_amount=elec_amount,
        water_bill=water_bill,
        society_maintenance=maint_amount,
        total_invoice_amount=total_amt,
        created_date=c_date,
        due_date=c_date + timedelta(days=7)
    )

    db.add(invoice)
    db.commit()

    return HTMLResponse(
        f"<script>"
        f"alert('Invoice #{next_seq} "
        f"generated successfully!');"
        f"window.location.href='/';"
        f"</script>"
    )


# ============================================================
# POST /payments
# ============================================================

@app.post("/payments")
def process_payment(
    house_id: str = Form(...),
    amount: float = Form(...),
    payment_method: str = Form(...),
    card_number: Optional[str] = Form(None),
    upi_id: Optional[str] = Form(None),
    payment_date: str = Form(...),
    simulate_fail: Optional[bool] = Form(False),
    db: Session = Depends(get_db)
):
    house = (
        db.query(models.House)
        .filter(
            models.House.house_id == house_id
        )
        .first()
    )

    if not house:
        return HTMLResponse(
            f"<script>"
            f"alert('Error: Register house ID "
            f"{house_id} first!');"
            f"window.location.href='/';"
            f"</script>"
        )

    count = (
        db.query(func.count(models.Payment.id))
        .filter(
            models.Payment.house_id == house_id
        )
        .scalar()
    )

    next_seq = count + 1

    payment_status = "SUCCESS"
    failure_reason = None
    txn_id = None

    # --------------------------------------------------------
    # FAILURE SIMULATION
    # --------------------------------------------------------

    if simulate_fail:
        payment_status = "FAILED"
        failure_reason = (
            "Transaction Declined: "
            "Bank Server Failure or Timeout "
            "(Error Code: ERR-BANK-504)"
        )
        txn_id = (
            f"FAIL-{int(time.time())}"
        )
    # --------------------------------------------------------------------------------------------------------------------------
    # PAYMENT GATEWAY
    # Inner exception handles invalid/unexpected gateway response, while outer exception handles communication failures such as 
    # timeout or gateway unavailability.
    # --------------------------------------------------------------------------------------------------------------------------
    else:
        try:
            payload = {
                "house_id": house_id,
                "amount": amount,
                "payment_method": payment_method,
                "card_number": card_number,
                "upi_id": upi_id
            }
            response = httpx.post(
                GATEWAY_URL,
                json=payload,
                timeout=5.0
            )
            if response.status_code == 200:
                res_data = response.json()
                txn_id = res_data.get(
                    "transaction_id",
                    f"TXN-{int(time.time())}"
                )
            else:
                payment_status = "FAILED"
                try:
                    failure_reason = (
                        response.json().get(
                            "detail",
                            "Transaction Declined "
                            "by Issuing Bank"
                        )
                    )
                except Exception:
                    failure_reason = (
                        "Transaction Declined "
                        "by Issuing Bank"
                    )
                txn_id = (
                    f"FAIL-{int(time.time())}"
                )

        except Exception:
            payment_status = "FAILED"
            failure_reason = (
                "Payment Gateway Unreachable "
                "or Connection Timeout"
            )
            txn_id = (
                f"FAIL-{int(time.time())}"
            )

    # --------------------------------------------------------
    # SAVE PAYMENT [ New Record ]
    # --------------------------------------------------------

    payment = models.Payment(
        house_id=house_id,
        month_sequence=next_seq,
        amount_paid=amount,
        payment_date=date.fromisoformat(
            payment_date
        ),
        payment_method=payment_method,
        transaction_id=txn_id,
        status=payment_status,
        failure_reason=failure_reason
    )

    db.add(payment)
    db.commit()

    # --------------------------------------------------------
    # RESULT
    # --------------------------------------------------------

    if payment_status == "SUCCESS":
        alert_msg = (
            f"Payment #{next_seq} Successful! "
            f"Txn ID: {txn_id}"
        )
    else:

        alert_msg = (
            f"Payment #{next_seq} FAILED! "
            f"Reason: {failure_reason}"
        )
    alert_msg = alert_msg.replace(
        "'",
        "\\'"
    )
    return HTMLResponse(
        f"<script>"
        f"alert('{alert_msg}');"
        f"window.location.href='/';"
        f"</script>"
    )


# ============================================================
# GET /tenants
# ============================================================

@app.get("/tenants")
def get_tenants(
    db: Session = Depends(get_db)
):
    """
    Returns all registered tenants with:
    House ID, Owner Name, Pending Payment,
    and Last Payment Date.
    """
    houses = db.query(
        models.House
    ).all()
    result = []
# ------------------------------------------------------
# Process each house one by one
# Get all invoices belonging to this house
# ----------------------------------------------------------
    for house in houses:
        invoices = (
            db.query(models.Invoice)
            .filter(
                models.Invoice.house_id
                == house.house_id
            )
            .all()
        )
        total_invoiced = sum(
            inv.total_invoice_amount
            for inv in invoices
        )
        payments = (
            db.query(models.Payment)
            .filter(
                models.Payment.house_id
                == house.house_id,
                models.Payment.status
                == "SUCCESS"
            )
            .order_by(
                models.Payment.payment_date.desc()
            )
            .all()
        )

        total_received = sum(
            pay.amount_paid
            for pay in payments
        )

        pending_payment = max(
            0.0,
            float(
                total_invoiced
                - total_received
            )
        )

        last_payment_date = (
            payments[0].payment_date.strftime(
                "%d-%b-%Y"
            )
            if payments
            else "N/A"
        )

        result.append({
            "house_id": house.house_id,
            "owner_name": house.owner_name,
            "pending_payment": round(
                pending_payment,
                2
            ),
            "last_payment_date":
                last_payment_date
        })

    return JSONResponse(
        content=result
    )