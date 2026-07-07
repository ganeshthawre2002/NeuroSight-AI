from pathlib import Path
import pandas as pd
import joblib


PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

DATA_PATH = PROJECT_ROOT / "data" / "telco_churn.csv"

MODEL_PATH = PROJECT_ROOT / "models" / "churn_model.pkl"


def load_dataset():
    """
    Load the Telco Churn dataset.
    """
    return pd.read_csv(DATA_PATH)


def save_model(model):
    """
    Save trained model.
    """
    MODEL_PATH.parent.mkdir(exist_ok=True)

    joblib.dump(model, MODEL_PATH)


def load_model():
    """
    Load trained model.
    """
    return joblib.load(MODEL_PATH)