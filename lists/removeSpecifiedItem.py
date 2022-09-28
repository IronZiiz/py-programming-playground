#Using remove() method
    #removes the specified item 
myList = ["Thiago", "Zilli"]
myList.remove("Thiago")
print(myList)
print("------------")

#Using pop() method 
    #removes the specified index
myList = ["Thiago", "Zilli"]
myList.pop(1)
print("------------")

#Using keyword del
myList = ["Thiago", "Zilli"]
del myList[1]
print(myList)
print("------------")

#Using clear() method 
myList = ["Thiago", "Zilli"]
myList.clear()
print(myList)