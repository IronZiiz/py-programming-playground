def hyn():
    print("------------")

# Local scope 
    # Only be used inside that function

def myFunction():
    x = 666  
    print(x)
myFunction()
hyn()

# Function Inside Function 
def myFunction():
    x = 300  
    def myInnerFunction(): 
        print(x) #varieble can be used here
    myInnerFunction()
myFunction()

# Global Scope
    # Can be used in all the code 

x = 666

def myFunction():
    print(x)
myFunction()

print(x)
hyn()

# Naming Variables
    # separete variable with same name (inside outside function)

x = 666

def myFunction(): 
    x = 333 
    print(x) # print 333

myFunction()

print(x) # print 666
hyn()

# Global Keyword 
    # creat global variable inside the function
def myFunction(): 
    global x
    x = 666 

myFunction()

print(x) # Print 666 too 
hyn()

    # Change global value inside the function

x = 333 

def myFunction():
    global x
    x = 666

myFunction()
print(x)
hyn()