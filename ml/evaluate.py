from pathlib import Path
import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "diabetes.csv"
MODEL_PATH = ROOT / "model" / "model.pkl"


def load_data():
    return pd.read_csv(DATA_PATH)


def evaluate_model():
    data = load_data()
    X = data.drop(columns=["outcome"])
    y = data["outcome"]

    model = joblib.load(MODEL_PATH)
    y_pred = model.predict(X)
    y_prob = model.predict_proba(X)[:, 1]

    print("Evaluation results")
    print(f"Accuracy: {accuracy_score(y, y_pred):.4f}")
    print(f"ROC AUC: {roc_auc_score(y, y_prob):.4f}")
    print("Classification report:\n")
    print(classification_report(y, y_pred, digits=4))


if __name__ == "__main__":
    evaluate_model()