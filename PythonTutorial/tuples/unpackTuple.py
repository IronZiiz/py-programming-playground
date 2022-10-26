myTuple = ("Thiago", "Zilli", "666")
(one, two, three) = myTuple
print(one)
print(two)
print(three)
print("------------")

#Using Asterisk 
    #When number of variables is lees than the number of values, use * and the values will be assigned to the variable as a list

myTuple = ("Thiago", "Zilli", "666")
(one, *two) = myTuple
print(one)
print(two)
print("------------")