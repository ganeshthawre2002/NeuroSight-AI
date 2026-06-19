from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "postgresql://postgres:17032004@host.docker.internal:5433/neurosight"
)

query = """
SELECT
"Contract",
CASE 
WHEN tenure < 12 THEN '0-12 Months'
WHEN tenure < 24 THEN '12-24 Months'
WHEN tenure < 48 THEN '24-48 Months'
ELSE '48+ Months'
END AS tenure_group,
COUNT(*) AS customers,
SUM(
CASE WHEN "Churn" ='Yes'
THEN 1 ELSE 0 END
) AS churned
FROM customers
GROUP BY "Contract", tenure_group;"""

df = pd.read_sql(query, engine)

df["churn_rate"] =(
    df["churned"] / df["customers"] * 100
).round(2)

highest = df.sort_values(
    "churn_rate", ascending=False
).iloc[0]

print("\n=== NeuroSight Executive Insight ===\n")


print(
    f"Highest risk segment: "
    f"{highest['Contract']} | "
    f"{highest['tenure_group']}"
)


print(
    f"Churn Rate:"
    f"{highest['churn_rate']}%"
)


def generate_insights():

    insights = []

    insights.append(
        "Month-to-Month customers have the highest churn risk andshould be targeted with contract conversin campaigns.")
    
    insights.append(
        "Customers within their first 12 months represent the most vulnerable retention segment."
    )

    insights.append(
        "Long-term contracts significantly reduce customer churn."
    )

    insights.append(
        "Retention programs should focus on onboarding, engagements, and loaylty incentives."
    )

    return insights


