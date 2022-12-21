def hyn():
    print("------------")
# shuffling arrays 

from numpy import random 
import numpy as np 

a = np.array([6, 66, 666])
random.shuffle(a) # invert order 
print(a)
hyn()

a = np.array([6, 66, 666])
print(random.permutation(a)) # Re-arranged array
hyn()

