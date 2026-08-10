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



############################################################
# Step 3: Calculate Average Study Hours , Attendance , Maximum previous Score and SleepHours
############################################################


print(Border)
print(" Step 3: Calculate Average Study Hours , Attendance , Maximum previous Score and SleepHours")
print(Border)

average_study_hours = df["StudyHours"].mean()
print("Average Study Hours are: ", average_study_hours)

average_attendance = df["Attendance"].mean()
print("Average Attendance: ",average_attendance)

maximum_previous_score = df["PreviousScore"].max()
print("Maximum Previous Score: ",maximum_previous_score)

minimum_sleep_hours = df["SleepHours"].min()
print("Minimum Sleep Hours are: ",minimum_sleep_hours)


############################################################
# Step 4: Distribution of passed and failed Students
############################################################


print(Border)
print("Step 4: Distribution of passed and failed Students")
print(Border)

result = df["FinalResult"].value_counts()
print("Final Result Distribution is ")
print(result)

pass_percent = (passed / total) * 100
print("Percenatage of Students who have passed is: ",pass_percent , "%")

failed_percent = (failed / total) * 100
print("Percenatage of Students who have failed is: ",failed_percent , "%")

if pass_percent > failed_percent:
    print("DataSet is imbalanced....")
else:
    print("The dataset is relatively balanced...")    







