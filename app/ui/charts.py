import requests
import pandas as pd
import streamlit as st
import plotly.express as px

from app.config import API_URL


def render_charts():

    # ============================
    # Contract Churn
    # ============================

    st.header("Contract Churn Analysis")

    contract_df = requests.get(
        f"{API_URL}/contract_churn",
        timeout=5
    ).json()

    contract_df = pd.DataFrame(contract_df)

    fig = px.bar(
        contract_df,
        x="Contract",
        y="churn_rate",
        title="Customer Churn Rate by Contract Type"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # ============================
    # Tenure Churn
    # ============================

    st.header("Tenure Churn Analysis")

    tenure_df = requests.get(
        f"{API_URL}/tenure_churn",
        timeout=5
    ).json()

    tenure_df = pd.DataFrame(tenure_df)

    fig = px.bar(
        tenure_df,
        x="tenure_group",
        y="churn_rate",
        title="Customer Churn Rate by Tenure Group"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # ============================
    # Payment Method Churn
    # ============================

    st.header("Payment Method Churn Analysis")

    payment_df = requests.get(
        f"{API_URL}/payment_method_churn",
        timeout=5
    ).json()

    payment_df = pd.DataFrame(payment_df)

    fig = px.bar(
        payment_df,
        x="PaymentMethod",
        y="churn_rate",
        title="Customer Churn Rate by Payment Method"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()