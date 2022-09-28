#Through the list items by using a for loop 

myList = ["one","two","three"]
for x in myList:
    print(x)
print("------------")

#Loop Through the Index Numbers
myList = ["one","two","three"]
for i in range(len(myList)):
    print(myList[i])
print("------------")

#Using a While Loop
    #Through the list items by using a while loop 
    #Use len() and start at 0 

myList = ["one","two","three"]
i = 0
while i < len(myList):
    print(myList[i])
    i = i + 1 
print("------------")

#Looping Using List Comprehension
    #Short hand for 
myList = ["one","two","three"]
[print(x) for x in myList]
print("------------")
