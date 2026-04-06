from pathlib import Path
import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "diabetes.csv"
MODEL_DIR = ROOT / "model"
MODEL_FILE = MODEL_DIR / "model.pkl"


def load_dataset() -> pd.DataFrame:
    return pd.read_csv(DATA_PATH)


def build_pipeline() -> Pipeline:
    return Pipeline([
        ("scaler", StandardScaler()),
        ("classifier", LogisticRegression(max_iter=1000, random_state=42)),
    ])


def train_model():
    df = load_dataset()
    X = df.drop(columns=["outcome"])
    y = df["outcome"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    pipeline = build_pipeline()
    pipeline.fit(X_train, y_train)

    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipeline, MODEL_FILE)

    test_score = pipeline.score(X_test, y_test)
    print(f"Training complete. Saved model to {MODEL_FILE}")
    print(f"Test accuracy: {test_score:.4f}")


if __name__ == "__main__":
    train_model()