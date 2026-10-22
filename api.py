from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from psycopg_pool import ConnectionPool
import psycopg
import joblib
from dotenv import load_dotenv
import pandas as pd
import os
import json
import numpy as np
from typing import Literal
from src.preprocess import training_columns

password = os.getenv("DB_PASSWORD") or os.getenv("POSTGRES_PASSWORD")
db_host = os.getenv("DB_HOST","localhost")
db_port = int(os.getenv("DB_PORT", "5432"))
db_name = os.getenv("DB_NAME","Telico_churn")
db_user = os.getenv("DB_USER","postgres")
ssl_mode = os.getenv("DB_SSLMODE", "prefer")

model = joblib.load("Customer-Churn-Prediction_Model")

class InputData(BaseModel):
  gender : Literal['Female','Male']
  SeniorCitizen: Literal[1,0]
  Partner: Literal['Yes', 'No']
  Dependents: Literal['Yes','No']
  tenure: int=Field(ge=0)
  PhoneService: Literal['Yes', 'No']
  MultipleLines: Literal["No", "Yes", "No phone service"]
  InternetService: Literal['Fiber optic', 'DSL','No']
  OnlineSecurity: Literal['No','Yes','No internet service']
  Contract: Literal['Month-to-month', 'Two year','one year']

pool = ConnectionPool(
    f"host={db_host} "
    f"port={db_port} "
    f"dbname={db_name} "
    f"user={db_user} "
    f"password={password} "
    f"sslmode={ssl_mode}"
)

app = FastAPI()
@app.post("/predict")
def predict(Data:InputData):
   try:
    features = [Data.gender,Data.SeniorCitizen,Data.Partner,Data.Dependents,Data.tenure,Data.PhoneService, Data.MultipleLines, Data.InternetService, Data.OnlineSecurity,Data.Contract]

    df = pd.DataFrame([features],columns=[
    "gender", "SeniorCitizen", "Partner", "Dependents",
    "tenure", "PhoneService", "MultipleLines",
    "InternetService", "OnlineSecurity", "Contract"])
    df["gender"] = df["gender"].map({"Female": 1, "Male": 0})
    df["Partner"] = df["Partner"].map({"Yes": 1, "No": 0})
    df["Dependents"] = df["Dependents"].map({"Yes": 1, "No": 0})
    df["PhoneService"] = df["PhoneService"].map({"Yes": 1, "No": 0})

    encoded_mult = pd.get_dummies(df["MultipleLines"], prefix="MultipleLines")
    encoded_int_serv = pd.get_dummies(df["InternetService"], prefix="InternetService")
    encoded_onl_serv = pd.get_dummies(df["OnlineSecurity"], prefix="OnlineSecurity")
    encoded_contract = pd.get_dummies(df["Contract"], prefix="Contract")
    int_features = pd.concat([df[["gender","SeniorCitizen","Partner", "Dependents", "tenure", "PhoneService"]],encoded_mult,encoded_int_serv,encoded_onl_serv,encoded_contract],axis=1)
    int_features = int_features.reindex(columns=training_columns,fill_value=0)
    prediction = model.predict(int_features)[0]
    with pool.connection() as conn:
      with conn.cursor() as cursor:
         cursor.execute("""
         INSERT INTO prediction_history
         (gender,SeniorCitizen,Partner,Dependents,tenure,PhoneService,MultipleLines, InternetService,OnlineSecurity,Contract,prediction)
         VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
         (Data.gender,Data.SeniorCitizen,Data.Partner,Data.Dependents,Data.tenure,Data.PhoneService, Data.MultipleLines, Data.InternetService, Data.OnlineSecurity,Data.Contract,prediction))
      conn.commit()
    return {'prediction': prediction.tolist()}
   except psycopg.OperationalError:
     raise HTTPException(status_code=503, detail='Database currently unavailable')

class PredictionHistory(BaseModel):
  id: int
  gender: str
  seniorcitizen: int
  partner: str
  dependents: str
  tenure: int
  phoneservice: str
  multiplelines: str
  internetservice: str
  onlinesecurity: str
  contract: str
  prediction: int

class PredictionResponse(BaseModel):
  predictions: list[PredictionHistory]
@app.get('/predictions', response_model=PredictionResponse)
def get_predictions():
  try:
   with pool.connection() as conn:
    with conn.cursor() as cursor:
      cursor.execute("SELECT * FROM prediction_history")
      rows = cursor.fetchall()
      columns = [desc.name for desc in cursor.description]
   predictions = [dict(zip(columns, row)) for row in rows]
   return {'predictions': predictions}
  except psycopg.OperationalError:
    raise HTTPException(status_code=503, detail="Database currently unavailable")

@app.get("/health")
def health_check():
  try:
   with pool.connection() as conn:
    with conn.cursor() as cursor:
      cursor.execute("SELECT 1")
   return {'api':'healthy','database':'healthy'}
  except psycopg.OperationalError:
    raise HTTPException(status_code=503, detail='Database currently unavailable')


















