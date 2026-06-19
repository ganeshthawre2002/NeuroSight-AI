from sqlalchemy import create_engine
import pandas as pd 

engine = create_engine(
    "postgresql://postgres:17032004@host.docker.internal:5433/neurosight"

)

query = """
SELECT
"Contract",
COUNT(*) AS customers,
SUM(
CASE WHEN "Churn" ='Yes'
THEN 1 ELSE 0 END
) AS churn
FROM customers
GROUP BY "Contract";"""


df = pd.read_sql(query, engine)

print(df)