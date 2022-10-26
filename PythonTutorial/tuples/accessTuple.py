myTuple = ("Thiago", "Zilli")
print(myTuple[1])
print("------------")

myTuple = ("Thiago", "Zilli")
print(myTuple[-1])
print("------------")

# Range of indexes
myTuple = ("Thiago", "Zilli", "666", "333", "Devil")
print(myTuple[1:3])
print("------------")

# Range of negative indexes
myTuple = ("Thiago", "Zilli", "666", "333", "Devil")
print(myTuple[-1:-3])
print("------------")

# Check if item exists
myTuple = ("Thiago", "Zilli", "666", "333", "Devil")
if "Thiago"in myTuple:
    print("YESSSS , 'Thiago is here!' ")
print("------------")