import streamlit as st


def render_executive_summary():

    st.header("Executive Summary")

    st.success(
        """
Key Findings:

• Overall churn rate is 26.54%

• Month-to-month customers represent the highest-risk segment

• First-year customers exhibit the greatest churn tendency

• Long-term contracts dramatically improve retention

• Customers who churn typically have higher monthly charges

• Retention strategies should prioritize early-stage customers and contract upgrades
"""
    )