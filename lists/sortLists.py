#sort()method that will sort the list alphanumerically, ascending, by default

#Sort Ascending
myList = ["Belzebu","Abaddon", "Demogorgon", "Cérbero"]
myList.sort()
print(myList)
print("------------")

myList = [666,333,111,222,555,777]
myList.sort()
print(myList)
print("------------")

#Sort Descending 
myList = ["Belzebu","Abaddon", "Demogorgon", "Cérbero"]
myList.sort(reverse= True)
print(myList)
print("------------")

myList = [666,333,111,222,555,777]
myList.sort(reverse= True)
print(myList)
print("------------")


#Customize Sort Function
    #Using Key word  argument key = function 
def myfunc(n): 
    return(n- 666)
myList = [666,333,111,222,555,777]
myList.sort(key = myfunc)
print(myList)
print("------------")

#Case insensitve Sort 
    #First capital letters
myList = ["Belzebu","abaddon", "demogorgon", "Cérbero"]
myList.sort()
print(myList)
print("------------")

myList = ["Belzebu","abaddon", "demogorgon", "Cérbero"]
myList.sort( key = str.lower)
print(myList)
print("------------")

#Reverse Order
    #Reverse the order o a list 
myList = ["Belzebu","abaddon", "demogorgon", "Cérbero"]
myList.reverse()
print(myList)
print("------------")