def hyn():
    print("------------")
# Sorting Arrays 
    # ordered sequence of the elements 
        # Ascending or descending
    # sort() method 

import numpy as np 

    # with numbers 
x = np.array([66, 6, 666])
print(np.sort(x))

    # with strings
y = np.array(['Mouse', 'Calculator', 'Book'])
print(np.sort(y))

    # with boolean values 
z = np.array([True, False, True, False])
print(np.sort(z))

hyn()
# Sorting a 2-D array 

xyz = np.array([[5, 4, 1],[65, 31, 532]])
print(np.sort(xyz))
