num = []
l = int(input('Enter the length :-'))

print('Enter the values :-\n')

for i in range(l):
  w = int(input())
  num.append(w)

if(l%2==0):
    index1 = (l//2)
    index2 = ((l//2)+1)
    median = (num[index1]+num[index2])/2
    print('median is :\n'median)
else:
    
    index2 = (((l//2)+1))
    median = num[index2]
    print('Median is \n'median)
