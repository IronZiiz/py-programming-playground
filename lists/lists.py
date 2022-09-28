#Multiple items in a single variable
    #Use to store collections of data

myList = ["Thiago", "Zilli"]
print(myList)
print("------------")

#List items are indexed, the first item has [0]

#list Methods
    #That will change the order
myList = ["Thiago", "Zilli"]
myList1= ["Devil"]

myList = myList.append("666")   # Adds an element at the end of the list
myList = myList.clear()         # Removes all the elements from the list
myList = myList.copy()          # Returns a copy of the list
myList = myList.count(0)        # Returns the numbes of elementes with the specified value
myList = myList.extend(myList1) # Extend the list with another list
myList = myList.index("Devil")  # Returns the index of the first element with specified value
myList = myList.insert(1, "666")# Adds an element at the specified position 
myList = myList.pop(1, "666")   # Removes the element at the specified position 
myList = myList.Remove("Devil") # Removes the item with the specified value 
myList = myList.Reverse()       # Reverses the order of the list
myList = myList.sort            # Sorts the list 


#Allow Duplicates 
    #Have items with te same value

myList = ["Thiago", "Zilli", "Thiago", "Zilli"]
print(myList)
print("------------")

#list Length
    #Determine how many items a list has 
myList = ["Thiago", "Zilli"] 
print(len(myList)) 
print("------------")

#Any Data Types 
myList1 = ["Hello","World"]
myList2 = [1,2,3,4,5]
myList3 = [True, False, False]

#A list with any data types
myList = ["Thiago", True, 666]

#type()
myList= ["Thiago", "Zilli"]
print(type(myList))
print("------------")

#list constructor 
    #Creating a new list 
myList = list(("Thiago", "Zilli"))
print(myList)
