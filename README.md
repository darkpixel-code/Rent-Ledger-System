# 🏠 Rent Ledger Microservices System

A production-grade Rent Ledger Application built using **FastAPI**, **PostgreSQL**, and **Docker**. The application features a architecture that separates core ledger operations from mock payment processing gateways, complete with a dynamic Bootstrap-based web dashboard.

---

## 📑 Project Summary

The Rent Ledger System automates property ledger management, invoicing, and tenant tracking:
* **Core Ledger Engine:** Tracks real-time running balances, calculates multi-line invoices, and updates account statuses using database transactions.
* **Mock Payment Gateway:** A process that handles payment method routing and simulates success/failure webhooks.
* **Interactive Dashboard:** Offers a unified interface for invoice generation, payment processing, ledger lookup, and real-time tenant summary tracking.

---

## 🔗 Quick Access & Setup

* **Dashboard URL:** http://localhost:8000/
* **Git Clone Command:** `git clone <repository-url> && cd rent-ledger-system`
* **Docker Run Command:** `docker compose up --build -d`
* **Docker View Logs:** `docker compose logs -f`
* **Docker Stop Command:** `docker compose down`

---

## 🛠️ API Reference & Endpoints

* `GET /tenants` — Fetches a summary list of all tenants, pending balances, and their last payment dates.
* `GET /tenants/{id}/statement?
asOf=YYYY-MM-DD` - Returns the ledger statement for a house up to the selected date.
* `POST /register-house` — Registers a new house ID along with the assigned owner name and monthly rent.
* `POST /generate-invoice` — Calculates and issues an invoice containing utility, water, maintenance, and rent totals.
* `POST /payment` — Routes payments to the mock gateway and records credit/failed ledger entries.

---

## 🏗️ System Architecture Flow

Frontend (Dashboard @ http://localhost:8000/) ➔ Main FastAPI Service ➔ PostgreSQL Database & Mock Payment (Port 8002)

1. **User Interface (`app/templates/index.html`):** 
Dashboard supplying user forms for house registration, billing, payment processing, and tenant lookups.

2. **Main Application Service (`app/main.py`):** 
app/main.py — FastAPI application entry point, mounting routers, template configurations and startup sequences.

3. **Database Layer (`app/database.py` & `app/models.py`):** Configures SQLAlchemy engine 
app/database.py — Configures the SQLAlchemy database engine, session local, and base metadata.
app/models.py — SQLAlchemy ORM models defining database tables for houses, invoices, payments, and unified ledger entries.

4. **Data Validation Layer (`app/schemas.py`):** 
Pydantic models ensuring data integrity and validation across request payloads and responses.

5. **Mock Payment Service (`app/gateway.py`):** 
Isolated microservice running on port `8002` to handle payment validation, provider mocking (GPay, PhonePe, Cards, Net Banking), and forced failure simulations.

6. **Data Seeding (`app/seed.py`):** 
Utility script populating initial sample records into the database for immediate testing and evaluation.

7. **Containerization(`Dockerfile`, `docker-compose.yml`):** 
docker-compose.yml — Docker Compose orchestration file managing the FastAPI application, PostgreSQL database and services.
Dockerfile — Container build instructions packaging the FastAPI application environment.

8.**Environment(`requirements.txt`):**
requirements.txt — Python package dependencies required by the application stack.

---

## 🚀 Step-by-Step Getting Started

### Prerequisites
* Docker Desktop installed and running.
* Git installed on your local machine.

### Installation & Launch

1. **Clone the repository:**
   `git clone <repository-url> && cd Rent-Ledger-System`

2. **Spin up the environment:**
   `docker compose up --build -d`

3. **Verify running containers:**
   `docker ps`

4. **Access the application:**
   Open your browser and navigate to `http://localhost:8000/`.

---

## 🧰 Summary of Included Features

* **House & Owner Management:** Map unique House IDs to specific owners with default rent baselines.
* **Flexible Invoicing:** Dynamic billing calculator incorporating electricity units, water costs, and recurring/quarterly maintenance fees.
* **Multi-Channel Payment Processing:** Supports UPI app selection (Google Pay, PhonePe, Paytm, BHIM), Credit/Debit Cards, and Net Banking options.
* **Failure Simulation Mode:** Integrated checkbox testing allowing developers to observe failed payment processing workflows and ledger status updates.
* **Real-time Tenant Summary Modal:** Embedded interface detailing total pending arrears and last recorded payment dates per tenant.
