# Health Risk Prediction FastAPI ML

A production-ready FastAPI web service for predicting diabetes risk based on patient health metrics using a machine learning model trained with scikit-learn.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Running Backend & Frontend](#running-backend--frontend)
- [API Documentation](#api-documentation)
- [Frontend UI](#frontend-ui)
- [Testing](#testing)
- [Docker Deployment](#docker-deployment)
- [Project Workflow](#project-workflow)
- [Model Details](#model-details)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project implements a machine learning pipeline that:
1. **Trains** a logistic regression classifier on the Pima Indians Diabetes dataset
2. **Serves** predictions via a FastAPI REST API with full swagger documentation
3. **Validates** input data using Pydantic schemas with data type and range checks
4. **Tests** all endpoints with comprehensive unit tests

The API predicts whether a patient has diabetes (binary classification) based on 8 health metrics, returning both the prediction class and probability score.

## Features

- ✅ **FastAPI REST API** - Modern, async Python web framework with automatic OpenAPI/Swagger documentation
- ✅ **Scikit-learn Pipeline** - Production-grade ML model with preprocessing (StandardScaler) and classification (Logistic Regression)
- ✅ **React Frontend** - Beautiful, responsive UI for entering patient data and viewing predictions
- ✅ **Input Validation** - Pydantic models enforce type safety and boundary constraints on all inputs
- ✅ **Comprehensive Testing** - pytest integration for API and business logic testing
- ✅ **Docker Support** - Containerized deployment with included Dockerfile
- ✅ **Error Handling** - Graceful HTTP error responses with meaningful messages
- ✅ **Model Persistence** - joblib serialization for model saving/loading
- ✅ **Health Checks** - Built-in `/health` endpoint for monitoring
- ✅ **Interactive UI** - Real-time form validation, visual results, medical recommendations

## Project Structure

```
health-risk-prediction-fastapi-ml/
│
├── app/                                    # FastAPI application
│   ├── __init__.py
│   ├── main.py                            # FastAPI app initialization
│   ├── routes/
│   │   └── predict.py                     # Prediction endpoint route
│   ├── schemas/
│   │   └── input_schema.py                # Pydantic models for request/response validation
│   ├── services/
│   │   └── prediction_service.py          # Business logic for predictions
│   ├── model/
│   │   └── model_loader.py                # Model loading and caching
│   └── utils/
│       └── preprocess.py                  # Input preprocessing utilities
│
├── ml/                                     # Machine learning training & evaluation
│   ├── __init__.py
│   ├── train.py                           # Model training script
│   └── evaluate.py                        # Model evaluation and metrics
│
├── frontend/                               # React frontend UI
│   ├── public/
│   │   └── index.html                     # HTML root file
│   ├── src/
│   │   ├── components/
│   │   │   ├── Header.js                  # Application header
│   │   │   ├── PredictionForm.js          # Patient data input form
│   │   │   └── ResultCard.js              # Results display component
│   │   ├── App.js                         # Main React component
│   │   └── index.js                       # React DOM entry point
│   ├── package.json                       # Dependencies and scripts
│   └── README.md                          # Frontend documentation
│
├── data/
│   └── diabetes.csv                       # Training dataset (Pima Indians Diabetes)
│
├── model/
│   └── model.pkl                          # Trained model (generated after running train.py)
│
├── tests/
│   └── test_api.py                        # API endpoint tests using pytest
│
├── requirements.txt                       # Python dependencies
├── Dockerfile                             # Docker container configuration
├── .gitignore                             # Git ignore patterns
├── LICENSE                                # MIT License
├── README.md                              # This file
├── FRONTEND_SETUP.md                      # Frontend setup guide
└── .git/                                  # Git repository
```

## Prerequisites

- **Python 3.10+** (tested on 3.12)
- **pip** or **conda** for package management
- **Docker** (optional, for containerized deployment)

## Installation

### 1. Clone or Download the Repository

```bash
cd health-risk-prediction-fastapi-ml
```

### 2. Create a Virtual Environment

Using venv (recommended):
```bash
python -m venv .venv
```

Activate it:
- **Windows:**
  ```bash
  .\.venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source .venv/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `fastapi>=0.100.0` - Web framework
- `uvicorn[standard]>=0.23.0` - ASGI server
- `scikit-learn>=1.3.0` - ML algorithms and preprocessing
- `pandas>=2.1.0` - Data manipulation
- `joblib>=1.3.0` - Model serialization
- `pytest>=8.0.0` - Testing framework

## Quick Start

### Step 1: Train the Model

```bash
python ml/train.py
```

**Output:**
```
Training complete. Saved model to ...\model\model.pkl
Test accuracy: 0.7722
```

This trains a logistic regression model on the diabetes dataset and saves it as `model/model.pkl`.

### Step 2: Start the API Server

```bash
uvicorn app.main:app --reload
```

**Output:**
```
INFO:     Will watch for changes in these directories: [...]
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

### Step 3: Test the API

In a new terminal:

**Windows (PowerShell):**
```powershell
$body = @{
    pregnancies = 2
    glucose = 120
    blood_pressure = 70
    skin_thickness = 30
    insulin = 88
    bmi = 28.5
    diabetes_pedigree_function = 0.5
    age = 33
} | ConvertTo-Json

$params = @{
    Uri = "http://127.0.0.1:8000/api/predict"
    Method = "POST"
    Headers = @{"Content-Type" = "application/json"}
    Body = $body
}

(Invoke-WebRequest @params).Content | ConvertFrom-Json
```

**macOS/Linux (bash/curl):**
```bash
curl -X POST "http://127.0.0.1:8000/api/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "pregnancies": 2,
    "glucose": 120,
    "blood_pressure": 70,
    "skin_thickness": 30,
    "insulin": 88,
    "bmi": 28.5,
    "diabetes_pedigree_function": 0.5,
    "age": 33
  }'
```

**Expected Response:**
```json
{
  "prediction": 0,
  "probability": 0.3421
}
```

## Running the Application

### Train the Model

```bash
python ml/train.py
```

Trains the logistic regression classifier on the Pima Indians Diabetes dataset and saves the pipeline to `model/model.pkl`.

### Evaluate the Model

```bash
python ml/evaluate.py
```

Generates evaluation metrics including accuracy, ROC AUC, and a detailed classification report.

### Run the FastAPI Server

#### Development Mode (with auto-reload)
```bash
uvicorn app.main:app --reload
```

#### Production Mode
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

The API will be available at `http://localhost:8000`

## Running Backend & Frontend

Once the model is trained, you can run the complete application with both backend and frontend:

### Option 1: Using Two Terminal Windows (Recommended for Development)

**Terminal 1 - Start FastAPI Backend:**
```bash
uvicorn app.main:app --reload
```
Output: `Uvicorn running on http://127.0.0.1:8000`

**Terminal 2 - Start React Frontend:**
```bash
cd frontend
npm install  # Only needed on first run
npm start
```
Output: `Compiled successfully! You can now view health-risk-prediction in the browser.`

The React app opens automatically at `http://localhost:3000`

### Option 2: Using One Terminal with Concurrently (Advanced)

Install `concurrently`:
```bash
npm install --save-dev concurrently
```

Add to `frontend/package.json` scripts:
```json
"start-all": "concurrently \"uvicorn app.main:app --reload\" \"npm --prefix ./frontend start\""
```

Then run both servers:
```bash
npm run start-all
```

### Using the Application

1. **Open the UI** - Navigate to `http://localhost:3000`
2. **Enter Patient Data** - Fill in the 8 health metrics:
   - Pregnancies
   - Glucose
   - Blood Pressure
   - Skin Thickness
   - Insulin
   - BMI
   - Diabetes Pedigree Function
   - Age
3. **Get Prediction** - Click the "Get Prediction" button
4. **View Results** - See risk classification (HIGH RISK / LOW RISK) with:
   - Prediction probability percentage
   - Visual progress bar
   - Tailored medical recommendations
   - Health tips

### Frontend Features

- ✅ **Real-time Form Validation** - All inputs validated with min/max bounds
- ✅ **Interactive Icons** - Visual icons for each health metric
- ✅ **Loading States** - Disabled form during API request
- ✅ **Error Handling** - User-friendly error messages if API fails
- ✅ **Responsive Design** - Works on desktop and mobile devices
- ✅ **Color-Coded Results** - Green for LOW RISK, Red for HIGH RISK
- ✅ **Medical Recommendations** - Personalized health suggestions based on prediction

### Troubleshooting

**Frontend fails to start:**
```bash
# Clear node modules and reinstall
cd frontend
rm -r node_modules package-lock.json
npm install
npm start
```

**CORS errors in browser console:**
- Ensure FastAPI is running on `http://127.0.0.1:8000`
- Check frontend/package.json has `"proxy": "http://127.0.0.1:8000"`

**Prediction fails with 503 error:**
- Ensure you've run `python ml/train.py` to generate `model/model.pkl`
- Check model file exists at `model/model.pkl`

**API returns 422 (Unprocessable Entity):**
- Verify all 8 input fields have valid values
- Check values are within valid ranges (non-negative, realistic)

## API Documentation

### Interactive API Documentation

Swagger UI (auto-generated):
```
http://localhost:8000/docs
```

ReDoc (alternative documentation):
```
http://localhost:8000/redoc
```

### Endpoints

#### Health Check

**Endpoint:** `GET /health`

**Description:** Check if the API is running

**Response:**
```json
{
  "status": "ok"
}
```

---

#### Make Prediction

**Endpoint:** `POST /api/predict`

**Description:** Predict diabetes risk based on patient health metrics

**Request Body (JSON):**
```json
{
  "pregnancies": 2,
  "glucose": 120.0,
  "blood_pressure": 70.0,
  "skin_thickness": 30.0,
  "insulin": 88.0,
  "bmi": 28.5,
  "diabetes_pedigree_function": 0.5,
  "age": 33
}
```

**Request Fields:**
| Field | Type | Description |
|-------|------|-------------|
| `pregnancies` | integer | Number of pregnancies (≥ 0) |
| `glucose` | float | Plasma glucose concentration (≥ 0) |
| `blood_pressure` | float | Diastolic blood pressure in mmHg (≥ 0) |
| `skin_thickness` | float | Triceps skinfold thickness in mm (≥ 0) |
| `insulin` | float | 2-hour serum insulin in mu U/ml (≥ 0) |
| `bmi` | float | Body mass index (≥ 0) |
| `diabetes_pedigree_function` | float | Diabetes pedigree function score (≥ 0) |
| `age` | integer | Age in years (≥ 0) |

**Response (200 OK):**
```json
{
  "prediction": 0,
  "probability": 0.3421
}
```

**Response Fields:**
| Field | Type | Description |
|-------|------|-------------|
| `prediction` | integer | 0 = no diabetes, 1 = diabetes |
| `probability` | float | Predicted probability for positive class (0-1) |

**Error Responses:**

- **422 Unprocessable Entity** - Missing or invalid fields
  ```json
  {
    "detail": "Missing required fields: insulin, age"
  }
  ```

- **503 Service Unavailable** - Model not found (train model first)
  ```json
  {
    "detail": "Trained model not found. Run `python ml/train.py` to generate `model/model.pkl`."
  }
  ```

- **500 Internal Server Error** - Server error
  ```json
  {
    "detail": "Prediction service error."
  }
  ```

### Example Usage

**Python:**
```python
import requests

url = "http://127.0.0.1:8000/api/predict"
payload = {
    "pregnancies": 2,
    "glucose": 120.0,
    "blood_pressure": 70.0,
    "skin_thickness": 30.0,
    "insulin": 88.0,
    "bmi": 28.5,
    "diabetes_pedigree_function": 0.5,
    "age": 33
}

response = requests.post(url, json=payload)
print(response.json())
```

**PowerShell (Windows):**
```powershell
$body = @{
    pregnancies = 2
    glucose = 120.0
    blood_pressure = 70.0
    skin_thickness = 30.0
    insulin = 88.0
    bmi = 28.5
    diabetes_pedigree_function = 0.5
    age = 33
} | ConvertTo-Json

$params = @{
    Uri = "http://127.0.0.1:8000/api/predict"
    Method = "POST"
    Headers = @{"Content-Type" = "application/json"}
    Body = $body
}

(Invoke-WebRequest @params).Content | ConvertFrom-Json
```

**cURL (macOS/Linux):**
```bash
curl -X POST "http://127.0.0.1:8000/api/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "pregnancies": 2,
    "glucose": 120.0,
    "blood_pressure": 70.0,
    "skin_thickness": 30.0,
    "insulin": 88.0,
    "bmi": 28.5,
    "diabetes_pedigree_function": 0.5,
    "age": 33
  }'
```

**JavaScript (Node.js):**
```javascript
const payload = {
    pregnancies: 2,
    glucose: 120.0,
    blood_pressure: 70.0,
    skin_thickness: 30.0,
    insulin: 88.0,
    bmi: 28.5,
    diabetes_pedigree_function: 0.5,
    age: 33
};

fetch('http://127.0.0.1:8000/api/predict', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
})
.then(res => res.json())
.then(data => console.log(data));
```

## Testing

### Run All Tests

```bash
pytest
```

### Run Tests with Verbose Output

```bash
pytest -v
```

### Run Specific Test File

```bash
pytest tests/test_api.py -v
```

### Run Tests with Coverage Report

```bash
pip install pytest-cov
pytest --cov=app
```

### Test Coverage

The test suite includes:
- **Health check endpoint** - Verifies `/health` returns `{"status": "ok"}`
- **Prediction endpoint** - Tests `/api/predict` with valid data
- **Error handling** - Checks HTTP error codes for missing model or invalid data

## Docker Deployment

### Build Docker Image

```bash
docker build -t health-risk-api:latest .
```

### Run Docker Container

```bash
docker run -p 8000:8000 health-risk-api:latest
```

The API will be accessible at `http://localhost:8000`

### Run with Volume Mount (for data persistence)

```bash
docker run -p 8000:8000 \
  -v $(pwd)/model:/app/model \
  -v $(pwd)/data:/app/data \
  health-risk-api:latest
```

### Docker Compose (Optional)

A full-stack compose setup starts both frontend and backend together:
- `api` runs the FastAPI backend
- `frontend` builds and serves the React app via nginx
- `/api` requests are proxied from the frontend to the backend

Create a `docker-compose.yml`:
```yaml
version: '3.8'
services:
  api:
    build:
      context: .
    ports:
      - "8000:8000"
    volumes:
      - ./model:/app/model
      - ./data:/app/data

  frontend:
    build:
      context: frontend
      dockerfile: Dockerfile
    ports:
      - "3000:80"
    depends_on:
      - api
```

Run with:
```bash
docker-compose up --build
```

Then browse:
- frontend: `http://localhost:3000`
- backend docs: `http://localhost:8000/docs`

## Project Workflow

### 1. Data Preparation
- Dataset: Pima Indians Diabetes (`data/diabetes.csv`)
- 768 samples, 8 features, binary target (outcome)
- Features are standardized during model training

### 2. Model Training
```bash
python ml/train.py
```

**Pipeline:**
1. Load data from `data/diabetes.csv`
2. Split into training (75%) and testing (25%)
3. StandardScaler preprocessing
4. Logistic Regression classifier (max_iter=1000)
5. Save model to `model/model.pkl`

### 3. Model Evaluation
```bash
python ml/evaluate.py
```

Metrics reported:
- **Accuracy** - Percentage of correct predictions
- **ROC AUC** - Area under the ROC curve (0-1)
- **Classification Report** - Precision, recall, F1-score per class

### 4. Serve Predictions
```bash
uvicorn app.main:app --reload
```

The API loads the trained model and makes predictions on new data.

## Model Details

### Algorithm: Logistic Regression
- **Type:** Binary classification
- **Framework:** scikit-learn
- **Hyperparameters:**
  - `max_iter=1000` - Maximum iterations for solver
  - `random_state=42` - Reproducibility

### Preprocessing Pipeline
1. **StandardScaler** - Normalizes features to mean=0, std=1
   - Improves convergence during training
   - Essential for distance-based algorithms

### Model Persistence
- **Format:** Pickle (.pkl)
- **Tool:** joblib
- **Location:** `model/model.pkl`

## Configuration

### Model Path
Edit `app/model/model_loader.py` to change the model location:
```python
MODEL_PATH = Path(__file__).resolve().parents[1] / "model" / "model.pkl"
```

### API Port
To change the port when running the server:
```bash
uvicorn app.main:app --port 5000
```

### Workers (Production)
```bash
uvicorn app.main:app --workers 4  # Use 4 worker processes
```

### Log Level
```bash
uvicorn app.main:app --log-level info
```

## Troubleshooting

### Issue: "Model not found" (503 error)

**Solution:** Train the model first
```bash
python ml/train.py
```

### Issue: "ModuleNotFoundError: No module named 'fastapi'"

**Solution:** Install dependencies
```bash
pip install -r requirements.txt
```

### Issue: "Port 8000 already in use"

**Solution:** Use a different port
```bash
uvicorn app.main:app --port 8001
```

### Issue: Invalid values in CSV file

**Solution:** Ensure `data/diabetes.csv` has:
- Column header: `pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age, outcome`
- All numeric values
- No null values in training data

### Issue: Docker build fails

**Solution:** Ensure Docker is running and check logs
```bash
docker build -t health-risk-api . --no-cache
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Add tests for new functionality
5. Run tests to ensure all pass (`pytest`)
6. Commit with clear messages (`git commit -am 'Add feature'`)
7. Push to the branch (`git push origin feature/improvement`)
8. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Dataset Attribution

The Pima Indians Diabetes Dataset is originally from the National Institute of Diabetes and Digestive and Kidney Diseases. It is publicly available on:
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Pima+Indians+Diabetes)
- [Kaggle Datasets](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)

**Citation:**
Smith, J.W., Everhart, J.E., Dickson, W.C., Knowler, W.C., & Johannes, R.S. (1988). Using the ADAP learning algorithm to forecast the onset of diabetes mellitus.