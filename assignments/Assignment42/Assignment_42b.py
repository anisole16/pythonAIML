# The value of program may vary with k value


from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler



# Features 

X = [
    [1,2] , [2,3] , [3,1] , [6,5]
]

labels = ["Red" ,"Red" , "Blue" , "Blue"]

sobj = StandardScaler()
X_scaled = sobj.fit_transform(X)

# Consider a new point
x =float(input("Enter the X co-ordinate: "))
y =float(input("Enter the Y co-ordinate: "))


new_point = [[x,y]]
new_point_scaled = sobj.transform(new_point)


print("\nPrediction the result: ")

for k in [1, 3, 5]:
    if k > len(X):
        print("Invalid k value....")
        continue

    kobj = KNeighborsClassifier(n_neighbors=k)
    kobj.fit(X_scaled , labels)
    result = kobj.predict(new_point_scaled)

    print(f"K = {k} -> {result[0]}")
