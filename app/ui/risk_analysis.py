import requests
import pandas as pd
import streamlit as st
import plotly.express as px

from app.config import API_URL


def render_risk_analysis():

    # ======================================
    # Customer Risk Analysis
    # ======================================

    st.header("Customer Risk Analysis")

    risk_df = requests.get(
        f"{API_URL}/customer_risk_segments",
        timeout=5
    ).json()

    risk_df = pd.DataFrame(risk_df)

    risk_summary = (
        risk_df["risk_segment"]
        .value_counts()
        .reset_index()
    )

    risk_summary.columns = [
        "Risk Segment",
        "Customers"
    ]

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Risk Table")

        st.dataframe(
            risk_summary,
            use_container_width=True
        )

    with col2:

        st.subheader("Risk Distribution")

        fig = px.pie(
            risk_summary,
            values="Customers",
            names="Risk Segment",
            title="Customer Risk Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

    # ======================================
    # Revenue Risk
    # ======================================

    st.header("Revenue Risk Analysis")

    revenue_df = requests.get(
        f"{API_URL}/revenue_risk",
        timeout=5
    ).json()

    revenue_df = pd.DataFrame(revenue_df)

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Revenue Risk Table")

        st.dataframe(
            revenue_df,
            use_container_width=True
        )

    with col2:

        fig = px.bar(
            revenue_df,
            x="risk_segment",
            y="revenue_at_risk",
            title="Revenue at Risk"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()