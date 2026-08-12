from datetime import date
from app.database import SessionLocal, engine, Base
from app import models

def seed_database():
    # Fresh setup for seeding
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        print("🌱 Seeding Jan 2026 to Aug 2026 full history with Failure Simulation Logs...")

        # ==========================================
        # 1. REGISTER ALL 10 HOUSES
        # ==========================================
        houses = [
            models.House(house_id="H101", owner_name="Rajesh Senapati", monthly_rent=15000),
            models.House(house_id="H102", owner_name="Ananya Mohanty", monthly_rent=20000),
            models.House(house_id="H103", owner_name="Amit Rout", monthly_rent=12500),
            models.House(house_id="H104", owner_name="Sneha Nayak", monthly_rent=18000),
            models.House(house_id="H105", owner_name="Vikram Samantray", monthly_rent=25000),
            models.House(house_id="H106", owner_name="Pooja Nayak", monthly_rent=14000),
            models.House(house_id="H107", owner_name="Suresh Senapati", monthly_rent=22000),
            models.House(house_id="H108", owner_name="Ritu Das", monthly_rent=16500),
            models.House(house_id="H109", owner_name="Manoj Mohapatra", monthly_rent=19000),
            models.House(house_id="H110", owner_name="Neha Roy", monthly_rent=30000),
        ]
        db.add_all(houses)
        db.commit()

        # ==========================================
        # 2. INVOICES (Jan 2026 - Aug 2026 for H101 to H110)
        # ==========================================
        invoices = [
            # --- H101 ---
            models.Invoice(house_id="H101", month_sequence=1, rent_amount=15000, electric_units=100, electric_amount=800, water_bill=300, society_maintenance=0, total_invoice_amount=16100, created_date=date(2026, 1, 1), due_date=date(2026, 1, 8)),
            models.Invoice(house_id="H101", month_sequence=2, rent_amount=15000, electric_units=110, electric_amount=880, water_bill=300, society_maintenance=0, total_invoice_amount=16180, created_date=date(2026, 2, 1), due_date=date(2026, 2, 8)),
            models.Invoice(house_id="H101", month_sequence=3, rent_amount=15000, electric_units=120, electric_amount=960, water_bill=300, society_maintenance=2500, total_invoice_amount=18760, created_date=date(2026, 3, 1), due_date=date(2026, 3, 8)),
            models.Invoice(house_id="H101", month_sequence=4, rent_amount=15000, electric_units=130, electric_amount=1040, water_bill=300, society_maintenance=0, total_invoice_amount=16340, created_date=date(2026, 4, 1), due_date=date(2026, 4, 8)),
            models.Invoice(house_id="H101", month_sequence=5, rent_amount=15000, electric_units=140, electric_amount=1120, water_bill=300, society_maintenance=0, total_invoice_amount=16420, created_date=date(2026, 5, 1), due_date=date(2026, 5, 8)),
            models.Invoice(house_id="H101", month_sequence=6, rent_amount=15000, electric_units=150, electric_amount=1200, water_bill=300, society_maintenance=2500, total_invoice_amount=19000, created_date=date(2026, 6, 1), due_date=date(2026, 6, 8)),
            models.Invoice(house_id="H101", month_sequence=7, rent_amount=15000, electric_units=160, electric_amount=1280, water_bill=300, society_maintenance=0, total_invoice_amount=16580, created_date=date(2026, 7, 1), due_date=date(2026, 7, 8)),
            models.Invoice(house_id="H101", month_sequence=8, rent_amount=15000, electric_units=150, electric_amount=1200, water_bill=300, society_maintenance=0, total_invoice_amount=16500, created_date=date(2026, 8, 1), due_date=date(2026, 8, 8)),

            # --- H102 ---
            models.Invoice(house_id="H102", month_sequence=1, rent_amount=20000, electric_units=150, electric_amount=1200, water_bill=400, society_maintenance=0, total_invoice_amount=21600, created_date=date(2026, 1, 1), due_date=date(2026, 1, 8)),
            models.Invoice(house_id="H102", month_sequence=2, rent_amount=20000, electric_units=160, electric_amount=1280, water_bill=400, society_maintenance=0, total_invoice_amount=21680, created_date=date(2026, 2, 1), due_date=date(2026, 2, 8)),
            models.Invoice(house_id="H102", month_sequence=3, rent_amount=20000, electric_units=170, electric_amount=1360, water_bill=400, society_maintenance=3000, total_invoice_amount=24760, created_date=date(2026, 3, 1), due_date=date(2026, 3, 8)),
            models.Invoice(house_id="H102", month_sequence=4, rent_amount=20000, electric_units=180, electric_amount=1440, water_bill=400, society_maintenance=0, total_invoice_amount=21840, created_date=date(2026, 4, 1), due_date=date(2026, 4, 8)),
            models.Invoice(house_id="H102", month_sequence=5, rent_amount=20000, electric_units=190, electric_amount=1520, water_bill=400, society_maintenance=0, total_invoice_amount=21920, created_date=date(2026, 5, 1), due_date=date(2026, 5, 8)),
            models.Invoice(house_id="H102", month_sequence=6, rent_amount=20000, electric_units=200, electric_amount=1600, water_bill=400, society_maintenance=3000, total_invoice_amount=25000, created_date=date(2026, 6, 1), due_date=date(2026, 6, 8)),
            models.Invoice(house_id="H102", month_sequence=7, rent_amount=20000, electric_units=210, electric_amount=1680, water_bill=400, society_maintenance=0, total_invoice_amount=22080, created_date=date(2026, 7, 1), due_date=date(2026, 7, 8)),
            models.Invoice(house_id="H102", month_sequence=8, rent_amount=20000, electric_units=200, electric_amount=1600, water_bill=400, society_maintenance=0, total_invoice_amount=22000, created_date=date(2026, 8, 1), due_date=date(2026, 8, 8)),

            # --- H103 ---
            models.Invoice(house_id="H103", month_sequence=1, rent_amount=12500, electric_units=90, electric_amount=720, water_bill=250, society_maintenance=0, total_invoice_amount=13470, created_date=date(2026, 1, 1), due_date=date(2026, 1, 8)),
            models.Invoice(house_id="H103", month_sequence=2, rent_amount=12500, electric_units=100, electric_amount=800, water_bill=250, society_maintenance=0, total_invoice_amount=13550, created_date=date(2026, 2, 1), due_date=date(2026, 2, 8)),
            models.Invoice(house_id="H103", month_sequence=3, rent_amount=12500, electric_units=110, electric_amount=880, water_bill=250, society_maintenance=2000, total_invoice_amount=15630, created_date=date(2026, 3, 1), due_date=date(2026, 3, 8)),
            models.Invoice(house_id="H103", month_sequence=4, rent_amount=12500, electric_units=100, electric_amount=800, water_bill=250, society_maintenance=0, total_invoice_amount=13550, created_date=date(2026, 4, 1), due_date=date(2026, 4, 8)),
            models.Invoice(house_id="H103", month_sequence=5, rent_amount=12500, electric_units=105, electric_amount=840, water_bill=250, society_maintenance=0, total_invoice_amount=13590, created_date=date(2026, 5, 1), due_date=date(2026, 5, 8)),
            models.Invoice(house_id="H103", month_sequence=6, rent_amount=12500, electric_units=110, electric_amount=880, water_bill=250, society_maintenance=2000, total_invoice_amount=15630, created_date=date(2026, 6, 1), due_date=date(2026, 6, 8)),
            models.Invoice(house_id="H103", month_sequence=7, rent_amount=12500, electric_units=115, electric_amount=920, water_bill=250, society_maintenance=0, total_invoice_amount=13670, created_date=date(2026, 7, 1), due_date=date(2026, 7, 8)),
            models.Invoice(house_id="H103", month_sequence=8, rent_amount=12500, electric_units=120, electric_amount=960, water_bill=250, society_maintenance=0, total_invoice_amount=13710, created_date=date(2026, 8, 1), due_date=date(2026, 8, 8)),

            # --- H104 ---
            models.Invoice(house_id="H104", month_sequence=1, rent_amount=18000, electric_units=130, electric_amount=1040, water_bill=350, society_maintenance=0, total_invoice_amount=19390, created_date=date(2026, 1, 1), due_date=date(2026, 1, 8)),
            models.Invoice(house_id="H104", month_sequence=2, rent_amount=18000, electric_units=140, electric_amount=1120, water_bill=350, society_maintenance=0, total_invoice_amount=19470, created_date=date(2026, 2, 1), due_date=date(2026, 2, 8)),
            models.Invoice(house_id="H104", month_sequence=3, rent_amount=18000, electric_units=150, electric_amount=1200, water_bill=350, society_maintenance=2500, total_invoice_amount=22050, created_date=date(2026, 3, 1), due_date=date(2026, 3, 8)),
            models.Invoice(house_id="H104", month_sequence=4, rent_amount=18000, electric_units=140, electric_amount=1120, water_bill=350, society_maintenance=0, total_invoice_amount=19470, created_date=date(2026, 4, 1), due_date=date(2026, 4, 8)),
            models.Invoice(house_id="H104", month_sequence=5, rent_amount=18000, electric_units=160, electric_amount=1280, water_bill=350, society_maintenance=0, total_invoice_amount=19630, created_date=date(2026, 5, 1), due_date=date(2026, 5, 8)),
            models.Invoice(house_id="H104", month_sequence=6, rent_amount=18000, electric_units=170, electric_amount=1360, water_bill=350, society_maintenance=2500, total_invoice_amount=22210, created_date=date(2026, 6, 1), due_date=date(2026, 6, 8)),
            models.Invoice(house_id="H104", month_sequence=7, rent_amount=18000, electric_units=180, electric_amount=1440, water_bill=350, society_maintenance=0, total_invoice_amount=19790, created_date=date(2026, 7, 1), due_date=date(2026, 7, 8)),
            models.Invoice(house_id="H104", month_sequence=8, rent_amount=18000, electric_units=175, electric_amount=1400, water_bill=350, society_maintenance=0, total_invoice_amount=19750, created_date=date(2026, 8, 1), due_date=date(2026, 8, 8)),

            # --- H105 ---
            models.Invoice(house_id="H105", month_sequence=1, rent_amount=25000, electric_units=200, electric_amount=1600, water_bill=500, society_maintenance=0, total_invoice_amount=27100, created_date=date(2026, 1, 1), due_date=date(2026, 1, 8)),
            models.Invoice(house_id="H105", month_sequence=2, rent_amount=25000, electric_units=210, electric_amount=1680, water_bill=500, society_maintenance=0, total_invoice_amount=27180, created_date=date(2026, 2, 1), due_date=date(2026, 2, 8)),
            models.Invoice(house_id="H105", month_sequence=3, rent_amount=25000, electric_units=220, electric_amount=1760, water_bill=500, society_maintenance=4000, total_invoice_amount=31260, created_date=date(2026, 3, 1), due_date=date(2026, 3, 8)),
            models.Invoice(house_id="H105", month_sequence=4, rent_amount=25000, electric_units=210, electric_amount=1680, water_bill=500, society_maintenance=0, total_invoice_amount=27180, created_date=date(2026, 4, 1), due_date=date(2026, 4, 8)),
            models.Invoice(house_id="H105", month_sequence=5, rent_amount=25000, electric_units=230, electric_amount=1840, water_bill=500, society_maintenance=0, total_invoice_amount=27340, created_date=date(2026, 5, 1), due_date=date(2026, 5, 8)),
            models.Invoice(house_id="H105", month_sequence=6, rent_amount=25000, electric_units=240, electric_amount=1920, water_bill=500, society_maintenance=4000, total_invoice_amount=31420, created_date=date(2026, 6, 1), due_date=date(2026, 6, 8)),
            models.Invoice(house_id="H105", month_sequence=7, rent_amount=25000, electric_units=250, electric_amount=2000, water_bill=500, society_maintenance=0, total_invoice_amount=27500, created_date=date(2026, 7, 1), due_date=date(2026, 7, 8)),
            models.Invoice(house_id="H105", month_sequence=8, rent_amount=25000, electric_units=240, electric_amount=1920, water_bill=500, society_maintenance=0, total_invoice_amount=27420, created_date=date(2026, 8, 1), due_date=date(2026, 8, 8)),

            # --- H106 ---
            models.Invoice(house_id="H106", month_sequence=1, rent_amount=14000, electric_units=100, electric_amount=800, water_bill=300, society_maintenance=0, total_invoice_amount=15100, created_date=date(2026, 1, 1), due_date=date(2026, 1, 8)),
            models.Invoice(house_id="H106", month_sequence=2, rent_amount=14000, electric_units=110, electric_amount=880, water_bill=300, society_maintenance=0, total_invoice_amount=15180, created_date=date(2026, 2, 1), due_date=date(2026, 2, 8)),
            models.Invoice(house_id="H106", month_sequence=3, rent_amount=14000, electric_units=120, electric_amount=960, water_bill=300, society_maintenance=2000, total_invoice_amount=17260, created_date=date(2026, 3, 1), due_date=date(2026, 3, 8)),
            models.Invoice(house_id="H106", month_sequence=4, rent_amount=14000, electric_units=115, electric_amount=920, water_bill=300, society_maintenance=0, total_invoice_amount=15220, created_date=date(2026, 4, 1), due_date=date(2026, 4, 8)),
            models.Invoice(house_id="H106", month_sequence=5, rent_amount=14000, electric_units=125, electric_amount=1000, water_bill=300, society_maintenance=0, total_invoice_amount=15300, created_date=date(2026, 5, 1), due_date=date(2026, 5, 8)),
            models.Invoice(house_id="H106", month_sequence=6, rent_amount=14000, electric_units=130, electric_amount=1040, water_bill=300, society_maintenance=2000, total_invoice_amount=17340, created_date=date(2026, 6, 1), due_date=date(2026, 6, 8)),
            models.Invoice(house_id="H106", month_sequence=7, rent_amount=14000, electric_units=135, electric_amount=1080, water_bill=300, society_maintenance=0, total_invoice_amount=15380, created_date=date(2026, 7, 1), due_date=date(2026, 7, 8)),
            models.Invoice(house_id="H106", month_sequence=8, rent_amount=14000, electric_units=140, electric_amount=1120, water_bill=300, society_maintenance=0, total_invoice_amount=15420, created_date=date(2026, 8, 1), due_date=date(2026, 8, 8)),

            # --- H107 ---
            models.Invoice(house_id="H107", month_sequence=1, rent_amount=22000, electric_units=180, electric_amount=1440, water_bill=450, society_maintenance=0, total_invoice_amount=23890, created_date=date(2026, 1, 1), due_date=date(2026, 1, 8)),
            models.Invoice(house_id="H107", month_sequence=2, rent_amount=22000, electric_units=190, electric_amount=1520, water_bill=450, society_maintenance=0, total_invoice_amount=23970, created_date=date(2026, 2, 1), due_date=date(2026, 2, 8)),
            models.Invoice(house_id="H107", month_sequence=3, rent_amount=22000, electric_units=200, electric_amount=1600, water_bill=450, society_maintenance=3500, total_invoice_amount=27550, created_date=date(2026, 3, 1), due_date=date(2026, 3, 8)),
            models.Invoice(house_id="H107", month_sequence=4, rent_amount=22000, electric_units=210, electric_amount=1680, water_bill=450, society_maintenance=0, total_invoice_amount=24130, created_date=date(2026, 4, 1), due_date=date(2026, 4, 8)),
            models.Invoice(house_id="H107", month_sequence=5, rent_amount=22000, electric_units=220, electric_amount=1760, water_bill=450, society_maintenance=0, total_invoice_amount=24210, created_date=date(2026, 5, 1), due_date=date(2026, 5, 8)),
            models.Invoice(house_id="H107", month_sequence=6, rent_amount=22000, electric_units=230, electric_amount=1840, water_bill=450, society_maintenance=3500, total_invoice_amount=27790, created_date=date(2026, 6, 1), due_date=date(2026, 6, 8)),
            models.Invoice(house_id="H107", month_sequence=7, rent_amount=22000, electric_units=240, electric_amount=1920, water_bill=450, society_maintenance=0, total_invoice_amount=24370, created_date=date(2026, 7, 1), due_date=date(2026, 7, 8)),
            models.Invoice(house_id="H107", month_sequence=8, rent_amount=22000, electric_units=230, electric_amount=1840, water_bill=450, society_maintenance=0, total_invoice_amount=24290, created_date=date(2026, 8, 1), due_date=date(2026, 8, 8)),

            # --- H108 ---
            models.Invoice(house_id="H108", month_sequence=1, rent_amount=16500, electric_units=120, electric_amount=960, water_bill=350, society_maintenance=0, total_invoice_amount=17810, created_date=date(2026, 1, 1), due_date=date(2026, 1, 8)),
            models.Invoice(house_id="H108", month_sequence=2, rent_amount=16500, electric_units=130, electric_amount=1040, water_bill=350, society_maintenance=0, total_invoice_amount=17890, created_date=date(2026, 2, 1), due_date=date(2026, 2, 8)),
            models.Invoice(house_id="H108", month_sequence=3, rent_amount=16500, electric_units=140, electric_amount=1120, water_bill=350, society_maintenance=2500, total_invoice_amount=20470, created_date=date(2026, 3, 1), due_date=date(2026, 3, 8)),
            models.Invoice(house_id="H108", month_sequence=4, rent_amount=16500, electric_units=135, electric_amount=1080, water_bill=350, society_maintenance=0, total_invoice_amount=17930, created_date=date(2026, 4, 1), due_date=date(2026, 4, 8)),
            models.Invoice(house_id="H108", month_sequence=5, rent_amount=16500, electric_units=145, electric_amount=1160, water_bill=350, society_maintenance=0, total_invoice_amount=18010, created_date=date(2026, 5, 1), due_date=date(2026, 5, 8)),
            models.Invoice(house_id="H108", month_sequence=6, rent_amount=16500, electric_units=150, electric_amount=1200, water_bill=350, society_maintenance=2500, total_invoice_amount=20550, created_date=date(2026, 6, 1), due_date=date(2026, 6, 8)),
            models.Invoice(house_id="H108", month_sequence=7, rent_amount=16500, electric_units=155, electric_amount=1240, water_bill=350, society_maintenance=0, total_invoice_amount=18090, created_date=date(2026, 7, 1), due_date=date(2026, 7, 8)),
            models.Invoice(house_id="H108", month_sequence=8, rent_amount=16500, electric_units=160, electric_amount=1280, water_bill=350, society_maintenance=0, total_invoice_amount=18130, created_date=date(2026, 8, 1), due_date=date(2026, 8, 8)),

            # --- H109 ---
            models.Invoice(house_id="H109", month_sequence=1, rent_amount=19000, electric_units=140, electric_amount=1120, water_bill=400, society_maintenance=0, total_invoice_amount=20520, created_date=date(2026, 1, 1), due_date=date(2026, 1, 8)),
            models.Invoice(house_id="H109", month_sequence=2, rent_amount=19000, electric_units=150, electric_amount=1200, water_bill=400, society_maintenance=0, total_invoice_amount=20600, created_date=date(2026, 2, 1), due_date=date(2026, 2, 8)),
            models.Invoice(house_id="H109", month_sequence=3, rent_amount=19000, electric_units=160, electric_amount=1280, water_bill=400, society_maintenance=3000, total_invoice_amount=23680, created_date=date(2026, 3, 1), due_date=date(2026, 3, 8)),
            models.Invoice(house_id="H109", month_sequence=4, rent_amount=19000, electric_units=155, electric_amount=1240, water_bill=400, society_maintenance=0, total_invoice_amount=20640, created_date=date(2026, 4, 1), due_date=date(2026, 4, 8)),
            models.Invoice(house_id="H109", month_sequence=5, rent_amount=19000, electric_units=165, electric_amount=1320, water_bill=400, society_maintenance=0, total_invoice_amount=20720, created_date=date(2026, 5, 1), due_date=date(2026, 5, 8)),
            models.Invoice(house_id="H109", month_sequence=6, rent_amount=19000, electric_units=170, electric_amount=1360, water_bill=400, society_maintenance=3000, total_invoice_amount=23760, created_date=date(2026, 6, 1), due_date=date(2026, 6, 8)),
            models.Invoice(house_id="H109", month_sequence=7, rent_amount=19000, electric_units=180, electric_amount=1440, water_bill=400, society_maintenance=0, total_invoice_amount=20840, created_date=date(2026, 7, 1), due_date=date(2026, 7, 8)),
            models.Invoice(house_id="H109", month_sequence=8, rent_amount=19000, electric_units=175, electric_amount=1400, water_bill=400, society_maintenance=0, total_invoice_amount=20800, created_date=date(2026, 8, 1), due_date=date(2026, 8, 8)),

            # --- H110 ---
            models.Invoice(house_id="H110", month_sequence=1, rent_amount=30000, electric_units=250, electric_amount=2000, water_bill=600, society_maintenance=0, total_invoice_amount=32600, created_date=date(2026, 1, 1), due_date=date(2026, 1, 8)),
            models.Invoice(house_id="H110", month_sequence=2, rent_amount=30000, electric_units=260, electric_amount=2080, water_bill=600, society_maintenance=0, total_invoice_amount=32680, created_date=date(2026, 2, 1), due_date=date(2026, 2, 8)),
            models.Invoice(house_id="H110", month_sequence=3, rent_amount=30000, electric_units=270, electric_amount=2160, water_bill=600, society_maintenance=5000, total_invoice_amount=37760, created_date=date(2026, 3, 1), due_date=date(2026, 3, 8)),
            models.Invoice(house_id="H110", month_sequence=4, rent_amount=30000, electric_units=280, electric_amount=2240, water_bill=600, society_maintenance=0, total_invoice_amount=32840, created_date=date(2026, 4, 1), due_date=date(2026, 4, 8)),
            models.Invoice(house_id="H110", month_sequence=5, rent_amount=30000, electric_units=290, electric_amount=2320, water_bill=600, society_maintenance=0, total_invoice_amount=32920, created_date=date(2026, 5, 1), due_date=date(2026, 5, 8)),
            models.Invoice(house_id="H110", month_sequence=6, rent_amount=30000, electric_units=300, electric_amount=2400, water_bill=600, society_maintenance=5000, total_invoice_amount=38000, created_date=date(2026, 6, 1), due_date=date(2026, 6, 8)),
            models.Invoice(house_id="H110", month_sequence=7, rent_amount=30000, electric_units=310, electric_amount=2480, water_bill=600, society_maintenance=0, total_invoice_amount=33080, created_date=date(2026, 7, 1), due_date=date(2026, 7, 8)),
            models.Invoice(house_id="H110", month_sequence=8, rent_amount=30000, electric_units=300, electric_amount=2400, water_bill=600, society_maintenance=0, total_invoice_amount=33000, created_date=date(2026, 8, 1), due_date=date(2026, 8, 8)),
        ]
        db.add_all(invoices)
        db.commit()

        # ==========================================
        # 3. PAYMENTS (Includes Successful & Failed Simulation)
        # ==========================================
        payments = [
            # H101 (All 8 Months Clear)
            models.Payment(house_id="H101", month_sequence=1, amount_paid=16100, payment_date=date(2026, 1, 5), payment_method="UPI", transaction_id="TXN-H101-1", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H101", month_sequence=2, amount_paid=16180, payment_date=date(2026, 2, 4), payment_method="UPI", transaction_id="TXN-H101-2", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H101", month_sequence=3, amount_paid=18760, payment_date=date(2026, 3, 5), payment_method="CARD", transaction_id="TXN-H101-3", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H101", month_sequence=4, amount_paid=16340, payment_date=date(2026, 4, 6), payment_method="UPI", transaction_id="TXN-H101-4", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H101", month_sequence=5, amount_paid=16420, payment_date=date(2026, 5, 5), payment_method="CARD", transaction_id="TXN-H101-5", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H101", month_sequence=6, amount_paid=19000, payment_date=date(2026, 6, 4), payment_method="UPI", transaction_id="TXN-H101-6", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H101", month_sequence=7, amount_paid=16580, payment_date=date(2026, 7, 5), payment_method="UPI", transaction_id="TXN-H101-7", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H101", month_sequence=8, amount_paid=16500, payment_date=date(2026, 8, 5), payment_method="UPI", transaction_id="TXN-H101-8", status=models.PaymentStatus.SUCCESS),

            # H102 (First attempt Failed in March, retry succeeded, Unpaid from April)
            models.Payment(house_id="H102", month_sequence=1, amount_paid=21600, payment_date=date(2026, 1, 6), payment_method="CARD", transaction_id="TXN-H102-1", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H102", month_sequence=2, amount_paid=21680, payment_date=date(2026, 2, 5), payment_method="CARD", transaction_id="TXN-H102-2", status=models.PaymentStatus.SUCCESS),
            # Failed Payment Simulation Record for Demo UI
            models.Payment(house_id="H102", month_sequence=3, amount_paid=24760, payment_date=date(2026, 3, 6), payment_method="CARD", transaction_id="FAIL-TXN-H102-3", status=models.PaymentStatus.FAILED, failure_reason="Insufficient Funds / Bank Rejected"),

            # H103 (Paid Late Every Month with 10% penalty)
            models.Payment(house_id="H103", month_sequence=1, amount_paid=14720, payment_date=date(2026, 1, 15), payment_method="UPI", transaction_id="TXN-H103-1", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H103", month_sequence=2, amount_paid=14800, payment_date=date(2026, 2, 18), payment_method="UPI", transaction_id="TXN-H103-2", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H103", month_sequence=3, amount_paid=16880, payment_date=date(2026, 3, 20), payment_method="UPI", transaction_id="TXN-H103-3", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H103", month_sequence=4, amount_paid=14800, payment_date=date(2026, 4, 12), payment_method="CARD", transaction_id="TXN-H103-4", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H103", month_sequence=5, amount_paid=14840, payment_date=date(2026, 5, 14), payment_method="UPI", transaction_id="TXN-H103-5", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H103", month_sequence=6, amount_paid=16880, payment_date=date(2026, 6, 19), payment_method="UPI", transaction_id="TXN-H103-6", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H103", month_sequence=7, amount_paid=14920, payment_date=date(2026, 7, 22), payment_method="CARD", transaction_id="TXN-H103-7", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H103", month_sequence=8, amount_paid=14960, payment_date=date(2026, 8, 10), payment_method="UPI", transaction_id="TXN-H103-8", status=models.PaymentStatus.SUCCESS),

            # H104 (Jan-Aug Clear)
            models.Payment(house_id="H104", month_sequence=1, amount_paid=19390, payment_date=date(2026, 1, 5), payment_method="UPI", transaction_id="TXN-H104-1", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H104", month_sequence=2, amount_paid=19470, payment_date=date(2026, 2, 6), payment_method="CARD", transaction_id="TXN-H104-2", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H104", month_sequence=3, amount_paid=22050, payment_date=date(2026, 3, 5), payment_method="UPI", transaction_id="TXN-H104-3", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H104", month_sequence=4, amount_paid=19470, payment_date=date(2026, 4, 4), payment_method="UPI", transaction_id="TXN-H104-4", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H104", month_sequence=5, amount_paid=19630, payment_date=date(2026, 5, 5), payment_method="CARD", transaction_id="TXN-H104-5", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H104", month_sequence=6, amount_paid=22210, payment_date=date(2026, 6, 6), payment_method="UPI", transaction_id="TXN-H104-6", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H104", month_sequence=7, amount_paid=19790, payment_date=date(2026, 7, 5), payment_method="UPI", transaction_id="TXN-H104-7", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H104", month_sequence=8, amount_paid=19750, payment_date=date(2026, 8, 4), payment_method="UPI", transaction_id="TXN-H104-8", status=models.PaymentStatus.SUCCESS),

            # H105 (High Rent Late Payer)
            models.Payment(house_id="H105", month_sequence=1, amount_paid=29600, payment_date=date(2026, 1, 20), payment_method="CARD", transaction_id="TXN-H105-1", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H105", month_sequence=2, amount_paid=29680, payment_date=date(2026, 2, 22), payment_method="CARD", transaction_id="TXN-H105-2", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H105", month_sequence=3, amount_paid=33760, payment_date=date(2026, 3, 19), payment_method="UPI", transaction_id="TXN-H105-3", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H105", month_sequence=4, amount_paid=29680, payment_date=date(2026, 4, 21), payment_method="CARD", transaction_id="TXN-H105-4", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H105", month_sequence=5, amount_paid=29840, payment_date=date(2026, 5, 18), payment_method="UPI", transaction_id="TXN-H105-5", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H105", month_sequence=6, amount_paid=33920, payment_date=date(2026, 6, 25), payment_method="UPI", transaction_id="TXN-H105-6", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H105", month_sequence=7, amount_paid=30000, payment_date=date(2026, 7, 20), payment_method="CARD", transaction_id="TXN-H105-7", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H105", month_sequence=8, amount_paid=29920, payment_date=date(2026, 8, 10), payment_method="UPI", transaction_id="TXN-H105-8", status=models.PaymentStatus.SUCCESS),

            # H106 (Jan-July Clear, August Pending)
            models.Payment(house_id="H106", month_sequence=1, amount_paid=15100, payment_date=date(2026, 1, 5), payment_method="UPI", transaction_id="TXN-H106-1", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H106", month_sequence=2, amount_paid=15180, payment_date=date(2026, 2, 6), payment_method="UPI", transaction_id="TXN-H106-2", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H106", month_sequence=3, amount_paid=17260, payment_date=date(2026, 3, 4), payment_method="CARD", transaction_id="TXN-H106-3", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H106", month_sequence=4, amount_paid=15220, payment_date=date(2026, 4, 5), payment_method="UPI", transaction_id="TXN-H106-4", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H106", month_sequence=5, amount_paid=15300, payment_date=date(2026, 5, 6), payment_method="UPI", transaction_id="TXN-H106-5", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H106", month_sequence=6, amount_paid=17340, payment_date=date(2026, 6, 5), payment_method="CARD", transaction_id="TXN-H106-6", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H106", month_sequence=7, amount_paid=15380, payment_date=date(2026, 7, 6), payment_method="UPI", transaction_id="TXN-H106-7", status=models.PaymentStatus.SUCCESS),

            # H107 (Jan-Aug Clear)
            models.Payment(house_id="H107", month_sequence=1, amount_paid=23890, payment_date=date(2026, 1, 4), payment_method="UPI", transaction_id="TXN-H107-1", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H107", month_sequence=2, amount_paid=23970, payment_date=date(2026, 2, 5), payment_method="CARD", transaction_id="TXN-H107-2", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H107", month_sequence=3, amount_paid=27550, payment_date=date(2026, 3, 6), payment_method="UPI", transaction_id="TXN-H107-3", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H107", month_sequence=4, amount_paid=24130, payment_date=date(2026, 4, 5), payment_method="UPI", transaction_id="TXN-H107-4", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H107", month_sequence=5, amount_paid=24210, payment_date=date(2026, 5, 4), payment_method="CARD", transaction_id="TXN-H107-5", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H107", month_sequence=6, amount_paid=27790, payment_date=date(2026, 6, 5), payment_method="UPI", transaction_id="TXN-H107-6", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H107", month_sequence=7, amount_paid=24370, payment_date=date(2026, 7, 6), payment_method="UPI", transaction_id="TXN-H107-7", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H107", month_sequence=8, amount_paid=24290, payment_date=date(2026, 8, 5), payment_method="UPI", transaction_id="TXN-H107-8", status=models.PaymentStatus.SUCCESS),

            # H108 (Jan-July Clear, August Pending)
            models.Payment(house_id="H108", month_sequence=1, amount_paid=17810, payment_date=date(2026, 1, 5), payment_method="UPI", transaction_id="TXN-H108-1", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H108", month_sequence=2, amount_paid=17890, payment_date=date(2026, 2, 5), payment_method="CARD", transaction_id="TXN-H108-2", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H108", month_sequence=3, amount_paid=20470, payment_date=date(2026, 3, 6), payment_method="UPI", transaction_id="TXN-H108-3", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H108", month_sequence=4, amount_paid=17930, payment_date=date(2026, 4, 4), payment_method="UPI", transaction_id="TXN-H108-4", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H108", month_sequence=5, amount_paid=18010, payment_date=date(2026, 5, 5), payment_method="CARD", transaction_id="TXN-H108-5", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H108", month_sequence=6, amount_paid=20550, payment_date=date(2026, 6, 6), payment_method="UPI", transaction_id="TXN-H108-6", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H108", month_sequence=7, amount_paid=18090, payment_date=date(2026, 7, 5), payment_method="UPI", transaction_id="TXN-H108-7", status=models.PaymentStatus.SUCCESS),

            # H109 (Paid Jan-April, May-Aug Pending)
            models.Payment(house_id="H109", month_sequence=1, amount_paid=20520, payment_date=date(2026, 1, 5), payment_method="UPI", transaction_id="TXN-H109-1", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H109", month_sequence=2, amount_paid=20600, payment_date=date(2026, 2, 6), payment_method="CARD", transaction_id="TXN-H109-2", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H109", month_sequence=3, amount_paid=23680, payment_date=date(2026, 3, 5), payment_method="UPI", transaction_id="TXN-H109-3", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H109", month_sequence=4, amount_paid=20640, payment_date=date(2026, 4, 7), payment_method="UPI", transaction_id="TXN-H109-4", status=models.PaymentStatus.SUCCESS),

            # H110 (Paid Jan-Feb, Mar-Aug Pending)
            models.Payment(house_id="H110", month_sequence=1, amount_paid=32600, payment_date=date(2026, 1, 6), payment_method="CARD", transaction_id="TXN-H110-1", status=models.PaymentStatus.SUCCESS),
            models.Payment(house_id="H110", month_sequence=2, amount_paid=32680, payment_date=date(2026, 2, 5), payment_method="UPI", transaction_id="TXN-H110-2", status=models.PaymentStatus.SUCCESS),
        ]
        db.add_all(payments)
        db.commit()

        print("FULL 8 MONTHS SEEDING COMPLETED FOR ALL 10 HOUSES!")

    except Exception as e:
        db.rollback()
        print(f"❌ Error during seeding: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()