import streamlit as st

from app.ui.kpi_cards import render_kpi_cards
from app.ui.executive_summary import render_executive_summary
from app.ui.charts import render_charts
from app.ui.risk_analysis import render_risk_analysis
from app.ui.ai_insights import render_ai_insights
from app.ui.about import render_about
from app.ui.prediction import prediction_page



#### Page Configuration


st.set_page_config(
    page_title="NeuroSight AI",
    layout="wide"
)



##### Sidebar Navigation


st.sidebar.title(" NeuroSight AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Prediction",
        "About"
    ]
)


###### Dashboard Page


if page == "Dashboard":

    st.title(" NeuroSight AI")
    st.caption("Customer Churn Intelligence Platform")

    st.divider()

    render_kpi_cards()

    st.divider()

    render_executive_summary()

    st.divider()

    render_charts()

    st.divider()

    render_risk_analysis()

    st.divider()

    render_ai_insights()



##### Prediction Page


elif page == "Prediction":

    prediction_page()



##### About Page


elif page == "About":

    render_about()