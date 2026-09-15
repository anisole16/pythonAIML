# Fraudulent Transaction Detection

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    BaggingClassifier,
    RandomForestClassifier,
    AdaBoostClassifier
)

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)


Border = "-" * 60


# -------------------------------------------------------
# Step 1 : Load the Data Set
# -------------------------------------------------------

print(Border)
print("Step 1 : Load the Data Set")
print(Border)

df = pd.read_csv("Fraudulent_Transaction_Detection.csv")

print(df.head())

print("\nSize of the Dataset:")
print(df.shape)

print("\nColumn names:")
print(df.columns)


# -------------------------------------------------------
# Step 2 : Check Missing Values
# -------------------------------------------------------

print("\n" + Border)
print("Step 2 : Check Missing Values")
print(Border)

print("Missing values are:")
print(df.isnull().sum())

df = df.dropna()

print("\nMissing values removed.")
print(Border)


# -------------------------------------------------------
# Step 3 : Define Features and Target
# -------------------------------------------------------

print("\n" + Border)
print("Step 3 : Define Features and Target")
print(Border)

target = "Fraud"

X = df.drop(target, axis=1)
Y = df[target]

print("\nFeatures:")
print(X.head())

print("\nTarget:")
print(Y.head())

print(Border)


# -------------------------------------------------------
# Step 4 : Encoding Categorical Variables
# -------------------------------------------------------

print("\n" + Border)
print("Step 4 : Encoding Categorical Variables")
print(Border)

categorical_columns = X.select_dtypes(
    include=["object", "category"]
).columns.tolist()

numerical_columns = X.select_dtypes(
    include=["int64", "float64"]
).columns.tolist()

print("\nCategorical columns:")
print(categorical_columns)

print("\nNumerical columns:")
print(numerical_columns)


# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numerical_columns),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_columns)
    ],
    remainder="drop"
)

print("\nPreprocessing created successfully.")


# -------------------------------------------------------
# Step 5 : Train Test Split
# -------------------------------------------------------

print("\n" + Border)
print("Step 5 : Train Test Split")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42,
    stratify=Y
)

print("\nTraining Data:", X_train.shape)
print("Testing Data:", X_test.shape)

print("\nData Split Successfully...")


# -------------------------------------------------------
# Step 6 : Create Models
# -------------------------------------------------------

print("\n" + Border)
print("Step 6 : Create Models")
print(Border)


decision_tree = DecisionTreeClassifier(
    max_depth=5,
    random_state=42
)


# Bagging 
bagging = BaggingClassifier(
    estimator=DecisionTreeClassifier(
        max_depth=5,
        random_state=42
    ),
    n_estimators=100,
    random_state=42
)


# Random Forest
r_forest = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    random_state=42,
    class_weight="balanced"
)


# AdaBoost
adaboost = AdaBoostClassifier(
    n_estimators=100,
    random_state=42
)


models = {
    "Decision Tree": decision_tree,
    "Bagging": bagging,
    "Random Forest": r_forest,
    "AdaBoost": adaboost
}

print("Model Creation done Successfully...")


# -------------------------------------------------------
# Step 7 : Train Models and Evaluate
# -------------------------------------------------------

print("\n" + Border)
print("Step 7 : Train Models and Evaluate")
print(Border)


result = []


for name, model in models.items():

    print("\n" + "=" * 60)
    print(name)
    print("=" * 60)

    # Create complete pipeline
    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", model)
        ]
    )

    # Train model using TRAINING data
    pipeline.fit(X_train, Y_train)

    # Predict using TEST data
    y_pred = pipeline.predict(X_test)

    # Metrics
    accuracy = accuracy_score(Y_test, y_pred)

    precision = precision_score(
        Y_test,
        y_pred,
        zero_division=0
    )

    recall = recall_score(
        Y_test,
        y_pred,
        zero_division=0
    )

    f1 = f1_score(
        Y_test,
        y_pred,
        zero_division=0
    )

    print("\nAccuracy :", accuracy)
    print("Precision:", precision)
    print("Recall   :", recall)
    print("F1 Score :", f1)

    print("\nConfusion Matrix:")
    print(confusion_matrix(Y_test, y_pred))

    print("\nClassification Report:")
    print(
        classification_report(
            Y_test,
            y_pred,
            zero_division=0
        )
    )

    result.append({
        "Model": name,
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1
    })


# -------------------------------------------------------
# Step 8 : Compare Models
# -------------------------------------------------------

print(Border)
print("Step 8 : Model Comparison")
print(Border)

result_df = pd.DataFrame(result)

print(result_df)


# -------------------------------------------------------
# Step 9 : Find Best Model
# -------------------------------------------------------

best_model = result_df.loc[
    result_df["F1 Score"].idxmax()
]

print("\n" + Border)
print("Best Model")
print(Border)

print("Model    :", best_model["Model"])
print("Accuracy :", best_model["Accuracy"])
print("Precision:", best_model["Precision"])
print("Recall   :", best_model["Recall"])
print("F1 Score :", best_model["F1 Score"])


# -------------------------------------------------------
# Step 10 : Visualize Model Comparison
# -------------------------------------------------------

result_df.set_index("Model")[
    ["Accuracy", "Precision", "Recall", "F1 Score"]
].plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Fraud Detection Model Comparison")
plt.ylabel("Score")
plt.xlabel("Models")
plt.xticks(rotation=0)
plt.legend(loc="lower right")
plt.tight_layout()
plt.show()

print(Border)