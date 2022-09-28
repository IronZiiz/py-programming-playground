#To change the value of a specific item, refer to the index number
myList = ["Thiago", "Zilli", "666"]
myList[1] = "Soares"
print(myList)
print("------------")

#Change a Range of Items Values 
myList = ["Thiago", "Zilli", "666"]
myList[:2] = ["Zilli", "AAAA"]
print (myList)
print("------------")

myList = ["Thiago", "Zilli", "666"]
myList[:2] = ["Zilli"]
print (myList)
print("------------")

#Insert Items 
myList = ["Thiago", "Zilli", "666"]
myList.insert(1,"AAA")
print(myList)