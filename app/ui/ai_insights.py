import streamlit as st

from app.insight_engine import generate_insights


def render_ai_insights():

    st.header(" AI Business Recommendations")

    insights = generate_insights()

    priorities = [
        "🔴 High Priority",
        "🟠 Medium Priority",
        "🟡 Medium Priority",
        "🟢 Long-Term Strategy",
        "🔵 Executive Insight",
    ]

    for priority, insight in zip(priorities, insights):

        with st.container(border=True):

            st.markdown(f"### {priority}")

            st.write(insight)

    st.divider()