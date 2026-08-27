# Salary VS Experience

from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

X = np.array([1 , 2 , 3, 4 , 5]).reshape(-1,1)
Y = np.array([20000 , 25000 , 30000 , 35000, 40000])

model = LinearRegression()

model = model.fit(X,Y)

exp = int(input("Enter Experience: "))

Y_pred = model.predict([[exp]])

print(f"Predicted salary for {exp} Years: ", Y_pred)

plt.scatter(X, Y, label="Actual Data")

# Regression line
plt.plot(X, model.predict(X), label="Regression Line")

plt.xlabel("Experience")
plt.ylabel("Salary")
plt.title("Salary vs Experience")

plt.legend()
plt.show()




