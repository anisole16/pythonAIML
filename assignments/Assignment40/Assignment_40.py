import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score


Border = "-" * 40


# ============================================================
# LOAD DATASET
# ============================================================

print(Border)
print("LOAD DATASET")
print(Border)

df = pd.read_csv("student_performance_ml.csv")

print(df)


# ============================================================
# FEATURES AND TARGET
# ============================================================

print("\n" + Border)
print("FEATURES AND TARGET")
print(Border)

X = df.drop("FinalResult", axis=1)
y = df["FinalResult"]


# ============================================================
# TRAIN TEST SPLIT
# ============================================================

print("\n" + Border)
print("TRAIN TEST SPLIT")
print(Border)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# ============================================================
# TRAIN DECISION TREE
# ============================================================

print("\n" + Border)
print("TRAIN DECISION TREE")
print(Border)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Testing Accuracy:", accuracy * 100, "%")


# ============================================================
# 1. FEATURE IMPORTANCE
# ============================================================

print("\n========== 1. FEATURE IMPORTANCE ==========")

importance_df = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

print(importance_df)

print(
    "Most Important:",
    importance_df.loc[
        importance_df["Importance"].idxmax(), "Feature"
    ]
)

print(
    "Least Important:",
    importance_df.loc[
        importance_df["Importance"].idxmin(), "Feature"
    ]
)


# ============================================================
# 2. WITHOUT SLEEPHOURS
# ============================================================

print("\n========== 2. WITHOUT SLEEPHOURS ==========")

X_no_sleep = df.drop(
    ["FinalResult", "SleepHours"], axis=1
)

X_train_ns, X_test_ns, y_train_ns, y_test_ns = train_test_split(
    X_no_sleep, y, test_size=0.2, random_state=42
)

model_no_sleep = DecisionTreeClassifier(random_state=42)

model_no_sleep.fit(X_train_ns, y_train_ns)

pred_ns = model_no_sleep.predict(X_test_ns)

accuracy_ns = accuracy_score(y_test_ns, pred_ns)

print("Accuracy without SleepHours:", accuracy_ns * 100, "%")
print("Original Accuracy:", accuracy * 100, "%")


# ============================================================
# 3. STUDYHOURS + ATTENDANCE
# ============================================================

print("\n========== 3. STUDYHOURS + ATTENDANCE ==========")

X_selected = df[["StudyHours", "Attendance"]]

X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(
    X_selected, y, test_size=0.2, random_state=42
)

model_selected = DecisionTreeClassifier(random_state=42)

model_selected.fit(X_train_s, y_train_s)

pred_s = model_selected.predict(X_test_s)

accuracy_s = accuracy_score(y_test_s, pred_s)

print(
    "StudyHours + Attendance Accuracy:",
    accuracy_s * 100,
    "%"
)

print("Full Feature Accuracy:", accuracy * 100, "%")


# ============================================================
# 4. FIVE NEW STUDENTS
# ============================================================


print("\n========== 4. FIVE NEW STUDENTS ==========")

new_students = pd.DataFrame({
    "StudyHours": [2, 4, 6, 8, 10],
    "Attendance": [60, 70, 80, 90, 95],
    "SleepHours": [5, 6, 7, 8, 7],
    "PreviousScore": [50, 60, 70, 80, 90],
    "AssignmentsCompleted": [4, 6, 7, 9, 10]
})

# Arrange columns exactly like training data
new_students = new_students[X.columns]

new_students["PredictedResult"] = model.predict(new_students)

print(new_students)


# ============================================================
# 6. MISCLASSIFIED STUDENTS
# ============================================================

print("\n========== 6. MISCLASSIFIED STUDENTS ==========")

results = X_test.copy()

results["Actual"] = y_test
results["Predicted"] = y_pred

misclassified = results[
    results["Actual"] != results["Predicted"]
]

print(misclassified)

print(
    "Number of Misclassified Students:",
    len(misclassified)
)


# ============================================================
# 7. RANDOM STATE COMPARISON
# ============================================================

print("\n========== 7. RANDOM STATE COMPARISON ==========")

for random_state in [0, 10, 42]:

    temp_model = DecisionTreeClassifier(
        random_state=random_state
    )

    temp_model.fit(X_train, y_train)

    temp_pred = temp_model.predict(X_test)

    temp_accuracy = accuracy_score(
        y_test, temp_pred
    )

    print(
        "random_state =", random_state,
        "->", temp_accuracy * 100, "%"
    )


# ============================================================
# 8. DECISION TREE
# ============================================================

print("\n========== 8. DECISION TREE ==========")

root_index = model.tree_.feature[0]

print(
    "Root Feature:",
    X.columns[root_index]
)

plt.figure(figsize=(15, 10))

plot_tree(
    model,
    feature_names=X.columns,
    class_names=[str(x) for x in model.classes_],
    filled=True
)

plt.show()


# ============================================================
# 9. PERFORMANCE INDEX
# ============================================================

print("\n========== 9. PERFORMANCE INDEX ==========")

df["PerformanceIndex"] = (
    df["StudyHours"] * 2 + df["Attendance"]
)

print(df)

X_new = df.drop("FinalResult", axis=1)
y_new = df["FinalResult"]

X_train_new, X_test_new, y_train_new, y_test_new = train_test_split(
    X_new, y_new, test_size=0.2, random_state=42
)

model_new = DecisionTreeClassifier(random_state=42)

model_new.fit(X_train_new, y_train_new)

pred_new = model_new.predict(X_test_new)

accuracy_new = accuracy_score(
    y_test_new, pred_new
)

print(
    "Accuracy with PerformanceIndex:",
    accuracy_new * 100,
    "%"
)

print(
    "Original Accuracy:",
    accuracy * 100,
    "%"
)


# ============================================================
# 10. MAX_DEPTH = NONE
# ============================================================

print("\n========== 10. MAX_DEPTH = NONE ==========")

model_unlimited = DecisionTreeClassifier(
    max_depth=None,
    random_state=42
)

model_unlimited.fit(X_train, y_train)

train_pred = model_unlimited.predict(X_train)
test_pred = model_unlimited.predict(X_test)

training_accuracy = accuracy_score(
    y_train, train_pred
)

testing_accuracy = accuracy_score(
    y_test, test_pred
)

print(
    "Training Accuracy:",
    training_accuracy * 100,
    "%"
)

print(
    "Testing Accuracy:",
    testing_accuracy * 100,
    "%"
)