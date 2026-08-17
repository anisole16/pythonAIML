import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
print("Size of The Datset: ", df.shape)
print("Columns are: ", df.columns)
print(df.dtypes)

print(Border)

##########################################################
# Describe the data
##########################################################

print(Border)
print("Describe the data")
print(Border)

print(df.describe())

print(Border)


##########################################################
# Add new Column
##########################################################

print(Border)
print("Add new Column")
print(Border)

df["Total"] = df["Math"] + df["Science"] + df["English"]

print(df)
print(Border)

##########################################################
# Check the Sudents who have scored more tha 85 in Science
##########################################################

print(Border)
print(" Check the Sudents who have scored more tha 85 in Science ")
print(Border)

result = df[df["Science"] > 85]
print(result)

print(Border)


##########################################################
# Replace the name
##########################################################

print(Border)
print(" Replace the name ")
print(Border)

df['Name'] = df['Name'].replace("Pooja" , "Puja")

print(df['Name'])

print(Border)

##########################################################
# Sort the Data in decending order
##########################################################

print(Border)
print(" Sort the Data in decending order")
print(Border)

df = df.sort_values(by= "Total" , ascending=False)
print(df)

print(Border)

##########################################################
# Bar plotting (importing matplotlib.pyplot)
##########################################################

print(Border)
print("Bar plotting")
print(Border)

plt.bar(df['Name'], df['Total'])

plt.xlabel('Student Name')
plt.ylabel('Total Marks')
plt.title('Student Names vs Total Marks')

plt.show()

print("Gaph ploted Successfully.....")

print(Border)


##########################################################
# Line plotting (importing matplotlib.pyplot)
##########################################################

print(Border)
print("Line plotting")
print(Border)

amit = df[df['Name'] == 'Amit'].iloc[0]

subjects = ['Math', 'Science', 'English']
marks = [amit['Math'], amit['Science'], amit['English']]

plt.plot(subjects, marks, marker='o')

plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.title("Amit's Marks Across Subjects")

plt.show()


##########################################################
# Fill the missing values
##########################################################

print(Border)
print("Fill the missing values")
print(Border)



data2 = {
    'Name': ['Amit', 'Sagar', 'Pooja' , "Rohit" , "Priya"],
    'Math': [np.nan, np.nan, 88 , 69 , 52],
    'Science': [91, np.nan, 85, 96 , 35 ]
}

df2 = pd.DataFrame(data2)

print("Before filling missing values:")
print(df2)

df2['Math'] = df2['Math'].fillna(df2['Math'].mean())
df2['Science'] = df2['Science'].fillna(df2['Science'].mean())

print("\nAfter filling missing values:")
print(df2)

print(Border)




