a = int(input('Enter a number :'))
i = 0
sum = 0

print('reversed digit is :')
while (a>0):
    c = a%10
    a = a//10
    sum = sum+c
    print(c)
print('Sum of reversed is :',sum)
