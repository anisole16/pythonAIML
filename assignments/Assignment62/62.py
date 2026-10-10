# Employee Attrition Prediction

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler , OneHotEncoder 
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

from sklearn.metrics import (
    confusion_matrix,accuracy_score,
    ConfusionMatrixDisplay,
    classification_report
)

Border = "-"*40
###############################################################
# Step 1: Load the Dataset
###############################################################
print(Border)
print("Step 1: Load the Dataset")
print(Border)

df = pd.read_csv("Employee_Attrition.csv")
print("Dataset Loaded Successfully...")

###############################################################
# Step 2: Display the Dataset
###############################################################
print(Border)
print(" Step 2: Display the Dataset")
print(Border)

print("Dataset shape: ")
print(df.shape)

print("\nColumn names: ")
print(df.columns)

print("First Five Shape: ")
print(df.head())

###############################################################
# Step 3: Check for the missing values
###############################################################
print(Border)
print("Step 3: Check for the missing values")
print(Border)

print("Missing values in each column: ")
print(df.isnull().sum())

print("Total missing values: ")
print(df.isnull().sum().sum())

###############################################################
# Step 4: Identify numrical and categorical features
###############################################################
print(Border)
print("Step 4: Identify numrical and categorical features")
print(Border)

num_features = df.select_dtypes(include=["int64" , "float64"]).columns.tolist()
print("Numeriacl features: ")
print(num_features)

cat_features = df.select_dtypes(include = ["object" , "category" , "bool"]).columns.tolist()
print("Categorical Features: ")
print(cat_features)

###############################################################
# Step 5: Convert Categorical into numeriacl features
###############################################################
print(Border)
print(" Step 5: Convert Categorical into numeriacl features")
print(Border)

# Overtime is categorical
print("Categorical value before encoding: ")
print(df["OverTime"].value_counts)

overtime_encoded = pd.get_dummies(
    df["OverTime"], prefix = "OverTime" , dtype=int
)
print("\nOvertime after Encoding: ")
print(overtime_encoded.head())

###############################################################
# Step 6: Convert Target variable into 0 and 1(Binary Encoding)
###############################################################
print(Border)
print(" Step 6: Convert Target variable into 0 and 1")
print(Border)

df["Attrition"] = df["Attrition"].map({"Yes": 1 , "No":0})
print(df["Attrition"].head())

###############################################################
# Step 7 : Seperate The Dependent and Independent Variables
###############################################################
print(Border)
print(" Step 7 : Seperate The Dependent and Independent Variables")
print(Border)
df = df.drop(
columns=[
"EmployeeNumber",
"EmployeeCount",
"Over18",
"StandardHours"
],
errors="ignore"
)

X = df.drop(columns=["Attrition"])
Y = df["Attrition"]

print("Independent Variables:", X.shape)
print("Dependent Variable:", Y.shape)

###############################################################
# Step 8: Divide the Dataset for training and Testing
#################################################################
print(Border)
print(" Step 7 : Seperate The Dependent and Independent Variables")
print(Border)

X_train , X_test , Y_train , Y_test = train_test_split(X , Y ,
                                                        test_size=0.2 , 
                                                        random_state=42,stratify=Y)
print("Training Dataset:", X_train.shape[0])
print("Testing Dataset:", X_test.shape[0])

###############################################################
# Step 9: Feature Scaling
#################################################################
print(Border)
print(" Step 9: Feature Scaling")
print(Border)
numerical_cols = X.select_dtypes(
    include=["number"]
).columns.tolist()

categorical_cols = X.select_dtypes(
    include=["object", "category", "bool"]
).columns.tolist()

numerical_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("num", numerical_transformer, numerical_cols),
    ("cat", categorical_transformer, categorical_cols)
])

###############################################################
# Step 10: Build the MLP Model with Two Hidden Layers
###############################################################

from sklearn.neural_network import MLPClassifier

print(Border)
print("Step 10: Build the MLP Model")
print(Border)

mlp = MLPClassifier(
    hidden_layer_sizes=(64, 32),
    activation="relu",
    solver="adam",
    learning_rate_init=0.001,
    max_iter=300,
    early_stopping=True,
    validation_fraction=0.15,
    random_state=42
)

model = Pipeline([
    ("preprocessor", preprocessor),
    ("mlp", mlp)
])

print("MLP Model Created Successfully")


###############################################################
# Step 11: Train the Model
###############################################################

