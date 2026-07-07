# NeuroSight AI Architecture

## Overview

NeuroSight AI is an end-to-end AI-powered Customer Churn Intelligence Platform designed to help businesses identify customers at risk of leaving and support data-driven retention strategies.

The platform integrates data engineering, analytics, machine learning, REST APIs, and interactive business dashboards into a single production-style application.

---

# System Architecture

```
                CSV Dataset
                     │
                     ▼
            ETL Pipeline (Python)
                     │
                     ▼
          PostgreSQL Data Warehouse
                     │
                     ▼
          KPI Service Layer (SQLAlchemy)
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
     FastAPI REST API     Machine Learning Model
          │                     │
          └──────────┬──────────┘
                     ▼
            Streamlit Dashboard
                     │
                     ▼
               Business Users
```

---

# Project Components

## 1. Data Layer

The ETL pipeline imports the Telco Customer Churn dataset, performs preprocessing, cleans missing values, converts data types, and loads the transformed data into PostgreSQL.

Responsibilities:

* Load raw CSV data
* Clean missing values
* Convert data types
* Store structured data
* Prepare data for analytics and machine learning

---

## 2. PostgreSQL Data Warehouse

PostgreSQL acts as the central analytical database.

Responsibilities:

* Store customer records
* Execute SQL aggregations
* Support analytical queries
* Serve as the single source of truth

---

## 3. KPI Service Layer

The KPI Service Layer contains reusable SQLAlchemy functions that generate business metrics.

Example KPIs:

* Total Customers
* Churn Rate
* Average Monthly Charges
* Revenue at Risk
* Customer Risk Segments

---

## 4. FastAPI Backend

FastAPI exposes business logic through REST endpoints.

Key Endpoints:

* GET /kpis
* GET /contract_churn
* GET /tenure_churn
* GET /payment_method_churn
* GET /customer_risk_segments
* GET /revenue_risk
* POST /predict

The backend acts as the communication bridge between the database, machine learning model, and frontend dashboard.

---

## 5. Machine Learning Layer

A Logistic Regression model predicts customer churn probability.

Workflow:

* Data preprocessing
* Feature engineering
* Model training
* Model evaluation
* Model serialization
* Prediction service

Evaluation metrics include:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC

---

## 6. Streamlit Dashboard

The dashboard provides business users with an interactive interface for exploring customer churn analytics.

Modules include:

* KPI Dashboard
* Executive Summary
* Churn Analytics
* Risk Analysis
* AI Business Insights
* Customer Churn Prediction
* Model Performance Dashboard

---

# Project Structure

```
app/
├── api.py
├── dashboard.py
├── etl.py
├── kpi_service.py
├── prediction_service.py
├── ml/
├── ui/
├── config.py
├── database.py
└── schemas.py
```

---

# Technology Stack

Programming Language

* Python

Backend

* FastAPI

Frontend

* Streamlit

Database

* PostgreSQL

Machine Learning

* Scikit-learn

Visualization

* Plotly

ORM

* SQLAlchemy

Containerization

* Docker

Environment Management

* python-dotenv

---

# Future Enhancements

* Cloud Deployment
* User Authentication
* Role-Based Access Control
* Automated Model Retraining
* Model Monitoring
* Explainable AI (SHAP)
* Feature Store
* CI/CD Pipeline
* Kubernetes Deployment
* Real-Time Prediction API
* Monitoring and Logging
* Business Report Generation

---

# Conclusion

NeuroSight AI demonstrates a complete end-to-end data and AI workflow, combining data engineering, analytics engineering, machine learning, API development, and business intelligence into a unified production-style application.
