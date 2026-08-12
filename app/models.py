import enum
from datetime import date, datetime
from sqlalchemy import Column, Integer, String, Float, Enum, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class PaymentStatus(str, enum.Enum):
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    PENDING = "PENDING"

class House(Base):
    __tablename__ = "houses"

    house_id = Column(String, primary_key=True, index=True)
    owner_name = Column(String, nullable=False)
    monthly_rent = Column(Float, nullable=False)

    invoices = relationship("Invoice", back_populates="house")
    payments = relationship("Payment", back_populates="house")

class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    house_id = Column(String, ForeignKey("houses.house_id"), nullable=False)
    month_sequence = Column(Integer, nullable=False)
    rent_amount = Column(Float, nullable=False)
    electric_units = Column(Float, default=0.0)
    electric_amount = Column(Float, default=0.0)
    water_bill = Column(Float, default=0.0)
    society_maintenance = Column(Float, default=0.0)
    total_invoice_amount = Column(Float, nullable=False)
    created_date = Column(Date, nullable=False)
    due_date = Column(Date, nullable=False)

    house = relationship("House", back_populates="invoices")

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    house_id = Column(String, ForeignKey("houses.house_id"), nullable=False)
    month_sequence = Column(Integer, nullable=False)
    amount_paid = Column(Float, nullable=False)
    payment_date = Column(Date, default=date.today)
    payment_method = Column(String, default="UPI")
    transaction_id = Column(String, unique=True, index=True, nullable=False)
    status = Column(Enum(PaymentStatus), default=PaymentStatus.SUCCESS, nullable=False)
    failure_reason = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    house = relationship("House", back_populates="payments")