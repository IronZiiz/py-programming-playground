myDict = {
    "name": "Thiago",
    "last name": "Zilli",
    "year": 17
}
x = myDict["name"]
print("------------")

# Use get()
myDict = {
    "name": "Thiago",
    "last name": "Zilli",
    "year": 17
}
x =  myDict.get("name")
print("------------")

# Get Keys 
myDict = {
    "name": "Thiago",
    "last name": "Zilli",
    "year": 17
}
x =  myDict.keys()
print(x)

myDict["name"] = "Albert"

print(x)

print("------------")

# Get Values
myDict = {
    "name": "Thiago",
    "last name": "Zilli",
    "year": 17
}
x =  myDict.values()
print(x)

myDict["name"] = "Albert"

print(x)

print("------------")

# Get items 
myDict = {
    "name": "Thiago",
    "last name": "Zilli",
    "year": 17
}
x =  myDict.items()
print(x)

myDict["name"] = "Albert"

print(x)

print("------------")


# Check if key exists
myDict = {
    "name": "Thiago",
    "last name": "Zilli",
    "year": 17
}
if "name" in myDict:
    print("Yes, 'name' is one of the keys in the myDict dictionary")
