# marks = 5 StudyHours + 45


from sklearn.linear_model import LinearRegression

X = [[1] , [2] , [3] , [4] , [5]]
Y = [50 , 55 , 60 , 65 , 70 ]

model = LinearRegression()
model = model.fit(X ,Y)

print("Coefficient : ")
print(model.coef_[0])

print("Intercept: ")
print(model.intercept_)