import pandas as pd

from app.database import engine


def generate_insights():

    query = """
    SELECT
        "Contract",

        CASE
            WHEN tenure <= 12 THEN '0-12 Months'
            WHEN tenure <= 24 THEN '12-24 Months'
            WHEN tenure <= 48 THEN '24-48 Months'
            ELSE '48+ Months'
        END AS tenure_group,

        COUNT(*) AS customers,

        SUM(
            CASE
                WHEN "Churn"='Yes'
                THEN 1
                ELSE 0
            END
        ) AS churned

    FROM customers

    GROUP BY
        "Contract",
        tenure_group
    """

    df = pd.read_sql(query, engine)

    df["churn_rate"] = (
        df["churned"] / df["customers"] * 100
    ).round(2)

    highest = df.sort_values(
        "churn_rate",
        ascending=False
    ).iloc[0]

    insights = []

    insights.append(
        f"Highest churn risk is {highest['Contract']} customers in the {highest['tenure_group']} tenure group ({highest['churn_rate']}% churn)."
    )

    insights.append(
        "Month-to-month customers should be prioritized for contract upgrade campaigns."
    )

    insights.append(
        "Customers in their first year require proactive retention programs."
    )

    insights.append(
        "Long-term contracts consistently produce the lowest churn."
    )

    insights.append(
        "Retention investments should focus on high-risk segments before customer acquisition."
    )

    return insights