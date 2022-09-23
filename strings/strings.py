#string literal with print()
print("------------") #separete prints
print("Devil")
print('Devil')
print("------------") #separete prints

#Assign String to a Variable 
a = "Thiago Zilli"
print(a)
print("------------") #separete prints

#Multiline Strings 

a = """AAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAA
"""
print(a)
print("------------") 

    #or 

b = '''BBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBB
'''
print(b)
print("------------") 

#Strings are Arrays
    #n Python are arrays of bytes representing unicode characters.
a = "Thiago Zilli"
print(a[1])
print("------------") 

#Looping through a String 
for x in "Thiago Zilli": #write Thiago Zilli 
    print(x)
print("------------") 

#String Length
a = "Thiago Zilli"
print(len(a)) #show me the legth of a string
print("------------") 

#Check String 
txt = "Thiago Zilli is a good boy"
print("boy" in txt) #To check if a certain phrase or character is present in a string,
print("------------") 

    #use it in an if

txt = "Thiago Zilli is a good boy"
if "boy" in txt: 
    print("YES, 'boy' is present")
print("------------") 

#Check if NOT
txt = "Thiago Zilli is a good boy"
print("boy" not in txt)
print("------------") 
    #use it in an if 

txt = "Thiago Zilli is a good boy"
if "boy" not in txt: 
    print("No, 'boy' is NOT present")
print("------------") 








