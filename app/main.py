from fastapi import FastAPI
from .routes.predict import router as predict_router

app = FastAPI(
    title="Health Risk Prediction API",
    description="""
A production-ready FastAPI web service for predicting diabetes risk based on patient health metrics.

## Features
- Binary classification model (Logistic Regression)
- Real-time predictions with probability scores
- Input validation with Pydantic schemas
- Full OpenAPI/Swagger documentation
- RESTful API design

## Machine Learning Model
- **Algorithm**: Logistic Regression with StandardScaler preprocessing
- **Dataset**: Pima Indians Diabetes Dataset (768 samples, 8 features)
- **Accuracy**: ~73%
- **Input Features**: 8 health metrics (pregnancies, glucose, blood pressure, skin thickness, insulin, BMI, diabetes pedigree function, age)

## Quick Start
1. Train the model: `python ml/train.py`
2. Start the server: `uvicorn app.main:app --reload`
3. View docs: http://localhost:8000/docs
4. Make predictions: POST /api/predict
    """,
    version="0.1.0",
    contact={
        "name": "API Support",
        "url": "https://github.com",
    },
)

app.include_router(predict_router, prefix="/api")


@app.get("/health", tags=["Health"], summary="Health Check", description="Check if the API is running and responding")
def health_check():
    """
    Health check endpoint for monitoring API availability.
    
    Returns:
    - **status**: "ok" if the service is running
    """
    return {"status": "ok"}

@app.get("/")
def home():
    return {"message": "API is running"}