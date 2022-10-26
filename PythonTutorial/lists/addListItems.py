#Using append() method
myList = ["Thiago","Zilli"]
myList.append("666")
print(myList)
print("------------")

#Using insert() method
myList = ["Thiago","Zilli"]
myList.insert(1,"João")
print(myList)
print("------------")

#Using extend() method 
myList = ["Thiago","Zilli"]
myList1= ["999","666","333"]
myList.extend(myList1)
print(myList)
print("------------")

#Add any iterable with extend() method
myList = ["Thiago","Zilli"]
myTuple= ("999","666","333")
myList.extend(myTuple)
print(myList)
