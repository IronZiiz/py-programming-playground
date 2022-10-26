def hyp():
 print("------------")

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# Syntax(lambda arguments : expression)

T = lambda x : x + 663
print(T(3))
hyp()

T = lambda x, y: x * y 
print(T(3,222))
hyp()

T = lambda x , y, z : x + y + z
print(T(220,222,224))
hyp()

# Use Lambda function as anonymos function inside another function 

def my_function(x): 
    return lambda y : y * x 

mydoubler = my_function(2)
print(mydoubler(333)) 
