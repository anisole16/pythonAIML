
# Customer Loan Approval Using Voting Classification

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score

Border = "-" * 40

# ------------------------------------------------------------------------------
# Step 1: Load the Dataset
# ------------------------------------------------------------------------------

print("Step 1: Load the Dataset")
df = pd.read_csv("Customer_Loan_Approval.csv")

print("Dataset loaded Successfully...")
print("Size of Dataset:", df.shape)

print(Border)

# ------------------------------------------------------------------------------
# Step 2: Check Null Values
# ------------------------------------------------------------------------------

print("Step 2: Check Null Values")
print(Border)

print(df.isnull().sum())
print()

df = df.dropna()

# ------------------------------------------------------------------------------
# Step 3: Find Features and Target
# ------------------------------------------------------------------------------

print("Step 3: Find Features and Target")
print(Border)

X = df[
    [
        'Age',
        'Income',
        'CreditScore',
        'ExistingLoan',
        'EmploymentExperience',
        'LoanAmount'
    ]
]

Y = df['LoanApproved']

print("Identification of Features and Target done Successfully....")

# ------------------------------------------------------------------------------
# Step 4: Split the Data for Training and Testing
# ------------------------------------------------------------------------------

print(Border)
print("Step 4: Split the Data for Training and Testing")
print(Border)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

# Feature Scaling
scaler = StandardScaler()

X_train_scale = scaler.fit_transform(X_train)
X_test_scale = scaler.transform(X_test)

print("Data Split Successfully...")

# ------------------------------------------------------------------------------
# Step 5: Logistic Regression
# ------------------------------------------------------------------------------

print(Border)
print("Step 5: Logistic Regression")
print(Border)

log_reg = LogisticRegression(random_state=42)
log_reg.fit(X_train_scale , y_train)
y_pred1 = log_reg.predict(X_test_scale)
print("Prediction of logistic Regression: ", y_pred1)
print(Border)


# --------------------------------------------------------------------------
# Step 6: Decision Tree Classifier
# --------------------------------------------------------------------------

print(Border)
print("Step 6: Decision Tree Classifier")
print(Border)

dt_cls = DecisionTreeClassifier(random_state=42)
dt_cls.fit(X_train_scale, y_train)

y_pred2 = dt_cls.predict(X_test_scale)

print("Prediction of Decision Tree: ", y_pred2)
print(Border)

# ------------------------------------------------------------------------------
# Step 7: KNN
# ------------------------------------------------------------------------------

print(Border)
print("Step 7: KNN")
print(Border)

kn_cls = KNeighborsClassifier(n_neighbors=5)
kn_cls.fit(X_train_scale , y_train)
y_pred3 = kn_cls.predict(X_test_scale)
print(Border)

# ------------------------------------------------------------------------------
# Step 8: Accuracy
# ------------------------------------------------------------------------------

print(Border)
print("Step 8: Accuracy")
print(Border)


acc_lr = accuracy_score(y_test , y_pred1)
acc_dt = accuracy_score(y_test , y_pred2)
acc_knn = accuracy_score(y_test , y_pred3)

print("Accuracy of Logistic Regession: ",acc_lr)
print("Accuracy of Decision Tree: ",acc_dt)
print("Accuracy of KNN: ",acc_knn)

print(Border)


# ------------------------------------------------------------------------------
# Step 9: Hard Voting wih accuray
# ------------------------------------------------------------------------------

print(Border)
print("Step 9: Hard Voting")
print(Border)

hard_voting = VotingClassifier(estimators=[
    ('lr', log_reg),
    ('dt' , dt_cls),
    ('knn' , kn_cls)
],
voting='hard')

hard_voting.fit(X_train_scale , y_train)
y_pred_hard = hard_voting.predict(X_test_scale)
acc_hard = accuracy_score(y_test , y_pred_hard)

print("Accuracy of Hard Voting: ",acc_hard)
print(Border)


# ------------------------------------------------------------------------------
# Step 10: Soft Voting wih accuray
# ------------------------------------------------------------------------------

print(Border)
print(" Step 10: Soft Voting wih accuray")
print(Border)

soft_voting = VotingClassifier(estimators=[
    ('lr', log_reg),
    ('dt' , dt_cls),
    ('knn' , kn_cls)
],
voting='soft')

soft_voting.fit(X_train_scale , y_train)
y_pred_soft = soft_voting.predict(X_test_scale)
acc_soft = accuracy_score(y_test , y_pred_soft)

print("Accuracy of Soft Voting: ",acc_soft)
print(Border)



# --------------------------------------------------------------------------
# Step 11: Compare
# --------------------------------------------------------------------------

print(Border)
print("Step 11: Compare")
print(Border)

compare = pd.DataFrame({
    'Model': [
        'Logistic Regression',
        'Decision Tree',
        'KNN',
        'Hard Voting',
        'Soft Voting'
    ],
    'Accuracy': [
        f"{acc_lr:.4f}",
        f"{acc_dt:.4f}",
        f"{acc_knn:.4f}",
        f"{acc_hard:.4f}",
        f"{acc_soft:.4f}"
    ]
})

print(compare)
print(Border)
