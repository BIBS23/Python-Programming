f1 = open("sum","w")
sum = 0
print('enter numbers\n')
for i in range (5):
  num =  input()
  f1.write(num+' ')
f1.close()
f2 = open("sum","r")
for i in f2 :
  s = i.split()
  for j in s:
    sum = sum + int(j)
print('you sum is ',sum)
f2.close()

