def hyn():
    print("------------")
# Is a sequence of characters that forms a search pattern
# check if a string contains the specified search pattern

# RegEx Module 

import re 
hyn()
texti = "The wyvern is not a dragon"
x = re.search("wyvern",texti)
print(x)
hyn()

# RegEx Functions 

# The findall() Function 
    # Functions returns a list containing all matches 
texti = "The wyvern is not a dragon"
x = re.findall("e",texti)
print(x)
hyn()

# The search() Function 
    # search the string and returns only first occurrence
texti = "The wyvern is not a dragon"
x = re.search("e",texti)
print(x)
hyn()

# The split() Function 
    # Return a list
texti = "The wyvern is not a dragon"
x = re.split("\s",texti)
print(x)
x = re.split("y\B",texti)
print(x)
hyn()

# The sub() Function 
    # replaces the matches with the text of your choice
texti = "The wyvern is not a dragon"
x = re.sub("\s","--",texti)
print(x)
x = re.sub("\s","--",texti,3)
print(x)
hyn()

# Match object
    # an object containing information about the search and the result
texti = "The wyvern is not a dragon"
x = re.search("is",texti)
print(x.span())

texti = "The wyvern 666 is not a dragon"
x = re.search("is",texti)
print(x.string)

x = re.search(r"\bT\w+",texti)
print(x.group())
