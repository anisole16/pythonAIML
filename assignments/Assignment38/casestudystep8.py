import pandas as pd
import matplotlib.pyplot as plt

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

############################################################
# Step 5: Analyze the StudyHour and Attendance VS FinalResult
############################################################

print(Border)
print("Step 5: Analyze the StudyHour and Attendance VS FinalResult")
print(Border)    

print("Average StudyHours By Result is: ")
print(df.groupby("FinalResult")
      ["StudyHours"].mean())

print("Average Attendance by Result: " )
print(df.groupby("FinalResult") 
      ["Attendance"].mean())

study_result = (df.groupby("FinalResult")
["StudyHours"].mean())

attendance_result = (df.groupby("FinalResult") 
["Attendance"].mean())


print("---------Observations---------------")
if study_result[1] > study_result[0]:
    print("Passed Students have higher study Hours than failed Students which" \
    " suggests that if study hours are increased marks are increased")
if attendance_result[1] > attendance_result[0]:
    print("Passed Students have higher Attendance than Failed Students")
else:
    print("Passes Students do not have Higher Attendance")
    print("Attendance is not dertermined for result")    


############################################################
# Step 6: Histogram of StudyHours
############################################################

print(Border)
print("Step 6: Histogram of StudyHours")
print(Border) 

plt.figure(figsize = (8,5))
plt.hist(df["SleepHours"] ,bins=10)
plt.xlabel("StudyHours")
plt.ylabel("Number of Students")
plt.title("Distribution of Study Hours")
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

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

############################################################
# Step 5: Analyze the StudyHour and Attendance VS FinalResult
############################################################

print(Border)
print("Step 5: Analyze the StudyHour and Attendance VS FinalResult")
print(Border)    

print("Average StudyHours By Result is: ")
print(df.groupby("FinalResult")
      ["StudyHours"].mean())

print("Average Attendance by Result: " )
print(df.groupby("FinalResult") 
      ["Attendance"].mean())

study_result = (df.groupby("FinalResult")
["StudyHours"].mean())

attendance_result = (df.groupby("FinalResult") 
["Attendance"].mean())


print("---------Observations---------------")
if study_result[1] > study_result[0]:
    print("Passed Students have higher study Hours than failed Students which" \
    " suggests that if study hours are increased marks are increased")
if attendance_result[1] > attendance_result[0]:
    print("Passed Students have higher Attendance than Failed Students")
else:
    print("Passes Students do not have Higher Attendance")
    print("Attendance is not dertermined for result")    


############################################################
# Step 6: Histogram of StudyHours
############################################################

print("\n" + Border) 
print("Step 6: Histogram of Study Hours") 
print(Border) 
plt.figure(figsize=(8, 5))
plt.hist(df["StudyHours"], bins=10)
plt.xlabel("Study Hours") 
plt.ylabel("Number of Students") 
plt.title("Distribution of Study Hours") 

plt.savefig("step6_study_hours_histogram.png")
plt.show()

############################################################
# Step 7: Scatter Plot of StudyHours VS PreviousScore
############################################################

print("\n" + Border)
print("Step 7: Scatter Plot of Study Hours VS Previous Score") 
print(Border) 



passed_students = df[df["FinalResult"] == 1]
failed_students = df[df["FinalResult"] == 0]
plt.figure(figsize=(8, 5)) 
plt.scatter( passed_students["StudyHours"], passed_students["PreviousScore"], label="Pass" )
plt.scatter( failed_students["StudyHours"], failed_students["PreviousScore"], label="Fail" )
plt.xlabel("Study Hours") 
plt.ylabel("Previous Score")
plt.title("Study Hours VS Previous Score") 
plt.grid() 
plt.legend() 
plt.savefig("step7_scatter.png") 
plt.show()


############################################################
# Step 8: BoxPlot For Attendance
############################################################

print("\n" + Border)
print("Step 8: Boxplot For Attendance") 
print(Border) 

plt.figure(figsize = (7,5))
plt.boxplot(df["Attendance"] , vert = True)
plt.ylabel("Attendance")
plt.title("BoxPlot of Attendance")
plt.show()

# Identify Outlier using IQR

Q1 = df["Attendance"].quantitle(0.25)
Q3 = df["Attendance"].quantitle(0.75)

IQR = Q3 - Q1

lower_limit =  Q1 - 1.5 * IQR
upper_limit = Q1 - 1.5 * IQR

outlier = df[
    (df["Attendance"] < lower_limit) |
    (df["Attendance"] < upper_limit)
]

print("\n-----------Attendance Outlier----------------")
if len(outlier) == 0:
    print("No Attendance Outlier are present ")
else:
    print(outlier["Attendance"])    






















