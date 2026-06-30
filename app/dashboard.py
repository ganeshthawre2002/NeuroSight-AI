import requests
import streamlit as st
import plotly.express as px

from insight_engine import generate_insights

from kpi_service import (
    get_contract_churn,
    get_tenure_churn,
    get_payment_method_churn,
    get_customer_risk_segments,
    get_revenue_risk,
)


######page configuration ####
st.set_page_config(
    page_title="Neurosight AI",
    layout="wide"
)


#### header ####
st.markdown("# Neurosight AI")
st.markdown("### Cutomer Churn Intelligence Platform")

st.divider()

#### kpis  ### API Configuration ###

API_URL = "http://127.0.0.1:8000"

#### KPI section ####

try:
    response = requests.get(
        f"{API_URL}/kpis",
        timeout=5
    )

    response.raise_for_status()

    kpis = response.json()

except Exception as e:
    st.error(f"Unabe to connect to FastAPI: {e}")
    st.stop()


col1, col2, col3, col4, col5, = st.columns(5)

with col1:
    st.metric(
        label="Total Customers",
        value=kpis["total_customers"]
    )

with col2:
    st.metric(
        label="Churned Customers",
        value=kpis["churned_customers"] 
    )

with col3:
    st.metric(
        label="Churn Rate",
        value=f"{kpis['churn_rate']}%"
    )   

with col4:
    st.metric(
        label="Average Monthly Charge",
        value=f"${kpis['avg_monthly_charge']:.2f}"
    )

with col5:
    st.metric(
        label="Average Tenure",
        value=f"{kpis['avg_tenure']:.2f} months"
    )

st.divider()


###### executive summary #####
st.header("Executive Summary")

st.success("""
Key Findings:

• Overall churn rate is 26.54%

• Month-to-month customers represent the highest-risk segment

• First-year customers exhibit the greatest churn tendency

• Long-term contracts dramatically improve retention

• Customers who churn typically have higher monthly charges

• Retention strategies should prioritize early-stage customers and contract upgrades
""")


##### contract churn analysis #####
st.header("Contract Churn Analysis")

contract_df = get_contract_churn()

fig1 = px.bar(
    contract_df,
    x="Contract",
    y="churn_rate",
    title= "Customer Churn Rate by Contract Type"
)

st.plotly_chart(fig1, use_container_width=True)

st.divider()

##### tenure churn analysis #####
st.header("Tenure Churn Analysis")

tenure_df = get_tenure_churn()

fig2 = px.bar(
    tenure_df,
    x="tenure_group",
    y="churn_rate",
    title="Customer Churn Rate by Tenure Group"
)

st.plotly_chart(fig2, use_container_width=True)

st.divider()    

##### payment method churn analysis #####
st.header("Payment Method Churn Analysis")      

payment_df = get_payment_method_churn()

fig3 = px.bar(
    payment_df,
    x="PaymentMethod",
    y="churn_rate",
    title= "Customer Churn Rate by Payment Method"
)

st.plotly_chart(fig3, use_container_width=True)

st.divider()    




###### customer segment risk #####

st.divider()

st.header("Customer Segment Risk")


#### loading data ####
risk_df = get_customer_risk_segments()


#### Creating summary 
risk_summary = risk_df["risk_segment"].value_counts()


#### layout 
col1, col2 = st.columns(2)

with col1:  
    st.subheader("Risk Table")
    st.dataframe(risk_summary)

with col2:
    st.subheader("Risk Distribution")
    fig = px.pie(
        values=risk_summary.values,
        names=risk_summary.index,
        title="Customer Risk Distribution"
        )
    
    st.plotly_chart(fig, use_container_width=True)


##### Revenue Risk Analysis #####

st.divider()

st.header("Revenue Risk Analysis")

revenue_df = get_revenue_risk()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Revenue Risk Table")
    st.dataframe(revenue_df)

with col2:
    fig = px.bar(
        revenue_df,
        x="risk_segment",
        y="revenue_at_risk",
        title="Revenue At Risk by Risk Segment"
    )

    st.plotly_chart(fig, use_container_width=True
    )











#### AI Bussiness Recommendations ####

insights = generate_insights()

for insight  in insights:
    st.success(insight)

##### About Section #####

st.divider()

st.header("About NeuroSight AI")

st.write("""
NeuroSight AI is an AI-powered Customer Churn Intelligence Platform that combines analytics, machine learning, and business intelligence to identify churn risk and support data-driven retention strategies.
""")

st.subheader("Current Capabilities")

st.markdown("""
- Data Ingestion & ETL
- PostgreSQL Data Warehouse
- Dockerized Database
- KPI Service Layer
- FastAPI Backend
- Customer Churn Analytics
- Machine Learning Prediction
- Executive Insights
- Interactive Streamlit Dashboard
""")

st.subheader("Upcoming Features")

st.markdown("""
- API-driven Analytics Dashboard
- AI Copilot
- Executive PDF Reports
- Automated Model Retraining
- Cloud Deployment
- User Authentication
- Monitoring & Logging
""")