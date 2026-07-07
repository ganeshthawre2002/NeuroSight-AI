# NeuroSight AI

> **An End-to-End AI-Powered Customer Churn Intelligence Platform**

NeuroSight AI is a production-style data analytics and machine learning application that combines **Data Engineering**, **Business Intelligence**, **Machine Learning**, **REST APIs**, and **Interactive Dashboards** into one complete system.

The platform enables organizations to analyze customer churn, identify high-risk customers, estimate revenue at risk, and generate AI-assisted business insights.

---

# Project Highlights

* End-to-End Data Pipeline
* PostgreSQL Data Warehouse
* ETL Pipeline (Python)
* FastAPI REST Backend
* Streamlit Dashboard
* Machine Learning Churn Prediction
* Interactive Business Visualizations
* Customer Risk Segmentation
* Revenue Risk Analysis
* AI Business Insights
* Docker Support
* Modular Project Architecture

---

# Technology Stack

| Layer            | Technology    |
| ---------------- | ------------- |
| Language         | Python        |
| Database         | PostgreSQL    |
| Backend          | FastAPI       |
| Frontend         | Streamlit     |
| Machine Learning | Scikit-learn  |
| Visualization    | Plotly        |
| ORM              | SQLAlchemy    |
| Containerization | Docker        |
| Environment      | python-dotenv |

---

# System Architecture

```text
                 CSV Dataset
                      │
                      ▼
              ETL Pipeline
                      │
                      ▼
         PostgreSQL Data Warehouse
                      │
                      ▼
             KPI Service Layer
                      │
          ┌───────────┴────────────┐
          ▼                        ▼
      FastAPI REST API      ML Prediction Engine
          │                        │
          └───────────┬────────────┘
                      ▼
             Streamlit Dashboard
                      │
                      ▼
                 Business Users
```

---

# Features

## Business Analytics

* Executive KPI Dashboard
* Customer Churn Analysis
* Contract Analysis
* Tenure Analysis
* Payment Method Analysis
* Revenue Risk Dashboard
* Customer Risk Segmentation

## Machine Learning

* Logistic Regression Model
* Probability-Based Predictions
* Model Evaluation Metrics
* Real-Time Prediction API

## Engineering

* Modular Architecture
* RESTful APIs
* Dockerized Database
* Environment Configuration
* Production-Style Folder Structure

---

# Project Structure

```text
NeuroSight-AI/
│
├── app/
│   ├── ml/
│   ├── ui/
│   ├── api.py
│   ├── dashboard.py
│   ├── etl.py
│   ├── prediction_service.py
│   ├── kpi_service.py
│   └── ...
│
├── data/
├── docs/
├── models/
├── sql/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# Machine Learning Pipeline

1. Load customer dataset
2. Data preprocessing
3. Feature engineering
4. Train Logistic Regression model
5. Evaluate model performance
6. Save trained model
7. Serve predictions through FastAPI
8. Display results in Streamlit

---

# API Endpoints

| Method | Endpoint                | Description               |
| ------ | ----------------------- | ------------------------- |
| GET    | /                       | Health Check              |
| GET    | /kpis                   | Business KPIs             |
| GET    | /contract_churn         | Contract Analysis         |
| GET    | /tenure_churn           | Tenure Analysis           |
| GET    | /payment_method_churn   | Payment Method Analysis   |
| GET    | /customer_risk_segments | Risk Segments             |
| GET    | /revenue_risk           | Revenue Analysis          |
| POST   | /predict                | Customer Churn Prediction |

Interactive API documentation:

* Swagger UI: `http://127.0.0.1:8000/docs`
* ReDoc: `http://127.0.0.1:8000/redoc`

---

# Dashboard Modules

* KPI Dashboard
* Executive Summary
* Churn Analytics
* Risk Analysis
* AI Insights
* Customer Prediction
* Model Performance
* About Page

---

# Getting Started

Clone the repository:

```bash
git clone https://github.com/your-username/NeuroSight-AI.git
cd NeuroSight-AI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the ETL pipeline:

```bash
python app/etl.py
```

Train the model:

```bash
python app/ml/train.py
```

Start the API:

```bash
python -m uvicorn app.api:app --reload
```

Start the dashboard:

```bash
streamlit run app/dashboard.py
```

---

# Documentation

Detailed documentation is available in the `docs/` directory:

* architecture.md
* api.md
* model.md
* deployment.md

---

# Future Roadmap

* Explainable AI (SHAP)
* Model Monitoring
* MLflow Integration
* Automated Retraining
* CI/CD Pipeline
* Cloud Deployment
* Authentication & Authorization
* Role-Based Access Control
* Real-Time Prediction Services
* Kubernetes Deployment

---

# Author

**Ganesh**

AI Data Engineer | Data Analytics | Analytics Engineering | Data Engineering | Machine Learning | AI Engineering | FastAPI | PostgreSQL | Streamlit | Docker | Scikit-learn

---

# License

This project is intended for educational and portfolio purposes.
