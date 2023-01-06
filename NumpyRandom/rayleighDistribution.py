# parameters 
    # scale  - standard deviation 
    # size   - the shape of the returned array

from numpy import random 
import matplotlib.pyplot as plt 
import seaborn as sns 

x = random.rayleigh(scale = 2, size = (3, 3))
print(x)

sns.distplot(x, hist = False)
plt.show()

# with 2 degrees of freedom rayleigh and chi square represent the same distributions
