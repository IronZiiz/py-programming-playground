def hyp():
     print("------------")
# Class is like an object constructor

# Creat a Class
class my_Class:
    x = 666

# Creat Object
t1 = my_Class()
print(t1.x) # Access value 
hyp()

# The __init__() Function 
    # Assign values to object propertiies, or other operations that are necessary to do when the object is being created
class things: 
    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2 
T = things("Mouse", "Cup")

print(T.t1)
print(T.t2)
hyp()

# The __str__() function 
    # controls what should be returned when the class object is represented as a string.

class things: 
    def __init__(self, t1, t2, n):
        self.t1 = t1
        self.t2 = t2
        self.n = n
    def __str__(self):
        return f"{self.t1}({self.t2})({self.n})"
T = things("Mouse", "Cup", 666)
print(T.t1)
print(T.t2)
print(T.n)
hyp()

# Object Methods 
class things: 
    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2
    
    def my_func(self):
        print("In my home there:"+self.t1," and " +self.t2)

T = things("Mouse", "Cup")
T.my_func()
hyp()

# The self Parameter 
    # access variables that belings to the class 
    # Can be have another name 
    # First parameter of any function in the class 
class things: 
    def __init__(ANYTHING, t1, t2):
        ANYTHING.t1 = t1
        ANYTHING.t2 = t2
    
    def my_func(ANYTHING):
        print("In my home there:"+ANYTHING.t1," and " +ANYTHING.t2)

T = things("Mouse", "Cup")
T.my_func()
hyp()

# Modify Object Properties 
class things: 
    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2
    
    def my_func(self):
        print("In my home there:"+self.t1," and " +self.t2)

T = things("Mouse", "Cup")
T.my_func()
T.t1 = "Chair"
T.my_func()
hyp()

# Delete Object properties 
class things: 
    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2
    
    def my_func(self):
        print("In my home there:"+self.t1," and " +self.t2)

T = things("Mouse", "Cup")
del T.t1 # compiled error
T.my_func()
hyp()

# Delete Objects 
class things: 
    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2
    
    def my_func(self):
        print("In my home there:"+self.t1," and " +self.t2)

T = things("Mouse", "Cup")
del T
T.my_func()
hyp()

# The pass Statement
class things: 
    pass 