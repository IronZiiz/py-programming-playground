def hyn():
    print("------------")

# The shape of an array is the number of elements in each dimension.

# Get the Shape of an Array 
    # attribute shape 

import numpy as np 
firstArray = np.array([[222,22,2],[6,66,666]])
print(firstArray.shape)
hyn()

# expecify number of dimension
secArray = np.array([6,66,666,6666,66666,6666], ndmin = 6)
print(secArray)
print("shape of array :", secArray.shape)