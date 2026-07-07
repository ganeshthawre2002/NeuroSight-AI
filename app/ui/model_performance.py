import streamlit as st
import pandas as pd
import plotly.express as px


def render_model_performance():

    st.title(" Model Performance")
    st.caption("Evaluation of the Customer Churn Prediction Model")

    st.divider()

    # =====================================
    # Performance Metrics
    # =====================================

    st.subheader("Overall Performance")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric("Accuracy", "80.5%")

    with col2:
        st.metric("Precision", "68.4%")

    with col3:
        st.metric("Recall", "55.1%")

    with col4:
        st.metric("F1 Score", "61.0%")

    with col5:
        st.metric("ROC-AUC", "84.2%")

    st.divider()

    # =====================================
    # Confusion Matrix
    # =====================================

    st.subheader("Confusion Matrix")

    confusion = pd.DataFrame(
        {
            "Predicted No": [929, 168],
            "Predicted Yes": [107, 205]
        },
        index=[
            "Actual No",
            "Actual Yes"
        ]
    )

    st.dataframe(
        confusion,
        use_container_width=True
    )

    st.divider()

    # =====================================
    # Classification Report
    # =====================================

    st.subheader("Classification Report")

    report = pd.DataFrame(
        {
            "Precision": [0.85, 0.66],
            "Recall": [0.90, 0.55],
            "F1 Score": [0.87, 0.60],
            "Support": [1036, 373]
        },
        index=[
            "No Churn",
            "Churn"
        ]
    )

    st.dataframe(
        report,
        use_container_width=True
    )

    st.divider()

    # =====================================
    # Metric Visualization
    # =====================================

    st.subheader("Performance Comparison")

    metrics = pd.DataFrame(
        {
            "Metric": [
                "Accuracy",
                "Precision",
                "Recall",
                "F1 Score",
                "ROC-AUC"
            ],
            "Score": [
                80.5,
                68.4,
                55.1,
                61.0,
                84.2
            ]
        }
    )

    fig = px.bar(
        metrics,
        x="Metric",
        y="Score",
        text="Score",
        title="Model Evaluation Metrics"
    )

    fig.update_traces(texttemplate="%{text:.1f}%", textposition="outside")

    fig.update_layout(
        yaxis_title="Percentage",
        xaxis_title="",
        height=450
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # =====================================
    # Model Summary
    # =====================================

    st.subheader("Model Summary")

    st.info(
        """
Model: Logistic Regression

Training Dataset: Telco Customer Churn

Algorithm: Logistic Regression

Features Used: 19

Training Split: 80%

Testing Split: 20%

The model demonstrates strong overall accuracy and ROC-AUC.
Recall can be further improved by feature engineering, hyperparameter tuning,
or experimenting with ensemble models such as Random Forest or XGBoost.
"""
    )

    st.divider()

    # =====================================
    # Future Improvements
    # =====================================

    st.subheader("Future Improvements")

    st.success("""
 Hyperparameter Tuning

 Feature Engineering

 Cross Validation

 SHAP Explainability

 Probability Calibration

 XGBoost Comparison

 Random Forest Benchmark

 Model Monitoring

 Automatic Retraining Pipeline
""")