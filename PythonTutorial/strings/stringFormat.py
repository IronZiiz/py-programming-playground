#String Format
    #using format() method 
a = 666 
txt = "The number of the beast is {}"
print(txt.format(a))
print("------------")

#Unlimited number of arguments 
a = 333 
b = 333 
c = 666 
txt = "The number of the beast is a sum of {} with {}  equal {}"
print(txt.format(a,b,c))
print("------------")

#Use index numbers {0}
a = 333 
b = 333 
c = 666 
txt = "The number of the beast is a sum of {2} with {0}  equal {1}"
print(txt.format(a,b,c))
print("------------")