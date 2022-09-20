#Global variables can be used inside/outside functions 

x = "Devil"
def myFunc():
    print("Good night", x)
    print("Good night"+ x)

myFunc()
print("------------") #separete prints

#Creat a variable with same name globlas variable inside a function
    #only can be used this new value inside the function
def myFunc1():
    x = "God"
    print("Good night", x)
    print("Good night"+ x)

myFunc1()
print("------------") #separete prints

#The global keyword 
    #Creat a global variable using word "global" inside function
def myFunc2():
    global z 
    z = "Thiago"

myFunc2()
print("My name is", z)
print("------------") #separete prints

#Change global variable inside function 
w = "Thiago"
print("My name is", w)

def myFunc3(): 
    global w
    w = "Matheus"

myFunc3()
print("My name is", w)
print("------------") #separete prints
