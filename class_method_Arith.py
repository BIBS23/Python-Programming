class Arith:

    def add(self):
        print('sum',self.a+self.b)
    def read(self):
        self.a = int(input('enter any two number1 :\n'))
        self.b = int(input('enter any two number2 :\n'))
A = Arith()
A.read()
A.add()
        
