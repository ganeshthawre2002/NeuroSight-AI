from fastapi import FastAPI
from app.kpi_service import (
    get_total_customers,
    get_churned_customers,
    get_churn_rate,
    get_avg_monthly_charge,
    get_avg_tenure,
    get_contract_churn,
    get_customer_risk_segments,
    get_payment_method_churn,
    get_revenue_risk,
    get_tenure_churn
)

app = FastAPI(
    title="NeuroSight AI API"
)

@app.get("/kpis")
def get_kpis():
    return {
        "total_customers": get_total_customers(),
        "churned_customers": get_churned_customers(),
        "churn_rate": get_churn_rate(),
        "avg_mothly_charge": get_avg_monthly_charge(),
        "avg_tenure":get_avg_tenure,
        "tenure_churn":get_tenure_churn,
        "revenue_risk":get_revenue_risk,
        "avg_tenure":get_avg_tenure,
        "payment_mothod_churn":get_payment_method_churn,
        "risk_segments":get_customer_risk_segments

    }


@app.get("/contract_churn")
def get_contract_churn():
    return get_contract_churn().to_dict(orient="records")

@app.get("/tenure_churn")
def get_tenure_churn():
    return get_tenure_churn().to_dict(orient="records") 

@app.get("/payment_method_churn")
def get_payment_method_churn():
    return get_payment_method_churn().to_dict(orient="records") 

@app.get("/customer_risk_segments")
def get_customer_risk_segments():
    return get_customer_risk_segments().to_dict(orient="records")

@app.get("/revenue_risk")
def get_revenue_risk():
    return get_revenue_risk().to_dict(orient="records") 


