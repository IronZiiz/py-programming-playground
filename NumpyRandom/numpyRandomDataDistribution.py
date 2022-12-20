def hyn():
    print("------------")
# set of random numbers that follow a 
#certain probability density function 

    # probabiliy is set by a number between 0 and 1 

from numpy import random 

# Random distribution  
tz = random.choice([6, 123, 512, 1245], p =[0.6, 0.1, 0.1,0.2],size= (100))
print(tz) #size = quantity of number generate
hyn()

tz = random.choice([6, 123, 512, 1245], p =[0.6, 0.1, 0.1,0.2],size= (4,5))
print(tz) #size = quantity of number generate
hyn()