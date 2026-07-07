# NeuroSight AI Deployment Guide

## Overview

This guide explains how to set up and run the NeuroSight AI project locally using Docker, PostgreSQL, FastAPI, and Streamlit.

---

# Prerequisites

Before running the project, install the following software:

* Python 3.11 or later
* PostgreSQL 16+
* Docker Desktop
* Git
* VS Code (recommended)

---

# Clone the Repository

```bash
git clone https://github.com/your-username/NeuroSight-AI.git

cd NeuroSight-AI
```

---

# Create Virtual Environment

Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root.

Example:

```text
DATABASE_URL=postgresql://postgres:password@localhost:5434/neurosight

API_URL=http://127.0.0.1:8000

OPENAI_API_KEY=your_openai_api_key
```

---

# Start PostgreSQL

Using Docker:

```bash
docker compose up -d
```

Verify:

```bash
docker ps
```

---

# Load Dataset

Run the ETL pipeline:

```bash
python app/etl.py
```

This will:

* Load the CSV dataset
* Clean the data
* Create the PostgreSQL table
* Populate the database

---

# Train the Machine Learning Model

```bash
python app/ml/train.py
```

This generates the trained model file:

```text
models/churn_model.pkl
```

---

# Evaluate the Model

```bash
python app/ml/evaluate.py
```

This displays:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC
* Confusion Matrix

---

# Start FastAPI

```bash
python -m uvicorn app.api:app --reload
```

Server:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

# Start Streamlit Dashboard

Open a second terminal:

```bash
streamlit run app/dashboard.py
```

Dashboard:

```text
http://localhost:8501
```

---

# Project Workflow

```text
CSV Dataset
      │
      ▼
ETL Pipeline
      │
      ▼
PostgreSQL Database
      │
      ▼
KPI Service Layer
      │
      ▼
FastAPI Backend
      │
      ├──────────────┐
      ▼              ▼
Machine Learning   REST API
      │              │
      └──────┬───────┘
             ▼
     Streamlit Dashboard
```

---

# Docker Commands

Start containers

```bash
docker compose up -d
```

Stop containers

```bash
docker compose down
```

View running containers

```bash
docker ps
```

View logs

```bash
docker compose logs
```

---

# Troubleshooting

### Database Connection Error

* Verify PostgreSQL is running.
* Check `DATABASE_URL` in `.env`.
* Confirm the database exists.

### FastAPI Not Starting

* Ensure all Python dependencies are installed.
* Verify imports are correct.
* Check that the trained model exists.

### Streamlit Cannot Connect

* Confirm FastAPI is running.
* Verify `API_URL` matches the backend address.

### Model File Missing

Run:

```bash
python app/ml/train.py
```

---

# Future Deployment

Planned deployment targets include:

* Docker Compose
* Render
* Railway
* Azure
* AWS
* Google Cloud Platform
* Kubernetes

---

# Conclusion

Following this guide will set up the complete NeuroSight AI application, including data ingestion, machine learning, REST API services, and the interactive dashboard. The project is designed with a modular architecture that supports future enhancements, cloud deployment, and production-scale improvements.
