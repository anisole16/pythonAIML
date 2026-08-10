import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score , confusion_matrix , classification_report


Border = "-"*30
#####################################################################
# Step 1 : Load the model
######################################################################


print(Border)
print("Step 1: Load the Dataset")
print(Border)

df = pd.read_csv("student_performance_ml.csv")
print(df.head()) # prints first five values by default
print(df.tail()) # prints last five values by default

print(Border)

#####################################################################
# Step 2: Data Analysis
######################################################################
print(Border)
print("Step 2: Data Analysis")
print(Border)
X = df[
    [
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours"
    ]
]

y = df["FinalResult"]

print("Features are:")
print(X.columns.tolist())

print("Target is:")
print(y)

print("Data Analysis Done Successfully...")
print(Border)


#####################################################################
# Step 3: Split the data for training and testing
######################################################################
print(Border)
print("Step 3: Split the data for training and testing")
print(Border)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Training data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)

#####################################################################
# Step 4: Train Decision Tree Model and make Predictions
######################################################################
print(Border)
print("Step 4: Train Decision Tree Model")
print(Border)

model = DecisionTreeClassifier(random_state=42)
model = model.fit(X_train , y_train)
result = model.predict(X_test)

print("Predictions made are: ")
print(result)

print(Border)

#####################################################################
# Step 5: Calculate Accuracy
######################################################################
print(Border)
print("Step 5: Calculate Accuracy")
print(Border)


accuracy = accuracy_score(y_test , result)
print("Accuracy is: ", accuracy * 100)
print(Border)


#####################################################################
# Step 6: Calculate confussion Matrix
######################################################################
print(Border)
print("Step 6: Calculate Confusion Matrix")
print(Border)

cm =confusion_matrix(y_test , result)
print("\nConfussion Matrix is: ")
print(cm)

print(Border)

#####################################################################
# Step 7: Classification Report
######################################################################
print(Border)
print("Step 7: Classification Report")
print(Border)

print("Classification Report: ")
print(classification_report(y_test , result))
print(Border)


#####################################################################
# Step 8: Check Training & Testing Accuracy
######################################################################
print(Border)
print("Step 8: Check Training & Testing Accuracy")
print(Border)

train_pred = model.predict(X_train)
test_pred = model.predict(X_test)

train_accuracy = accuracy_score(y_train , train_pred)
test_accuracy = accuracy_score(y_test , test_pred)

print("Training Accuracy is: ",train_accuracy * 100)
print("Testing Accuracy is: ",test_accuracy * 100)

print(Border)



#####################################################################
# Step 9: Compare max_depth
######################################################################
print(Border)
print("Step 9: Compare max_depth")
print(Border)


depths = [1 ,3 , None]
print("\nDecision Tree Comparison: ")

for depth in depths:
    tree = DecisionTreeClassifier(
        max_depth=depth , random_state=42
    )

    tree.fit(X_train , y_train)
    train_pred = tree.predict(X_train)
    test_pred = tree.predict(X_test)

    train_acc = accuracy_score(y_train , train_pred)
    test_acc= accuracy_score(y_test , test_pred)

    print("Maximum depth: ", depth)
    print("Training accuracy: ", train_acc)
    print("Testing Accuracy: ", test_acc)


print(Border)  


#####################################################################
# Step 10: Predict Result of New Student
######################################################################


new_student = pd.DataFrame({
    
        "StudyHours" : [6],
        "Attendance" : [85],
        "PreviousScore" : [66],
        "AssignmentsCompleted" : [7],
        "SleepHours" : [7]

})

predictions = model.predict(new_student)
print("\nNew Student Predictions: ")
print(predictions[0])

print(Border)
print("End of Case Study")
print(Border)



      










