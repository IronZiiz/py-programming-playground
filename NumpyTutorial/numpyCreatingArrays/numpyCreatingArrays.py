def hyn():
    print("------------")
# array object in NumPy is called ndarray

import numpy as np 

firstArray = np.array([6,66,666])
print(firstArray)
print(type(firstArray))
hyn()

# Dimensions in Arrays  
secArray =  np.array(666)
print(secArray)
hyn()

# 1 -D arrays 
thiArray = np.array([666,66,6])
print(thiArray)
hyn()

# 2 -D arrays
    # often used to represent matrix or 2nd tensor 

fouArray = np.array([3,3],[6,6])
print(fouArray)
hyn()

# 3 -D arrays
    # often used to represent matrix or 3nd tensor 

fivArray = np.array([3,3],[6,6],[9,9])
print(fouArray)
hyn()

# Check Number of dimensions 
secArray =  np.array(666)
thiArray = np.array([666,66,6])
fouArray = np.array([3,3],[6,6])
fivArray = np.array([3,3],[6,6],[9,9])

print(secArray.ndim)
print(thiArray.ndim)
print(fouArray.ndim)
print(fivArray.ndim)
hyn()

# Higher Dimensional Arrays 
    # using the ndmin argument 

sixArray = np.array([666], ndmin= 6)
print(sixArray)
print("Number of dimension: ",sixArray.ndim)
hyn()


