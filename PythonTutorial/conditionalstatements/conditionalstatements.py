# if 
T = 666
Z = 333

if T > Z: 
    print("T is greater than Z") #Must have identation
print("------------")

# elif (if the previous conditions were not true, then try this condition").

T = 666
Z = 333

if Z > T: 
    print("Z is greater than T")
elif T > Z: 
    print("T is greater than Z")
print("------------")


# else 
T = 666
Z = 333

if Z > T: 
    print("Z is greater than T")

else: 
    print("Z is equal T or smaller than T.")

print("------------")

# Ternary Operators, or conditional Expressions 
# Short hand if 
T = 666
Z = 333

if T > Z: print("T is greater than Z")
print("------------")

# Short hand if...Else 
T = 666
Z = 333

print("T") if T > Z else print("Z")
print("------------")

# Logical operator 'and' with conditional statementes

T = 666
Z = 333

if T > Z and (T/Z) == 2:
    print("Both conditions are True")
print("------------")

# Logical operator "or" with conditional statements
T = 666
Z = 333

if T > Z or T == Z:
    print("At least one of the conditions is True")
print("------------")

# Nested if 

T = 666

if T > 333: 
    print("Above 333")
    if T > 666: 
        print("Ando also above 666")
    else: 
        print("But not above 666")
print("------------")

# 'pass' statement for 'if' statement with no content
T = 666

if T > 666:
    pass #avoid getting an error