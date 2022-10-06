def hyp():
     print("------------")

# using LISTS as ARRAYS ]
    # Numpy work with arrays in Python 

names = ["Thiago", "Mario", "Elrond"]
print(names)
hyp()

# Access the elements of an Array 
x = names[0]
print(x)
hyp()

    # Change value 

names[0] = "Galadriel"
print(names)
hyp()

# The length of an Array 
x = len(names)
print("The leght of array 'names' is " + x)
hyp()

# Looping Array Elements 
for x in names: 
    print(x)
hyp()

# Adding Array Elements 
names.append("Johann")
print(names)
hyp()

# Removing Array Elements 
names.pop(1)
print(names)
hyp()

 # or 

names.remove("Johann")
print(names)
hyp()