def hyn():
    print("------------")

# An iterator is an object that contains a countable number of values.
# Traverse through all the values.
# An interator is an object which imoplements the iterator protocol

# Iterator vc Iterable 
    ##Lists, tuples, dictionaries, and sets are all iterable objects 


tupleZilli = ("Thiago", "Zilli")
myit = iter(tupleZilli)

print(next(myit))
print(next(myit))
hyn()

myName = "Thiago Zilli"
myit = iter(myName)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
hyn()

# Looping Through an Iterator 
tupleZilli = ("Thiago", "Zilli")
for x in tupleZilli:
    print(x)
hyn()

myName = "Thiago Zilli"
for x in myName:
    print(x)
hyn()

#  Create  an Iterator 
class myNumbers:
    def __iter__(self):
        self.a = 666
        return self 
    
    def __next__(self):
        if self.a <= 800:
            x = self.a 
            self.a +=6
            return x 
        else:
            raise StopIteration

myclass = myNumbers()
myiter  = iter(myclass)

for x in myiter:
    print(x)
hyn()

