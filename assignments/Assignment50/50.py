# breast Cancer Case Study


from sklearn.datasets import load_breast_cancer

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

import matplotlib.pyplot as plt
import pandas as pd

from sklearn.metrics import (classification_report ,
accuracy_score , recall_score,
confusion_matrix , precision_score , f1_score)


Border = "-"*30
# Step 1: Load the Dataset

print(Border)
print("# Step 1: Load the Dataset")
print(Border)

data = load_breast_cancer()

X = pd.DataFrame(data.data,columns=data.feature_names)
Y = pd.Series(data.target)

print("DataSet Loaded Successfully....")
print("Number of Records: ",X.shape[0])
print("Number of Features: ",X.shape[1])


print(Border)
print("Step 2: Analyze the Dataset")
print(Border)

print("First Five Records:  ",X.head())
print("Information of Dataset: ",X.info())

print("Missing Values:")
print(X.isnull().sum())



print(Border)
print("# Step 3:  EDA")
print(Border)

print("Summary Statistics: ")
print(X.describe())


print(Border)
print(" Step 4:  Feature Co-relation")
print(Border)

plt.figure(figsize=(12,10))
plt.imshow(X.corr() , aspect="auto")
plt.colorbar()
plt.title("Feature Corelation Matrix")
plt.xlabel("Features")
plt.ylabel("Features")
plt.show()


print(Border)
print(" Step 5:  Split the Dataset")
print(Border)

X_train , X_test , Y_train , Y_test = train_test_split(X ,Y, test_size=0.2,
                                                        random_state=42,stratify=Y)

print("Training Samples: ")
print(X_train.shape[0])
print("Testing Samples: ")
print(X_test.shape[0])


print(Border)
print(" Step 6:  Scale the dataset")
print(Border)

scalar = StandardScaler()

X_train_scaled = scalar.fit_transform(X_train)
X_test_scaled = scalar.transform(X_test)

print("Model Scalled Successfullyy....")

print(Border)
print(" Step 7:  Build the model")
print(Border)

model = LogisticRegression(max_iter=10000)
model.fit(X_train_scaled , Y_train)

print("Model Build Successfully...")

print(Border)
print(" Step 8:  Test the model")
print(Border)

Y_pred = model.predict(X_test_scaled)

print(Border)
print(" Step 9:  Evaluate the model")
print(Border)

accuracy = accuracy_score(Y_test,Y_pred)
print("Accuracy: ",accuracy)

precision = precision_score(Y_test , Y_pred)
print("Precisison: ",precision)

recall = recall_score(Y_test, Y_pred)
print("Recall: ",recall)

f1 = f1_score(Y_test, Y_pred)
print("F1 Score: ",f1)

cm = confusion_matrix(Y_test , Y_pred)
print("Confussion Matrix: ")
print(cm)



print(Border)
print(" Step 10:  Classification Report")
print(Border)

print("\nClassification Report: ")
print(classification_report(Y_test,Y_pred,target_names=data.target_names))

























print(Border)