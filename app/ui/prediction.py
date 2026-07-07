import requests
import streamlit as st

from app.config import API_URL


def prediction_page():

    st.title(" AI Customer Churn Prediction")

    st.write(
        "Enter customer information below and let the AI model predict the customer's churn risk."
    )

    st.divider()

    with st.form("prediction_form"):

        gender = st.selectbox("Gender", ["Male", "Female"])

        senior = st.selectbox("Senior Citizen", [0, 1])

        partner = st.selectbox("Partner", ["Yes", "No"])

        dependents = st.selectbox("Dependents", ["Yes", "No"])

        tenure = st.number_input(
            "Tenure (Months)",
            min_value=0,
            max_value=100,
            value=12
        )

        phone = st.selectbox(
            "Phone Service",
            ["Yes", "No"]
        )

        multiple = st.selectbox(
            "Multiple Lines",
            [
                "Yes",
                "No",
                "No phone service"
            ]
        )

        internet = st.selectbox(
            "Internet Service",
            [
                "DSL",
                "Fiber optic",
                "No"
            ]
        )

        online_security = st.selectbox(
            "Online Security",
            [
                "Yes",
                "No",
                "No internet service"
            ]
        )

        backup = st.selectbox(
            "Online Backup",
            [
                "Yes",
                "No",
                "No internet service"
            ]
        )

        device = st.selectbox(
            "Device Protection",
            [
                "Yes",
                "No",
                "No internet service"
            ]
        )

        tech = st.selectbox(
            "Tech Support",
            [
                "Yes",
                "No",
                "No internet service"
            ]
        )

        tv = st.selectbox(
            "Streaming TV",
            [
                "Yes",
                "No",
                "No internet service"
            ]
        )

        movies = st.selectbox(
            "Streaming Movies",
            [
                "Yes",
                "No",
                "No internet service"
            ]
        )

        contract = st.selectbox(
            "Contract",
            [
                "Month-to-month",
                "One year",
                "Two year"
            ]
        )

        paperless = st.selectbox(
            "Paperless Billing",
            [
                "Yes",
                "No"
            ]
        )

        payment = st.selectbox(
            "Payment Method",
            [
                "Electronic check",
                "Mailed check",
                "Bank transfer (automatic)",
                "Credit card (automatic)"
            ]
        )

        monthly = st.number_input(
            "Monthly Charges ($)",
            min_value=0.0,
            value=75.0
        )

        total = st.number_input(
            "Total Charges ($)",
            min_value=0.0,
            value=900.0
        )

        submit = st.form_submit_button("🔍 Predict Churn")

    if submit:

        payload = {
            "gender": gender,
            "SeniorCitizen": senior,
            "Partner": partner,
            "Dependents": dependents,
            "tenure": tenure,
            "PhoneService": phone,
            "MultipleLines": multiple,
            "InternetService": internet,
            "OnlineSecurity": online_security,
            "OnlineBackup": backup,
            "DeviceProtection": device,
            "TechSupport": tech,
            "StreamingTV": tv,
            "StreamingMovies": movies,
            "Contract": contract,
            "PaperlessBilling": paperless,
            "PaymentMethod": payment,
            "MonthlyCharges": monthly,
            "TotalCharges": total
        }

        try:

            response = requests.post(
                f"{API_URL}/predict",
                json=payload,
                timeout=10
            )

            response.raise_for_status()

            result = response.json()

        except Exception as e:

            st.error(f"Unable to connect to Prediction API.\n\n{e}")
            st.stop()

        probability = result["probability"]

        st.divider()

        st.header("Prediction Result")

        if result["prediction"] == "Yes":

            st.error(" High Churn Risk Customer")

            st.metric(
                "Churn Probability",
                f"{probability:.2%}"
            )

            st.progress(probability)

            st.warning("""
###  Recommended Business Actions

- Contact the customer within 48 hours.
- Offer a personalized retention discount.
- Recommend upgrading to a long-term contract.
- Assign the customer to the retention team.
- Schedule a customer satisfaction follow-up.
""")

        else:

            st.success(" Customer Likely to Stay")

            st.metric(
                "Retention Probability",
                f"{(1 - probability):.2%}"
            )

            st.progress(1 - probability)

            st.info("""
###  Recommended Actions

- Continue regular customer engagement.
- Promote premium products and services.
- Encourage loyalty rewards.
- Offer referral incentives.
""")

        st.divider()

        st.subheader("Prediction Confidence")

        confidence = max(probability, 1 - probability)

        st.metric(
            "Model Confidence",
            f"{confidence:.2%}"
        )

        st.progress(confidence)

        st.divider()

        with st.expander(" Developer Details"):

            st.json(result)