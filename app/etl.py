from pathlib import Path
import pandas as pd



from churn_analysis import (
    calculate_kpis,
    contract_analysis,
    tech_support_analysis,
    online_security_analysis,
)


##### loading datasets ######

project_root = Path(__file__).parent.parent
csv_file = project_root / "data" / "telco_churn.csv"


df = pd.read_csv(csv_file)


#### Cleaning total charges 
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

print("\n ===== Dataset overview =====")
print("Shape:", df.shape)


print("\n ===== Missing total Charges =====")
print(df["TotalCharges"].isnull().sum())


### KPI summary 
print("\n ===== kpi summary =====")
kpis = calculate_kpis(df)


### contract analysis 
print("\n ====== contract analysis =====") 
print(contract_analysis(df))

### tech support analysis
print("\n ====== tech support analysis =====")
print(tech_support_analysis(df))    

### online security analysis
print("\n ====== online security analysis =====")
print(online_security_analysis(df))

