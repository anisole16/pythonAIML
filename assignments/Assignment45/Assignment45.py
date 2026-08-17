import pandas as pd
import matplotlib.pyplot as plt

Border = "-"*30
##########################################################
# Load the data
##########################################################

print(Border)
print("# Load the data")
print(Border)

data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}

df = pd.DataFrame(data)
print(df)

##########################################################
# Normalize he Math column
##########################################################

print(Border)
print("Normalize the Math column")
print(Border)

df["Math_Normalized"]  = (
    (df['Math'] - df['Math'].min()) / (df['Math'].max() - df['Math'].min() )
)
print("Normalized Math: ")
print(df[['Name' , 'Math' , 'Math_Normalized']])

print(Border)


##########################################################
# Create Gender Column
##########################################################

print(Border)
print("Create Gender Column")
print(Border)

df['Gender'] = ['Male' , 'Male' , 'Female']


df = pd.get_dummies(df , columns=['Gender'], dtype=int)
print(df)
print(Border)

##########################################################
# Group by Gender and calculate the average marks
##########################################################

print(Border)
print("Group by Gender and calculate the average marks")
print(Border)

data1 = pd.DataFrame(data)
print(data1)

data1['Gender'] = ['Male' , 'Male' , 'Female']

average_marks = data1.groupby('Gender')[['Math' , 'Science', 'English']].mean()

print(average_marks)

print(Border)

##########################################################
#Plot the pie-chart for SAGAR
##########################################################

print(Border)
print("Plot the pie-chart for SAGAR")
print(Border)

sagar = df[df['Name'] == 'Sagar'].iloc[0]

subjects = ['Math' , 'Science' , 'English']
marks = [sagar['Math'] , sagar['Science'] , sagar['English']]

plt.figure(figsize = (6,6))
plt.pie(marks , labels=subjects , autopct='%1.1f%%')
plt.title("Sagar's  Acadamic Graph ")
plt.show()
print("Pie chart ploted Sucesfully....")

print(Border)

##########################################################,.,.../l;l,.
# Add Status Column ie pass/fail
##########################################################

print(Border)
print("Add Status Column ie pass/fail")
print(Border)

df['Total'] = df[['Math' , 'Science' , 'English']].sum(axis =1)

df['Status'] = df['Total'].apply(lambda x: 'Pass' if x >= 250 else 'Fail')
print(df[['Name' , 'Total' , 'Status']])

print(Border)

##########################################################
# Count the number of passed students
##########################################################

print(Border)
print("Count the number of passed students")
print(Border)

passed_count = (df['Status'] == 'Pass').sum()
print("Number of passed Students is: ",passed_count)

print(Border)

##########################################################
# Convert Dataset to csv
##########################################################

print(Border)
print("Convert Dataset to csv")
print(Border)

df.to_csv('final_student.csv' , index=False)
print("csv exported Successfully...")

print(Border)

##########################################################
# Histogram maths Marks
##########################################################

print(Border)
print("Histogram maths Marks")
print(Border)

plt.figure(figsize=(7,5))
plt.hist(df['Math'] ,bins=5 , edgecolor='black')
plt.xlabel("Maths Marks")
plt.ylabel("Number of Students")
plt.title("Histogram of math marks")
plt.show()

print(Border)

##########################################################
# Rename the column
##########################################################

print(Border)
print("Rename the column")
print(Border)

df.rename(columns={'Math' : 'Mathematics'} , inplace=True)
print(df)
print(Border)

##########################################################
# BoxPlot of English Marks
##########################################################

print(Border)
print("BoxPlot of English Marks")
print(Border)

plt.figure(figsize=(6,3))
plt.boxplot(df['English'])
plt.ylabel('English Marks')
plt.title("BoxPlot of English Marks")
plt.show()

print(Border)





 