from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "postgresql://postgres:17032004@localhost:5433/neurosight"
)

try:
    df = pd.read_sql(
        "SELECT table_name FROM information_schema.tables WHERE table_schema='public'",
        engine
    )

    print(df)

except Exception as e:
    print(e)
    