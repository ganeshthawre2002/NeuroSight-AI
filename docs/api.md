# NeuroSight AI API Documentation

## Overview

The NeuroSight AI API provides RESTful endpoints for accessing customer churn analytics, business KPIs, and machine learning predictions.

**Base URL**

```
http://127.0.0.1:8000
```

---

# API Endpoints

## GET /

### Description

Health check endpoint.

### Response

```json
{
  "message": "NeuroSight AI API is running."
}
```

---

## GET /kpis

### Description

Returns key business metrics for the customer base.

### Response

```json
{
  "total_customers": 7043,
  "churned_customers": 1869,
  "churn_rate": 26.54,
  "avg_monthly_charge": 64.76,
  "avg_tenure": 32.37
}
```

---

## GET /contract_churn

### Description

Returns churn rates grouped by contract type.

### Response

```json
[
  {
    "Contract": "Month-to-month",
    "churn_rate": 42.71
  },
  {
    "Contract": "One year",
    "churn_rate": 11.27
  }
]
```

---

## GET /tenure_churn

### Description

Returns churn rates grouped by customer tenure.

### Response

```json
[
  {
    "tenure_group": "0-12 Months",
    "churn_rate": 47.5
  }
]
```

---

## GET /payment_method_churn

### Description

Returns churn analysis grouped by payment method.

### Response

```json
[
  {
    "PaymentMethod": "Electronic check",
    "churn_rate": 45.3
  }
]
```

---

## GET /customer_risk_segments

### Description

Returns customer records with assigned business risk segments.

### Response

```json
[
  {
    "customerID": "7590",
    "risk_segment": "Critical Risk"
  }
]
```

---

## GET /revenue_risk

### Description

Calculates revenue exposure by customer risk segment.

### Response

```json
[
  {
    "risk_segment": "Critical Risk",
    "customers": 845,
    "total_revenue": 65231.47,
    "revenue_at_risk": 28114.63
  }
]
```

---

## POST /predict

### Description

Predicts whether a customer is likely to churn using the trained machine learning model.

### Request Body

```json
{
  "gender": "Male",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "tenure": 24,
  "PhoneService": "Yes",
  "MultipleLines": "No",
  "InternetService": "Fiber optic",
  "OnlineSecurity": "No",
  "OnlineBackup": "Yes",
  "DeviceProtection": "No",
  "TechSupport": "No",
  "StreamingTV": "Yes",
  "StreamingMovies": "Yes",
  "Contract": "Month-to-month",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Electronic check",
  "MonthlyCharges": 89.5,
  "TotalCharges": 2148.0
}
```

### Response

```json
{
  "prediction": "Yes",
  "probability": 0.8732
}
```

---

# HTTP Status Codes

| Code | Meaning                        |
| ---- | ------------------------------ |
| 200  | Request completed successfully |
| 400  | Invalid request data           |
| 404  | Resource not found             |
| 422  | Validation error               |
| 500  | Internal server error          |

---

# Technologies

* FastAPI
* Pydantic
* SQLAlchemy
* PostgreSQL
* Scikit-learn
* Streamlit

---

# Interactive API Documentation

Once the FastAPI server is running, interactive documentation is available at:

* Swagger UI: `http://127.0.0.1:8000/docs`
* ReDoc: `http://127.0.0.1:8000/redoc`
