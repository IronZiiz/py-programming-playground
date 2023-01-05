# multinomial distrubution  
    # most results 

# Parameters 
    # n = number of possible outcomes
    # pvals = list of probabilities of outcomes
    # size = shape of the returned array 

#ex Dice roll

from numpy import random 
import matplotlib.pyplot  as plt 
import seaborn as sns

x = random.multinomial(n = 6 , pvals = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6 ])
print(x)

 
sns.distplot(x)
plt.show()