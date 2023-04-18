class Person:
    def __init__(self,name,age,salary) :
        self.name = name
        self.age = age
        self.salary = salary
    def display(self):
        print('name of the person is \n',self.name)
        print('age of the person is \n',self.age)
        print('salary of the person is \n',self.salary)
n = input('enter the name of the person : ')
a = int(input('enter the age of the person  : '))
s = int(input('enter the salary of the person : '))
p = Person(n,a,s)
p.display()
        
