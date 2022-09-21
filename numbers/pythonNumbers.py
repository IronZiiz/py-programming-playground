#Three numeric types in Python

#int 
x = 666
y = -666
z =2923132232132 
print("------------") #separete prints
print(type(x))
print(type(y))
print(type(z))
print("------------") #separete prints

#float 

x = 66.6
y = 6.66
z = -666.6

print(type(x))
print(type(y))
print(type(z))
print("------------") #separete prints

#complex 

x = 333 + 333j
y = 666j 
z = -666j

print(type(x))
print(type(y))
print(type(z))
print("------------") #separete prints

#Type conversion 
    #Convert from one type to another 

x = 666
y = 66.6
z = 666j

#convert from int to float 
a = float(x)

#convert from float to int
b = int(y)

#convert from int to complex 
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
print("------------") #separete prints
 
#Random Number 
    #In python doens't have a function random number
    #but has a built-in module called random 

import random 
print (random.randrange(1, 666))
