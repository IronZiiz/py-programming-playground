def hyn():
    print("------------")
# Open a File on the Server
tz = open("/home/ziiz/Documents/Programming/learningPhython/FileHanding/first.txt","rt")
print(tz.read())
hyn()

# Read Only Parts of the File 
tz = open("/home/ziiz/Documents/Programming/learningPhython/FileHanding/first.txt","r")
print(tz.read(5)) # return five characters 
hyn()

# Read Lines
tz = open("/home/ziiz/Documents/Programming/learningPhython/FileHanding/first.txt","r")
print(tz.readline())
hyn()

tz = open("/home/ziiz/Documents/Programming/learningPhython/FileHanding/first.txt","r")
for x in tz:
    print(x)

hyn()

# Close Files
tz = open("/home/ziiz/Documents/Programming/learningPhython/FileHanding/first.txt","r")
print(tz.readline())
tz.close() # always close your files

hyn()
