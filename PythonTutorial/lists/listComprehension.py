# List Comprehension
myList = ["six", "six1", "six2"]
newList = []

for x in myList:
    if "i" in x:
        newList.append(x)

print(newList) # Want a new list, containg only objects with the letter "i"
print("------------")

# With list comprehension 
myList = ["six", "six1", "six2"]
newList = [x for x in myList if "i" in x]
print(newList)
print("------------")

# The Syntax
    # newlist = [expression for item in iterable if condition == True]


#Condition (accepts the items tha valuate to True)
myList = ["six", "six1", "six2"]
newList = [x for x in myList if x != "six"] #No included six 
print(newList)
print("------------")

newList = [x for x in range(10)]
print(newList)
print("------------")

#Same example, but with a condition:
newList = [x for x in range(10) if x < 6]
print(newList)
print("------------")

#Expression
myList = ["six", "sixi", "sixii"]
newList = [x.upper() for x in myList]
print(newList)
print("------------")

#Set all values in the new list
myList = ["six", "sixi", "sixii"]
newList = ['sixiii' for x in myList]
print(newList)
print("------------")

myList = ["six", "sixi", "sixii"]
newList = [x if x != "six" else "sixi " for x in myList]
print(newList)
print("------------")