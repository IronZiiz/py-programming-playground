def hyn():
    print("------------")
# format method

number = 666
txt = "The devil number is {} dollar"
print(txt.format(number))
hyn()

# add parameters

number = 666999333
txt = "The {:.2f} is a long number"
print(txt.format(number))
hyn()

# Multiple Values 
number1 = 333
number2 = 666
number3 = 999

mySequence = "My sequence is {:.1f}, {:.2f} and {:.3f}"
print(mySequence.format(number1,number2,number3))
hyn()

# Index number
number1 = 333
number2 = 666
number3 = 999

mySequence = "My sequence is {1}, {2} and {0:.3f}"
print(mySequence.format(number1,number2,number3))
hyn()

# Named Indexes 
mySequence = "My sequence is {number1}, {number2} and {number3}"
print(mySequence.format(number1="222",number2="444",number3="666"))
hyn()