def hyn():
    print("------------")

# Intarating Arrays 
import numpy as np 

x = np.array([6, 66, 666, 1, 11, 111])

for x in x: 
    print(x)
hyn()

# Intarating 2-D arrays 
x = np.array([[6, 66, 666], [1, 11, 111]])
for x in x: 
    print(x)

x = np.array([[6, 66, 666], [1, 11, 111]])
for x in x: 
    for y in x:
        print(y) # Return actual values. Scalars 

hyn()

# Intarating 3-D arrays 
x = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in x: 
    for y in x:
        for z in y:
            print(z)  
hyn()
# Intarating Arrays using nditer 
        # This method is very easy to intarating array with large dimesion 
x = np.array([[[6,66],[77,777]],[[23],[1456, 231]]])
for x in np.nditer(x, flags = ["refs_ok"]):
    print(x)

hyn( )
# Interating Array with different Data types 
    # use the op_dtypes argument to change datatypes while interating 
    # By default numpy cannot change the data type in the array, but it can do so using another space called buffer
    # use method nditer() with flag = ['buffered']Por padrão o numpy não pode alterar o data type no array, mas pode fazer isso usando outro espaco chamado buffer 

x = np.array([6, 66, 666])

for x in np.nditer(x, flags = ['buffered'], op_dtypes = ['S']): # change to string
    print(x)
hyn()

# Interating with different Step Size
    # filtering and followed by interation
x = np.array([[1,2,4],[1,6,7]])
for x in np.nditer((x[:, ::2])): 
    print(x)
hyn()

# Enumerated interation using ndenumerate()
    # send me the index of element 
x = np.array([[6, 66, 666],[1, 11, 333]])

for idx, x in np.ndenumerate(x):
    print(idx, x)