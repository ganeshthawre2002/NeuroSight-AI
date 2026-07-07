import requests
import streamlit as st

from app.config import API_URL


def render_kpi_cards():

    try:
        response = requests.get(
            f"{API_URL}/kpis",
            timeout=5
        )

        response.raise_for_status()

        kpis = response.json()

    except Exception as e:
        st.error(f"Unable to connect to FastAPI.\n\n{e}")
        st.stop()

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric(
            "Total Customers",
            kpis["total_customers"]
        )

    with col2:
        st.metric(
            "Churned Customers",
            kpis["churned_customers"]
        )

    with col3:
        st.metric(
            "Churn Rate",
            f"{kpis['churn_rate']}%"
        )

    with col4:
        st.metric(
            "Average Monthly Charge",
            f"${kpis['avg_monthly_charge']:.2f}"
        )

    with col5:
        st.metric(
            "Average Tenure",
            f"{kpis['avg_tenure']:.2f} months"
        )