import pandas as pd

FEATURE_COLUMNS = [
    "pregnancies",
    "glucose",
    "blood_pressure",
    "skin_thickness",
    "insulin",
    "bmi",
    "diabetes_pedigree_function",
    "age",
]


def transform_input(payload: dict) -> pd.DataFrame:
    if not isinstance(payload, dict):
        raise ValueError("Input payload must be a dictionary.")

    missing = [col for col in FEATURE_COLUMNS if col not in payload]
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(missing)}")

    df = pd.DataFrame([payload])
    return df[FEATURE_COLUMNS]