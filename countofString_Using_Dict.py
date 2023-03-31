mystring = input('Enter your String')
mydict = {}
for ch in mystring:
  if(ch not in mydict):
    mydict[ch] = mystring.count(ch)
print(mydict)
