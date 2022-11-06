# numpy array copy vs view 

"""
The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.
"""
# COPY 
import numpy as np 
from globalFunctionsFolder.globalFunctions import hyn 

firstArray = np.array([6, 66, 666])
x = firstArray.copy()
firstArray[1] = 666999

print(firstArray)
print(x)
hyn()

# VIEW 
secArray = np.array([7,222, 2211 , 3334, 555])
y = secArray.view()
secArray[1] = 777

print(secArray)
print(x)
hyn()

# Make changes in the VIEW:
thiArray = np.array([333, 101, 2231 ,31224])
z = thiArray.view()
z[0] = 666

print(thiArray)
print(x)
hyn()

# Check if array owns its data
    # attribute base 
forArray = np.array([25, 0, 10, 1321, 1917])
x = forArray.copy()
y = forArray.view()

print(x.base)
print(y.base)
