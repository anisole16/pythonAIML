# predict marks using study Hours

from sklearn.linear_model import LinearRegression

X = [[1] , [2] , [3] , [4] , [5]]
Y = [50 , 55 , 60 , 65 , 70]

model = LinearRegression()
model = model.fit(X,Y)

hrs = float(input("Enter Study Hours: "))

Y_pred = model.predict([[hrs]])

print("Predicted Marks: ")
print(Y_pred[0])