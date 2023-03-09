a = int(input('enter no of words'))
ListA = []
ListB = []

for i in range(0,a):
    w = input()
    ListA.append(w)
for j in ListA:
    if(j not in ListB):
        ListB.append(j)
print(ListB)
