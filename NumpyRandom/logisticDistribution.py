# Important to machine learning in logistc regression 
    # parameters 
    # loc = where the peake is 
    # scale = standard deviation 
    # size = array returned 

from numpy import random 
import matplotlib.pyplot  as plt 
import seaborn as sns 

x = random.logistic(loc = 1, scale = 2, size= (3,3))
print(x)

sns.distplot(x, hist = False)
plt.show()

# Difference Between logistic and normal distribution 
    # Logistis is more possibility of occurence of an event 
    # further away from mean 

sns.distplot(random.normal(scale = 2, size = 1000), hist = False, label ='normal')
sns.distplot(random.logistic(size = 1000), hist = False, label ='logistic')
plt.show()