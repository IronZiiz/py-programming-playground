def hyn():
    print("------------")

# Searching Arrays 
    # where() method 
import numpy as np 

x = np.array([6, 66 ,666 , 6 , 2 ,4 ,6 ,7 ,8, 9, 9])
y = np.where(x == 6)
print(y) # return indexes where the values are six

x = np.array([6, 66 ,666 , 6 , 2 ,4 ,6 ,7 ,8, 9, 9])
y = np.where(x%2 == 0) # search index where the values are evehyn()
print(y)

x = np.array([6, 66 ,666 , 6 , 2 ,4 ,6 ,7 ,8, 9, 9])
y = np.where(x%2 == 1) # search index where the values are odd

hyn()

# Search Sorted 

x = np.array([1, 3, 2, 4])
y = np.searchsorted(x, 3)# read left side. 
print(y) # return where the value would be inserted  

x = np.array([1, 3, 2, 4])
y = np.searchsorted(x, 3, side = 'right')# read rigth side. 
print(y) # return where the value would be inserted  
hyn()

# multiple values
    # use an array with the specified values
x = np.array([1, 3, 2, 4])
y = np.searchsorted(x, [2 , 4])
print(y) 