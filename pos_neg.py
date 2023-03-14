
posList = []
negList = []

l = int(input('enter the length'))

f = open("num","w")

for i in range(l):
  
  i=i+1
  
  print('enter value',i)
  
  numbers = input()
  
  f.write(numbers+"\n")
  
print('file created')
f.close()

f2 = open("num","r")

for i in f2:
  
  i = i.strip()
  number=int(i)
   
  if(number>0):
    
    posList.append(number)
    
  else:
    
    negList.append(number)
    
print('positive numbers is :',posList)

print('negative numbers is :',negList)

f2.close()
