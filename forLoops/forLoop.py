# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

mylist= list("Thiago", "Zilli", "666")
for x in mylist:
    print(x)
print("------------")

# Looping through a string
for x in "Thiago Zilli":
    print(x)
print("------------")

# The break Statement 
mylist= list("Thiago", "Zilli", "666")
for x in mylist:
    print(x)
    if x == "Zilli":
        break 
print("------------")

# The continue Statement
mylist= list("Thiago", "Zilli", "666")
for x in mylist:
    if x == "Zilli":
        continue 
    print(x) 
print("------------")

# The range() Function 
for x in range(6): 
    print(x) #value  0 to 5 
print("------------")

for x in range(6, 66): 
    print(x) #value  2 to 5 
print("------------")


for x in range(6, 66, 3): # Increment 3 
    print(x)
print("------------")

# Else in For Loop 
for x in range(6,66):
    print(x)
else:
    print("Finally finished!")
print("------------")

# Nested Loop 
person = list("name:", "year:", "height:")
features = list("Thiago", "18", 1.8)

for x in person: 
    for y in features: 
        print(x,y)
print("------------")

# The pass Statement 

for x in [6, 66, 66]: 
    pass 
