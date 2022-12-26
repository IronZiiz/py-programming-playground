def hyn():
    print("------------")
# Poisson Distribution 
    # it estimates how many times as event can happen in a specified time 
    # parameters
        # lam : occurents 
        # size: form of  array  returned 

from numpy import random 
import matplotlib.pyplot as plt 
import seaborn as sns 


x = random.poisson(lam = 2, size =10)
print(x)

# Visualization of poisson distribution 
sns. distplot(x, kde = False )
plt.show()

# Difference between normal and poisson distribution 
    # Is discrete 

sns.distplot(random.normal(loc = 50, scale = 7, size = 1000), hist = False, label = 'normal')
sns.distplot(random.poisson(lam = 50, size = 1000), hist = False, label = 'poisson')

plt.show()

# Difference between poisson and binomial distribution 
    # poison : distribution is for continuos trials 
    # binomial : distribution is for discrete trials 

sns.distplot(random.binomial(n = 1000 , p = 0.01, size  = 1000), hist = False, label = 'binomial')
sns.distplot(random.poisson(lam = 10, size = 1000), hist = False, label = 'poisson ')

plt.show()