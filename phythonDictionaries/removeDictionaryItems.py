# Removes the item with the specified key name
myDict = {
    "name": "Thiago",
    "last name": "Zilli",
    "year": 17
}
myDict.pop("name")
print(myDict)
print("------------")


# Removes the las insert item 
myDict = {
    "name": "Thiago",
    "last name": "Zilli",
    "year": 17
}
myDict.popitem()
print(myDict)
print("------------")

# del keyword
myDict = {
    "name": "Thiago",
    "last name": "Zilli",
    "year": 17
}
del myDict["name"]
print(myDict)
print("------------")

myDict = {
    "name": "Thiago",
    "last name": "Zilli",
    "year": 17
}
del myDict
print(myDict)
print("------------")


# empties the dictionary
myDict = {
    "name": "Thiago",
    "last name": "Zilli",
    "year": 17
}
myDict.clear()
print(myDict)
print("------------")
