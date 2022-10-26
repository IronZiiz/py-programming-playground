# A file containing a set of functions 

#  Create a module
    # this is on the myModule.py

# Use a mudele 
import myModule
myModule.getName("Thiago")
myModule.hyn()

# Variables in Module 
import myModule

x = myModule.objects["name"]
print(x)
myModule.hyn()

# Re-naming a Module 
import myModule as m1

x = m1.objects["weight"]
print(x)
m1.hyn()

# Built-in Modules 
import platform
x = platform.system()
print(x)
m1.hyn()

# Using the dir() 
    #list all the function names 
import platform
x = dir(platform)
print(x)
m1.hyn()

# Import from Module 
    # import only parts from a module
from myModule import objects
print(objects["height"])