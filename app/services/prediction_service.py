from ..model.model_loader import load_model
from ..utils.preprocess import transform_input

_model = None


def get_model():
    global _model
    if _model is None:
        _model = load_model()
    return _model


def predict(features: dict) -> dict:
    model = get_model()
    transformed = transform_input(features)
    probability = model.predict_proba(transformed)[:, 1][0]
    prediction = int(model.predict(transformed)[0])

    return {
        "prediction": prediction,
        "probability": float(round(probability, 4)),
    }