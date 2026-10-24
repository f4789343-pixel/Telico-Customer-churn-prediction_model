# Telico-Customer-Churn-prediction_model

* A subscription business wants to identify customers who are likely to stop using its service so it can prioritize retention efforts.
* This model identifies the customers who are likely stop using its service based on features.

## 1. Overview

Explain:
- Application predicts who will likely to stop using the service.
- when user sends prediction request model recieves the input and make predictions based on input.

## 2. Problem Statement

Describe the problem, the prediction objective, the target variable, and the expected inputs.

- **Problem:** Identify customers who are likely to stop using the service.
- **predicts:** Model predicts the customers who are likely to stop using the service by learning patterns in stored datasets.
- **target variable:** Churn
- **expected inputs:** ['gender', 'SeniorCitizen', 'Partner', 'Dependents',
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
5. install requirements.txt
6. run pytest

### Environment Variables

- **Database_password**
- **DB_HOST**
- **DB_PORT**

### Run Locally

Provide the commands to start the API and any required database services.
1. create virtual environment. `bash python -m venv venv` 
2. install requirements.txt. `python -m pip install -r requirements.txt`
3. install uvicorn. `pip install uvicorn`
4. run uvicorn. `python -m uvicorn api:app --reload`
5. open browser and search URL. `http://localhost:8000/docs`

## 10. Docker Deployment

The application uses Docker Compose to run the FastAPI service and PostgreSQL database in separate containers.

### Services

- **API:** Runs the FastAPI application and exposes the prediction endpoints.
- **PostgreSQL:** Stores prediction history and other application data.

### Port Configuration

| Service | Container Port | Host Port |
|---|---:|---:|
| FastAPI | 8000 | 8000 |
| PostgreSQL | 5432 | 5432 |

The API is accessible locally at `http://localhost:8000`. Interactive API documentation is available at `http://localhost:8000/docs`.

The PostgreSQL host port is only needed for direct connections from the host machine; the API connects to the database using the database service name and container port.


### Database Configuration

Database settings are provided through environment variables. Configure the required values in your local environment file or deployment environment.

Do not commit passwords, database credentials, or other secrets to version control.

### Persistent Storage

Docker Compose uses a named volume to persist PostgreSQL data beyond the lifetime of an individual container.

Stopping or recreating containers does not normally delete the named volume. Removing the volume, however, can permanently delete the stored database data.

### Start the Application

Build the image and start the services:

```bash
docker compose up --build
```

Run the services in the background:

```bash
docker compose up --build -d
```

### View Logs

```bash
docker compose logs -f
```

To view logs for only the API service:

```bash
docker compose logs -f api
```

Replace `api` with the actual service name in your Compose file if it differs.

### Stop the Application

Stop and remove the running containers and Compose-created network:

```bash
docker compose down
```

The named database volume is retained by default, so database records can persist when the services are started again.

**Warning:** Use `docker compose down -v` only when you intentionally want to remove the associated named volumes and their stored database data.

## 11. API Documentation

### `GET /health`

* health check returns healthy, if API and Database running successfully.
* It returns unhealthy and detail, if it's not working.

### `POST /predict`

Explain the required request fields.

**Example request:**

```json
{
  "gender": "Female",
  "SeniorCitizen": 1,
  "Partner": "Yes",
  "Dependents": "Yes",
  "tenure": 0,
  "PhoneService": "Yes",
  "MultipleLines": "No",
  "InternetService": "Fiber optic",
  "OnlineSecurity": "No",
  "Contract": "Month-to-month"
}
```

**Example response:**

```json
{
  "prediction": 0
}
```

## 12. Live Deployment

- **API URL:** [telico-customer-churn-prediction-model.onrender.com]
- **Interactive documentation:** [telico-customer-churn-prediction-model.onrender.com]/docs
- **Hosting platform:** [render]
- **Database:** [neon]


## 13. Testing

Document how to run the tests and verify:
- Input validation
- Prediction responses
- Database connectivity
- Prediction-history persistence
- Container startup and service connectivity

## 14. Limitations

Document known model limitations, dataset limitations, performance concerns, and deployment constraints.
* Model limitations: Accuracy is not improving even with different classification algorithms.
* The features are not explaining variations more accurately that's changing algorithms are not improving accuarcy.
* dataset limitations: There are many string features that requires more preprocessing and many features not explaining variations in dataset.
* deployment limitations: Getting outputs from docs may take longer cause of free host(render and neon).
* inputs are case sensitive, inserting all lowercase and uppercases gives errors.

## 15. Future Improvements

* Choosing features that explain more variance in datasets, may improve performance accuracy.
* Improve the input valdations more conveniently.
* handles the errors more clearly.
* Chooses the stronger hosting performance and fixes the service future service errors.
* Try to improve accuracy by using the dimensonality reduction, it will may explain more variance.
* improve the feature engineering.
