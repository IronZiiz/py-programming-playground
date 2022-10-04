z = 660  #define indexing 
while z < 666: 
    print(z)
    z+=1 #counter
print("------------")

# The 'break' statement
    #Stop the loop 
z = 660 
while z < 666:
    print(z)
    if z == 663:
        break 
    z += 1 
print("------------")


# The 'continue' statement
z = 660 
while z < 666:
    z += 1 
    if z == 663:
        continue
    print(z)
print("------------")

# The 'else' statement
z = 660 
while z < 666:
    print(z)
    z += 1 
else: 
    print("z is no longer less than 6")
print("------------")