# All string methods return new values. They do not change the original string.

#capitalize method
txt = "thiago"
txt = txt.capitalize() 
print(txt)
print("------------") #separete prints

#casefold()
txt = "Thiago"
txt = txt.casefold()
print(txt)
print("------------") #separete prints

#center
txt = "Thiago"
txt = txt.center(66)
print(txt)
print("------------") #separete prints

#count()
txt = "Thiago Thiago Thiago "
txt = txt.count("thiago")
print(txt)
print("------------") #separete prints

#endcode()
txt = "Thiago Zilli"
txt = txt.encode()
print(txt)
print("------------") #separete prints

#endswith()
txt = "Thiago"
txt = txt.endswith("Thiago")
print(txt)
print("------------") #separete prints

#expandtabs()
txt = "Thi\tag\to "
txt = txt.expandtabs(55)
print(txt)
print("------------") #separete prints

#find()
txt = "Thiago"
txt = txt.find("a")
print(txt)
print("------------") #separete prints

#format_map()
txt = "Thiago"
txt = txt.format_map("x")
print(txt)
print("------------") #separete prints


#index()
txt = "Thiago"
txt = txt.index("a")
print(txt)
print("------------") #separete prints

#isalnum()
num = "666" 
num = num.isalnum()
print(num)
print("------------") #separete prints

#isalpha()
txt = "aaaaa"
txt = txt.isalpha()
print(txt)
print("------------") #separete prints

#isdecimal()
flo ="666"
flo = flo.isdecimal()
print(flo)
print("------------") #separete prints

#isdigit()
txt = "6666666"
txt = txt.isdigit()
print(txt)
print("------------") #separete prints

#isidefier()
txt = "T_HIAgo"
txt = txt.isidentifier()
print(txt)
print("------------") #separete prints

#islower()
txt = "thiago"
txt = txt.islower()
print(txt)
print("------------") #separete prints

#isnumeric()
txt = "666"
txt = txt.isnumeric()
print(txt)
print("------------") #separete prints


#isprintable()
txt = "thiago\nzilli"
txt = txt.isprintable
print(txt)
print("------------") #separete prints


#isspace()
txt = " "
txt = txt.isspace()
print(txt)
print("------------") #separete prints

#istitle 
"""
    The istitle() method returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False.
    Symbols and numbers are ignored.
"""
txt = "This is a title"
txt = txt.istitle()
print(txt)
print("------------") #separete prints

#isupper()
txt  = "THIAGO ZILLI"
txt = txt.isupper()
print(txt)
print("------------") #separete prints

#join()
"""
   Join all items in a tuple into a string, using a hash character as separator
"""
txtTuple = ("Thiago", "Zilli")
x = "#".join(txtTuple)
print(x)
print("------------") #separete prints

#ljust()
txt = "Thiago"
x = txt.ljust(20, "X")
print(x,"Zilli") 
print("------------") #separete prints

#lower()
txt = "THIAGO ZILLI"
txt = txt.lower()
print(txt)
print("------------") #separete prints

#lstrip()
txt = "kakakaka Hello kakaka"
x = txt.lstrip("ka")
print(x)
print("------------") #separete prints



#Only a few methods are present here. There are many others