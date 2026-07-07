from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report,
)

from app.ml.train import train


def evaluate():

    model, X_test, y_test = train()

    predictions = model.predict(X_test)

    probabilities = model.predict_proba(X_test)[:, 1]

    print("\n========== MODEL EVALUATION ==========\n")

    print(f"Accuracy  : {accuracy_score(y_test, predictions):.4f}")
    print(f"Precision : {precision_score(y_test, predictions):.4f}")
    print(f"Recall    : {recall_score(y_test, predictions):.4f}")
    print(f"F1 Score  : {f1_score(y_test, predictions):.4f}")
    print(f"ROC AUC   : {roc_auc_score(y_test, probabilities):.4f}")

    print("\nConfusion Matrix\n")
    print(confusion_matrix(y_test, predictions))

    print("\nClassification Report\n")
    print(classification_report(y_test, predictions))


if __name__ == "__main__":
    evaluate()