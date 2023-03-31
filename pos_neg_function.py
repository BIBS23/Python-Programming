def pos_neg(mylist):
  pos = []
  neg = []
  for i in mylist:
    if(i>0):
      pos.append(i) 
    if(i<0):
      neg.append(i)
  return pos,neg
    

mylist = []
n = int(input('Enter the size'))
for i in range(n):
  a = int(input())
  mylist.append(a)
pos , neg = pos_neg(mylist)
print('Positive numbers are : ',pos)
print('Negative numbers are : ',neg)
