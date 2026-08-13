from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier

import pandas as pd

Border = "-"*40

##################################################################################
#Step 1 : Load the Dataset
###################################################################################

print(Border)
print("Step 1 : Load the Dataset")
print(Border)

Data = pd.read_csv("MarvellousInfosystems_PlayPredictor.csv")

print("Original Data: ")
print(Data)
print("Total number of columns are: ", Data.shape)

print(Border)

##################################################################################
#Step 2 : Clean the Dataset
###################################################################################

print(Border)
print("Step 2 : Clean the Dataset")
print(Border)

wobj = LabelEncoder()   # creates object of Label Encorder
tobj = LabelEncoder()
pobj = LabelEncoder()


# Converting String into numeric value
Data["Weather"] = wobj.fit_transform(Data["Weather"])
Data["Temperature"] = tobj.fit_transform(Data["Temperature"])
Data["Play"] = pobj.fit_transform(Data["Play"])

print("\nEncoded Data: ")
print(Data)

# Features
X = Data[["Weather" , "Temperature"]]

# Label
Y = Data["Play"]

print(Border)

##################################################################################
#Step 3 : Train the model
###################################################################################

print(Border)
print("Step 3 : Train the model")
print(Border)

model = KNeighborsClassifier(n_neighbors=5)

model = model.fit(X ,Y)

print("Model Training done Successfully...")
print(Border)

##################################################################################
#Step 4 : Test the model
###################################################################################

print(Border)
print("Step 4 : Test the model")
print(Border)

weather = input("\nEnter Weather(Sunny/Overcast/Rainy): ")
temperature = input("\nEnter Temperature(Hot/Cold/Mild): ")

# Convert user input into numeric values
weather_value = wobj.transform([weather])[0]
temperature_value = tobj.transform([temperature])[0]

# Create DataFrame with the same feature names used during training
test_data = pd.DataFrame(
    [[weather_value, temperature_value]],
    columns=["Weather", "Temperature"]
)

# Predict
predict = model.predict(test_data)

# Convert numeric prediction back to original string
result = pobj.inverse_transform(predict)

print("\nFinal Prediction is: ", result[0])






