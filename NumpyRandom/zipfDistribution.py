# used to sample data based on zipf's law 
    #Zipf's Law: In a collection, the nth common term is 1/n times of the most common term. 

    # Parameters 
        # a = distribution parameter 
        # size = the shape of the returned array 

from numpy import random 
import matplotlib.pyplot as plt 
import seaborn as sns 

x = random.zipf(a = 2, size= 666)
print(x)
sns.distplot(x[x<6], kde =False ) # only x < 10 

plt.show()