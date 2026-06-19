from sqlalchemy import create_engine
import pandas as pd

##### PostgreSQL Connection ###
engine = create_engine(
    "postgresql://postgres:17032004@host.docker.internal:5433/neurosight"

)
   


def get_total_customers():
    query = """
    SELECT COUNT(*) AS total_customers
    FROM customers
    """
    return pd.read_sql(query, engine).iloc[0, 0]


def get_churned_customers():
    query = """
    SELECT COUNT(*) AS churned_customers
    FROM customers
    WHERE "Churn" = 'Yes'
    """
    return pd.read_sql(query, engine).iloc[0, 0]


def get_churn_rate():
    query = """
    SELECT
        ROUND(
            (
                100.0 *
                SUM(CASE WHEN "Churn"='Yes' THEN 1 ELSE 0 END)
                / COUNT(*)
            )::numeric,
            2
        ) AS churn_rate
    FROM customers
    """
    return pd.read_sql(query, engine).iloc[0, 0]


def get_avg_monthly_charge():
    query = """
    SELECT AVG("MonthlyCharges") AS avg_monthly_charge
    FROM customers
    """
    value = pd.read_sql(query, engine).iloc[0, 0]
    return round(float(value), 2)


def get_avg_tenure():
    query = """
    SELECT AVG(tenure) AS avg_tenure
    FROM customers
    """
    value = pd.read_sql(query, engine).iloc[0, 0]
    return round(float(value), 2)


def get_contract_churn():
    query = """
    SELECT
        "Contract",
        ROUND(
            (
                100.0 *
                SUM(CASE WHEN "Churn"='Yes' THEN 1 ELSE 0 END)
                / COUNT(*)
            )::numeric,
            2
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
    
    ROUND(
        (
            100.0 *
            SUM(CASE WHEN "Churn"='Yes' THEN 1 ELSE 0 END)
            / COUNT(*)
        )::numeric,
        2
    ) AS churn_rate
FROM customers
GROUP BY
    CASE
        WHEN tenure <= 12 THEN '0-12 Months'
        WHEN tenure <= 24 THEN '12-24 Months'
        WHEN tenure <= 48 THEN '24-48 Months'
        ELSE '48+ Months'
    END
ORDER BY MIN(tenure)
"""
    return pd.read_sql(query, engine)



def get_payment_method_churn():
    query = """
    SELECT
        "PaymentMethod",

        ROUND(
            (
                100.0 *
                SUM(
                    CASE
                        WHEN "Churn" = 'Yes' THEN 1
                        ELSE 0
                    END
                )
                / COUNT(*)
            )::numeric,
            2
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
            WHEN "Contract" = 'one year' THEN 'Medium Risk'
            ELSE 'Low Risk'
        END AS risk_segment,
        
        COUNT(*) AS customers,

        ROUND(SUM("MonthlyCharges"):: numeric, 2) AS total_revenue,

        ROUND(
            (
                SUM(CASE WHEN "Churn" = 'Yes' THEN "MonthlyCharges" ELSE 0 END)
            )::numeric, 2) AS revenue_at_risk

FROM customers
GROUP BY risk_segment
ORDER BY revenue_at_risk DESC
    """

    return pd.read_sql(query, engine)









if __name__ == "__main__":
    print("Total Customers:", get_total_customers())
    print("Churned Customers:", get_churned_customers())
    print("Churn Rate:", get_churn_rate(), "%")
    print("Average Monthly Charge:", get_avg_monthly_charge())
    print("Average Tenure:", get_avg_tenure())

    print("\nContract Churn Analysis")
    print(get_contract_churn())

    print("\nTenure Churn")
    print(get_tenure_churn())

    print("\nPayment Method Churn")
    print(get_payment_method_churn())
    print("Customer Segment Risk:", get_customer_risk_segments())
    print("Revenue Risk:", get_revenue_risk())