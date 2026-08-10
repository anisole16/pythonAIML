import pandas as pd

Border = "-"*50


#####################################
# Step 1: Load the Dataset
#####################################

print(Border)
print("Step 1: Load the dataset")
print("Border")

df = pd.read_csv("student_performance_ml.csv")

print("----The First Five Records are------")
print(df.head())

print("-------The Last Five Records are------")
print(df.tail())

print("------The total Rows and columns in the dataset is--------")
print(df.shape)

print("\n ------------Column names--------------")
print(df.columns.tolist())

print("\n-------DataTypes-------------")
print(df.dtypes)


############################################################
# Step 2: Find number of students , Passed and Failed
############################################################


print(Border)
print("Step 2: Find number of students Passed and Failed")
print(Border)

total = len(df)   # total number of students
passed = (df["FinalResult"] == 1).sum()       # passed Students
failed = (df["FinalResult"] == 0).sum()       # failed Students
print("Total number of Students are: ",total)
print("Number of Passed Students: ",passed)
print("Number of Failed Students: ",failed)
