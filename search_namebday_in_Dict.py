name_birthday = {}
n = int(input('Enter the size of dictionary to add names and Birthdays:\n'))
for i in range(2):
  name = input('Enter name :')
  birthday = input('Enter birthday :')
  name_birthday['name'] = name 
  name_birthday['birthday'] = birthday
search = input('enter the name to search :\n')
if (search == name_birthday['name']):
  print(name_birthday)
