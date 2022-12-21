# visualize random distribution 
    # graphs 

import matplotlib.pyplot as plt 
import seaborn as sns 
from numpy import random

# plotting a distplot
arr = random.randint(100, size = 10)
sns.distplot(arr)
plt.show()

# without the histogram 
sns.distplot(arr, hist = False)
plt.show()