def hyn():
    print("------------")
# Generate random number
from numpy import random 

tz = random.randint(100) # integer num 
print(tz)

hyn()

# Generate random float 
tz = random.rand() # float number between 0 and 1 
print(tz)
hyn()

# Generate random Array 
    # integers 
tz = random.randint(100, size=(4)) # one dimension 
print(tz)
hyn()

tz1 = random.randint(100, size=(2,3)) # two dimension
print(tz1)
hyn()

    # float 
tz = random.rand(5) # generate five float numbers 
print(tz)
hyn()

tz1 = random.rand(3, 3)
print(tz)
hyn()

# Generate random number from array 
    # choice module 
tz = random.choice([1, 6, 12, 19, 194, 45, 59])
print(tz)
hyn()

tz1 = random.choice([1, 6, 12, 19, 194, 45, 59], size = (3, 3))
print(tz1)
