# used to describe the time to occurence a next event
    # Poisson distribution deals with number of occurences of an event in a time period whereas exponential distribution deals with the time between these events.

from numpy import random 
import matplotlib.pyplot as plt 
import seaborn as sns 

sns.distplot(random.exponential(size = 666), hist = False)
plt.show()