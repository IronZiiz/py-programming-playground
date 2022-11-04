def hyn():
    print("------------")

import numpy as np 

firstArray = np.array([6,66,666])
print(firstArray[0:2])
print(firstArray[0:])
print(firstArray[:2])
hyn()

# Negative Slicing 
secArray = np.array([7, 777, 999 ,333, 222, 111])
print(secArray[-3:-1]) # 3 from the end to index 1 
hyn()

# Step 
thiArray = np.array([8, 88, 911, 222, 444, 555])
print(thiArray[1:5:2]) 
print(thiArray[::2])
hyn()

# slicing 2-D array 
fouArray = np.array([[6,66,666],[7,777,77]])
print(fouArray[1, 1:3]) # second element 
print(fouArray[0:3, 2]) # Return two elements both elements 
print(fouArray[0:2, 2:3])

hyn()


