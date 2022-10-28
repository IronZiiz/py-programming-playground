def hyn():
    print("------------")
# write to an Existing File 

tz = open("/home/ziiz/Documents/Programming/learningPhython/FileHanding/first.txt","a") # 'a' append to the end of the file 
tz.write("This is the end! For you my friend... ")
tz.close()

tz = open("/home/ziiz/Documents/Programming/learningPhython/FileHanding/first.txt", "r")
print(tz.read())
hyn()

tz = open("/home/ziiz/Documents/Programming/learningPhython/FileHanding/first.txt","w") # 'w' method will overwrite the entire file 
tz.write("This is the end! For you my friend... ")
tz.close()

tz = open("/home/ziiz/Documents/Programming/learningPhython/FileHanding/first.txt", "r")
print(tz.read())
hyn()

# Create a New file 
    # use open() method and 'x' parameter 
#tz = open("/home/ziiz/Documents/Programming/learningPhython/FileHanding/NewFile.txt", "x")
tz = open("/home/ziiz/Documents/Programming/learningPhython/FileHanding/NewFile.txt", "w")
tz.write("This is my new file")
tz = open("/home/ziiz/Documents/Programming/learningPhython/FileHanding/NewFile.txt", "a")
tz.write(" This is the end for you my friend")
tz.close()

tz = open("/home/ziiz/Documents/Programming/learningPhython/FileHanding/NewFile.txt", "r")
print(tz.read())
hyn()