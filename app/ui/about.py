import streamlit as st


def render_about():

    st.header("About NeuroSight AI")

    st.write(
        """
NeuroSight AI is an AI-powered Customer Churn Intelligence Platform that combines
Data Engineering, Business Intelligence, Machine Learning, and Artificial Intelligence
to help organizations predict customer churn and improve retention strategies.
"""
    )

    st.subheader("Current Capabilities")

    st.markdown("""
- Data Ingestion & ETL Pipeline
- PostgreSQL Data Warehouse
- Dockerized Database
- FastAPI Backend
- REST API Architecture
- Streamlit Dashboard
- KPI Analytics
- Customer Risk Segmentation
- Revenue Risk Analysis
- AI Business Recommendations
""")

    st.subheader("Upcoming Features")

    st.markdown("""
- Churn Prediction API
- AI Copilot
- Executive PDF Reports
- Model Monitoring
- Automated Retraining
- User Authentication
- Cloud Deployment
- CI/CD Pipeline
- Observability & Logging
""")

    st.divider()