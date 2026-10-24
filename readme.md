# Telico-Customer-Churn-prediction_model

* A subscription business wants to identify customers who are likely to stop using its service so it can prioritize retention efforts.
* This model identifies the customers who are likely stop using its service based on features.

## 1. Overview

Explain:
- Application predicts who will likely to stop using the service.
- when user sends prediction request model recieves the input and make predictions based on input.

## 2. Problem Statement

Describe the problem, the prediction objective, the target variable, and the expected inputs.

**Problem:** Identify customers who are likely to stop using the service.
**predicts:** Model predicts the customers who are likely to stop using the service by learning patterns in stored datasets.
**target variable:** Churn
**expected inputs:** ['gender', 'SeniorCitizen', 'Partner', 'Dependents',
       'tenure', 'PhoneService', 'MultipleLines', 'InternetService',
       'OnlineSecurity','Contract']

## 3. Dataset

- **Source:** [IBM Telco Customer Churn dataset/kaggle]
- **Samples:** [7043]
- **Features:** [23]
- **Target:** [Churn]

### Data Preprocessing

- Missing-value handling
- converted text values into numerical
- Categorical encoding
- Feature scaling 
- Usefull feature selection
- Train-test split

## 4. Project Workflow

Describe the complete pipeline:

1. Receive an API request.
2. Validate input data.
3. Apply the required preprocessing.
4. Generate a prediction using the trained model.
5. Return the prediction as JSON.
6. Store the prediction and relevant input data in PostgreSQL.


## 5. Model Development

- **Algorithm:** [LogisticRegression]
- **Training approach:** [Sckit-learn]
- **Validation strategy:** [Accuracy, precision score, recall score, Confusion Matrix, roc_auc_curve]
- **Model persistence:** [joblib.dump() save the trained model and joblib.load() load the model to use.]

## 6. Model Evaluation

| Metric | Result |
|---|---:|
Accuracy: 0.8076650106458482
Precision Score: 0.659375
Recall Score: 0.5656836461126006
f1 Score: 0.6089466089466089
Confusion Matrix: [[927 109]
                  [162 211]]
roc_auc_score: 0.8559550550167171

## 7. Tech Stack

- Python
- pandas, NumPy, scikit-learn, pytest, joblib, uvicorn etc
- FastAPI and Pydantic
- PostgreSQL
- Docker and Docker Compose
- Render or [hosting platform]

## 8. Project Structure

Explain the purpose of the important directories and files.

```text
project/
├── src/
├── tests/
├── api.py
├── Dockerfile
├── compose.yaml
├── pyproject.toml
├── requirements.txt
├── .env.example
└── README.md
```



## 9. Local Installation and Setup

## Prerequisites

The following tools are required:

- **Git** — to clone the repository.
- **Python 3.11** — required for running the application locally and installing its dependencies.
- **Docker Desktop** — required for containerized execution.
- **Docker Compose** — used to run the API and database services together.

Python dependencies are specified in `requirements.txt`.

**Downloads:**
- [Python](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- [Docker Desktop](https://docs.docker.com/get-started/get-docker/)


### Installation

```bash
git clone https://github.com/f4789343-pixel/Telico-Customer-churn-prediction_model.git
cd Customer-Churn-Prediction_Model
```

Explain how to create a virtual environment and install dependencies.
1. go to powersell
2. run the git clone
3. create folder for it
4. create virtual environment.
5. 

### Environment Variables

Document the required variable names and their purposes. Provide example placeholders, never real credentials.

### Run Locally

Provide the commands to start the API and any required database services.

## 10. Docker Deployment

Explain how to build and start the application:

```bash
docker compose up --build
```

Document the exposed ports, services, database configuration, persistent storage, and shutdown procedure.

## 11. API Documentation

### `GET /health`

Describe the health-check response.

### `POST /predict`

Explain the required request fields.

**Example request:**

```json
{
  "feature_1": 1.0,
  "feature_2": 2.0
}
```

**Example response:**

```json
{
  "prediction": 0.0
}
```

Replace these examples with the application's actual schema and response.

Explain input validation and relevant error responses.

## 12. Live Deployment

- **API URL:** [telico-customer-churn-prediction-model.onrender.com]
- **Interactive documentation:** [telico-customer-churn-prediction-model.onrender.com]/docs
- **Hosting platform:** [render]
- **Database:** [neon]

Explain any deployment-specific configuration without exposing secrets.

## 13. Testing

Document how to run the tests and verify:
- Input validation
- Prediction responses
- Database connectivity
- Prediction-history persistence
- Container startup and service connectivity

## 14. Limitations

Document known model limitations, dataset limitations, performance concerns, and deployment constraints.

## 15. Future Improvements

List realistic improvements, such as stronger validation, monitoring, model retraining, automated tests, or improved prediction quality.

## 16. License

Specify the project's license, if applicable.