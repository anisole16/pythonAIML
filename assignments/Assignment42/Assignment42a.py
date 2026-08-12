import math
from sklearn.preprocessing import StandardScaler

X = [
    [1, 2],
    [2, 3],
    [3, 1],
    [6, 5]
]

labels = ["Red", "Red", "Blue", "Blue"]

# Using StandardScaler
sobj = StandardScaler()
X_scaled = sobj.fit_transform(X)

x = float(input("Enter X coordinate: "))
y = float(input("Enter Y coordinate: "))


new_point = sobj.transform([[x, y]])

# Calculate Euclidean Distance
distance = []

for i in range(len(X_scaled)):
    d = math.sqrt(
        (new_point[0][0] - X_scaled[i][0]) ** 2 +
        (new_point[0][1] - X_scaled[i][1]) ** 2
    )

    distance.append((d, labels[i]))

# Sort distances
distance.sort()

# Consider 3 nearest neighbors
near = distance[:3]

print("\nNearest Neighbors:")

for d, label in near:
    print("Distance:", round(d, 2), "Class:", label)

# Count classes
red = 0
blue = 0

for d, label in near:
    if label == "Red":
        red += 1
    else:
        blue += 1

# Prediction
if red > blue:
    print("\nPrediction class: Red")
else:
    print("\nPrediction class: Blue")