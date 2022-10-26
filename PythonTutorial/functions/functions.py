# Creating a function 
    # using "def"
from ctypes import resize


def myFunction():
    print("Thiago Zilli is a good man")
def hyphen():
    print("------------")


# Calling a Function 
def myFunction():
    print("Thiago Zilli is a good man")

myFunction()
hyphen()

# Arguments 
def myFunction(objt1):
    print(objt1 + "666")

myFunction("Thiago")
myFunction("Zilli")
hyphen()

# Number of Arguments 
    # Must be have number correct of arguments

def nameComplete(firstName, lastName):
    print(firstName + " " + lastName)
nameComplete("Thiago", "Zilli")
hyphen()

# Arbitrary Arguments 
    # use *
def myFunction(*names):
    print("Last name is: "+ names[-1])

myFunction("João", "Mario", "Johann")
hyphen()

# Keyword Arguments
def myFunction(name3, name2, name1):
    print("Last name is: "+ name3)
myFunction(name1 = "Thiago", name2 = "Johann", name3 = "Mario")
hyphen()

# Arbitrary Keyword Arguments 
    # use **
def myFunction(**namesObj): 
    print("Last object: " + namesObj["third"])
    
myFunction(first = "Pen", second = "table", third = "chair")
hyphen()

# Default Parameter Value 
def myFunction(name = "Thiago"):
    print("My name is " + name)

myFunction("Johann")
myFunction() #default 
myFunction("Mario")
hyphen()

# Passing a List as an Argument 
def myFunction(name):
    for x in name: 
        print(x)
name = ["Thiago", "Mario", "Johann"]
myFunction(name)
hyphen()

# Return Values 
def myFunction(x): 
    return 333*x 
print(myFunction(2))
print(myFunction(3))
hyphen()

# Pass statement
def myFunction():
    pass 


# Recursion 
def myFuncRecursion(x):
    if(x > 660):
        result = x + myFuncRecursion(x -  1)
        print(result)
    else:
        result = 660 
    return result

print("\n Recursion result")
myFuncRecursion(666)