import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
df = pd.read_csv("data/Customer-Churn.csv")
print(df.shape)
print(df.info())
print(df["customerID"].head())
print(df.columns)
print(df.isnull().sum())
print(df["Partner"].value_counts())
df["gender"] = df["gender"].map({"Female": 1, "Male": 0})
df["Partner"] = df["Partner"].map({"Yes": 1, "No": 0})
df["Dependents"] = df["Dependents"].map({"Yes": 1, "No": 0})
df["PhoneService"] = df["PhoneService"].map({"Yes": 1, "No": 0})
df['Churn'] = df["Churn"].map({"Yes": 1, "No": 0})
encoded_mult = pd.get_dummies(df['MultipleLines'], dtype=int)
encoded_int_serv = pd.get_dummies(df["InternetService"], dtype=int)
encoded_onl_serv = pd.get_dummies(df["OnlineSecurity"], dtype=int)
encoded_contract = pd.get_dummies(df["Contract"], dtype=int)

features = ["gender","SeniorCitizen","Partner", "Dependents", "tenure", "PhoneService"]
X = df[features]
y = df["Churn"]
X = pd.concat([X,encoded_mult,encoded_int_serv,encoded_onl_serv,encoded_contract], axis=1)

x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)
print(x_train.shape)
print(x_test.shape)
print(y.value_counts())




