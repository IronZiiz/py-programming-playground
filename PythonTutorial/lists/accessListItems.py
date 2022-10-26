#Access Items 
myList = ["Thiago", "Zilli", "666"]
print(myList[1])
print("------------")

#Negative Indexing 
myList = ["Thiago", "Zilli", "666"]
print(myList[-1])
print("------------")

#Range of Indexes 
    #Specifying where to start and where to end the range 
myList = ["Thiago", "Zilli", "666", "333", "Devil"]
print = (myList[2:4]) #4 is not include 
print("------------")

#Range of Negative Indexes 
myList = ["Thiago", "Zilli", "666", "333", "Devil"]
print = (myList[-3:-1])
print("------------")

#Check if Item Exists 
myList = ["Thiago", "Zilli", "666", "333", "Devil"]
if "ZIlli" in myList:
    print("Yes, 'Zilli' is in the fruits list")