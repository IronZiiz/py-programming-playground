mySet = {"Thiago", "Zilli"}
mySet.add("666")
print(mySet)
print("------------")

#Use update() method 
mySet = {"Thiago", "Zilli"}
mySeti = {"666", "999"}

mySet.update(mySeti)
print(mySet)
print("------------")

#Add any iterable 
mySet = {"Thiago", "Zilli"}
myList = ["666", "999"]

mySet.update(myList)
print(mySet)