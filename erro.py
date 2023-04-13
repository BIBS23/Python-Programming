class student:
    total =0
    def init (self,name,roll,totalmarks = 0):
        self.name = name
        self.totalmarks = totalmarks
        student.total+=1
        print(f'A new student{self,name} is added with roll no {self}')
        print(f'Total number of students is {student.total}')
        def getmarks(self,marks):
            
            for m in marks:
                self.totalmarks+=m
                self.avg = self,totalmarks/len(marks)
        def average(self):
            return self,avg
s1 = student('bibin',10,0)
s2 = student('maya',23)

s1.getmarks([23,25,24])
print(s1.totalmarks)

print(s1.average())
print(s1)
