
def max_min(mylist):
  maxvalue = max(mylist)
  minvalue = min(mylist)
  return maxvalue,minvalue

mylist = [];
n = int(input('Enter the size'))
for i in range(n):
  a = input()
  mylist.append(a)
x,y = max_min(mylist)
print(x,y)
