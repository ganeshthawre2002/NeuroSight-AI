import pandas as pd

from app.ml.utils import load_model


model = load_model()


def predict_customer(customer_data: dict):

    df = pd.DataFrame([customer_data])

    prediction = model.predict(df)[0]

    probability = model.predict_proba(df)[0][1]

    return {
        "prediction": "Yes" if prediction == 1 else "No",
        "probability": round(float(probability), 4)
    }