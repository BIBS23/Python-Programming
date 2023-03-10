ListA = []
intList = []
negList = []
l = int(input('enter length'))
for i in range(l):
    w = input()
    ListA.append(w)
for i in ListA:
    if(int(i)>0):
        intList.append(i)
    else:
        negList.append(i)
print('List  of positive integers is :',intList)
print('List  of negative integers is :',negList)
