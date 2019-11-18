#Programming Assignment 7 Problem 1 _ Sergio _ 2ECE-A 

import numpy as np
X = np.random.random((5,5))
print(X)
#normalization formula
for x in X:
    Z = (x-X.mean()) / X.std()
    print(Z)
    