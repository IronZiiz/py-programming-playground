def hyn():
    print("------------")

# Written with JavaScript Object notation 

# JSON in Python 
    #import module

import json

x = '{"name":"Thiago Zilli", "age":18, "city":"Curitiba"}'

y = json.loads(x)

print(y["name"])
hyn()

import json 
x = { 
    "name": "Thiago Zilli",
    "age": 18,
    "city": "Curitiba"
}

y = json.dumps(x)
print(y)
hyn()

# all the legal data types 

x = { 
    "name": "Thiago Zilli",
    "age": 18,
    "married":False, 
    "divorced":False, 
    "children": None,
    "pets": 4, 
    "cars": [
        {"Model": "Fiat uno"}
    ]

}
print(json.dumps(x))
hyn()

# Format the Result 
print(json.dumps(x, indent = 6))
print(json.dumps(x, indent = 6, separators = (".","=")))
hyn()

# Order the Result 
print(json.dumps(x, indent = 6, sort_keys=True))