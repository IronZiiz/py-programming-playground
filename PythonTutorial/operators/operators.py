#used to perform operations on variables and values.
"""
Arithmetic operators
Assignment operators
Logical operators
Identity Operators 
Membership Operators
Bitwise Operators
"""

#Arithmetic
x = 344
y = 322

a = x+y
b = x-y
c = x*y
d = x/y
e = x%y
f = x**y
g = x//y

#Assignment 
a=666
a+=333
a-=333
a*=333
a/=333
a%=333
a//=3
a**=0
a =666
a&=3 # does a bitwise AND operation on them and assigns the result to the variable.
a|=3 # does a bitwise OR operation on them and assigns the result to the variable.
a^=3 # does a bitwise XOR operation on them and assigns the result to the variable.
a>>=3# The right shift assignment operator (>>=) moves the specified amount of bits to the right and assigns the result to the variable.
a<<=3# The left shift assignment operator (<<=) moves the specified amount of bits to the left and assigns the result to the variable.

#Comparison Operators
x = 322
y = 344

x == y
x != y
x > y 
x < y
x >= y
x <= y


#Logical operators
x = 666
print(x < 333 and x < 667) #return False
print(x < 333 or x < 667)  #return True 
print (not(x>333 and x<667))#return False beacause 'not' is used to reverse the result 
print("------------")

#Identity Operators 
#compare the objects, not if they are equal, but if they are actually the same object, with the same memory location

x = ["666", "333"]
y = ["666", "333"]
z = x 

print(z is x) #Same memory location. Return True
print(x is y) #not same memory location. Return False
print(x is not y)#not same memory location.Retun True 
print(x == y) #Equal values, but not same memory Location. Return True
print("------------")

x = ["Devil", "666"]
print("Devil" in x) #Return True
print("God" in x)   #Return True


#Bitwise Operators 
"""
& 	AND	Sets each bit to 1 if both bits are 1
|	OR	Sets each bit to 1 if one of two bits is 1
 ^	XOR	Sets each bit to 1 if only one of two bits is 1
~ 	NOT	Inverts all the bits
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
"""

