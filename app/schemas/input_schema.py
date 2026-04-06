from pydantic import BaseModel, Field


class PredictionInput(BaseModel):
    """Patient health metrics for diabetes risk prediction."""
    
    pregnancies: int = Field(..., ge=0, description="Number of pregnancies (count)", example=2)
    glucose: float = Field(..., ge=0, description="Plasma glucose concentration (mg/dL)", example=120.0)
    blood_pressure: float = Field(..., ge=0, description="Diastolic blood pressure (mmHg)", example=70.0)
    skin_thickness: float = Field(..., ge=0, description="Triceps skinfold thickness (mm)", example=30.0)
    insulin: float = Field(..., ge=0, description="2-Hour serum insulin (mu U/ml)", example=88.0)
    bmi: float = Field(..., ge=0, description="Body mass index (kg/m²)", example=28.5)
    diabetes_pedigree_function: float = Field(..., ge=0, description="Diabetes pedigree function score (0-1)", example=0.5)
    age: int = Field(..., ge=0, description="Age in years", example=33)
    
    class Config:
        schema_extra = {
            "example": {
                "pregnancies": 2,
                "glucose": 120.0,
                "blood_pressure": 70.0,
                "skin_thickness": 30.0,
                "insulin": 88.0,
                "bmi": 28.5,
                "diabetes_pedigree_function": 0.5,
                "age": 33
            }
        }


class PredictionOutput(BaseModel):
    """Prediction result with risk classification and probability."""
    
    prediction: int = Field(..., description="Predicted risk label (0 = no diabetes, 1 = diabetes)", example=0)
    probability: float = Field(..., description="Predicted probability for positive class (0.0-1.0)", example=0.0493)
    
    class Config:
        schema_extra = {
            "example": {
                "prediction": 0,
                "probability": 0.0493
            }
        }