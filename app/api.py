from fastapi import FastAPI

from app.kpi_service import (
    get_total_customers,
    get_churned_customers,
    get_churn_rate,
    get_avg_monthly_charge,
    get_avg_tenure,
    get_contract_churn,
    get_tenure_churn,
    get_payment_method_churn,
    get_customer_risk_segments,
    get_revenue_risk,
)

from app.schemas import CustomerInput
from app.prediction_service import predict


app = FastAPI(
    title="NeuroSight AI API",
    version="1.0.0",
    description="Customer Churn Intelligence Platform API"
)


@app.get("/")
def home():
    return {
        "message": "NeuroSight AI API is running."
    }


@app.get("/kpis")
def get_kpis():

    return {
        "total_customers": get_total_customers(),
        "churned_customers": get_churned_customers(),
        "churn_rate": get_churn_rate(),
        "avg_monthly_charge": get_avg_monthly_charge(),
        "avg_tenure": get_avg_tenure(),
    }


@app.get("/contract_churn")
def contract_churn():
    return get_contract_churn().to_dict(
        orient="records"
    )


@app.get("/tenure_churn")
def tenure_churn():
    return get_tenure_churn().to_dict(
        orient="records"
    )


@app.get("/payment_method_churn")
def payment_method_churn():
    return get_payment_method_churn().to_dict(
        orient="records"
    )


@app.get("/customer_risk_segments")
def customer_risk_segments():
    return get_customer_risk_segments().to_dict(
        orient="records"
    )


@app.get("/revenue_risk")
def revenue_risk():
    return get_revenue_risk().to_dict(
        orient="records"
    )



##### ML Prediction Endpoint


@app.post("/predict")
def predict_customer(customer: CustomerInput):

    result = predict(customer.model_dump())

    return result