info = {}
info['name'] = 'bibin'
info['branch'] = 'cse'
info['branch'] = 'ece' # it will update the branch
info.pop('name') # it will pop the name
info['name'] = 'sandy' # name will be added 
print(info) 
for i in info:
    print(i,info[i]) # it will print the whole key and value
    
    
 # to print the dictionary as a list
grades = {90:'A',80:"B",70:"C"}
print(list(grades.items()))

# to print as a tuple

for (key,value) in grades.items():
    print(key,value)
    
   
thekeys = list(info.keys()) # it will print the keys
thekeys.sort() # it will sort the keys
print(thekeys)
