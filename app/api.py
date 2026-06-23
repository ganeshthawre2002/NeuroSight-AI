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

