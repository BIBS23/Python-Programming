aList = [];
n = int(input('Enter the length'))



print('enter the numbers')

for i in range (0,n):
    num = int(input())
    aList.append(num)
target = int(input('enter the target'))

if target in aList:
    print(aList.index(target))
else:
    print('not found')

