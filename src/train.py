from preprocess import x_train, x_test, y_train, y_test
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix


model = LogisticRegression(max_iter=10000, random_state=42)
model.fit(x_train,y_train)
prediction = model.predict(x_test)

accuracy = accuracy_score(y_test, prediction)
precision = precision_score(y_test, prediction)
recall = recall_score(y_test, prediction)
f1 = f1_score(y_test, prediction)
confusion_mat = confusion_matrix(y_test, prediction)
print("Accuracy:",accuracy)
print("Precision Score:", precision)
print("Recall Score:", recall)
print("f1 Score:", f1)
print("Confusion Matrix:", confusion_mat)