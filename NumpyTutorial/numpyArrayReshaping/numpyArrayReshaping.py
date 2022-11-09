def hyn():
    print("------------")

# Reshape from 1-D to 2-D
import numpy as np 

firstArray = np.array([12, 124, 412, 1245, 1681, 1923, 1950, 1223, 1205, 190, 899 ,231])
newArray = firstArray.reshape(4, 3) # matriz with four lines and 3 colluns
print(newArray) 
hyn()

# Reshape from 1-D to 3-D
secArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newArray = secArray.reshape(2, 3, 2) # with two arrays with two colluns and three lines 
print(newArray)
hyn()

# Can we reshape into any shape ?
    # thiArray = np.array([345, 123, 456, 657, 490, 905, 777, 231])
    # newArray = thiArray.reshape(3, 3) # error 
    # print(newArray)

# Returns Copy or View? 
thiArray = np.array([345, 123, 456, 657, 490, 905, 777, 231])
newArray = thiArray.reshape(2, 4)
print(newArray)
hyn() 

# Unknown Dimension
    # Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.
    # Pass -1 as the value, and NumPy will calculate this number for you.

fourArray = np.array([345, 123, 456, 657, 490, 905, 777, 231])
newArray = fourArray.reshape(2, 2, -1)
print(newArray)
hyn() 

# Flattening the arrays 
    # Flattening array means converting a multidimensional array into a 1D array.

fivArray = np.array([[222, 333, 777], [555, 888, 999]])
newArray = fivArray.reshape(-1)
print(newArray)
