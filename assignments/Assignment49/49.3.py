import numpy as np
from sklearn.preprocessing import StandardScaler

# Two points
P1 = np.array([20, 20000])
P2 = np.array([30, 80000])

# Euclidean distance before scaling
distance_before = np.linalg.norm(P1 - P2)

# Apply Standard Scaling
data = np.array([P1, P2])

scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Scaled points
P1_scaled = scaled_data[0]
P2_scaled = scaled_data[1]

# Euclidean distance after scaling
distance_after = np.linalg.norm(P1_scaled - P2_scaled)

print("Points before scaling:")
print("P1:", P1)
print("P2:", P2)

print("\nEuclidean distance before scaling:", distance_before)

print("\nPoints after Standard Scaling:")
print("P1:", P1_scaled)
print("P2:", P2_scaled)

print("\nEuclidean distance after scaling:", distance_after)

# before scaling large scale features are present 
# after scaling the points are modified in range 