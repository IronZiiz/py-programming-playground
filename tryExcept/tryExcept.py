from xml.dom import XMLNS_NAMESPACE


def hyn():
    print("------------")
# use when your test result in error 

# Exception Handing 
    # Generate an error message
try: 
    print(x)
except:
    print("x is not defined")
hyn()
# Many Exceptions 
try: 
    x = 1/0
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong") #Return this

try: 
    print(T)
except NameError:
    print("Variable T is not defined") #Return this
except:
    print("Something else went wrong")
hyn()

# Else 
    # print message when no errors
try: 
    print("Thiago Zilli")
except:
    print("Something went wrong")
else: 
    print("Nothin went wrong")
hyn()

# Finally
    # Will be excuted regardless if the try block raises an error or not 
try: 
    print(T)
except: 
    print("Something went wrong")
finally:
    print("Nobody cares. I'm excecuted ")

hyn()

try: 
    f = open("/home/ziiz/Documents/Programming/learningPhython/tryExcept/tryExceptText.txt")
    try: 
        f.write("Thiago")
    except:
        print("Something went wrong when  writing to the file")
    finally: 
        f.close()
except:
    print("Something went wrong when opening the file")
hyn()