print(Border)
print("Step 11: Train the Model")
print(Border)

model.fit(X_train, Y_train)

print("Model Training Completed Successfully")


###############################################################
# Step 12: Display Training Iterations
###############################################################

print(Border)
print("Step 12: Display Training Iterations")
print(Border)

iterations = model.named_steps["mlp"].n_iter_

print("Number of Training Iterations:", iterations)


###############################################################
# Step 13: Calculate Training Accuracy
###############################################################

print(Border)
print("Step 13: Calculate Training Accuracy")
print(Border)

Y_train_pred = model.predict(X_train)

train_accuracy = accuracy_score(
    Y_train,
    Y_train_pred
)

print(f"Training Accuracy: {train_accuracy * 100:.2f}%")


###############################################################
# Step 14: Calculate Testing Accuracy
###############################################################

print(Border)
print("Step 14: Calculate Testing Accuracy")
print(Border)

Y_test_pred = model.predict(X_test)

test_accuracy = accuracy_score(
    Y_test,
    Y_test_pred
)

print(f"Testing Accuracy: {test_accuracy * 100:.2f}%")


###############################################################
# Step 15: Confusion Matrix and Classification Report
###############################################################


print(Border)
print("Step 15: Confusion Matrix")
print(Border)

cm = confusion_matrix(
    Y_test,
    Y_test_pred,
    labels=[0, 1]
)

print(cm)

print("\nClassification Report:")

print(classification_report(
    Y_test,
    Y_test_pred,
    labels=[0, 1],
    target_names=["No Attrition", "Attrition"],
    zero_division=0
))

ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["No Attrition", "Attrition"]
).plot()

plt.title("Employee Attrition Confusion Matrix")
plt.tight_layout()
plt.show()


###############################################################
# Step 16: Plot the Loss Curve
###############################################################

print(Border)
print("Step 16: Plot the Loss Curve")
print(Border)

loss_values = model.named_steps["mlp"].loss_curve_

plt.figure(figsize=(8, 5))

plt.plot(
    range(1, len(loss_values) + 1),
    loss_values,
    label="Training Loss"
)

plt.xlabel("Iteration")
plt.ylabel("Loss")
plt.title("MLP Training Loss Curve")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


###############################################################
# Step 17: Create PredictAttrition() Function
###############################################################

print(Border)
print("Step 17: Create PredictAttrition Function")
print(Border)

def PredictAttrition(employee_data):

    if isinstance(employee_data, dict):
        employee_data = pd.DataFrame([employee_data])

    elif not isinstance(employee_data, pd.DataFrame):
        raise TypeError(
            "Input must be a dictionary or DataFrame"
        )

    employee_data = employee_data.drop(
        columns=["Attrition"],
        errors="ignore"
    )

    employee_data = employee_data.reindex(
        columns=X.columns
    )

    predictions = model.predict(employee_data)

    probabilities = model.predict_proba(
        employee_data
    )[:, 1]

    results = pd.DataFrame({
        "Predicted_Attrition": [
            "Yes" if value == 1 else "No"
            for value in predictions
        ],
        "Attrition_Probability": probabilities
    })

    return results

print("PredictAttrition Function Created Successfully")


###############################################################
# Step 18: Test Five Employee Records
###############################################################

print(Border)
print("Step 18: Test Five Employee Records")
print(Border)

five_employees = X_test.sample(
    n=5,
    random_state=10
)

predictions = PredictAttrition(five_employees)

actual_values = Y_test.loc[
    five_employees.index
].map({
    0: "No",
    1: "Yes"
}).to_numpy()

comparison = predictions.copy()
comparison["Actual_Attrition"] = actual_values

print(comparison.to_string())


###############################################################
# Step 19: Check Overfitting and Underfitting
###############################################################

print(Border)
print("Step 19: Check Overfitting and Underfitting")
print(Border)

accuracy_gap = train_accuracy - test_accuracy

print(f"Training Accuracy: {train_accuracy * 100:.2f}%")
print(f"Testing Accuracy: {test_accuracy * 100:.2f}%")

print(
    f"Accuracy Gap: {accuracy_gap * 100:.2f} percentage points"
)

if train_accuracy < 0.70 and test_accuracy < 0.70:
    print("Possible Underfitting")

elif accuracy_gap > 0.10:
    print("Possible Overfitting")

else:
    print("No strong overfitting signal from accuracy alone")

print("Check the classification report and loss curve too.")





