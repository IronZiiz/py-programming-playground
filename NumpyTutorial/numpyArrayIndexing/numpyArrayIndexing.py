def hyn():
    print("------------")

# Access array elements 
import numpy as np 

firstArray = np.array([6, 66, 666])
print(firstArray[1])
print(firstArray[1] + firstArray[2])
hyn()

# Access 2-D Array 
secArray = np.array([[3, 33, 333],[6, 66, 666]])
print("3nd element on 1s row", secArray[0,2])
hyn()

# Acess 3-D Array 
thiArray = np.array([[[1, 1, 1],[3, 3, 3]],[[7, 7, 7],[6, 6, 6]]])
print(thiArray[1, 0, 1])
hyn()

# Negative indexing 
secArray = np.array([[3, 33, 333],[6, 66, 666]])
print("last element from 2nd dim: ",secArray[1, -1] )