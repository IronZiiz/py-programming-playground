def hyn():
    print("------------")

# Filtering Arrays 
    # creating a new array with only elements that you choose 
    # using a boolean index list 

import numpy as np 

x = np.array([6, 66, 666 ,6666])
y = [False, False, True, False]

z = x[y]
print(z)
hyn()

# Creating the Filter Array 
x = np.array([6, 66, 666 ,6666])
    # Create an empty list
filter_arr = []
 
for element in x: 
    if element > 66: 
        filter_arr.append(True)
    else: 
        filter_arr.append(False)

y = x[filter_arr]

print(filter_arr)
print(y)
hyn()

# Only even elements 
x = np.array([2,3124,412415,15,215443,665,7,68,68,786,86,786,86,7,679672,132,1])

filter_arr = []

for element in x: 
    if element % 2 == 0: 
        filter_arr.append(True)
    else: 
        filter_arr.append(False)

y = x[filter_arr]

print(filter_arr)
print(y)
hyn()

# Creating Filter Directly from Array

x = np.array([12, 35,14, 125, 567, 13, 666])
filter_arr = x > 12 

y = x[filter_arr]

print(filter_arr)
print(y)
hyn()

x = np.array([2,3124,412415,15,215443,665,7,68,68,786,86,786,86,7,679672,132,1])
filter_arr = x % 2 == 0 

y = x[filter_arr]

print(filter_arr)
print(y)
hyn()