# Equal chances of occuring 
    #   low bound {default 0.0}
    #   high bound {default 1.0}
    # size  the shape of the returned array

from numpy import random 
import matplotlib.pyplot as plt 
import seaborn as sns 


x = random.uniform(low = 0.0, high = 100.0 , size=(3, 3)) # array 3 x 3 
print(x)

sns.distplot(x, hist = False )
plt.show()
