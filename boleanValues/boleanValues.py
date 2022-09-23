#Two answers in Bolean Values:True or False

print(666 > 333)    #Return True
print(666 == 333)   #Return False
print(666 < 333)    #Return False
print("------------") #separete prints

#using if 
a = 666
b = 333

if b > a : 
    print("b is greater than a")
else: 
    print("b is not greater than a")

print("------------") #separete prints

#Evaluate Values and Variables 
    #using bool()function

print(bool("Thiago"))
print(bool("666"))
print("------------") #separete prints

x = "Thiago"
y = 666

print(bool(x))
print(bool(y))
print("------------") #separete prints

#Most Values are True 
    #except empty strings.
    #except 0
    #Any list, tuple, set, and dictionary are True, except empty ones.

bool("Thiago Zilli")
bool(666)
bool(["black", "blackI", "blackII"])

#Some Values are false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#An object that is made from a class with a __len__ function that returns 0 or False
class myClass():
    def __len__(self):
        return 0

myobj = myClass()
print(bool(myobj))
print("------------") #separete prints

#Functions can Return a Boolean
def zilliFunction(): 
    return True 

print(zilliFunction())
print("------------") #separete prints

def zilliFunction(): 
    return True 

if zilliFunction():
    print("Good Boy")
else: 
    print("Bad Boy")

print("------------") #separete prints

#Using the isistance() function for check if an object is an integer or not
x = 666 
print(isinstance(x, int)) #return boolean value 
