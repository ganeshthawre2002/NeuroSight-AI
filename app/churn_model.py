import pandas as pd 
import joblib


#### loading model ###
model = joblib.load("models/churn_model.pkl")

### loading dataset ###
df = pd.read_csv("data/telco_churn.csv")


##### data cleaning ###
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

df = df.dropna()

customer_ids = df["customerID"]

### Remove ID ####
df = df.drop("customerID", axis=1)

#### encode target ###
df["Churn"] = df["Churn"].map({
    "No": 0,
    "Yes": 1
})


##### one hot encoding ###
df_encoded = pd.get_dummies(
    df,
    drop_first = True
)

##### Feature ###
X = df_encoded.drop("Churn", axis=1)

#### probabilities ##
probabilities = model.predict_proba(X)

results = pd.DataFrame({
    "CutomerID": customer_ids,
    "Churn_Probabilities": probabilities[:, 1]
})

results = results.sort_values(
    by="Churn_Probabilities",
    ascending=False
)

print("\n Top 20 Highest Risk Customers\n")
print(results.head(20))




