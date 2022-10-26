# is a package manager for python packages 

# install pip
    # sudo apt-get install python3
    # sudo apt install python3-pip

# example with a package 
    # pip install camelcase 

import camelcase 

c = camelcase.CamelCase()
txt = "thiago zilli"
print(c.hump(txt))

# Remove package
    # uninstall packagename

# List packages
    # pip list