def hyn():
    print("------------")

# Splitting NumPy arrays
    # Breaks one array into multiple 

import numpy as np 

x = np.array([6, 66 ,666])
y = np.array_split(x, 3)
print(y)
hyn()

# Split into Arrays 

x = np.array([111, 11, 1, 2 ,22 ,222 ,333, 33, 3])
y = np.array_split(x, 3)

print(y[0])
print(y[1])
print(y[2])
    # Return new arrays with index
hyn()

# Splitting 2-D Arrays 
x = np.array([[2,22,222], [3, 33, 333], [4, 44, 444]])
y = np.array_split(x, 2)
print(y)
hyn()
# split the 2-D array into three 2-D arrays along rows 
x = np.array([[2,22,222], [3, 33, 333], [4, 44, 444]])
y = np.array_split(x, 3, axis = 1)
print(y)
hyn()

# opposit of hstack()
    # use hsplit() method
x = np.array([[2,22,222], [3, 33, 333], [4, 44, 444]])
y = np.hsplit(x, 3)
print(y)