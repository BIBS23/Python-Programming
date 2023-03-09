a = int(input('enter no of numbers'))
ListA = ['bibin',2,4.0]
intList = []
floatList = []
stringList = []


for i in ListA:
    if(type(i) == float):
        floatList.append(i)
    if(type(i) == int):
        intList.append(i)
    else:
        stringList.append(i)

print('float values is : ',floatList)

print('float values is : ',intList)

print('float values is : ',stringList)
