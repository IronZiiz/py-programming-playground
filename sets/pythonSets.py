#Used to store multiple items in a single variable
    #Is unordered, unchangeable, unindexed 

mySet = {"Thiago", "Zilli"}
print(mySet)
print("------------")

#Duplicates not allowed
    #ignore duplicate values
mySet = {"Thiago", "Zilli", "Thiago"}
print(mySet)
print("------------")

#Get the length of a set 
    #Use len()
mySet = {"Thiago", "Zilli"}
print(len(mySet))
print("------------")

#Set items - Data types 
mySeti = {"Thiago", "Zilli"}
mySetii = {6,66,666}
mySetiii = {True, False, True}
mySetiv = {"Thiago", True, 666}

#Use type()
mySeti = {"Thiago", "Zilli"}
print(type(mySet))
print("------------")

#Use set() constructor
mySet = set(("Thiago", "Zilli"))
print(mySet)