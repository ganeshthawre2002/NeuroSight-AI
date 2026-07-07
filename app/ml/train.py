from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

from app.ml.preprocess import build_preprocessor
from app.ml.utils import load_dataset, save_model

def train():

    df = load_dataset()

    # Remove missing rows
    df = df.dropna()

    # Features
    X = df.drop(
        columns=[
            "customerID",
            "Churn"
        ]
    )

    # Target
    y = df["Churn"].map(
        {
            "No": 0,
            "Yes": 1
        }
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    preprocessor = build_preprocessor(X_train)

    model = Pipeline(
        steps=[
            (
                "preprocessor",
                preprocessor
            ),
            (
                "classifier",
                LogisticRegression(
                    max_iter=1000
                )
            )
        ]
    )

    model.fit(
        X_train,
        y_train
    )

    save_model(model)

    print("Model trained successfully.")

    return (
        model,
        X_test,
        y_test
    )


if __name__ == "__main__":
    train()