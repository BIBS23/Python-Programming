import math

a = int(input('enter the value of a'))
b= int(input('Enter the value of b'))
c= int(input('Enter the value of c'))

d= b*b-4*a*c

if(d==0):
    print('Both Roots are equal')
    print('Roots are : ',math.sqrt(b*b-4*a*c)/2*a)
elif(d>0):
    print('Root 1 is : ',(-b+math.sqrt(b*b-4*a*c))/(2*a))
    print('Root 2 is : ',(-b-math.sqrt(b*b-4*a*c))/(2*a))
else:
    print('Roots are imaginary')
