def hyn():
    print("------------")
# import module datetime 

import datetime
from sqlite3 import Date 

x = datetime.datetime.now()
print(x)
hyn()

# print year, month, day, hour, minute, second and microsecond

import datetime 
x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))
hyn()

# Creating Date objects
import datetime 

x = datetime.datetime(2022, 10, 13)
print(x)
hyn()

# strftime() method

import datetime 
x = datetime.datetime(6666,6,6)
print(x.strftime("%B"))

