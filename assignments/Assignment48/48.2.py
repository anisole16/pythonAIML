# predict the output of the following


from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

X = np.array([1 , 2, 3 , 4 , 5]).reshape(-1,1)
Y = np.array([3 , 4 , 2 , 4 ,5])

model = LinearRegression()
model = model.fit(X,Y)

print("Mean of X: ", np.mean(X))
print("Mean of Y: ", np.mean(Y))
print("Slope (m): ", model.coef_[0])
print("Intercept: ", model.intercept_)

print("Regression Equation is: ")
print(f" Y = {model.coef_[0]}X + {model.intercept_}")

print()

# calculate all Y value using the equation

Y_pred = model.predict(X)
print(Y_pred)


for x, actual, predicted in zip(X.flatten(), Y, Y_pred):
    print(f"X = {x}, Actual Y = {actual}, Predicted Y = {predicted}")

# Calculate MSE
mse = mean_squared_error(Y, Y_pred)
print("\nMSE: ", mse)

# Calculate R2
r2 = r2_score(Y, Y_pred)
print("R2 Score: ", r2)

# Note

# zip is used to combine various values of multiple clumn together( X ,Y Y_pred)
# flatten is used because X is treated as 2-D array thus to create a single array flatten is used