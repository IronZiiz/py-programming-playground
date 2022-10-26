# Tuples are unchangeable or immutable, but there is a workaraund
    #Convert tuple into a list, soon convert the list back into a tuple 

x = ("Thiago", "Zilli")
y = list(x)
y[1] = "666"
x = tuple(y)
print(x)
print("------------")

# Add items
x = ("Thiago", "Zilli")
y = list(x)
y.append("Devil")
myTuple = tuple(y)
print(myTuple)
print("------------")

# add tuple to a tuple 
myTuple = ("Thiago", "Zilli")
y = ("666",)
myTuple += y 
print(myTuple)
print("------------")

# Remove Items 
x = ("Thiago", "Zilli")
y = list(x)
y.remove("Zilli")
myTuple = tuple(y)
print(myTuple)

# Delete tuple
myTuple = ("Thiago", "Zilli")
del myTuple
 
