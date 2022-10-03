myDict = {
    "name": "Thiago",
    "last name": "Zilli",
    "year": 17
}

for x in myDict:
    print(x)
print("------------")

# Print all values
myDict = {
    "name": "Thiago",
    "last name": "Zilli",
    "year": 17
}
for x in myDict:
    print(myDict[x])
print("------------")

    # or 

myDict = {
    "name": "Thiago",
    "last name": "Zilli",
    "year": 17
}
for x in myDict.values():
    print(x)
print("------------")

# Return Keys 
myDict = {
    "name": "Thiago",
    "last name": "Zilli",
    "year": 17
}
for x in myDict.keys():
    print(x)
print("------------")

# Return Keys and values 

myDict = {
    "name": "Thiago",
    "last name": "Zilli",
    "year": 17
}
for x, y in myDict.items():
    print(x, y)
print("------------")
