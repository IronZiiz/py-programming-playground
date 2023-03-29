# function
    # things you do often

def line(): 
    print("-" *10)

line()
line()

# parameters 
def msg(txt): 
    line()
    print(txt)
    line()

msg("Zilli")

# more examples 

def sum(a,b): 
    sum = a +b
    line()
    print(sum)
    line()
    
n1 = 331
n2 = 335

sum(n1, n2)

# packaging 

def counter(*num):  
    print(num)

counter(6, 66, 66) 

# lists 
def double(lst): 
    pos = 0
    while pos<len(lst):
        lst[pos] *= 2
        pos +=1

values = [6, 66 ,666 ]
double(values) 
print(values)