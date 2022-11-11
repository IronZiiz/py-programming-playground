def hyn():
    print("------------")
#Joining NumPy Arrays 
    # putting contents of two or more arrayss in a single array
    # concatenate() method

import numpy as np 

x = np.array([6, 66, 666])
y = np.array([3, 33, 333])

xy = np.concatenate((x, y))
print(xy)

x = np.array([[6, 66, 666], [5, 55, 555]])
y = np.array([[3, 33, 333], [7, 77, 777]])

xy = np.concatenate((x, y), axis = 1) # specify row (axis = 1)
hyn()

# Joining Arrays Using Stack Functions
    # along a new axis
x = np.array([6, 66, 666])
y = np.array([3, 33, 333])

xy = np.stack((x, y), axis = 1)
print(xy)
hyn()

# Stacking Along Rown
    # hstack method to stack along rows
x = np.array([6, 66, 666])
y = np.array([3, 33, 333])

xy = np.hstack((x, y))
print(xy)
hyn()

# Stacking Along Columns 
    # vstack() to stack along colums 
x = np.array([6, 66, 666])
y = np.array([3, 33, 333])

xy = np.vstack((x, y))
print(xy)
hyn()

# Stacking Along Height (depth)
    # dstack() to stack along height
x = np.array([6, 66, 666])
y = np.array([3, 33, 333])

xy = np.dstack((x, y))
print(xy)
hyn()
