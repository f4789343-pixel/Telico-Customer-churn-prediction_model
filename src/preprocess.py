import pandas as pd

df = pd.read_csv("data/Customer-Churn.csv")
print(df.shape)
print(df.info())
print(df["customerID"].head())
print(df.columns)
print(df["gender"])
df["gender"] = df["gender"].map({"Female": 1, "Male": 0})
print(df.isnull().sum())
print(df["SeniorCitizen"].value_counts())
print(df["Partner"].value_counts())
df["Partner"] = df["Partner"].map({"Yes": 1, "No": 0})
df["Dependents"] = df["Dependents"].map({"Yes": 1, "No": 0})
print(df["PhoneService"].value_counts())
df["PhoneService"] = df["PhoneService"].map({"Yes": 1, "No": 0})
print(df["MultipleLines"].value_counts())
print(df["Partner"].value_counts())
print(df.columns.value_counts())
print(df["Dependents"].value_counts())


