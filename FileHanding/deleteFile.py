# necessary import OS module 

import os 
tz = open("/home/ziiz/Documents/Programming/learningPhython/FileHanding/NewFile1.txt", "w")
os.remove("/home/ziiz/Documents/Programming/learningPhython/FileHanding/NewFile1.txt")


# Check if File exist

if os.path.exists("/home/ziiz/Documents/Programming/learningPhython/FileHanding/NewFile1.txt"):
    os.remove("/home/ziiz/Documents/Programming/learningPhython/FileHanding/NewFile1.txt")
else: 
    print("The file does not exist")

# Create and Delete folder
os.rmdir("/home/ziiz/Documents/Programming/learningPhython/NewFolder")

if os.path.exists("/home/ziiz/Documents/Programming/learningPhython/NewFolder"):
    os.remove("/home/ziiz/Documents/Programming/learningPhython/FileHanding/NewFile1.txt")
else: 
    print("The folder does not exist")