 # Gaussian distribution 
    # parameters 
        # log (mean) 
        # scale (standard deviation ) eixo x
        # size 
import matplotlib.pyplot as plt 
import seaborn as sns 

from numpy import random 

x = random.normal(loc = 0, scale= 1 ,size = (1000))
sns.distplot(x) 

plt.show()
