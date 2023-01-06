# verify the hypothesis 
    # parameters 
    # df - degree of freedom 
    # size - the shape of the returned array 

from numpy import random 
import matplotlib.pyplot as plt 
import seaborn as sns 

x = random.chisquare(df = 2, size = (3,3))
print(x)

sns.distplot(x,hist= False)
plt.show()