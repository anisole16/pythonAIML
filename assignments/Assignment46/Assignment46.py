import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

Border = "-" * 30

# Step 1 : Load the data
print(Border)
print("Step 1 : Load the data")
print(Border)

data = pd.read_csv("Advertising.csv")

print("Dataset:")
print(data)

# Step 2 : Prepare the data
print(Border)
print("Step 2 : Prepare the data")
print(Border)

X = data[["TV", "radio", "newspaper"]]
Y = data["sales"]

print("Independent variables:", X.shape)
print("Dependent variables:", Y.shape)

# Step 3 : Train the model
print(Border)
print("Step 3 : Train the model")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, Y_train)

# Step 4 : Test the model
print(Border)
print("Step 4 : Test the model")
print(Border)

Y_pred = model.predict(X_test)

print(Y_pred)

# Step 5 : Display predicted and expected output
print(Border)
print("Step 5 : Display predicted and expected output")
print(Border)

print("Predicted Sales\tExpected Sales")

for predicted, expected in zip(Y_pred, Y_test):
    print(f"{predicted:.2f}\t\t{expected:.2f}")