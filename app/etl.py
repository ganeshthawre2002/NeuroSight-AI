from pathlib import Path

import pandas as pd

from app.database import engine


##### Project Paths


project_root = Path(__file__).parent.parent
csv_file = project_root / "data" / "telco_churn.csv"

print(f"Loading file: {csv_file}")



##### Load Dataset


df = pd.read_csv(csv_file)

print("\nDataset loaded successfully")

print("\nShape")
print(df.shape)

print("\nColumns")
print(df.columns.tolist())

print("\nData Types")
print(df.dtypes)

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())

print("\nChurn Distribution")
print(df["Churn"].value_counts())



##### Data Cleaning


# Replace blank strings with None
df["TotalCharges"] = df["TotalCharges"].replace(" ", None)

# Convert to numeric
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

print("\nTotalCharges Data Type")
print(df["TotalCharges"].dtype)

print("\nMissing TotalCharges")
print(df["TotalCharges"].isnull().sum())



#### Load into PostgreSQL


df.to_sql(
    name="customers",
    con=engine,
    if_exists="replace",
    index=False
)

print("\nData loaded into PostgreSQL successfully.")