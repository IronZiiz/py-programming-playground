#Use remove() method
mySet = {"Thiago", "Zilli"}
mySet.remove("Zilli")
print(mySet)
print("------------")

#Use discard() method 
mySet = {"Thiago", "Zilli"}
mySet.discard("Zilli")
print(mySet)
print("------------")

#Use pop() method 
    #Remove the last item, but the set is unordered
mySet = {"Thiago", "Zilli"}
x = mySet.pop()
print(x)
print("------------")

#Use clear() method
mySet = {"Thiago", "Zilli"}
mySet.clear()
print(mySet)
print("------------")

#Use del 
mySet = {"Thiago", "Zilli"}
del mySet
print(mySet)
print("------------")
