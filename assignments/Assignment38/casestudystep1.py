import pandas as pd

#####################################
# Step 1: Load the Dataset
#####################################

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