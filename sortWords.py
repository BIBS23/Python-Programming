a = int(input('enter no of words'))
List_A = []

for i in range(a):
    print('word',i+1)
    w = input()
    List_A.append(w)
List_A.sort()

print(List_A)
