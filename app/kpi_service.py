import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd

load_dotenv()   

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    raise ValueError("DATABASE_URL not found. Check your .env file")

engine = create_engine(DATABASE_URL)
# =========================
# SAFE HELPER
# =========================
def safe_float(value):
    if value is None:
        return 0.0
    return round(float(value), 2)


def safe_int(value):
    if value is None:
        return 0
    return int(value)


# =========================
# KPI FUNCTIONS
# =========================

def get_total_customers():
    query = """
    SELECT COUNT(*) AS total_customers
    FROM customers
    """
    return safe_int(pd.read_sql(query, engine).iloc[0, 0])


def get_churned_customers():
    query = """
    SELECT COUNT(*) AS churned_customers
    FROM customers
    WHERE "Churn" = 'Yes'
    """
    return safe_int(pd.read_sql(query, engine).iloc[0, 0])


def get_churn_rate():
    query = """
    SELECT
        (
            100.0 *
            SUM(CASE WHEN "Churn"='Yes' THEN 1 ELSE 0 END)
            / COUNT(*)
        ) AS churn_rate
    FROM customers
    """
    value = pd.read_sql(query, engine).iloc[0, 0]
    return safe_float(value)


def get_avg_monthly_charge():
    query = """
    SELECT AVG("MonthlyCharges") AS avg_monthly_charge
    FROM customers
    """
    value = pd.read_sql(query, engine).iloc[0, 0]
    return safe_float(value)


def get_avg_tenure():
    query = """
    SELECT AVG(tenure) AS avg_tenure
    FROM customers
    """
    value = pd.read_sql(query, engine).iloc[0, 0]
    return safe_float(value)


def get_contract_churn():
    query = """
    SELECT
        "Contract",
        (
            100.0 *
            SUM(CASE WHEN "Churn"='Yes' THEN 1 ELSE 0 END)
            / COUNT(*)
        ) AS churn_rate
    FROM customers
    GROUP BY "Contract"
    ORDER BY churn_rate DESC
    """
    return pd.read_sql(query, engine)


def get_tenure_churn():
    query = """
    SELECT
        CASE
            WHEN tenure <= 12 THEN '0-12 Months'
            WHEN tenure <= 24 THEN '12-24 Months'
            WHEN tenure <= 48 THEN '24-48 Months'
            ELSE '48+ Months'
        END AS tenure_group,

        (
            100.0 *
            SUM(CASE WHEN "Churn"='Yes' THEN 1 ELSE 0 END)
            / COUNT(*)
        ) AS churn_rate

    FROM customers
    GROUP BY 1
    ORDER BY MIN(tenure)
    """
    return pd.read_sql(query, engine)


def get_payment_method_churn():
    query = """
    SELECT
        "PaymentMethod",
        (
            100.0 *
            SUM(CASE WHEN "Churn"='Yes' THEN 1 ELSE 0 END)
            / COUNT(*)
        ) AS churn_rate
    FROM customers
    GROUP BY "PaymentMethod"
    ORDER BY churn_rate DESC
    """
    return pd.read_sql(query, engine)


def get_customer_risk_segments():
    query = """
    SELECT
        "customerID",
        tenure,
        "MonthlyCharges",
        "Contract",
        "Churn",

        CASE
            WHEN tenure <= 12
                 AND "Contract" = 'Month-to-month'
                 AND "MonthlyCharges" > 70
                THEN 'Critical Risk'

            WHEN tenure <= 24
                 AND "Contract" = 'Month-to-month'
                THEN 'High Risk'

            WHEN "Contract" = 'One year'
                THEN 'Medium Risk'

            ELSE 'Low Risk'
        END AS risk_segment

    FROM customers
    """
    return pd.read_sql(query, engine)


def get_revenue_risk():
    query = """
    SELECT
        CASE
            WHEN tenure <= 12 AND "Contract" = 'Month-to-month' THEN 'Critical Risk'
            WHEN tenure <= 24 AND "Contract" = 'Month-to-month' THEN 'High Risk'
            WHEN "Contract" = 'One year' THEN 'Medium Risk'
            ELSE 'Low Risk'
        END AS risk_segment,

        COUNT(*) AS customers,

        SUM("MonthlyCharges") AS total_revenue,

        SUM(
            CASE WHEN "Churn" = 'Yes'
            THEN "MonthlyCharges"
            ELSE 0 END
        ) AS revenue_at_risk

    FROM customers
    GROUP BY risk_segment
    ORDER BY revenue_at_risk DESC
    """
    return pd.read_sql(query, engine)


# =========================
# LOCAL TEST
# =========================
if __name__ == "__main__":
    print("Total Customers:", get_total_customers())
    print("Churned Customers:", get_churned_customers())
    print("Churn Rate:", get_churn_rate(), "%")
    print("Average Monthly Charge:", get_avg_monthly_charge())
    print("Average Tenure:", get_avg_tenure())