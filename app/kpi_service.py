import pandas as pd

from app.database import engine


##### Helpers


def safe_int(value):
    if value is None:
        return 0
    return int(value)


def safe_float(value):
    if value is None:
        return 0.0
    return round(float(value), 2)


def query_dataframe(sql: str):
    return pd.read_sql(sql, engine)



##### KPIs


def get_total_customers():
    sql = """
    SELECT COUNT(*) AS total_customers
    FROM customers
    """
    return safe_int(query_dataframe(sql).iloc[0, 0])


def get_churned_customers():
    sql = """
    SELECT COUNT(*) AS churned_customers
    FROM customers
    WHERE "Churn"='Yes'
    """
    return safe_int(query_dataframe(sql).iloc[0, 0])


def get_churn_rate():
    sql = """
    SELECT
        (
            100.0 *
            SUM(CASE WHEN "Churn"='Yes' THEN 1 ELSE 0 END)
            / COUNT(*)
        ) AS churn_rate
    FROM customers
    """
    return safe_float(query_dataframe(sql).iloc[0, 0])


def get_avg_monthly_charge():
    sql = """
    SELECT AVG("MonthlyCharges")
    FROM customers
    """
    return safe_float(query_dataframe(sql).iloc[0, 0])


def get_avg_tenure():
    sql = """
    SELECT AVG(tenure)
    FROM customers
    """
    return safe_float(query_dataframe(sql).iloc[0, 0])


##### Charts


def get_contract_churn():
    sql = """
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
    return query_dataframe(sql)


def get_tenure_churn():
    sql = """
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

    GROUP BY 1

    ORDER BY MIN(tenure)
    """
    return query_dataframe(sql)


def get_payment_method_churn():
    sql = """
    SELECT
        "PaymentMethod",

        ROUND(
            (
                100.0 *
                SUM(CASE WHEN "Churn"='Yes' THEN 1 ELSE 0 END)
                / COUNT(*)
            )::numeric,
            2
        ) AS churn_rate

    FROM customers

    GROUP BY "PaymentMethod"

    ORDER BY churn_rate DESC
    """
    return query_dataframe(sql)



##### Customer Risk


def get_customer_risk_segments():
    sql = """
    SELECT
        "customerID",
        tenure,
        "MonthlyCharges",
        "Contract",
        "Churn",

        CASE

            WHEN tenure <= 12
                 AND "Contract"='Month-to-month'
                 AND "MonthlyCharges">70

                THEN 'Critical Risk'

            WHEN tenure <= 24
                 AND "Contract"='Month-to-month'

                THEN 'High Risk'

            WHEN "Contract"='One year'

                THEN 'Medium Risk'

            ELSE 'Low Risk'

        END AS risk_segment

    FROM customers
    """
    return query_dataframe(sql)


def get_revenue_risk():
    sql = """
    SELECT

        CASE

            WHEN tenure <= 12
                 AND "Contract"='Month-to-month'

                THEN 'Critical Risk'

            WHEN tenure <= 24
                 AND "Contract"='Month-to-month'

                THEN 'High Risk'

            WHEN "Contract"='One year'

                THEN 'Medium Risk'

            ELSE 'Low Risk'

        END AS risk_segment,

        COUNT(*) AS customers,

        ROUND(
            SUM("MonthlyCharges")::numeric,
            2
        ) AS total_revenue,

        ROUND(
            SUM(
                CASE
                    WHEN "Churn"='Yes'
                    THEN "MonthlyCharges"
                    ELSE 0
                END
            )::numeric,
            2
        ) AS revenue_at_risk

    FROM customers

    GROUP BY risk_segment

    ORDER BY revenue_at_risk DESC
    """

    return query_dataframe(sql)



##### Local Test


if __name__ == "__main__":

    print("Total Customers:", get_total_customers())
    print("Churned Customers:", get_churned_customers())
    print("Churn Rate:", get_churn_rate())
    print("Average Monthly Charge:", get_avg_monthly_charge())
    print("Average Tenure:", get_avg_tenure())