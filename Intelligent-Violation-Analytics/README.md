# 🚀 Intelligent Violation Analytics & Risk Scoring Engine

An AI-driven backend system that analyzes candidate violations during online assessments and calculates a dynamic risk score with automated cancellation decisions and admin analytics.

---

## 📌 Project Overview

The Intelligent Risk Scoring Engine is designed to:

- Analyze real-time violation logs
- Assign weighted risk scores
- Detect suspicious behavioral patterns
- Auto-cancel high-risk candidates
- Provide administrative analytics dashboards (API-based)

This system simulates an AI-powered proctoring backend.

---

## 🏗️ System Architecture

```
app/
│
├── main.py                  # FastAPI entry point
├── config.py                # Thresholds & configuration
│
└── risk_engine/
    ├── models.py            # Pydantic data models
    ├── scoring.py           # Risk scoring logic
    ├── patterns.py          # Pattern detection logic
    ├── cancellation.py      # Auto-cancellation rules
    └── analytics.py         # Admin analytics utilities
```

---

## ⚙️ Technologies Used

- Python 3.13
- FastAPI
- Uvicorn
- Pydantic
- REST API Architecture

---

## 🧠 Core Features

### 1️⃣ Risk Score Calculation
- Severity-based weighting (Low, Medium, High)
- Confidence score multiplier
- Cumulative scoring per candidate

### 2️⃣ Suspicious Pattern Detection
- Burst violation detection (multiple violations in short time window)
- Repeated high-severity violation detection

### 3️⃣ Auto Cancellation Logic
- Auto-cancel if score exceeds threshold
- Auto-cancel on repeated high severity violations
- Warning category for moderate risk

### 4️⃣ Admin Analytics APIs
- Overall violation summary
- Timeline view (sorted by timestamp)
- Severity distribution report

---

## 🚀 How to Run the Project

### Step 1: Install Dependencies

```bash
pip install fastapi uvicorn
```

### Step 2: Start the Server

```bash
uvicorn app.main:app --reload
```

### Step 3: Open API Documentation

Open in browser:

```
http://127.0.0.1:8000/docs
```

Swagger UI will allow full testing of all APIs.

---

## 📡 API Endpoints

### 🔹 POST `/risk/analyze`
Analyze candidate violations.

**Input:** List of violation objects  
**Output:**
- Risk score
- Risk category (Low / Medium / High)
- Cancellation decision
- Suspicious patterns
- Severity distribution

---

### 🔹 GET `/admin/summary`
Returns:
- Total violations
- Overall risk score
- Patterns detected
- Cancellation status

---

### 🔹 GET `/admin/timeline`
Returns violations sorted by timestamp.

---

### 🔹 GET `/admin/severity-distribution`
Returns aggregated severity breakdown.

---

## 📊 Sample Test Input

```json
[
  {
    "candidate_id": "U101",
    "violation_type": "phone_detected",
    "severity_level": "high",
    "confidence_score": 0.95,
    "frame_reference": "frame_01.jpg",
    "timestamp": "2026-02-20T10:30:00"
  }
]
```

---

## 🎯 Risk Classification Logic

| Score Range | Category |
|-------------|----------|
| 0 - 5       | Low      |
| 6 - 10      | Medium   |
| 11+         | High     |

---

## 🔐 Cancellation Rules

- Score exceeds cancellation threshold
- Repeated high severity violations detected
- Moderate warning if threshold not exceeded but risk rising

---

## 📈 Future Improvements

- Database integration (PostgreSQL / MongoDB)
- Real-time streaming support
- Machine Learning anomaly detection
- Dashboard UI (React / Angular)
- Role-based authentication

---

## 👨‍💻 Author

Developed as part of an advanced backend analytics system project.

---

## 🏆 Project Status

✅ Fully functional  
✅ API documented  
✅ Modular architecture  
✅ Submission ready  

---
