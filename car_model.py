class Car :
    def __init__(self,model,year,price):
        self.model = model
        self.year = year
        self.price = price
    def cost(self):
        print('price is : ',self.price)
        print('model : \n',self.model,'\n','year :\n',self.year)
m = input('enter the model ')
y = int(input('ener the year : '))
p = int(input('ener the price : '))
c1 = Car(m,y,p)
c2 = Car(m,y,p)
c1.cost()
c2.cost()
        
        
