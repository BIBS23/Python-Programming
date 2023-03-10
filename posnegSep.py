
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


f2 = open("num","r")

for i in f2:
  i = f2.readline()
  
  content = i.strip()
  
  
  
  if(int(content)>0):
    
    posList.append(int(content))
    
  else:
    
    negList.append(int(content))
    
print('positive numbers is :',posList)

print('negative numbers is :',negList)
f.close()
f2.close()
