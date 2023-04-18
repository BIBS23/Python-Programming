class Rectangle:

    def __init__(self,l,b):
        self.l = l
        self.b = b    
    def area(self):
        area = self.l * self.b;
        print(area)

l = int(input('enter the length : '))
b = int(input('enter the breadth : '))
r = Rectangle(l,b)
r.area()
