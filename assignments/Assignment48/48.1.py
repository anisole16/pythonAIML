# predict the output of the following


from sklearn.linear_model import LinearRegression
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

