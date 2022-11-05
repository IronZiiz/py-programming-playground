# same data types default python

"""
-- extras --
 i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
""" 

import numpy as np 
from globalFunctionsFolder.globalFunctions import hyn

firstArray = np.array([6, 66, 666])
print(firstArray.dtype)
secArray = np.array(['thiago','Zilli'])
hyn()

# Creating Array with a defined data type 

thiArray = np.array([6, 66, 666], dtype = 'b')
print(thiArray)
print(thiArray.dtype)
hyn()

# What if a Value can not be conveted? 
"""
    ValueError: In Python ValueError is raised when the type of passed argument to a function is unexpected/incorrect.
"""

# converting Data type on existing array 
    # astype method 
        # create a copy of the array and allows you to specify the data type 
fouArray = np.array([6.66, 6.666, 666.6])
newArray =  fouArray.astype('i')
print(newArray)
print(newArray.dtype)


