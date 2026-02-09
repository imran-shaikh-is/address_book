# 📘 Address Book API (FastAPI)

A minimal and clean **Address Book REST API** built using **FastAPI** and **SQLite**.  
This project allows users to manage addresses with geographic coordinates and search nearby addresses based on distance.

The API is fully testable using **FastAPI Swagger UI** — no frontend UI required.

---

## 🚀 Features

- ➕ Create new addresses with latitude & longitude
- ✏️ Update existing addresses
- ❌ Delete addresses
- 📄 Retrieve all stored addresses
- 📍 Find nearby addresses within a given distance (km)
- ✅ Input validation using Pydantic
- 🗄️ SQLite database persistence
- 📂 Structured and clean project layout
- 📝 Application-level logging

---

## 🛠️ Tech Stack

- **Python** 3.10+
- **FastAPI**
- **SQLite**
- **SQLAlchemy (ORM)**
- **Pydantic**
- **Geopy**
- **Uvicorn**

---

## 📂 Project Structure

```text
address_book/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── utils.py
│   └── logging_config.py
├── requirements.txt
└── README.md
```
---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/imran-shaikh-is/address_book.git
cd address_book
```
---
2️⃣ Create a Virtual Environment
```bash
python -m venv venv
```
Activate the environment

Linux / Mac
```bash
source venv/bin/activate
```
Windows
```bash
venv\Scripts\activate
```
---
3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
---
▶️ Run the Application
```bash
uvicorn app.main:app --reload
```
The server will start at:
```bash
http://127.0.0.1:8000
```
---
📑 API Documentation (Swagger UI)
FastAPI provides an interactive API documentation interface:
```bash
http://127.0.0.1:8000/docs
```
You can use this UI to test all available API endpoints.
---
📌 Available API Endpoints
➕ Create Address
```bash
POST /addresses/
```
📄 Get All Addresses
```bash
GET /addresses/
```
✏️ Update Address
```bash
PUT /addresses/{address_id}
```
❌ Delete Address
```bash
DELETE /addresses/{address_id}
```
📍 Find Nearby Addresses
```bash
GET /addresses/nearby?latitude=<lat>&longitude=<lon>&distance_km=<km>
```
---
📍 Distance Calculation
- Uses Geopy for accurate geodesic distance calculation
- Distance is calculated in kilometers
- Only addresses within the given radius are returned
---
🗄️ Database
- Uses SQLite
- Database file is created automatically on application startup
- Tables are created using SQLAlchemy ORM
---
📝 Logging
- Basic production-level logging is implemented
- Logs application events and errors for easier debugging
---
✅ Notes
- ❌ No authentication implemented (not required)
- ❌ No frontend UI (Swagger UI is sufficient)
- ✔ Designed to demonstrate FastAPI best practices and clean architecture

👤 Author

Imran Shaikh
---
🎯 Assignment Goal Completion

- ✔ Minimal FastAPI REST API
- ✔ SQLite persistence
- ✔ Address validation
- ✔ Distance-based address retrieval
- ✔ Clean and maintainable project structure
