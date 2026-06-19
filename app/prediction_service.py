import pandas as pd 
import joblib

### load model #
model = joblib.load("models/churn_model.pkl")

### load dataset #
df = pd.read_csv("data/telco_churn.csv")

### data cleaning #
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")


df = df.dropna()

customer_ids = df["customerID"]

#### romoving id ####
df = df.drop("customerID", axis=1)

### encode target ##
df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})


## one hot encode ###
df_encoded = pd.get_dummies(df, drop_first=True)


#### feature ##
X = df_encoded.drop("Churn", axis=1)


#### probabilities ##
probabilities = model.predict_proba(X)

results = pd.DataFrame({
    "CustomerID": customer_ids,
    "Churn_Probability:": probabilities[:, 1]
})

results = results.sort_values(by="Churn_Probability:", ascending=False) 

print("\nTop 20 Highest Risk Customers\n")
print(results.head(20))