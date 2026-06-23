from pathlib import Path
import pandas as pd



#### Project Root ####

project_root = Path(__file__).parent.parent

#### dataset path ####

csv_file = project_root / "data" / "telco_churn.csv"

print(f"Loading file: {csv_file}")

### loading csv ###

df = pd.read_csv(csv_file)

print("\n Dataset loaded successfully")

print("\nShape")
print(df.shape)

print("\nColumns")
print(df.columns.tolist())

print("\ndata types")
print(df.dtypes)

print("\nmissing values")
print(df.isnull().sum())

print("\nduplicate rows")
print(df.duplicated().sum())


print("\Churn Distribution")
print(df["Churn"].value_counts())

# Replace blank values with NaN
df["TotalCharges"] = df["TotalCharges"].replace(" ", None)

# Convert to numeric
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

print("\nTotalCharges dtype:")
print(df["TotalCharges"].dtype)

print("\nMissing TotalCharges:")
print(df["TotalCharges"].isnull().sum())




### connecting postgresql database 

from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:17032004@localhost:5434/neurosight"
)

df.to_sql(
    "customers",
    engine,
    if_exists="replace",
    index=False

)


print("\nData loaded into postgresql successfully")
