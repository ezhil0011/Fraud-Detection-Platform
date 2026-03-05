# Fraud Detection Platform

A **Machine Learning powered Fraud Detection System** that analyzes financial transactions and predicts whether a transaction is fraudulent or legitimate in real-time.

This project demonstrates how **AI, APIs, and a web dashboard** can be combined to build a modern fraud detection platform similar to systems used in fintech companies.

---

# Features

*  **Real-Time Fraud Detection** using Machine Learning
*  **FastAPI Backend** for fraud prediction API
*  **Interactive Dashboard** for testing transactions
*  **Random Forest ML Model** trained on transaction data
*  **REST API Endpoint** for fraud prediction
*  **React Frontend Dashboard**

---

#  System Architecture

```
User Transaction
        │
        ▼
React Dashboard
        │
        ▼
FastAPI Backend
        │
        ▼
Machine Learning Model
        │
        ▼
Fraud Prediction
```

---

#  Project Structure

```
fraud-detection-platform
│
├── backend
│   ├── app
│   │   ├── main.py
│   │   ├── fraud_model.py
│   │   └── schemas.py
│   │
│   └── ml
│       ├── train_model.py
│       └── model.pkl
│
├── data
│   └── transactions.csv
│
├── dashboard
│   ├── src
│   │   └── App.js
│   └── package.json
│
└── README.md
```

---

#  Installation

## 1️ Clone the Repository

```
git clone https://github.com/yourusername/fraud-detection-platform.git
cd fraud-detection-platform
```

---

#  Train the Machine Learning Model

Run:

```
python backend/ml/train_model.py
```

This will generate:

```
backend/ml/model.pkl
```

---

#  Start the Fraud Detection API

Run the FastAPI server:

```
uvicorn backend.app.main:app --reload
```

Open the API documentation:

```
http://127.0.0.1:8000/docs
```

---

#  Start the Dashboard

Go to the dashboard folder:

```
cd dashboard
```

Start the React app:

```
npm start
```

Open:

```
http://localhost:3000
```

---

#  API Endpoint

### POST `/predict`

Example request:

```
{
  "amount": 5000,
  "transaction_type": 1,
  "account_age_days": 20,
  "location_risk": 1
}
```

Example response:

```
{
  "fraud_probability": 0.95,
  "status": "BLOCKED"
}
```

---

#  Machine Learning Model

Algorithm used:

* Random Forest Classifier

Features used:

* Transaction Amount
* Transaction Type
* Account Age
* Location Risk

---

#  Technologies Used

* Python
* FastAPI
* Scikit-learn
* React
* Pandas
* NumPy

---

#  Future Improvements

*  Real-time fraud monitoring charts
*  Fraud location heatmaps
*  Transaction streaming using Kafka
*  Docker containerization
*  Cloud deployment

---

#  License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

Developed as a **Machine Learning & Full-Stack Project** demonstrating real-time fraud detection systems used in financial technology platforms.
 
 
 
 
 
 
 
 
 # Fraud-Detection-Platform
