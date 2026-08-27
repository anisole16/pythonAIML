# Standard Scalar

import numpy as np
from sklearn.preprocessing import StandardScaler

X = np.array([[25 , 20000 ],
             [30, 40000], 
              [35, 80000]
                ])

scalar = StandardScaler()
scaled_value = scalar.fit_transform(X)

print(scaled_value)


# Feature Scaling is Called As Standard Scalar
