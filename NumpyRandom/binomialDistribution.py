def hyn():
    print("------------")
# Binomial distribution 
    # binary scenarios 
        # parameters 
            # n = trials 
            # p = probability 
            # size = shape 

from numpy import random 
import matplotlib.pyplot as plt 
import seaborn as sns 

x = random.binomial(n  = 100, p = 0.5, size =1000)
print(x)    
hyn()

y = random.normal(loc  = 50, scale = 5, size =1000)

sns.distplot(y, hist = False, label = 'Normal' )
sns.distplot(x, hist = False, label = 'Binomial')
plt.show()

hyn()