#Join two Lists
    #Using + operator

listI = ["one", "Two", "Three"]
listII = [ 999,666,333]

listIII = listI + listII
print(listIII)
print("------------")

#Using append() method 
listI = ["one", "Two", "Three"]
listII = [ 999,666,333]

for x in listII: 
    listI.append(x)
print(listI)
print("------------")

#Using extend() method
listI = ["one", "Two", "Three"]
listII = [ 999,666,333]

listI.extend(listII)
print(listI)