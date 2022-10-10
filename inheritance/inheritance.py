import numbers


def hyp():
    print("------------")
# class that inherits all the methods and properties from another class
    # parent class is the base class 
    # child class is the derived class

# Create a Parent Class

class Things:
    def __init__(self, obj1, obj2):
        self.obj1 = obj1
        self.obj2 = obj2

    def printObjects(self):
        print(self.obj1, self.obj2)

x = Things("chair, book")
x.printObjects()
hyp()

# Creat a Child Class
class furniture(Things):
    pass # not wanto to add any other properties or methods to the class

x = furniture("Sofa", "mirror")
x.printObjects()
hyp()

# Add the __init__() Function
    # in child class
class furniture(Things):
    def __init__(self, obj1, obj2)  # Overriddes the inheritance of the parent's 

    # keep the inheritance of the parent's __init__() function
class furniture(Things):
    def __init__(self, obj1, obj2):
        Things.__init__(self, obj1, obj2)
    

# Use the super() Function 
    # Will make the child class inherit all te methods and properties from its parent
class furniture(Things):
    def __init__(self, obj1, obj2):
        super().__init__(obj1, obj2)

# Add Properties 
class furniture(Things):
    def __init__(self, obj1, obj2):
        super().__init__(obj1, obj2)
        self.numberOfObjects = numbers

x = furniture("Bookshelf", "Table", 2)

# Add Methods 
class furniture(Things):
    def __init__(self, obj1, obj2):
        super().__init__(obj1, obj2)
        self.numberOfObjects = numbers
    
    def myObjects(self):
        print("This is my furnitures",self.obj1,self.obj2, ".Total:",self.numberOfObjects)
    