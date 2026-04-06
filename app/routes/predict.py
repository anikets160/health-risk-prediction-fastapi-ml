from fastapi import APIRouter, HTTPException
from ..schemas.input_schema import PredictionInput, PredictionOutput
from ..services.prediction_service import predict

router = APIRouter()


@router.post(
    "/predict",
    response_model=PredictionOutput,
    summary="Diabetes Risk Prediction",
    description="Predict diabetes risk based on patient health metrics using a trained logistic regression model.",
    tags=["Predictions"]
)
def predict_route(payload: PredictionInput):
    """
    Predict diabetes risk for a patient.
    
    This endpoint accepts patient health metrics and returns:
    - **prediction**: Binary classification (0=no diabetes, 1=diabetes)
    - **probability**: Probability score (0-1) for the positive class
    
    The model was trained on the Pima Indians Diabetes Dataset with 73% accuracy.
    """
    try:
        result = predict(payload.dict())
        return result
    except FileNotFoundError as exc:
        raise HTTPException(status_code=503, detail=str(exc))
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))
    except Exception as exc:
        raise HTTPException(status_code=500, detail="Prediction service error.")